import sys

from menu import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from botones import MainWindow
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
main()