import rules
from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import socket,pickle
from gui import Ui_MainWindow
import threading

def screate():
    host = "127.0.0.1"
    port = 8080
    serverSocket = socket.socket()
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((host,port))
    serverSocket.listen(5)
    (screate.client,(ip,port)) = serverSocket.accept()

def gcreate():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    gcreate.ui = Ui_MainWindow()
    gcreate.ui.setupUi(MainWindow)

    scene = QGraphicsScene()
    gcreate.ui.graphicsView.setScene(scene)
    pix0 = QPixmap(os.getcwd() + "/resources/images/map.jpg")
    pixmapItem0 = scene.addPixmap(pix0)

    pix1 = QPixmap(os.getcwd() + "/resources/images/flag0.gif")
    pix2 = QPixmap(os.getcwd() + "/resources/images/flag1.gif")
    pix3 = QPixmap(os.getcwd() + "/resources/images/flag2.gif")
    pix4 = QPixmap(os.getcwd() + "/resources/images/flag3.gif")
    pix5 = QPixmap(os.getcwd() + "/resources/images/flag4.gif")
    pix6 = QPixmap(os.getcwd() + "/resources/images/flag5.gif")

    gcreate.pixmapItem1 = scene.addPixmap(pix1)
    gcreate.pixmapItem2 = scene.addPixmap(pix2)
    gcreate.pixmapItem3 = scene.addPixmap(pix3)
    gcreate.pixmapItem4 = scene.addPixmap(pix4)
    gcreate.pixmapItem5 = scene.addPixmap(pix5)
    gcreate.pixmapItem6 = scene.addPixmap(pix6)

    gcreate.ui.pushButton.setEnabled(False)
    gcreate.ui.pushButton_3.setEnabled(False)
    gcreate.ui.comboBox.setEnabled(False)
    gcreate.ui.label.setText("Start the Game")
    gcreate.ui.label.setEnabled(False)
    
    gcreate.ui.pushButton_4.clicked.connect(but4_pushed)
    gcreate.ui.pushButton.clicked.connect(but_pushed)

    MainWindow.show()  # The show() method displays the widget on the screen.
    sys.exit(app.exec_())  # Finally, we enter the mainloop of the application.

def play_move():
    gcreate.pixmapItem1.setOffset(int(ncreate.lis[0][1]), int(ncreate.lis[0][2]) - 50)
    gcreate.pixmapItem2.setOffset(int(ncreate.lis[1][1]), int(ncreate.lis[1][2]) - 50)
    gcreate.pixmapItem3.setOffset(int(ncreate.lis[2][1]), int(ncreate.lis[2][2]) - 50)
    gcreate.pixmapItem4.setOffset(int(ncreate.lis[3][1]), int(ncreate.lis[3][2]) - 50)
    gcreate.pixmapItem5.setOffset(int(ncreate.lis[4][1]), int(ncreate.lis[4][2]) - 50)
    gcreate.pixmapItem6.setOffset(int(ncreate.lis[5][1]), int(ncreate.lis[5][2]) - 50)
    gcreate.ui.comboBox.clear()


def but4_pushed():
    e3.set()

def but_pushed():
    gcreate.ui.label.setText("Move is played")

def det_moves(pos_trans, num):
    for x in range(len(pos_trans)):
        s = pos_trans[x][0] + " " + pos_trans[x][1]
        print(s)
        gcreate.ui.comboBox.addItem(s)
    while gcreate.ui.label.text() != "Move is played":
        QApplication.processEvents()
    ns = gcreate.ui.comboBox.currentText()
    nl = ns.split (" ")
    l = list(ncreate.lis[num])
    l[0] = nl[0]
    t = tuple(l)
    ncreate.lis[num] = t


def start_gui():
    gcreate.ui.label.setEnabled(True)

    x1 = int(ncreate.lis[1][1])
    y1 = int(ncreate.lis[1][2])

    x2 = int(ncreate.lis[2][1])
    y2 = int(ncreate.lis[2][2])

    x3 = int(ncreate.lis[3][1])
    y3 = int(ncreate.lis[3][2])

    x4 = int(ncreate.lis[4][1])
    y4 = int(ncreate.lis[4][2])

    x5 = int(ncreate.lis[5][1])
    y5 = int(ncreate.lis[5][2])

    xx = int(ncreate.lis[0][1])
    xy = int(ncreate.lis[0][2])

    gcreate.pixmapItem1.setOffset(xx,xy-50)
    gcreate.pixmapItem2.setOffset(x1,y1-50)
    gcreate.pixmapItem3.setOffset(x2,y2-50)
    gcreate.pixmapItem4.setOffset(x3,y3-50)
    gcreate.pixmapItem5.setOffset(x4,y4-50)
    gcreate.pixmapItem6.setOffset(x5,y5-50)
    gcreate.ui.pushButton.setEnabled(True)
    gcreate.ui.pushButton_3.setEnabled(True)
    gcreate.ui.pushButton_4.setEnabled(False)
    gcreate.ui.comboBox.setEnabled(True)

def ncreate():
    ncreate.lis = rules.start()
    lis1 = pickle.dumps(ncreate.lis)
    screate.client.send(lis1)
    for y in range(22):
        for x in range(6):
            e1.wait()
            if x > 0:
                data = screate.client.recv(4096)
                ncreate.lis = pickle.loads(data)
                lis2 = pickle.dumps(ncreate.lis)
                screate.client.send(lis2)
                print(ncreate.lis)
            else:
                while gcreate.ui.label.text() != "Move is played":
                    QApplication.processEvents()
                lis1 = pickle.dumps(ncreate.lis)
                screate.client.send(lis1)
            e1.clear()
            e2.set()

def start_game():
    e3.wait()
    start_gui()
    for y in range(22):
        for x in range(6):
            e1.set()
            e2.wait()
            if x == 0:
                labeltext = "Move of Player no." + str(x)
                gcreate.ui.label.setText(labeltext)
                det_moves(rules.poss_mov_det(ncreate.lis[x][0],x),x)
            play_move()
            e2.clear()

e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
t1 = threading.Thread(target = screate)
t2 = threading.Thread(target = gcreate)
t3 = threading.Thread(target = ncreate)
t4 = threading.Thread(target = start_game)

t1.start()
t1.join()
t2.start()
t3.start()
t4.start()