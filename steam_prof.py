import requests
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from steam_web_api import Steam
import os
import sys

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('Main_Steam.ui',self)
        self.show()

        self.Steamid_Submit_Btn.clicked.connect(self.SteamIdSubmit)

        self.AppStart()

        self.SteamKey = os.environ.get("STEAM_API_KEY")
        self.steam = Steam(self.SteamKey)





    def SteamIdSubmit(self):
        self.steamid = self.Steamid_Input.text().strip()
        #my steam id: 76561198140493349


        if  self.steamid and len(self.steamid) == 17:

            try:
                res = self.steam.users.get_user_details(self.steamid)["player"]
                self.SteamIdErr.setVisible(False)
                self.Result.setVisible(True)
                self.ProfName.setText(res["personaname"])
                self.ProfImage.setPixmap(self.GetImage(res["avatarfull"]))


            except Exception as e:
                print(e)
                self.SteamIdErr.setVisible(True)
                self.Result.setVisible(False)

        else:
            self.SteamIdErr.setVisible(True)
            self.Result.setVisible(False)




    def AppStart(self):
        self.Result.setVisible(False)
        self.SteamIdErr.setVisible(False)

    def GetImage(self, URL):
        response = requests.get(URL)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()




