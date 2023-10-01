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
                    icon: "search_icon.svg"
                    Layout.fillWidth: true
                    onTextEdited: MovieListProxy.set_search(text)
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
                    model: MovieListProxy.sorting_options
                    Layout.fillWidth: true

                    onActivated: MovieListProxy.current_sorting = currentText
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
                    model: MovieList.genres

                    TextButton{
                        text: modelData
                        color: "black"
                        font.bold: MovieListProxy.current_genre == text? true : false
                        font.pixelSize: 16

                        onClicked: MovieListProxy.current_genre = text
                    }
                }
            }
        }

        Item{
            Layout.fillHeight: true
        }
    }
}