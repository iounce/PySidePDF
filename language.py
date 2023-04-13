# -*- coding: utf-8 -*-

import enum

class Language(enum.Enum):
    Chinese = 1
    English = 2

class Locale:
    Chinese = 'zh_CN'
    English = 'en_US'