# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_feedback.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_FeedbackWindow(object):
    def setupUi(self, FeedbackWindow):
        if not FeedbackWindow.objectName():
            FeedbackWindow.setObjectName(u"FeedbackWindow")
        FeedbackWindow.resize(463, 255)
        self.wid_main = QWidget(FeedbackWindow)
        self.wid_main.setObjectName(u"wid_main")
        self.wid_main.setGeometry(QRect(0, 0, 461, 251))
        self.gridLayout = QGridLayout(self.wid_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.layout = QVBoxLayout()
        self.layout.setObjectName(u"layout")

        self.gridLayout.addLayout(self.layout, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lbl_logo = QLabel(self.wid_main)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setEnabled(True)
        self.lbl_logo.setMinimumSize(QSize(32, 32))
        self.lbl_logo.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.lbl_logo)

        self.lbl_title = QLabel(self.wid_main)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(80, 40))
        self.lbl_title.setMaximumSize(QSize(80, 40))

        self.horizontalLayout_3.addWidget(self.lbl_title)

        self.horizontalSpacer = QSpacerItem(32, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.wid_main)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(FeedbackWindow)

        QMetaObject.connectSlotsByName(FeedbackWindow)
    # setupUi

    def retranslateUi(self, FeedbackWindow):
        FeedbackWindow.setWindowTitle("")
        self.lbl_logo.setText("")
        self.lbl_title.setText(QCoreApplication.translate("FeedbackWindow", u"title_this_window", None))
        self.btn_close.setText("")
    # retranslateUi

