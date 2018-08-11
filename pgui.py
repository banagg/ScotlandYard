#! /usr/bin/python3

# Character Encoding: UTF-8

#

# Here we provide the necessary imports.

# The basic GUI widgets are located in QtWidgets module. 

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1050, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1050, 700))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(1050, 680))
        self.centralWidget.setMaximumSize(QtCore.QSize(1050, 680))
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(400, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1050, 19))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuGame_Mode = QtWidgets.QMenu(self.menuBar)
        self.menuGame_Mode.setObjectName("menuGame_Mode")
        MainWindow.setMenuBar(self.menuBar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRules = QtWidgets.QAction(MainWindow)
        self.actionRules.setObjectName("actionRules")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPlayer_v_Player = QtWidgets.QAction(MainWindow)
        self.actionPlayer_v_Player.setObjectName("actionPlayer_v_Player")
        self.actionPlayer_v_Computer = QtWidgets.QAction(MainWindow)
        self.actionPlayer_v_Computer.setObjectName("actionPlayer_v_Computer")
        self.menuFile.addAction(self.actionNew_Game)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionRules)
        self.menuHelp.addAction(self.actionAbout)
        self.menuGame_Mode.addAction(self.actionPlayer_v_Player)
        self.menuGame_Mode.addAction(self.actionPlayer_v_Computer)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuGame_Mode.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.pushButton_2.setText(_translate("MainWindow", "Moves"))
        self.pushButton_3.setText(_translate("MainWindow", "Detectives"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Game"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuGame_Mode.setTitle(_translate("MainWindow", "Game Mode"))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRules.setText(_translate("MainWindow", "Rules"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPlayer_v_Player.setText(_translate("MainWindow", "Player v Player"))
        self.actionPlayer_v_Computer.setText(_translate("MainWindow", "Player v Computer"))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

scene = QGraphicsScene()
ui.graphicsView.setScene(scene)

pix1 = QPixmap(os.getcwd() + "/resources/images/map.jpg")
pixmapItem1 = scene.addPixmap(pix1)
pix2 = QPixmap(os.getcwd() + "/resources/images/flag1.gif")
pixmapItem2 = scene.addPixmap(pix2)
pixmapItem2.setOffset(500,600)

MainWindow.show()  # The show() method displays the widget on the screen.


sys.exit(app.exec_())  # Finally, we enter the mainloop of the application.