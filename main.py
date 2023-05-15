from PySide2.QtWidgets import QMainWindow, QApplication
from design import Ui_MainWindow
from math import pow, fabs

class calculator(QMainWindow):
    def __init__(self,parent=None):
        super(calculator, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pdButton.clicked.connect(self.pd_run)
        self.ui.ntButton.clicked.connect(self.newton_run)

    def pd_run(self):
        coef = list(map(float, self.ui.coef_edit.text().split(' ')))
        eps = float(self.ui.eps_edit.text())
        left = float(self.ui.left_edit.text())
        right = float(self.ui.right_edit.text())

        root = poldel(left,right,eps,coef)
        self.ui.pd_Label.setText(f'Корень: {root:.6f}')

    def newton_run(self):
        coef = list(map(float, self.ui.coef_edit.text().split(' ')))
        eps = float(self.ui.eps_edit.text())
        left = float(self.ui.left_edit.text())
        right = float(self.ui.right_edit.text())

        root = newton(left,coef,eps,1000)
        self.ui.nt_label.setText(f'Корень: {root:.6f}')

def f(x, coef):
    """ Вычисление значения полинома на заданной точке """
    # Задайте полином и его коэффициенты
    a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 = coef
    fx = a0 + a1 * x + a2 * pow(x, 2) + a3 * pow(x, 3) + a4 * pow(x, 4) + a5 * pow(x, 5) + a6 * pow(x, 6) + a7 * pow(x, 7) + a8 * pow(x, 8) + a9 * pow(x, 9) + a10 * pow(x, 10) + a11 * pow(x, 11) + a12 * pow(x, 12)
    return fx


def f_prim(x, coef):
    """ Вычисление значения производной полинома в заданной точке"""
    a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12 = coef
    f_prim = a1 + 2 * a2 * x + 3 * a3 * pow(x, 2) + 4 * a4 * pow(x, 3) + 5 * a5 * pow(x, 4) + 6 * a6 * pow(x, 5) + 7 * a7 * pow(x, 6) + 8 * a8 * pow(x, 7) + 9 * a9 * pow(x, 8) + 10 * a10 * pow(x, 9) + 11 * a11 * pow(x, 10) + 12 * a12 * pow(x, 11)
    return f_prim

# def poldel(left, right, coef, eps):
#     """ Решение уравнения методом половинного деления (бинарный поиск) с заданной точностью """
#     center = (left + right) / 2
#     while fabs(f(center, coef)) > eps:
#         if f(left, coef) * f(center, coef) < 0:
#             right = center
#         else:
#             left = center
#
#         center = (left + right) / 2
#
#     return center
def poldel(left, right, eps,coef):
    mid = (left + right) / 2.0
    while abs(f(mid,coef)) > eps:
        if f(mid,coef) == 0:
            return mid
        elif f(left,coef) * f(mid,coef) < 0:
            right = mid
        else:
            left = mid
        mid = (left + right) / 2.0
    return mid

#def newton(x0, coef, eps):
#    """ Решение уравнения методом Ньютона с заданной точностью """
#    x = x0
#    while abs(f(x, coef)) > eps:
#        x -= f(x, coef) / f_prim(x, coef)
#    return x
# max_iter=1000
def newton(left, coef, eps, max_iter):
    xn = left

    for n in range(0, max_iter):
        fxn = f(xn,coef)
        if abs(fxn) < eps:
            return xn
        Dfxn = f_prim(xn,coef)
        if Dfxn == 0:
            return None
        xn = xn - fxn / Dfxn

    return None

if __name__ == '__main__':
    app = QApplication([])
    window = calculator()
    window.show()
    app.exec_()