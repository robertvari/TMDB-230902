import QtQuick
import Qt5Compat.GraphicalEffects

Item{

    Rectangle{
        id: source_rect
        anchors.fill: parent
        border.color: "#e3e3e3"
        radius: 10

        Text{
            text: "Movie card..."
        }

        visible: false
    }

    DropShadow {
        anchors.fill: parent
        horizontalOffset: 3
        verticalOffset: 3
        radius: 8.0
        color: "#e3e3e3"
        source: source_rect
    }
}

