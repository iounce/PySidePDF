# -*- coding: utf-8 -*-

import enum

class ColumnIndex(enum.Enum):
    Check = 0
    Name = 1
    Count = 2
    Range = 3
    Status = 4
    Action = 5

class ColumnStatus(enum.Enum):
    Init = 0
    Start = 1
    Running = 2
    End = 3
    Exception = 4
    Done = 5