# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'baseball.ui'
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

class Ui_Baseball(object):
    def setupUi(self, Baseball):
        if Baseball.objectName():
            Baseball.setObjectName(u"Baseball")
        Baseball.resize(790, 460)
        Baseball.setMinimumSize(QSize(790, 460))
        Baseball.setMaximumSize(QSize(790, 460))
        Baseball.setStyleSheet(u"QMainWindow{\n"
"	background-color: #3C4148\n"
"}")
        self.centralwidget = QWidget(Baseball)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #3C4148")
        self.hud = QWidget(self.centralwidget)
        self.hud.setObjectName(u"hud")
        self.hud.setGeometry(QRect(30, 260, 730, 170))
        self.count = QWidget(self.hud)
        self.count.setObjectName(u"count")
        self.count.setGeometry(QRect(0, 0, 320, 171))
        self.strikes = QWidget(self.count)
        self.strikes.setObjectName(u"strikes")
        self.strikes.setGeometry(QRect(170, 0, 150, 120))
        self.strikes_label = QLabel(self.strikes)
        self.strikes_label.setObjectName(u"strikes_label")
        self.strikes_label.setGeometry(QRect(0, 0, 150, 30))
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.strikes_label.setFont(font)
        self.strikes_label.setStyleSheet(u"color: white;")
        self.strikes_label.setScaledContents(False)
        self.strikes_label.setAlignment(Qt.AlignCenter)
        self.strike1_bg = QLabel(self.strikes)
        self.strike1_bg.setObjectName(u"strike1_bg")
        self.strike1_bg.setGeometry(QRect(17, 30, 50, 50))
        self.strike1_bg.setAutoFillBackground(False)
        self.strike1_bg.setStyleSheet(u"")
        self.strike1_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.strike1_bg.setScaledContents(True)
        self.strike1_bg.setMargin(8)
        self.strike2_bg = QLabel(self.strikes)
        self.strike2_bg.setObjectName(u"strike2_bg")
        self.strike2_bg.setGeometry(QRect(83, 30, 50, 50))
        self.strike2_bg.setAutoFillBackground(False)
        self.strike2_bg.setStyleSheet(u"")
        self.strike2_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.strike2_bg.setScaledContents(True)
        self.strike2_bg.setMargin(8)
        self.strike2 = QLabel(self.strikes)
        self.strike2.setObjectName(u"strike2")
        self.strike2.setGeometry(QRect(83, 30, 50, 50))
        self.strike2.setAutoFillBackground(False)
        self.strike2.setStyleSheet(u"")
        self.strike2.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.strike2.setScaledContents(True)
        self.strike2.setMargin(8)
        self.strike1 = QLabel(self.strikes)
        self.strike1.setObjectName(u"strike1")
        self.strike1.setEnabled(True)
        self.strike1.setGeometry(QRect(17, 30, 50, 50))
        self.strike1.setAutoFillBackground(False)
        self.strike1.setStyleSheet(u"")
        self.strike1.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.strike1.setScaledContents(True)
        self.strike1.setMargin(8)
        self.strikes_add = QPushButton(self.strikes)
        self.strikes_add.setObjectName(u"strikes_add")
        self.strikes_add.setGeometry(QRect(50, 80, 100, 40))
        font1 = QFont()
        font1.setFamily(u"Open Sans")
        font1.setPointSize(14)
        font1.setUnderline(False)
        self.strikes_add.setFont(font1)
        self.strikes_add.setLayoutDirection(Qt.RightToLeft)
        self.strikes_add.setStyleSheet(u"QPushButton{\n"
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
        self.strikes_add.setIconSize(QSize(30, 30))
        self.strikes_add.setFlat(False)
        self.strike_minus = QPushButton(self.strikes)
        self.strike_minus.setObjectName(u"strike_minus")
        self.strike_minus.setGeometry(QRect(0, 80, 40, 40))
        self.strike_minus.setLayoutDirection(Qt.LeftToRight)
        self.strike_minus.setStyleSheet(u"QPushButton{\n"
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
"}")
        icon = QIcon()
        icon.addFile(u":/icons/minus.png", QSize(), QIcon.Normal, QIcon.On)
        self.strike_minus.setIcon(icon)
        self.strike_minus.setIconSize(QSize(30, 30))
        self.strike_minus.setFlat(False)
        self.balls = QWidget(self.count)
        self.balls.setObjectName(u"balls")
        self.balls.setGeometry(QRect(0, 0, 150, 120))
        self.balls_label = QLabel(self.balls)
        self.balls_label.setObjectName(u"balls_label")
        self.balls_label.setGeometry(QRect(0, 0, 150, 30))
        self.balls_label.setFont(font)
        self.balls_label.setStyleSheet(u"color: white;")
        self.balls_label.setScaledContents(False)
        self.balls_label.setAlignment(Qt.AlignCenter)
        self.ball1_bg = QLabel(self.balls)
        self.ball1_bg.setObjectName(u"ball1_bg")
        self.ball1_bg.setGeometry(QRect(0, 30, 50, 50))
        self.ball1_bg.setAutoFillBackground(False)
        self.ball1_bg.setStyleSheet(u"")
        self.ball1_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.ball1_bg.setScaledContents(True)
        self.ball1_bg.setMargin(8)
        self.ball2_bg = QLabel(self.balls)
        self.ball2_bg.setObjectName(u"ball2_bg")
        self.ball2_bg.setGeometry(QRect(50, 30, 50, 50))
        self.ball2_bg.setAutoFillBackground(False)
        self.ball2_bg.setStyleSheet(u"")
        self.ball2_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.ball2_bg.setScaledContents(True)
        self.ball2_bg.setMargin(8)
        self.ball3_bg = QLabel(self.balls)
        self.ball3_bg.setObjectName(u"ball3_bg")
        self.ball3_bg.setGeometry(QRect(100, 30, 50, 50))
        self.ball3_bg.setAutoFillBackground(False)
        self.ball3_bg.setStyleSheet(u"")
        self.ball3_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.ball3_bg.setScaledContents(True)
        self.ball3_bg.setMargin(8)
        self.ball2 = QLabel(self.balls)
        self.ball2.setObjectName(u"ball2")
        self.ball2.setEnabled(True)
        self.ball2.setGeometry(QRect(50, 30, 50, 50))
        self.ball2.setAutoFillBackground(False)
        self.ball2.setStyleSheet(u"")
        self.ball2.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.ball2.setScaledContents(True)
        self.ball2.setMargin(8)
        self.ball3 = QLabel(self.balls)
        self.ball3.setObjectName(u"ball3")
        self.ball3.setEnabled(True)
        self.ball3.setGeometry(QRect(100, 30, 50, 50))
        self.ball3.setAutoFillBackground(False)
        self.ball3.setStyleSheet(u"")
        self.ball3.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.ball3.setScaledContents(True)
        self.ball3.setMargin(8)
        self.ball1 = QLabel(self.balls)
        self.ball1.setObjectName(u"ball1")
        self.ball1.setEnabled(True)
        self.ball1.setGeometry(QRect(0, 30, 50, 50))
        self.ball1.setAutoFillBackground(False)
        self.ball1.setStyleSheet(u"")
        self.ball1.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.ball1.setScaledContents(True)
        self.ball1.setMargin(8)
        self.balls_add = QPushButton(self.balls)
        self.balls_add.setObjectName(u"balls_add")
        self.balls_add.setGeometry(QRect(50, 80, 100, 40))
        self.balls_add.setFont(font1)
        self.balls_add.setLayoutDirection(Qt.RightToLeft)
        self.balls_add.setStyleSheet(u"QPushButton{\n"
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
        self.balls_add.setIconSize(QSize(30, 30))
        self.balls_add.setFlat(False)
        self.balls_minus = QPushButton(self.balls)
        self.balls_minus.setObjectName(u"balls_minus")
        self.balls_minus.setGeometry(QRect(0, 80, 40, 40))
        self.balls_minus.setLayoutDirection(Qt.LeftToRight)
        self.balls_minus.setStyleSheet(u"QPushButton{\n"
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
"\n"
"")
        self.balls_minus.setIcon(icon)
        self.balls_minus.setIconSize(QSize(30, 30))
        self.balls_minus.setFlat(False)
        self.reset_count = QPushButton(self.count)
        self.reset_count.setObjectName(u"reset_count")
        self.reset_count.setGeometry(QRect(0, 130, 320, 40))
        font2 = QFont()
        font2.setFamily(u"Open Sans")
        font2.setPointSize(14)
        self.reset_count.setFont(font2)
        self.reset_count.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: #507DBC;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #2C4567;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #507DBC;\n"
"border: 0px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/refresh.png", QSize(), QIcon.Normal, QIcon.On)
        self.reset_count.setIcon(icon1)
        self.reset_count.setIconSize(QSize(28, 28))
        self.bases = QWidget(self.hud)
        self.bases.setObjectName(u"bases")
        self.bases.setGeometry(QRect(510, 0, 220, 170))
        self.base1 = QPushButton(self.bases)
        self.base1.setObjectName(u"base1")
        self.base1.setGeometry(QRect(120, 60, 100, 100))
        self.base1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0,0,0,0%);\n"
"	border-image: url(:/icons/empty_base.png);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:off{\n"
"	border-image: url(:/icons/empty_base.png);\n"
"}\n"
"\n"
"QPushButton:on{\n"
"	border-image: url(:/icons/highlighted_base.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-image: url(:/icons/pressed_base.png);\n"
"}\n"
"")
        self.base1.setCheckable(True)
        self.base1.setChecked(False)
        self.base1.setProperty("mask", QPixmap(u":/icons/mask_base.png"))
        self.base2 = QPushButton(self.bases)
        self.base2.setObjectName(u"base2")
        self.base2.setGeometry(QRect(60, 0, 100, 100))
        self.base2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0,0,0,0%);\n"
"	border-image: url(:/icons/empty_base.png);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:off{\n"
"	border-image: url(:/icons/empty_base.png);\n"
"}\n"
"\n"
"QPushButton:on{\n"
"	border-image: url(:/icons/highlighted_base.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-image: url(:/icons/pressed_base.png);\n"
"}\n"
"")
        self.base2.setCheckable(True)
        self.base2.setChecked(False)
        self.base2.setProperty("mask", QPixmap(u":/icons/mask_base.png"))
        self.base3 = QPushButton(self.bases)
        self.base3.setObjectName(u"base3")
        self.base3.setGeometry(QRect(0, 60, 100, 100))
        self.base3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0,0,0,0%);\n"
"	border-image: url(:/icons/empty_base.png);\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:off{\n"
"	border-image: url(:/icons/empty_base.png);\n"
"}\n"
"\n"
"QPushButton:on{\n"
"	border-image: url(:/icons/highlighted_base.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-image: url(:/icons/pressed_base.png);\n"
"}\n"
"")
        self.base3.setCheckable(True)
        self.base3.setChecked(False)
        self.base3.setProperty("mask", QPixmap(u":/icons/mask_base.png"))
        self.reset_bases = QPushButton(self.bases)
        self.reset_bases.setObjectName(u"reset_bases")
        self.reset_bases.setGeometry(QRect(90, 130, 40, 40))
        self.reset_bases.setFont(font2)
        self.reset_bases.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: #507DBC;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #2C4567;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #507DBC;\n"
"border: 0px;\n"
"}\n"
"")
        self.reset_bases.setIcon(icon1)
        self.reset_bases.setIconSize(QSize(28, 28))
        self.outs = QWidget(self.hud)
        self.outs.setObjectName(u"outs")
        self.outs.setGeometry(QRect(340, 0, 150, 171))
        self.outs_label = QLabel(self.outs)
        self.outs_label.setObjectName(u"outs_label")
        self.outs_label.setGeometry(QRect(0, 0, 150, 30))
        self.outs_label.setFont(font)
        self.outs_label.setStyleSheet(u"color: white;")
        self.outs_label.setScaledContents(False)
        self.outs_label.setAlignment(Qt.AlignCenter)
        self.out1_bg = QLabel(self.outs)
        self.out1_bg.setObjectName(u"out1_bg")
        self.out1_bg.setGeometry(QRect(0, 30, 50, 50))
        self.out1_bg.setAutoFillBackground(False)
        self.out1_bg.setStyleSheet(u"")
        self.out1_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.out1_bg.setScaledContents(True)
        self.out1_bg.setMargin(8)
        self.out2_bg = QLabel(self.outs)
        self.out2_bg.setObjectName(u"out2_bg")
        self.out2_bg.setGeometry(QRect(50, 30, 50, 50))
        self.out2_bg.setAutoFillBackground(False)
        self.out2_bg.setStyleSheet(u"")
        self.out2_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.out2_bg.setScaledContents(True)
        self.out2_bg.setMargin(8)
        self.out2 = QLabel(self.outs)
        self.out2.setObjectName(u"out2")
        self.out2.setGeometry(QRect(50, 30, 50, 50))
        self.out2.setAutoFillBackground(False)
        self.out2.setStyleSheet(u"")
        self.out2.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.out2.setScaledContents(True)
        self.out2.setMargin(8)
        self.out1 = QLabel(self.outs)
        self.out1.setObjectName(u"out1")
        self.out1.setEnabled(True)
        self.out1.setGeometry(QRect(0, 30, 50, 50))
        self.out1.setAutoFillBackground(False)
        self.out1.setStyleSheet(u"")
        self.out1.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.out1.setScaledContents(True)
        self.out1.setMargin(8)
        self.out_plus = QPushButton(self.outs)
        self.out_plus.setObjectName(u"out_plus")
        self.out_plus.setGeometry(QRect(50, 80, 100, 40))
        self.out_plus.setFont(font1)
        self.out_plus.setLayoutDirection(Qt.RightToLeft)
        self.out_plus.setStyleSheet(u"QPushButton{\n"
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
        self.out_plus.setIconSize(QSize(30, 30))
        self.out_plus.setFlat(False)
        self.out_minus = QPushButton(self.outs)
        self.out_minus.setObjectName(u"out_minus")
        self.out_minus.setGeometry(QRect(0, 80, 40, 40))
        self.out_minus.setLayoutDirection(Qt.LeftToRight)
        self.out_minus.setStyleSheet(u"QPushButton{\n"
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
"}")
        self.out_minus.setIcon(icon)
        self.out_minus.setIconSize(QSize(30, 30))
        self.out_minus.setFlat(False)
        self.reset_outs = QPushButton(self.outs)
        self.reset_outs.setObjectName(u"reset_outs")
        self.reset_outs.setGeometry(QRect(0, 130, 150, 40))
        self.reset_outs.setFont(font2)
        self.reset_outs.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: #507DBC;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"background-color: #2C4567;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #507DBC;\n"
"border: 0px;\n"
"}\n"
"")
        self.reset_outs.setIcon(icon1)
        self.reset_outs.setIconSize(QSize(28, 28))
        self.out3 = QLabel(self.outs)
        self.out3.setObjectName(u"out3")
        self.out3.setGeometry(QRect(100, 30, 50, 50))
        self.out3.setAutoFillBackground(False)
        self.out3.setStyleSheet(u"")
        self.out3.setPixmap(QPixmap(u":/icons/hilighted_circle.png"))
        self.out3.setScaledContents(True)
        self.out3.setMargin(8)
        self.out3_bg = QLabel(self.outs)
        self.out3_bg.setObjectName(u"out3_bg")
        self.out3_bg.setGeometry(QRect(100, 30, 50, 50))
        self.out3_bg.setAutoFillBackground(False)
        self.out3_bg.setStyleSheet(u"")
        self.out3_bg.setPixmap(QPixmap(u":/icons/empty_circle.png"))
        self.out3_bg.setScaledContents(True)
        self.out3_bg.setMargin(8)
        self.outs_label.raise_()
        self.out1_bg.raise_()
        self.out2_bg.raise_()
        self.out2.raise_()
        self.out1.raise_()
        self.out_plus.raise_()
        self.out_minus.raise_()
        self.reset_outs.raise_()
        self.out3_bg.raise_()
        self.out3.raise_()
        self.score = QWidget(self.centralwidget)
        self.score.setObjectName(u"score")
        self.score.setGeometry(QRect(90, 30, 610, 200))
        self.home = QWidget(self.score)
        self.home.setObjectName(u"home")
        self.home.setEnabled(True)
        self.home.setGeometry(QRect(410, 0, 200, 200))
        self.home.setStyleSheet(u"#home:enabled{\n"
"	border: 5px solid #9D44B5\n"
"}\n"
"#home:disabled{\n"
"	border: 0px solid #9D44B5\n"
"}")
        self.home_name = QLabel(self.home)
        self.home_name.setObjectName(u"home_name")
        self.home_name.setGeometry(QRect(10, 10, 181, 31))
        font3 = QFont()
        font3.setFamily(u"Open Sans")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setKerning(True)
        self.home_name.setFont(font3)
        self.home_name.setStyleSheet(u"color: white;")
        self.home_name.setScaledContents(False)
        self.home_name.setAlignment(Qt.AlignCenter)
        self.home_score = QLabel(self.home)
        self.home_score.setObjectName(u"home_score")
        self.home_score.setGeometry(QRect(9, 40, 181, 101))
        font4 = QFont()
        font4.setFamily(u"Open Sans Extrabold")
        font4.setPointSize(84)
        font4.setBold(False)
        font4.setWeight(50)
        self.home_score.setFont(font4)
        self.home_score.setStyleSheet(u"color: white")
        self.home_score.setScaledContents(False)
        self.home_score.setAlignment(Qt.AlignCenter)
        self.home_minus = QPushButton(self.home)
        self.home_minus.setObjectName(u"home_minus")
        self.home_minus.setGeometry(QRect(10, 150, 40, 40))
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
"\n"
"")
        self.home_minus.setIcon(icon)
        self.home_minus.setIconSize(QSize(30, 30))
        self.home_minus.setFlat(False)
        self.home_plus = QPushButton(self.home)
        self.home_plus.setObjectName(u"home_plus")
        self.home_plus.setGeometry(QRect(60, 150, 130, 40))
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/plus.png", QSize(), QIcon.Normal, QIcon.On)
        self.home_plus.setIcon(icon2)
        self.home_plus.setIconSize(QSize(30, 30))
        self.home_plus.setFlat(False)
        self.visitor = QWidget(self.score)
        self.visitor.setObjectName(u"visitor")
        self.visitor.setEnabled(True)
        self.visitor.setGeometry(QRect(0, 0, 200, 200))
        self.visitor.setStyleSheet(u"#visitor:enabled{\n"
"	border: 5px solid #9D44B5\n"
"}\n"
"#visitor:disabled{\n"
"	border: 0px solid #9D44B5\n"
"}")
        self.visitor_name = QLabel(self.visitor)
        self.visitor_name.setObjectName(u"visitor_name")
        self.visitor_name.setGeometry(QRect(10, 10, 181, 31))
        self.visitor_name.setFont(font3)
        self.visitor_name.setStyleSheet(u"color: white;")
        self.visitor_name.setScaledContents(False)
        self.visitor_name.setAlignment(Qt.AlignCenter)
        self.visitor_score = QLabel(self.visitor)
        self.visitor_score.setObjectName(u"visitor_score")
        self.visitor_score.setGeometry(QRect(9, 40, 181, 101))
        self.visitor_score.setFont(font4)
        self.visitor_score.setStyleSheet(u"color: white")
        self.visitor_score.setScaledContents(False)
        self.visitor_score.setAlignment(Qt.AlignCenter)
        self.visitor_minus = QPushButton(self.visitor)
        self.visitor_minus.setObjectName(u"visitor_minus")
        self.visitor_minus.setGeometry(QRect(10, 150, 40, 40))
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
"\n"
"")
        self.visitor_minus.setIcon(icon)
        self.visitor_minus.setIconSize(QSize(30, 30))
        self.visitor_minus.setFlat(False)
        self.visitor_plus = QPushButton(self.visitor)
        self.visitor_plus.setObjectName(u"visitor_plus")
        self.visitor_plus.setGeometry(QRect(60, 150, 130, 40))
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
        self.visitor_plus.setIcon(icon2)
        self.visitor_plus.setIconSize(QSize(30, 30))
        self.visitor_plus.setFlat(False)
        self.inning = QWidget(self.score)
        self.inning.setObjectName(u"inning")
        self.inning.setGeometry(QRect(220, 10, 170, 180))
        self.inning_bottom = QPushButton(self.inning)
        self.inning_bottom.setObjectName(u"inning_bottom")
        self.inning_bottom.setEnabled(True)
        self.inning_bottom.setGeometry(QRect(40, 140, 90, 40))
        self.inning_bottom.setLayoutDirection(Qt.LeftToRight)
        self.inning_bottom.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 0px solid #9D44B5;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: white;\n"
"background-color: #9D44B5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"border: 5px solid #9D44B5;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #9D44B5;\n"
"border: 0px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/down.png", QSize(), QIcon.Normal, QIcon.On)
        self.inning_bottom.setIcon(icon3)
        self.inning_bottom.setIconSize(QSize(50, 50))
        self.inning_bottom.setCheckable(False)
        self.inning_bottom.setFlat(False)
        self.inning_top = QPushButton(self.inning)
        self.inning_top.setObjectName(u"inning_top")
        self.inning_top.setEnabled(False)
        self.inning_top.setGeometry(QRect(40, 30, 90, 40))
        self.inning_top.setLayoutDirection(Qt.LeftToRight)
        self.inning_top.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"border: 0px solid #9D44B5;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: white;\n"
"background-color: #9D44B5;\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: white;\n"
"border: 5px solid #9D44B5;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: white;\n"
"background-color: #9D44B5;\n"
"border: 0px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/up.png", QSize(), QIcon.Normal, QIcon.On)
        self.inning_top.setIcon(icon4)
        self.inning_top.setIconSize(QSize(50, 50))
        self.inning_top.setCheckable(False)
        self.inning_top.setFlat(False)
        self.inning_number = QLabel(self.inning)
        self.inning_number.setObjectName(u"inning_number")
        self.inning_number.setGeometry(QRect(40, 70, 90, 70))
        font5 = QFont()
        font5.setFamily(u"Open Sans Extrabold")
        font5.setPointSize(42)
        font5.setBold(False)
        font5.setWeight(50)
        self.inning_number.setFont(font5)
        self.inning_number.setStyleSheet(u"color: white")
        self.inning_number.setScaledContents(False)
        self.inning_number.setAlignment(Qt.AlignCenter)
        self.inning_minus = QPushButton(self.inning)
        self.inning_minus.setObjectName(u"inning_minus")
        self.inning_minus.setGeometry(QRect(0, 85, 40, 40))
        self.inning_minus.setLayoutDirection(Qt.LeftToRight)
        self.inning_minus.setStyleSheet(u"QPushButton{\n"
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
"\n"
"")
        self.inning_minus.setIcon(icon)
        self.inning_minus.setIconSize(QSize(30, 30))
        self.inning_minus.setFlat(False)
        self.inning_plus = QPushButton(self.inning)
        self.inning_plus.setObjectName(u"inning_plus")
        self.inning_plus.setGeometry(QRect(130, 85, 40, 40))
        self.inning_plus.setLayoutDirection(Qt.LeftToRight)
        self.inning_plus.setStyleSheet(u"QPushButton{\n"
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
        self.inning_plus.setIcon(icon2)
        self.inning_plus.setIconSize(QSize(30, 30))
        self.inning_plus.setFlat(False)
        self.inning_label = QLabel(self.inning)
        self.inning_label.setObjectName(u"inning_label")
        self.inning_label.setGeometry(QRect(0, 0, 170, 30))
        self.inning_label.setFont(font)
        self.inning_label.setStyleSheet(u"color: white;")
        self.inning_label.setScaledContents(False)
        self.inning_label.setAlignment(Qt.AlignCenter)
        Baseball.setCentralWidget(self.centralwidget)

        self.retranslateUi(Baseball)

        self.strikes_add.setDefault(False)
        self.strike_minus.setDefault(False)
        self.balls_add.setDefault(False)
        self.balls_minus.setDefault(False)
        self.out_plus.setDefault(False)
        self.out_minus.setDefault(False)
        self.home_minus.setDefault(False)
        self.home_plus.setDefault(False)
        self.visitor_minus.setDefault(False)
        self.visitor_plus.setDefault(False)
        self.inning_bottom.setDefault(False)
        self.inning_top.setDefault(False)
        self.inning_minus.setDefault(False)
        self.inning_plus.setDefault(False)


        QMetaObject.connectSlotsByName(Baseball)
    # setupUi

    def retranslateUi(self, Baseball):
        Baseball.setWindowTitle(QCoreApplication.translate("Baseball", u"Baseball Scorekeeper", None))
        self.strikes_label.setText(QCoreApplication.translate("Baseball", u"STRIKES", None))
        self.strike1_bg.setText("")
        self.strike2_bg.setText("")
        self.strike2.setText("")
        self.strike1.setText("")
        self.strikes_add.setText(QCoreApplication.translate("Baseball", u"Strike", None))
        self.strike_minus.setText("")
        self.balls_label.setText(QCoreApplication.translate("Baseball", u"BALLS", None))
        self.ball1_bg.setText("")
        self.ball2_bg.setText("")
        self.ball3_bg.setText("")
        self.ball2.setText("")
        self.ball3.setText("")
        self.ball1.setText("")
        self.balls_add.setText(QCoreApplication.translate("Baseball", u"Ball", None))
        self.balls_minus.setText("")
        self.reset_count.setText(QCoreApplication.translate("Baseball", u"Reset Count", None))
        self.base1.setText("")
        self.base2.setText("")
        self.base3.setText("")
        self.reset_bases.setText("")
        self.outs_label.setText(QCoreApplication.translate("Baseball", u"OUTS", None))
        self.out1_bg.setText("")
        self.out2_bg.setText("")
        self.out2.setText("")
        self.out1.setText("")
        self.out_plus.setText(QCoreApplication.translate("Baseball", u"Out", None))
        self.out_minus.setText("")
        self.reset_outs.setText(QCoreApplication.translate("Baseball", u"Reset Outs", None))
        self.out3.setText("")
        self.out3_bg.setText("")
        self.home_name.setText(QCoreApplication.translate("Baseball", u"HOME", None))
        self.home_score.setText(QCoreApplication.translate("Baseball", u"0", None))
        self.home_minus.setText("")
        self.home_plus.setText(QCoreApplication.translate("Baseball", u"Add Run", None))
        self.visitor_name.setText(QCoreApplication.translate("Baseball", u"VISITOR", None))
        self.visitor_score.setText(QCoreApplication.translate("Baseball", u"0", None))
        self.visitor_minus.setText("")
        self.visitor_plus.setText(QCoreApplication.translate("Baseball", u"Add Run", None))
        self.inning_bottom.setText("")
        self.inning_top.setText("")
        self.inning_number.setText(QCoreApplication.translate("Baseball", u"12", None))
        self.inning_minus.setText("")
        self.inning_plus.setText("")
        self.inning_label.setText(QCoreApplication.translate("Baseball", u"INNING", None))
    # retranslateUi

