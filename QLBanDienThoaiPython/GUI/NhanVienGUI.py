from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import StaffBLL
import Staff

# Cua so test
class NhanVienGUI(QMainWindow):
    def __init__(self,staff):
        self.staff = staff
        # print(data)
        super(NhanVienGUI,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/NhanVien.ui',self)
        self.txtUserName.setText(staff.getUserName())
        self.loadListStaff()
        # Bắt sự kiện click button search
        self.btnSearch.clicked.connect(self.handleSearch)
        # Bắt sự kiện click 1 dòng trong table
        self.tblStaff.cellClicked.connect(self.handleCellClicked)
        # Bắt sự kiện click button add
        self.btnAdd.clicked.connect(self.handleAddStaff)
        # Bắt sự kiện click button update
        self.btnEdit.clicked.connect(self.handleUpdateStaff)
        # Bắt sự kiện click button delete
        self.btnDelete.clicked.connect(self.handleDeleteStaff)
        # Bắt sự kiện click button reset
        self.btnReset.clicked.connect(self.handleResetStaff)
        # Bắt sự kiện click button reload
        self.btnReload.clicked.connect(self.handleReload)

    # Load dữ liệu lên table Staff
    def loadListStaff(self):
        listStaff = StaffBLL.StaffBLL().getListStaff()
        self.tblStaff.clearContents()
        self.tblStaff.setColumnCount(7)
        self.tblStaff.setRowCount(20)
        self.tblStaff.setHorizontalHeaderLabels(
            ['StaffID', 'FullName', 'UserName', 'Email', 'Address', 'PhoneNumber', 'Gender'])
        self.tblStaff.verticalHeader().setVisible(False)
        self.tblStaff.resizeColumnsToContents()
        self.tblStaff.setColumnWidth(0, 50)
        self.tblStaff.setColumnWidth(1, 130)
        self.tblStaff.setColumnWidth(2, 130)
        self.tblStaff.setColumnWidth(3, 220)
        self.tblStaff.setColumnWidth(4, 220)
        self.tblStaff.setColumnWidth(5, 100)
        self.tblStaff.setColumnWidth(6, 70)
        for row, staff in enumerate(listStaff):
            self.tblStaff.setItem(row, 0, QTableWidgetItem(str(staff.getStaffID())))
            self.tblStaff.setItem(row, 1, QTableWidgetItem(str(staff.getFullName())))
            self.tblStaff.setItem(row, 2, QTableWidgetItem(str(staff.getUserName())))
            self.tblStaff.setItem(row, 3, QTableWidgetItem(str(staff.getEmail())))
            self.tblStaff.setItem(row, 4, QTableWidgetItem(str(staff.getAddress())))
            self.tblStaff.setItem(row, 5, QTableWidgetItem(str(staff.getPhoneNumber())))
            self.tblStaff.setItem(row, 6, QTableWidgetItem(str(staff.getGender())))

    # Load dữ liệu search
    def loadListStaffSearch(self, listStafftSearch):
        self.tblStaff.clearContents()
        self.tblStaff.setColumnCount(7)
        self.tblStaff.setRowCount(20)
        self.tblStaff.setHorizontalHeaderLabels(
            ['StaffID', 'FullName', 'UserName', 'Email', 'Address', 'PhoneNumber', 'Gender'])
        self.tblStaff.verticalHeader().setVisible(False)
        self.tblStaff.resizeColumnsToContents()
        self.tblStaff.setColumnWidth(0, 50)
        self.tblStaff.setColumnWidth(1, 130)
        self.tblStaff.setColumnWidth(2, 130)
        self.tblStaff.setColumnWidth(3, 220)
        self.tblStaff.setColumnWidth(4, 220)
        self.tblStaff.setColumnWidth(5, 100)
        self.tblStaff.setColumnWidth(6, 70)
        for row, staff in enumerate(listStafftSearch):
            self.tblStaff.setItem(row, 0, QTableWidgetItem(str(staff.getStaffID())))
            self.tblStaff.setItem(row, 1, QTableWidgetItem(str(staff.getFullName())))
            self.tblStaff.setItem(row, 2, QTableWidgetItem(str(staff.getUserName())))
            self.tblStaff.setItem(row, 3, QTableWidgetItem(str(staff.getEmail())))
            self.tblStaff.setItem(row, 4, QTableWidgetItem(str(staff.getAddress())))
            self.tblStaff.setItem(row, 5, QTableWidgetItem(str(staff.getPhoneNumber())))
            self.tblStaff.setItem(row, 6, QTableWidgetItem(str(staff.getGender())))


    # Xử lý sử kiện click 1 dòng trong table
    def handleCellClicked(self, row, column):
        id = self.tblStaff.item(row, 0).text()
        fullName = self.tblStaff.item(row, 1).text()
        usreName = self.tblStaff.item(row, 2).text()
        email = self.tblStaff.item(row, 3).text()
        address = self.tblStaff.item(row, 4).text()
        phoneNumber = self.tblStaff.item(row, 5).text()
        gender = self.tblStaff.item(row, 6).text()

        self.txtStaffID.setText(id)
        self.txtStaffFullName.setText(fullName)
        self.txtStaffUserName.setText(usreName)
        self.txtStaffEmail.setText(email)
        self.txtStaffPhone.setText(phoneNumber)
        self.txtStaffAddress.setText(address)

        i=0
        for i in range(self.cbxGender.count()):
            # print(self.cbxGender.itemText(i))
            if(self.cbxGender.itemText(i) == gender):
                self.cbxGender.setCurrentIndex(i)
                break        

    # Xử lý thêm mới nhân viên
    def handleAddStaff(self):
        fullName = self.txtStaffFullName.text()
        userName = self.txtStaffUserName.text()
        email = self.txtStaffEmail.text()
        gender = self.cbxGender.currentText()
        phoneNumber = self.txtStaffPhone.text()
        address = self.txtStaffAddress.text()
        if (fullName=="" or userName=="" or email=="" or phoneNumber=="" or address == ""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin")
        else:
            staff =Staff.Staff()
            staff.setFullName(fullName)
            staff.setUserName(userName)
            staff.setEmail(email)
            staff.setAddress(address)
            staff.setPhoneNumber(phoneNumber)
            staff.setGender(gender)
            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn thêm mới nhân viên?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(StaffBLL.StaffBLL().insertStaff(staff) == True):
                    QMessageBox.information(self, "Thông báo!", "Thêm thành công")
                    self.loadListStaff()
                else:
                    QMessageBox.information(self, "Thông báo!", "Thêm thất bại")

        

    # Xử lý cập nhật nhân viên
    def handleUpdateStaff(self):
        id = self.txtStaffID.text()
        fullName = self.txtStaffFullName.text()
        userName = self.txtStaffUserName.text()
        email = self.txtStaffEmail.text()
        gender = self.cbxGender.currentText()
        phoneNumber = self.txtStaffPhone.text()
        address = self.txtStaffAddress.text()
        if (id == "" or fullName=="" or userName=="" or email=="" or phoneNumber=="" or address == ""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin")
        else:
            staff =Staff.Staff()
            staff.setStaffID(id)
            staff.setFullName(fullName)
            staff.setUserName(userName)
            staff.setEmail(email)
            staff.setAddress(address)
            staff.setPhoneNumber(phoneNumber)
            staff.setGender(gender)
            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn cập nhật nhân viên?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(StaffBLL.StaffBLL().updateStaff(staff) == True):
                    QMessageBox.information(self, "Thông báo!", "Cập nhật thành công")
                    self.loadListStaff()
                else:
                    QMessageBox.information(self, "Thông báo!", "Cập nhật thất bại")



    # Xử lý xóa nhân viên
    def handleDeleteStaff(self):
        id = self.txtStaffID.text()
        fullName = self.txtStaffFullName.text()
        userName = self.txtStaffUserName.text()
        email = self.txtStaffEmail.text()
        phoneNumber = self.txtStaffPhone.text()
        address = self.txtStaffAddress.text()
        if (id == "" or fullName=="" or userName=="" or email=="" or phoneNumber=="" or address == ""):
            pass
        else:
            msgBox = QMessageBox()
            msgBox.setText("Bạn có chắc muốn xóa hay không?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()            
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(StaffBLL.StaffBLL().deleteStaff(id) == True):
                    QMessageBox.information(self, "Thông báo!", "Xóa nhân viên thành công")
                    self.loadListStaff()
                    self.handleResetStaff()                   
                else:
                    QMessageBox.information(self, "Thông báo!", "Xóa thất bại")



    # Xử lý reset ô nhập liệu
    def handleResetStaff(self):
        self.txtStaffID.setText("")
        self.txtStaffFullName.setText("")
        self.txtStaffUserName.setText("")
        self.txtStaffEmail.setText("")
        self.txtStaffPhone.setText("")
        self.txtStaffAddress.setText("")

    # Xử lý reload table
    def handleReload(self):
        self.loadListStaff()       



    # Xử lý sự kiện tìm kiếm nhân viên
    def handleSearch(self):
        if self.cbxFilter.currentText() == "Search By Code":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listStaffSearch = StaffBLL.StaffBLL().getStaffSearchByCode(keySearch)
                if(len(listStaffSearch) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListStaffSearch(listStaffSearch)
                else:
                    self.loadListStaffSearch(listStaffSearch)
        elif self.cbxFilter.currentText() == "Search By Name":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listStaffSearch = StaffBLL.StaffBLL().getStaffSearchByName(keySearch)
                if(len(listStaffSearch) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListStaffSearch(listStaffSearch)
                else:
                    self.loadListStaffSearch(listStaffSearch)
