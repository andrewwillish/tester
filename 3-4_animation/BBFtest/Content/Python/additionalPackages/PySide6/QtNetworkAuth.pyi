# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations
"""
This file contains the exact signatures for all functions in module
PySide6.QtNetworkAuth, except for defaults which are replaced by "...".

# mypy: disable-error-code="override, overload-overlap"
"""

# Module `PySide6.QtNetworkAuth`

import PySide6.QtNetworkAuth
import PySide6.QtCore
import PySide6.QtNetwork

import enum
import typing
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


class QAbstractOAuth(PySide6.QtCore.QObject):

    authorizationUrlChanged  : typing.ClassVar[Signal] = ... # authorizationUrlChanged(QUrl)
    authorizeWithBrowser     : typing.ClassVar[Signal] = ... # authorizeWithBrowser(QUrl)
    clientIdentifierChanged  : typing.ClassVar[Signal] = ... # clientIdentifierChanged(QString)
    contentTypeChanged       : typing.ClassVar[Signal] = ... # contentTypeChanged(ContentType)
    extraTokensChanged       : typing.ClassVar[Signal] = ... # extraTokensChanged(QVariantMap)
    finished                 : typing.ClassVar[Signal] = ... # finished(QNetworkReply*)
    granted                  : typing.ClassVar[Signal] = ... # granted()
    replyDataReceived        : typing.ClassVar[Signal] = ... # replyDataReceived(QByteArray)
    requestFailed            : typing.ClassVar[Signal] = ... # requestFailed(Error)
    statusChanged            : typing.ClassVar[Signal] = ... # statusChanged(Status)
    tokenChanged             : typing.ClassVar[Signal] = ... # tokenChanged(QString)

    class ContentType(enum.Enum):

        WwwFormUrlEncoded         = ...  # 0x0
        Json                      = ...  # 0x1

    class Error(enum.Enum):

        NoError                   = ...  # 0x0
        NetworkError              = ...  # 0x1
        ServerError               = ...  # 0x2
        OAuthTokenNotFoundError   = ...  # 0x3
        OAuthTokenSecretNotFoundError = ...  # 0x4
        OAuthCallbackNotVerified  = ...  # 0x5

    class Stage(enum.Enum):

        RequestingTemporaryCredentials = ...  # 0x0
        RequestingAuthorization   = ...  # 0x1
        RequestingAccessToken     = ...  # 0x2
        RefreshingAccessToken     = ...  # 0x3

    class Status(enum.Enum):

        NotAuthenticated          = ...  # 0x0
        TemporaryCredentialsReceived = ...  # 0x1
        Granted                   = ...  # 0x2
        RefreshingToken           = ...  # 0x3


    def authorizationUrl(self) -> PySide6.QtCore.QUrl: ...
    def callback(self) -> str: ...
    def clientIdentifier(self) -> str: ...
    def contentType(self) -> PySide6.QtNetworkAuth.QAbstractOAuth.ContentType: ...
    def deleteResource(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def extraTokens(self) -> typing.Dict[str, typing.Any]: ...
    @staticmethod
    def generateRandomString(length: int) -> PySide6.QtCore.QByteArray: ...
    def get(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def grant(self) -> None: ...
    def head(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def networkAccessManager(self) -> PySide6.QtNetwork.QNetworkAccessManager: ...
    def post(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def prepareRequest(self, request: PySide6.QtNetwork.QNetworkRequest, verb: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview, body: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview= ...) -> None: ...
    def put(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def replyHandler(self) -> PySide6.QtNetworkAuth.QAbstractOAuthReplyHandler: ...
    def resourceOwnerAuthorization(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any]) -> None: ...
    def setAuthorizationUrl(self, url: PySide6.QtCore.QUrl | str) -> None: ...
    def setClientIdentifier(self, clientIdentifier: str) -> None: ...
    def setContentType(self, contentType: PySide6.QtNetworkAuth.QAbstractOAuth.ContentType) -> None: ...
    def setModifyParametersFunction(self, modifyParametersFunction: object) -> None: ...
    def setNetworkAccessManager(self, networkAccessManager: PySide6.QtNetwork.QNetworkAccessManager) -> None: ...
    def setReplyHandler(self, handler: PySide6.QtNetworkAuth.QAbstractOAuthReplyHandler) -> None: ...
    def setStatus(self, status: PySide6.QtNetworkAuth.QAbstractOAuth.Status) -> None: ...
    def setToken(self, token: str) -> None: ...
    def status(self) -> PySide6.QtNetworkAuth.QAbstractOAuth.Status: ...
    def token(self) -> str: ...


class QAbstractOAuth2(PySide6.QtNetworkAuth.QAbstractOAuth):

    authorizationCallbackReceived: typing.ClassVar[Signal] = ... # authorizationCallbackReceived(QVariantMap)
    clientIdentifierSharedKeyChanged: typing.ClassVar[Signal] = ... # clientIdentifierSharedKeyChanged(QString)
    error                    : typing.ClassVar[Signal] = ... # error(QString,QString,QUrl)
    expirationAtChanged      : typing.ClassVar[Signal] = ... # expirationAtChanged(QDateTime)
    refreshTokenChanged      : typing.ClassVar[Signal] = ... # refreshTokenChanged(QString)
    responseTypeChanged      : typing.ClassVar[Signal] = ... # responseTypeChanged(QString)
    scopeChanged             : typing.ClassVar[Signal] = ... # scopeChanged(QString)
    sslConfigurationChanged  : typing.ClassVar[Signal] = ... # sslConfigurationChanged(QSslConfiguration)
    stateChanged             : typing.ClassVar[Signal] = ... # stateChanged(QString)
    userAgentChanged         : typing.ClassVar[Signal] = ... # userAgentChanged(QString)

    @typing.overload
    def __init__(self, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def clientIdentifierSharedKey(self) -> str: ...
    def createAuthenticatedUrl(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtCore.QUrl: ...
    def deleteResource(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def expirationAt(self) -> PySide6.QtCore.QDateTime: ...
    def get(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def head(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @typing.overload
    def post(self, url: PySide6.QtCore.QUrl | str, multiPart: PySide6.QtNetwork.QHttpMultiPart) -> PySide6.QtNetwork.QNetworkReply: ...
    @typing.overload
    def post(self, url: PySide6.QtCore.QUrl | str, data: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview) -> PySide6.QtNetwork.QNetworkReply: ...
    @typing.overload
    def post(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def prepareRequest(self, request: PySide6.QtNetwork.QNetworkRequest, verb: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview, body: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview= ...) -> None: ...
    @typing.overload
    def put(self, url: PySide6.QtCore.QUrl | str, multiPart: PySide6.QtNetwork.QHttpMultiPart) -> PySide6.QtNetwork.QNetworkReply: ...
    @typing.overload
    def put(self, url: PySide6.QtCore.QUrl | str, data: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview) -> PySide6.QtNetwork.QNetworkReply: ...
    @typing.overload
    def put(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def refreshToken(self) -> str: ...
    def responseType(self) -> str: ...
    def scope(self) -> str: ...
    def setClientIdentifierSharedKey(self, clientIdentifierSharedKey: str) -> None: ...
    def setRefreshToken(self, refreshToken: str) -> None: ...
    def setResponseType(self, responseType: str) -> None: ...
    def setScope(self, scope: str) -> None: ...
    def setSslConfiguration(self, configuration: PySide6.QtNetwork.QSslConfiguration) -> None: ...
    def setState(self, state: str) -> None: ...
    def setUserAgent(self, userAgent: str) -> None: ...
    def sslConfiguration(self) -> PySide6.QtNetwork.QSslConfiguration: ...
    def state(self) -> str: ...
    def userAgent(self) -> str: ...


class QAbstractOAuthReplyHandler(PySide6.QtCore.QObject):

    callbackDataReceived     : typing.ClassVar[Signal] = ... # callbackDataReceived(QByteArray)
    callbackReceived         : typing.ClassVar[Signal] = ... # callbackReceived(QVariantMap)
    replyDataReceived        : typing.ClassVar[Signal] = ... # replyDataReceived(QByteArray)
    tokenRequestErrorOccurred: typing.ClassVar[Signal] = ... # tokenRequestErrorOccurred(QAbstractOAuth::Error,QString)
    tokensReceived           : typing.ClassVar[Signal] = ... # tokensReceived(QVariantMap)

    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def callback(self) -> str: ...
    def networkReplyFinished(self, reply: PySide6.QtNetwork.QNetworkReply) -> None: ...


class QIntList(object): ...


class QOAuth1(PySide6.QtNetworkAuth.QAbstractOAuth):

    clientSharedSecretChanged: typing.ClassVar[Signal] = ... # clientSharedSecretChanged(QString)
    signatureMethodChanged   : typing.ClassVar[Signal] = ... # signatureMethodChanged(QOAuth1::SignatureMethod)
    temporaryCredentialsUrlChanged: typing.ClassVar[Signal] = ... # temporaryCredentialsUrlChanged(QUrl)
    tokenCredentialsUrlChanged: typing.ClassVar[Signal] = ... # tokenCredentialsUrlChanged(QUrl)
    tokenSecretChanged       : typing.ClassVar[Signal] = ... # tokenSecretChanged(QString)

    class SignatureMethod(enum.Enum):

        Hmac_Sha1                 = ...  # 0x0
        Rsa_Sha1                  = ...  # 0x1
        PlainText                 = ...  # 0x2


    @typing.overload
    def __init__(self, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, clientIdentifier: str, clientSharedSecret: str, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def clientCredentials(self) -> typing.Tuple[str, str]: ...
    def clientSharedSecret(self) -> str: ...
    def continueGrantWithVerifier(self, verifier: str) -> None: ...
    def deleteResource(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @staticmethod
    def generateAuthorizationHeader(oauthParams: typing.Dict[str, typing.Any]) -> PySide6.QtCore.QByteArray: ...
    def get(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def grant(self) -> None: ...
    def head(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @staticmethod
    def nonce() -> PySide6.QtCore.QByteArray: ...
    def post(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def prepareRequest(self, request: PySide6.QtNetwork.QNetworkRequest, verb: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview, body: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview= ...) -> None: ...
    def put(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def requestTemporaryCredentials(self, operation: PySide6.QtNetwork.QNetworkAccessManager.Operation, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    def requestTokenCredentials(self, operation: PySide6.QtNetwork.QNetworkAccessManager.Operation, url: PySide6.QtCore.QUrl | str, temporaryToken: typing.Tuple[str, str], parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtNetwork.QNetworkReply: ...
    @typing.overload
    def setClientCredentials(self, clientIdentifier: str, clientSharedSecret: str) -> None: ...
    @typing.overload
    def setClientCredentials(self, clientCredentials: typing.Tuple[str, str]) -> None: ...
    def setClientSharedSecret(self, clientSharedSecret: str) -> None: ...
    def setSignatureMethod(self, value: PySide6.QtNetworkAuth.QOAuth1.SignatureMethod) -> None: ...
    def setTemporaryCredentialsUrl(self, url: PySide6.QtCore.QUrl | str) -> None: ...
    @typing.overload
    def setTokenCredentials(self, token: str, tokenSecret: str) -> None: ...
    @typing.overload
    def setTokenCredentials(self, tokenCredentials: typing.Tuple[str, str]) -> None: ...
    def setTokenCredentialsUrl(self, url: PySide6.QtCore.QUrl | str) -> None: ...
    def setTokenSecret(self, tokenSecret: str) -> None: ...
    @typing.overload
    def setup(self, request: PySide6.QtNetwork.QNetworkRequest, signingParameters: typing.Dict[str, typing.Any], operation: PySide6.QtNetwork.QNetworkAccessManager.Operation) -> None: ...
    @typing.overload
    def setup(self, request: PySide6.QtNetwork.QNetworkRequest, signingParameters: typing.Dict[str, typing.Any], operationVerb: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview) -> None: ...
    def signatureMethod(self) -> PySide6.QtNetworkAuth.QOAuth1.SignatureMethod: ...
    def temporaryCredentialsUrl(self) -> PySide6.QtCore.QUrl: ...
    def tokenCredentials(self) -> typing.Tuple[str, str]: ...
    def tokenCredentialsUrl(self) -> PySide6.QtCore.QUrl: ...
    def tokenSecret(self) -> str: ...


class QOAuth1Signature(Shiboken.Object):

    class HttpRequestMethod(enum.Enum):

        Unknown                   = ...  # 0x0
        Head                      = ...  # 0x1
        Get                       = ...  # 0x2
        Put                       = ...  # 0x3
        Post                      = ...  # 0x4
        Delete                    = ...  # 0x5
        Custom                    = ...  # 0x6


    @typing.overload
    def __init__(self, other: PySide6.QtNetworkAuth.QOAuth1Signature) -> None: ...
    @typing.overload
    def __init__(self, url: PySide6.QtCore.QUrl | str= ..., method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod = ..., parameters: typing.Dict[str, typing.Any] = ...) -> None: ...
    @typing.overload
    def __init__(self, url: PySide6.QtCore.QUrl | str, clientSharedKey: str, tokenSecret: str, method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod = ..., parameters: typing.Dict[str, typing.Any] = ...) -> None: ...

    def __copy__(self) -> typing.Self: ...
    def addRequestBody(self, body: PySide6.QtCore.QUrlQuery) -> None: ...
    def clientSharedKey(self) -> str: ...
    def customMethodString(self) -> PySide6.QtCore.QByteArray: ...
    def hmacSha1(self) -> PySide6.QtCore.QByteArray: ...
    def httpRequestMethod(self) -> PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod: ...
    def insert(self, key: str, value: typing.Any) -> None: ...
    def keys(self) -> typing.List[str]: ...
    def parameters(self) -> typing.Dict[str, typing.Any]: ...
    @typing.overload  # type: ignore[misc]
    def plainText(self) -> PySide6.QtCore.QByteArray: ...
    @typing.overload
    @staticmethod
    def plainText(clientSharedSecret: str, tokenSecret: str) -> PySide6.QtCore.QByteArray: ...
    def rsaSha1(self) -> PySide6.QtCore.QByteArray: ...
    def setClientSharedKey(self, secret: str) -> None: ...
    def setCustomMethodString(self, verb: PySide6.QtCore.QByteArray | bytes | bytearray | memoryview) -> None: ...
    def setHttpRequestMethod(self, method: PySide6.QtNetworkAuth.QOAuth1Signature.HttpRequestMethod) -> None: ...
    def setParameters(self, parameters: typing.Dict[str, typing.Any]) -> None: ...
    def setTokenSecret(self, secret: str) -> None: ...
    def setUrl(self, url: PySide6.QtCore.QUrl | str) -> None: ...
    def swap(self, other: PySide6.QtNetworkAuth.QOAuth1Signature) -> None: ...
    def take(self, key: str) -> typing.Any: ...
    def tokenSecret(self) -> str: ...
    def url(self) -> PySide6.QtCore.QUrl: ...
    def value(self, key: str, defaultValue: typing.Any = ...) -> typing.Any: ...


class QOAuth2AuthorizationCodeFlow(PySide6.QtNetworkAuth.QAbstractOAuth2):

    accessTokenUrlChanged    : typing.ClassVar[Signal] = ... # accessTokenUrlChanged(QUrl)

    class PkceMethod(enum.Enum):

        S256                      = ...  # 0x0
        Plain                     = ...  # 0x1
        None_                     = ...  # 0xff


    @typing.overload
    def __init__(self, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, clientIdentifier: str, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, clientIdentifier: str, authorizationUrl: PySide6.QtCore.QUrl | str, accessTokenUrl: PySide6.QtCore.QUrl | str, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, authorizationUrl: PySide6.QtCore.QUrl | str, accessTokenUrl: PySide6.QtCore.QUrl | str, manager: PySide6.QtNetwork.QNetworkAccessManager, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def accessTokenUrl(self) -> PySide6.QtCore.QUrl: ...
    def buildAuthenticateUrl(self, parameters: typing.Dict[str, typing.Any] = ...) -> PySide6.QtCore.QUrl: ...
    def grant(self) -> None: ...
    def pkceMethod(self) -> PySide6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod: ...
    def refreshAccessToken(self) -> None: ...
    def requestAccessToken(self, code: str) -> None: ...
    def resourceOwnerAuthorization(self, url: PySide6.QtCore.QUrl | str, parameters: typing.Dict[str, typing.Any] = ...) -> None: ...
    def setAccessTokenUrl(self, accessTokenUrl: PySide6.QtCore.QUrl | str) -> None: ...
    def setPkceMethod(self, method: PySide6.QtNetworkAuth.QOAuth2AuthorizationCodeFlow.PkceMethod, length: int = ...) -> None: ...


class QOAuthHttpServerReplyHandler(PySide6.QtNetworkAuth.QOAuthOobReplyHandler):

    @typing.overload
    def __init__(self, address: PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress, port: int, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...
    @typing.overload
    def __init__(self, port: int, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def callback(self) -> str: ...
    def callbackPath(self) -> str: ...
    def callbackText(self) -> str: ...
    def close(self) -> None: ...
    def isListening(self) -> bool: ...
    def listen(self, address: PySide6.QtNetwork.QHostAddress | PySide6.QtNetwork.QHostAddress.SpecialAddress= ..., port: int = ...) -> bool: ...
    def port(self) -> int: ...
    def setCallbackPath(self, path: str) -> None: ...
    def setCallbackText(self, text: str) -> None: ...


class QOAuthOobReplyHandler(PySide6.QtNetworkAuth.QAbstractOAuthReplyHandler):

    def __init__(self, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def callback(self) -> str: ...
    def networkReplyFinished(self, reply: PySide6.QtNetwork.QNetworkReply) -> None: ...


class QOAuthUriSchemeReplyHandler(PySide6.QtNetworkAuth.QOAuthOobReplyHandler):

    redirectUrlChanged       : typing.ClassVar[Signal] = ... # redirectUrlChanged()

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject) -> None: ...
    @typing.overload
    def __init__(self, redirectUrl: PySide6.QtCore.QUrl | str, parent: PySide6.QtCore.QObject | None= ...) -> None: ...

    def callback(self) -> str: ...
    def close(self) -> None: ...
    def isListening(self) -> bool: ...
    def listen(self) -> bool: ...
    def redirectUrl(self) -> PySide6.QtCore.QUrl: ...
    def setRedirectUrl(self, url: PySide6.QtCore.QUrl | str) -> None: ...


# eof