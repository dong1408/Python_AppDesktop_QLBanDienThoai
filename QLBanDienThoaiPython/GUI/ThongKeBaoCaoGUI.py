from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from datetime import datetime
UserRole = QtCore.Qt.ItemDataRole.UserRole
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import OrderBLL
import CategoryBLL
import ProductBLL
import CategoryItem
import Category
import Product

class ThongKeBaoCaoGUI(QMainWindow):

    def __init__(self,staff):
        self.staff = staff
        super(ThongKeBaoCaoGUI, self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/ThongKeBaoCao.ui', self)
        self.setDefault()        
        self.loadCategoryToCbx()
        self.loadTableOrderDefault()
        self.loadTableProductDefault()
        # Bắt sự kiện click button filter doanh thu theo quý
        self.btnFilterByQuarterly.clicked.connect(self.handleQuarterlyRevenueStatistics)
        # Bắt sự kiện click button filter doanh thu theo tháng
        self.btnFilterByMonthRevenue.clicked.connect(self.handelMonthlyRevenueStatistics)
        # Bắt sự kiện click button reload table order
        self.btnReloadTableOrder.clicked.connect(self.handleReloadTableOrder)
        # Bắt sự kiện click button reload table product
        self.btnReloadTableProduct.clicked.connect(self.handleReloadTableProduct)
        # Bắt sự kiện click button filter sản phẩm theo danh mục
        self.btnSearch.clicked.connect(self.handleStatisticsByCategory)
        # Bắt sự kiện click button filter sản phẩm theo ngày tháng
        self.btnFilterByMonthProduct.clicked.connect(self.handleMonthlyProductStatistics)

    # Load dữ liệu lên combobox Category
    def loadCategoryToCbx(self):
        listCat = CategoryBLL.CategoryBLL().getListCategory()
        model = QStandardItemModel()
        for category in listCat:
            item = QStandardItem(category.getCategoryName())
            item.setData(category, role = UserRole)  # Lưu trữ đối tượng Category
            model.appendRow(item)
        self.cbxCategory.setModel(model)

    def setDefault(self):
        for i in range(2000,2100):
            self.cbxYear.addItem(str(i))
        # Lấy thời gian hiện tại
        timeNow = datetime.now()
        self.dateFromByRevenue.setDate(timeNow)
        self.dateToByRevenue.setDate(timeNow)     
        self.dateFromByProduct.setDate(timeNow)
        self.dateToByProduct.setDate(timeNow)

    # load table Order mặc định
    def loadTableOrderDefault(self):
        now = datetime.now() # Lấy thời điểm hiện tại
        firstDay = datetime.strptime((str(now.year)+"-"+str(now.month)+"-"+str(1)), "%Y-%m-%d").date() 
        result = OrderBLL.OrderBLL().statisticalOrderByMonth(firstDay, now)
        self.tblInvoice.clearContents()
        self.tblInvoice.setColumnCount(4)
        self.tblInvoice.setRowCount(20)
        self.tblInvoice.setHorizontalHeaderLabels(['OrderID', 'CustomerName', 'CreateAt', 'Total'])
        self.tblInvoice.verticalHeader().setVisible(False)
        self.tblInvoice.resizeColumnsToContents()
        self.tblInvoice.setColumnWidth(0, 70)
        self.tblInvoice.setColumnWidth(1, 150)
        self.tblInvoice.setColumnWidth(2, 100)
        self.tblInvoice.setColumnWidth(3, 100)
        total = 0
        for row, item in enumerate(result):
            self.tblInvoice.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tblInvoice.setItem(row, 1, QTableWidgetItem(str(item[1])))
            self.tblInvoice.setItem(row, 2, QTableWidgetItem(str(item[2])))
            self.tblInvoice.setItem(row, 3, QTableWidgetItem(str(item[3])))
            total += int(item[3])
        self.txtTotalRevenue.setText(str(total))

    # load Table Order search
    def loadTableOrderSearch(self, Data):
        self.tblInvoice.clearContents()
        self.tblInvoice.setColumnCount(4)
        self.tblInvoice.setRowCount(20)
        self.tblInvoice.setHorizontalHeaderLabels(['OrderID', 'CustomerName', 'CreateAt', 'Total'])
        self.tblInvoice.verticalHeader().setVisible(False)
        self.tblInvoice.resizeColumnsToContents()
        self.tblInvoice.setColumnWidth(0, 70)
        self.tblInvoice.setColumnWidth(1, 150)
        self.tblInvoice.setColumnWidth(2, 100)
        self.tblInvoice.setColumnWidth(3, 100)
        total = 0
        for row, item in enumerate(Data):
            self.tblInvoice.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tblInvoice.setItem(row, 1, QTableWidgetItem(str(item[1])))
            self.tblInvoice.setItem(row, 2, QTableWidgetItem(str(item[2])))
            self.tblInvoice.setItem(row, 3, QTableWidgetItem(str(item[3])))
            total += int(item[3])
        self.txtTotalRevenue.setText(str(total))

    # load table product mặc định
    def loadTableProductDefault(self):
        now = datetime.now() # Lấy thời điểm hiện tại
        firstDay = datetime.strptime((str(now.year)+"-"+str(now.month)+"-"+str(1)), "%Y-%m-%d").date() 
        result = OrderBLL.OrderBLL().statisticalProductByMonth(firstDay, now)
        self.tblProduct.clearContents()
        self.tblProduct.setColumnCount(5)
        self.tblProduct.setRowCount(20)
        self.tblProduct.setHorizontalHeaderLabels(['ProductID', 'ProductName', 'NumSold', 'Price', 'Total'])
        self.tblProduct.verticalHeader().setVisible(False)
        self.tblProduct.resizeColumnsToContents()
        self.tblProduct.setColumnWidth(0, 70)
        self.tblProduct.setColumnWidth(1, 130)
        self.tblProduct.setColumnWidth(2, 70)
        self.tblProduct.setColumnWidth(3, 100)
        self.tblProduct.setColumnWidth(4, 100)
        bestSold=0
        nameProductSold = None
        sumAmountSold = 0
        for row, item in enumerate(result):
            self.tblProduct.setItem(row, 0, QTableWidgetItem(str(item[2])))
            self.tblProduct.setItem(row, 1, QTableWidgetItem(str(item[1])))
            self.tblProduct.setItem(row, 2, QTableWidgetItem(str(item[0])))
            self.tblProduct.setItem(row, 3, QTableWidgetItem(str(item[3])))
            total = int(item[0]) * int(item[3])            
            self.tblProduct.setItem(row, 4, QTableWidgetItem(str(total)))
            sumAmountSold += int(item[0])
            if(int(item[0]) >= bestSold):
                bestSold = item[0]
                nameProductSold = item[1]
        self.txtTotalQuantitySold.setText(str(sumAmountSold))
        if(nameProductSold == None):
            self.txtBestSeller.setText("Không có")
        else:
            self.txtBestSeller.setText(nameProductSold)

    # load table product search
    def loadTableProductSearch(self,data):
        self.tblProduct.clearContents()
        self.tblProduct.setColumnCount(5)
        self.tblProduct.setRowCount(20)
        self.tblProduct.setHorizontalHeaderLabels(['ProductID', 'ProductName', 'NumSold', 'Price', 'Total'])
        self.tblProduct.verticalHeader().setVisible(False)
        self.tblProduct.resizeColumnsToContents()
        self.tblProduct.setColumnWidth(0, 70)
        self.tblProduct.setColumnWidth(1, 130)
        self.tblProduct.setColumnWidth(2, 70)
        self.tblProduct.setColumnWidth(3, 100)
        self.tblProduct.setColumnWidth(4, 100)
        bestSold=0
        nameProductSold = None
        sumAmountSold = 0
        for row, item in enumerate(data):
            self.tblProduct.setItem(row, 0, QTableWidgetItem(str(item[2])))
            self.tblProduct.setItem(row, 1, QTableWidgetItem(str(item[1])))
            self.tblProduct.setItem(row, 2, QTableWidgetItem(str(item[0])))
            self.tblProduct.setItem(row, 3, QTableWidgetItem(str(item[3])))
            total = int(item[0]) * int(item[3])            
            self.tblProduct.setItem(row, 4, QTableWidgetItem(str(total)))
            sumAmountSold += int(item[0])
            if(int(item[0]) >= bestSold):
                bestSold = item[0]
                nameProductSold = item[1]
        self.txtTotalQuantitySold.setText(str(sumAmountSold))
        if(nameProductSold == None):
            self.txtBestSeller.setText("Không có")
        else:
            self.txtBestSeller.setText(nameProductSold)

    # Xử lý thống kê doanh thu theo quý
    def handleQuarterlyRevenueStatistics(self):
        quarterly = self.cbxQuarterly.currentText()
        year = self.cbxYear.currentText()
        if(quarterly == "Quarterly 1"):
            result = OrderBLL.OrderBLL().statisticalOrderByQuarterlyOne(year)
            if(len(result) == 0):
                QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
            else:
                self.loadTableOrderSearch(result)
        elif(quarterly == "Quarterly 2"):
            result = OrderBLL.OrderBLL().statisticalOrderByQuarterlyTwo(year)
            if(len(result) == 0):
                QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
            else:
                self.loadTableOrderSearch(result)
        elif(quarterly == "Quarterly 3"):
            result = OrderBLL.OrderBLL().statisticalOrderByQuarterlyThree(year)
            if(len(result) == 0):
                QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
            else:
                self.loadTableOrderSearch(result)
        elif(quarterly == "Quarterly 4"):
            result = OrderBLL.OrderBLL().statisticalOrderByQuarterlyFour(year)
            if(len(result) == 0):
                QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
            else:
                self.loadTableOrderSearch(result)

    
    # Xử lý thống kê doanh thu theo tháng
    def handelMonthlyRevenueStatistics(self):
        selectedDateFrom = self.dateFromByRevenue.date()
        selectedDateTo = self.dateToByRevenue.date()
        dateFrom = datetime.strptime((str(selectedDateFrom.year())+"-"+str(selectedDateFrom.month())+"-"+str(selectedDateFrom.day())),"%Y-%m-%d").date()
        dateTo = datetime.strptime((str(selectedDateTo.year())+"-"+str(selectedDateTo.month())+"-"+str(selectedDateTo.day())),"%Y-%m-%d").date()
        if(dateFrom > dateTo):
            QMessageBox.information(self, "Thông báo!", "Vui lòng nhập thông tin hợp lệ. Ngày sau phải lớn hơn ngày trước!")
        else:
            result = OrderBLL.OrderBLL().statisticalOrderByMonth(dateFrom, dateTo)
            if(len(result) == 0):
                QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
            else:
                self.loadTableOrderSearch(result)

    # Xử lý reload table order
    def handleReloadTableOrder(self):
        self.loadTableOrderDefault()

    # Xứ lý reload table product
    def handleReloadTableProduct(self):
        self.loadTableProductDefault()


    # Xử lý thống kê sản phẩm theo danh mục sản phẩm
    def handleStatisticsByCategory(self):
        catId = self.cbxCategory.currentData().getCategoryID()
        result = OrderBLL.OrderBLL().statisticalProductByCategory(catId)
        if(len(result) == 0):
            QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
        else:
            self.loadTableProductSearch(result)

    # Xử lý thống kê sản phẩm theo ngày
    def handleMonthlyProductStatistics(self):
        selectedDateFrom = self.dateFromByProduct.date()
        selectedDateTo = self.dateToByProduct.date()
        dateFrom = datetime.strptime((str(selectedDateFrom.year())+"-"+str(selectedDateFrom.month())+"-"+str(selectedDateFrom.day())),"%Y-%m-%d").date()
        dateTo = datetime.strptime((str(selectedDateTo.year())+"-"+str(selectedDateTo.month())+"-"+str(selectedDateTo.day())),"%Y-%m-%d").date()
        if(dateFrom > dateTo):
            QMessageBox.information(self, "Thông báo!", "Vui lòng nhập thông tin hợp lệ. Ngày sau phải lớn hơn ngày trước!")
        else:
            result = OrderBLL.OrderBLL().statisticalProductByMonth(dateFrom, dateTo)
            if(len(result) == 0):
                QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
            else:
                self.loadTableProductSearch(result)

    

    
