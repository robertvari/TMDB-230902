import QtQuick

Text{
    text: "Text Button"
    font.bold: true
    font.pixelSize: 20
    color: "white"

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor

        onClicked: print(parent.text)
    }
}