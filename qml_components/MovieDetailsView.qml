import QtQuick
import QtQuick.Layouts
import "custom_components"

Rectangle{
    id: root
    color: "black"

    Image{
        source: MovieDetails.backdrop
        width: parent.width
        height: parent.height
        fillMode: Image.PreserveAspectCrop
        opacity: 0.3
    }

    RowLayout{
        id: main_layout
        width: root.width

        Image{
            source: MovieDetails.poster
        }

        ColumnLayout{
            Text{
                text: MovieDetails.title
                font.pixelSize: 60
                color: "white"
            }

            RowLayout{
                SubtitleText{
                    text: MovieDetails.release_date
                    color: "white"
                }

                SubtitleText{text: " - "; color: "white"}

                SubtitleText{
                    text: MovieDetails.genres
                    color: "white"
                }

                SubtitleText{text: " - "; color: "white"}

                SubtitleText{
                    text: MovieDetails.runtime
                    color: "white"
                }
            }

            SubtitleText{
                text: MovieDetails.tagline
                color: "white"
            }

            SubtitleText{
                text: "Overview"
                color: "white"
            }

            Text{
                text: MovieDetails.overview
                Layout.fillWidth: true
                wrapMode: Text.WrapAtWordBoundaryOrAnywhere
                color: "white"
                font.pixelSize: 18
            }

            Item{
                Layout.fillHeight: true
            }
        }
    }
}