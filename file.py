# -*- coding: utf-8 -*-

import enum
import os
from PySide6.QtWidgets import QCheckBox

class FileType(enum.Enum):
    SrcFile = 0
    DstFile = 1
    SrcDir = 2
    DstDir = 3

class FileManager:
    def __init__(self):
        self.file_id = 0
        self.all_files = []
        self.checked_files = []
        self.id2file = {}
        self.file2id = {}
        self.widget2id = {}
        self.src2dst = {}

    def gen_id(self):
        self.file_id += 1
        return self.file_id

    def get_file_id(self, file):
        return self.file2id.get(file)

    def get_widget_id(self, widget):
        return self.widget2id.get(widget)

    def get_check_widget(self, file_id):
        check_widget = None
        for (k,v) in self.widget2id.items():
            if v == file_id and isinstance(k, QCheckBox):
                check_widget = k
                break
        return check_widget

    def get_file(self, widget, file_type):
        result = None

        file_id = self.get_widget_id(widget)
        if file_id:
            file = self.id2file.get(file_id)
            if file_type == FileType.SrcFile:
                result = file
            elif file_type == FileType.DstFile:
                result = self.src2dst.get(file)
            elif file_type == FileType.SrcDir:
                result = os.path.dirname(file)
            elif file_type == FileType.DstDir:
                dst_file = self.src2dst.get(file)
                if dst_file:
                    result = os.path.dirname(dst_file)

        return result

    def remove_file(self, widget):
        file_id = self.get_widget_id(widget)
        if file_id:
            del self.widget2id[widget]

            file = self.id2file.get(file_id)
            if file:
                del self.id2file[file_id]
                del self.file2id[file]
                self.all_files.remove(file)

                if file in self.checked_files:
                    self.checked_files.remove(file)

                if file in self.src2dst:
                    del self.src2dst[file]

    def add_widget(self, widget, file_id):
        self.widget2id[widget] = file_id

    def add_file(self, file_id, file):
        self.id2file[file_id] = file
        self.file2id[file] = file_id
        self.all_files.append(file)
        self.checked_files.append(file)

    def add_convert(self, src_file, dst_file):
        self.src2dst[src_file] = dst_file

    def set_checked(self, widget, checked):
        pdf_file = self.get_file(widget, FileType.SrcFile)
        if checked:
            if pdf_file not in self.checked_files:
                self.checked_files.append(pdf_file)
        else:
            if pdf_file in self.checked_files:
                self.checked_files.remove(pdf_file)

    def set_all_checked(self, widgets, checked):
        self.checked_files = []
        if checked:
            for widget in widgets:
                pdf_file = self.get_file(widget, FileType.SrcFile)
                self.checked_files.append(pdf_file)

    def exists(self, file):
        return file in self.all_files

    def clear(self):
        self.all_files = []
        self.checked_files = []
        self.id2file = {}
        self.file2id = {}
        self.widget2id = {}
        self.src2dst = {}


