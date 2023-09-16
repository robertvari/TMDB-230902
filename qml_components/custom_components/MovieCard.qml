import QtQuick
import Qt5Compat.GraphicalEffects
import QtQuick.Layouts

Item{
    Rectangle{
        id: source_rect
        anchors.fill: parent
        border.color: "#e3e3e3"
        radius: 10
        visible: false

        Image{
            id: poster
            source: "../../resources/poster.jpg"
            sourceSize: Qt.size(source_rect.width, source_rect.height)

            Rectangle{
                id: popularity_progress
                width: 50
                height: 50
                radius: width
                color: "lightBlue"
                anchors.bottom: parent.bottom
                anchors.bottomMargin: -25
                x: 10
            }
        }

        Item{
            id: movie_details_container
            width: parent.width
            anchors.top: poster.bottom
            anchors.topMargin: 25
            anchors.bottom: source_rect.bottom

            ColumnLayout{
                anchors.fill: parent
                anchors.margins: 10

                SubtitleText{
                    text: "Indiana Jones and the Dial of Destiny"
                    wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                    Layout.fillWidth: movie_details_container.width
                }

                Text{
                    text: "28 Jun 2023"
                    opacity: 0.5
                }
            }
        }
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

