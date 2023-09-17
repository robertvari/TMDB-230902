import QtQuick
import QtQuick.Controls
// import QtQuick.Controls.Material

TextField{
    placeholderText: "Placeholder text"
    font.pixelSize: 16
    leftPadding: 30

    // custom props
    property string icon

    background: Rectangle{
        radius: 10
        border.color: "#e3e3e3"
    }

    Image{
        source: Resources.get(icon)
        sourceSize: Qt.size(20, 20)
        opacity: 0.3
        y: 2
        x: 3
    }
}