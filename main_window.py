# -*- coding: utf-8 -*-

import json
import os
import threading

from PySide6.QtGui import QAction, QCursor
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QLabel, \
    QHBoxLayout, QVBoxLayout, QWidget, \
    QFileDialog, QBoxLayout, QHeaderView, QMenu, QCheckBox, QProgressBar, QDialog

from text import TextType, Text
from ui_main import Ui_MainWindow
from theme_window import ThemeWindow
from feedback_window import FeedbackWindow
from about_window import AboutWindow
from message_window import MessageWindow
from toast import ToastWidget

from column import ColumnIndex, ColumnStatus
from cursor import CursorDirection
from language import Language
from action import Action
from icon import LogoIcon, MenuIcon, LabelIcon
from style import LabelStyle, ButtonStyle, MenuStyle, WidgetStyle, TableWidgetStyle, ProgressBarStyle
from utils import StringUtils, ButtonUtils, FileUtils, PageUtils, TitleUtils
from file import FileType, FileManager
from widget import WidgetType, WidgetManager
from thread import ConvertThread

class MainWindow(QMainWindow):
    def __init__(self, p_theme, p_translator, p_setting):
        super(MainWindow, self).__init__()

        self.theme = p_theme
        self.translator = p_translator
        self.setting = p_setting

        self.thread = ConvertThread(self)
        self.thread.thread_signal.connect(self.proc_convert_signal)
        self.convert_done = True

        self.cursor_direction = CursorDirection.Default
        self.left_btn_pressed = False
        self.drag_point = 0

        self.action = Action.Pdf2Word
        self.check_state = Qt.Checked
        self.output_dir = ''
        self.tab_btn = None
        self.cn_menu = None
        self.en_menu = None
        self.open_label = None

        self.wid_mng = WidgetManager()
        self.file_mng = FileManager()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init()

    def init(self):
        self.init_window()
        self.init_app_bar()
        self.init_more_menu()
        self.init_tab_menu()
        self.init_output_bar()
        self.init_table()
        self.init_label()
        self.init_language()

    def init_window(self):
        self.ui.wid_main.setStyleSheet(WidgetStyle.get_border('wid_main'))
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint \
                            | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint \
                            | Qt.WindowMaximizeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMouseTracking(True)

    def init_app_bar(self):
        self.ui.lbl_logo.setMinimumSize(QSize(24, 24))
        self.ui.lbl_logo.setMaximumSize(QSize(24, 24))
        self.ui.lbl_logo.setPixmap(LogoIcon.get_pixmap())
        self.ui.lbl_logo.setScaledContents(True)

        self.ui.btn_max.setVisible(True)
        self.ui.btn_restore.setVisible(False)

        self.ui.btn_more.setFlat(True)
        self.ui.btn_min.setFlat(True)
        self.ui.btn_close.setFlat(True)
        self.ui.btn_max.setFlat(True)
        self.ui.btn_restore.setFlat(True)

        self.ui.btn_more.setIcon(MenuIcon.get_more())
        self.ui.btn_min.setIcon(MenuIcon.get_min())
        self.ui.btn_close.setIcon(MenuIcon.get_close())
        self.ui.btn_max.setIcon(MenuIcon.get_max())
        self.ui.btn_restore.setIcon(MenuIcon.get_restore())

        self.ui.btn_more.setIconSize(QSize(24, 24))
        self.ui.btn_min.setIconSize(QSize(24, 24))
        self.ui.btn_close.setIconSize(QSize(24, 24))
        self.ui.btn_max.setIconSize(QSize(24, 24))
        self.ui.btn_restore.setIconSize(QSize(24, 24))

        self.ui.btn_close.setStyleSheet(ButtonStyle.get_close())

        self.ui.btn_min.clicked.connect(self.on_min)
        self.ui.btn_close.clicked.connect(self.on_exit)
        self.ui.btn_max.clicked.connect(self.on_max)
        self.ui.btn_restore.clicked.connect(self.on_restore)

        self.ui.lbl_title.setStyleSheet(LabelStyle.get_title())

    def init_output_bar(self):
        self.ui.com_dir.setCurrentIndex(0)
        self.ui.com_dir.currentIndexChanged.connect(self.on_choose_dir)

        style = ButtonStyle.get_action()
        self.ui.btn_clear.setStyleSheet(style)
        self.ui.btn_convert.setStyleSheet(style)

        self.ui.btn_clear.clicked.connect(self.on_clear)
        self.ui.btn_convert.clicked.connect(self.on_convert)

    def init_more_menu(self):
        menu = QMenu(self)
        menu.setStyleSheet(MenuStyle.get_more())

        action = QAction(MainWindow.tr('menu_theme'), self)
        action.setIcon(MenuIcon.get_theme())
        action.triggered.connect(self.on_show_theme)
        menu.addAction(action)
        self.wid_mng.add(action, text = 'menu_theme', widget_type = WidgetType.DynamicWidget)

        languageMenu = QMenu(MainWindow.tr('menu_language'))
        languageMenu.setIcon(MenuIcon.get_language())
        menu.addMenu(languageMenu)
        self.wid_mng.add(languageMenu, text = 'menu_language', widget_type = WidgetType.DynamicWidget)

        action = QAction(MainWindow.tr('menu_chinese'), languageMenu)
        action.setCheckable(True)
        action.setChecked(True)
        action.triggered.connect(self.on_show_chinese)
        languageMenu.addAction(action)
        self.cn_menu = action
        self.wid_mng.add(action, text = 'menu_chinese', widget_type = WidgetType.DynamicWidget)

        action = QAction(MainWindow.tr('menu_english'), languageMenu)
        action.setCheckable(True)
        action.setChecked(False)
        action.triggered.connect(self.on_show_english)
        languageMenu.addAction(action)
        self.en_menu = action
        self.wid_mng.add(action, text = 'menu_english', widget_type = WidgetType.DynamicWidget)

        action = QAction(MainWindow.tr('menu_feedback'), self)
        action.setIcon(MenuIcon.get_feedback())
        action.triggered.connect(self.on_show_feedback)
        menu.addAction(action)
        self.wid_mng.add(action, text = 'menu_feedback', widget_type = WidgetType.DynamicWidget)

        action = QAction(MainWindow.tr('menu_about'), self)
        action.setIcon(MenuIcon.get_about())
        action.triggered.connect(self.on_show_about)
        menu.addAction(action)
        self.wid_mng.add(action, text = 'menu_about', widget_type = WidgetType.DynamicWidget)

        self.ui.btn_more.setMenu(menu)
        self.ui.btn_more.setStyleSheet(ButtonStyle.get_more())

    def init_language(self):
        if self.setting.get_language() == Language.Chinese.value:
            self.cn_menu.setChecked(True)
            self.en_menu.setChecked(False)
        else:
            self.en_menu.setChecked(True)
            self.cn_menu.setChecked(False)

    def init_tab_menu(self):
        layout = QVBoxLayout()
        layout.setSpacing(3)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setDirection(QBoxLayout.TopToBottom)

        bkg_color = self.theme.get_primary_color()
        style = ButtonStyle.get_tab(bkg_color, self.theme)

        btn = ButtonUtils.get_tab(MenuIcon.get_pdf2word(), MainWindow.tr('menu_pdf2word'), style, True)
        self.tab_btn = btn
        self.wid_mng.add(btn, text = 'menu_pdf2word', widget_type = WidgetType.DynamicWidget)
        self.wid_mng.add(btn, text = 'menu_pdf2word', widget_type = WidgetType.StyleWidget)
        btn.clicked.connect(self.on_click_tab_menu)
        layout.addWidget(btn, 1)
        
        bkg_color = self.get_unclicked_tab_menu_color()
        style = ButtonStyle.get_tab(bkg_color, self.theme)

        btn = ButtonUtils.get_tab(MenuIcon.get_word2pdf(), MainWindow.tr('menu_word2pdf'), style, False)
        self.wid_mng.add(btn, text='menu_word2pdf', widget_type=WidgetType.DynamicWidget)
        self.wid_mng.add(btn, text='menu_word2pdf', widget_type=WidgetType.StyleWidget)
        btn.clicked.connect(self.on_click_tab_menu)
        layout.addWidget(btn, 1)

        btn = ButtonUtils.get_tab(MenuIcon.get_excel2pdf(), MainWindow.tr('menu_excel2pdf'), style, False)
        self.wid_mng.add(btn, text='menu_excel2pdf', widget_type=WidgetType.DynamicWidget)
        self.wid_mng.add(btn, text='menu_excel2pdf', widget_type=WidgetType.StyleWidget)
        btn.clicked.connect(self.on_click_tab_menu)
        layout.addWidget(btn, 1)

        btn = ButtonUtils.get_tab(MenuIcon.get_ppt2pdf(), MainWindow.tr('menu_ppt2pdf'), style, False)
        self.wid_mng.add(btn, text='menu_ppt2pdf', widget_type=WidgetType.DynamicWidget)
        self.wid_mng.add(btn, text='menu_ppt2pdf', widget_type=WidgetType.StyleWidget)
        btn.clicked.connect(self.on_click_tab_menu)
        layout.addWidget(btn, 1)

        layout.addStretch(10)

        self.ui.tab_menu.setLayout(layout)

    def init_table(self):
        self.ui.tbl_main.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tbl_main.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tbl_main.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tbl_main.horizontalHeader().setSectionResizeMode(ColumnIndex.Check.value, QHeaderView.Interactive)
        self.ui.tbl_main.horizontalHeader().setSectionResizeMode(ColumnIndex.Name.value, QHeaderView.Interactive)
        self.ui.tbl_main.horizontalHeader().setSectionResizeMode(ColumnIndex.Status.value, QHeaderView.Interactive)
        self.ui.tbl_main.horizontalHeader().sectionClicked.connect(self.on_section_clicked)
        self.ui.tbl_main.itemSelectionChanged.connect(self.on_item_selection_changed)
        style = TableWidgetStyle.get_selection(self.theme.get_primary_color(), self.theme.get_secondary_text_color())
        self.ui.tbl_main.setStyleSheet(style)
        self.wid_mng.add(self.ui.tbl_main, text = 'tbl_main', widget_type = WidgetType.StyleWidget)

        self.ui.tbl_main.setVisible(False)

    def init_label(self):
        self.init_open_label()
        self.init_open_table_label()

    def init_open_label(self):
        label = QLabel()
        label.setMaximumSize(QSize(48, 48))
        label.setMinimumSize(QSize(48, 48))
        label.setPixmap(LabelIcon.get_add(QSize(48, 48)))
        label.setScaledContents(True)

        color = self.theme.get_primary_color()
        style = LabelStyle.get_open_hover(color)
        self.wid_mng.add(label, text = 'lbl_open', widget_type = WidgetType.StyleWidget)
        
        label.setStyleSheet(style)
        label.setToolTip(self.get_widget_text(TextType.AddFileLabel))
        self.open_label = label
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        layout.setAlignment(label, Qt.AlignHCenter)
        self.ui.lbl_open.setStyleSheet(LabelStyle.get_open('lbl_open'))
        self.ui.lbl_open.setAlignment(Qt.AlignCenter)
        self.ui.lbl_open.setLayout(layout)
        self.ui.lbl_open.mousePressEvent = self.on_choose_file
        self.wid_mng.add(label, text = 'tip_add_file', widget_type = WidgetType.DynamicWidget)

        self.ui.lbl_open.setVisible(True)

    def init_open_table_label(self):
        label = QLabel()
        label.setMaximumSize(QSize(32, 32))
        label.setMinimumSize(QSize(32, 32))
        label.setPixmap(LabelIcon.get_add(QSize(32, 32)))
        label.setScaledContents(True)
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label)
        layout.setAlignment(label, Qt.AlignHCenter)
        
        color = self.theme.get_primary_color()
        style = LabelStyle.get_table_open('lbl_table_open', color)
        self.wid_mng.add(self.ui.lbl_table_open, text = 'lbl_table_open', widget_type = WidgetType.StyleWidget)
        
        self.ui.lbl_table_open.setStyleSheet(style)
        self.ui.lbl_table_open.setToolTip(self.get_widget_text(TextType.AddFileLabel))
        self.ui.lbl_table_open.setAlignment(Qt.AlignCenter)
        self.ui.lbl_table_open.setLayout(layout)
        self.ui.lbl_table_open.mousePressEvent = self.on_choose_file
        self.wid_mng.add(self.ui.lbl_table_open, text = 'tip_add_file', widget_type = WidgetType.DynamicWidget)

        self.ui.lbl_table_open.setVisible(False)

    def show_table(self):
        self.ui.lbl_open.setVisible(False)
        self.ui.lbl_table_open.setVisible(True)
        self.ui.tbl_main.setVisible(True)

    def show_open_label(self):
        self.ui.lbl_open.setVisible(True)
        self.ui.lbl_table_open.setVisible(False)
        self.ui.tbl_main.setVisible(False)

    def reset_table(self):
        self.ui.tbl_main.setRowCount(0)
        self.ui.tbl_main.clearContents()
        
    def add_table_row(self, file_name):
        print(file_name)
        
        file_id = self.file_mng.gen_id()
        self.file_mng.add_file(file_id, file_name)

        row = self.ui.tbl_main.rowCount()
        self.ui.tbl_main.setRowCount(row + 1)
        self.ui.tbl_main.setRowHeight(row, 40)

        column = ColumnIndex.Check.value
        widget = QWidget(self.ui.tbl_main)
        layout = QHBoxLayout(widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

        check = QCheckBox()
        check.setCheckable(True)
        check.setChecked(True)
        check.clicked.connect(self.on_check_file)
        self.file_mng.add_widget(check, file_id)
        layout.addWidget(check)
        style = WidgetStyle.get_action(self.theme.get_primary_color())
        widget.setStyleSheet(style)
        self.wid_mng.add(widget, text = 'widget_check' + str(row), widget_type = WidgetType.StyleWidget)
        self.ui.tbl_main.setCellWidget(row, column, widget)

        column = ColumnIndex.Name.value
        item = QTableWidgetItem(os.path.basename(file_name))
        item.setFlags(item.flags and (~Qt.ItemFlag.ItemIsEditable))
        self.ui.tbl_main.setItem(row, column, item)

        column = ColumnIndex.Count.value
        page_count = PageUtils.get_count(file_name, self.action)
        item = QTableWidgetItem(str(page_count))
        item.setFlags(item.flags and (~Qt.ItemFlag.ItemIsEditable))
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tbl_main.setItem(row, column, item)

        column = ColumnIndex.Range.value
        item = QTableWidgetItem(MainWindow.tr('range_all'))
        item.setFlags(item.flags and (~Qt.ItemFlag.ItemIsEditable))
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.tbl_main.setItem(row, column, item)

        column = ColumnIndex.Status.value
        color = self.theme.get_primary_color()
        widget = QWidget()

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        label = QLabel(MainWindow.tr('status_init'))
        layout.addWidget(label)
        self.wid_mng.add(label, file_id = file_id, widget_type = WidgetType.StatusLabel)

        progress_bar = QProgressBar()
        progress_bar.setRange(0, 0)
        style = ProgressBarStyle.get_action(color)
        progress_bar.setStyleSheet(style)
        progress_bar.setEnabled(False)
        progress_bar.setVisible(False)
        layout.addWidget(progress_bar)
        self.wid_mng.add(progress_bar, text = 'progress_bar' + str(row), widget_type = WidgetType.StyleWidget)
        self.wid_mng.add(progress_bar, file_id = file_id, widget_type = WidgetType.StatusProgressBar)

        widget.setLayout(layout)
        style = WidgetStyle.get_action(color)
        widget.setStyleSheet(style)
        self.wid_mng.add(progress_bar, text = 'progress_widget' + str(row), widget_type = WidgetType.StyleWidget)
        self.ui.tbl_main.setCellWidget(row, column, widget)

        column = ColumnIndex.Action.value
        style = LabelStyle.get_action(color)

        width = 26
        height = 26
        blank_width = 10
        blank_height = 26
        total_width = 0
        total_height = 0

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel()
        label.setMaximumSize(QSize(width, height))
        label.setMinimumSize(QSize(width, height))
        label.setPixmap(self.get_open_file_icon(QSize(width, height)))
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setText('')
        label.setStyleSheet(style)
        label.setToolTip(self.get_widget_text(TextType.OpenFileLabel))
        label.mousePressEvent = self.on_open_src_file
        layout.addWidget(label)
        self.file_mng.add_widget(label, file_id)
        total_width += width
        total_height += height
        self.wid_mng.add(label, text = 'lbl_open_src_file' + str(row), widget_type = WidgetType.StyleWidget)

        label = QLabel()
        label.setMaximumSize(QSize(blank_width, blank_height))
        label.setMinimumSize(QSize(blank_width, blank_height))
        label.setText('')
        layout.addWidget(label)
        total_width += blank_width
        total_height += blank_height

        label = QLabel()
        label.setMaximumSize(QSize(width, height))
        label.setMinimumSize(QSize(width, height))
        label.setPixmap(LabelIcon.get_folder(QSize(width, height)))
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setText('')
        label.setStyleSheet(style)
        label.setToolTip(MainWindow.tr('tip_open_folder'))
        label.mousePressEvent = self.on_open_src_folder
        layout.addWidget(label)
        self.file_mng.add_widget(label, file_id)
        total_width += width
        total_height += height
        self.wid_mng.add(label, text = 'lbl_open_folder' + str(row), widget_type = WidgetType.StyleWidget)
        
        label = QLabel()
        label.setMaximumSize(QSize(blank_width, blank_height))
        label.setMinimumSize(QSize(blank_width, blank_height))
        label.setText('')
        layout.addWidget(label)
        total_width += blank_width
        total_height += blank_height

        label = QLabel()
        label.setMaximumSize(QSize(width, height))
        label.setMinimumSize(QSize(width, height))
        label.setPixmap(LabelIcon.get_close(QSize(width, height)))
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setText('')
        label.setStyleSheet(LabelStyle.get_close())
        label.setToolTip(MainWindow.tr('tip_delete_file'))
        label.mousePressEvent = self.on_delete_table_row
        layout.addWidget(label)
        self.file_mng.add_widget(label, file_id)
        total_width += width
        total_height += height

        widget = QWidget()
        widget.setLayout(layout)
        style = WidgetStyle.get_action(self.theme.get_primary_color())
        widget.setStyleSheet(style)
        self.wid_mng.add(widget, text = 'widget_action' + str(row), widget_type = WidgetType.StyleWidget)
        self.ui.tbl_main.setCellWidget(row, column, widget)
        
        self.show_table()

        self.ui.tbl_main.selectRow(row)

    @staticmethod
    def get_status_text(status, msg):
        extra = ''
        if len(msg) > 0:
            extra = '[' + msg + ']'

        text = ''
        if status == ColumnStatus.End.value:
            text = MainWindow.tr('status_succ') + extra
        elif status == ColumnStatus.Exception.value:
            text = MainWindow.tr('status_fail') + extra

        return text
        
    def get_row(self, file_id):
        row = None
        check_widget = self.file_mng.get_check_widget(file_id)
        for i in range(self.ui.tbl_main.rowCount()):
            item = self.ui.tbl_main.cellWidget(i, ColumnIndex.Check.value)
            checks = item.findChildren(QCheckBox)
            if check_widget in checks:
                row = i
                break

        return row

    def get_open_file_icon(self, size, update=False):
        if self.action == Action.Pdf2Word:
            if not update:
                return LabelIcon.get_pdf(size)
            else:
                return LabelIcon.get_word(size)
        elif self.action == Action.Word2Pdf:
            if not update:
                return LabelIcon.get_word(size)
            else:
                return LabelIcon.get_pdf(size)
        elif self.action == Action.Excel2Pdf:
            if not update:
                return LabelIcon.get_excel(size)
            else:
                return LabelIcon.get_pdf(size)
        elif self.action == Action.PPT2Pdf:
            if not update:
                return LabelIcon.get_ppt(size)
            else:
                return LabelIcon.get_pdf(size)
        else:
            return LabelIcon.get_file(size)

    def get_widget_text(self, text_type):
        return MainWindow.tr(Text.get(self.action, text_type))
        
    def update_widget_text(self):
        self.open_label.setToolTip(self.get_widget_text(TextType.AddFileLabel))
        self.ui.lbl_table_open.setToolTip(self.get_widget_text(TextType.AddFileLabel))

        self.ui.com_dir.clear()
        self.ui.com_dir.addItem(self.get_widget_text(TextType.OutputPathComboBox))
        self.ui.com_dir.addItem(MainWindow.tr('title_user_path'))
        self.ui.com_dir.setCurrentIndex(0)

    def update_status_column(self, file_id, status, msg):
        if status == ColumnStatus.Start.value or status == ColumnStatus.Running.value:
            progress_bar = self.wid_mng.get(file_id = file_id, widget_type = WidgetType.StatusProgressBar)
            if progress_bar:
                progress_bar.setVisible(True)
                progress_bar.setEnabled(True)
                progress_bar.setRange(0, 0)
                
                color = self.theme.get_primary_color()
                style = ProgressBarStyle.get_action(color)
                progress_bar.setStyleSheet(style)

            status_label = self.wid_mng.get(file_id = file_id, widget_type = WidgetType.StatusLabel)
            if status_label:
                status_label.setVisible(False)
        elif status == ColumnStatus.End.value or status == ColumnStatus.Exception.value:
            progress_bar = self.wid_mng.get(file_id = file_id, widget_type = WidgetType.StatusProgressBar)
            if progress_bar:
                progress_bar.setEnabled(False)
                progress_bar.setVisible(False)

            status_label = self.wid_mng.get(file_id = file_id, widget_type = WidgetType.StatusLabel)
            if status_label:
                status_label.setText(self.get_status_text(status, msg))
                status_label.setVisible(True)

    def update_action_column(self, file_id):
        row = self.get_row(file_id)
        column = ColumnIndex.Action.value

        color = self.theme.get_primary_color()
        style = LabelStyle.get_action(color)

        width = 26
        height = 26
        blank_width = 10
        blank_height = 26
        total_width = 0
        total_height = 0

        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel()
        label.setMaximumSize(QSize(width, height))
        label.setMinimumSize(QSize(width, height))
        label.setPixmap(self.get_open_file_icon(QSize(width, height), True))
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setText('')
        label.setStyleSheet(style)
        label.setToolTip(self.get_widget_text(TextType.StartFileLabel))
        label.mousePressEvent = self.on_open_dst_file
        layout.addWidget(label)
        self.file_mng.add_widget(label, file_id)
        total_width += width
        total_height += height
        self.wid_mng.add(label, text = 'lbl_open_dst_file' + str(row), widget_type = WidgetType.StyleWidget)

        label = QLabel()
        label.setMaximumSize(QSize(blank_width, blank_height))
        label.setMinimumSize(QSize(blank_width, blank_height))
        label.setText('')
        layout.addWidget(label)
        total_width += blank_width
        total_height += blank_height

        label = QLabel()
        label.setMaximumSize(QSize(width, height))
        label.setMinimumSize(QSize(width, height))
        label.setPixmap(LabelIcon.get_folder(QSize(width, height)))
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setText('')
        label.setStyleSheet(style)
        label.setToolTip(MainWindow.tr('tip_open_folder'))
        label.mousePressEvent = self.on_open_dst_folder
        layout.addWidget(label)
        self.file_mng.add_widget(label, file_id)
        total_width += width
        total_height += height
        self.wid_mng.add(label, text = 'lbl_open_folder' + str(row), widget_type = WidgetType.StyleWidget)

        label = QLabel()
        label.setMaximumSize(QSize(blank_width, blank_height))
        label.setMinimumSize(QSize(blank_width, blank_height))
        label.setText('')
        layout.addWidget(label)
        total_width += blank_width
        total_height += blank_height

        label = QLabel()
        label.setMaximumSize(QSize(width, height))
        label.setMinimumSize(QSize(width, height))
        label.setPixmap(LabelIcon.get_close(QSize(width, height)))
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignCenter)
        label.setText('')
        label.setStyleSheet(LabelStyle.get_close())
        label.setToolTip(MainWindow.tr('tip_delete_file'))
        label.mousePressEvent = self.on_delete_table_row
        layout.addWidget(label)
        self.file_mng.add_widget(label, file_id)
        total_width += width
        total_height += height

        widget = QWidget()
        widget.setLayout(layout)
        style = WidgetStyle.get_action(self.theme.get_primary_color())
        widget.setStyleSheet(style)
        self.wid_mng.add(widget, text = 'widget_action' + str(row), widget_type = WidgetType.StyleWidget)
        self.ui.tbl_main.setCellWidget(row, column, widget)

        self.ui.tbl_main.selectRow(row)

        self.update_action_column_color(row, True)

    def update_action_column_color(self, row, selected):
        if selected:
            color = self.theme.get_selected_color()
        else:
            color = self.theme.get_unselected_color()

        for index in (ColumnIndex.Status.value, ColumnIndex.Action.value):
            widget = self.ui.tbl_main.cellWidget(row, index)
            if widget:
                widget.setStyleSheet(WidgetStyle.get_selection(color))
                
    def update_clicked_tab_menu_color(self, btn):
        bkg_color = self.theme.get_primary_color()
        style = ButtonStyle.get_tab(bkg_color, self.theme)
        btn.setStyleSheet(style)
        
    def get_unclicked_tab_menu_color(self):
        if StringUtils.contains(self.theme.get_theme_name(), 'dark'):
            return self.theme.get_secondary_dark_color()
        else:
            return self.theme.get_secondary_light_color()
        
    def update_unclicked_tab_menu_color(self, btn):
        bkg_color = self.get_unclicked_tab_menu_color()
        style = ButtonStyle.get_tab(bkg_color, self.theme)
        btn.setStyleSheet(style)
        
    def update_style_widgets(self):
        color = self.theme.get_primary_color()
        text_color = self.theme.get_primary_text_color()
        bkg_color = color
        style = None

        style_widgets = self.wid_mng.get_all(WidgetType.StyleWidget)
        for (name, widget) in style_widgets.items():
            if name in ['menu_pdf2word', 'menu_word2pdf', 'menu_excel2pdf', 'menu_ppt2pdf', 'menu_pdf_split', 'menu_pdf_merge']:
                bkg_color = self.get_unclicked_tab_menu_color()
                style = ButtonStyle.get_tab(bkg_color, self.theme)
            elif name == 'lbl_open':
                style = LabelStyle.get_open_hover(color)
            elif name == 'lbl_table_open':
                style = LabelStyle.get_table_open('lbl_table_open', color)
            elif StringUtils.contains(name, 'lbl_open_src_file') or StringUtils.contains(name, 'lbl_open_dst_file') or StringUtils.contains(name, 'lbl_open_folder'):
                style = LabelStyle.get_action(color)
            elif StringUtils.contains(name, 'widget_action') or StringUtils.contains(name, 'progress_widget'):
                style = WidgetStyle.get_action(color)
            elif StringUtils.contains(name, 'widget_check'):
                style = WidgetStyle.get_action(color)
            elif StringUtils.contains(name, 'tbl_main'):
                style = TableWidgetStyle.get_selection(color, self.theme.get_secondary_text_color())
            elif StringUtils.contains(name, 'progress_bar'):
                style = ProgressBarStyle.get_action(color)

            if style:
                # noinspection PyBroadException
                try:
                    widget.setStyleSheet(style)
                except:
                    pass

        self.update_clicked_tab_menu_color(self.tab_btn)

    def update_dynamic_widgets(self):
        dynamic_widgets = self.wid_mng.get_all(WidgetType.DynamicWidget)
        for (widget, text) in dynamic_widgets.items():
            if isinstance(widget, QLabel):
                widget.setToolTip(MainWindow.tr(text))
            elif isinstance(widget, QMenu):
                widget.setTitle(MainWindow.tr(text))
            else:
                widget.setText(MainWindow.tr(text))

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.ui.btn_max.setVisible(False)
        self.ui.btn_restore.setVisible(True)
        self.showMaximized()

    def on_restore(self):
        self.ui.btn_max.setVisible(True)
        self.ui.btn_restore.setVisible(False)
        self.showNormal()

    def on_exit(self):
        if not self.convert_done:
            dlg = MessageWindow(self, self.theme, MainWindow.tr('title_exit'), MainWindow.tr('tip_exit_running'))
            result = dlg.exec()
            if result != QDialog.DialogCode.Accepted:
                return

        one = QApplication.instance()
        one.quit()
        
    def on_click_tab_menu(self):
        btn = self.sender()
        text = btn.text()

        action = None
        if text == MainWindow.tr('menu_pdf2word'):
            action = Action.Pdf2Word
        elif text == MainWindow.tr('menu_word2pdf'):
            action = Action.Word2Pdf
        elif text == MainWindow.tr('menu_excel2pdf'):
            action = Action.Excel2Pdf
        elif text == MainWindow.tr('menu_ppt2pdf'):
            action = Action.PPT2Pdf
        elif text == MainWindow.tr('menu_pdf_split'):
            action = Action.PDFSplit
        elif text == MainWindow.tr('menu_pdf_merge'):
            action = Action.PDFMerge

        if action == self.action:
            return

        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        self.action = action
        self.update_unclicked_tab_menu_color(self.tab_btn)
        self.update_clicked_tab_menu_color(btn)
        self.tab_btn = btn

        self.update_widget_text()

        self.reset_table()
        self.show_open_label()
        self.file_mng.clear()

    def on_show_theme(self):
        dlg = ThemeWindow(self, self.theme)
        dlg.theme_signal.connect(self.proc_theme_signal)
        dlg.show()
        
    def on_show_chinese(self):
        cn_checked = self.cn_menu.isChecked()
        en_checked = not cn_checked

        self.cn_menu.setChecked(cn_checked)
        self.en_menu.setChecked(en_checked)

        if cn_checked:
            self.translator.load('zh_CN')
            self.setting.save(Language.Chinese.value, self.theme.get_theme_name())
        else:
            self.translator.load('en_US')
            self.setting.save(Language.English.value, self.theme.get_theme_name())

        self.ui.retranslateUi(self)
        self.update_dynamic_widgets()
        
    def on_show_english(self):
        en_checked = self.en_menu.isChecked()
        cn_checked = not en_checked
        
        self.en_menu.setChecked(en_checked)
        self.cn_menu.setChecked(cn_checked)

        if en_checked:
            self.translator.load('en_US')
            self.setting.save(Language.English.value, self.theme.get_theme_name())
        else:
            self.translator.load('zh_CN')
            self.setting.save(Language.Chinese.value, self.theme.get_theme_name())

        self.ui.retranslateUi(self)
        self.update_dynamic_widgets()

    def on_show_feedback(self):
        dlg = FeedbackWindow(self, self.theme)
        dlg.show()

    def on_show_about(self):
        dlg = AboutWindow(self, self.theme)
        dlg.show()

    def proc_theme_signal(self, content):
        self.update_style_widgets()

        language = Language.Chinese if self.cn_menu and self.cn_menu.isChecked() else Language.English
        self.setting.save(language.value, FileUtils.get_name(content))

    def proc_convert_signal(self, content):
        content = json.loads(content)
        file_id = content['file_id']
        status = content['status']
        msg = content['msg']
        
        if status == ColumnStatus.Done.value:
            self.convert_done = True
            return
        
        self.update_status_column(file_id, status, msg)
        
        if status == ColumnStatus.End.value:
            self.update_action_column(file_id)

    def on_clear(self):
        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        self.reset_table()
        self.show_open_label()
        self.file_mng.clear()

    def thread_convert(self):
        checked_files = self.file_mng.checked_files
        for src_file in checked_files:
            file_id = self.file_mng.get_file_id(src_file)
            print("thread_convert:", file_id, src_file, self.action)

            self.thread.start(file_id)

            if len(self.output_dir) > 0:  # self path
                file_name = os.path.basename(src_file)
                dst_file = os.path.join(
                    self.output_dir, FileUtils.get_filename(file_name, self.action))
            else:
                dst_file = FileUtils.get_filename(src_file, self.action)

            print('src: ', src_file, self.action)
            print('dst: ', dst_file, self.action)

            self.thread.add(file_id, src_file, dst_file, self.action)

            self.file_mng.add_convert(src_file, dst_file)

        self.thread.wait()

    def on_convert(self):
        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        checked_files = self.file_mng.checked_files
        
        print(checked_files)

        if len(checked_files) == 0:
            return

        self.convert_done = False

        # noinspection PyBroadException
        try:
            thread = threading.Thread(target=self.thread_convert)
            thread.start()
        except:
            print('convert exception')

    def on_choose_file(self, e):
        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        if e.button() == Qt.LeftButton:
            dlg_title = TitleUtils.get_open_file(self.action)
            result = QFileDialog.getOpenFileName(self, MainWindow.tr(dlg_title), os.getcwd(), FileUtils.get_file_filter(self.action))
            # tuple(path, postfix)
            file_name = result[0]
            if len(file_name) > 0:
                if self.file_mng.exists(file_name):
                    return

                self.add_table_row(file_name)

    def on_choose_dir(self, index):
        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        if index == 0:
            self.output_dir = ''
            self.ui.lbl_path.setText('')
        elif index == 1:
            result = QFileDialog.getExistingDirectory(self, MainWindow.tr('title_open_folder'), os.getcwd())
            if len(result) > 0:
                self.output_dir = result
                self.ui.lbl_path.setText(result)
            else:
                self.output_dir = ''
                self.ui.com_dir.setCurrentIndex(0)

    def on_check_file(self, checked):
        self.file_mng.set_checked(self.sender(), checked)

    def on_open_src_file(self, e):
        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        if e.button() == Qt.LeftButton:
            widget = self.childAt(e.scenePosition().toPoint())

            src_file = self.file_mng.get_file(widget, FileType.SrcFile)
            if src_file:
                FileUtils.start_file(src_file)

    def on_open_dst_file(self, e):
        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        if e.button() == Qt.LeftButton:
            widget = self.childAt(e.scenePosition().toPoint())

            dst_file = self.file_mng.get_file(widget, FileType.DstFile)
            if dst_file:
                FileUtils.start_file(dst_file)

    def on_open_src_folder(self, e):
        if e.button() == Qt.LeftButton:
            widget = self.childAt(e.scenePosition().toPoint())

            src_dir = self.file_mng.get_file(widget, FileType.SrcDir)
            if src_dir:
                FileUtils.start_file(src_dir)

    def on_open_dst_folder(self, e):
        if e.button() == Qt.LeftButton:
            widget = self.childAt(e.scenePosition().toPoint())
            
            dst_dir = self.file_mng.get_file(widget, FileType.DstDir)
            if dst_dir:
                FileUtils.start_file(dst_dir)

    def on_section_clicked(self, column):
        if column != ColumnIndex.Check.value:
            return

        all_checks = []
        for i in range(self.ui.tbl_main.rowCount()):
            item = self.ui.tbl_main.cellWidget(i, ColumnIndex.Check.value)
            checks = item.findChildren(QCheckBox)
            all_checks.extend(checks)

        if self.check_state == Qt.Checked:
            state = Qt.Unchecked
            checked = False
        else:
            state = Qt.Checked
            checked = True

        for check in all_checks:
            check.setCheckState(state)

        self.check_state = state

        self.file_mng.set_all_checked(all_checks, checked)

    def on_item_selection_changed(self):
        if len(self.ui.tbl_main.selectedItems()) == 0 and len(self.file_mng.all_files) > 0:
            self.ui.tbl_main.selectRow(0)

    def on_delete_table_row(self, e):
        if not self.convert_done:
            toast = ToastWidget(self, self.theme, MainWindow.tr('tip_convert_running'))
            toast.show()
            return

        if e.button() == Qt.LeftButton:
            widget = self.childAt(e.scenePosition().toPoint())
            file_id = self.file_mng.get_widget_id(widget)
            row = self.get_row(file_id)
            self.ui.tbl_main.removeRow(row)
            self.file_mng.remove_file(widget)

    def get_cursor_direction(self, global_point):
        padding = 1

        rect = self.rect()
        top_left = self.mapToGlobal(rect.topLeft())
        bottom_right = self.mapToGlobal(rect.bottomRight())

        x = global_point.x()
        y = global_point.y()

        if top_left.x() + padding >= x >= top_left.x() and top_left.y() + padding >= y >= top_left.y():
            self.cursor_direction = CursorDirection.LeftTop
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif bottom_right.x() - padding <= x <= bottom_right.x() and bottom_right.y() - padding <= y <= bottom_right.y():
            self.cursor_direction = CursorDirection.RightBottom
            self.setCursor(QCursor(Qt.SizeFDiagCursor))
        elif top_left.x() + padding >= x >= top_left.x() and bottom_right.y() - padding <= y <= bottom_right.y():
            self.cursor_direction = CursorDirection.LeftBottom
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif bottom_right.x() >= x >= bottom_right.x() - padding and top_left.y() <= y <= top_left.y() + padding:
            self.cursor_direction = CursorDirection.RightTop
            self.setCursor(QCursor(Qt.SizeBDiagCursor))
        elif top_left.x() + padding >= x >= top_left.x():
            self.cursor_direction = CursorDirection.Left
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif bottom_right.x() >= x >= bottom_right.x() - padding:
            self.cursor_direction = CursorDirection.Right
            self.setCursor(QCursor(Qt.SizeHorCursor))
        elif top_left.y() <= y <= top_left.y() + padding:
            self.cursor_direction = CursorDirection.Up
            self.setCursor(QCursor(Qt.SizeVerCursor))
        elif bottom_right.y() >= y >= bottom_right.y() - padding:
            self.cursor_direction = CursorDirection.Down
            self.setCursor(QCursor(Qt.SizeVerCursor))
        else:
            self.cursor_direction = CursorDirection.Default
            self.setCursor(QCursor(Qt.ArrowCursor))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_btn_pressed = True

            if self.cursor_direction != CursorDirection.Default:
                self.mouseGrabber()
            else:
                self.drag_point = e.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        global_point = e.globalPos()
        rect = self.rect()
        top_left = self.mapToGlobal(rect.topLeft())
        bottom_right = self.mapToGlobal(rect.bottomRight())

        if not self.left_btn_pressed:
            self.get_cursor_direction(global_point)
        else:
            if self.cursor_direction != CursorDirection.Default:
                move_rect = QRect(top_left, bottom_right)

                if self.cursor_direction == CursorDirection.Left:
                    if bottom_right.x() - global_point.x() <= self.minimumWidth():
                        move_rect.setX(top_left.x())
                    else:
                        move_rect.setX(global_point.x())
                elif self.cursor_direction == CursorDirection.Right:
                    move_rect.setWidth(global_point.x() - top_left.x())
                elif self.cursor_direction == CursorDirection.Up:
                    if bottom_right.y() - global_point.y() <= self.minimumHeight():
                        move_rect.setY(top_left.y())
                    else:
                        move_rect.setY(global_point.y())
                elif self.cursor_direction == CursorDirection.Down:
                    move_rect.setHeight(global_point.y() - top_left.y())
                elif self.cursor_direction == CursorDirection.LeftTop:
                    if bottom_right.x() - global_point.x() <= self.minimumWidth():
                        move_rect.setX(top_left.x())
                    else:
                        move_rect.setX(global_point.x())

                    if bottom_right.y() - global_point.y() <= self.minimumHeight():
                        move_rect.setY(top_left.y())
                    else:
                        move_rect.setY(global_point.y())
                elif self.cursor_direction == CursorDirection.RightTop:
                    move_rect.setWidth(global_point.x() - top_left.x())
                    move_rect.setY(global_point.y())
                elif self.cursor_direction == CursorDirection.LeftBottom:
                    move_rect.setX(global_point.x())
                    move_rect.setHeight(global_point.y() - top_left.y())
                elif self.cursor_direction == CursorDirection.RightBottom:
                    move_rect.setWidth(global_point.x() - top_left.x())
                    move_rect.setHeight(global_point.y() - top_left.y())
                else:
                    pass

                self.setGeometry(move_rect)
            else:
                self.move(e.globalPos() - self.drag_point)
                e.accept()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_btn_pressed = False

            if self.cursor_direction != CursorDirection.Default:
                self.releaseMouse()
                self.setCursor(QCursor(Qt.ArrowCursor))
