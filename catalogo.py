from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox
from PySide6.QtCore import Qt


class CatalogoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Libros")
        self.setGeometry(100, 100, 500, 500)

        # Lista para gestionar los libros como arreglos (listas)
        self.libros = []

        # Configuración de layout
        self.layout = QVBoxLayout()

        # Crear lista gráfica
        self.lista_libros = QListWidget()
        self.layout.addWidget(self.lista_libros)

        # Botones
        self.btn_agregar = QPushButton("Agregar Libro")
        self.btn_agregar.clicked.connect(self.agregar_libro)
        self.layout.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton("Eliminar Libro")
        self.btn_eliminar.clicked.connect(self.eliminar_libro)
        self.layout.addWidget(self.btn_eliminar)

        self.btn_ordenar = QPushButton("Ordenar por ISBN")
        self.btn_ordenar.clicked.connect(self.ordenar_libros)
        self.layout.addWidget(self.btn_ordenar)

        # Configuración de layout
        self.setLayout(self.layout)

    def actualizar_lista(self):
        """Actualiza la lista gráfica de libros en la interfaz"""
        self.lista_libros.clear()
        for libro in self.libros:
            self.lista_libros.addItem(f"{libro['titulo']} - ISBN: {libro['isbn']}")

    def agregar_libro(self):
        """Agrega un libro a la lista"""
        titulo, ok_titulo = QInputDialog.getText(self, "Agregar Libro", "Título del Libro:")
        if ok_titulo and titulo:
            isbn, ok_isbn = QInputDialog.getText(self, "Agregar Libro", "ISBN del Libro:")
            if ok_isbn and isbn:
                try:
                    isbn = int(isbn)  # Convertir ISBN a número
                    self.libros.append({"titulo": titulo, "isbn": isbn})
                    self.actualizar_lista()
                except ValueError:
                    QMessageBox.warning(self, "ISBN Inválido", "El ISBN debe ser un número.")
            else:
                QMessageBox.warning(self, "Error", "Debe ingresar un ISBN válido.")
        else:
            QMessageBox.warning(self, "Error", "Debe ingresar un título válido.")

    def eliminar_libro(self):
        """Elimina el libro seleccionado de la lista"""
        selected_item = self.lista_libros.currentRow()
        if selected_item >= 0:
            self.libros.pop(selected_item)
            self.actualizar_lista()
        else:
            QMessageBox.warning(self, "Eliminar Libro", "Seleccione un libro para eliminar.")

    def ordenar_libros(self):
        """Ordena los libros por ISBN"""
        self.libros.sort(key=lambda libro: libro["isbn"])
        self.actualizar_lista()


if __name__ == "__main__":
    app = QApplication([])
    window = CatalogoWidget()
    window.show()
    app.exec()
