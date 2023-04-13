# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.wid_main = QWidget(MainWindow)
        self.wid_main.setObjectName(u"wid_main")
        self.wid_main.setMouseTracking(True)
        self.gridLayout = QGridLayout(self.wid_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_123 = QVBoxLayout()
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.tab_menu = QWidget(self.wid_main)
        self.tab_menu.setObjectName(u"tab_menu")
        self.tab_menu.setMinimumSize(QSize(150, 0))
        self.tab_menu.setMaximumSize(QSize(150, 16777215))
        self.tab_menu.setMouseTracking(True)

        self.verticalLayout_123.addWidget(self.tab_menu)


        self.gridLayout.addLayout(self.verticalLayout_123, 2, 0, 4, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tbl_main = QTableWidget(self.wid_main)
        if (self.tbl_main.columnCount() < 6):
            self.tbl_main.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_main.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_main.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_main.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_main.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_main.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_main.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tbl_main.setObjectName(u"tbl_main")
        self.tbl_main.setMinimumSize(QSize(0, 0))
        self.tbl_main.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.tbl_main)

        self.lbl_table_open = QLabel(self.wid_main)
        self.lbl_table_open.setObjectName(u"lbl_table_open")
        self.lbl_table_open.setMinimumSize(QSize(0, 40))
        self.lbl_table_open.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.lbl_table_open)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.lbl_open = QLabel(self.wid_main)
        self.lbl_open.setObjectName(u"lbl_open")
        self.lbl_open.setMinimumSize(QSize(0, 0))
        self.lbl_open.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.lbl_open)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 2, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_dir = QLabel(self.wid_main)
        self.lbl_dir.setObjectName(u"lbl_dir")

        self.horizontalLayout.addWidget(self.lbl_dir)

        self.com_dir = QComboBox(self.wid_main)
        self.com_dir.addItem("")
        self.com_dir.addItem("")
        self.com_dir.setObjectName(u"com_dir")
        self.com_dir.setMinimumSize(QSize(0, 0))
        self.com_dir.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout.addWidget(self.com_dir)

        self.lbl_path = QLabel(self.wid_main)
        self.lbl_path.setObjectName(u"lbl_path")

        self.horizontalLayout.addWidget(self.lbl_path)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_clear = QPushButton(self.wid_main)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.btn_clear)

        self.btn_convert = QPushButton(self.wid_main)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setMinimumSize(QSize(100, 40))

        self.horizontalLayout.addWidget(self.btn_convert)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_blank = QLabel(self.wid_main)
        self.lbl_blank.setObjectName(u"lbl_blank")
        self.lbl_blank.setMinimumSize(QSize(0, 16))
        self.lbl_blank.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_4.addWidget(self.lbl_blank)


        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_blank2 = QLabel(self.wid_main)
        self.lbl_blank2.setObjectName(u"lbl_blank2")
        self.lbl_blank2.setMinimumSize(QSize(0, 10))
        self.lbl_blank2.setMaximumSize(QSize(16777215, 10))
        self.lbl_blank2.setMouseTracking(True)

        self.horizontalLayout_5.addWidget(self.lbl_blank2)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lbl_logo = QLabel(self.wid_main)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setEnabled(True)
        self.lbl_logo.setMinimumSize(QSize(32, 32))
        self.lbl_logo.setMaximumSize(QSize(32, 32))
        self.lbl_logo.setMouseTracking(True)

        self.horizontalLayout_3.addWidget(self.lbl_logo)

        self.lbl_title = QLabel(self.wid_main)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setMinimumSize(QSize(200, 40))
        self.lbl_title.setMaximumSize(QSize(200, 40))
        self.lbl_title.setMouseTracking(True)

        self.horizontalLayout_3.addWidget(self.lbl_title)

        self.horizontalSpacer = QSpacerItem(80, 32, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_more = QPushButton(self.wid_main)
        self.btn_more.setObjectName(u"btn_more")
        self.btn_more.setMinimumSize(QSize(32, 32))
        self.btn_more.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_more)

        self.btn_min = QPushButton(self.wid_main)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(32, 32))
        self.btn_min.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.wid_main)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(32, 32))
        self.btn_max.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_max)

        self.btn_restore = QPushButton(self.wid_main)
        self.btn_restore.setObjectName(u"btn_restore")
        self.btn_restore.setMinimumSize(QSize(32, 32))
        self.btn_restore.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_restore)

        self.btn_close = QPushButton(self.wid_main)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(32, 32))
        self.btn_close.setMaximumSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbl_blank3 = QLabel(self.wid_main)
        self.lbl_blank3.setObjectName(u"lbl_blank3")
        self.lbl_blank3.setMinimumSize(QSize(0, 10))
        self.lbl_blank3.setMaximumSize(QSize(16777215, 10))
        self.lbl_blank3.setMouseTracking(True)

        self.horizontalLayout_6.addWidget(self.lbl_blank3)


        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 4)

        MainWindow.setCentralWidget(self.wid_main)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tbl_main.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"col_check", None));
        ___qtablewidgetitem1 = self.tbl_main.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"col_name", None));
        ___qtablewidgetitem2 = self.tbl_main.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"col_count", None));
        ___qtablewidgetitem3 = self.tbl_main.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"col_range", None));
        ___qtablewidgetitem4 = self.tbl_main.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"col_status", None));
        ___qtablewidgetitem5 = self.tbl_main.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"col_action", None));
        self.lbl_table_open.setText("")
        self.lbl_open.setText("")
        self.lbl_dir.setText(QCoreApplication.translate("MainWindow", u"title_output_folder", None))
        self.com_dir.setItemText(0, QCoreApplication.translate("MainWindow", u"title_pdf_path", None))
        self.com_dir.setItemText(1, QCoreApplication.translate("MainWindow", u"title_user_path", None))

        self.lbl_path.setText("")
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"title_clear", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"title_convert", None))
        self.lbl_blank.setText("")
        self.lbl_blank2.setText("")
        self.lbl_logo.setText("")
        self.lbl_title.setText(QCoreApplication.translate("MainWindow", u"title_this_app", None))
        self.btn_more.setText("")
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_restore.setText("")
        self.btn_close.setText("")
        self.lbl_blank3.setText("")
    # retranslateUi

