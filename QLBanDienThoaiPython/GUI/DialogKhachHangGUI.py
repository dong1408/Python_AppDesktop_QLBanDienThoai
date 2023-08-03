from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import Customer
import CustomerBLL


# Cua so test
class DialogKhachHangGUI(QtWidgets.QDialog):
    customer = None
    listCustomer = None
    def __init__(self):
        super(DialogKhachHangGUI,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/DialogKhachHang.ui',self)
        self.loadListCustomer()

        # Kết nối các sự kiện click với các phương thức tương ứng
        self.btnSelect.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        # Bắt sự kiện click button search
        self.btnSearch.clicked.connect(self.handleSearch)
        # Bắt sự kiện click button refresh
        self.btnRefresh.clicked.connect(self.handleRefresh)
        # Bắt sự kiện click 1 dòng table
        self.tblCustomer.cellClicked.connect(self.handleCellClicked)


    # Load dữ liệu lên table Staff
    def loadListCustomer(self):
        self.listCustomer = CustomerBLL.CustomerBLL().getListCustomer()
        self.tblCustomer.clearContents()
        self.tblCustomer.setColumnCount(5)
        self.tblCustomer.setRowCount(20)
        self.tblCustomer.setHorizontalHeaderLabels(
            ['CustomerID', 'CustomerName', 'PhoneNumber', 'Email', 'Address'])
        self.tblCustomer.verticalHeader().setVisible(False)
        self.tblCustomer.resizeColumnsToContents()
        self.tblCustomer.setColumnWidth(0, 80)
        self.tblCustomer.setColumnWidth(1, 140)
        self.tblCustomer.setColumnWidth(2, 100)
        self.tblCustomer.setColumnWidth(3, 200)
        self.tblCustomer.setColumnWidth(4, 215)
        for row, cus in enumerate(self.listCustomer):
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
        self.tblCustomer.setColumnWidth(0, 80)
        self.tblCustomer.setColumnWidth(1, 140)
        self.tblCustomer.setColumnWidth(2, 100)
        self.tblCustomer.setColumnWidth(3, 200)
        self.tblCustomer.setColumnWidth(4, 215)
        for row, cus in enumerate(listCustomertSearch):
            self.tblCustomer.setItem(row, 0, QTableWidgetItem(str(cus.getCustomerID())))
            self.tblCustomer.setItem(row, 1, QTableWidgetItem(str(cus.getCustomerName())))
            self.tblCustomer.setItem(row, 2, QTableWidgetItem(str(cus.getPhoneNumber())))
            self.tblCustomer.setItem(row, 3, QTableWidgetItem(str(cus.getEmail())))
            self.tblCustomer.setItem(row, 4, QTableWidgetItem(str(cus.getAddress())))

    # Xử lý sự kiện tìm kiếm khách hàng
    def handleSearch(self):
        if self.cbxFilter.currentText() == "Search By Code":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                self.listCustomer = CustomerBLL.CustomerBLL().getCustomerSearchByCode(keySearch)
                if(len(self.listCustomer) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListCustomerSearch(self.listCustomer)
                else:
                    self.loadListCustomerSearch(self.listCustomer)
        elif self.cbxFilter.currentText() == "Search By Name":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                self.listCustomer = CustomerBLL.CustomerBLL().getCustomerSearchByName(keySearch)
                if(len(self.listCustomer) == 0):                    
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListCustomerSearch(self.listCustomer)
                else:
                    self.loadListCustomerSearch(self.listCustomer)
        elif self.cbxFilter.currentText() == "Search By PhoneNumber":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                self.listCustomer = CustomerBLL.CustomerBLL().getCustomerSearchByPhone(keySearch)
                if(len(self.listCustomer) == 0):                    
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListCustomerSearch(self.listCustomer)
                else:
                    self.loadListCustomerSearch(self.listCustomer)

    # Xử lý refresh 
    def handleRefresh(self):
        self.loadListCustomer()

    def handleCellClicked(self, row, column):
        self.customer = self.listCustomer[row]
        
    def getCustomerClick(self):
        if self.customer == None:
            return None
        return self.customer
        