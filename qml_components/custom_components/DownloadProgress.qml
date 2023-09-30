import QtQuick

Item{
    id: root
    implicitHeight: 10
    visible: MovieList.is_downloading

    property int max_value: MovieList.download_max_count
    property int current_value: MovieList.download_current_value

    Rectangle{
        height: root.height
        width: (root.width / root.max_value) * root.current_value
        color: "#05B4E3"
        radius: root.height / 2
    }
}