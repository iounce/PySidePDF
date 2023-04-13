# -*- coding: utf-8 -*-

import enum

class Action(enum.Enum):
    Pdf2Word = 10
    Pdf2Excel = 11
    Pdf2PPT = 12
    Pdf2Image = 13
    Word2Pdf = 20
    Excel2Pdf = 21
    PPT2Pdf = 22
    PDFSplit = 30
    PDFMerge = 31