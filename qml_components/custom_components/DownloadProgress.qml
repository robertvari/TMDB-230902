import QtQuick

Item{
    id: root
    implicitHeight: 10
    visible: true

    property int max_value: 20
    property int current_value: 10

    Rectangle{
        height: root.height
        width: (root.width / root.max_value) * root.current_value
        color: "#05B4E3"
        radius: root.height / 2
    }
}