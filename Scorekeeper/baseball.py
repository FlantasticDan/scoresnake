import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QFontDatabase
from PySide2.QtCore import Qt
from ui_baseball import Ui_Baseball

class BaseballGUI(QMainWindow):
    def __init__(self):
        super(BaseballGUI, self).__init__()

        self.UI = Ui_Baseball()

        self.fonts()

        self.UI.setupUi(self)

        self.prepare_ui()

    def fonts(self):
        '''Add fonts to the Qt Font Database.'''
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-Bold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-ExtraBold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-Regular.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-SemiBold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-SemiBold.ttf')

    def prepare_ui(self):
        '''Prepares the UI for the user by solving the shortcomings presented by Qt Designer.'''
        # Clear the Indicator Dots
        self.clear_count()
        self.clear_outs()

        self.mask_button(self.UI.base1)
        self.mask_button(self.UI.base2)
        self.mask_button(self.UI.base3)

    def mask_button(self, button):
        '''Masks the given button by using the QPixmap in the 'mask' property of the button.'''
        scale = button.property(u'mask').scaled(100, 100)
        mask = scale.mask()
        button.setMask(mask)

    def clear_strikes(self):
        '''Clears the strike indicators.'''
        self.UI.strike1.setVisible(False)
        self.UI.strike2.setVisible(False)

    def clear_balls(self):
        '''Clears the ball indicators.'''
        self.UI.ball1.setVisible(False)
        self.UI.ball2.setVisible(False)
        self.UI.ball3.setVisible(False)

    def clear_count(self):
        '''Clears the ball and strike count indicators.'''
        self.clear_balls()
        self.clear_strikes()

    def clear_outs(self):
        '''Clears the out indicators.'''
        self.UI.out1.setVisible(False)
        self.UI.out2.setVisible(False)
        self.UI.out3.setVisible(False)


if __name__ == '__main__':

    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    APP = QApplication(sys.argv)

    WINDOW = BaseballGUI()
    WINDOW.show()

    APP.exec_()