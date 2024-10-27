# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSplitter, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
import resources_rc
from arbol import ArbolBinarioWidget
from catalogo import CatalogoWidget
from Entregas import RecientesWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 580))
        MainWindow.setMaximumSize(QSize(800, 580))
        MainWindow.setStyleSheet(u"background-color: rgb(43, 45, 48);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.barraMenu = QWidget(self.centralwidget)
        self.barraMenu.setObjectName(u"barraMenu")
        self.barraMenu.setGeometry(QRect(10, 0, 231, 560))
        self.barraMenu.setMinimumSize(QSize(0, 0))
        self.barraMenu.setAutoFillBackground(False)
        self.barraMenu.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255,89 ,0 );\n"
"}\n"
"QPushButton{\n"
"color:white; \n"
"text-align:left;\n"
"height:45px;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"padding: 5px;\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(238, 92, 2);\n}}")
        self.layoutWidget = QWidget(self.barraMenu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 70, 190, 450))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.b1Menu = QPushButton(self.layoutWidget)
        self.b1Menu.setObjectName(u"b1Menu")
        self.b1Menu.setEnabled(True)
        icon = QIcon()
        icon.addFile(u":/Fotos/resources png/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b1Menu.setIcon(icon)
        self.b1Menu.setIconSize(QSize(25, 25))
        self.b1Menu.setCheckable(True)
        self.b1Menu.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b1Menu)

        self.b2Catalogo = QPushButton(self.layoutWidget)
        self.b2Catalogo.setObjectName(u"b2Catalogo")
        icon1 = QIcon()
        icon1.addFile(u":/Fotos/resources png/catalog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b2Catalogo.setIcon(icon1)
        self.b2Catalogo.setIconSize(QSize(25, 25))
        self.b2Catalogo.setCheckable(True)
        self.b2Catalogo.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b2Catalogo)

        self.b3Acciones = QPushButton(self.layoutWidget)
        self.b3Acciones.setObjectName(u"b3Acciones")
        icon2 = QIcon()
        icon2.addFile(u":/Fotos/resources png/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b3Acciones.setIcon(icon2)
        self.b3Acciones.setIconSize(QSize(25, 25))
        self.b3Acciones.setCheckable(True)
        self.b3Acciones.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b3Acciones)

        self.b4Espera = QPushButton(self.layoutWidget)
        self.b4Espera.setObjectName(u"b4Espera")
        icon3 = QIcon()
        icon3.addFile(u":/Fotos/resources png/wait.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b4Espera.setIcon(icon3)
        self.b4Espera.setIconSize(QSize(25, 25))
        self.b4Espera.setCheckable(True)
        self.b4Espera.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b4Espera)

        self.b5Historial = QPushButton(self.layoutWidget)
        self.b5Historial.setObjectName(u"b5Historial")
        icon4 = QIcon()
        icon4.addFile(u":/Fotos/resources png/demography.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b5Historial.setIcon(icon4)
        self.b5Historial.setIconSize(QSize(25, 25))
        self.b5Historial.setCheckable(True)
        self.b5Historial.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b5Historial)

        self.b6Arboles = QPushButton(self.layoutWidget)
        self.b6Arboles.setObjectName(u"b6Arboles")
        icon5 = QIcon()
        icon5.addFile(u":/Fotos/resources png/tree.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b6Arboles.setIcon(icon5)
        self.b6Arboles.setIconSize(QSize(25, 25))
        self.b6Arboles.setCheckable(True)
        self.b6Arboles.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b6Arboles)

        self.b7Salir = QPushButton(self.layoutWidget)
        self.b7Salir.setObjectName(u"b7Salir")
        icon6 = QIcon()
        icon6.addFile(u":/Fotos/resources png/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.b7Salir.setIcon(icon6)
        self.b7Salir.setIconSize(QSize(25, 25))
        self.b7Salir.setCheckable(True)
        self.b7Salir.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.b7Salir)

        self.menuPrincipal = QWidget(self.centralwidget)
        self.menuPrincipal.setObjectName(u"menuPrincipal")
        self.menuPrincipal.setGeometry(QRect(240, 0, 550, 550))
        self.menuPrincipal.setMinimumSize(QSize(550, 560))
        self.menuPrincipal.setMaximumSize(QSize(550, 560))
        self.menuPrincipal.setAutoFillBackground(False)
        self.menuPrincipal.setStyleSheet(u"background-color:rgb(255, 255, 255);\n")
        self.splitter = QSplitter(self.menuPrincipal)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 551, 560))
        self.splitter.setOrientation(Qt.Vertical)
        self.stackedWidget = QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(550, 550))
        self.stackedWidget.setStyleSheet(u"QLabel{\n"
                                         u"color:black;\n}"
                                         u"QPushButton{\n"
                                         "background-color: rgb(255,255,255);\n"
                                        "border-radius: 10px;\n"
                                        "border-style: outset;\n"
                                        "border-width: 1px;\n"
                                        "border-color: rgb(0,0,0);\n"
                                         "color: black;\n}")
        self.principal = QWidget()
        self.principal.setObjectName(u"principal")
        self.splitter_2 = QSplitter(self.principal)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(40, 110, 473, 380))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 50, 50, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.label_3.setPalette(palette)
        font = QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_3)
        self.label_8 = QLabel(self.splitter_2)
        self.label_8.setObjectName(u"label_8")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.label_8.setPalette(palette1)
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_8)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(473, 140))
        self.label.setMaximumSize(QSize(473, 140))
        self.label.setPixmap(QPixmap(u":/Fotos/resources png/Anahuac Mayab Logo 2.png"))
        self.label.setScaledContents(True)
        self.splitter_2.addWidget(self.label)
        self.stackedWidget.addWidget(self.principal)
        self.catalog_page = CatalogoWidget()
        self.catalog_page.setObjectName(u"catalog_page")
        self.stackedWidget.addWidget(self.catalog_page)
        self.recientes_page = RecientesWidget()
        self.recientes_page.setObjectName(u"recientes_page")
        self.stackedWidget.addWidget(self.recientes_page)
        self.espera_page = QWidget()
        self.espera_page.setObjectName(u"espera_page")
        self.stackedWidget.addWidget(self.espera_page)
        self.historial_page = QWidget()
        self.historial_page.setObjectName(u"historial_page")
        self.stackedWidget.addWidget(self.historial_page)
        self.arboles_page = ArbolBinarioWidget()
        self.arboles_page.setObjectName(u"arboles_page")
        self.stackedWidget.addWidget(self.arboles_page)
        self.splitter.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.b7Salir.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b1Menu.setText(QCoreApplication.translate("MainWindow", u"Menu principal", None))
        self.b2Catalogo.setText(QCoreApplication.translate("MainWindow", u"Cat\u00e1logo de libros", None))
        self.b3Acciones.setText(QCoreApplication.translate("MainWindow", u"Acciones recientes", None))
        self.b4Espera.setText(QCoreApplication.translate("MainWindow", u"Lista de espera", None))
        self.b5Historial.setText(QCoreApplication.translate("MainWindow", u"Historial de pr\u00e9stamos", None))
        self.b6Arboles.setText(QCoreApplication.translate("MainWindow", u"\u00c1rboles", None))
        self.b7Salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Proyecto final\n\nSebatián Velasco Cantu - 00517161", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Estructuras de datos", None))
        self.label.setText("")
    # retranslateUi

