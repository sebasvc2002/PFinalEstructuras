from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QGraphicsView, QGraphicsScene, \
    QGraphicsEllipseItem, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen


class NodoArbol:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ArbolBinarioWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.tree_root = None  # Root of the binary tree

        # Layouts and Widgets
        self.layout = QVBoxLayout()

        # Input for adding nodes
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Introduce valor")

        # Buttons for actions
        self.add_button = QPushButton("Añadir nodo")
        self.delete_button = QPushButton("Borrar nodo")
        self.preorder_button = QPushButton("Preorden")
        self.inorder_button = QPushButton("Inorden")
        self.postorder_button = QPushButton("Postorden")
        self.result_label = QLabel("Traversal Result: ")

        # Tree visualization
        self.scene = QGraphicsScene()
        self.graphics_view = QGraphicsView(self.scene)
        self.graphics_view.setRenderHint(QPainter.Antialiasing)

        # Connect buttons
        self.add_button.clicked.connect(self.nuevo_nodo)
        self.delete_button.clicked.connect(self.borrar_nodo)
        self.preorder_button.clicked.connect(self.rPreorden)
        self.inorder_button.clicked.connect(self.rInorden)
        self.postorder_button.clicked.connect(self.rPostorden)

        # Assemble layout
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)
        self.layout.addWidget(self.preorder_button)
        self.layout.addWidget(self.inorder_button)
        self.layout.addWidget(self.postorder_button)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.graphics_view)

        self.setLayout(self.layout)

    def nuevo_nodo(self):
        value = self.input_field.text().strip()
        if value:
            try:
            # Insert the node
                self.tree_root = self._insertar(self.tree_root, float(value))
                self.input_field.clear()
                self.refresh_Arbol()
            except ValueError:
                self.show_error()


    def borrar_nodo(self):
        value = self.input_field.text().strip()
        if value:
            # Delete the node
            self.tree_root = self._delete(self.tree_root, float(value))
            self.input_field.clear()
            self.refresh_Arbol()

    def rPreorden(self):
        result = self._preorder(self.tree_root)
        self.result_label.setText(f"Resultado: {result}")

    def rInorden(self):
        result = self._inorden(self.tree_root)
        self.result_label.setText(f"Resultado:: {result}")

    def rPostorden(self):
        result = self._postorden(self.tree_root)
        self.result_label.setText(f"Resultado:: {result}")
    def show_error(self):
        # Crear un mensaje emergente
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("¡Inserta solamente números!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # Tree operations
    def _insertar(self, node, value):
        if node is None:
            return NodoArbol(value)
        elif value < node.value:
            node.left = self._insertar(node.left, value)
        else:
            node.right = self._insertar(node.right, value)
        return node

    def _delete(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._nodo_min_valor(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
        return node

    def _nodo_min_valor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _preorder(self, node):
        if node:
            return [node.value] + self._preorder(node.left) + self._preorder(node.right)
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
        self._dibujar_Arbol(self.tree_root, 250, 50, 120)

    def _dibujar_Arbol(self, node, x, y, x_offset):
        if node:
            # Draw the node as a circle with a value label
            node_item = QGraphicsEllipseItem(x - 15, y - 15, 30, 30)
            node_item.setBrush(Qt.gray)
            self.scene.addItem(node_item)

            # Add the node's value as text inside the circle
            text_item = self.scene.addText(str(node.value))
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
