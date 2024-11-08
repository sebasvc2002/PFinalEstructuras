from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox,QComboBox
from PySide6.QtCore import Qt

class GrafosWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Libros")
        self.setGeometry(100, 100, 500, 500)
    #Grafos
    def grafo(self):
