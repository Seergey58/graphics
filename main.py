import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np
import math as m
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

# scoplenie = pyfits.open("C:/v523cas60s-001.fit")
# zvezdochka = scoplenie[0].data

def ok1():
    x_0 = int(txt.get())
    R = int(txt2.get())
    y_0 = int(txt1.get())
    scoplenie = pyfits.open("C:/v523cas60s-001.fit")
    zvezdochka = scoplenie[0].data
    Y_axes = zvezdochka[y_0][(x_0 - R):(x_0 + R)]
    print(Y_axes)
    X_axes = []
    for i in range((x_0 - R), (x_0 + R)):
        X_axes.append(i)
    print(X_axes)
    fig = plt.figure()
    # graphic = plt.figure() # создали область Figure
    lor = fig.add_subplot(111)  # добавили к Figure область Axes. 111 - это первая строка, первый столбец и первая # (единственная) ячейка на сетке Figure.
    lor.set_title("Звездочка горизонтальная ")
    lor.set_xlabel("координата")
    lor.set_ylabel("Возмоожно это светимомсть")
    lor.plot(X_axes, Y_axes, color="yellow")

    plt.show()

def ok2():
    x_0 = int(txt.get())
    R = int(txt2.get())
    y_0 = int(txt1.get())
    scoplenie = pyfits.open("C:/v523cas60s-001.fit")
    zvezdochka = scoplenie[0].data
    zvezdochka = np.transpose(zvezdochka)
    Y1_axes = zvezdochka[x_0][(y_0 - R):(y_0 + R)]
    X1_axes = []
    for j in range((y_0 - R),(y_0 + R)):
        X1_axes.append(j)
    print(X1_axes)
    scoplenie.close()
    fig1 = plt.figure()
    graph = plt.Figure()
    rol = fig1.add_subplot(111)

    rol.set_title("Звездочка вертикальная")
    rol.set_xlabel("координата")
    rol.set_ylabel("Допустим светимость")
    rol.plot(X1_axes, Y1_axes, color = "red")

    plt.show()

    plt.show()


# def ok3(vert, color='Red'):
#     scoplenie = pyfits.open("C:/v523cas60s-001.fit")
#     zvezdochka = scoplenie[0].data
#
#     x_0 = int(txt.get())
#     R = int(txt2.get())
#     y_0 = int(txt1.get())
#
#     vert = []
#     for i in range(-R, R):
#         for l in range(-R, R):
#             vert.append([x_0 + i, y_0 + l, zvezdochka[x_0 + l][y_0 + i]])
#     plot_3D(vert, color="BuGn")
#
#     #global x_0, y_0, R
#     fig2 = plt.figure()
#     D = fig2.add_subplot(111, projection='3d')
#     x = [S[0] for S in vert]
#     y = [S[1] for S in vert]
#     z = [S[2] for S in vert]
#     D.plot_trisurf(x, y, z)
#     plt.show()

    # vert = []
    # for i in range(-R, R):
    #     for l in range(-R, R):
    #         vert.append([x_0 + i, y_0 + l, zvezdochka[x_0 + l][y_0 + i]])
    # plot_3D(vert, color="BuGn")


# x_0 = 385
# y_0 = 357
# R = 20
# R_vn = 15
# R_zv = 5




# lor.plot(X_axes, Y_axes, color = "yellow")
#
# plt.show()

# zvezdochka = np.transpose(zvezdochka)
# Y1_axes = zvezdochka[x_0][(y_0 - R):(y_0 + R)]
# X1_axes = []
# for j in range((y_0 - R),(y_0 + R)):
#     X1_axes.append(j)
# print(X1_axes)
# scoplenie.close()
# fig1 = plt.figure()
# graph = plt.Figure()
# rol = fig1.add_subplot(111)
#
# rol.set_title("Звездочка вертикальная")
# rol.set_xlabel("координата")
# rol.set_ylabel("Допустим светимость")
# rol.plot(X1_axes, Y1_axes, color = "red")
#
# plt.show()
#

def ok4():
    x_0 = int(txt.get())
    R = int(txt2.get())
    y_0 = int(txt1.get())
    R_vn = int(txt3.get())
    R_zv = int(txt4.get())
    scoplenie = pyfits.open("C:/v523cas60s-001.fit")
    zvezdochka = scoplenie[0].data
    exp = scoplenie[0].header['EXPTIME']
    sum_f = 0
    edin_f = 0
    for j in range(-R_vn, R_vn):
            for l in range (-R_vn, R_vn):
                if m.sqrt(l**2+j**2)>=R_vn and m.sqrt(l**2+j**2)<=R:
                    edin_f += 1
                    sum_f += zvezdochka[x_0+l][y_0+j]
    sr_fona = sum_f/edin_f
    # print(sr_fona)

    edin_zv = 0
    sum_zv = 0
    for k in range(-R_zv, R_zv):
        for i in range(-R_zv, R_zv):
            if  m.sqrt(i**2+k**2)<=R_zv: # расстояние пикселя от центра:
                edin_zv += 1
                sum_zv += zvezdochka[x_0 + i][y_0 + k]

    # print(sum_zv)
    sum_zvezda_istinnoe = (sum_zv - edin_zv*sr_fona)/exp


    print(sum_zvezda_istinnoe)

window = Tk()
window.title("Выбери свою звезду")
window.geometry("1000x600")

lbl = Label(window, text = "Центр по x", font=("Times New Roman", 15))
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

lbl1 = Label(window, text = "Центр по у", font=("Times New Roman", 15))
lbl1.grid(column=0, row=1)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=1)

lbl2 = Label(window, text = "Размер графика", font=("Times New Roman", 15))
lbl2.grid(column=0, row=2)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=2)

lbl3 = Label(window, text = "Радиус внешний", font=("Times New Roman", 15))
lbl3.grid(column=0, row=3)
txt3 = Entry(window,width=10)
txt3.grid(column=1, row=3)

lbl4 = Label(window, text = "Радиус внутренний", font=("Times New Roman", 15))
lbl4.grid(column=0, row=4)
txt4 = Entry(window,width=10)
txt4.grid(column=1, row=4)


lbl = Label(window, text = "Горизонталь", font=("Times New Roman", 15))
lbl.grid(column=2, row=0)
btn = Button(window, text=('Показать'), font=("Times New Roman", 15),command=ok1)
btn.grid(column=3, row=0)

lbl = Label(window, text = "Вертикаль", font=("Times New Roman", 15))
lbl.grid(column=2, row=1)
btn = Button(window, text=('Показать'), font=("Times New Roman", 15), command=ok2)
btn.grid(column=3, row=1)

lbl = Label(window, text = "3D", font=("Times New Roman", 15))
lbl.grid(column=2, row=2)
btn = Button(window, text=('Показать'), font=("Times New Roman", 15))
btn.grid(column=3, row=2)

lbl = Label(window, text = "Отсчеты", font=("Times New Roman", 15))
lbl.grid(column=2, row=3)
btn = Button(window, text=('Показать'), font=("Times New Roman", 15)),command=ok4)
btn.grid(column=3, row=3)
window.mainloop()
