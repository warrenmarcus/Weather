
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtGui import *
import sys
import requests


class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.initUI()



    def initUI(self):
        self.bgcolor = "background-color: qlineargradient(x1: 0, y1: .75, x2: 1  , stop: 1 #9bf2e3, stop: 0 #ffa3ce)"
        self.revBg = "background-color: qlineargradient(x1: 0, y1: .75, x2: 1  , stop: 1 #ffa3ce, stop: 0 #9bf2e3)"
        self.trans = "background-color: transparent"


        self.setGeometry(400,300,600,400)
        self.setWindowTitle("Weather App")
        self.setStyleSheet(self.bgcolor)

        self.frame1 = QtWidgets.QFrame(self)
        self.frame1.resize(400,325)
        self.frame1.setStyleSheet(self.trans)
        self.frame1.move(150,35)


        self.Labelsetup()

        self.citySelect = QtWidgets.QLineEdit(self)
        self.citySelect.setStyleSheet(self.revBg)
        self.citySelect.move(25, 350)
        self.citySelect.returnPressed.connect(self.onSubmit)

    def Labelsetup(self):

        font1 = 'MS Gothic'

        self.cityLabel = QtWidgets.QLabel(self.frame1)
        self.cityLabel.move(100, 10)
        self.cityLabel.setFont(QFont(font1, 35))

        self.Temp = QtWidgets.QLabel(self.frame1)
        self.Temp.move(100,75)
        self.Temp.setFont(QFont(font1, 35))

        self.subTemp = QtWidgets.QLabel(self.frame1)
        self.subTemp.move(100,125)
        self.subTemp.setFont(QFont(font1, 14))

        self.subdata = QtWidgets.QLabel(self.frame1)
        self.subdata.move(100,175)
        self.subdata.setFont(QFont(font1,20))

        self.statLabel = QtWidgets.QLabel(self)
        self.statLabel.move(25,25)
        self.statLabel.resize(175, 175)
        self.statLabel.setStyleSheet(self.trans)

        self.cond = QtWidgets.QLabel(self)
        self.cond.move(73, 200)
        self.cond.setFont(QFont(font1,20))
        self.cond.setStyleSheet(self.trans)




    def onSubmit(self):
        city = self.citySelect.text()
        self.getWeather(city)
        self.citySelect.setText('')

    def getCondition(self, condition):
        if condition == "Rain":
            pixmap = QPixmap(rainImage)
            self.statLabel.setPixmap(pixmap)
        if condition == "Clear":

            pixmap = QPixmap(sunImage)
            self.statLabel.setPixmap(pixmap)

        if condition == "Clouds":
            pixmap = QPixmap(cloud)
            self.statLabel.setPixmap(pixmap)
        if condition =="Smoke":
            pixmap = QPixmap(smoke)
            self.statLabel.setPixmap(pixmap)


    def getWeather(self,city):
        api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8363e074658aba90f3d8dcd32a55095b"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']

    # Data
        temp = int((json_data['main']['temp'] - 273)*(1.8)+32)
        max_temp = int((json_data['main']['temp_max'] - 273)*(1.8)+32)
        min_temp = int((json_data['main']['temp_min'] - 273)*(1.8)+32)
        humidity = str(json_data['main']['humidity'])
        wind = json_data['wind']['gust']
        flike = int((json_data['main']['feels_like'] - 273)*(1.8)+32)
        sunrise = str(json_data['sys']['sunrise'])
        sunset = str(json_data['sys']['sunset'])


        info =  str(temp) + '\u00b0' + "F"
        subtemp = " H: " + str(max_temp) + '\u00b0' + " L: " + str(min_temp) + '\u00b0'
        data = "Feels like: " + str(flike) + '\u00b0' + "F" + \
               "\nHumidity " + humidity + "%" + \
               "\nWind speed " + str(round((wind * 2.24), 2)) + 'mph'


        self.Temp.setText(info)
        self.Temp.adjustSize()

        self.subTemp.setText(subtemp)
        self.subTemp.adjustSize()

        self.subdata.setText(data)
        self.subdata.adjustSize()

        self.getCondition(condition)
        self.cond.setText(condition)

        self.cityLabel.setText(city)
        self.cityLabel.adjustSize()
def canvas():
    app = QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())


sunImage = r'sunpng.png'
rainImage = r'rain.png'
cloud = r'clearClouds2.png'
smoke = r'smoke.png'
canvas()


