import QtQuick

Text{
    id: root
    text: "Text Button"
    font.bold: true
    font.pixelSize: 20
    color: "white"

    signal clicked

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor

        onClicked: root.clicked()
    }
}