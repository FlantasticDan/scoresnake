import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QFontDatabase
from PySide2.QtCore import Qt
from ui_baseball import Ui_Baseball
from scorekeeper import BaseballScorekeeper

class BaseballGUI(QMainWindow):
    def __init__(self):
        super(BaseballGUI, self).__init__()

        # Assign Helper Classes
        self.ui = Ui_Baseball()
        self.keeper = BaseballScorekeeper()

        self.fonts()

        # Draw GUI
        self.ui.setupUi(self)
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

        # Mask Base Toggle Buttons
        self.mask_button(self.ui.base1)
        self.mask_button(self.ui.base2)
        self.mask_button(self.ui.base3)

        # Hide Home Score Buttons
        self.set_home_inactive()
        self.set_visitor_active()


    def mask_button(self, button):
        '''Masks the given button by using the QPixmap in the 'mask' property of the button.'''
        scale = button.property(u'mask').scaled(100, 100)
        mask = scale.mask()
        button.setMask(mask)

    def clear_strikes(self):
        '''Clears the strike indicators.'''
        self.ui.strike1.setVisible(False)
        self.ui.strike2.setVisible(False)

    def clear_balls(self):
        '''Clears the ball indicators.'''
        self.ui.ball1.setVisible(False)
        self.ui.ball2.setVisible(False)
        self.ui.ball3.setVisible(False)

    def clear_count(self):
        '''Clears the ball and strike count indicators.'''
        self.clear_balls()
        self.clear_strikes()

    def clear_outs(self):
        '''Clears the out indicators.'''
        self.ui.out1.setVisible(False)
        self.ui.out2.setVisible(False)
        self.ui.out3.setVisible(False)

    def set_home_inactive(self):
        self.ui.home_plus.setVisible(False)
        self.ui.home_minus.setVisible(False)
        self.ui.home.setEnabled(False)

    def set_home_active(self):
        self.ui.home_plus.setVisible(True)
        self.ui.home_minus.setVisible(True)
        self.ui.home.setEnabled(True)

    def set_visitor_inactive(self):
        self.ui.visitor_plus.setVisible(False)
        self.ui.visitor_minus.setVisible(False)
        self.ui.visitor.setEnabled(False)

    def set_visitor_active(self):
        self.ui.visitor_plus.setVisible(True)
        self.ui.visitor_minus.setVisible(True)
        self.ui.visitor.setEnabled(True)


if __name__ == '__main__':

    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    APP = QApplication(sys.argv)

    WINDOW = BaseballGUI()
    WINDOW.show()

    APP.exec_()