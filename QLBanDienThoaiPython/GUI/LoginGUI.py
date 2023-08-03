from PyQt6 import QtCore, QtGui, QtWidgets, uic     
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
import sys
import main
import RegisterGUI
sys.path.append('./QLBanDienThoaiPython/BLL')
import StaffBLL

class LoginGUI(QMainWindow):

    def __init__(self):
        super(LoginGUI, self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/Login.ui', self)
        self.btnLogin.clicked.connect(self.checkLoginSucces)
        self.btnRegister.clicked.connect(self.handlRegister)

    def checkLoginSucces(self):
        userName = self.txtUserName.text()
        passWord = self.txtPassword.text()
        if(userName == "" or passWord ==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin")
        else:
            staff = StaffBLL.StaffBLL().checkLogin(userName, passWord) 
            if(staff != None):
                mainGUI = main.MainWindow(staff)
                self.hide()
                mainGUI.show()        
            else:
                QMessageBox.information(self, "Thông báo!", "Thông tin tài khoản hoặc mật khẩu không chính xác!")

    def handlRegister(self):
        registerGUI = RegisterGUI.RegisterGUI()
        self.hide()
        registerGUI.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginGUI()
    window.show()
    sys.exit(app.exec())