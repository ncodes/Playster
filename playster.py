# -*- coding: utf-8 -*-
import ui
import sys
from PyQt4 import QtCore, QtGui
from components import server

class Main(QtGui.QWidget):

    # Initialize the widget
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.playster = ui.Ui_Playster()
        self.playster.setupUi(self)
        self.setup()

    # Shows or hides the window frame
    def showWindowFrame(self, show = True):
        if show:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.FramelessWindowHint)
        else:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


    # resize the app. Applies to both app window and webview
    def resizeWindow(self, width, height):
        self.resize(QtCore.QSize(width, height))
        self.playster.appView.resize(QtCore.QSize(width, height))


    # setup the login window
    def setup(self):

        # set title
        self.setWindowTitle('Playster - The internet\'s social music player')

        # set icon
        self.setWindowIcon(QtGui.QIcon(":/icon"))

        # resize the app window and webview
        self.resizeWindow(1000, 600)

        # set flags for fixed and translucent window
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        #self.components.appView.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Hide the window frame
        self.showWindowFrame(0)

        # set webview background to be transparent
        palette = self.playster.appView.palette()
        palette.setBrush(QtGui.QPalette.Base, QtCore.Qt.transparent)
        self.playster.appView.page().setPalette(palette)
        self.playster.appView.setAttribute(QtCore.Qt.WA_OpaquePaintEvent, False)

        # start server
        server.start()

        # set webview url
        #self.appView.webView.setUrl(QtCore.QUrl('qrc:///mainPage'))
        self.playster.appView.setUrl(QtCore.QUrl('http://google.com'))

# run app
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    playsterApp = Main()
    playsterApp.show()
    sys.exit(app.exec_())