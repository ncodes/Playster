# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Fri Aug 16 21:52:46 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Playster(object):
    def setupUi(self, Playster):
        Playster.setObjectName(_fromUtf8("Playster"))
        Playster.resize(795, 541)
        self.appView = QtWebKit.QWebView(Playster)
        self.appView.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.appView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.appView.setObjectName(_fromUtf8("appView"))

        self.retranslateUi(Playster)
        QtCore.QMetaObject.connectSlotsByName(Playster)

    def retranslateUi(self, Playster):
        Playster.setWindowTitle(_translate("Playster", "App", None))

from PyQt4 import QtWebKit
