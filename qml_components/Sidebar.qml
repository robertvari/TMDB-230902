import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "custom_components"

Item{
    width: 258

    RoundedBox{
        width: parent.width
        height: childrenRect.height + 20

        ColumnLayout{
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.margins: 10

            TitleText{text: "Search & Filter"}

            // Input field for search.
            IconTextField{
                placeholderText: "Search..."
                icon: "../../resources/search_icon.svg"
                Layout.fillWidth: true
            }
            // ComboBox for sorting
            // Genre filters
        }
    }

}