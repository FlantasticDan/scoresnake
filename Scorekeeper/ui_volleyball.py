# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'volleyball.ui'
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

class Ui_Volleyball(object):
    def setupUi(self, Volleyball):
        if Volleyball.objectName():
            Volleyball.setObjectName(u"Volleyball")
        Volleyball.resize(790, 460)
        Volleyball.setMinimumSize(QSize(790, 460))
        Volleyball.setMaximumSize(QSize(790, 460))
        icon = QIcon()
        icon.addFile(u":/icons/volleyball_solid.png", QSize(), QIcon.Normal, QIcon.On)
        Volleyball.setWindowIcon(icon)
        Volleyball.setStyleSheet(u"QMainWindow{\n"
"	background-color: #3C4148\n"
"}")
        self.centralwidget = QWidget(Volleyball)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #3C4148")
        self.vistor = QWidget(self.centralwidget)
        self.vistor.setObjectName(u"vistor")
        self.vistor.setGeometry(QRect(80, 30, 190, 275))
        self.visitor_score = QLabel(self.vistor)
        self.visitor_score.setObjectName(u"visitor_score")
        self.visitor_score.setGeometry(QRect(0, 25, 190, 100))
        font = QFont()
        font.setFamily(u"Open Sans Extrabold")
        font.setPointSize(84)
        font.setBold(False)
        font.setWeight(50)
        self.visitor_score.setFont(font)
        self.visitor_score.setStyleSheet(u"color: white")
        self.visitor_score.setScaledContents(False)
        self.visitor_score.setAlignment(Qt.AlignCenter)
        self.visitor_plus = QPushButton(self.vistor)
        self.visitor_plus.setObjectName(u"visitor_plus")
        self.visitor_plus.setGeometry(QRect(50, 135, 140, 40))
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(14)
        font1.setUnderline(False)
        self.visitor_plus.setFont(font1)
        self.visitor_plus.setLayoutDirection(Qt.RightToLeft)
        self.visitor_plus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: #4DA167;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #326742;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #4DA167;\n"
"border: 0px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/plus.png", QSize(), QIcon.Normal, QIcon.On)
        self.visitor_plus.setIcon(icon1)
        self.visitor_plus.setIconSize(QSize(30, 30))
        self.visitor_plus.setFlat(False)
        self.visitor_name = QLabel(self.vistor)
        self.visitor_name.setObjectName(u"visitor_name")
        self.visitor_name.setGeometry(QRect(0, -5, 190, 30))
        font2 = QFont()
        font2.setFamily(u"Open Sans")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.visitor_name.setFont(font2)
        self.visitor_name.setStyleSheet(u"color: white;")
        self.visitor_name.setScaledContents(False)
        self.visitor_name.setAlignment(Qt.AlignCenter)
        self.visitor_minus = QPushButton(self.vistor)
        self.visitor_minus.setObjectName(u"visitor_minus")
        self.visitor_minus.setEnabled(True)
        self.visitor_minus.setGeometry(QRect(0, 135, 40, 40))
        self.visitor_minus.setLayoutDirection(Qt.LeftToRight)
        self.visitor_minus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #DB4848;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #DB4848;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #8C2E2E;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #81858A;\n"
"border: 0px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/minus.png", QSize(), QIcon.Normal, QIcon.On)
        self.visitor_minus.setIcon(icon2)
        self.visitor_minus.setIconSize(QSize(30, 30))
        self.visitor_minus.setFlat(False)
        self.visitor_sets = QLabel(self.vistor)
        self.visitor_sets.setObjectName(u"visitor_sets")
        self.visitor_sets.setGeometry(QRect(0, 210, 190, 60))
        font3 = QFont()
        font3.setFamily(u"Open Sans Extrabold")
        font3.setPointSize(42)
        font3.setBold(False)
        font3.setWeight(50)
        self.visitor_sets.setFont(font3)
        self.visitor_sets.setStyleSheet(u"color: white")
        self.visitor_sets.setScaledContents(False)
        self.visitor_sets.setAlignment(Qt.AlignCenter)
        self.visitor_sets.setMargin(0)
        self.visitor_sets.setIndent(0)
        self.visitor_sets_minus = QPushButton(self.vistor)
        self.visitor_sets_minus.setObjectName(u"visitor_sets_minus")
        self.visitor_sets_minus.setGeometry(QRect(10, 220, 40, 40))
        self.visitor_sets_minus.setLayoutDirection(Qt.LeftToRight)
        self.visitor_sets_minus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #DB4848;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #DB4848;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #8C2E2E;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #81858A;\n"
"border: 0px;\n"
"}\n"
"")
        self.visitor_sets_minus.setIcon(icon2)
        self.visitor_sets_minus.setIconSize(QSize(30, 30))
        self.visitor_sets_minus.setFlat(False)
        self.visitor_sets_plus = QPushButton(self.vistor)
        self.visitor_sets_plus.setObjectName(u"visitor_sets_plus")
        self.visitor_sets_plus.setGeometry(QRect(140, 220, 40, 40))
        self.visitor_sets_plus.setLayoutDirection(Qt.LeftToRight)
        self.visitor_sets_plus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #4DA167;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #4DA167;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #326742;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.visitor_sets_plus.setIcon(icon1)
        self.visitor_sets_plus.setIconSize(QSize(30, 30))
        self.visitor_sets_plus.setFlat(False)
        self.visitor_sets_label = QLabel(self.vistor)
        self.visitor_sets_label.setObjectName(u"visitor_sets_label")
        self.visitor_sets_label.setGeometry(QRect(0, 185, 190, 20))
        font4 = QFont()
        font4.setFamily(u"Open Sans")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        font4.setKerning(True)
        self.visitor_sets_label.setFont(font4)
        self.visitor_sets_label.setStyleSheet(u"color: white;")
        self.visitor_sets_label.setScaledContents(False)
        self.visitor_sets_label.setAlignment(Qt.AlignCenter)
        self.home = QWidget(self.centralwidget)
        self.home.setObjectName(u"home")
        self.home.setGeometry(QRect(520, 30, 190, 275))
        self.home_score = QLabel(self.home)
        self.home_score.setObjectName(u"home_score")
        self.home_score.setGeometry(QRect(0, 25, 190, 100))
        self.home_score.setFont(font)
        self.home_score.setStyleSheet(u"color: white")
        self.home_score.setScaledContents(False)
        self.home_score.setAlignment(Qt.AlignCenter)
        self.home_plus = QPushButton(self.home)
        self.home_plus.setObjectName(u"home_plus")
        self.home_plus.setGeometry(QRect(50, 135, 140, 40))
        self.home_plus.setFont(font1)
        self.home_plus.setLayoutDirection(Qt.RightToLeft)
        self.home_plus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: #4DA167;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #326742;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #4DA167;\n"
"border: 0px;\n"
"}\n"
"")
        self.home_plus.setIcon(icon1)
        self.home_plus.setIconSize(QSize(30, 30))
        self.home_plus.setFlat(False)
        self.home_name = QLabel(self.home)
        self.home_name.setObjectName(u"home_name")
        self.home_name.setGeometry(QRect(0, -5, 190, 30))
        self.home_name.setFont(font2)
        self.home_name.setStyleSheet(u"color: white;")
        self.home_name.setScaledContents(False)
        self.home_name.setAlignment(Qt.AlignCenter)
        self.home_minus = QPushButton(self.home)
        self.home_minus.setObjectName(u"home_minus")
        self.home_minus.setEnabled(True)
        self.home_minus.setGeometry(QRect(0, 135, 40, 40))
        self.home_minus.setLayoutDirection(Qt.LeftToRight)
        self.home_minus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #DB4848;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #DB4848;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #8C2E2E;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #81858A;\n"
"border: 0px;\n"
"}\n"
"")
        self.home_minus.setIcon(icon2)
        self.home_minus.setIconSize(QSize(30, 30))
        self.home_minus.setFlat(False)
        self.home_sets = QLabel(self.home)
        self.home_sets.setObjectName(u"home_sets")
        self.home_sets.setGeometry(QRect(0, 210, 190, 60))
        self.home_sets.setFont(font3)
        self.home_sets.setStyleSheet(u"color: white")
        self.home_sets.setScaledContents(False)
        self.home_sets.setAlignment(Qt.AlignCenter)
        self.home_sets.setMargin(0)
        self.home_sets.setIndent(0)
        self.home_sets_minus = QPushButton(self.home)
        self.home_sets_minus.setObjectName(u"home_sets_minus")
        self.home_sets_minus.setGeometry(QRect(10, 220, 40, 40))
        self.home_sets_minus.setLayoutDirection(Qt.LeftToRight)
        self.home_sets_minus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #DB4848;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #DB4848;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #8C2E2E;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #81858A;\n"
"border: 0px;\n"
"}\n"
"")
        self.home_sets_minus.setIcon(icon2)
        self.home_sets_minus.setIconSize(QSize(30, 30))
        self.home_sets_minus.setFlat(False)
        self.home_sets_plus = QPushButton(self.home)
        self.home_sets_plus.setObjectName(u"home_sets_plus")
        self.home_sets_plus.setGeometry(QRect(140, 220, 40, 40))
        self.home_sets_plus.setLayoutDirection(Qt.LeftToRight)
        self.home_sets_plus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #4DA167;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #4DA167;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #326742;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.home_sets_plus.setIcon(icon1)
        self.home_sets_plus.setIconSize(QSize(30, 30))
        self.home_sets_plus.setFlat(False)
        self.home_sets_label = QLabel(self.home)
        self.home_sets_label.setObjectName(u"home_sets_label")
        self.home_sets_label.setGeometry(QRect(0, 185, 190, 20))
        self.home_sets_label.setFont(font4)
        self.home_sets_label.setStyleSheet(u"color: white;")
        self.home_sets_label.setScaledContents(False)
        self.home_sets_label.setAlignment(Qt.AlignCenter)
        self.home_sets.raise_()
        self.home_score.raise_()
        self.home_plus.raise_()
        self.home_name.raise_()
        self.home_minus.raise_()
        self.home_sets_minus.raise_()
        self.home_sets_plus.raise_()
        self.home_sets_label.raise_()
        self.sets = QWidget(self.centralwidget)
        self.sets.setObjectName(u"sets")
        self.sets.setGeometry(QRect(300, 128, 190, 80))
        self.set_plus = QPushButton(self.sets)
        self.set_plus.setObjectName(u"set_plus")
        self.set_plus.setGeometry(QRect(140, 30, 40, 40))
        self.set_plus.setLayoutDirection(Qt.LeftToRight)
        self.set_plus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #4DA167;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #4DA167;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #326742;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #81858A;\n"
"border: 0px;\n"
"}\n"
"")
        self.set_plus.setIcon(icon1)
        self.set_plus.setIconSize(QSize(30, 30))
        self.set_plus.setFlat(False)
        self.set_label = QLabel(self.sets)
        self.set_label.setObjectName(u"set_label")
        self.set_label.setGeometry(QRect(0, -5, 190, 31))
        self.set_label.setFont(font4)
        self.set_label.setStyleSheet(u"color: white;")
        self.set_label.setScaledContents(False)
        self.set_label.setAlignment(Qt.AlignCenter)
        self.set_minus = QPushButton(self.sets)
        self.set_minus.setObjectName(u"set_minus")
        self.set_minus.setGeometry(QRect(10, 30, 40, 40))
        self.set_minus.setLayoutDirection(Qt.LeftToRight)
        self.set_minus.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #DB4848;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #DB4848;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #8C2E2E;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #81858A;\n"
"border: 0px;\n"
"}\n"
"")
        self.set_minus.setIcon(icon2)
        self.set_minus.setIconSize(QSize(30, 30))
        self.set_minus.setFlat(False)
        self.set = QLabel(self.sets)
        self.set.setObjectName(u"set")
        self.set.setGeometry(QRect(0, 20, 190, 60))
        self.set.setFont(font3)
        self.set.setStyleSheet(u"color: white")
        self.set.setScaledContents(False)
        self.set.setAlignment(Qt.AlignCenter)
        self.set.setMargin(0)
        self.set.setIndent(0)
        self.set.raise_()
        self.set_plus.raise_()
        self.set_label.raise_()
        self.set_minus.raise_()
        self.bestof = QWidget(self.centralwidget)
        self.bestof.setObjectName(u"bestof")
        self.bestof.setGeometry(QRect(270, 350, 90, 70))
        self.bestof_5 = QPushButton(self.bestof)
        self.bestof_5.setObjectName(u"bestof_5")
        self.bestof_5.setGeometry(QRect(50, 30, 40, 40))
        font5 = QFont()
        font5.setFamily(u"Open Sans SemiBold")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.bestof_5.setFont(font5)
        self.bestof_5.setLayoutDirection(Qt.LeftToRight)
        self.bestof_5.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #9d44b5;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:on{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.bestof_5.setIconSize(QSize(30, 30))
        self.bestof_5.setCheckable(False)
        self.bestof_5.setChecked(False)
        self.bestof_5.setFlat(False)
        self.bestof_label = QLabel(self.bestof)
        self.bestof_label.setObjectName(u"bestof_label")
        self.bestof_label.setGeometry(QRect(0, 0, 90, 30))
        self.bestof_label.setFont(font4)
        self.bestof_label.setStyleSheet(u"color: white;")
        self.bestof_label.setScaledContents(False)
        self.bestof_label.setAlignment(Qt.AlignCenter)
        self.bestof_3 = QPushButton(self.bestof)
        self.bestof_3.setObjectName(u"bestof_3")
        self.bestof_3.setEnabled(True)
        self.bestof_3.setGeometry(QRect(0, 30, 40, 40))
        self.bestof_3.setFont(font5)
        self.bestof_3.setLayoutDirection(Qt.LeftToRight)
        self.bestof_3.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #9d44b5;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:on{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.bestof_3.setIconSize(QSize(30, 30))
        self.bestof_3.setCheckable(False)
        self.bestof_3.setFlat(False)
        self.points = QWidget(self.centralwidget)
        self.points.setObjectName(u"points")
        self.points.setGeometry(QRect(420, 350, 90, 70))
        self.pts_25 = QPushButton(self.points)
        self.pts_25.setObjectName(u"pts_25")
        self.pts_25.setEnabled(True)
        self.pts_25.setGeometry(QRect(50, 30, 40, 40))
        self.pts_25.setFont(font5)
        self.pts_25.setLayoutDirection(Qt.LeftToRight)
        self.pts_25.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #9d44b5;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:on{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.pts_25.setIconSize(QSize(30, 30))
        self.pts_25.setCheckable(False)
        self.pts_25.setChecked(False)
        self.pts_25.setFlat(False)
        self.pts_label = QLabel(self.points)
        self.pts_label.setObjectName(u"pts_label")
        self.pts_label.setGeometry(QRect(0, 0, 90, 30))
        self.pts_label.setFont(font4)
        self.pts_label.setStyleSheet(u"color: white;")
        self.pts_label.setScaledContents(False)
        self.pts_label.setAlignment(Qt.AlignCenter)
        self.pts_15 = QPushButton(self.points)
        self.pts_15.setObjectName(u"pts_15")
        self.pts_15.setGeometry(QRect(0, 30, 40, 40))
        self.pts_15.setFont(font5)
        self.pts_15.setLayoutDirection(Qt.LeftToRight)
        self.pts_15.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 5px solid #9d44b5;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:on{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #9d44b5;\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"")
        self.pts_15.setIconSize(QSize(30, 30))
        self.pts_15.setCheckable(False)
        self.pts_15.setFlat(False)
        Volleyball.setCentralWidget(self.centralwidget)

        self.retranslateUi(Volleyball)

        self.visitor_plus.setDefault(False)
        self.visitor_minus.setDefault(False)
        self.visitor_sets_minus.setDefault(False)
        self.visitor_sets_plus.setDefault(False)
        self.home_plus.setDefault(False)
        self.home_minus.setDefault(False)
        self.home_sets_minus.setDefault(False)
        self.home_sets_plus.setDefault(False)
        self.set_plus.setDefault(False)
        self.set_minus.setDefault(False)
        self.bestof_5.setDefault(False)
        self.bestof_3.setDefault(False)
        self.pts_25.setDefault(False)
        self.pts_15.setDefault(False)


        QMetaObject.connectSlotsByName(Volleyball)
    # setupUi

    def retranslateUi(self, Volleyball):
        Volleyball.setWindowTitle(QCoreApplication.translate("Volleyball", u"Volleyball Scorekeeper", None))
        self.visitor_score.setText(QCoreApplication.translate("Volleyball", u"0", None))
        self.visitor_plus.setText(QCoreApplication.translate("Volleyball", u"Add Point", None))
        self.visitor_name.setText(QCoreApplication.translate("Volleyball", u"VISITOR", None))
        self.visitor_minus.setText("")
        self.visitor_sets.setText(QCoreApplication.translate("Volleyball", u"0", None))
        self.visitor_sets_minus.setText("")
        self.visitor_sets_plus.setText("")
        self.visitor_sets_label.setText(QCoreApplication.translate("Volleyball", u"SETS WON", None))
        self.home_score.setText(QCoreApplication.translate("Volleyball", u"0", None))
        self.home_plus.setText(QCoreApplication.translate("Volleyball", u"Add Point", None))
        self.home_name.setText(QCoreApplication.translate("Volleyball", u"HOME", None))
        self.home_minus.setText("")
        self.home_sets.setText(QCoreApplication.translate("Volleyball", u"0", None))
        self.home_sets_minus.setText("")
        self.home_sets_plus.setText("")
        self.home_sets_label.setText(QCoreApplication.translate("Volleyball", u"SETS WON", None))
        self.set_plus.setText("")
        self.set_label.setText(QCoreApplication.translate("Volleyball", u"SET", None))
        self.set_minus.setText("")
        self.set.setText(QCoreApplication.translate("Volleyball", u"0", None))
        self.bestof_5.setText(QCoreApplication.translate("Volleyball", u"5", None))
        self.bestof_label.setText(QCoreApplication.translate("Volleyball", u"BEST OF", None))
        self.bestof_3.setText(QCoreApplication.translate("Volleyball", u"3", None))
        self.pts_25.setText(QCoreApplication.translate("Volleyball", u"25", None))
        self.pts_label.setText(QCoreApplication.translate("Volleyball", u"POINTS", None))
        self.pts_15.setText(QCoreApplication.translate("Volleyball", u"15", None))
    # retranslateUi

