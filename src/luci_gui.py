import sys
from PyQt4 import QtCore, QtGui

from sliders_widget import Ui_Form


class SlidersForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.updateBrightness = self.updateBrightness

    def updateBrightness(self, brightness):
        print brightness


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    sliders_form = SlidersForm()
    sliders_form.show()
    sys.exit(app.exec_())
