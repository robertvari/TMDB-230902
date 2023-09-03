import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "custom_components"


Rectangle{
    color: "#032541"
    height: 64

    RowLayout{
        TextButton{text: "Movies"}
        TextButton{text: "TV Shows"}
        TextButton{text: "People"}
        TextButton{text: "More"}
    }
}