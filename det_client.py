import rules
import socket, pickle
from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

localhost = "192.168.43.201"
port = 8079
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((localhost, port))
det_no = 1

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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(400, 0))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 5)
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
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
        self.pushButton_3.setText(_translate("MainWindow", "Detectives"))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.pushButton_4.setText(_translate("MainWindow", "Start Game"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuGame_Mode.setTitle(_translate("MainWindow", "Game Mode"))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRules.setText(_translate("MainWindow", "Rules"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionPlayer_v_Player.setText(_translate("MainWindow", "Player v Player"))
        self.actionPlayer_v_Computer.setText(_translate("MainWindow", "Player v Computer"))

lis = rules.start()

def play_move(y, x):
    if x == 0 and y == 3:
        pixmapItem0 = scene.addPixmap(pix0)
    if y == 3 or y == 8 or y == 13 or y == 18:
        pixmapItem0.setOffset(int(lis[0][1]), int(lis[0][2]) - 50)

    pixmapItem2.setOffset(int(lis[1][1]), int(lis[1][2]) - 50)
    pixmapItem3.setOffset(int(lis[2][1]), int(lis[2][2]) - 50)
    pixmapItem4.setOffset(int(lis[3][1]), int(lis[3][2]) - 50)
    pixmapItem5.setOffset(int(lis[4][1]), int(lis[4][2]) - 50)
    pixmapItem6.setOffset(int(lis[5][1]), int(lis[5][2]) - 50)
    ui.comboBox.clear()

def but_pushed():
    ui.label.setText("Move is played")

def det_moves(pos_trans, num):
    for x in range(len(pos_trans)):
        s = pos_trans[x][0] + " " + pos_trans[x][1]
        ui.comboBox.addItem(s)
    while ui.label.text() != "Move is played":
        QApplication.processEvents()
    ns = ui.comboBox.currentText()
    nl = ns.split (" ")
    l = list(lis[num])
    l[0] = nl[0]
    u = rules.conv(int(l[0]))
    l[1] = int(u[0])
    l[2] = int(u[1])
    t = tuple(l)
    lis[num] = t

def start_game():
    global lis
    data = mysocket.recv(4096)
    lis = pickle.loads(data)
    print (lis)
    ui.label.setEnabled(True)

    x1 = int(lis[1][1])
    y1 = int(lis[1][2])

    x2 = int(lis[2][1])
    y2 = int(lis[2][2])

    x3 = int(lis[3][1])
    y3 = int(lis[3][2])

    x4 = int(lis[4][1])
    y4 = int(lis[4][2])

    x5 = int(lis[5][1])
    y5 = int(lis[5][2])

    xx = int(lis[0][1])
    xy = int(lis[0][2])

    pix0 = QPixmap(os.getcwd() + "/resources/images/flag0.gif")
    pix2 = QPixmap(os.getcwd() + "/resources/images/flag1.gif")
    pix3 = QPixmap(os.getcwd() + "/resources/images/flag2.gif")
    pix4 = QPixmap(os.getcwd() + "/resources/images/flag3.gif")
    pix5 = QPixmap(os.getcwd() + "/resources/images/flag4.gif")
    pix6 = QPixmap(os.getcwd() + "/resources/images/flag5.gif")

    global pixmapItem0
    global pixmapItem2
    global pixmapItem3
    global pixmapItem4
    global pixmapItem5
    global pixmapItem6
    pixmapItem2 = scene.addPixmap(pix2)
    pixmapItem3 = scene.addPixmap(pix3)
    pixmapItem4 = scene.addPixmap(pix4)
    pixmapItem5 = scene.addPixmap(pix5)
    pixmapItem6 = scene.addPixmap(pix6)

    pixmapItem2.setOffset(x1,y1-50)
    pixmapItem3.setOffset(x2,y2-50)
    pixmapItem4.setOffset(x3,y3-50)
    pixmapItem5.setOffset(x4,y4-50)
    pixmapItem6.setOffset(x5,y5-50)
    ui.pushButton.setEnabled(True)
    ui.pushButton_3.setEnabled(True)
    ui.pushButton_4.setEnabled(False)
    ui.comboBox.setEnabled(True)

    for y in range(22):
        for x in range(6):
            if x ==  det_no:
                labeltext = "Move of Detective no." + str(x)
                ui.label.setText(labeltext)
                det_moves(rules.poss_mov_det(lis[x][0],x),x)
                lis1 = pickle.dumps(lis)
                mysocket.send(lis1)
            else:
                data = mysocket.recv(4096)
                lis = pickle.loads(data)
                print (lis)
            play_move(y, x)
    pixmapItem0.setOffset(int(lis[0][1]), int(lis[0][2]) - 50)



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

scene = QGraphicsScene()
ui.graphicsView.setScene(scene)

pix1 = QPixmap(os.getcwd() + "/resources/images/map.jpg")
pixmapItem1 = scene.addPixmap(pix1)

ui.pushButton.setEnabled(False)
ui.pushButton_3.setEnabled(False)
ui.pushButton_4.setEnabled(False)
ui.comboBox.setEnabled(False)
ui.label.setText("Start the Game")
ui.label.setEnabled(False)
#Game has started

ui.pushButton.clicked.connect(but_pushed)
start_game()

MainWindow.show()  # The show() method displays the widget on the screen.

sys.exit(app.exec_())  # Finally, we enter the mainloop of the application.