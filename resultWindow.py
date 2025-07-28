from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import requests

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super(SecondWindow,self).__init__()
        uic.loadUi('ResWindow.ui',self)
        self.ProfName.setText(data['personaname'])
        self.ProfImage.setPixmap(self.GetImage(data["avatarfull"]))

        self.status_map = {
            1: "Online",
            2: "Busy",
            3: "Away",
            4: "Snooze",
            5: "Looking to trade",
            6: "Looking to play"

            }
        self.CurrStatus.setText(self.status_map[data["personastate"]])

    def GetImage(self, URL):
        response = requests.get(URL)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap