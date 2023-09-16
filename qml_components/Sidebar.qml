import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material
import "custom_components"

Item{
    width: 258

    ColumnLayout{ 
        anchors.fill: parent  

        RoundedBox{
            width: parent.width
            height: childrenRect.height + 20

            ColumnLayout{
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.margins: 10

                TitleText{text: "Search"}

                // Input field for search.
                IconTextField{
                    placeholderText: "Search..."
                    icon: "../../resources/search_icon.svg"
                    Layout.fillWidth: true
                }
            }
        }

        RoundedBox{
            width: parent.width
            height: childrenRect.height + 20

            ColumnLayout{
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.margins: 10

                TitleText{text: "Sort"}
                
                // ComboBox for sorting
                ComboBox{
                    model: ["Popularity Descending", "Popularity Ascending", "Rating Descending", "Rating Ascending", "Release Date Descending", "Release Date Ascending", "Title (A-Z)", "Title (Z-A)"]
                    Layout.fillWidth: true
                }
            }
        }

        RoundedBox{
            width: parent.width
            height: childrenRect.height + 20

            ColumnLayout{
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.margins: 10

                TitleText{text: "Genres"}
                // Genre filters

                Repeater{
                    model: ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy"]

                    TextButton{
                        text: modelData
                        color: "black"
                        font.bold: false
                        font.pixelSize: 16
                    }
                }
            }
        }

        Item{
            Layout.fillHeight: true
        }
    }
}