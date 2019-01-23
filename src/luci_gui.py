import sys
from PyQt4 import QtCore, QtGui

from sliders_widget import Ui_Form

import luci


class SlidersForm(QtGui.QWidget):
    def __init__(self, luci_dev='/dev/ttyACM0', parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.luci = luci.Luci(dev=luci_dev)

    def updateBrightness(self, brightness):
        print self.luci.set_brightness(b=brightness)

    def updateDarkness(self, darkness):
        print self.luci.set_darkness(d=darkness)

    def updateFrequency(self, frequency):
        print self.luci.set_frequency(hz=frequency)

    def updateDutyCycle(self, duty_cycle):
        print self.luci.set_duty_cycle(dc=duty_cycle)

    def updateDarknessCheckbox(self, cb):
        if cb:
            darkness = self.ui.verticalSlider_darkness.value()
            print self.luci.set_darkness(d=darkness)
        else:
            print self.luci.set_darkness(d=0)

    def updateDutyCycleShift(self, shift):
        if shift:
            print self.luci.set_phase_shift(s=1)
        else:
            print self.luci.set_phase_shift(s=0)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    sliders_form = SlidersForm()
    sliders_form.show()
    sys.exit(app.exec_())
