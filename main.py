import subprocess
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLineEdit, QRadioButton)
from PyQt5.QtGui import QFont

hasVideo = True
link = ""

class appmain(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        linkinput = QLineEdit(self)
        linkinput.move(10,10)

        radiobuttonV = QRadioButton("Video", self)
        radiobuttonV.formattype = "Video"
        radiobuttonV.toggled.connect(self.radioClicked)
        radiobuttonV.setChecked(True)

        radiobuttonA = QRadioButton("Audio", self)
        radiobuttonA.formattype = "Audio"
        radiobuttonA.toggled.connect(self.radioClicked)

        radiobuttonV.move(10, 50)
        radiobuttonA.move(10, 80)

        btn = QPushButton('Download', self)
        btn.setToolTip('<b>start</b>')
        btn.resize(btn.sizeHint())
        btn.move(10, 160)

        btn.clicked.connect(self.buttonClicked)
        linkinput.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('yotub dl ting')
        self.show()

    def onChanged(self, text):
        global link
        link = text
    
    def buttonClicked(self):
        if hasVideo:
            print("Downloading %s with video" % link)
            subprocess.run(["yt-dlp.exe", "-S", "res,ext:mp4:m4a", "--recode", "mp4", "-o", "\"%(title)s.%(ext)s\"", "%s" % link])
        else:
            print("Downloading %s with no video" % link)
            subprocess.run(["yt-dlp.exe", "--format", "bestaudio", "-x", "--audio-format", "mp3", "-o", "\"%(title)s.%(ext)s\"", "%s" % link])


    def radioClicked(self):
        global hasVideo
        radioButton = self.sender()
        if radioButton.isChecked():
            if radioButton.formattype == "Audio":
                hasVideo = False
            else:
                hasVideo = True  

def main():
    app = QApplication(sys.argv)
    widgetmain = appmain()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()