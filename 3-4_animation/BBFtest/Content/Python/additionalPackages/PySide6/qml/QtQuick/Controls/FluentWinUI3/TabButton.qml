// Copyright (C) 2024 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only

import QtQuick
import QtQuick.Controls.impl
import QtQuick.Templates as T

T.TabButton {
    id: control

    implicitWidth: Math.max(implicitBackgroundWidth + leftInset + rightInset,
                            implicitContentWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(implicitBackgroundHeight + topInset + bottomInset,
                             implicitContentHeight + topPadding + bottomPadding)

    spacing: config.spacing || 0

    topPadding: config.topPadding || 0
    bottomPadding: config.bottomPadding || 0
    leftPadding: config.leftPadding || 0
    rightPadding: config.rightPadding || 0

    topInset: -config.topInset || 0
    bottomInset: -config.bottomInset || 0
    leftInset: -config.leftInset || 0
    rightInset: -config.rightInset || 0

    icon.width: 16
    icon.height: 16
    icon.color: control.down ? __pressedText : control.hovered ? __hoveredText : control.palette.buttonText

    readonly property string __currentState: [
        checked && "checked",
        !enabled && "disabled",
        enabled && !down && hovered && "hovered",
        down && "pressed"
    ].filter(Boolean).join("_") || "normal"
    readonly property var config: Config.controls.tabbutton[__currentState] || {}

    readonly property color __pressedText: Application.styleHints.colorScheme == Qt.Light
                                            ? Qt.rgba(control.palette.buttonText.r, control.palette.buttonText.g, control.palette.buttonText.b, 0.447)
                                            : Qt.rgba(control.palette.buttonText.r, control.palette.buttonText.g, control.palette.buttonText.b, 0.529)
    readonly property color __hoveredText: Application.styleHints.colorScheme == Qt.Light
                                            ? Qt.rgba(control.palette.buttonText.r, control.palette.buttonText.g, control.palette.buttonText.b, 0.62)
                                            : Qt.rgba(control.palette.buttonText.r, control.palette.buttonText.g, control.palette.buttonText.b, 0.7725)

    readonly property Item __focusFrameTarget: control

    contentItem: IconLabel {
        spacing: control.spacing
        mirrored: control.mirrored
        display: control.display
        alignment: control.config.label.textVAlignment | control.config.label.textHAlignment
        text: control.text
        font: control.font
        icon: control.icon
        color: control.icon.color
    }

    background: StyleImage {
        imageConfig: control.config.background
        property Rectangle selector: Rectangle {
            parent: control.background
            x: (parent.width - implicitWidth) / 2
            y: parent.height - height
            height: 3
            implicitWidth: 16
            radius: height * 0.5
            color: control.palette.accent
            visible: control.checked

            states: State {
                name: "checked"
                when: control.checked
                PropertyChanges {
                    target: control.background.selector
                    width: 16
                }
            }

            transitions: Transition {
                to: "checked"
                ParallelAnimation {
                    NumberAnimation { target: control.background.selector; property: "opacity"; from: 0; to: 1; easing.type: Easing.Linear; duration: 83}
                    NumberAnimation { target: control.background.selector; property: "scale"; from: 0.33; to: 1; easing.type: Easing.InOutCubic; duration: 167}
                }
            }
        }
    }
}