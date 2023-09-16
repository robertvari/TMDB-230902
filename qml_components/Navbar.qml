import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "custom_components"


Rectangle{
    color: "#032541"
    height: 64

    RowLayout{
        spacing: 30
        anchors.fill: parent
        anchors.leftMargin: 30

        Image{
            source: "../resources/logo.svg"
            
            MouseArea{
                anchors.fill: parent
                cursorShape: Qt.PointingHandCursor

                onClicked: print("Home")
            }
        }

        TextButton{text: "Movies"}
        TextButton{text: "TV Shows"}
        TextButton{text: "People"}
        TextButton{text: "More"}
        
        // Spacer
        Item{Layout.fillWidth: true}
    }
}