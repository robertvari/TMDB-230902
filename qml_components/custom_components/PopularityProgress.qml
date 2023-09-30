import QtQuick

Rectangle{
    id: root
    width: 50
    height: 50
    radius: width
    color: "black"
    anchors.bottom: parent.bottom
    anchors.bottomMargin: -25
    x: 10

    property int popularity
    onPopularityChanged: draw_canvas.requestPaint()

    Canvas{
        id: draw_canvas
        width: parent.width
        height: parent.height

        onPaint: {
            var ctx = getContext("2d")

            var radiant = root.popularity * 0.062831853071796
        }
    }

    Text{
        anchors.centerIn: parent
        text: root.popularity
        font.bold: true
        font.pixelSize: 24
        color: "white"
    }
}