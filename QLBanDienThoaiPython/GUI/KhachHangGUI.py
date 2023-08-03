from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import Customer
import CustomerBLL

# Cua so test
class KhachHangGUI(QMainWindow):
    def __init__(self, staff):
        self.staff = staff
        super(KhachHangGUI,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/KhachHang.ui',self)
        self.txtUserName.setText(staff.getUserName())
        self.loadListCustomer()
        # Bắt sự kiện click button search
        self.btnSearch.clicked.connect(self.handleSearch)
        # Bắt sự kiện click 1 dòng trong table
        self.tblCustomer.cellClicked.connect(self.handleCellClicked)
        # Bắt sự kiện click button add
        self.btnAdd.clicked.connect(self.handleAddCustomer)
        # Bắt sự kiện click button update
        self.btnEdit.clicked.connect(self.handleUpdateCustomer)
        # Bắt sự kiện click button delete
        self.btnDelete.clicked.connect(self.handleDeleteCustomer)
        # Bắt sự kiện click button reset
        self.btnReset.clicked.connect(self.handleResetCustomer)
        # Bắt sự kiện click button reload
        self.btnReload.clicked.connect(self.handleReload)

    # Load dữ liệu lên table Staff
    def loadListCustomer(self):
        listCustomer = CustomerBLL.CustomerBLL().getListCustomer()
        self.tblCustomer.clearContents()
        self.tblCustomer.setColumnCount(5)
        self.tblCustomer.setRowCount(20)
        self.tblCustomer.setHorizontalHeaderLabels(
            ['CustomerID', 'CustomerName', 'PhoneNumber', 'Email', 'Address'])
        self.tblCustomer.verticalHeader().setVisible(False)
        self.tblCustomer.resizeColumnsToContents()
        self.tblCustomer.setColumnWidth(0, 100)
        self.tblCustomer.setColumnWidth(1, 190)
        self.tblCustomer.setColumnWidth(2, 150)
        self.tblCustomer.setColumnWidth(3, 245)
        self.tblCustomer.setColumnWidth(4, 245)
        for row, cus in enumerate(listCustomer):
            self.tblCustomer.setItem(row, 0, QTableWidgetItem(str(cus.getCustomerID())))
            self.tblCustomer.setItem(row, 1, QTableWidgetItem(str(cus.getCustomerName())))
            self.tblCustomer.setItem(row, 2, QTableWidgetItem(str(cus.getPhoneNumber())))
            self.tblCustomer.setItem(row, 3, QTableWidgetItem(str(cus.getEmail())))
            self.tblCustomer.setItem(row, 4, QTableWidgetItem(str(cus.getAddress())))
        
    # Load dữ liệu search
    def loadListCustomerSearch(self, listCustomertSearch):
        self.tblCustomer.clearContents()
        self.tblCustomer.setColumnCount(5)
        self.tblCustomer.setRowCount(20)
        self.tblCustomer.setHorizontalHeaderLabels(
            ['CustomerID', 'CustomerName', 'PhoneNumber', 'Email', 'Address'])
        self.tblCustomer.verticalHeader().setVisible(False)
        self.tblCustomer.resizeColumnsToContents()
        self.tblCustomer.setColumnWidth(0, 100)
        self.tblCustomer.setColumnWidth(1, 190)
        self.tblCustomer.setColumnWidth(2, 150)
        self.tblCustomer.setColumnWidth(3, 245)
        self.tblCustomer.setColumnWidth(4, 245)
        for row, cus in enumerate(listCustomertSearch):
            self.tblCustomer.setItem(row, 0, QTableWidgetItem(str(cus.getCustomerID())))
            self.tblCustomer.setItem(row, 1, QTableWidgetItem(str(cus.getCustomerName())))
            self.tblCustomer.setItem(row, 2, QTableWidgetItem(str(cus.getPhoneNumber())))
            self.tblCustomer.setItem(row, 3, QTableWidgetItem(str(cus.getEmail())))
            self.tblCustomer.setItem(row, 4, QTableWidgetItem(str(cus.getAddress())))


    # Xử lý sử kiện click 1 dòng trong table
    def handleCellClicked(self, row, column):
        id = self.tblCustomer.item(row, 0).text()
        name = self.tblCustomer.item(row, 1).text()
        phone = self.tblCustomer.item(row, 2).text()
        email = self.tblCustomer.item(row, 3).text()
        address = self.tblCustomer.item(row, 4).text()
    
        self.txtID.setText(id)
        self.txtName.setText(name)
        self.txtEmail.setText(email)
        self.txtPhone.setText(phone)
        self.txtAddress.setText(address)
   

    # Xử lý thêm mới khách hàng
    def handleAddCustomer(self):
        name = self.txtName.text()
        email = self.txtEmail.text()
        phone = self.txtPhone.text()
        address = self.txtAddress.text()
        if (name=="" or email=="" or phone=="" or address==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin")
        else:
            customer =Customer.Customer()
            customer.setCustomerName(name)
            customer.setEmail(email)
            customer.setAddress(address)
            customer.setPhoneNumber(phone)
            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn thêm mới khách hàng?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(CustomerBLL.CustomerBLL().insertCustomer(customer) == True):
                    QMessageBox.information(self, "Thông báo!", "Thêm thành công")
                    self.loadListCustomer()
                else:
                    QMessageBox.information(self, "Thông báo!", "Thêm thất bại")

        

    # Xử lý cập nhật khách hàng
    def handleUpdateCustomer(self):
        id = self.txtID.text()
        name = self.txtName.text()
        email = self.txtEmail.text()
        phone = self.txtPhone.text()
        address = self.txtAddress.text()
        if (name=="" or email=="" or phone=="" or address=="" or id ==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin")
        else:
            customer =Customer.Customer()
            customer.setCustomerID(id)
            customer.setCustomerName(name)
            customer.setEmail(email)
            customer.setAddress(address)
            customer.setPhoneNumber(phone)
            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn cập nhật khách hàng?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(CustomerBLL.CustomerBLL().updateCustomer(customer) == True):
                    QMessageBox.information(self, "Thông báo!", "Cập nhật thành công")
                    self.loadListCustomer()
                else:
                    QMessageBox.information(self, "Thông báo!", "Cập nhật thất bại")



    # Xử lý xóa khách hàng
    def handleDeleteCustomer(self):
        id = self.txtID.text()
        name = self.txtName.text()
        email = self.txtEmail.text()
        phone = self.txtPhone.text()
        address = self.txtAddress.text()
        if (name=="" or email=="" or phone=="" or address=="" or id ==""):
            pass
        else:
            msgBox = QMessageBox()
            msgBox.setText("Bạn có chắc muốn xóa hay không?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()            
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(CustomerBLL.CustomerBLL().deleteCustomer(id) == True):
                    QMessageBox.information(self, "Thông báo!", "Xóa khách hàng thành công")
                    self.loadListCustomer()
                    self.handleResetCustomer()                   
                else:
                    QMessageBox.information(self, "Thông báo!", "Xóa thất bại")



    # Xử lý reset ô nhập liệu
    def handleResetCustomer(self):
        self.txtID.setText("")
        self.txtName.setText("")
        self.txtEmail.setText("")
        self.txtPhone.setText("")
        self.txtAddress.setText("")


    def handleReload(self):
        self.loadListCustomer()

    # Xử lý sự kiện tìm kiếm khách hàng
    def handleSearch(self):
        if self.cbxFilter.currentText() == "Search By Code":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listCustomerSearch = CustomerBLL.CustomerBLL().getCustomerSearchByCode(keySearch)
                if(len(listCustomerSearch) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListCustomerSearch(listCustomerSearch)
                else:
                    self.loadListCustomerSearch(listCustomerSearch)
        elif self.cbxFilter.currentText() == "Search By Name":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listCustomerSearch = CustomerBLL.CustomerBLL().getCustomerSearchByName(keySearch)
                if(len(listCustomerSearch) == 0):                    
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListCustomerSearch(listCustomerSearch)
                else:
                    self.loadListCustomerSearch(listCustomerSearch)