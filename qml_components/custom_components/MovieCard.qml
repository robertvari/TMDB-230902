import QtQuick
import Qt5Compat.GraphicalEffects
import QtQuick.Layouts

Item{
    id: root

    property string title: "Movie Title"
    property string release_date: "Date"
    property int popularity: 100
    property var poster


    Rectangle{
        id: source_rect
        anchors.fill: parent
        border.color: "#e3e3e3"
        radius: 10
        visible: false

        Image{
            id: poster
            source: poster
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

                Text{
                    text: root.popularity
                }
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
                    text: root.title
                    wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                    Layout.fillWidth: movie_details_container.width
                }

                Text{
                    text: root.release_date
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

    MouseArea{
        anchors.fill: parent
        cursorShape: Qt.PointingHandCursor

        onClicked: main_layout.state = "movie-details"
    }
}

