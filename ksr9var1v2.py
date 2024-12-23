import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

g = 9.8

root = Tk()  # создание окна
root.title("Задача 9. Вариант 1. Вершинина ПМоП2")
root.iconbitmap(default="лиса.ico")  # добавление иконки)))
root.geometry("1920x1080")  # задание размера окна

# ------------------------------------------------оформление первого и второго фрейма-------------------------------------------------
# создаем набор вкладок
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
# создаем фреймы
frame1 = tk.Frame(notebook, bg="white")
frame2 = tk.Frame(notebook, bg="white")
frame3 = tk.Frame(notebook, bg="white")
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)

# добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Формулировка задачи")
notebook.add(frame2, text="Формулы численных методов")
notebook.add(frame3, text="Результаты")

image_path_1 = "frame1.jpg"
image_1 = Image.open(image_path_1)
image_1 = image_1.resize((1142, 750))
photo_1 = ImageTk.PhotoImage(image_1)

#фото frame1
label_image_1 = tk.Label(frame1, image=photo_1)
label_image_1.place(x=0, y=0)

image_path_2 = "frame2.png"
image_2 = Image.open(image_path_2)
image_2 = image_2.resize((1117, 790))
photo_2 = ImageTk.PhotoImage(image_2)

#фото frame2
label_image_2 = tk.Label(frame2, image=photo_2)
label_image_2.place(x=0, y=0)
# ------------------------------------------------оформление первого и второго фрейма-------------------------------------------------
# ------------------------------------------------Численные методы-------------------------------------------------
def mainFunction(x,v,sigma,alpha):
    alpha_in_radians = np.deg2rad(alpha)
    TG = (np.tan(alpha_in_radians / 2)) ** 2
    numerator=-0.6*np.sqrt(2*g)*sigma
    denominator=TG*np.pi*v**(3/2) if v>0 else 0
    U=numerator/denominator
    return U

def istResh(x, v0, sigma, alpha):
    U_0 = v0 ** (5 / 2)
    alpha_in_radians = np.deg2rad(alpha)
    TG = (np.tan(alpha_in_radians / 2)) ** 2
    numerator = -1.5 * np.sqrt(2 * g) * sigma * x
    denominator = TG * np.pi
    U = ((numerator / denominator) + U_0) ** (2 / 5) if ((numerator / denominator) + U_0)>0 else 0
    return U

def bigAndHalfStepForRK4(x,v,h,sigma,alpha):
    k1=mainFunction(x,v,sigma,alpha)
    k2=mainFunction(x+h/2,v+h/2*k1,sigma,alpha)
    k3=mainFunction(x+h/2,v+h/2*k2,sigma,alpha)
    k4=mainFunction(x+h,v+h*k3,sigma,alpha)
    v=v+h/6*(k1+2.0*k2+2.0*k3+k4)
    return v

def methodRK4WithLocalErrorControl(S,epsilon,h):
    if abs(S)<(epsilon/32):
        return 2
    if abs(S)>epsilon:
        return 0
    if (abs(S)>=(epsilon/32)) and (abs(S)<=epsilon):
        return 1

# ------------------------------------------------Численные методы-------------------------------------------------
# ------------------------------------------------Ввод данных-------------------------------------------------

# Значения по умолчанию для каждого параметра
default_values = {
    "sigma": 0.1,
    "alpha": 15,
    "x0": 0,
    "v0": 2,
    "h": 0.1,
    "epsilon": 0.00000000001,
    "maxN":10000,
    "controlExit":0.001
}

label_sigma = tk.Label(frame3, text="Площадь отверстия sigma:", font=("Times New Roman", 10), bg="white")
entry_sigma = tk.Entry(frame3, font=("Times New Roman", 10))
entry_sigma.insert(0, str(default_values["sigma"]))  
label_sigma.grid(row=0, column=0, sticky="w", padx=5, pady=0)
entry_sigma.grid(row=0, column=1, padx=5, pady=0)

label_alpha = tk.Label(frame3, text="Угол раствора alpha:", font=("Times New Roman", 10), bg="white")
entry_alpha = tk.Entry(frame3, font=("Times New Roman", 10))
entry_alpha.insert(0, str(default_values["alpha"])) 
label_alpha.grid(row=1, column=0, sticky="w", padx=5, pady=0)
entry_alpha.grid(row=1, column=1, padx=5, pady=0)

label_x0 = tk.Label(frame3, text="Начальное время x0:", font=("Times New Roman", 10), bg="white")
entry_x0 = tk.Entry(frame3, font=("Times New Roman", 10))
entry_x0.insert(0, str(default_values["x0"])) 
label_x0.grid(row=2, column=0, sticky="w", padx=5, pady=0)
entry_x0.grid(row=2, column=1, padx=5, pady=0)

label_v0 = tk.Label(frame3, text="Начальная высота столба жидкости v0:", font=("Times New Roman", 10), bg="white")
entry_v0 = tk.Entry(frame3, font=("Times New Roman", 10))
entry_v0.insert(0, str(default_values["v0"]))  
label_v0.grid(row=3, column=0, sticky="w", padx=5, pady=0)
entry_v0.grid(row=3, column=1, padx=5, pady=0)

label_h = tk.Label(frame3, text="Начальный шаг h:", font=("Times New Roman", 10), bg="white")
entry_h = tk.Entry(frame3, font=("Times New Roman", 10))
entry_h.insert(0, str(default_values["h"])) 
label_h.grid(row=4, column=0, sticky="w", padx=5, pady=0)
entry_h.grid(row=4, column=1, padx=5, pady=0)

label_epsilon = tk.Label(frame3, text="Параметр контроля локальной погрешности epsilon:", font=("Times New Roman", 10), bg="white")
entry_epsilon = tk.Entry(frame3, font=("Times New Roman", 10))
entry_epsilon.insert(0, str(default_values["epsilon"]))  
label_epsilon.grid(row=5, column=0, sticky="w", padx=5, pady=0)
entry_epsilon.grid(row=5, column=1, padx=5, pady=0)

label_N = tk.Label(frame3, text="Максимальное количество шагов", font=("Times New Roman", 10), bg="white")
entry_N = tk.Entry(frame3, font=("Times New Roman", 10))
entry_N.insert(0, str(default_values["maxN"]))  
label_N.grid(row=6, column=0, sticky="w", padx=5, pady=0)
entry_N.grid(row=6, column=1, padx=5, pady=0)

label_controlExit = tk.Label(frame3, text="Контроль выхода за нижнюю границу по v", font=("Times New Roman", 10), bg="white")
entry_controlExit = tk.Entry(frame3, font=("Times New Roman", 10))
entry_controlExit.insert(0, str(default_values["controlExit"]))  
label_controlExit.grid(row=7, column=0, sticky="w", padx=5, pady=0)
entry_controlExit.grid(row=7, column=1, padx=5, pady=0)
# ------------------------------------------------Ввод данных-------------------------------------------------
# ------------------------------------------------Таблица-------------------------------------------------
# Создаем вертикальную полосу прокрутки
y_scrollbar = tk.Scrollbar(frame3, orient="vertical")

# Создаем таблицу Treeview
treeview = ttk.Treeview(frame3, columns=("i", "xi", "vi", "v2i", "hi", "|v2i-vi|", "c1", "c2", "ui", "Ei"), show="headings", yscrollcommand=y_scrollbar.set)

# Настройка заголовков
treeview.heading("i", text="i")
treeview.heading("xi", text="xi")
treeview.heading("vi", text="vi")
treeview.heading("v2i", text="v2i")
treeview.heading("hi", text="hi")
treeview.heading("|v2i-vi|", text="|v2i-vi|")
treeview.heading("c1", text="c1")
treeview.heading("c2", text="c2")
treeview.heading("ui", text="ui")
treeview.heading("Ei", text="Ei")

# Определяем ширину столбцов
treeview.column("i", width=50)
treeview.column("xi", width=100)
treeview.column("vi", width=150)
treeview.column("v2i", width=150)
treeview.column("hi", width=100)
treeview.column("|v2i-vi|", width=150)
treeview.column("c1", width=20)
treeview.column("c2", width=20)
treeview.column("ui", width=150)
treeview.column("Ei", width=150)

# Размещение таблицы 
treeview.grid(row=0, column=2, columnspan=9, rowspan=8, padx=5, pady=5)  

# Размещение вертикальной полосы прокрутки
y_scrollbar.grid(row=0, column=11, rowspan=8, sticky="ns")  # Прокрутка в 8-й колонке
y_scrollbar.config(command=treeview.yview)

treeview.configure(yscrollcommand=y_scrollbar.set)
# ------------------------------------------------Таблица-------------------------------------------------
# ------------------------------------------------Построение графика-------------------------------------------------
def plot_graph(xi_values, vi_values, ui_values):
    # Создаем фигуру и оси для графика
    fig, ax = plt.subplots(figsize=(10, 5))

    # Строим график зависимости vi от xi с синими точками (численное решение)
    ax.plot(xi_values, vi_values, label="vi(xi) - численное решение", color="b", marker="o", markersize=2)
    # Строим красную траекторию зависимости ui от xi (аналитическое решение)
    ax.plot(xi_values, ui_values, label="ui(xi) - аналитическое решение", color="r", linestyle='-', linewidth=2)

    # Настройки графика
    ax.set_title("График зависимости vi и ui от xi", fontsize=14)
    ax.set_xlabel("xi", fontsize=12)
    ax.set_ylabel("vi / ui", fontsize=12)
    ax.grid(True)
    ax.legend()

    # Удаляем предыдущий график, если он существует
    if hasattr(plot_graph, "canvas"):
        plot_graph.canvas.get_tk_widget().destroy()

    # Создаём новый canvas для нового графика
    plot_graph.canvas = FigureCanvasTkAgg(fig, frame_graph)
    plot_graph.canvas.draw()

    # Обновляем расположение графика
    plot_graph.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

# Размещение фрейма для графика с использованием grid
frame_graph = tk.Frame(frame3, bg="white")
frame_graph.grid(row=9, column=0, columnspan=8, rowspan=9, padx=0, pady=0, sticky="nsew")

frame3.grid_rowconfigure(9, weight=1)  # Даем вес 1 для строки с графиком
frame3.grid_columnconfigure(0, weight=1)  # Даем вес 1 для первой колонки
frame3.grid_columnconfigure(1, weight=1)  # Даем вес 1 для второй колонки
frame3.grid_columnconfigure(2, weight=2)  # Даем вес 2 для колонок с таблицей (чтобы они были шире)

# ------------------------------------------------Построение графика-------------------------------------------------
# ------------------------------------------------Заполнение таблицы-------------------------------------------------

# ------------------------------------------------Справка-------------------------------------------------
def update_labels(c1_max, c2_max, h_max, h_min, max_OLP, max_x, max_E, h_max_index, h_min_index, v_v22_max_index, E_max_index):
    # Обновляем значения в лейблах справа от таблицы
    label_c1_value.config(text=f"{c1_max}")
    label_c2_value.config(text=f"{c2_max}")
    label_h_max_value.config(text=f"{h_max:.5f}")
    label_h_min_value.config(text=f"{h_min:.16f}")
    label_max_OLP_value.config(text=f"{max_OLP:.5e}")
    label_max_x_value.config(text=f"{max_x:.5f}")
    label_max_E_value.config(text=f"{max_E:.6f}")
    # Вывод шага
    label_h_max_stepZN.config(text=f"{h_max_index}")
    label_h_min_stepZN.config(text=f"{h_min_index}")
    label_max_OLP_stepZN.config(text=f"{v_v22_max_index}")
    label_max_E_stepZN.config(text=f"{E_max_index}")
    


# Лейблы для отображения чисел делений, удвоений, максимального и минимального шага и т.д.
label_c1 = tk.Label(frame3, text="Число делений шага:", font=("Times New Roman", 12), bg="white")
label_c1.grid(column=9, row=10, sticky="w", padx=0, pady=1)
label_c1_value = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_c1_value.grid(column=10, row=10, sticky="w", padx=0, pady=1)

label_c2 = tk.Label(frame3, text="Число удвоений шага:", font=("Times New Roman", 12), bg="white")
label_c2.grid(column=9, row=11, sticky="w", padx=0, pady=1)
label_c2_value = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_c2_value.grid(column=10, row=11, sticky="w", padx=0, pady=1)

label_h_max = tk.Label(frame3, text="Максимальный шаг:", font=("Times New Roman", 12), bg="white")
label_h_max.grid(column=9, row=12, sticky="w", padx=0, pady=1)
label_h_max_value = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_h_max_value.grid(column=10, row=12, sticky="w", padx=0, pady=1)

label_h_max_step = tk.Label(frame3, text="i=", font=("Times New Roman", 12), bg="white")
label_h_max_step.grid(column=11, row=12, sticky="w", padx=0, pady=1)
label_h_max_stepZN = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_h_max_stepZN.grid(column=12, row=12, sticky="w", padx=0, pady=1)

label_h_min = tk.Label(frame3, text="Минимальный шаг:", font=("Times New Roman", 12), bg="white")
label_h_min.grid(column=9, row=13, sticky="w", padx=0, pady=1)
label_h_min_value = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_h_min_value.grid(column=10, row=13, sticky="w", padx=0, pady=1)

label_h_min_step = tk.Label(frame3, text="i=", font=("Times New Roman", 12), bg="white")
label_h_min_step.grid(column=11, row=13, sticky="w", padx=0, pady=1)
label_h_min_stepZN = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_h_min_stepZN.grid(column=12, row=13, sticky="w", padx=0, pady=1)

label_max_OLP = tk.Label(frame3, text="Максимальный |v-v2i| :", font=("Times New Roman", 12), bg="white")
label_max_OLP.grid(column=9, row=14, sticky="w", padx=0, pady=1)
label_max_OLP_value = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_max_OLP_value.grid(column=10, row=14, sticky="w", padx=0, pady=1)

label_max_OLP_step = tk.Label(frame3, text="i=", font=("Times New Roman", 12), bg="white")
label_max_OLP_step.grid(column=11, row=14, sticky="w", padx=0, pady=1)
label_max_OLP_stepZN = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_max_OLP_stepZN.grid(column=12, row=14, sticky="w", padx=0, pady=1)

label_max_E = tk.Label(frame3, text="Максимальная глобальная погрешность:", font=("Times New Roman", 12), bg="white")
label_max_E.grid(column=9, row=15, sticky="w", padx=0, pady=1)
label_max_E_value = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_max_E_value.grid(column=10, row=15, sticky="w", padx=0, pady=1)

label_max_E_step = tk.Label(frame3, text="i=", font=("Times New Roman", 12), bg="white")
label_max_E_step.grid(column=11, row=15, sticky="w", padx=0, pady=1)
label_max_E_stepZN = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_max_E_stepZN.grid(column=12, row=15, sticky="w", padx=0, pady=1)

label_max_x = tk.Label(frame3, text="Время вытекания жидкости:", font=("Times New Roman", 12), bg="white")
label_max_x.grid(column=9, row=16, sticky="w", padx=0, pady=1)
label_max_x_value = tk.Label(frame3, text="0", font=("Times New Roman", 12), bg="white", fg="blue")
label_max_x_value.grid(column=10, row=16, sticky="w", padx=0, pady=1)

def calculate():
    try:
        # Очищаем таблицу
        for item in treeview.get_children():
            treeview.delete(item)

        plt.clf()  # Очистить график
        plot_graph.xi_values = []
        plot_graph.vi_values = []
        plot_graph.ui_values = []

        # Считываем новые значения из полей ввода
        sigma = float(entry_sigma.get())
        alpha = float(entry_alpha.get())
        x0 = float(entry_x0.get())
        v0 = float(entry_v0.get())
        h = float(entry_h.get())
        epsilon = float(entry_epsilon.get())
        maxN = int(entry_N.get())
        controlExit = float(entry_controlExit.get())

        # Начальные условия
        u0 = v0  # Начальное значение для u0
        v = v0
        x = x0
        c1 = 0  # Число делений шага
        c2 = 0  # Число удвоений шага

        # Создаем списки для хранения данных
        i_values = []
        xi_values = []
        vi_values = []
        v2_values = []
        h_values = []
        v_v22_values = []
        c1_values = []
        c2_values = []
        ui_values = []
        E_values = []

        for i in range(maxN + 1):
            # Расчет нового значения для v с использованием метода Рунге-Кутты
            V = bigAndHalfStepForRK4(x, v, h, sigma, alpha)
            v12 = bigAndHalfStepForRK4(x, v, h / 2, sigma, alpha)
            v22 = bigAndHalfStepForRK4(x + h / 2, v12, h / 2, sigma, alpha)
            S = abs(V - v22) / 15
            control = methodRK4WithLocalErrorControl(S, epsilon, h)

            if control == 0:  # Делим шаг
                while control == 0:
                    h = h / 2
                    v12 = bigAndHalfStepForRK4(x, v, h / 2, sigma, alpha)
                    v22 = bigAndHalfStepForRK4(x + h / 2, v12, h / 2, sigma, alpha)
                    V = bigAndHalfStepForRK4(x, v, h, sigma, alpha)
                    S = abs(V - v22) / 15
                    control = methodRK4WithLocalErrorControl(S, epsilon, h)
                    c1 += 1  # Увеличиваем счетчик деления шага
            elif control == 2:  # Удваиваем шаг
                h = 2.0 * h
                v = V
                x += h
                c2 += 1  # Увеличиваем счетчик удвоения шага
            else:  # Не меняем шаг
                v = V
                x += h

            # Вычисляем аналитическое решение
            u = istResh(x, u0, sigma, alpha)
            E = abs(u - v)

            # Добавляем данные в таблицу
            treeview.insert("", "end", values=(
                f"{i}",
                f"{x:.10f}",
                f"{v:.16f}",
                f"{v22:.16f}",
                f"{h:.16f}",
                f"{S:.20f}",
                f"{c1}",
                f"{c2}",
                f"{u:.20f}",
                f"{E:.20f}"
            ))

            # Сохраняем данные в списки
            i_values.append(i)
            xi_values.append(x)
            vi_values.append(v)
            v2_values.append(v22)
            h_values.append(h)
            v_v22_values.append(S)
            c1_values.append(c1)
            c2_values.append(c2)
            ui_values.append(u)
            E_values.append(E)

            # Выход из цикла, если выполнено условие
            if (v <= controlExit) or (i >= maxN) or (v < 0) or (v22 < 0):
                break

        # Индексы для максимальных/минимальных значений
        h_max_index = h_values.index(max(h_values))
        h_min_index = h_values.index(min(h_values))
        v_v22_max_index = v_v22_values.index(max(v_v22_values))
        E_max_index = E_values.index(max(E_values))

        # Строим график
        plot_graph(xi_values, vi_values, ui_values)

        # Обновляем лейблы
        update_labels(
            max(c1_values), max(c2_values), max(h_values), min(h_values),
            max(v_v22_values), max(xi_values), max(E_values),
            h_max_index, h_min_index, v_v22_max_index, E_max_index
        )

    except ValueError:
        print("Ошибка: Пожалуйста, убедитесь, что все поля заполнены корректно.")
# ------------------------------------------------Заполнение таблицы-------------------------------------------------
# ------------------------------------------------Кнопка-------------------------------------------------
# кнопка для запуска вычислений
button_calculate = tk.Button(frame3, text="Начать расчёт", font=("Times New Roman", 10), command=calculate)
button_calculate.grid(row=8, column=3, columnspan=1, pady=10)
# ------------------------------------------------Кнопка-------------------------------------------------


root.mainloop()