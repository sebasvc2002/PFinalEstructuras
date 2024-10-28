from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox
from PySide6.QtCore import Qt

class CatalogoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Libros")
        self.setGeometry(100, 100, 550, 500)

        # Lista para gestionar los libros como arreglos (listas)
        self.libros = []

        # Configuración de Vlayout
        self.layout = QVBoxLayout()

        # Botones
        self.btn_agregar = QPushButton("Agregar Libro")
        self.btn_agregar.clicked.connect(self.agregar_libro)
        self.btn_agregar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.layout.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton("Eliminar Libro")
        self.btn_eliminar.clicked.connect(self.eliminar_libro)
        self.btn_eliminar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.layout.addWidget(self.btn_eliminar)

        self.btn_ordenar = QPushButton("Ordenar por ISBN")
        self.btn_ordenar.clicked.connect(self.ordenar_libros)
        self.btn_ordenar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.layout.addWidget(self.btn_ordenar)

        self.btn_buscar = QPushButton("Buscar por ISBN")
        self.btn_buscar.clicked.connect(self.buscar_libro)
        self.btn_buscar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.layout.addWidget(self.btn_buscar)

        # Crear lista gráfica
        self.lista_libros = QListWidget()
        self.lista_libros.setStyleSheet("background-color: rgb(40,40,40); color: white;border-radius: 10px;max-height: 350px;font-size: 15px;")
        self.layout.addWidget(self.lista_libros)

        # Configuración de Vlayout
        self.setLayout(self.layout)

    def actualizar_pila(self):
        """Actualiza la lista gráfica de libros en la interfaz"""
        self.lista_libros.clear()
        for libro in self.libros:
            self.lista_libros.addItem(f"{libro['titulo']} - ISBN: {libro['isbn']}")
            print(self.libros)

    def agregar_libro(self):
        """Agrega un libro a la lista"""
        titulo, ok_titulo = QInputDialog.getText(self, "Agregar Libro", "Título del Libro:")
        if ok_titulo and titulo:
            isbn, ok_isbn = QInputDialog.getText(self, "Agregar Libro", "ISBN del Libro:")
            if ok_isbn and isbn:
                try:
                    isbn = int(isbn)  # Convertir ISBN a número
                    self.libros.append({"titulo": titulo, "isbn": isbn})
                    self.actualizar_pila()
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
            self.actualizar_pila()
        else:
            QMessageBox.warning(self, "Eliminar Libro", "Seleccione un libro para eliminar.")

    def ordenar_libros(self):
        """Ordena los libros por ISBN"""
        self.libros.sort(key=lambda libro: libro["isbn"])
        self.actualizar_pila()

    def buscar_libro(self):
        """Busca un libro por ISBN usando búsqueda binaria"""
        isbn, ok_isbn = QInputDialog.getText(self, "Buscar Libro", "ISBN del Libro:")
        if ok_isbn and isbn:
            try:
                isbn = int(isbn)  # Convertir ISBN a número
                self.ordenar_libros()  # Asegurarse de que la lista esté ordenada
                index = self.binary_search(isbn)
                if index != -1:
                    QMessageBox.information(self, "Libro Encontrado", f"Libro encontrado: {self.libros[index]['titulo']}\nPosición: {index+1}")
                else:
                    QMessageBox.warning(self, "No Encontrado", "No se encontró un libro con ese ISBN.")
            except ValueError:
                QMessageBox.warning(self, "ISBN Inválido", "El ISBN debe ser un número.")
        else:
            QMessageBox.warning(self, "Error", "Debe ingresar un ISBN válido.")

    def binary_search(self, isbn):
        """Realiza una búsqueda binaria en la lista de libros por ISBN"""
        low, high = 0, len(self.libros) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_isbn = self.libros[mid]["isbn"]
            if mid_isbn == isbn:
                return mid
            elif mid_isbn < isbn:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == "__main__":
    app = QApplication([])
    window = CatalogoWidget()
    window.show()
    app.exec()