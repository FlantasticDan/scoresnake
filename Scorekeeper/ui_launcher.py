# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcher.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_launcher(object):
    def setupUi(self, launcher):
        if launcher.objectName():
            launcher.setObjectName(u"launcher")
        launcher.setWindowModality(Qt.ApplicationModal)
        launcher.resize(600, 400)
        launcher.setMinimumSize(QSize(600, 400))
        launcher.setMaximumSize(QSize(600, 400))
        icon = QIcon()
        icon.addFile(u":/icons/scoresnake_icon.png", QSize(), QIcon.Normal, QIcon.On)
        launcher.setWindowIcon(icon)
        launcher.setStyleSheet(u"background-color: #3C4148")
        self.visitor_label = QLabel(launcher)
        self.visitor_label.setObjectName(u"visitor_label")
        self.visitor_label.setGeometry(QRect(40, 115, 200, 20))
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.visitor_label.setFont(font)
        self.visitor_label.setStyleSheet(u"color: white;")
        self.visitor_label.setAlignment(Qt.AlignCenter)
        self.visitor_label.setIndent(-1)
        self.visitor_text = QLineEdit(launcher)
        self.visitor_text.setObjectName(u"visitor_text")
        self.visitor_text.setGeometry(QRect(40, 140, 200, 40))
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.visitor_text.setFont(font1)
        self.visitor_text.setStyleSheet(u"QLineEdit{\n"
"	color: white;\n"
"	border: 2px solid #85898f;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.visitor_text.setAlignment(Qt.AlignCenter)
        self.logo_icon = QLabel(launcher)
        self.logo_icon.setObjectName(u"logo_icon")
        self.logo_icon.setGeometry(QRect(260, 20, 75, 75))
        self.logo_icon.setPixmap(QPixmap(u":/icons/scoresnake_icon_light.png"))
        self.logo_icon.setScaledContents(True)
        self.logo_icon.setAlignment(Qt.AlignCenter)
        self.home_text = QLineEdit(launcher)
        self.home_text.setObjectName(u"home_text")
        self.home_text.setGeometry(QRect(360, 140, 200, 40))
        self.home_text.setFont(font1)
        self.home_text.setStyleSheet(u"QLineEdit{\n"
"	color: white;\n"
"	border: 2px solid #85898f;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.home_text.setAlignment(Qt.AlignCenter)
        self.home_label = QLabel(launcher)
        self.home_label.setObjectName(u"home_label")
        self.home_label.setGeometry(QRect(360, 115, 200, 20))
        self.home_label.setFont(font)
        self.home_label.setStyleSheet(u"color: white;")
        self.home_label.setAlignment(Qt.AlignCenter)
        self.home_label.setIndent(-1)
        self.server_label = QLabel(launcher)
        self.server_label.setObjectName(u"server_label")
        self.server_label.setGeometry(QRect(200, 205, 200, 20))
        self.server_label.setFont(font)
        self.server_label.setStyleSheet(u"color: white;")
        self.server_label.setAlignment(Qt.AlignCenter)
        self.server_label.setIndent(-1)
        self.server_ip = QLineEdit(launcher)
        self.server_ip.setObjectName(u"server_ip")
        self.server_ip.setGeometry(QRect(200, 230, 200, 40))
        self.server_ip.setFont(font1)
        self.server_ip.setStyleSheet(u"QLineEdit{\n"
"	color: white;\n"
"	border: 2px solid #85898f;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.server_ip.setAlignment(Qt.AlignCenter)
        self.baseball_button = QPushButton(launcher)
        self.baseball_button.setObjectName(u"baseball_button")
        self.baseball_button.setGeometry(QRect(260, 290, 80, 80))
        self.baseball_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0,0,0,0%);\n"
"	border-image: url(:/icons/baseball_outline.png);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(0,0,0,0%);\n"
"	border-image: url(:/icons/baseball_solid.png);\n"
"	border: 0px;\n"
"}")
        self.baseball_button.setProperty("mask", QPixmap(u":/icons/baseball_mask.png"))

        self.retranslateUi(launcher)

        QMetaObject.connectSlotsByName(launcher)
    # setupUi

    def retranslateUi(self, launcher):
        launcher.setWindowTitle(QCoreApplication.translate("launcher", u"Scoresnake Launcher", None))
        self.visitor_label.setText(QCoreApplication.translate("launcher", u"VISITOR", None))
        self.logo_icon.setText("")
        self.home_label.setText(QCoreApplication.translate("launcher", u"HOME", None))
        self.server_label.setText(QCoreApplication.translate("launcher", u"SERVER IP", None))
#if QT_CONFIG(tooltip)
        self.server_ip.setToolTip(QCoreApplication.translate("launcher", u"IP address of the server running the scorebug.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.baseball_button.setToolTip(QCoreApplication.translate("launcher", u"Launch Baseball Scorekeeper", None))
#endif // QT_CONFIG(tooltip)
        self.baseball_button.setText("")
    # retranslateUi

