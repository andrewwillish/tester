# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.QtHelp, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.QtHelp`

import PySide6.QtHelp
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets

import enum
import typing
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QCompressedHelpInfo(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: PySide6.QtHelp.QCompressedHelpInfo) -> None: ...

    def __copy__(self) -> typing.Self: ...
    def component(self) -> str: ...
    @staticmethod
    def fromCompressedHelpFile(documentationFileName: str) -> PySide6.QtHelp.QCompressedHelpInfo: ...
    def isNull(self) -> bool: ...
    def namespaceName(self) -> str: ...
    def swap(self, other: PySide6.QtHelp.QCompressedHelpInfo) -> None: ...
    def version(self) -> PySide6.QtCore.QVersionNumber: ...


class QHelpContentItem(Shiboken.Object):
    def child(self, row: int) -> PySide6.QtHelp.QHelpContentItem: ...
    def childCount(self) -> int: ...
    def childPosition(self, child: PySide6.QtHelp.QHelpContentItem) -> int: ...
    def parent(self) -> PySide6.QtHelp.QHelpContentItem: ...
    def row(self) -> int: ...
    def title(self) -> str: ...
    def url(self) -> PySide6.QtCore.QUrl: ...


class QHelpContentModel(PySide6.QtCore.QAbstractItemModel):

    contentsCreated          : typing.ClassVar[Signal] = ... # contentsCreated()
    contentsCreationStarted  : typing.ClassVar[Signal] = ... # contentsCreationStarted()
    def columnCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex= ...) -> int: ...
    def contentItemAt(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> PySide6.QtHelp.QHelpContentItem: ...
    def createContents(self, customFilterName: str) -> None: ...
    def createContentsForCurrentFilter(self) -> None: ...
    def data(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, role: int) -> typing.Any: ...
    def index(self, row: int, column: int, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex= ...) -> PySide6.QtCore.QModelIndex: ...
    def isCreatingContents(self) -> bool: ...
    @typing.overload
    def parent(self) -> PySide6.QtCore.QObject: ...
    @typing.overload
    def parent(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> PySide6.QtCore.QModelIndex: ...
    def rowCount(self, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex= ...) -> int: ...


class QHelpContentWidget(PySide6.QtWidgets.QTreeView):

    linkActivated            : typing.ClassVar[Signal] = ... # linkActivated(QUrl)
    def indexOf(self, link: PySide6.QtCore.QUrl | str) -> PySide6.QtCore.QModelIndex: ...


class QHelpEngine(PySide6.QtHelp.QHelpEngineCore):

    def __init__(self, collectionFile: str, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def contentModel(self) -> PySide6.QtHelp.QHelpContentModel: ...
    def contentWidget(self) -> PySide6.QtHelp.QHelpContentWidget: ...
    def indexModel(self) -> PySide6.QtHelp.QHelpIndexModel: ...
    def indexWidget(self) -> PySide6.QtHelp.QHelpIndexWidget: ...
    def searchEngine(self) -> PySide6.QtHelp.QHelpSearchEngine: ...


class QHelpEngineCore(PySide6.QtCore.QObject):

    currentFilterChanged     : typing.ClassVar[Signal] = ... # currentFilterChanged(QString)
    readersAboutToBeInvalidated: typing.ClassVar[Signal] = ... # readersAboutToBeInvalidated()
    setupFinished            : typing.ClassVar[Signal] = ... # setupFinished()
    setupStarted             : typing.ClassVar[Signal] = ... # setupStarted()
    warning                  : typing.ClassVar[Signal] = ... # warning(QString)

    def __init__(self, collectionFile: str, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def addCustomFilter(self, filterName: str, attributes: typing.Sequence[str]) -> bool: ...
    def autoSaveFilter(self) -> bool: ...
    def collectionFile(self) -> str: ...
    def copyCollectionFile(self, fileName: str) -> bool: ...
    def currentFilter(self) -> str: ...
    def customFilters(self) -> typing.List[str]: ...
    def customValue(self, key: str, defaultValue: typing.Any = ...) -> typing.Any: ...
    def documentationFileName(self, namespaceName: str) -> str: ...
    @typing.overload
    def documentsForIdentifier(self, id: str) -> typing.List[PySide6.QtHelp.QHelpLink]: ...
    @typing.overload
    def documentsForIdentifier(self, id: str, filterName: str) -> typing.List[PySide6.QtHelp.QHelpLink]: ...
    @typing.overload
    def documentsForKeyword(self, keyword: str) -> typing.List[PySide6.QtHelp.QHelpLink]: ...
    @typing.overload
    def documentsForKeyword(self, keyword: str, filterName: str) -> typing.List[PySide6.QtHelp.QHelpLink]: ...
    def error(self) -> str: ...
    def fileData(self, url: PySide6.QtCore.QUrl | str) -> PySide6.QtCore.QByteArray: ...
    @typing.overload
    def files(self, namespaceName: str, filterName: str, extensionFilter: str = ...) -> typing.List[PySide6.QtCore.QUrl]: ...
    @typing.overload
    def files(self, namespaceName: str, filterAttributes: typing.Sequence[str], extensionFilter: str = ...) -> typing.List[PySide6.QtCore.QUrl]: ...
    def filterAttributeSets(self, namespaceName: str) -> typing.List[typing.List[str]]: ...
    @typing.overload
    def filterAttributes(self) -> typing.List[str]: ...
    @typing.overload
    def filterAttributes(self, filterName: str) -> typing.List[str]: ...
    def filterEngine(self) -> PySide6.QtHelp.QHelpFilterEngine: ...
    def findFile(self, url: PySide6.QtCore.QUrl | str) -> PySide6.QtCore.QUrl: ...
    def isReadOnly(self) -> bool: ...
    @staticmethod
    def metaData(documentationFileName: str, name: str) -> typing.Any: ...
    @staticmethod
    def namespaceName(documentationFileName: str) -> str: ...
    def registerDocumentation(self, documentationFileName: str) -> bool: ...
    def registeredDocumentations(self) -> typing.List[str]: ...
    def removeCustomFilter(self, filterName: str) -> bool: ...
    def removeCustomValue(self, key: str) -> bool: ...
    def setAutoSaveFilter(self, save: bool) -> None: ...
    def setCollectionFile(self, fileName: str) -> None: ...
    def setCurrentFilter(self, filterName: str) -> None: ...
    def setCustomValue(self, key: str, value: typing.Any) -> bool: ...
    def setReadOnly(self, enable: bool) -> None: ...
    def setUsesFilterEngine(self, uses: bool) -> None: ...
    def setupData(self) -> bool: ...
    def unregisterDocumentation(self, namespaceName: str) -> bool: ...
    def usesFilterEngine(self) -> bool: ...


class QHelpFilterData(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: PySide6.QtHelp.QHelpFilterData) -> None: ...

    def __copy__(self) -> typing.Self: ...
    def __eq__(self, other: PySide6.QtHelp.QHelpFilterData) -> bool: ...
    def components(self) -> typing.List[str]: ...
    def setComponents(self, components: typing.Sequence[str]) -> None: ...
    def setVersions(self, versions: typing.Sequence[PySide6.QtCore.QVersionNumber]) -> None: ...
    def swap(self, other: PySide6.QtHelp.QHelpFilterData) -> None: ...
    def versions(self) -> typing.List[PySide6.QtCore.QVersionNumber]: ...


class QHelpFilterEngine(PySide6.QtCore.QObject):

    filterActivated          : typing.ClassVar[Signal] = ... # filterActivated(QString)

    def __init__(self, helpEngine: PySide6.QtHelp.QHelpEngineCore) -> None: ...

    def activeFilter(self) -> str: ...
    def availableComponents(self) -> typing.List[str]: ...
    def availableVersions(self) -> typing.List[PySide6.QtCore.QVersionNumber]: ...
    def filterData(self, filterName: str) -> PySide6.QtHelp.QHelpFilterData: ...
    def filters(self) -> typing.List[str]: ...
    @typing.overload
    def indices(self) -> typing.List[str]: ...
    @typing.overload
    def indices(self, filterName: str) -> typing.List[str]: ...
    def namespaceToComponent(self) -> typing.Dict[str, str]: ...
    def namespaceToVersion(self) -> typing.Dict[str, PySide6.QtCore.QVersionNumber]: ...
    def namespacesForFilter(self, filterName: str) -> typing.List[str]: ...
    def removeFilter(self, filterName: str) -> bool: ...
    def setActiveFilter(self, filterName: str) -> bool: ...
    def setFilterData(self, filterName: str, filterData: PySide6.QtHelp.QHelpFilterData) -> bool: ...


class QHelpFilterSettingsWidget(PySide6.QtWidgets.QWidget):

    def __init__(self, parent: PySide6.QtWidgets.QWidget | None= ...) -> None: ...

    def applySettings(self, filterEngine: PySide6.QtHelp.QHelpFilterEngine) -> bool: ...
    def readSettings(self, filterEngine: PySide6.QtHelp.QHelpFilterEngine) -> None: ...
    def setAvailableComponents(self, components: typing.Sequence[str]) -> None: ...
    def setAvailableVersions(self, versions: typing.Sequence[PySide6.QtCore.QVersionNumber]) -> None: ...


class QHelpGlobal(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, QHelpGlobal: PySide6.QtHelp.QHelpGlobal) -> None: ...

    def __copy__(self) -> typing.Self: ...
    @staticmethod
    def documentTitle(content: str) -> str: ...
    @staticmethod
    def uniquifyConnectionName(name: str, pointer: int) -> str: ...


class QHelpIndexModel(PySide6.QtCore.QStringListModel):

    indexCreated             : typing.ClassVar[Signal] = ... # indexCreated()
    indexCreationStarted     : typing.ClassVar[Signal] = ... # indexCreationStarted()
    def createIndex(self, customFilterName: str) -> None: ...
    def createIndexForCurrentFilter(self) -> None: ...
    def filter(self, filter: str, wildcard: str = ...) -> PySide6.QtCore.QModelIndex: ...
    def helpEngine(self) -> PySide6.QtHelp.QHelpEngineCore: ...
    def isCreatingIndex(self) -> bool: ...


class QHelpIndexWidget(PySide6.QtWidgets.QListView):

    documentActivated        : typing.ClassVar[Signal] = ... # documentActivated(QHelpLink,QString)
    documentsActivated       : typing.ClassVar[Signal] = ... # documentsActivated(QList<QHelpLink>,QString)
    linkActivated            : typing.ClassVar[Signal] = ... # linkActivated(QUrl,QString)
    linksActivated           : typing.ClassVar[Signal] = ... # linksActivated(QMultiMap<QString,QUrl>,QString)
    def activateCurrentItem(self) -> None: ...
    def filterIndices(self, filter: str, wildcard: str = ...) -> None: ...


class QHelpLink(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, QHelpLink: PySide6.QtHelp.QHelpLink) -> None: ...

    def __copy__(self) -> typing.Self: ...


class QHelpSearchEngine(PySide6.QtCore.QObject):

    indexingFinished         : typing.ClassVar[Signal] = ... # indexingFinished()
    indexingStarted          : typing.ClassVar[Signal] = ... # indexingStarted()
    searchingFinished        : typing.ClassVar[Signal] = ... # searchingFinished(int)
    searchingStarted         : typing.ClassVar[Signal] = ... # searchingStarted()

    def __init__(self, helpEngine: PySide6.QtHelp.QHelpEngineCore, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def cancelIndexing(self) -> None: ...
    def cancelSearching(self) -> None: ...
    def hitCount(self) -> int: ...
    def hits(self, start: int, end: int) -> typing.List[typing.Tuple[str, str]]: ...
    def hitsCount(self) -> int: ...
    def query(self) -> typing.List[PySide6.QtHelp.QHelpSearchQuery]: ...
    def queryWidget(self) -> PySide6.QtHelp.QHelpSearchQueryWidget: ...
    def reindexDocumentation(self) -> None: ...
    def resultWidget(self) -> PySide6.QtHelp.QHelpSearchResultWidget: ...
    def scheduleIndexDocumentation(self) -> None: ...
    @typing.overload
    def search(self, searchInput: str) -> None: ...
    @typing.overload
    def search(self, queryList: typing.Sequence[PySide6.QtHelp.QHelpSearchQuery]) -> None: ...
    def searchInput(self) -> str: ...
    def searchResultCount(self) -> int: ...
    def searchResults(self, start: int, end: int) -> typing.List[PySide6.QtHelp.QHelpSearchResult]: ...


class QHelpSearchEngineCore(PySide6.QtCore.QObject):

    indexingFinished         : typing.ClassVar[Signal] = ... # indexingFinished()
    indexingStarted          : typing.ClassVar[Signal] = ... # indexingStarted()
    searchingFinished        : typing.ClassVar[Signal] = ... # searchingFinished()
    searchingStarted         : typing.ClassVar[Signal] = ... # searchingStarted()

    def __init__(self, helpEngine: PySide6.QtHelp.QHelpEngineCore, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def cancelIndexing(self) -> None: ...
    def cancelSearching(self) -> None: ...
    def reindexDocumentation(self) -> None: ...
    def scheduleIndexDocumentation(self) -> None: ...
    def search(self, searchInput: str) -> None: ...
    def searchInput(self) -> str: ...
    def searchResultCount(self) -> int: ...
    def searchResults(self, start: int, end: int) -> typing.List[PySide6.QtHelp.QHelpSearchResult]: ...


class QHelpSearchQuery(Shiboken.Object):

    class FieldName(enum.Enum):

        DEFAULT                   = ...  # 0x0
        FUZZY                     = ...  # 0x1
        WITHOUT                   = ...  # 0x2
        PHRASE                    = ...  # 0x3
        ALL                       = ...  # 0x4
        ATLEAST                   = ...  # 0x5


    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, field: PySide6.QtHelp.QHelpSearchQuery.FieldName, wordList_: typing.Sequence[str]) -> None: ...
    @typing.overload
    def __init__(self, QHelpSearchQuery: PySide6.QtHelp.QHelpSearchQuery) -> None: ...

    def __copy__(self) -> typing.Self: ...


class QHelpSearchQueryWidget(PySide6.QtWidgets.QWidget):

    search                   : typing.ClassVar[Signal] = ... # search()

    def __init__(self, parent: PySide6.QtWidgets.QWidget | None= ...) -> None: ...

    def changeEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def collapseExtendedSearch(self) -> None: ...
    def expandExtendedSearch(self) -> None: ...
    def focusInEvent(self, focusEvent: PySide6.QtGui.QFocusEvent) -> None: ...
    def isCompactMode(self) -> bool: ...
    def query(self) -> typing.List[PySide6.QtHelp.QHelpSearchQuery]: ...
    def searchInput(self) -> str: ...
    def setCompactMode(self, on: bool) -> None: ...
    def setQuery(self, queryList: typing.Sequence[PySide6.QtHelp.QHelpSearchQuery]) -> None: ...
    def setSearchInput(self, searchInput: str) -> None: ...


class QHelpSearchResult(Shiboken.Object):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: PySide6.QtHelp.QHelpSearchResult) -> None: ...
    @typing.overload
    def __init__(self, url: PySide6.QtCore.QUrl | str, title: str, snippet: str) -> None: ...

    def snippet(self) -> str: ...
    def title(self) -> str: ...
    def url(self) -> PySide6.QtCore.QUrl: ...


class QHelpSearchResultWidget(PySide6.QtWidgets.QWidget):

    requestShowLink          : typing.ClassVar[Signal] = ... # requestShowLink(QUrl)
    def changeEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def linkAt(self, point: PySide6.QtCore.QPoint) -> PySide6.QtCore.QUrl: ...


class QIntList(object): ...


# eof