from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox,QComboBox
from PySide6.QtCore import Qt


class RecientesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Libros")
        self.setGeometry(100, 100, 500, 500)

        # Lista para gestionar los libros como arreglos (listas)
        self.acciones = []

        # Configuración de Vlayout
        self.layout = QVBoxLayout()
        self.layout.addSpacing(15)


        # Botones
        self._tipoAccion = QComboBox()
        self._tipoAccion.addItem("Check-in")
        self._tipoAccion.addItem("Check-out")
        self._tipoAccion.addItem("Perdido")
        self._tipoAccion.addItem("Dañado")
        self._tipoAccion.setStyleSheet("background-color: rgb(40,40,40); color: white;border-radius: 10px;min-height: 40px;font-size: 15px;")
        self.layout.addWidget(self._tipoAccion)
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


        # Configuración de Vlayout
        self.setLayout(self.layout)

    def actualizar_lista(self):
        """Actualiza la lista gráfica de libros en la interfaz"""
        self.Pila_Libros.clear()
        for libro in self.acciones:
            self.Pila_Libros.addItem(f"{libro['titulo']} - ISBN: {libro['isbn']} - {libro['accion']}")

    def agregar_accion(self):
        """Agrega un libro a la lista"""
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
        """Elimina el libro seleccionado de la lista"""
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
