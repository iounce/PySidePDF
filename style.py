# -*- coding: utf-8 -*-

from PySide6.QtGui import QColor

from utils import ColorUtils, StringUtils

class LabelStyle:
    @staticmethod
    def get_title():
        return 'QLabel{font-size:16px; padding-left:8px}'

    @staticmethod
    def get_open_hover(color):
        return 'QLabel:hover{background-color:%s}' % color

    @staticmethod
    def get_open(name):
        return 'QLabel#%s{border-width:1px;border-style:solid}' % name

    @staticmethod
    def get_table_open(name, color):
        return 'QLabel#%s{border-width:1px;border-style:dashed;border-color:%s} QLabel:hover#%s{background-color:%s}' % (
            name, color, name, color)

    @staticmethod
    def get_action(color):
        return 'QLabel:hover{background-color:%s}' % color

    @staticmethod
    def get_close():
        return 'QLabel:hover{background-color:red}'

    @staticmethod
    def get_default():
        return 'QLabel{padding-left:14px; border-radius:6px;border-width:1px;border-color:black;border-style: solid} QLabel:hover{border-width:2px;}'

    @staticmethod
    def get_theme(color):
        return 'QLabel{padding-left:10px; background-color: %s} QLabel:hover{border-width:1px; border-style: solid}' % color

class ButtonStyle:
    @staticmethod
    def get_close():
        return 'QPushButton:hover{background-color:red}'

    @staticmethod
    def get_more():
        return 'QPushButton::menu-indicator{width:0px}'

    @staticmethod
    def get_tab(bkg_color, theme):
        if StringUtils.contains(theme.get_theme_name(), 'dark'):
            text_color = '#f5f5f5'
        else:
            text_color = '#424242'
        return 'QPushButton{background-color:%s; color:%s; text-align: left;}' % (bkg_color, text_color)

    @staticmethod
    def get_action():
        return 'QPushButton:hover{border-style:solid;border-width:3px}'

class MenuStyle:
    @staticmethod
    def get_more():
        return 'QMenu::item{height:20px; width:100px}'

class WidgetStyle:
    @staticmethod
    def get_selection(color):
        return 'QWidget{background-color:%s}' % color

    @staticmethod
    def get_border(name):
        return 'QWidget#%s{border:1px solid; border-color:#4f5b62}' % name

    @staticmethod
    def get_action(color):
        rgb = int(color[1:], 16)
        rgb_color = QColor(rgb)
        color = QColor(rgb_color.red(), rgb_color.green(), rgb_color.blue())
        return 'QWidget{background-color:%s}' % color.rgb()

class TableWidgetStyle:
    @staticmethod
    def get_selection(bkg_color, text_color):
        return 'QTableWidget::item::selected{background:%s; selection-color:%s}' \
        % (ColorUtils.hex2rgb(bkg_color), ColorUtils.hex2rgb(text_color))

class ProgressBarStyle:
    @staticmethod
    def get_action(color):
        return 'QProgressBar{border-radius:20px;background-color: %s}  \
        QProgressBar::chunk{border-radius:20px;width:6px;margin:1px;background-color: #ff5722}' % color