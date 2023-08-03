from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys

# Cua so test
class test_w(QMainWindow):
    def __init__(self):
        super(test_w,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/test.ui',self)