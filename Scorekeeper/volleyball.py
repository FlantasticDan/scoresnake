'''GUI for Volleyball Scorkeeping'''

import sys
import keyboard
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QFontDatabase
from PySide2.QtCore import Qt
from ui_volleyball import Ui_Volleyball
from scorekeeper import VolleyballScorekeeper

class VolleyballGUI(QMainWindow):
    def __init__(self, home='home', visitor='visitor', serverIP='127.0.0.1', debug=False):
        super(VolleyballGUI, self).__init__()

        # Assign Helper Classes
        self.ui = Ui_Volleyball()
        self.keeper = VolleyballScorekeeper(serverIP=serverIP)

        if debug:
            self.fonts()

        # Draw GUI
        self.ui.setupUi(self)

        self.update()
        self.connect_buttons()
        # self.add_keyboard_hooks()

        self.ui.home_name.setText(home.upper())
        self.ui.visitor_name.setText(visitor.upper())

    def closeEvent(self, event):
        self.keeper.server.stop_heartbeat()
        # keyboard.unhook_all_hotkeys()

    def fonts(self):
        '''Add fonts to the Qt Font Database.'''
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-Bold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-ExtraBold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-Regular.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-SemiBold.ttf')
        QFontDatabase.addApplicationFont(u':/fonts/OpenSans-SemiBold.ttf')

    def update(self):
        '''Update the UI with the data from the authoratative scorekeeper.'''

        # Scores
        self.ui.home_score.setText(str(self.keeper.home))
        self.ui.visitor_score.setText(str(self.keeper.visitor))
        if self.keeper.home == 0:
            self.ui.home_minus.setEnabled(False)
        else:
            self.ui.home_minus.setEnabled(True)
        if self.keeper.visitor == 0:
            self.ui.visitor_minus.setEnabled(False)
        else:
            self.ui.visitor_minus.setEnabled(True)

        # Sets
        self.ui.set.setText(str(self.keeper.set))
        if self.keeper.set == 1:
            self.ui.set_minus.setEnabled(False)
            self.ui.set_plus.setEnabled(True)
        elif self.keeper.set == self.keeper.bestof:
            self.ui.set_plus.setEnabled(False)
            self.ui.set_minus.setEnabled(True)
        else:
            self.ui.set_minus.setEnabled(True)
            self.ui.set_plus.setEnabled(True)
        self.ui.home_sets.setText(str(self.keeper.home_sets))
        self.ui.visitor_sets.setText(str(self.keeper.visitor_sets))
        if self.keeper.visitor_sets == 0:
            self.ui.visitor_sets_minus.setEnabled(False)
        else:
            self.ui.visitor_sets_minus.setEnabled(True)
        if self.keeper.home_sets == 0:
            self.ui.home_sets_minus.setEnabled(False)
        else:
            self.ui.home_sets_minus.setEnabled(True)
        
        # Toggles
        if self.keeper.bestof == 5:
            self.ui.bestof_5.setEnabled(False)
            self.ui.bestof_3.setEnabled(True)
        elif self.keeper.bestof == 3:
            self.ui.bestof_5.setEnabled(True)
            self.ui.bestof_3.setEnabled(False)
        
        if self.keeper.points == 25:
            self.ui.pts_25.setEnabled(False)
            self.ui.pts_15.setEnabled(True)
        elif self.keeper.points == 15:
            self.ui.pts_25.setEnabled(True)
            self.ui.pts_15.setEnabled(False)

    def connect_buttons(self):
        # Scoring
        self.ui.visitor_plus.clicked.connect(self.visitor_score_handler)
        self.ui.visitor_minus.clicked.connect(self.minus_visitor_score_handler)
        self.ui.home_plus.clicked.connect(self.home_score_handler)
        self.ui.home_minus.clicked.connect(self.minus_home_score_handler)

        # Sets
        self.ui.visitor_sets_plus.clicked.connect(self.visitor_set_handler)
        self.ui.visitor_sets_minus.clicked.connect(self.minus_visitor_set_handler)
        self.ui.home_sets_plus.clicked.connect(self.home_set_handler)
        self.ui.home_sets_minus.clicked.connect(self.minus_home_set_handler)
        self.ui.set_plus.clicked.connect(self.set_handler)
        self.ui.set_minus.clicked.connect(self.minus_set_handler)

        # Toggles
        self.ui.bestof_3.clicked.connect(self.bestof_3_handler)
        self.ui.bestof_5.clicked.connect(self.bestof_5_handler)
        self.ui.pts_15.clicked.connect(self.points_15_handler)
        self.ui.pts_25.clicked.connect(self.points_25_handler)


    def home_score_handler(self):
        self.keeper.home_score()
        self.update()

    def minus_home_score_handler(self):
        self.keeper.minus_home_score()
        self.update()

    def visitor_score_handler(self):
        self.keeper.visitor_score()
        self.update()

    def minus_visitor_score_handler(self):
        self.keeper.minus_visitor_score()
        self.update()

    def visitor_set_handler(self):
        self.keeper.vistor_set()
        self.update()

    def minus_visitor_set_handler(self):
        self.keeper.minus_vistor_set()
        self.update()

    def home_set_handler(self):
        self.keeper.home_set()
        self.update()

    def minus_home_set_handler(self):
        self.keeper.minus_home_set()
        self.update()

    def set_handler(self):
        self.keeper.new_set()
        self.update()

    def minus_set_handler(self):
        self.keeper.last_set()
        self.update()

    def bestof_3_handler(self):
        self.keeper.change_bestof_3()
        self.update()

    def bestof_5_handler(self):
        self.keeper.change_bestof_5()
        self.update()
    
    def points_15_handler(self):
        self.keeper.change_points_15()
        self.update()
    
    def points_25_handler(self):
        self.keeper.change_points_25()
        self.update()

if __name__ == '__main__':

    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    APP = QApplication(sys.argv)

    WINDOW = VolleyballGUI(debug=True)
    WINDOW.show()

    APP.exec_()