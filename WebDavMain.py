# -*- coding: utf-8 -*-

# Author Storm Shadow
#@mrfearless

import os
import sys
import re
import time
from time import time, sleep
import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QProcess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QComboBox,
        QDialog, QGroupBox, QLabel, QLineEdit, QSpinBox, QStyle, QSystemTrayIcon,
        QTextEdit, QSplashScreen, QMessageBox)
import time
import datetime
from datetime import datetime
import string
import subprocess
from subprocess import Popen, PIPE, call

import icons
dn = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, str(dn))
os.chdir(dn)


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)


try:
    with open("mapperbatcher.bat") as text_file:
        pass
except IOError:
    with open("mapperbatcher.bat", "w") as text_file:
        text_file.write('')

try:
    print os.getcwd()
    os.system("mapperbatcher.bat")
except IOError:
    pass





YOURAPIKEY = "" #enter your Google Maps JavaScript API
batcher = '''
:S_CHECK
IF EXIST S:\NUL ECHO S: Drive Exists - [DNSADRESS]
ECHO S: Connecting Drive...
NET USE S: /DELETE
NET USE S: \\\DNSADRESS@SSL@PORT somepass /USER:someuser /PERSISTENT:YES

'''
class Ui_messageformForm(QtWidgets.QWidget):
    def setupUi1(self, messageformForm):
        messageformForm.setObjectName("messageformForm")
        messageformForm.resize(404, 169)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(messageformForm.sizePolicy().hasHeightForWidth())
        messageformForm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        messageformForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        messageformForm.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(messageformForm)
        self.label.setGeometry(QtCore.QRect(40, 20, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(messageformForm)
        QtCore.QMetaObject.connectSlotsByName(messageformForm)

    def retranslateUi(self, messageformForm):
        _translate = QtCore.QCoreApplication.translate
        messageformForm.setWindowTitle(_translate("messageformForm", "Notice"))
        self.label.setText(_translate("messageformForm", "Will Be added in\n"
" future version"))

class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 314)
        MainWindow.setMinimumSize(QtCore.QSize(425, 314))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QToolTip\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #2a82da;\n"
"color: #ffffff;\n"
"border-radius: 3px;\n"
"opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  color: rgb(220,220,220);\n"
"  outline: none;\n"
"}\n"
"\n"

                                                                  "\n"
                                 "QPushButton:hover\n"
                                 "{\n"
                                 "border-radius: 3px;\n"
                                 "border: 1px solid #2a82da;\n"
                                "background-color: rgb(80, 80, 80);\n"
                                 "}\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e2352e, stop: 1 #e20046);\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 269, 12))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.comboBoxdrive = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdrive.setGeometry(QtCore.QRect(120, 50, 261, 21))
        self.comboBoxdrive.setEditable(True)
        self.comboBoxdrive.setObjectName("comboBoxdrive")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.comboBoxdrive.addItem("")
        self.label_station = QtWidgets.QLabel(self.centralwidget)
        self.label_station.setGeometry(QtCore.QRect(40, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_station.setFont(font)
        self.label_station.setAutoFillBackground(False)
        self.label_station.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_station.setTextFormat(QtCore.Qt.PlainText)
        self.label_station.setWordWrap(False)
        self.label_station.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_station.setObjectName("label_station")
        self.label_dns = QtWidgets.QLabel(self.centralwidget)
        self.label_dns.setGeometry(QtCore.QRect(40, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_dns.setFont(font)
        self.label_dns.setAutoFillBackground(False)
        self.label_dns.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_dns.setTextFormat(QtCore.Qt.PlainText)
        self.label_dns.setWordWrap(False)
        self.label_dns.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_dns.setObjectName("label_dns")
        self.comboBoxdrive_adress = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdrive_adress.setGeometry(QtCore.QRect(120, 90, 261, 21))
        self.comboBoxdrive_adress.setEditable(True)
        self.comboBoxdrive_adress.setObjectName("comboBoxdrive_adress")
        self.comboBoxdrive_adress.addItem("")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setGeometry(QtCore.QRect(40, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_port.setFont(font)
        self.label_port.setAutoFillBackground(False)
        self.label_port.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_port.setTextFormat(QtCore.Qt.PlainText)
        self.label_port.setWordWrap(False)
        self.label_port.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_port.setObjectName("label_port")
        self.comboBoxdrive_port = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdrive_port.setGeometry(QtCore.QRect(120, 130, 261, 21))
        self.comboBoxdrive_port.setEditable(True)
        self.comboBoxdrive_port.setObjectName("comboBoxdrive_port")
        self.comboBoxdrive_port.addItem("")
        self.comboBoxdrive_user = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxdrive_user.setGeometry(QtCore.QRect(120, 170, 261, 21))
        self.comboBoxdrive_user.setEditable(True)
        self.comboBoxdrive_user.setObjectName("comboBoxdrive_user")
        self.comboBoxdrive_user.addItem("")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(40, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_username.setFont(font)
        self.label_username.setAutoFillBackground(False)
        self.label_username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_username.setTextFormat(QtCore.Qt.PlainText)
        self.label_username.setWordWrap(False)
        self.label_username.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_username.setObjectName("label_username")
        self.label_passw = QtWidgets.QLabel(self.centralwidget)
        self.label_passw.setGeometry(QtCore.QRect(40, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_passw.setFont(font)
        self.label_passw.setAutoFillBackground(False)
        self.label_passw.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_passw.setTextFormat(QtCore.Qt.PlainText)
        self.label_passw.setWordWrap(False)
        self.label_passw.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_passw.setObjectName("label_passw")
        self.lineEditpass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditpass.setGeometry(QtCore.QRect(120, 210, 261, 21))
        self.lineEditpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditpass.setObjectName("lineEditpass")
        self.pushButtonapply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonapply.setGeometry(QtCore.QRect(150, 250, 71, 21))
        self.pushButtonapply.setObjectName("pushButtonapply")
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reset.setGeometry(QtCore.QRect(240, 250, 61, 21))
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.pushButton_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Quit.setGeometry(QtCore.QRect(320, 250, 61, 21))
        self.pushButton_Quit.setObjectName("pushButton_Quit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 250, 20, 20))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionBy_Storm_Shadow = QtWidgets.QAction(MainWindow)
        self.actionBy_Storm_Shadow.setObjectName("actionBy_Storm_Shadow")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButtonapply.clicked.connect(self.chuppa)
        self.pushButton_Quit.clicked.connect(self.quit_Gui)
        self.path = dn
        os.chdir(str(self.path))
        os.path.join(os.path.expanduser('~'), os.path.expandvars(str(self.path)))
        sys.path.insert(0, str(self.path))
        print self.path

    def chuppa(self):
        foldervalue = self.comboBoxdrive.currentText()
        dnsvalue = self.comboBoxdrive_adress.currentText()
        portvalue = self.comboBoxdrive_port.currentText()
        sudervalue = self.comboBoxdrive_user.currentText()
        passvalue = self.lineEditpass.text()
        print foldervalue
        print dnsvalue
        print portvalue
        print sudervalue
        print passvalue
        new_str1 = string.replace(batcher, ':S', str(foldervalue))
        new_str2 = string.replace(new_str1, 'S:', str(foldervalue))
        new_str3 = string.replace(new_str2, 'DNSADRESS', str(dnsvalue))
        new_str4 = string.replace(new_str3, 'somepass', passvalue)
        new_str5 = string.replace(new_str4, 'someuser', sudervalue)
        self.new_str6 = string.replace(new_str5, 'PORT', portvalue)
        maphtml = self.new_str6
        print self.new_str6
        with open("mapperbatcher.bat", "w") as text_file:
            text_file.write(self.new_str6)
            time.sleep(2)
        os.chdir(dn)
        print os.getcwd()
        os.system("mapperbatcher.bat")
        #filepath = dn
        #p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE)
        #"stdout, stderr = p.communicate()
        #print p.returncode  # is 0 if success

    #def Slingcatser(self):
    #    with open("mapperbatcher.bat", "w") as text_file:
    #        text_file.write(self.new_str6)
    #        time.sleep(2)
    #    os.chdir(dn)
    #    print os.getcwd()
    #    os.system("mapperbatcher.bat")
    #    filepath = dn
    #    p = subprocess.Popen(filepath, shell=True, stdout=subprocess.PIPE)

    #    stdout, stderr = p.communicate()
    #    print p.returncode  # is 0 if success
    #    if p.returncode == 0:
    #        SystemTrayIcon.welcome1()





    def quit_Gui(self):
        QApplication.instance().closeAllWindows()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NAS WebDav  Automapper"))
        self.label.setText(_translate("MainWindow", "WHat networkfolder would you like to connect to ?"))
        self.comboBoxdrive.setCurrentText(_translate("MainWindow", "A:"))
        self.comboBoxdrive.setItemText(0, _translate("MainWindow", "A:"))
        self.comboBoxdrive.setItemText(1, _translate("MainWindow", "B:"))
        self.comboBoxdrive.setItemText(2, _translate("MainWindow", "C:"))
        self.comboBoxdrive.setItemText(3, _translate("MainWindow", "D:"))
        self.comboBoxdrive.setItemText(4, _translate("MainWindow", "E:"))
        self.comboBoxdrive.setItemText(5, _translate("MainWindow", "F:"))
        self.comboBoxdrive.setItemText(6, _translate("MainWindow", "G:"))
        self.comboBoxdrive.setItemText(7, _translate("MainWindow", "H:"))
        self.comboBoxdrive.setItemText(8, _translate("MainWindow", "I:"))
        self.comboBoxdrive.setItemText(9, _translate("MainWindow", "J:"))
        self.comboBoxdrive.setItemText(10, _translate("MainWindow", "K:"))
        self.comboBoxdrive.setItemText(11, _translate("MainWindow", "L:"))
        self.comboBoxdrive.setItemText(12, _translate("MainWindow", "M:"))
        self.comboBoxdrive.setItemText(13, _translate("MainWindow", "N:"))
        self.comboBoxdrive.setItemText(14, _translate("MainWindow", "O:"))
        self.comboBoxdrive.setItemText(15, _translate("MainWindow", "P:"))
        self.comboBoxdrive.setItemText(16, _translate("MainWindow", "Q:"))
        self.comboBoxdrive.setItemText(17, _translate("MainWindow", "R:"))
        self.comboBoxdrive.setItemText(18, _translate("MainWindow", "S:"))
        self.comboBoxdrive.setItemText(19, _translate("MainWindow", "T:"))
        self.comboBoxdrive.setItemText(20, _translate("MainWindow", "U:"))
        self.comboBoxdrive.setItemText(21, _translate("MainWindow", "V:"))
        self.comboBoxdrive.setItemText(22, _translate("MainWindow", "W:"))
        self.comboBoxdrive.setItemText(23, _translate("MainWindow", "X:"))
        self.comboBoxdrive.setItemText(24, _translate("MainWindow", "Y:"))
        self.comboBoxdrive.setItemText(25, _translate("MainWindow", "Z:"))
        self.label_station.setText(_translate("MainWindow", "Station"))
        self.label_dns.setText(_translate("MainWindow", "Dns adresse"))
        self.comboBoxdrive_adress.setCurrentText(_translate("MainWindow", "dns.adress.com"))
        self.comboBoxdrive_adress.setItemText(0, _translate("MainWindow", "dns.adress.com"))
        self.comboBoxdrive_adress.setToolTip("Dont type https://")
        self.label_port.setText(_translate("MainWindow", "Port Number"))
        self.comboBoxdrive_port.setCurrentText(_translate("MainWindow", "5006"))
        self.comboBoxdrive_port.setItemText(0, _translate("MainWindow", "5006"))
        self.comboBoxdrive_user.setCurrentText(_translate("MainWindow", "admin"))
        self.comboBoxdrive_user.setItemText(0, _translate("MainWindow", "admin"))
        self.label_username.setText(_translate("MainWindow", "Username"))
        self.label_passw.setText(_translate("MainWindow", "Password"))
        self.pushButtonapply.setText(_translate("MainWindow", "Apply"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_Quit.setText(_translate("MainWindow", "Quit"))
        self.pushButton.setToolTip(_translate("MainWindow", "Author"))
        self.actionBy_Storm_Shadow.setText(_translate("MainWindow", "By Storm Shadow"))


class RightClickMenu(QtWidgets.QMenu):
    def __init__(self, parent=None):
        QtWidgets.QMenu.__init__(self, "Edit", parent)

        icon = QtGui.QIcon(":/ico/github.png")
        self.devAction = QAction(icon, "developer", self,
                                triggered=self.devv)
        self.addAction(self.devAction)

        icon = QtGui.QIcon(":/ico/1475190361_ip_adress.png")
        self.updateAction = QAction(icon, "Follow me on Twitter", self,
                                triggered=self.Followme)
        self.addAction(self.updateAction)


    def devv(self):
        import webbrowser
        webbrowser.open('https://github.com/techbliss/Nas_Dns_Automapper')

    def Followme(self):
        import webbrowser
        webbrowser.open('https://twitter.com/zadow28')


class LeftClickMenu(QtWidgets.QMenu, QSplashScreen):
    def __init__(self, parent=None):
        QtWidgets.QMenu.__init__(self, "File", parent)
        _translate = QtCore.QCoreApplication.translate

        icon = QtGui.QIcon(":/ico/record.png")
        self.maximizeAction = QAction(icon, "Setup Preferences", self,
                                      triggered=self.showm)
        self.addAction(self.maximizeAction)

        icon = QtGui.QIcon(":/ico/stop.png")
        self.quitAction = QAction(icon, "Quit", self,
                                  triggered=QApplication.instance().quit)
        self.addAction(self.quitAction)

    def showm(self):
        MainWindow.show()

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, parent)
        self.setIcon(QtGui.QIcon(":/ico/record.png"))

        self.right_menu = RightClickMenu()


        self.setContextMenu(self.right_menu)

        self.left_menu = LeftClickMenu()

        self.activated.connect(self.click_trap)

    def click_trap(self, value):
        if value == self.Trigger:  # left click!
            self.left_menu.exec_(QtGui.QCursor.pos())

    def welcome1(self):
        self.showMessage("Done setup mapped drive")

    def welcome2(self):
        self.showMessage("Welcome to ScreenRecorder", "You can also use the menu in the system tray")

    def show(self):
        QtWidgets.QSystemTrayIcon.show(self)
       # QtCore.QTimer.singleShot(100, self.welcome)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")

    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "Systray",
                "I couldn't detect any system tray on this system.")
        tray = SystemTrayIcon()
        tray.show()
        QApplication.setQuitOnLastWindowClosed(False)

    QApplication.setQuitOnLastWindowClosed(False)
    tray = SystemTrayIcon()
    tray.show()
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    messageformForm = QtWidgets.QWidget()
    ui2 = Ui_messageformForm()
    ui2.setupUi1(messageformForm)
    Form = QtWidgets.QWidget()
    sys.exit(app.exec_())


