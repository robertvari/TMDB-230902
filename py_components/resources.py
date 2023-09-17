from PySide6.QtCore import QObject, Slot, QUrl
import os


RESOURCES_PATH = os.path.dirname(__file__).replace("py_components", "resources")

class Resources(QObject):
    @Slot(str, result=QUrl)
    def get(self, file_name):
        full_path = os.path.join(RESOURCES_PATH, file_name)
        assert os.path.exists(full_path), f"Resurce does not exist: {full_path}"
        
        return QUrl().fromLocalFile(full_path)
    
if __name__ == "__main__":
    r = Resources()
    print(r.get("logo.svg"))