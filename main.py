from PySide2.QtWidgets import QMainWindow, QApplication
from design import Ui_mainWindow

def sp(a, b, c, g, h, n):
    dx = (h - g) / n
    integral = 0
    for i in range(n):
        x0 = g + i * dx
        x1 = g + (i + 1) * dx
        xi = (x0 + x1) / 2
        fi = a * xi ** b + c
        integral += fi * dx
    return integral

class calculator(QMainWindow):
    def __init__(self,parent=None):
        super(calculator, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.sp_button.clicked.connect(self.run_sp)
        self.ui.simpson_button.clicked.connect(self.run_simpson)

    def run_sp(self):
        a = float(self.ui.a_line.text())
        b = float(self.ui.b_line.text())
        c = float(self.ui.c_line.text())
        g = float(self.ui.g_line.text())
        h = float(self.ui.h_line.text())
        n = float(self.ui.n_line.text())
        root = sp(a,b,c,g,h,n)
        self.ui.sp_label.setText(f'Корень: {root:.6f}')

    def run_simpson(self):
        a = float(self.ui.a_line.text())
        b = float(self.ui.b_line.text())
        c = float(self.ui.c_line.text())
        g = float(self.ui.g_line.text())
        h = float(self.ui.h_line.text())
        n = float(self.ui.n_line.text())
        root = simpson(a,b,c,g,h,n)
        self.ui.simpson_label.setText(f'Корень: {root:.6f}')


def sp(a,b,c,g,h,n):
    dx = (h - g) / n
    integral = 0
    for i in range(int(n)):
        x0 = g + i * dx
        x1 = g + (i + 1) * dx
        xi = (x0 + x1) / 2
        fi = a * xi ** b + c
        integral += fi * dx
    return integral

def simpson(a, b, c, g, h, n):
    dx = (h - g) / n
    integral = 0
    for i in range(int(n)):
        x0 = g + i * dx
        x1 = g + (i + 1) * dx
        xi = (x0 + x1) / 2
        fi0 = a * x0 ** b + c
        fi1 = a * x1 ** b + c
        fxi = a * xi ** b + c
        integral += dx / 6 * (fi0 + 4*fxi + fi1)
    return integral

if __name__ == '__main__':
    app = QApplication([])
    window = calculator()
    window.show()
    app.exec_()