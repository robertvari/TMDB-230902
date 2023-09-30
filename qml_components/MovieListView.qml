import QtQuick
import QtQuick.Layouts
import "custom_components"

Item{
    GridView{
        id: grid_view
        anchors.fill: parent
        cellWidth: 184
        cellHeight: 386
        model: MovieList
        clip: true

        delegate: MovieCard{
            width: grid_view.cellWidth - 10
            height: grid_view.cellHeight - 10
            
            title: movie_data.title
            release_date: movie_data.display_date
            popularity: movie_data.vote_average
            poster: movie_data.poster_path
        }
    }
}