from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtGui import QDoubleValidator
from datetime import datetime
from PyQt6.QtCore import QDate
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import OrderBLL
import Order
import OrderDetailBLL
import OrderDetail
import StaffBLL
import CustomerBLL
import ProductBLL

# Cua so test
class HoaDonGUI(QMainWindow):
    def __init__(self, staff):
        self.staff = staff
        super(HoaDonGUI,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/HoaDon.ui',self)
        self.txtUserName.setText(staff.getUserName())
        self.setDefault()
        # load danh sách hóa đơn
        self.loadListOrder()
        # Load tbl chi tiết hóa đơn mặc định
        self.loadDetailOrderDefault()
        # Bắt sự kiện click 1 dòng trong tblInvoice
        self.tblInvoice.cellClicked.connect(self.handleTblInvoiceCellClicked)
        # Bắt sự kiện click button Search (tìm kiếm theo mã, theo tên khách hàng)
        self.btnSearchDefault.clicked.connect(self.handleSearchOrder)
        # Bắt sự kiện click button SearchByPrice (tìm kiếm theo giá)
        self.btnSearchByPrice.clicked.connect(self.handleSearchOrderByPrice)
        # Bắt sự kiện click button Search By Date (tìm kiếm theo ngày)
        self.btnSearchByDate.clicked.connect(self.handleSearchByDate)
        # Bắt sự kiện click button reload table invoice
        self.btnReloadTblInvoice.clicked.connect(self.handleReloadTableInvoice)


    # load danh sách hóa đơn    
    def loadListOrder(self):
        listOrder = OrderBLL.OrderBLL().getListOrder()
        self.tblInvoice.clearContents()
        self.tblInvoice.setColumnCount(6)
        self.tblInvoice.setRowCount(20)
        self.tblInvoice.setHorizontalHeaderLabels(['OrderID', 'StaffName', 'CustomerName', 'CreateAt', 'Amount', 'Total'])
        self.tblInvoice.verticalHeader().setVisible(False)
        self.tblInvoice.resizeColumnsToContents()
        self.tblInvoice.setColumnWidth(0, 50)
        self.tblInvoice.setColumnWidth(1, 120)
        self.tblInvoice.setColumnWidth(2, 120)
        self.tblInvoice.setColumnWidth(3, 120)
        self.tblInvoice.setColumnWidth(4, 50)
        self.tblInvoice.setColumnWidth(5, 100)
        for row, od in enumerate(listOrder):
            self.tblInvoice.setItem(row, 0, QTableWidgetItem(str(od.getOrderID())))
            self.tblInvoice.setItem(row, 1, QTableWidgetItem(StaffBLL.StaffBLL().getNameStaffByID(od.getStaffID())))
            self.tblInvoice.setItem(row, 2, QTableWidgetItem(CustomerBLL.CustomerBLL().getNameCustomerByID(od.getCustomerID())))
            self.tblInvoice.setItem(row, 3, QTableWidgetItem(str(od.getCreateAt())))
            self.tblInvoice.setItem(row, 4, QTableWidgetItem(str(od.getAmount())))
            self.tblInvoice.setItem(row, 5, QTableWidgetItem(str(od.getTotal())))

    # load danh sách hóa đơn search 
    def loadListOrderSearch(self, listOrderSearch):
        self.tblInvoice.clearContents()
        self.tblInvoice.setColumnCount(6)
        self.tblInvoice.setRowCount(20)
        self.tblInvoice.setHorizontalHeaderLabels(['OrderID', 'StaffName', 'CustomerName', 'CreateAt', 'Amount', 'Total'])
        self.tblInvoice.verticalHeader().setVisible(False)
        self.tblInvoice.resizeColumnsToContents()
        self.tblInvoice.setColumnWidth(0, 50)
        self.tblInvoice.setColumnWidth(1, 120)
        self.tblInvoice.setColumnWidth(2, 120)
        self.tblInvoice.setColumnWidth(3, 120)
        self.tblInvoice.setColumnWidth(4, 50)
        self.tblInvoice.setColumnWidth(5, 100)
        for row, od in enumerate(listOrderSearch):
            self.tblInvoice.setItem(row, 0, QTableWidgetItem(str(od.getOrderID())))
            self.tblInvoice.setItem(row, 1, QTableWidgetItem(StaffBLL.StaffBLL().getNameStaffByID(od.getStaffID())))
            self.tblInvoice.setItem(row, 2, QTableWidgetItem(CustomerBLL.CustomerBLL().getNameCustomerByID(od.getCustomerID())))
            self.tblInvoice.setItem(row, 3, QTableWidgetItem(str(od.getCreateAt())))
            self.tblInvoice.setItem(row, 4, QTableWidgetItem(str(od.getAmount())))
            self.tblInvoice.setItem(row, 5, QTableWidgetItem(str(od.getTotal())))

    # Xử lý sự kiện click 1 dòng trong tblInvoice
    def handleTblInvoiceCellClicked(self, row, column):
        invoiceId = self.tblInvoice.item(row, 0).text()
        self.loadDetailOrderByOrderID(invoiceId)

        staffName = self.tblInvoice.item(row, 1).text()
        cusName = self.tblInvoice.item(row, 2).text()
        createAt = self.tblInvoice.item(row, 3).text()
        amount = self.tblInvoice.item(row, 4).text()
        total = self.tblInvoice.item(row, 5).text()

        dateCreate = datetime.strptime(createAt, "%Y-%m-%d").date()
        self.txtInvoiceID.setText(invoiceId)
        self.txtStaffName.setText(staffName)
        self.txtCusName.setText(cusName)
        self.dateCreate.setDate(dateCreate)
        self.txtAmount.setText(amount)
        self.txtTotal.setText(total)

    # Load table chi tiết hóa đơn mặc định    
    def loadDetailOrderDefault(self):
        self.tblDetailInvoice.clearContents()
        self.tblDetailInvoice.setColumnCount(5)
        self.tblDetailInvoice.setRowCount(20)
        self.tblDetailInvoice.setHorizontalHeaderLabels(['OrderID', 'ProductName', 'Amount', 'Price', 'SubTotal'])
        self.tblDetailInvoice.verticalHeader().setVisible(False)
        self.tblDetailInvoice.resizeColumnsToContents()
        self.tblDetailInvoice.setColumnWidth(0, 60)
        self.tblDetailInvoice.setColumnWidth(1, 140)
        self.tblDetailInvoice.setColumnWidth(2, 60)
        self.tblDetailInvoice.setColumnWidth(3, 100)
        self.tblDetailInvoice.setColumnWidth(4, 100)

    # Load chi tiết hóa đơn theo mã hóa đơn
    def loadDetailOrderByOrderID(self, id):
        listDetailOrder = OrderDetailBLL.OrderDetailBLL().getListOrderDetailByOrderID(id)
        self.tblDetailInvoice.clearContents()
        self.tblDetailInvoice.setColumnCount(5)
        self.tblDetailInvoice.setRowCount(20)
        self.tblDetailInvoice.setHorizontalHeaderLabels(['OrderID', 'ProductName', 'Amount', 'Price', 'SubTotal'])
        self.tblDetailInvoice.verticalHeader().setVisible(False)
        self.tblDetailInvoice.resizeColumnsToContents()
        self.tblDetailInvoice.setColumnWidth(0, 60)
        self.tblDetailInvoice.setColumnWidth(1, 140)
        self.tblDetailInvoice.setColumnWidth(2, 60)
        self.tblDetailInvoice.setColumnWidth(3, 100)
        self.tblDetailInvoice.setColumnWidth(4, 100)
        for row, odd in enumerate(listDetailOrder):
            self.tblDetailInvoice.setItem(row, 0, QTableWidgetItem(str(odd.getOrderID())))
            self.tblDetailInvoice.setItem(row, 1, QTableWidgetItem(str(ProductBLL.ProductBLL().getNameProductByID(odd.getProductID()))))
            self.tblDetailInvoice.setItem(row, 2, QTableWidgetItem(str(odd.getAmount())))
            self.tblDetailInvoice.setItem(row, 3, QTableWidgetItem(str(odd.getPrice())))
            self.tblDetailInvoice.setItem(row, 4, QTableWidgetItem(str(odd.getSubTotal())))

    # Xử lý search hóa đơn theo mã, tên khách hàng
    def handleSearchOrder(self):
        if self.cbxFilter.currentText() == "Search By Code Order":
            keySearch = self.txtSearch.text()
            if(keySearch == ""):
                pass
            else:
                listOrderSearch = OrderBLL.OrderBLL().getOrderByID(keySearch)
                if(len(listOrderSearch) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                else:
                    self.loadListOrderSearch(listOrderSearch)
        elif self.cbxFilter.currentText() == "Search By Customer Name":
            keySearch = self.txtSearch.text()
            if(keySearch == ""):
                pass
            else:
                listOrderSearch = OrderBLL.OrderBLL().getOrderByCustomerName(keySearch)
                if(len(listOrderSearch) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                else:
                    self.loadListOrderSearch(listOrderSearch)

    # Xử lý search hóa đơn theo giá
    def handleSearchOrderByPrice(self):
        if(self.txtPriceFrom.text() and self.txtPriceTo.text()):             
            try:
                priceFrom = float(self.txtPriceFrom.text())
                priceTo = float(self.txtPriceTo.text())
                if(priceTo >= priceFrom):
                    listOrderSearch = OrderBLL.OrderBLL().getOrderByPrice(priceFrom, priceTo)
                    if(len(listOrderSearch) == 0):
                        QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    else:
                        self.loadListOrderSearch(listOrderSearch)
                else:
                    QMessageBox.information(self, "Thông báo!", "Giá sau phải lớn hơn giá trước!")
            except ValueError:
                QMessageBox.information(self, "Thông báo!", "Vui lòng nhập số!")
                self.txtPriceFrom.setText("")
                self.txtPriceTo.setText("")
        else:
            QMessageBox.information(self, "Thông báo!", "Vui lòng nhập đủ thông tin tìm kiếm!")

    # Xử lý search theo ngày
    def handleSearchByDate(self):
        selectedDateFrom = self.dateFrom.date()
        selectedDateTo = self.dateTo.date()
        dateFrom = datetime.strptime((str(selectedDateFrom.year())+"-"+str(selectedDateFrom.month())+"-"+str(selectedDateFrom.day())),"%Y-%m-%d").date()
        dateTo = datetime.strptime((str(selectedDateTo.year())+"-"+str(selectedDateTo.month())+"-"+str(selectedDateTo.day())),"%Y-%m-%d").date()
        if(dateFrom > dateTo):
            QMessageBox.information(self, "Thông báo!", "Vui lòng nhập thông tin hợp lệ. Ngày sau phải lớn hơn ngày trước!")
        else:
            listOrderSearch = OrderBLL.OrderBLL().getOrderByDate(dateFrom, dateTo)
            if(len(listOrderSearch) == 0):
                QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
            else:
                self.loadListOrderSearch(listOrderSearch)

    # Xử lý reload table invoice
    def handleReloadTableInvoice(self):
        self.loadListOrder()
        self.loadDetailOrderDefault()

    def setDefault(self):
        timeNow = datetime.now()
        self.dateFrom.setDate(timeNow)
        self.dateTo.setDate(timeNow)            
        self.txtPriceFrom.setValidator(QDoubleValidator())
        self.txtPriceTo.setValidator(QDoubleValidator())

    