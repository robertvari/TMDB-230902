import QtQuick
import QtQuick.Layouts
import "custom_components"

Rectangle{
    id: root
    color: "lightGreen"

    ColumnLayout{
        width: parent.width

        Text{
            text: MovieDetails.title
            font.pixelSize: 60
        }

        SubtitleText{
            text: MovieDetails.tagline
        }

        Text{
            text: MovieDetails.overview
            Layout.fillWidth: true
            wrapMode: Text.WrapAtWordBoundaryOrAnywhere
        }

        Text{
            text: MovieDetails.genres
        }

        Text{
            text: MovieDetails.release_date
        }

        Text{
            text: MovieDetails.runtime
        }

        Item{
            implicitWidth: 50
            implicitHeight: 50

            PopularityProgress{
                popularity: MovieDetails.vote_average
            }
        }


        Image{
            source: MovieDetails.poster
        }

        Image{
            source: MovieDetails.backdrop
        }
    }

}