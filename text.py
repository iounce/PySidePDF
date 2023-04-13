# -*- coding: utf-8 -*-

import enum

from action import Action

class TextType(enum.Enum):
    OutputPathComboBox = 1
    OpenFileDialog = 2
    AddFileLabel = 3
    OpenFileLabel = 4
    StartFileLabel = 5

class Text:
    @staticmethod
    def get(action, text_type):
        text = ''
        if action == Action.Pdf2Word:
            if text_type == TextType.OutputPathComboBox:
                text = 'title_pdf_path'
            elif text_type == TextType.OpenFileDialog:
                text = 'title_open_pdf'
            elif text_type == TextType.AddFileLabel:
                text = 'tip_add_pdf'
            elif text_type == TextType.OpenFileLabel:
                text = 'tip_open_pdf'
            elif text_type == TextType.StartFileLabel:
                text = 'tip_open_word'
        elif action == Action.Word2Pdf:
            if text_type == TextType.OutputPathComboBox:
                text = 'title_word_path'
            elif text_type == TextType.OpenFileDialog:
                text = 'title_open_word'
            elif text_type == TextType.AddFileLabel:
                text = 'tip_add_word'
            elif text_type == TextType.OpenFileLabel:
                text = 'tip_open_word'
            elif text_type == TextType.StartFileLabel:
                text = 'tip_open_pdf'
        elif action == Action.Excel2Pdf:
            if text_type == TextType.OutputPathComboBox:
                text = 'title_excel_path'
            elif text_type == TextType.OpenFileDialog:
                text = 'title_open_excel'
            elif text_type == TextType.AddFileLabel:
                text = 'tip_add_excel'
            elif text_type == TextType.OpenFileLabel:
                text = 'tip_open_excel'
            elif text_type == TextType.StartFileLabel:
                text = 'tip_open_pdf'
        elif action == Action.PPT2Pdf:
            if text_type == TextType.OutputPathComboBox:
                text = 'title_ppt_path'
            elif text_type == TextType.OpenFileDialog:
                text = 'title_open_ppt'
            elif text_type == TextType.AddFileLabel:
                text = 'tip_add_ppt'
            elif text_type == TextType.OpenFileLabel:
                text = 'tip_open_ppt'
            elif text_type == TextType.StartFileLabel:
                text = 'tip_open_pdf'

        return text