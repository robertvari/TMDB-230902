import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material


ApplicationWindow{
    visible: true
    width: 1280
    height: 720
    title: "The Movie Database"
    //visibility: "Maximized"

    Material.accent: Material.LightBlue

    ColumnLayout{
        anchors.fill: parent
        anchors.margins: 20
    }
}