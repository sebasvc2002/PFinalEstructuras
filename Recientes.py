from PySide6.QtGui import QColor, QPalette, QBrush, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox,QComboBox, QHBoxLayout
from PySide6.QtCore import Qt,QSize


class RecientesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Libros")
        self.setGeometry(100, 100, 500, 500)

        # Creación de un arreglo para utilizar como pila
        self.acciones = []

        # Configuración de Vlayout
        self.layout = QVBoxLayout()
        self.infoLayout=QHBoxLayout()
        self.layout.addSpacing(15)


        # Botones
        self.icon=QIcon("resources png/info.png")
        self.bInfo = QPushButton("")
        self.bInfo.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.bInfo.setIcon(self.icon)
        self.bInfo.setIconSize(QSize(35,35))
        self.bInfo.clicked.connect(self.info)
        self.infoLayout.addWidget(self.bInfo)
        self.bInfo.setMaximumWidth(50)

        self._tipoAccion = QComboBox()
        self._tipoAccion.addItem("Check-in")
        self._tipoAccion.addItem("Check-out")
        self._tipoAccion.addItem("Perdido")
        self._tipoAccion.addItem("Dañado")
        self._tipoAccion.setStyleSheet("background-color: rgb(40,40,40); color: white;border-radius: 10px;min-height: 40px;font-size: 15px;")
        self.infoLayout.addWidget(self._tipoAccion)
        self.layout.addLayout(self.infoLayout)

        self.btn_agregar = QPushButton("Agregar Libro")
        self.btn_agregar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.btn_agregar.clicked.connect(self.agregar_accion)
        self.layout.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton("Eliminar acción más reciente")
        self.btn_eliminar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.btn_eliminar.clicked.connect(self.borrar_accion)
        self.layout.addWidget(self.btn_eliminar)

        # Crear lista gráfica
        self.Pila_Libros = QListWidget()
        self.Pila_Libros.setStyleSheet("background-color: rgb(40,40,40); color: white;border-radius: 10px;max-height: 350px;font-size: 15px;")

        self.layout.addWidget(self.Pila_Libros)


        # Configuración del layout
        self.setLayout(self.layout)

    #Funciones de la pila
    def info(self):
        QMessageBox.information(self, "Acerca de ","1. Seleccionar acción de la lista desplegable\n2. Seleccionar 'Agregar Libro'\n3. Seleccionar 'Eliminar acción más reciente' en caso de haberse equivocado")

    def actualizar_lista(self):
        """Actualiza la lista gráfica de libros en la interfaz"""
        self.Pila_Libros.clear()
        for libro in self.acciones:
            self.Pila_Libros.addItem(f"{self.acciones.index(libro)+1}. {libro['titulo']} - ISBN: {libro['isbn']} - {libro['accion']}")

    def agregar_accion(self):
        titulo, ok_titulo = QInputDialog.getText(self, "Título", "Título del Libro:")
        if ok_titulo and titulo:
            isbn, ok_isbn = QInputDialog.getText(self, "Hacer registro", "ISBN del Libro:")
            if ok_isbn and isbn:
                try:
                    isbn = int(isbn)# Convertir ISBN a número
                    accion = self._tipoAccion.currentText()
                    self.acciones.append({"accion": accion,"titulo": titulo, "isbn": isbn})
                    self.actualizar_lista()
                except ValueError:
                    QMessageBox.warning(self, "ISBN Inválido", "El ISBN debe ser un número.")
            else:
                QMessageBox.warning(self, "Error", "Debe ingresar un ISBN válido.")
        else:
            QMessageBox.warning(self, "Error", "Debe ingresar un título válido.")

    def borrar_accion(self):
        if len(self.acciones)==0:
            QMessageBox.warning(self, "Error", "No hay acciones para eliminar")
        else:
            self.acciones.pop()
        self.actualizar_lista()



if __name__ == "__main__":
    app = QApplication([])
    window = RecientesWidget()
    window.show()
    app.exec()
