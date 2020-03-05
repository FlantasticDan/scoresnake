'''GUI for Baseball Scorkeeping'''

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QFontDatabase
from PySide2.QtCore import Qt
from ui_baseball import Ui_Baseball
from scorekeeper import BaseballScorekeeper

class BaseballGUI(QMainWindow):
    def __init__(self, home='home', visitor='visitor', serverIP='127.0.0.1', debug=False):
        super(BaseballGUI, self).__init__()

        # Assign Helper Classes
        self.ui = Ui_Baseball()
        self.keeper = BaseballScorekeeper(serverIP=serverIP)

        if debug:
            self.fonts()

        # Draw GUI
        self.ui.setupUi(self)
        self.prepare_ui()

        self.update()
        self.connect_buttons()

        self.ui.home_name.setText(home.upper())
        self.ui.visitor_name.setText(visitor.upper())

    def closeEvent(self, event):
        self.keeper.server.stop_heartbeat()

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

    def update(self):
        '''Update the UI with the data from the authoratative scorekeeper.'''

        # Scores
        self.ui.home_score.setText(str(self.keeper.home))
        self.ui.visitor_score.setText(str(self.keeper.visitor))
        self.ui.home_minus.setEnabled(bool(self.keeper.home))
        self.ui.visitor_minus.setEnabled(bool(self.keeper.visitor))

        # Inning
        self.ui.inning_number.setText(str(self.keeper.inning))
        self.ui.inning_top.setEnabled(not self.keeper.top)
        self.ui.inning_bottom.setEnabled(not self.keeper.bottom)
        if self.keeper.top:
            self.set_visitor_active()
            self.set_home_inactive()
        elif self.keeper.bottom:
            self.set_home_active()
            self.set_visitor_inactive()
        self.ui.inning_minus.setEnabled(bool(self.keeper.inning - 1))

        # Count
        if self.keeper.strikes > 0:
            self.ui.strike1.setVisible(True)
            if self.keeper.strikes > 1:
                self.ui.strike2.setVisible(True)
            else:
                self.ui.strike2.setVisible(False)
        else:
            self.clear_strikes()

        if self.keeper.balls > 0:
            self.ui.ball1.setVisible(True)
            if self.keeper.balls > 1:
                self.ui.ball2.setVisible(True)
                if self.keeper.balls > 2:
                    self.ui.ball3.setVisible(True)
                else:
                    self.ui.ball3.setVisible(False)
            else:
                self.ui.ball2.setVisible(False)
                self.ui.ball3.setVisible(False)
        else:
            self.clear_balls()

        self.ui.balls_minus.setEnabled(bool(self.keeper.balls))
        self.ui.strike_minus.setEnabled(bool(self.keeper.strikes))

        # Outs
        if self.keeper.outs > 0:
            self.ui.out1.setVisible(True)
            if self.keeper.outs > 1:
                self.ui.out2.setVisible(True)
            else:
                self.ui.out2.setVisible(False)
        else:
            self.clear_outs()
        self.ui.out_minus.setEnabled(bool(self.keeper.outs))

        # Bases
        self.ui.base1.setChecked(self.keeper.base1)
        self.ui.base2.setChecked(self.keeper.base2)
        self.ui.base3.setChecked(self.keeper.base3)

    def connect_buttons(self):
        '''Connect QButtons to their handlers.'''
        # Scoring Buttons
        self.ui.home_plus.clicked.connect(self.score_handler)
        self.ui.visitor_plus.clicked.connect(self.score_handler)
        self.ui.home_minus.clicked.connect(self.minus_score_handler)
        self.ui.visitor_minus.clicked.connect(self.minus_score_handler)

        # Inning Buttons
        self.ui.inning_plus.clicked.connect(self.add_inning_handler)
        self.ui.inning_minus.clicked.connect(self.minus_inning_handler)
        self.ui.inning_top.clicked.connect(self.top_inning_handler)
        self.ui.inning_bottom.clicked.connect(self.bottom_inning_handler)

        # Count Buttons
        self.ui.balls_add.clicked.connect(self.ball_handler)
        self.ui.balls_minus.clicked.connect(self.minus_ball_handler)
        self.ui.strikes_add.clicked.connect(self.strike_handler)
        self.ui.strike_minus.clicked.connect(self.minus_strike_handler)
        self.ui.reset_count.clicked.connect(self.reset_count_handler)

        # Outs
        self.ui.out_plus.clicked.connect(self.out_handler)
        self.ui.out_minus.clicked.connect(self.minus_out_handler)
        self.ui.reset_outs.clicked.connect(self.reset_outs_handler)

        # Bases
        self.ui.base1.clicked.connect(self.base1_handler)
        self.ui.base2.clicked.connect(self.base2_handler)
        self.ui.base3.clicked.connect(self.base3_handler)
        self.ui.reset_bases.clicked.connect(self.reset_bases_handler)

    def score_handler(self):
        self.keeper.score()
        self.update()

    def minus_score_handler(self):
        self.keeper.minus_score()
        self.update()

    def add_inning_handler(self):
        self.keeper.new_inning()
        self.update()

    def minus_inning_handler(self):
        self.keeper.old_inning()
        self.update()

    def top_inning_handler(self):
        self.keeper.top_inning()
        self.update()

    def bottom_inning_handler(self):
        self.keeper.bottom_inning()
        self.update()

    def ball_handler(self):
        self.keeper.ball()
        self.update()

    def minus_ball_handler(self):
        self.keeper.minus_ball()
        self.update()

    def strike_handler(self):
        self.keeper.strike()
        self.update()

    def minus_strike_handler(self):
        self.keeper.minus_strike()
        self.update()

    def reset_count_handler(self):
        self.keeper.reset_count()
        self.update()

    def out_handler(self):
        self.keeper.out()
        self.update()

    def minus_out_handler(self):
        self.keeper.minus_out()
        self.update()

    def reset_outs_handler(self):
        self.keeper.reset_outs()
        self.update()

    def base1_handler(self):
        self.keeper.base1_toggle()
        self.update()

    def base2_handler(self):
        self.keeper.base2_toggle()
        self.update()

    def base3_handler(self):
        self.keeper.base3_toggle()
        self.update()

    def reset_bases_handler(self):
        self.keeper.reset_bases()
        self.update()


if __name__ == '__main__':

    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    APP = QApplication(sys.argv)

    WINDOW = BaseballGUI(debug=True)
    WINDOW.show()

    APP.exec_()
