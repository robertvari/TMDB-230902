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
        spacing: 0

        Rectangle{
            color: "#032541"
            Layout.fillWidth: true
            height: 64

            Label{
                text: "Navbar..."
                color: "white"
            }
        }

        Rectangle{
            color: "lightGreen"
            Layout.fillHeight: true
            Layout.fillWidth: true

            Label{
                text: "Content..."
            }
        }
    }
}