# -*- coding: utf-8 -*-

import enum
import sys

from win32com import client

from action import Action

class OfficeType(enum.Enum):
    Word = 1
    Excel = 2
    PPT = 3

class OfficeApp:
    App_Office_Word = "Word.Application"
    App_Office_Excel = "Excel.Application"
    App_Office_PPT = "Powerpoint.Application"
    App_WPS_Word = "Kwps.Application"
    App_WPS_Excel = "Ket.Application"
    App_WPS_PPT = "Kwpp.Application"

class Office:
    @staticmethod
    def is_windows():
        if sys.platform.find('win32') != -1:
            return True
        else:
            return False

    @staticmethod
    def get_app_name(office_type):
        if office_type == OfficeType.Word:
            return OfficeApp.App_Office_Word, OfficeApp.App_WPS_Word
        elif office_type == OfficeType.Excel:
            return OfficeApp.App_Office_Excel, OfficeApp.App_WPS_Excel
        elif office_type == OfficeType.PPT:
            return OfficeApp.App_Office_PPT, OfficeApp.App_WPS_PPT
        else:
            return None

    @staticmethod
    def get_app(office_type):
        app_name = Office.get_app_name(office_type)
        if not app_name:
            return

        app = client.Dispatch(app_name[0])
        if not app:
            app = client.Dispatch(app_name[1])

        return app

    @staticmethod
    def get_page_count(src_file, action):
        if not Office.is_windows():
            raise Exception('Unsupported platform!')

        if action == Action.Word2Pdf:
            office_type = OfficeType.Word
        elif action == Action.Excel2Pdf:
            office_type = OfficeType.Excel
        elif action == Action.PPT2Pdf:
            office_type = OfficeType.PPT
        else:
            return -1

        app = Office.get_app(office_type)
        if not app:
            return -1

        if office_type == OfficeType.Word:
            return Office.get_word_count(src_file)
        elif office_type == OfficeType.Excel:
            return Office.get_excel_count(src_file)
        elif office_type == OfficeType.PPT:
            return Office.get_ppt_count(src_file)
        else:
            return -1

    @staticmethod
    def get_word_count(src_file):
        if not Office.is_windows():
            raise Exception('Unsupported platform!')

        word = Office.get_app(OfficeType.Word)
        if not word:
            return -1

        doc = word.Documents.Open(src_file)
        doc.Repaginate()
        count = doc.ComputeStatistics(2)
        doc.Close()

        word.Quit()

        return count

    @staticmethod
    def get_excel_count(src_file):
        if not Office.is_windows():
            raise Exception('Unsupported platform!')

        excel = Office.get_app(OfficeType.Excel)
        if not excel:
            return -1

        doc = excel.Workbooks.Open(src_file)
        count = doc.Sheets.Count
        doc.Close()

        excel.Quit()

        return count

    @staticmethod
    def get_ppt_count(src_file):
        if not Office.is_windows():
            raise Exception('Unsupported platform!')

        ppt = Office.get_app(OfficeType.PPT)
        if not ppt:
            return -1

        doc = ppt.Presentations.Open(src_file)
        count = len(doc.slides)
        doc.Close()

        ppt.Quit()

        return count

    @staticmethod
    def word2pdf(src_file, dst_file):
        if not Office.is_windows():
            raise Exception('Unsupported platform!')

        word = Office.get_app(OfficeType.Word)
        if not word:
            return

        doc = word.Documents.Open(src_file)
        doc.SaveAs(dst_file, FileFormat=17)
        doc.Close()

        word.Quit()

    @staticmethod
    def excel2pdf(src_file, dst_file):
        if not Office.is_windows():
            raise Exception('Unsupported platform!')

        excel = Office.get_app(OfficeType.Excel)
        if not excel:
            return

        doc = excel.Workbooks.Open(src_file)
        #doc.SaveAs(dst_file, FileFormat=57)
        doc.ExportAsFixedFormat(0, dst_file)
        doc.Close()

        excel.Quit()

    @staticmethod
    def ppt2pdf(src_file, dst_file):
        if not Office.is_windows():
            raise Exception('Unsupported platform!')

        ppt = Office.get_app(OfficeType.PPT)
        if not ppt:
            return

        doc = ppt.Presentations.Open(src_file)
        doc.SaveAs(dst_file, FileFormat=32)
        doc.Close()

        ppt.Quit()