from PyQt5.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QListWidget, QPushButton, QInputDialog, QMessageBox, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

class CatalogoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Catálogo de Libros")
        self.setGeometry(100, 100, 550, 500)

        # Lista para gestionar los libros como arreglos (listas)
        self.libros = []

        # Configuración de Vlayout
        self.layout = QVBoxLayout()
        self.infoLayout=QHBoxLayout()

        # Botones
        self.icon=QIcon("resources png/info.png")
        self.bInfo = QPushButton("")
        self.bInfo.clicked.connect(self.info)
        self.bInfo.setIcon(self.icon)
        self.bInfo.setIconSize(QSize(35,35))
        self.bInfo.setMaximumWidth(40)
        self.bInfo.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.infoLayout.addWidget(self.bInfo)


        self.btn_agregar = QPushButton("Agregar Libro")
        self.btn_agregar.clicked.connect(self.agregar_libro)
        self.btn_agregar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.infoLayout.addWidget(self.btn_agregar)
        self.layout.addLayout(self.infoLayout)

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

    #Funciones de la lista
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
        selected_item = self.lista_libros.currentRow()
        if selected_item >= 0:
            self.libros.pop(selected_item)
            self.actualizar_pila()
        else:
            QMessageBox.warning(self, "Eliminar Libro", "Seleccione un libro para eliminar.")

    #Ordenar los libros por ISBN
    def ordenar_libros(self):
        self.libros.sort(key=lambda libro: libro["isbn"])
        self.actualizar_pila()

    #Buscar libro a través de su ISBN
    def buscar_libro(self):
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

    #Búsqueda binaria de un libro
    def binary_search(self, isbn):
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

    def info(self):
        QMessageBox.information(self, "Acerca de", "1. Seleccionar una acción a realizar\n2. Ingresar el título del libro y su ISBN\n3. Visualizar la lista de libros")


if __name__ == "__main__":
    app = QApplication([])
    window = CatalogoWidget()
    window.show()
    app.exec()