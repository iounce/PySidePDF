# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time

from PySide6.QtCore import QSize
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QPushButton

from action import Action
from language import Language
from office import Office
from pdf import PdfFile
from theme import Theme

class StringUtils:
    @staticmethod
    def contains(string, substring):
        return string.find(substring) != -1

class FileUtils:
    @staticmethod
    def get_name(filename):
        return os.path.splitext(filename)[0]

    @staticmethod
    def get_fullname(name, ext = '.xml'):
        if ext in name:
            return name
        return name + ext

    @staticmethod
    def get_filename(src_file, action):
        if action == Action.Pdf2Word:
            return src_file.replace('.pdf', '.docx')
        elif action == Action.Pdf2Excel:
            return src_file.replace('.pdf', '.xlsx')
        elif action == Action.Pdf2PPT:
            return src_file.replace('.pdf', '.pptx')
        elif action == Action.Pdf2Image:
            return src_file.replace('.pdf', '.png')
        elif action == Action.Word2Pdf:
            return src_file.replace('.docx', '.pdf')
        elif action == Action.Excel2Pdf:
            return src_file.replace('.xlsx', '.pdf')
        elif action == Action.PPT2Pdf:
            return src_file.replace('.pptx', '.pdf')
        else:
            return src_file

    @staticmethod
    def get_file_filter(action):
        if action == Action.Pdf2Word:
            return 'pdf(*.pdf)'
        elif action == Action.Pdf2Excel:
            return 'pdf(*.pdf)'
        elif action == Action.Pdf2PPT:
            return 'pdf(*.pdf)'
        elif action == Action.Pdf2Image:
            return 'pdf(*.pdf)'
        elif action == Action.Word2Pdf:
            return 'docx(*.docx)'
        elif action == Action.Excel2Pdf:
            return 'xlsx(*.xlsx)'
        elif action == Action.PPT2Pdf:
            return 'pptx(*.pptx)'
        else:
            return '(*.*)'

    @staticmethod
    def start_file(path):
        if sys.platform.find('win32') != -1:
            os.startfile(path)
        elif sys.platform.find('darwin') != -1:
            subprocess.call(["open", path])
        elif sys.platform.find('linux') != -1:
            subprocess.call(["xdg-open", path])

class TitleUtils:
    @staticmethod
    def get_open_file(action):
        if action == Action.Pdf2Word:
            return 'title_open_pdf'
        elif action == Action.Pdf2Excel:
            return 'title_open_pdf'
        elif action == Action.Pdf2PPT:
            return 'title_open_pdf'
        elif action == Action.Pdf2Image:
            return 'title_open_pdf'
        elif action == Action.Word2Pdf:
            return 'title_open_word'
        elif action == Action.Excel2Pdf:
            return 'title_open_excel'
        elif action == Action.PPT2Pdf:
            return 'title_open_ppt'
        else:
            return ''

class PageUtils:
    @staticmethod
    def get_count(src_file, action):
        count = -1
        try:
            if action == Action.Pdf2Word:
                count = PdfFile.get_page_count(src_file)
        except Exception as e:
            print(e)

        return count

class DateUtils:
    @staticmethod
    def get_year():
        return time.strftime('%Y', time.localtime(time.time()))

    @staticmethod
    def get_date():
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))

class ColorUtils:
    @staticmethod
    def hex2rgb(color):
        value = int(color[1:], 16)
        rgb_color = QColor(value)
        rgb_color = QColor(rgb_color.red(), rgb_color.green(), rgb_color.blue())
        return rgb_color.rgb()

class ButtonUtils:
    @staticmethod
    def get_tab(icon, text, style, checked):
        btn = QPushButton()
        btn.setFlat(True)
        btn.setCheckable(True)
        btn.setChecked(checked)
        btn.setAutoExclusive(True)
        btn.setIcon(icon)
        btn.setIconSize(QSize(24, 24))
        btn.setText(text)
        btn.setStyleSheet(style)
        return btn

class LanguageUtils:
    @staticmethod
    def validate(language):
        languages = [Language.Chinese.value, Language.English.value]
        return language in languages

class ThemeUtils:
    @staticmethod
    def validate(theme):
        theme = FileUtils.get_fullname(theme)
        return theme in Theme.get_all_themes()