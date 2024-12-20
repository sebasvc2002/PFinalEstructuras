#Autor Sebastián Velasco Cantú

from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QGraphicsView, QGraphicsScene, \
    QGraphicsEllipseItem, QMessageBox,QHBoxLayout, QApplication
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPainter, QPen, QColor, QIcon


class NodoArbol:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ArbolBinarioWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(550, 500)
        self.raiz_arbol = None  # Root of the binary tree


        self.icon=QIcon("resources png/info.png")
        # Layouts
        self.layout = QVBoxLayout()
        self.layouth=QHBoxLayout()
        self.layouth1=QHBoxLayout()
        self.layoutInfo=QHBoxLayout()

        # Añadir nodos
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Introduce valor")
        self.input_field.setStyleSheet("background-color: rgb(40,40,40); color: white;border-radius: 10px;min-height: 40px;font-size: 15px;")
        self.bInfo = QPushButton("")
        self.bInfo.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.bInfo.setIcon(self.icon)
        self.bInfo.setIconSize(QSize(35,35))



        # Botones
        self.bAgregar = QPushButton("Añadir nodo")
        self.bAgregar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.BEliminar = QPushButton("Borrar nodo")
        self.BEliminar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.BBuscar = QPushButton("Buscar nodo")
        self.BBuscar.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.BPreorden = QPushButton("Preorden")
        self.BPreorden.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.BInorden = QPushButton("Inorden")
        self.BInorden.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")
        self.bPostorden = QPushButton("Postorden")
        self.bPostorden.setStyleSheet("QPushButton{background-color: rgb(63,63,63); color: white;border-radius: 10px;font-size: 15px;min-height: 40px;}QPushButton:hover{border: 2px solid rgb(255,255,255);}")

        # Visualización del árbol binario
        self.scene = QGraphicsScene()
        self.graphics_view = QGraphicsView(self.scene)
        self.graphics_view.setRenderHint(QPainter.Antialiasing)
        self.scene.setBackgroundBrush(QBrush(QColor("#8b8b8b")))
        self.graphics_view.setFixedSize(535, 450)

        #Habilitar scroll del árbol
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scene.setSceneRect(0, 0, 1000, 1000)


        # Conectar botones
        self.bInfo.clicked.connect(self.info)
        self.bAgregar.clicked.connect(self.nuevo_nodo)
        self.BEliminar.clicked.connect(self.borrar_nodo)
        self.BBuscar.clicked.connect(self.buscar_nodo)
        self.BPreorden.clicked.connect(self.rPreorden)
        self.BInorden.clicked.connect(self.rInorden)
        self.bPostorden.clicked.connect(self.rPostorden)

        # Organización del layout
        self.layout.addSpacing(25)
        self.layoutInfo.addWidget(self.input_field)
        self.layoutInfo.addWidget(self.bInfo)
        self.layout.addLayout(self.layoutInfo)
        self.layouth.addWidget(self.bAgregar)
        self.layouth.addWidget(self.BEliminar)
        self.layouth.addWidget(self.BBuscar)
        self.layout.addLayout(self.layouth)
        self.layouth1.addWidget(self.BPreorden)
        self.layouth1.addWidget(self.BInorden)
        self.layouth1.addWidget(self.bPostorden)

        self.layout.addLayout(self.layouth1)
        self.layout.addSpacing(15)
        self.layout.addWidget(self.graphics_view)

        self.setLayout(self.layout)

    #Funciones de los botones
    def info(self):
        QMessageBox.information(self, "Acerca de","1. Ingresar un valor en el campo de texto\n2. Seleccionar la acción a realizar\n3. Visualizar el árbol binario")
    def nuevo_nodo(self):
        value = self.input_field.text().strip()
        if value:
            try:
            # Insert the node
                self.raiz_arbol = self._insertar(self.raiz_arbol, int(value))
                self.input_field.clear()
                self.refresh_Arbol()
            except ValueError:
                self.show_error()


    def borrar_nodo(self):
        value = self.input_field.text().strip()
        if value:
            # Delete the node
            self.raiz_arbol = self._borrar(self.raiz_arbol, int(value))
            self.input_field.clear()
            self.refresh_Arbol()
    def buscar_nodo(self):
        value = self.input_field.text().strip()
        if value:
            try:
                value = int(value)
                if value in self._preorden(self.raiz_arbol):
                    QMessageBox.information(self, "Resultado", f"Valor: {value} encontrado")
                else:
                    QMessageBox.information(self, "Resultado", f"Resultado: {value} no encontrado")
            except ValueError:
                self.show_error()
    def rPreorden(self):
        resultado = self._preorden(self.raiz_arbol)
        QMessageBox.information(self, "Preorden", f"Resultado:\n {resultado}")

    def rInorden(self):
        resultado = self._inorden(self.raiz_arbol)
        QMessageBox.information(self, "Inorden", f"Resultado:\n {resultado}")

    def rPostorden(self):
        resultado = self._postorden(self.raiz_arbol)
        QMessageBox.information(self, "Postorden", f"Resultado:\n {resultado}")
    def show_error(self):
        # Crear un mensaje emergente
       QMessageBox.warning(self, "Error", "Solamente ingresar números enteros")

    # Métodos del árbol binario
    def _insertar(self, node, value):
        if node is None:
            return NodoArbol(value)
        elif value < node.value:
            node.left = self._insertar(node.left, value)
        else:
            node.right = self._insertar(node.right, value)
        return node

    def _borrar(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._borrar(node.left, value)
        elif value > node.value:
            node.right = self._borrar(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._nodo_min_valor(node.right)
            node.value = temp.value
            node.right = self._borrar(node.right, temp.value)
        return node

    def _nodo_min_valor(self, node):
        actual = node
        while actual.left is not None:
            actual = actual.left
        return actual

    def _preorden(self, node):
        if node:
            return [node.value] + self._preorden(node.left) + self._preorden(node.right)
        return []

    def _inorden(self, node):
        if node:
            return self._inorden(node.left) + [node.value] + self._inorden(node.right)
        return []

    def _postorden(self, node):
        if node:
            return self._postorden(node.left) + self._postorden(node.right) + [node.value]
        return []

    def refresh_Arbol(self):
        self.scene.clear()
        self._dibujar_Arbol(self.raiz_arbol, 250, 50, 120)

    def _dibujar_Arbol(self, node, x, y, x_offset):
        if node:
            # Draw the node as a circle with a value label
            node_item = QGraphicsEllipseItem(x - 15, y - 15, 30, 30)
            node_item.setBrush(QBrush(QColor("#fe9560")))
            self.scene.addItem(node_item)

            # Add the node's value as text inside the circle
            text_item = self.scene.addText(str(node.value))
            text_item.setDefaultTextColor(Qt.black)
            text_item.setPos(x - 8, y - 10)

            # Create a pen for drawing lines
            pen = QPen(Qt.black)

            # Draw a line to the left child, if it exists
            if node.left:
                left_x = x - x_offset
                left_y = y + 50
                self.scene.addLine(x, y, left_x, left_y, pen)  # Use pen here
                self._dibujar_Arbol(node.left, left_x, left_y, x_offset // 2)

            # Draw a line to the right child, if it exists
            if node.right:
                right_x = x + x_offset
                right_y = y + 50
                self.scene.addLine(x, y, right_x, right_y, pen)  # Use pen here
                self._dibujar_Arbol(node.right, right_x, right_y, x_offset // 2)
if __name__ == "__main__":
    app = QApplication([])
    ventana = ArbolBinarioWidget()
    ventana.show()
    app.exec()