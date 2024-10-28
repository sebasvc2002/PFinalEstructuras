from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox,QComboBox, QLabel,QHBoxLayout
from PySide6.QtCore import Qt
from collections import deque
class EsperaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Espera")
        self.setGeometry(100, 100, 550, 500)
        #Creación de la lista
        self.espera1 = deque()
        self.espera2 = deque()
        self.espera3 = deque()
        self.CurrentEspera=deque()
        # Configuración de Vlayout
        self.Vlayout = QVBoxLayout()
        self.HLayout=QHBoxLayout()
        # Botones
        self.TLibro = QComboBox()
        self.TLibro.addItem("Harry Potter - J.K. Rowling")
        self.TLibro.addItem("El Señor de los Anillos - J.R.R. Tolkien")
        self.TLibro.addItem("Cien años de soledad - Gabriel García Márquez")
        self.Vlayout.addSpacing(20)
        self.HLayout.addWidget(self.TLibro)
        self.BGo = QPushButton("Go")
        self.BGo.clicked.connect(self.go)
        self.BGo.setStyleSheet("background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 30px;")
        self.HLayout.addWidget(self.BGo)
        self.Vlayout.addLayout(self.HLayout)


        self.BAgregar = QPushButton("Agregar persona a la lista")
        self.BAgregar.clicked.connect(self.agregar_persona)
        self.BAgregar.setStyleSheet("background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 30px;")
        self.Vlayout.addWidget(self.BAgregar)
        self.BAtender = QPushButton("Atender persona")
        self.BAtender.clicked.connect(self.atender_persona)
        self.BAtender.setStyleSheet("background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 30px;")
        self.Vlayout.addWidget(self.BAtender)
        self.Vlayout.addSpacing(10)



        self.ColaLibros = QListWidget()
        self.ColaLibros.setStyleSheet("background-color: rgb(40,40,40); color: white;border-radius: 10px;max-height: 400px;font-size: 15px;")
        self.Vlayout.addWidget(self.ColaLibros)

        self.setLayout(self.Vlayout)
        self.go()
        self.TLibro.currentIndexChanged.connect(self.go)
        print(self.espera1)

    def agregar_persona(self):
        """Agrega una persona a la lista"""
        dq=self.TLibro.currentText()
        nombre, ok_nombre = QInputDialog.getText(self, "Agregar persona", "Nombre de la persona:")
        if dq=="Harry Potter - J.K. Rowling":
            if ok_nombre and nombre:
                try:
                    self.espera1.append(nombre)
                    self.actualizar_lista()
                except ValueError:
                    QMessageBox.critical(self, "Error", "El nombre debe ser texto")
        elif dq=="El Señor de los Anillos - J.R.R. Tolkien":
            if ok_nombre and nombre:
                try:
                    self.espera2.append(nombre)
                    self.actualizar_lista()
                except ValueError:
                    QMessageBox.critical(self, "Error", "El nombre debe ser texto")
        elif dq=="Cien años de soledad - Gabriel García Márquez":
            if ok_nombre and nombre:
                try:
                    self.espera3.append(nombre)
                    self.actualizar_lista()
                except ValueError:
                    QMessageBox.critical(self, "Error", "El nombre debe ser texto")
        else:
            pass

    def atender_persona(self):
        dq=self.TLibro.currentText()
        if dq == "Harry Potter - J.K. Rowling":
            self.espera1.popleft()
            self.actualizar_lista()
        elif dq == "El Señor de los Anillos - J.R.R. Tolkien":
            self.espera2.popleft()
            self.actualizar_lista()
        elif dq == "Cien años de soledad - Gabriel García Márquez":
            self.espera3.popleft()
            self.actualizar_lista()
        else:
            pass

    def go(self):
        self.actualizar_lista()
        dq=self.TLibro.currentText()
        if dq == "Harry Potter - J.K. Rowling":
            self.CurrentEspera=self.espera1

        elif dq == "El Señor de los Anillos - J.R.R. Tolkien":
            self.CurrentEspera=self.espera2

        elif dq == "Cien años de soledad - Gabriel García Márquez":
            self.CurrentEspera=self.espera3

        else:
            pass
    def actualizar_lista(self):
        """Actualiza la lista gráfica de personas en la interfaz"""
        self.ColaLibros.clear()
        for persona in self.CurrentEspera:
            self.ColaLibros.addItem(f"{persona}")
if __name__ == "__main__":
    app = QApplication([])
    ventana = EsperaWidget()
    ventana.show()
    app.exec()