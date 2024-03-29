# Form implementation generated from reading ui file 'add_room.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(310, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 240, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 190, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(310, 210, 221, 20))
        self.name_edit.setObjectName("name_edit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 240, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.area_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.area_spin.setGeometry(QtCore.QRect(310, 260, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.area_spin.setFont(font)
        self.area_spin.setMinimum(10)
        self.area_spin.setMaximum(50)
        self.area_spin.setObjectName("area_spin")
        self.cost_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.cost_spin.setGeometry(QtCore.QRect(430, 260, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cost_spin.setFont(font)
        self.cost_spin.setMinimum(450)
        self.cost_spin.setMaximum(2500)
        self.cost_spin.setObjectName("cost_spin")
        self.band_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.band_radio.setGeometry(QtCore.QRect(310, 290, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.band_radio.setFont(font)
        self.band_radio.setChecked(True)
        self.band_radio.setObjectName("band_radio")
        self.vocal_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.vocal_radio.setGeometry(QtCore.QRect(310, 310, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vocal_radio.setFont(font)
        self.vocal_radio.setObjectName("vocal_radio")
        self.drums_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.drums_radio.setGeometry(QtCore.QRect(310, 330, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.drums_radio.setFont(font)
        self.drums_radio.setObjectName("drums_radio")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.label_2.setText(_translate("MainWindow", "Площадь (м^2)"))
        self.label_3.setText(_translate("MainWindow", "Название"))
        self.label_4.setText(_translate("MainWindow", "Стоимость (3 ч)"))
        self.band_radio.setText(_translate("MainWindow", "Групповая"))
        self.vocal_radio.setText(_translate("MainWindow", "Вокальная"))
        self.drums_radio.setText(_translate("MainWindow", "Барабанная"))
