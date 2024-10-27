from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox,QComboBox
from PySide6.QtCore import Qt


class RecientesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Libros")
        self.setGeometry(100, 100, 500, 500)

        # Lista para gestionar los libros como arreglos (listas)
        self.acciones = []

        # Configuración de layout
        self.layout = QVBoxLayout()



        # Botones
        self._tipoAccion = QComboBox()
        self._tipoAccion.addItem("Check-in")
        self._tipoAccion.addItem("Check-out")
        self._tipoAccion.addItem("Perdido")
        self.layout.addWidget(self._tipoAccion)
        self.btn_agregar = QPushButton("Agregar Libro")
        self.btn_agregar.clicked.connect(self.agregar_accion)
        self.layout.addWidget(self.btn_agregar)
        self.btn_eliminar = QPushButton("Eliminar acción más reciente")
        self.btn_eliminar.clicked.connect(self.borrar_accion)
        self.layout.addWidget(self.btn_eliminar)
        # Crear lista gráfica
        self.Pila_Libros = QListWidget()
        self.layout.addWidget(self.Pila_Libros)


        # Configuración de layout
        self.setLayout(self.layout)

    def actualizar_lista(self):
        """Actualiza la lista gráfica de libros en la interfaz"""
        self.Pila_Libros.clear()
        QMessageBox.about(self, "Mensaje", "Acción realizada con éxito.")
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
        self.acciones.pop()
        self.actualizar_lista()



if __name__ == "__main__":
    app = QApplication([])
    window = RecientesWidget()
    window.show()
    app.exec()
