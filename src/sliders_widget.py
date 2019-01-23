# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sliders.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(322, 360)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(322, 360))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_darkness_value = QtGui.QLabel(Form)
        self.label_darkness_value.setText(_fromUtf8(""))
        self.label_darkness_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_darkness_value.setObjectName(_fromUtf8("label_darkness_value"))
        self.gridLayout.addWidget(self.label_darkness_value, 4, 1, 1, 1)
        self.checkBox_darkness = QtGui.QCheckBox(Form)
        self.checkBox_darkness.setMinimumSize(QtCore.QSize(62, 0))
        self.checkBox_darkness.setChecked(True)
        self.checkBox_darkness.setObjectName(_fromUtf8("checkBox_darkness"))
        self.gridLayout.addWidget(self.checkBox_darkness, 12, 1, 1, 1)
        self.label_frequency_value = QtGui.QLabel(Form)
        self.label_frequency_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_frequency_value.setObjectName(_fromUtf8("label_frequency_value"))
        self.gridLayout.addWidget(self.label_frequency_value, 4, 2, 1, 1)
        self.checkBox_shift = QtGui.QCheckBox(Form)
        self.checkBox_shift.setObjectName(_fromUtf8("checkBox_shift"))
        self.gridLayout.addWidget(self.checkBox_shift, 12, 3, 1, 1)
        self.label_duty_cycle = QtGui.QLabel(Form)
        self.label_duty_cycle.setObjectName(_fromUtf8("label_duty_cycle"))
        self.gridLayout.addWidget(self.label_duty_cycle, 0, 3, 1, 1)
        self.verticalSlider_duty_cycle = QtGui.QSlider(Form)
        self.verticalSlider_duty_cycle.setMaximum(100)
        self.verticalSlider_duty_cycle.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_duty_cycle.setObjectName(_fromUtf8("verticalSlider_duty_cycle"))
        self.gridLayout.addWidget(self.verticalSlider_duty_cycle, 9, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_duty_cycle_value = QtGui.QLabel(Form)
        self.label_duty_cycle_value.setText(_fromUtf8(""))
        self.label_duty_cycle_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_duty_cycle_value.setObjectName(_fromUtf8("label_duty_cycle_value"))
        self.gridLayout.addWidget(self.label_duty_cycle_value, 4, 3, 1, 1)
        self.label_darkness = QtGui.QLabel(Form)
        self.label_darkness.setObjectName(_fromUtf8("label_darkness"))
        self.gridLayout.addWidget(self.label_darkness, 0, 1, 1, 1)
        self.verticalSlider_darkness = QtGui.QSlider(Form)
        self.verticalSlider_darkness.setMaximum(255)
        self.verticalSlider_darkness.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_darkness.setObjectName(_fromUtf8("verticalSlider_darkness"))
        self.gridLayout.addWidget(self.verticalSlider_darkness, 9, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_brightnes_value = QtGui.QLabel(Form)
        self.label_brightnes_value.setText(_fromUtf8(""))
        self.label_brightnes_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_brightnes_value.setObjectName(_fromUtf8("label_brightnes_value"))
        self.gridLayout.addWidget(self.label_brightnes_value, 4, 0, 1, 1)
        self.verticalSlider_frequency = QtGui.QSlider(Form)
        self.verticalSlider_frequency.setMinimum(1)
        self.verticalSlider_frequency.setMaximum(50)
        self.verticalSlider_frequency.setPageStep(5)
        self.verticalSlider_frequency.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_frequency.setObjectName(_fromUtf8("verticalSlider_frequency"))
        self.gridLayout.addWidget(self.verticalSlider_frequency, 9, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalSlider_brightness = QtGui.QSlider(Form)
        self.verticalSlider_brightness.setMaximum(255)
        self.verticalSlider_brightness.setPageStep(10)
        self.verticalSlider_brightness.setProperty("value", 5)
        self.verticalSlider_brightness.setTracking(True)
        self.verticalSlider_brightness.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_brightness.setTickPosition(QtGui.QSlider.NoTicks)
        self.verticalSlider_brightness.setObjectName(_fromUtf8("verticalSlider_brightness"))
        self.gridLayout.addWidget(self.verticalSlider_brightness, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_brightness = QtGui.QLabel(Form)
        self.label_brightness.setObjectName(_fromUtf8("label_brightness"))
        self.gridLayout.addWidget(self.label_brightness, 0, 0, 1, 1)
        self.label_frequency = QtGui.QLabel(Form)
        self.label_frequency.setObjectName(_fromUtf8("label_frequency"))
        self.gridLayout.addWidget(self.label_frequency, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.verticalSlider_brightness, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Form.updateBrightness)
        QtCore.QObject.connect(self.verticalSlider_darkness, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Form.updateDarkness)
        QtCore.QObject.connect(self.verticalSlider_frequency, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Form.updateFrequency)
        QtCore.QObject.connect(self.verticalSlider_duty_cycle, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Form.updateDutyCycle)
        QtCore.QObject.connect(self.checkBox_darkness, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Form.updateDarknessCheckbox)
        QtCore.QObject.connect(self.checkBox_shift, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Form.updateDutyCycleShift)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.verticalSlider_brightness, self.verticalSlider_darkness)
        Form.setTabOrder(self.verticalSlider_darkness, self.checkBox_darkness)
        Form.setTabOrder(self.checkBox_darkness, self.verticalSlider_frequency)
        Form.setTabOrder(self.verticalSlider_frequency, self.verticalSlider_duty_cycle)
        Form.setTabOrder(self.verticalSlider_duty_cycle, self.checkBox_shift)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.checkBox_darkness.setText(_translate("Form", "active", None))
        self.label_frequency_value.setText(_translate("Form", "Hz", None))
        self.checkBox_shift.setText(_translate("Form", "shift", None))
        self.label_duty_cycle.setText(_translate("Form", "Duty Cycle", None))
        self.label_darkness.setText(_translate("Form", "Darkness", None))
        self.label_brightness.setText(_translate("Form", "Brightness", None))
        self.label_frequency.setText(_translate("Form", "Frequency", None))

