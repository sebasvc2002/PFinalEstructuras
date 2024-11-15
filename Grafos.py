import sys
from PySide6.QtWidgets import (
    QApplication, QDialog,QWidget, QVBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem
)
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import Qt, QPointF
import math

class Grafos:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = sum([weight for u, v, weight in result])
        return result, minimumCost


class GrafosWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            "QPushButton {background-color: rgb(63,63,63); color: white; border-radius: 10px; font-size: 15px; min-height: 40px;}"
            "QPushButton:hover {border: 2px solid rgb(255,255,255);}"
        )
        self.setWindowTitle("Grafos")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.lista = QListWidget()
        self.layout.addWidget(self.lista)

        self.btn_agregar = QPushButton("Agregar Arista")
        self.btn_agregar.clicked.connect(self.agregar_arista)
        self.layout.addWidget(self.btn_agregar)

        self.btn_calcular = QPushButton("Calcular MST")
        self.btn_calcular.clicked.connect(self.calcular_mst)
        self.layout.addWidget(self.btn_calcular)

        self.btn_visualizar = QPushButton("Visualizar Grafo")
        self.btn_visualizar.clicked.connect(self.visualizar_grafo)
        self.layout.addWidget(self.btn_visualizar)

        self.grafo = Grafos(7)
        self.node_positions = self.calculate_node_positions()

    def calculate_node_positions(self):
        positions = []
        radius = 200
        center_x, center_y = 400, 300
        for i in range(self.grafo.V):
            angle = 2 * 3.14159 * i / self.grafo.V
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            positions.append((x, y))
        return positions

    def agregar_arista(self):
        try:
            u, ok_u = QInputDialog.getInt(self, "Agregar Arista", "Nodo u (0-6):", 0, 0, 6)
            if not ok_u:
                return
            v, ok_v = QInputDialog.getInt(self, "Agregar Arista", "Nodo v (0-6):", 0, 0, 6)
            if not ok_v:
                return
            w, ok_w = QInputDialog.getInt(self, "Agregar Arista", "Peso:", 0, 0)
            if not ok_w:
                return

            if u == v:
                QMessageBox.warning(self, "Error", "No se puede agregar un bucle.")
                return

            self.grafo.addEdge(u, v, w)
            self.lista.addItem(f"Arista {u} -- {v} con peso {w}")

        except ValueError:
            QMessageBox.critical(self, "Error", "Entrada inválida.")

    def calcular_mst(self):
        self.lista.clear()
        result, cost = self.grafo.KruskalMST()
        self.lista.addItem(f"Costo total del MST: {cost}")
        for u, v, w in result:
            self.lista.addItem(f"Arista {u} -- {v} con peso {w}")
        self.mst_edges = result

    def visualizar_grafo(self):
        dialog = GraphDialog(self.node_positions, self.grafo.graph, getattr(self, 'mst_edges', []))
        dialog.exec()
class GraphDialog(QDialog):
    def __init__(self, node_positions, edges, mst_edges):
        super().__init__()
        self.setWindowTitle("Graph Visualization")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.bRegresar = QPushButton("Regresar")
        self.bRegresar.clicked.connect(self.close)
        self.layout.addWidget(self.bRegresar)
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.layout.addWidget(self.view)

        self.node_positions = node_positions
        self.edges = edges
        self.mst_edges = mst_edges

        self.draw_graph()

    def draw_graph(self):
        for i, (x, y) in enumerate(self.node_positions):
            node = QGraphicsEllipseItem(x - 10, y - 10, 20, 20)
            node.setBrush(Qt.white)
            self.scene.addItem(node)
            label = self.scene.addText(str(i))
            label.setPos(x - 5, y - 10)

        for u, v, w in self.edges:
            x1, y1 = self.node_positions[u]
            x2, y2 = self.node_positions[v]
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(QPen(Qt.black, 2))
            self.scene.addItem(line)

        for u, v, w in self.mst_edges:
            x1, y1 = self.node_positions[u]
            x2, y2 = self.node_positions[v]
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(QPen(Qt.red, 2))
            self.scene.addItem(line)
    def closeEvent(self, event):
        self.scene.clear()
        event.accept()
if __name__ == "__main__":
    app = QApplication([])
    ventana = GrafosWidget()
    ventana.show()
    sys.exit(app.exec())