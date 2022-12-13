import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np

scoplenie = pyfits.open("C:/v523cas60s-001.fit")
zvezdochka = scoplenie[0].data
Y_axes = zvezdochka[357][369:407]
print(Y_axes)
X_axes = []
for i in range(369,407):
    X_axes.append(i)
print(X_axes)
zvezdochka = np.transpose(zvezdochka)
Y1_axes = zvezdochka[384][338:376]
X1_axes = []
for j in range(338,376):
    X1_axes.append(j)
print(X1_axes)
scoplenie.close()

fig = plt.figure()
#graphic = plt.figure() # создали область Figure
lor = fig.add_subplot(111) # добавили к Figure область Axes. 111 - это первая строка, первый столбец и первая # (единственная) ячейка на сетке Figure.
lor.set_title("Звездочка горизонтальная ")
lor.set_xlabel("координата")
lor.set_ylabel("Возмоожно это светимомсть")
lor.plot(X_axes, Y_axes, color = "yellow")

plt.show()

fig1 = plt.figure()
graph = plt.Figure()
rol = fig1.add_subplot(111)

rol.set_title("Звездочка вертикальная")
rol.set_xlabel("координата")
rol.set_ylabel("Допустим светимость")
rol.plot(X1_axes, Y1_axes, color = "red")

plt.show()


