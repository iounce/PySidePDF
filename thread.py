# -*- coding: utf-8 -*-

import threading
import json
from PySide6.QtCore import QObject, Signal

from action import Action
from converter import Converter
from column import ColumnStatus

class ConvertThread(QObject):
    thread_signal = Signal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.threads = []

    @staticmethod
    def gen_msg(file_id, status, msg):
        content = {'file_id': file_id, 'status': status, 'msg': msg}
        return json.dumps(content)

    def start(self, file_id):
        self.thread_signal.emit(self.gen_msg(file_id, ColumnStatus.Start.value, ''))

    def convert(self, file_id, src_file, dst_file, action):
        try:
            print('convert: ', src_file, '|', dst_file, '|', action)

            self.thread_signal.emit(self.gen_msg(file_id, ColumnStatus.Running.value, ''))

            Converter.convert(src_file, dst_file, action)

            self.thread_signal.emit(self.gen_msg(file_id, ColumnStatus.End.value, ''))
        except Exception as e:
            self.thread_signal.emit(self.gen_msg(file_id, ColumnStatus.Exception.value, str(e)))
            print(e)

    def add(self, file_id, src_file, dst_file, action):
        thread = None
        # noinspection PyBroadException
        try:
            thread = threading.Thread(target=self.convert, args=(file_id, src_file, dst_file, action))
            thread.start()
        except:
            thread = None
            print('thread exception')

        if thread:
            self.threads.append(thread)
            print('add: ', file_id, src_file, dst_file, action)

    def wait(self):
        # noinspection PyBroadException
        try:
            for thread in self.threads:
                thread.join()
        except:
            print('join exception')

        self.threads = []
        self.thread_signal.emit(self.gen_msg(-1, ColumnStatus.Done.value, ''))