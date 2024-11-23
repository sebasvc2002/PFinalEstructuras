#Autor Sebastián Velasco Cantú
import sys

from PySide6.QtWidgets import (
    QApplication, QDialog,QWidget, QVBoxLayout,QHBoxLayout, QListWidget, QPushButton, QInputDialog, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsTextItem, QGraphicsLineItem,QGraphicsPixmapItem
)
from PySide6.QtGui import QPen, QColor, QIcon,QPixmap
from PySide6.QtCore import Qt, QPointF, QSize
import math

class Grafos:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def addEdge(self, u, v, w):
        self.grafo.append([u, v, w])

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

    def Kruskal(self):
        result = []
        i = 0
        e = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        parent = list(range(self.V))
        rank = [0] * self.V

        while e < self.V - 1 and i < len(self.grafo):
            u, v, w = self.grafo[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        costoMinimo = sum([weight for u, v, weight in result])
        return result, costoMinimo


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

        # Layouts
        self.lista = QListWidget()
        self.infoLayout=QHBoxLayout()
        self.layout.addWidget(self.lista)

        # Botones
        self.Icon=QIcon("resources png/info.png")
        self.bInfo = QPushButton("")
        self.bInfo.setIcon(self.Icon)
        self.bInfo.setIconSize(QSize(35,35))
        self.bInfo.setMaximumWidth(50)
        self.bInfo.clicked.connect(self.info)
        self.infoLayout.addWidget(self.bInfo)

        self.btn_agregar = QPushButton("Agregar destino")
        self.btn_agregar.clicked.connect(self.agregar_arista)
        self.infoLayout.addWidget(self.btn_agregar)
        self.layout.addLayout(self.infoLayout)

        self.btn_calcular = QPushButton("Calcular costo mínimo")
        self.btn_calcular.clicked.connect(self.calcularKruskal)
        self.layout.addWidget(self.btn_calcular)

        self.btn_visualizar = QPushButton("Visualizar Grafo")
        self.btn_visualizar.clicked.connect(self.visualizar_grafo)
        self.layout.addWidget(self.btn_visualizar)

        # Grafo
        self.grafo = Grafos(7)
        self.node_positions = self.calcular_posiciones_nodos()

    #Funciones del grafo
    def calcular_posiciones_nodos(self):
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
            u, ok_u = QInputDialog.getInt(self, "Agregar Origen", "Número de casa (0-6):", 0, 0, 6)
            if not ok_u:
                return
            v, ok_v = QInputDialog.getInt(self, "Agregar Destino", "Número de casa (0-6):", 0, 0, 6)
            if not ok_v:
                return
            w, ok_w = QInputDialog.getInt(self, "Agregar distancia", "Distancia:", 0, 0)
            if not ok_w:
                return

            if u == v:
                QMessageBox.warning(self, "Error", "No se puede agregar un ciclo.")
                return

            self.grafo.addEdge(u, v, w)
            self.lista.addItem(f"Origen: Casa {u} -- Destino: Casa {v} con distancia {w}km")

        except ValueError:
            QMessageBox.critical(self, "Error", "Entrada inválida.")

    def calcularKruskal(self):
        self.lista.clear()
        result, cost = self.grafo.Kruskal()
        self.lista.addItem(f"Distancia total: {cost}")
        for u, v, w in result:
            self.lista.addItem(f"Origen: Casa {u}- Destino: Casa {v} con distancia {w}")
        self.mst_edges = result

    def visualizar_grafo(self):
        dialog = GraphDialog(self.node_positions, self.grafo.grafo, getattr(self, 'mst_edges', []))
        dialog.exec()

    def info(self):
        QMessageBox.information(self, "Acerca de", "1. Seleccionar el botón 'agregar destino'\n2. Elegir casa de origen\n3. Elegir casa destino\n4. Agregar distancia\n5. Seleccionar 'calcular costo mínimo' para obtener el recorrido más eficiente\n6. Seleccionar 'visualizar grafo' para ver el grafo")

#Visualizar grafo
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
        self.view.setStyleSheet("background-color: rgb(43,45,48)")

        self.node_positions = node_positions
        self.edges = edges
        self.mst_edges = mst_edges

        self.dibujar_Grafo()

    def dibujar_Grafo(self):
        node_image = QPixmap("resources png/home.png")  # Replace with the path to your image

        for i, (x, y) in enumerate(self.node_positions):
            node = QGraphicsPixmapItem(node_image)
            node.setPos(x - node_image.width() / 2, y - node_image.height() / 2)
            self.scene.addItem(node)
            label = QGraphicsTextItem(str(i))
            label.setDefaultTextColor(Qt.black)
            label.setPos(x - 5, y - 10)
            self.scene.addItem(label)

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
    #cerrar ventana
    def closeEvent(self, event):
        self.scene.clear()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    ventana = GrafosWidget()
    ventana.show()
    sys.exit(app.exec())