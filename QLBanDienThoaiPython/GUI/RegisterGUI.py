from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import StaffBLL
import Staff

# Cua so test
class RegisterGUI(QMainWindow):
    def __init__(self):        
        super(RegisterGUI,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/Register.ui',self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterGUI()
    window.show()
    sys.exit(app.exec())