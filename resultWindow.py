from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap,QMovie
import requests

class SecondWindow(QtWidgets.QMainWindow):
    def __init__(self, userdata, gamedata):
        super(SecondWindow,self).__init__()
        uic.loadUi('ResWindow.ui',self)

        self.firsttab(userdata)
        self.secondtab(userdata,gamedata)
        self.setStyleSheet(open("style.qss").read())


    def secondtab(self,userdata, gamedata):
        if userdata["communityvisibilitystate"] != 3:
            self.ProfilePrivateMess.setText("This Profile is Private!")
        else:
            self.GameTitle1.setText(gamedata["games"][0]["name"])
            self.GameImage1.setPixmap(self.GetImage(f'https://cdn.cloudflare.steamstatic.com/steam/apps/{gamedata["games"][0]["appid"]}/capsule_231x87.jpg'))
            self.GameHours1.setText(str(gamedata["games"][0]["playtime_forever"]//60) + " hours")

    def firsttab(self, userdata):
        self.ProfName.setText(userdata['personaname'])
        self.ProfImage.setPixmap(self.GetImage(userdata["avatarfull"]))

        #76561198140493349
        #76561197960287930

        self.status_map = {
            1: "Online",
            2: "Busy",
            3: "Away",
            4: "Snooze",
            5: "Looking to trade",
            6: "Looking to play"
            }

        self.status = userdata.get("personastate", 0)

        self.CurrStatus.setText(self.status_map.get(self.status, "Offline"))

        self.country = userdata.get('loccountrycode')

        if self.country:
            self.Country.setText(userdata["loccountrycode"])
            #https://flagsapi.com/#sizes
            self.CountryFlag.setPixmap(self.GetImage(f'https://flagsapi.com/{userdata["loccountrycode"]}/flat/48.png'))
        else:
            self.Country.setText("Unknown")
            self.CountryFlag.clear()

        self.ProfileUrl.setText(f'<a href=\"{userdata['profileurl']}\"> {userdata['profileurl']} </a>')

    def GetImage(self, url):
        try:
            response = requests.get(url)
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            return pixmap

        except Exception as e:
            print(e)
            return None