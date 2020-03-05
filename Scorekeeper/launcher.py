import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QFontDatabase
from PySide2.QtCore import Qt
from ui_launcher import Ui_launcher
from baseball import BaseballGUI

class ScoresnakeGUI(QMainWindow):
    def __init__(self):
        super(ScoresnakeGUI, self).__init__()

        self.ui = Ui_launcher()

        self.fonts()

        # Draw GUI
        self.ui.setupUi(self)

        # Buttons
        self.mask_button(self.ui.baseball_button)
        self.ui.baseball_button.clicked.connect(self.baseball_button_handler)


    def fonts(self):
        '''Add fonts to the Qt Font Database.'''
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-Bold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-ExtraBold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-Regular.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-SemiBold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-SemiBold.ttf')
    
    def mask_button(self, button):
        '''Masks the given button by using the QPixmap in the 'mask' property of the button.'''
        scale = button.property(u'mask').scaled(80, 80)
        mask = scale.mask()
        button.setMask(mask)
    
    def baseball_button_handler(self):
        kwargs = dict()

        if self.ui.home_text.text() != '':
            kwargs['home'] = self.ui.home_text.text()

        if self.ui.visitor_text.text() != '':
            kwargs['visitor'] = self.ui.visitor_text.text()

        if self.ui.server_ip.text() != '':
            kwargs['serverIP'] = self.ui.server_ip.text()

        baseball = BaseballGUI(**kwargs)

        self.close()

        baseball.show()
        baseball.exec()


if __name__ == '__main__':

    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    APP = QApplication(sys.argv)

    WINDOW = ScoresnakeGUI()
    WINDOW.show()
    sys.exit(APP.exec_())
