import sys
from array import array

from PySide6.QtGui import QColor, QPalette,QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox,QComboBox,QLabel
from PySide6.QtCore import Qt

# Clase de lista circular doblemente ligada
class doubly_linked_list:
    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.nodo_sig = None
            self.nodo_ant = None

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def __str__(self):
        array = []
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            array.append(nodo_actual.valor)
            nodo_actual = nodo_actual.nodo_sig
        return str(array)

    def prepend(self, valor):
        nuevo_nodo = self.Nodo(valor)
        if self.cabeza is None and self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cabeza.nodo_ant = nuevo_nodo
            nuevo_nodo.nodo_sig = self.cabeza
            self.cabeza = nuevo_nodo
        self.size += 1

    def append(self, valor):
        nuevo_nodo = self.Nodo(valor)
        if self.cabeza is None and self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_sig = nuevo_nodo
            nuevo_nodo.nodo_ant = self.cola
            self.cola = nuevo_nodo
        self.size += 1

    def shift(self):
        if self.size == 0:
            self.cabeza = None
            self.cola = None
        elif self.size > 0:
            nodo_borrado = self.cabeza
            self.cabeza = nodo_borrado.nodo_sig
            if self.cabeza is not None:
                self.cabeza.nodo_ant = None
            nodo_borrado.nodo_sig = None
            self.size -= 1
        else:
            return None

    def pop(self):
        if self.size == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_borrado = self.cola
            self.cola = nodo_borrado.nodo_ant
            if self.cola is not None:
                self.cola.nodo_sig = None
            nodo_borrado.nodo_ant = None
            self.size -= 1
            return nodo_borrado.valor

    def get(self, index):
        if index == self.size - 1:
            return self.cola
        elif index == 0:
            return self.cabeza
        elif not (index >= self.size or index < 0):
            indice_balanceado = int(self.size / 2)
            if index <= indice_balanceado:
                nodo_actual = self.cabeza
                contador = 0
                while contador != index:
                    nodo_actual = nodo_actual.nodo_sig
                    contador += 1
                return nodo_actual
            else:
                nodo_actual = self.cola
                contador = self.size - 1
                while contador != index:
                    nodo_actual = nodo_actual.nodo_ant
                    contador -= 1
                return nodo_actual
        else:
            return None

    def update(self, index, valor):
        nodo_objetivo = self.get(index)
        if nodo_objetivo is not None:
            nodo_objetivo.valor = valor
        else:
            return None

    def insert(self, index, valor):
        if index == self.size - 1:
            return self.append(valor)
        elif not (index >= self.size or index < 0):
            nuevo_nodo = self.Nodo(valor)
            nodos_ant = self.get(index)
            nodos_sig = nodos_ant.nodo_sig
            nodos_ant.nodo_sig = nuevo_nodo
            nuevo_nodo.nodo_ant = nodos_ant
            nuevo_nodo.nodo_sig = nodos_sig
            if nodos_sig is not None:
                nodos_sig.nodo_ant = nuevo_nodo
            self.size += 1
        else:
            return None

    def remove(self, index):
        if index == 0:
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        elif not (index >= self.size or index < 0):
            nodo_borrado = self.get(index)
            nodos_ant = nodo_borrado.nodo_ant
            nodos_sig = nodo_borrado.nodo_sig
            nodos_ant.nodo_sig = nodos_sig
            if nodos_sig is not None:
                nodos_sig.nodo_ant = nodos_ant
            nodo_borrado.nodo_sig = None
            nodo_borrado.nodo_ant = None
            self.size -= 1
            return nodo_borrado
        else:
            return None

    def reverse(self):
        nodos_revertidos = None
        nodo_actual = self.cabeza
        self.cola = nodo_actual
        while nodo_actual is not None:
            nodos_revertidos = nodo_actual.nodo_ant
            nodo_actual.nodo_ant = nodo_actual.nodo_sig
            nodo_actual.nodo_sig = nodos_revertidos
            nodo_actual = nodo_actual.nodo_ant
        if nodos_revertidos is not None:
            self.cabeza = nodos_revertidos.nodo_ant

class ListaWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de reproducción")
        self.setGeometry(100,100,500,500)
        self.lista = doubly_linked_list()

        # Layouts
        self.layout = QVBoxLayout()
        self.Hlayout1=QHBoxLayout()
        self.Hlayout2=QHBoxLayout()
        self.Hlayout3 = QHBoxLayout()
        self.index=0

        #botones
        self.player=QLabel("Reproductor")
        self.pixmap=QPixmap("resources png/Music.png")
        self.pixmap=self.pixmap.scaled(100,100,Qt.KeepAspectRatio)
        self.player.setPixmap(self.pixmap)
        self.player.setAlignment(Qt.AlignCenter)
        self.Actual=QLabel("Canción actual:")
        self.Actual.setAlignment(Qt.AlignCenter)
        self.CActual=QLabel("Ninguna")

        self.BAgregar = QPushButton("Agregar canción")
        self.BAgregar.clicked.connect(self.agregar_cancion)
        self.BAgregar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.BEliminar = QPushButton("Eliminar canción")
        self.BEliminar.clicked.connect(self.eliminar_cancion)
        self.BEliminar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.BSiguiente = QPushButton("Siguiente canción")
        self.BSiguiente.clicked.connect(self.siguiente_cancion)
        self.BSiguiente.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.BAnterior = QPushButton("Canción anterior")
        self.BAnterior.clicked.connect(self.cancion_anterior)
        self.BAnterior.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")



        self.lista_rep = QListWidget()
        self.lista_rep.setStyleSheet("background-color: rgb(40,40,40); color: white;border-radius: 10px;max-height: 350px;font-size: 15px;")

        #Configuración de layout
        self.Hlayout2.addWidget(self.BAgregar)
        self.Hlayout2.addWidget(self.BEliminar)
        self.Hlayout3.addWidget(self.BSiguiente)
        self.Hlayout3.addWidget(self.BAnterior)
        self.layout.addSpacing(50)
        self.layout.addWidget(self.player)
        self.layout.addWidget(self.Actual)
        self.layout.addWidget(self.CActual)
        self.layout.addLayout(self.Hlayout2)
        self.layout.addLayout(self.Hlayout3)
        self.layout.addSpacing(100)
        self.layout.alignment()
        self.Hlayout1.addLayout(self.layout)
        self.Hlayout1.addWidget(self.lista_rep)
        self.setLayout(self.Hlayout1)

    # Funciones de los botones
    def agregar_cancion(self):
        cancion, ok_cancion = QInputDialog.getText(self, "Agregar canción", "Nombre de la canción:")
        if ok_cancion and cancion:
            autor, ok_autor = QInputDialog.getText(self, "Agregar canción", "Nombre del autor:")
            try:
                self.lista.append({"cancion": cancion, "autor": autor})
                self.actualizar_lista()
            except ValueError:
                QMessageBox.critical(self, "Error", "El nombre debe ser texto")
    def eliminar_cancion(self):
        selectedItem=self.lista_rep.currentRow()
        if selectedItem>=0:
            self.lista.remove(selectedItem)
            self.actualizar_lista()
            self.index=0
        else:
            QMessageBox.warning(self, "Error", "Debe seleccionar una canción")
    def siguiente_cancion(self):
        nodo=None
        try:
            self.index=(self.index+1)%self.lista.size
            nodo = self.lista.get(self.index)
        except ZeroDivisionError:
            pass
        if nodo is not None:
            self.CActual.setText(f"{nodo.valor['cancion']} - {nodo.valor['autor']}")
        else:
            self.CActual.setText("Ninguna")
    def cancion_anterior(self):
        nodo=None
        try:
            self.index = (self.index - 1) % self.lista.size
            nodo = self.lista.get(self.index)
        except ZeroDivisionError:
            pass

        if nodo is not None:
            self.CActual.setText(f"{nodo.valor['cancion']} - {nodo.valor['autor']}")
        else:
            self.CActual.setText("Ninguna")
    def actualizar_lista(self):
        self.lista_rep.clear()
        for i in range(self.lista.size):
            nodo=self.lista.get(i)
            self.lista_rep.addItem(f"{i+1}. {nodo.valor['cancion']} - {nodo.valor['autor']}")
        if self.lista.size>0:
            nodo=self.lista.get(self.index)
            self.CActual.setText(f"{nodo.valor['cancion']} - {nodo.valor['autor']}")
        else:
            self.CActual.setText("Ninguna")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ListaWidget()
    ventana.show()
    app.exec()
