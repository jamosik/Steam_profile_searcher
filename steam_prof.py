from PyQt5 import QtWidgets, uic
from steam_web_api import Steam
import os
import sys
from resultWindow import SecondWindow

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('Main_Steam.ui',self)
        self.setStyleSheet(open("style.qss").read())
        self.show()

        self.Steamid_Submit_Btn.clicked.connect(self.SteamIdSubmit)

        self.AppStart()

        self.SteamKey = os.environ.get("STEAM_API_KEY")

        try:
            self.steam = Steam(self.SteamKey)
        except Exception as e:
            print(e)




    def SteamIdSubmit(self):
        self.steamid = self.Steamid_Input.text().strip()
        #my steam id: 76561198140493349


        if  self.steamid and len(self.steamid) == 17:

            try:
                userdata = self.steam.users.get_user_details(self.steamid)["player"]
                gamedata = self.steam.users.get_user_recently_played_games(self.steamid)
                self.SteamIdErr.setVisible(False)
                self.secWin  = SecondWindow(userdata, gamedata)
                self.secWin.show()



            except Exception as e:
                print(e)
                self.SteamIdErr.setVisible(True)


        else:
            self.SteamIdErr.setVisible(True)





    def AppStart(self):
        self.SteamIdErr.setVisible(False)



app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()




