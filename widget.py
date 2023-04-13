# -*- coding: utf-8 -*-

import enum

class WidgetType(enum.Enum):
    StatusProgressBar = 0
    StatusLabel = 1
    DynamicWidget = 2
    StyleWidget = 3

class WidgetManager:
    def __init__(self):
        self.id2widget = {}
        self.widget2text = {}
        self.text2widget = {}

    @staticmethod
    def key(file_id, widget_type):
        return str(file_id) + '_' + str(widget_type.value)

    def add(self, widget, text = None, file_id = None, widget_type = None):
        if widget_type == WidgetType.DynamicWidget:
            self.widget2text[widget] = text
        elif widget_type == WidgetType.StyleWidget:
            self.text2widget[text] = widget
        else:
            self.id2widget[self.key(file_id, widget_type)] = widget

    def get(self, widget = None, file_id = None, widget_type = None):
        if widget_type == WidgetType.DynamicWidget:
            return self.widget2text.get(widget)
        else:
            return self.id2widget.get(self.key(file_id, widget_type))

    def get_all(self, widget_type):
        widgets = {}
        if widget_type == WidgetType.DynamicWidget:
            widgets = self.widget2text
        elif widget_type == WidgetType.StyleWidget:
            widgets = self.text2widget
        return widgets

    def clear(self):
        self.id2widget = {}
        self.widget2text = {}
        self.text2widget = {}