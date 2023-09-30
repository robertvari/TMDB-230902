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
            var centerX = width / 2
            var centerY = height / 2
            var radius = width / 2

            ctx.reset()
            ctx.beginPath()
            ctx.fillStyle = root.popularity > 70 ? "lightgreen" : "yellow"

            ctx.arc(centerX, centerY, radius, 0, radiant, false)
            ctx.lineTo(centerX, centerY)
            ctx.fill()
        }

        rotation: -90
    }

    Rectangle{
        color: root.color
        width: root.width -10
        height: width
        radius: width
        anchors.centerIn: parent
    }

    Text{
        anchors.centerIn: parent
        text: root.popularity
        font.bold: true
        font.pixelSize: 24
        color: "white"
    }
}