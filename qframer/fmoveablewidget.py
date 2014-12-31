#!/usr/bin/python
# -*- coding: utf-8 -*-

from .qt.QtCore import *
from .qt.QtGui import *

from .ftitlebar import FTitleBar
from .fstatusbar import FStatusBar


class FMoveableWidget(QFrame):

    def __init__(self, parent=None):
        super(FMoveableWidget, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setFocus()
        # 鼠标点击事件
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - \
                self.frameGeometry().topLeft()
            event.accept()

    def mouseReleaseEvent(self, event):
        # 鼠标释放事件
        if hasattr(self, "dragPosition"):
            del self.dragPosition

    def mouseMoveEvent(self, event):        
        if hasattr(self, "dragPosition"):
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
