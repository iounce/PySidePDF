# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator

from icon import LogoIcon
from main_window import MainWindow
from setting import Setting
from theme import Theme

if __name__ == "__main__":
    setting = Setting()
    setting.load()

    locale = setting.get_locale()
    theme = setting.get_theme()

    print('main:', locale, theme)

    translator = QTranslator()
    translator.load(locale)

    app = QApplication(sys.argv)

    app.installTranslator(translator)

    window = MainWindow(Theme(app, theme), translator, setting)
    window.setWindowIcon(LogoIcon.get_icon())
    window.show()

    sys.exit(app.exec())
