from PySide6.QtCore import QObject, Slot, QUrl
import os, requests
from os.path import expanduser


RESOURCES_PATH = os.path.dirname(__file__).replace("py_components", "resources")
CACHE_FOLDER = os.path.join(expanduser("~"), "TMDB_CACHE")

class Resources(QObject):
    @Slot(str, result=QUrl)
    def get(self, file_name):
        full_path = os.path.join(RESOURCES_PATH, file_name)
        assert os.path.exists(full_path), f"Resurce does not exist: {full_path}"
        
        return QUrl().fromLocalFile(full_path)


def get_image_from_url(url):
    # create cache folder
    if not os.path.exists(CACHE_FOLDER):
        os.makedirs(CACHE_FOLDER)
    
    image_file_name = url.split("/")[-1]
    image_path = os.path.join(CACHE_FOLDER, image_file_name)

    # if image exists return with a QUrl
    if os.path.exists(image_path):
        # print(f"Get: {image_path}")
        return QUrl().fromLocalFile(image_path)
    
    assert requests.get(url).status_code == 200, f"BAD REQUEST: {url}"

    img_data = requests.get(url).content
    with open(image_path, "wb") as f:
        f.write(img_data)

    print(f"Downloading: {url}")
    return QUrl().fromLocalFile(image_path) 

if __name__ == "__main__":
    get_image_from_url("https://image.tmdb.org/t/p/w300/1H2xEZOixs0z0JKwyjANZiKNNVJ.jpg")