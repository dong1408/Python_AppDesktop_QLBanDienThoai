from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.uic import loadUi
import datetime

import DialogKhachHangGUI
UserRole = QtCore.Qt.ItemDataRole.UserRole
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import Product
import Staff
import Customer
import Category
import StaffBLL
import Order
import OrderDetail
import ProductBLL
import CustomerBLL
import CategoryBLL
import OrderBLL
import OrderDetailBLL

# Cua so test
class BanHangGUI(QMainWindow):
    listCart = []
    rowClickedTableCart = None
    TotalAmountProInCart = 0
    TotalPrice = 0
    def __init__(self, staff):
        self.staff = staff
        super(BanHangGUI,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/BanHang.ui',self)
        self.loadListProduct()
        self.loadCategoryToCbx()
        self.loadListCartDefault()
        self.txtUserName.setText(staff.getUserName())
        self.txtStaffID.setText(str(staff.getStaffID()))
        self.txtStaffName.setText(staff.getUserName())
        # Bắt sự kiện click 1 dòng trong table Product
        self.tblPro.cellClicked.connect(self.handleCellClicked)
        # Bắt sự kiện search product theo giá
        self.btnSearchByPrice.clicked.connect(self.handleSearchByPrice)
        # Bắt sự kiện search product theo filter code, name, cat
        self.btnSearchByFilter.clicked.connect(self.handleSearch)
        # Bắt sự kiện click button reload
        self.btnReload.clicked.connect(self.handleReload)
        # Bắt sự kiện click button AddCart
        self.btnAddCart.clicked.connect(self.handleAddCart)
        # Bắt sự kiện click button DeleteCart
        self.btnDeleteCart.clicked.connect(self.handleDeleteCart)
        # Bắt sự kiện click button Pay
        self.btnPay.clicked.connect(self.handlePay)

        # Bắt sự kiện show dialog khách hàng
        self.btnDialogCus.clicked.connect(self.handleShowDialogCustomer)


    # Load dữ liệu lên combobox Category
    def loadCategoryToCbx(self):
        listCat = CategoryBLL.CategoryBLL().getListCategory()
        model = QStandardItemModel()
        for category in listCat:
            item = QStandardItem(category.getCategoryName())
            item.setData(category, role = UserRole)  # Lưu trữ đối tượng Category
            model.appendRow(item)
        self.cbxCatPro.setModel(model)

    # Load dữ liệu lên table Product
    def loadListProduct(self):
        listProduct = ProductBLL.ProductBLL().getListProduct()
        self.tblPro.clearContents()
        self.tblPro.setColumnCount(5)
        self.tblPro.setRowCount(20)
        self.tblPro.setHorizontalHeaderLabels(
            ['ProductID', 'ProductName', 'Amount', 'Price', 'Category'])
        self.tblPro.verticalHeader().setVisible(False)
        self.tblPro.resizeColumnsToContents()
        self.tblPro.setColumnWidth(0, 80)
        self.tblPro.setColumnWidth(1, 150)
        self.tblPro.setColumnWidth(2, 50)
        self.tblPro.setColumnWidth(3, 100)
        self.tblPro.setColumnWidth(4, 100)
        for row, pro in enumerate(listProduct):
            self.tblPro.setItem(
                row, 0, QTableWidgetItem(str(pro.getProductID())))
            self.tblPro.setItem(row, 1, QTableWidgetItem(
                str(pro.getProductName())))
            self.tblPro.setItem(row, 2, QTableWidgetItem(str(pro.getAmount())))
            self.tblPro.setItem(row, 3, QTableWidgetItem(str(pro.getPrice())))
            self.tblPro.setItem(row, 4, QTableWidgetItem(str(CategoryBLL.CategoryBLL().getNameCategoryByID(pro.getCategoryID()))))


    # Load dữ liệu search
    def loadListProductSearch(self, listProductSearch):
        self.tblPro.clearContents()
        self.tblPro.setColumnCount(5)
        self.tblPro.setRowCount(20)
        self.tblPro.setHorizontalHeaderLabels(
            ['ProductID', 'ProductName', 'Amount', 'Price', 'Category'])
        self.tblPro.verticalHeader().setVisible(False)
        self.tblPro.resizeColumnsToContents()
        self.tblPro.setColumnWidth(0, 80)
        self.tblPro.setColumnWidth(1, 150)
        self.tblPro.setColumnWidth(2, 50)
        self.tblPro.setColumnWidth(3, 100)
        self.tblPro.setColumnWidth(4, 100)
        for row, pro in enumerate(listProductSearch):
            self.tblPro.setItem(
                row, 0, QTableWidgetItem(str(pro.getProductID())))
            self.tblPro.setItem(row, 1, QTableWidgetItem(
                str(pro.getProductName())))
            self.tblPro.setItem(row, 2, QTableWidgetItem(str(pro.getAmount())))
            self.tblPro.setItem(row, 3, QTableWidgetItem(str(pro.getPrice())))
            self.tblPro.setItem(
                row, 4, QTableWidgetItem(str(CategoryBLL.CategoryBLL().getNameCategoryByID(pro.getCategoryID()))))
            
    # Xử lý sử kiện click 1 dòng trong table Product
    def handleCellClicked(self, row, column):
        id = self.tblPro.item(row, 0).text()
        name = self.tblPro.item(row, 1).text()
        amount = self.tblPro.item(row, 2).text()
        price = self.tblPro.item(row, 3).text()
        categoryName = self.tblPro.item(row, 4).text()

        self.txtProID.setText(id)
        self.txtProName.setText(name)
        self.txtProAmountCurrent.setText(amount)
        self.txtProPrice.setText(price)
        self.spinProAmountPur.setValue(0)

        i=0
        while(True):
            cat = self.cbxCatPro.itemData(i,UserRole)
            if(cat.getCategoryName() == categoryName):
                self.cbxCatPro.setCurrentIndex(i)
                break
            i=i+1

    # Xử lý reset ô nhập liệu
    def handleReset(self):
        self.txtProID.setText("")
        self.txtProName.setText("")
        self.txtProAmountCurrent.setText("")
        self.txtProPrice.setText("")
        self.spinProAmountPur.setValue(0)


    # Reload table product
    def handleReload(self):
        self.loadListProduct()

    # Xử lý search sản phẩm theo giá
    def handleSearchByPrice(self):
        priceFrom = self.txtPriceFrom.text()
        priceTo = self.txtPriceTo.text()
        if(priceFrom =="" or priceTo==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng nhập đủ thông tin")
        elif(priceFrom>priceTo):
            QMessageBox.information(self, "Thông báo!", "Giá sau phải lớn hơn giá trước!")
        else:
            listProductSearch = ProductBLL.ProductBLL().getProductSearchByPrice(priceFrom, priceTo)
            if(len(listProductSearch) == 0):
                QMessageBox.information(self, "Thông báo!", "Không tìm thấy sản phẩm")
                self.loadListProductSearch(listProductSearch)
            else:
                self.loadListProductSearch(listProductSearch)

    # Tìm kiếm sản phẩm
    def handleSearch(self):
        if self.cbxFilter.currentText() == "Search By Code":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listProductSearch = ProductBLL.ProductBLL().getProductSearchByCode(keySearch)
                if(len(listProductSearch) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                else:
                    self.loadListProductSearch(listProductSearch)
        elif self.cbxFilter.currentText() == "Search By Name":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listProductSearch = ProductBLL.ProductBLL().getProductSearchByName(keySearch)
                if(len(listProductSearch) == 0):
                    self.loadListProductSearch(listProductSearch)
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                else:
                    self.loadListProductSearch(listProductSearch)
        elif self.cbxFilter.currentText() == "Search By Category":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listProductSearch = ProductBLL.ProductBLL().getProductSearchByCategory(keySearch)
                if(len(listProductSearch) == 0):
                    self.loadListProductSearch(listProductSearch)
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                else:
                    self.loadListProductSearch(listProductSearch)

    # load title cart
    def loadListCartDefault(self):
        self.tblCart.clearContents()
        self.tblCart.setColumnCount(6)
        self.tblCart.setRowCount(20)
        self.tblCart.setHorizontalHeaderLabels(
            ['STT', 'ProductID', 'ProductName', 'Amount', 'Price', 'SubTotal'])
        self.tblCart.verticalHeader().setVisible(False)
        self.tblCart.resizeColumnsToContents()
        self.tblCart.setColumnWidth(0, 30)
        self.tblCart.setColumnWidth(1, 90)
        self.tblCart.setColumnWidth(2, 140)
        self.tblCart.setColumnWidth(3, 50)
        self.tblCart.setColumnWidth(4, 100)
        self.tblCart.setColumnWidth(5, 100)

    # Load dữ liệu giỏ hàng
    def loadListCart(self,listOrderDetail):
        self.tblCart.clearContents()
        self.tblCart.setColumnCount(6)
        self.tblCart.setRowCount(20)
        self.tblCart.setHorizontalHeaderLabels(
            ['STT', 'ProductID', 'ProductName', 'Amount', 'Price', 'SubTotal'])
        self.tblCart.verticalHeader().setVisible(False)
        self.tblCart.resizeColumnsToContents()
        self.tblCart.setColumnWidth(0, 30)
        self.tblCart.setColumnWidth(1, 90)
        self.tblCart.setColumnWidth(2, 140)
        self.tblCart.setColumnWidth(3, 50)
        self.tblCart.setColumnWidth(4, 100)
        self.tblCart.setColumnWidth(5, 100)
        total = 0
        i=1
        for row, od in enumerate(listOrderDetail):
            self.tblCart.setItem(row, 0, QTableWidgetItem(str(i)))
            self.tblCart.setItem(row, 1, QTableWidgetItem(str(od.getProductID())))
            self.tblCart.setItem(row, 2, QTableWidgetItem(str(ProductBLL.ProductBLL().getNameProductByID(od.getProductID()))))
            self.tblCart.setItem(row, 3, QTableWidgetItem(str(od.getAmount())))
            self.tblCart.setItem(row, 4, QTableWidgetItem(str(od.getPrice())))
            self.tblCart.setItem(row, 5, QTableWidgetItem(str(od.getSubTotal())))
            total = float(total) + (float(od.getAmount()) * float(od.getPrice()))
            self.TotalAmountProInCart = self.TotalAmountProInCart + int(od.getAmount())
            self.TotalPrice = self.TotalPrice + float(od.getSubTotal())
            i=i+1
        self.txtTotal.setText(str(total))

    # Kiểm tra sản phẩm đã có trong giỏ hàng
    def checkItemExistCart(self, id):
        if(len(self.listCart) == 0):
            return False
        else:
            for item in self.listCart:
                if(item.getProductID() == id):
                    return True
            return False

    # Thêm sản phẩm vào giỏ hàng
    def handleAddCart(self):
        idPro = self.txtProID.text()
        namePro = self.txtProName.text()
        pricePro = self.txtProPrice.text()
        idCat = self.cbxCatPro.currentData().getCategoryID()
        quantityCurrent = self.txtProAmountCurrent.text()
        quantityPur = self.spinProAmountPur.value()
        if(idPro =="" or namePro == "" or pricePro == "" or idCat == "" or quantityCurrent=="" or quantityPur==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng chọn sản phẩm muốn mua")
        elif(quantityPur==0):
            QMessageBox.information(self, "Thông báo!", "Vui lòng nhập số lượng sản phẩm muốn mua")
        elif(float(quantityPur)>float(quantityCurrent)):
            QMessageBox.information(self, "Thông báo!", "Vượt quá số lượng sản phẩm có trong hệ thống")
        elif(self.checkItemExistCart(idPro) == True):
            for item in self.listCart:
                if(item.getProductID() == idPro):
                    amountPur = float(item.getAmount()) + float(quantityPur)
                    if(amountPur > float(ProductBLL.ProductBLL().getAmountProductByID(item.getProductID()))):
                        QMessageBox.information(self, "Thông báo!", "Vượt quá số lượng sản phẩm có trong hệ thống")
                        break
                    else:
                        item.setAmount(amountPur)
                        item.setSubTotal(amountPur * float(item.getPrice()))
                        break
            self.loadListCart(self.listCart)
        else:
            orderDetail = OrderDetail.OrderDetail()
            orderDetail.setProductID(idPro)
            orderDetail.setAmount(quantityPur)
            orderDetail.setPrice(pricePro)
            orderDetail.setSubTotal(float(orderDetail.getAmount()) * float(orderDetail.getPrice()))
            self.listCart.append(orderDetail)
            QMessageBox.information(self, "Thông báo!", "Thêm vào giỏ hàng thành công")
            self.loadListCart(self.listCart)
            self.handleReset()

    # Xóa sản phẩm khỏi giỏ hàng
    def handleDeleteCart(self):
        current_row = self.tblCart.currentRow()
        if current_row < 0:
            return
        else:
            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn xóa sản phẩm khỏi giỏ hàng?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()            
            if  buttonClicked == QMessageBox.StandardButton.Yes:
                self.listCart.pop( )
                self.loadListCart(self.listCart)

    
    # Show dialog khách hàng
    def handleShowDialogCustomer(self):
        dialogCus = DialogKhachHangGUI.DialogKhachHangGUI()
        result = dialogCus.exec()
        # if result == QDialog.Accepted:
        #     print("123")
        # if result == QDialog.rejected:
        #     print("456")
        if result == 1:
            customer = dialogCus.getCustomerClick()
            if(customer == None):
                pass
            else:
                self.txtCusID.setText(str(customer.getCustomerID()))
                self.txtCusName.setText(customer.getCustomerName())
        if result == 0:
            pass 

    # Xử lý thanh toán
    def handlePay(self):
        if(len(self.listCart) == 0):
            QMessageBox.information(self, "Thông báo!", "Hiện tại không có sản phẩm nào trong giỏ hàng!!")
        elif(self.txtCusID.text()=="" or self.txtCusName.text() == ""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin!!")
        else:
            staffID = self.staff.getStaffID()
            customerID = self.txtCusID.text()
            ceartAt = datetime.datetime.now()
            order = Order.Order()
            order.setStaffID(staffID)
            order.setCustomerID(customerID)
            order.setCreateAt(ceartAt)
            order.setAmount(self.TotalAmountProInCart)
            order.setTotal(self.TotalPrice)

            msgBox = QMessageBox()
            msgBox.setText("Xác nhận thanh toán?")
            msgBox.setWindowTitle("Thông báo")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
            if buttonClicked == QMessageBox.StandardButton.Yes:
                idOrder = OrderBLL.OrderBLL().createOrder(order)
                for item in self.listCart:
                    orderDetail = OrderDetail.OrderDetail()
                    orderDetail.setOrderID(idOrder)
                    orderDetail.setProductID(item.getProductID())
                    orderDetail.setAmount(item.getAmount())
                    orderDetail.setPrice(item.getPrice())
                    orderDetail.setSubTotal(item.getSubTotal())
                    product = ProductBLL.ProductBLL().getProductById(item.getProductID())
                    amountRemaining = int(product.getAmount()) - int(item.getAmount())
                    ProductBLL.ProductBLL().updateAmountProduct(item.getProductID(), amountRemaining)
                    OrderDetailBLL.OrderDetailBLL().createOrderDetail(orderDetail)
                QMessageBox.information(self, "Thông báo!", "Thanh toán thành công!!")
                self.loadListProduct()
                self.handleReset()
                self.listCart.clear()
                self.loadListCartDefault()
                self.txtTotal.setText("")
                self.txtCusID.setText("")
                self.txtCusName.setText("")




    
       