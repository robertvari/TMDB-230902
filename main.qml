import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material
import "qml_components"

ApplicationWindow{
    visible: true
    width: 1280
    height: 720
    title: "The Movie Database"
    //visibility: "Maximized"

    Material.accent: Material.LightBlue

    ColumnLayout{
        anchors.fill: parent
        spacing: 0

        Navbar{Layout.fillWidth: true}

        Item{
            Layout.fillHeight: true
            Layout.fillWidth: true

            RowLayout{
                anchors.fill: parent
                anchors.leftMargin: 200
                anchors.rightMargin: 200

                Sidebar{Layout.fillHeight: true}
                MovieListView{Layout.fillWidth: true; Layout.fillHeight: true}
            }
        }
    }
}