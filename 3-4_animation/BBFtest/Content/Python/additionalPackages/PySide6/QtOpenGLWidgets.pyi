# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.QtOpenGLWidgets, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.QtOpenGLWidgets`

import PySide6.QtOpenGLWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import enum
import typing
from PySide6.QtCore import Signal


class QIntList(object): ...


class QOpenGLWidget(PySide6.QtWidgets.QWidget):

    aboutToCompose           : typing.ClassVar[Signal] = ... # aboutToCompose()
    aboutToResize            : typing.ClassVar[Signal] = ... # aboutToResize()
    frameSwapped             : typing.ClassVar[Signal] = ... # frameSwapped()
    resized                  : typing.ClassVar[Signal] = ... # resized()

    class TargetBuffer(enum.Enum):

        LeftBuffer                = ...  # 0x0
        RightBuffer               = ...  # 0x1

    class UpdateBehavior(enum.Enum):

        NoPartialUpdate           = ...  # 0x0
        PartialUpdate             = ...  # 0x1


    def __init__(self, parent: PySide6.QtWidgets.QWidget | None= ..., f: PySide6.QtCore.Qt.WindowType = ...) -> None: ...

    def context(self) -> PySide6.QtGui.QOpenGLContext: ...
    def currentTargetBuffer(self) -> PySide6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer: ...
    @typing.overload
    def defaultFramebufferObject(self) -> int: ...
    @typing.overload
    def defaultFramebufferObject(self, targetBuffer: PySide6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer) -> int: ...
    def doneCurrent(self) -> None: ...
    def event(self, e: PySide6.QtCore.QEvent) -> bool: ...
    def format(self) -> PySide6.QtGui.QSurfaceFormat: ...
    @typing.overload
    def grabFramebuffer(self) -> PySide6.QtGui.QImage: ...
    @typing.overload
    def grabFramebuffer(self, targetBuffer: PySide6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer) -> PySide6.QtGui.QImage: ...
    def initializeGL(self) -> None: ...
    def isValid(self) -> bool: ...
    @typing.overload
    def makeCurrent(self) -> None: ...
    @typing.overload
    def makeCurrent(self, targetBuffer: PySide6.QtOpenGLWidgets.QOpenGLWidget.TargetBuffer) -> None: ...
    def metric(self, metric: PySide6.QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def paintEngine(self) -> PySide6.QtGui.QPaintEngine: ...
    def paintEvent(self, e: PySide6.QtGui.QPaintEvent) -> None: ...
    def paintGL(self) -> None: ...
    def redirected(self, p: PySide6.QtCore.QPoint) -> PySide6.QtGui.QPaintDevice: ...
    def resizeEvent(self, e: PySide6.QtGui.QResizeEvent) -> None: ...
    def resizeGL(self, w: int, h: int) -> None: ...
    def setFormat(self, format: PySide6.QtGui.QSurfaceFormat | PySide6.QtGui.QSurfaceFormat.FormatOption) -> None: ...
    def setTextureFormat(self, texFormat: int) -> None: ...
    def setUpdateBehavior(self, updateBehavior: PySide6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior) -> None: ...
    def textureFormat(self) -> int: ...
    def updateBehavior(self) -> PySide6.QtOpenGLWidgets.QOpenGLWidget.UpdateBehavior: ...


# eof