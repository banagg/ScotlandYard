import rules
import socket, pickle
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import gui

def ccreate():
    localhost = "127.0.0.1"
    port = 8080
    ccreate.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ccreate.mysocket.connect((localhost, port))

    data = ccreate.mysocket.recv(4096)
    ccreate.lis = pickle.loads(data)
    e1.set()
    print (ccreate.lis)

def gcreate():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    gcreate.ui = gui.Ui_MainWindow()
    gcreate.ui.setupUi(MainWindow)

    gcreate.ui.pushButton.setEnabled(False)
    gcreate.ui.pushButton_3.setEnabled(False)
    gcreate.ui.pushButton_4.setEnabled(False)
    gcreate.ui.comboBox.setEnabled(False)
    gcreate.ui.label.setText("Start the Game")
    gcreate.ui.label.setEnabled(False)
    gcreate.ui.pushButton.clicked.connect(but_pushed)

    e1.wait()
    gcreate.ui.label.setEnabled(True)
    x1 = int(ccreate.lis[1][1])
    y1 = int(ccreate.lis[1][2])

    x2 = int(ccreate.lis[2][1])
    y2 = int(ccreate.lis[2][2])

    x3 = int(ccreate.lis[3][1])
    y3 = int(ccreate.lis[3][2])

    x4 = int(ccreate.lis[4][1])
    y4 = int(ccreate.lis[4][2])

    x5 = int(ccreate.lis[5][1])
    y5 = int(ccreate.lis[5][2])

    xx = int(ccreate.lis[0][1])
    xy = int(ccreate.lis[0][2])

    gcreate.pixmapItem2 = gcreate.ui.scene.addPixmap(gcreate.ui.pix2)
    gcreate.pixmapItem3 = gcreate.ui.scene.addPixmap(gcreate.ui.pix3)
    gcreate.pixmapItem4 = gcreate.ui.scene.addPixmap(gcreate.ui.pix4)
    gcreate.pixmapItem5 = gcreate.ui.scene.addPixmap(gcreate.ui.pix5)
    gcreate.pixmapItem6 = gcreate.ui.scene.addPixmap(gcreate.ui.pix6)

    gcreate.pixmapItem2.setOffset(x1,y1-50)
    gcreate.pixmapItem3.setOffset(x2,y2-50)
    gcreate.pixmapItem4.setOffset(x3,y3-50)
    gcreate.pixmapItem5.setOffset(x4,y4-50)
    gcreate.pixmapItem6.setOffset(x5,y5-50)
    gcreate.ui.pushButton.setEnabled(True)
    gcreate.ui.pushButton_3.setEnabled(True)
    gcreate.ui.pushButton_4.setEnabled(False)
    gcreate.ui.comboBox.setEnabled(True)

    MainWindow.show()

    sys.exit(app.exec_())

def play_move(y, x):
    if x == 0 and y == 3:
        start_game.pixmapItem0 = gcreate.scene.addPixmap(pix0)
    if y == 3 or y == 8 or y == 13 or y == 18:
        start_game.pixmapItem0.setOffset(int(ccreate.lis[0][1]), int(ccreate.lis[0][2]) - 50)

    gcreate.pixmapItem2.setOffset(int(ccreate.lis[1][1]), int(ccreate.lis[1][2]) - 50)
    gcreate.pixmapItem3.setOffset(int(ccreate.lis[2][1]), int(ccreate.lis[2][2]) - 50)
    gcreate.pixmapItem4.setOffset(int(ccreate.lis[3][1]), int(ccreate.lis[3][2]) - 50)
    gcreate.pixmapItem5.setOffset(int(ccreate.lis[4][1]), int(ccreate.lis[4][2]) - 50)
    gcreate.pixmapItem6.setOffset(int(ccreate.lis[5][1]), int(ccreate.lis[5][2]) - 50)
    gcreate.ui.comboBox.clear()

def but_pushed():
    gcreate.ui.label.setText("Move is played")

def det_moves(pos_trans, num):
    for x in range(len(pos_trans)):
        s = pos_trans[x][0] + " " + pos_trans[x][1]
        gcreate.ui.comboBox.addItem(s)
    while gcreate.ui.label.text() != "Move is played":
        QApplication.processEvents()
    ns = gcreate.ui.comboBox.currentText()
    nl = ns.split (" ")
    l = list(ccreate.lis[num])
    l[0] = nl[0]
    u = rules.conv(int(l[0]))
    l[1] = int(u[0])
    l[2] = int(u[1])
    t = tuple(l)
    ccreate.lis[num] = t

def fcreate():
    lis1 = pickle.dumps(ccreate.lis)
    ccreate.mysocket.send(lis1)

def start_game():
    start_game.det_no = 1
    for y in range(22):
        for x in range(6):
            if x ==  start_game.det_no:
                labeltext = "Move of Detective no." + str(x)
                gcreate.ui.label.setText(labeltext)
                det_moves(rules.poss_mov_det(ccreate.lis[x][0],x),x)
                lis1 = pickle.dumps(ccreate.lis)
                ccreate.mysocket.send(lis1)
            else:
                data = ccreate.mysocket.recv(4096)
                ccreate.lis = pickle.loads(data)
                print (ccreate.lis)
            play_move(y, x)
    start_game.pixmapItem0.setOffset(int(ccreate.lis[0][1]), int(ccreate.lis[0][2]) - 50)


e1 = threading.Event()
t1 = threading.Thread(target = ccreate)
t2 = threading.Thread(target = gcreate)
t3 = threading.Thread(target = start_game)

t1.start()
t1.join()
t2.start()
t3.start()