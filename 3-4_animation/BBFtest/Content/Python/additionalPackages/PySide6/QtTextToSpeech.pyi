# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.QtTextToSpeech, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.QtTextToSpeech`

import PySide6.QtTextToSpeech
import PySide6.QtCore

import enum
import typing
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QIntList(object): ...


class QTextToSpeech(PySide6.QtCore.QObject):

    aboutToSynthesize        : typing.ClassVar[Signal] = ... # aboutToSynthesize(qsizetype)
    engineChanged            : typing.ClassVar[Signal] = ... # engineChanged(QString)
    errorOccurred            : typing.ClassVar[Signal] = ... # errorOccurred(QTextToSpeech::ErrorReason,QString)
    localeChanged            : typing.ClassVar[Signal] = ... # localeChanged(QLocale)
    pitchChanged             : typing.ClassVar[Signal] = ... # pitchChanged(double)
    rateChanged              : typing.ClassVar[Signal] = ... # rateChanged(double)
    sayingWord               : typing.ClassVar[Signal] = ... # sayingWord(QString,qsizetype,qsizetype,qsizetype)
    stateChanged             : typing.ClassVar[Signal] = ... # stateChanged(QTextToSpeech::State)
    voiceChanged             : typing.ClassVar[Signal] = ... # voiceChanged(QVoice)
    volumeChanged            : typing.ClassVar[Signal] = ... # volumeChanged(double)

    class BoundaryHint(enum.Enum):

        Default                   = ...  # 0x0
        Immediate                 = ...  # 0x1
        Word                      = ...  # 0x2
        Sentence                  = ...  # 0x3
        Utterance                 = ...  # 0x4

    class Capability(enum.Flag):

        None_                     = ...  # 0x0
        Speak                     = ...  # 0x1
        PauseResume               = ...  # 0x2
        WordByWordProgress        = ...  # 0x4
        Synthesize                = ...  # 0x8

    class ErrorReason(enum.Enum):

        NoError                   = ...  # 0x0
        Initialization            = ...  # 0x1
        Configuration             = ...  # 0x2
        Input                     = ...  # 0x3
        Playback                  = ...  # 0x4

    class State(enum.Enum):

        Ready                     = ...  # 0x0
        Speaking                  = ...  # 0x1
        Paused                    = ...  # 0x2
        Error                     = ...  # 0x3
        Synthesizing              = ...  # 0x4


    @typing.overload
    def __init__(self, engine: str, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, engine: str, params: typing.Dict[str, typing.Any], parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def allVoices(self, locale: PySide6.QtCore.QLocale | PySide6.QtCore.QLocale.Language) -> typing.List[PySide6.QtTextToSpeech.QVoice]: ...
    @staticmethod
    def availableEngines() -> typing.List[str]: ...
    def availableLocales(self) -> typing.List[PySide6.QtCore.QLocale]: ...
    def availableVoices(self) -> typing.List[PySide6.QtTextToSpeech.QVoice]: ...
    def engine(self) -> str: ...
    def engineCapabilities(self) -> PySide6.QtTextToSpeech.QTextToSpeech.Capability: ...
    def enqueue(self, text: str) -> int: ...
    def errorReason(self) -> PySide6.QtTextToSpeech.QTextToSpeech.ErrorReason: ...
    def errorString(self) -> str: ...
    def locale(self) -> PySide6.QtCore.QLocale: ...
    def pause(self, boundaryHint: PySide6.QtTextToSpeech.QTextToSpeech.BoundaryHint = ...) -> None: ...
    def pitch(self) -> float: ...
    def rate(self) -> float: ...
    def resume(self) -> None: ...
    def say(self, text: str) -> None: ...
    def setEngine(self, engine: str, params: typing.Dict[str, typing.Any] = ...) -> bool: ...
    def setLocale(self, locale: PySide6.QtCore.QLocale | PySide6.QtCore.QLocale.Language) -> None: ...
    def setPitch(self, pitch: float) -> None: ...
    def setRate(self, rate: float) -> None: ...
    def setVoice(self, voice: PySide6.QtTextToSpeech.QVoice) -> None: ...
    def setVolume(self, volume: float) -> None: ...
    def state(self) -> PySide6.QtTextToSpeech.QTextToSpeech.State: ...
    def stop(self, boundaryHint: PySide6.QtTextToSpeech.QTextToSpeech.BoundaryHint = ...) -> None: ...
    def voice(self) -> PySide6.QtTextToSpeech.QVoice: ...
    def volume(self) -> float: ...


class QTextToSpeechEngine(PySide6.QtCore.QObject):

    errorOccurred            : typing.ClassVar[Signal] = ... # errorOccurred(QTextToSpeech::ErrorReason,QString)
    sayingWord               : typing.ClassVar[Signal] = ... # sayingWord(QString,qsizetype,qsizetype)
    stateChanged             : typing.ClassVar[Signal] = ... # stateChanged(QTextToSpeech::State)
    synthesized              : typing.ClassVar[Signal] = ... # synthesized(QAudioFormat,QByteArray)

    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def availableLocales(self) -> typing.List[PySide6.QtCore.QLocale]: ...
    def availableVoices(self) -> typing.List[PySide6.QtTextToSpeech.QVoice]: ...
    def capabilities(self) -> PySide6.QtTextToSpeech.QTextToSpeech.Capability: ...
    @staticmethod
    def createVoice(name: str, locale: PySide6.QtCore.QLocale | PySide6.QtCore.QLocale.Language, gender: PySide6.QtTextToSpeech.QVoice.Gender, age: PySide6.QtTextToSpeech.QVoice.Age, data: typing.Any) -> PySide6.QtTextToSpeech.QVoice: ...
    def errorReason(self) -> PySide6.QtTextToSpeech.QTextToSpeech.ErrorReason: ...
    def errorString(self) -> str: ...
    def locale(self) -> PySide6.QtCore.QLocale: ...
    def pause(self, boundaryHint: PySide6.QtTextToSpeech.QTextToSpeech.BoundaryHint) -> None: ...
    def pitch(self) -> float: ...
    def rate(self) -> float: ...
    def resume(self) -> None: ...
    def say(self, text: str) -> None: ...
    def setLocale(self, locale: PySide6.QtCore.QLocale | PySide6.QtCore.QLocale.Language) -> bool: ...
    def setPitch(self, pitch: float) -> bool: ...
    def setRate(self, rate: float) -> bool: ...
    def setVoice(self, voice: PySide6.QtTextToSpeech.QVoice) -> bool: ...
    def setVolume(self, volume: float) -> bool: ...
    def state(self) -> PySide6.QtTextToSpeech.QTextToSpeech.State: ...
    def stop(self, boundaryHint: PySide6.QtTextToSpeech.QTextToSpeech.BoundaryHint) -> None: ...
    def synthesize(self, text: str) -> None: ...
    def voice(self) -> PySide6.QtTextToSpeech.QVoice: ...
    @staticmethod
    def voiceData(voice: PySide6.QtTextToSpeech.QVoice) -> typing.Any: ...
    def volume(self) -> float: ...


class QVoice(Shiboken.Object):

    class Age(enum.Enum):

        Child                     = ...  # 0x0
        Teenager                  = ...  # 0x1
        Adult                     = ...  # 0x2
        Senior                    = ...  # 0x3
        Other                     = ...  # 0x4

    class Gender(enum.Enum):

        Male                      = ...  # 0x0
        Female                    = ...  # 0x1
        Unknown                   = ...  # 0x2


    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: PySide6.QtTextToSpeech.QVoice) -> None: ...

    def __copy__(self) -> typing.Self: ...
    def __eq__(self, rhs: PySide6.QtTextToSpeech.QVoice) -> bool: ...
    def __lshift__(self, str: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def __ne__(self, rhs: PySide6.QtTextToSpeech.QVoice) -> bool: ...
    def __repr__(self) -> str: ...
    def __rshift__(self, str: PySide6.QtCore.QDataStream) -> PySide6.QtCore.QDataStream: ...
    def age(self) -> PySide6.QtTextToSpeech.QVoice.Age: ...
    @staticmethod
    def ageName(age: PySide6.QtTextToSpeech.QVoice.Age) -> str: ...
    def gender(self) -> PySide6.QtTextToSpeech.QVoice.Gender: ...
    @staticmethod
    def genderName(gender: PySide6.QtTextToSpeech.QVoice.Gender) -> str: ...
    def language(self) -> PySide6.QtCore.QLocale.Language: ...
    def locale(self) -> PySide6.QtCore.QLocale: ...
    def name(self) -> str: ...
    def swap(self, other: PySide6.QtTextToSpeech.QVoice) -> None: ...


# eof