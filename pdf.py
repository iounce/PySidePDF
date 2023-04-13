# -*- coding: utf-8 -*-

import pdfplumber

class PdfFile:
    @staticmethod
    def get_page_count(filename):
        # noinspection PyBroadException
        try:
            pdf = pdfplumber.open(filename)
            count = len(pdf.pages)
        except FileNotFoundError:
            count = 0
        except:
            count = 0

        return count