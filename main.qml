import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material
import "qml_components"
import "qml_components/custom_components"

ApplicationWindow{
    visible: true
    width: 1280
    height: 720
    title: "The Movie Database"
    //visibility: "Maximized"

    Material.accent: Material.LightBlue

    ColumnLayout{
        id: main_layout
        anchors.fill: parent
        spacing: 10

        state: "movie-list"
        states: [
            State{
                name: "movie-details"
                PropertyChanges{
                    target: movie_details_view
                    visible: true
                }
                PropertyChanges{
                    target: movie_list_view
                    visible: false
                }
            }
        ]

        Navbar{Layout.fillWidth: true}

        // Progressbar
        DownloadProgress{Layout.fillWidth: true}
        
        Item{ // Movie List view
            id: movie_list_view
            Layout.fillHeight: true
            Layout.fillWidth: true
            visible: true

            RowLayout{
                anchors.fill: parent
                anchors.leftMargin: 200
                anchors.rightMargin: 200

                Sidebar{Layout.fillHeight: true}
                MovieListView{Layout.fillWidth: true; Layout.fillHeight: true}
            }
        }

        MovieDetailsView{
            id: movie_details_view
            Layout.fillWidth: true
            Layout.fillHeight: true
            visible: false
        }
    }
}