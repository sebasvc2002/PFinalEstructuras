from menu import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test1")
        self.b1Menu.clicked.connect(self.switch_menu)
        self.b2Catalogo.clicked.connect(self.switch_catalogo)
        self.b3Acciones.clicked.connect(self.switch_Acciones)
        self.b4Espera.clicked.connect(self.switch_Espera)
        self.b5Historial.clicked.connect(self.switch_Historial)
        self.b6Arboles.clicked.connect(self.switch_Arboles)

    def switch_menu(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_catalogo(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_Acciones(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_Espera(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_Historial(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_Arboles(self):
        self.stackedWidget.setCurrentIndex(5)
