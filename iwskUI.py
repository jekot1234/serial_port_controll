# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iwsk.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1145, 962)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.portSelect = QtWidgets.QComboBox(self.centralwidget)
        self.portSelect.setGeometry(QtCore.QRect(20, 40, 91, 22))
        self.portSelect.setObjectName("portSelect")
        self.refreshCOMList = QtWidgets.QPushButton(self.centralwidget)
        self.refreshCOMList.setGeometry(QtCore.QRect(20, 70, 91, 23))
        self.refreshCOMList.setObjectName("refreshCOMList")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 111, 111))
        self.groupBox.setObjectName("groupBox")
        self.choseCOM = QtWidgets.QPushButton(self.groupBox)
        self.choseCOM.setGeometry(QtCore.QRect(10, 80, 91, 23))
        self.choseCOM.setObjectName("choseCOM")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 20, 111, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.baudSelect = QtWidgets.QComboBox(self.groupBox_2)
        self.baudSelect.setGeometry(QtCore.QRect(10, 30, 91, 22))
        self.baudSelect.setObjectName("baudSelect")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.baudSelect.addItem("")
        self.autoBauding = QtWidgets.QPushButton(self.groupBox_2)
        self.autoBauding.setEnabled(False)
        self.autoBauding.setGeometry(QtCore.QRect(10, 70, 91, 23))
        self.autoBauding.setObjectName("autoBauding")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 20, 111, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.characterBytesize = QtWidgets.QComboBox(self.groupBox_3)
        self.characterBytesize.setEnabled(False)
        self.characterBytesize.setGeometry(QtCore.QRect(60, 20, 41, 22))
        self.characterBytesize.setObjectName("characterBytesize")
        self.characterBytesize.addItem("")
        self.characterBytesize.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 47, 16))
        self.label_2.setObjectName("label_2")
        self.characterStopbits = QtWidgets.QComboBox(self.groupBox_3)
        self.characterStopbits.setEnabled(False)
        self.characterStopbits.setGeometry(QtCore.QRect(60, 50, 41, 22))
        self.characterStopbits.setObjectName("characterStopbits")
        self.characterStopbits.addItem("")
        self.characterStopbits.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 47, 21))
        self.label_3.setObjectName("label_3")
        self.characterParity = QtWidgets.QComboBox(self.groupBox_3)
        self.characterParity.setEnabled(False)
        self.characterParity.setGeometry(QtCore.QRect(60, 80, 41, 22))
        self.characterParity.setObjectName("characterParity")
        self.characterParity.addItem("")
        self.characterParity.addItem("")
        self.characterParity.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 47, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(370, 20, 111, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.XON_XOFF = QtWidgets.QCheckBox(self.groupBox_4)
        self.XON_XOFF.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.XON_XOFF.setObjectName("XON_XOFF")
        self.RTS_CTS = QtWidgets.QCheckBox(self.groupBox_4)
        self.RTS_CTS.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.RTS_CTS.setObjectName("RTS_CTS")
        self.DTR_DSR = QtWidgets.QCheckBox(self.groupBox_4)
        self.DTR_DSR.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.DTR_DSR.setObjectName("DTR_DSR")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(630, 20, 131, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.DTR = QtWidgets.QCheckBox(self.groupBox_5)
        self.DTR.setEnabled(False)
        self.DTR.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.DTR.setObjectName("DTR")
        self.RTS = QtWidgets.QCheckBox(self.groupBox_5)
        self.RTS.setEnabled(False)
        self.RTS.setGeometry(QtCore.QRect(20, 50, 70, 17))
        self.RTS.setObjectName("RTS")
        self.manual = QtWidgets.QCheckBox(self.groupBox_5)
        self.manual.setGeometry(QtCore.QRect(20, 80, 70, 17))
        self.manual.setObjectName("manual")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(490, 20, 131, 111))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(60, 50, 47, 13))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(60, 20, 47, 13))
        self.label_6.setObjectName("label_6")
        self.monitoring_start = QtWidgets.QPushButton(self.groupBox_6)
        self.monitoring_start.setEnabled(False)
        self.monitoring_start.setGeometry(QtCore.QRect(10, 80, 51, 23))
        self.monitoring_start.setObjectName("monitoring_start")
        self.monitoring_stop = QtWidgets.QPushButton(self.groupBox_6)
        self.monitoring_stop.setEnabled(False)
        self.monitoring_stop.setGeometry(QtCore.QRect(70, 80, 51, 23))
        self.monitoring_stop.setObjectName("monitoring_stop")
        self.DSR = QtWidgets.QLabel(self.groupBox_6)
        self.DSR.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.DSR.setText("")
        self.DSR.setObjectName("DSR")
        self.CTS = QtWidgets.QLabel(self.groupBox_6)
        self.CTS.setGeometry(QtCore.QRect(20, 50, 31, 16))
        self.CTS.setText("")
        self.CTS.setObjectName("CTS")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(780, 20, 171, 111))
        self.groupBox_7.setObjectName("groupBox_7")
        self.chosen_term = QtWidgets.QComboBox(self.groupBox_7)
        self.chosen_term.setGeometry(QtCore.QRect(10, 40, 71, 22))
        self.chosen_term.setObjectName("chosen_term")
        self.chosen_term.addItem("")
        self.chosen_term.addItem("")
        self.chosen_term.addItem("")
        self.chosen_term.addItem("")
        self.chosen_term.addItem("")
        self.userdefTerminator = QtWidgets.QLineEdit(self.groupBox_7)
        self.userdefTerminator.setEnabled(True)
        self.userdefTerminator.setGeometry(QtCore.QRect(90, 40, 71, 20))
        self.userdefTerminator.setToolTip("")
        self.userdefTerminator.setInputMask("")
        self.userdefTerminator.setText("")
        self.userdefTerminator.setObjectName("userdefTerminator")
        self.update_terminator = QtWidgets.QPushButton(self.groupBox_7)
        self.update_terminator.setEnabled(False)
        self.update_terminator.setGeometry(QtCore.QRect(90, 70, 71, 23))
        self.update_terminator.setObjectName("update_terminator")
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setGeometry(QtCore.QRect(30, 290, 541, 641))
        self.groupBox_8.setObjectName("groupBox_8")
        self.sendText = QtWidgets.QPlainTextEdit(self.groupBox_8)
        self.sendText.setGeometry(QtCore.QRect(10, 20, 521, 541))
        self.sendText.setObjectName("sendText")
        self.send = QtWidgets.QPushButton(self.groupBox_8)
        self.send.setEnabled(False)
        self.send.setGeometry(QtCore.QRect(440, 590, 75, 23))
        self.send.setObjectName("send")
        self.send_transaction = QtWidgets.QPushButton(self.groupBox_8)
        self.send_transaction.setEnabled(False)
        self.send_transaction.setGeometry(QtCore.QRect(120, 590, 71, 23))
        self.send_transaction.setObjectName("send_transaction")
        self.transaction_timeout = QtWidgets.QLineEdit(self.groupBox_8)
        self.transaction_timeout.setEnabled(True)
        self.transaction_timeout.setGeometry(QtCore.QRect(210, 591, 71, 21))
        self.transaction_timeout.setToolTip("")
        self.transaction_timeout.setStatusTip("")
        self.transaction_timeout.setWhatsThis("")
        self.transaction_timeout.setAccessibleName("")
        self.transaction_timeout.setAccessibleDescription("")
        self.transaction_timeout.setInputMask("")
        self.transaction_timeout.setText("")
        self.transaction_timeout.setObjectName("transaction_timeout")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(590, 290, 541, 641))
        self.groupBox_9.setObjectName("groupBox_9")
        self.receivText = QtWidgets.QPlainTextEdit(self.groupBox_9)
        self.receivText.setGeometry(QtCore.QRect(10, 20, 521, 541))
        self.receivText.setReadOnly(True)
        self.receivText.setObjectName("receivText")
        self.recieve = QtWidgets.QPushButton(self.groupBox_9)
        self.recieve.setEnabled(False)
        self.recieve.setGeometry(QtCore.QRect(340, 590, 75, 23))
        self.recieve.setObjectName("recieve")
        self.cancelRecieving = QtWidgets.QPushButton(self.groupBox_9)
        self.cancelRecieving.setEnabled(False)
        self.cancelRecieving.setGeometry(QtCore.QRect(440, 590, 75, 23))
        self.cancelRecieving.setObjectName("cancelRecieving")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(970, 20, 161, 111))
        self.groupBox_10.setObjectName("groupBox_10")
        self.ping = QtWidgets.QPushButton(self.groupBox_10)
        self.ping.setEnabled(False)
        self.ping.setGeometry(QtCore.QRect(10, 40, 61, 23))
        self.ping.setObjectName("ping")
        self.label = QtWidgets.QLabel(self.groupBox_10)
        self.label.setGeometry(QtCore.QRect(90, 30, 61, 16))
        self.label.setObjectName("label")
        self.responseTime = QtWidgets.QLabel(self.groupBox_10)
        self.responseTime.setGeometry(QtCore.QRect(100, 50, 47, 13))
        self.responseTime.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.responseTime.setObjectName("responseTime")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(350, 150, 461, 121))
        self.groupBox_11.setObjectName("groupBox_11")
        self.selectedCOM = QtWidgets.QLabel(self.groupBox_11)
        self.selectedCOM.setGeometry(QtCore.QRect(90, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.selectedCOM.setFont(font)
        self.selectedCOM.setAlignment(QtCore.Qt.AlignCenter)
        self.selectedCOM.setObjectName("selectedCOM")
        self.openPort = QtWidgets.QPushButton(self.groupBox_11)
        self.openPort.setEnabled(False)
        self.openPort.setGeometry(QtCore.QRect(130, 80, 81, 23))
        self.openPort.setObjectName("openPort")
        self.closePort = QtWidgets.QPushButton(self.groupBox_11)
        self.closePort.setEnabled(False)
        self.closePort.setGeometry(QtCore.QRect(240, 80, 81, 23))
        self.closePort.setObjectName("closePort")
        self.COMstatus = QtWidgets.QLabel(self.groupBox_11)
        self.COMstatus.setGeometry(QtCore.QRect(240, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.COMstatus.setFont(font)
        self.COMstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.COMstatus.setObjectName("COMstatus")
        self.listen_block = QtWidgets.QCheckBox(self.groupBox_11)
        self.listen_block.setEnabled(False)
        self.listen_block.setGeometry(QtCore.QRect(360, 80, 101, 21))
        self.listen_block.setObjectName("listen_block")
        self.groupBox_7.raise_()
        self.groupBox_4.raise_()
        self.groupBox.raise_()
        self.groupBox_6.raise_()
        self.groupBox_5.raise_()
        self.groupBox_2.raise_()
        self.portSelect.raise_()
        self.refreshCOMList.raise_()
        self.groupBox_3.raise_()
        self.groupBox_8.raise_()
        self.groupBox_9.raise_()
        self.groupBox_10.raise_()
        self.groupBox_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refreshCOMList.setText(_translate("MainWindow", "Odśwież listę"))
        self.groupBox.setTitle(_translate("MainWindow", "Wybór portu"))
        self.choseCOM.setText(_translate("MainWindow", "Wybierz"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Szybkość transmisji"))
        self.baudSelect.setItemText(0, _translate("MainWindow", "150"))
        self.baudSelect.setItemText(1, _translate("MainWindow", "200"))
        self.baudSelect.setItemText(2, _translate("MainWindow", "300"))
        self.baudSelect.setItemText(3, _translate("MainWindow", "600"))
        self.baudSelect.setItemText(4, _translate("MainWindow", "1200"))
        self.baudSelect.setItemText(5, _translate("MainWindow", "1800"))
        self.baudSelect.setItemText(6, _translate("MainWindow", "2400"))
        self.baudSelect.setItemText(7, _translate("MainWindow", "4800"))
        self.baudSelect.setItemText(8, _translate("MainWindow", "9600"))
        self.baudSelect.setItemText(9, _translate("MainWindow", "19200"))
        self.baudSelect.setItemText(10, _translate("MainWindow", "38400"))
        self.baudSelect.setItemText(11, _translate("MainWindow", "57600"))
        self.baudSelect.setItemText(12, _translate("MainWindow", "115200"))
        self.autoBauding.setText(_translate("MainWindow", "Autobauding"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Format znaku"))
        self.characterBytesize.setItemText(0, _translate("MainWindow", "7"))
        self.characterBytesize.setItemText(1, _translate("MainWindow", "8"))
        self.label_2.setText(_translate("MainWindow", "Długość"))
        self.characterStopbits.setItemText(0, _translate("MainWindow", "1"))
        self.characterStopbits.setItemText(1, _translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "Stop"))
        self.characterParity.setItemText(0, _translate("MainWindow", "E"))
        self.characterParity.setItemText(1, _translate("MainWindow", "O"))
        self.characterParity.setItemText(2, _translate("MainWindow", "N"))
        self.label_4.setText(_translate("MainWindow", "Kontrola"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Kontrola przepływu"))
        self.XON_XOFF.setText(_translate("MainWindow", "XON/XOFF"))
        self.RTS_CTS.setText(_translate("MainWindow", "RTS/CTS"))
        self.DTR_DSR.setText(_translate("MainWindow", "DTR/DSR"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sterowanie przepływem"))
        self.DTR.setText(_translate("MainWindow", "DTR"))
        self.RTS.setText(_translate("MainWindow", "RTS"))
        self.manual.setText(_translate("MainWindow", "Ręczne"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Monitorowanie stanu"))
        self.label_7.setText(_translate("MainWindow", "CTS"))
        self.label_6.setText(_translate("MainWindow", "DSR"))
        self.monitoring_start.setText(_translate("MainWindow", "Start"))
        self.monitoring_stop.setText(_translate("MainWindow", "Stop"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Wybór terminatora"))
        self.chosen_term.setItemText(0, _translate("MainWindow", "CR-LF"))
        self.chosen_term.setItemText(1, _translate("MainWindow", "CR"))
        self.chosen_term.setItemText(2, _translate("MainWindow", "LF"))
        self.chosen_term.setItemText(3, _translate("MainWindow", "brak"))
        self.chosen_term.setItemText(4, _translate("MainWindow", "własny"))
        self.userdefTerminator.setStatusTip(_translate("MainWindow", "dupa1"))
        self.userdefTerminator.setWhatsThis(_translate("MainWindow", "dupa2"))
        self.userdefTerminator.setAccessibleName(_translate("MainWindow", "dupa3"))
        self.userdefTerminator.setAccessibleDescription(_translate("MainWindow", "dupa4"))
        self.userdefTerminator.setPlaceholderText(_translate("MainWindow", "HEX np. ff ff"))
        self.update_terminator.setText(_translate("MainWindow", "Aktualizuj"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Nadawanie"))
        self.send.setText(_translate("MainWindow", "Wyślij"))
        self.send_transaction.setText(_translate("MainWindow", "Transakcja"))
        self.transaction_timeout.setPlaceholderText(_translate("MainWindow", "timeout w s"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Odbieranie"))
        self.recieve.setText(_translate("MainWindow", "Odbieraj"))
        self.cancelRecieving.setText(_translate("MainWindow", "Przerwij"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Testowanie Łącza"))
        self.ping.setText(_translate("MainWindow", "PING"))
        self.label.setText(_translate("MainWindow", "Czas odp.:"))
        self.responseTime.setText(_translate("MainWindow", "0.000s"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Status portu"))
        self.selectedCOM.setText(_translate("MainWindow", "Brak portu"))
        self.openPort.setText(_translate("MainWindow", "Otwórz"))
        self.closePort.setText(_translate("MainWindow", "Zamknij"))
        self.COMstatus.setText(_translate("MainWindow", "Zamknięty"))
        self.listen_block.setText(_translate("MainWindow", "Blokuj nasłuch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
