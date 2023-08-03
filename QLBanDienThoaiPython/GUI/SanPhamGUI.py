from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
UserRole = QtCore.Qt.ItemDataRole.UserRole
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import CategoryBLL
import ProductBLL
import CategoryItem
import Category
import Product


class SanPhamGUI(QMainWindow):

    def __init__(self,staff):
        self.staff = staff
        super(SanPhamGUI, self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/SanPham.ui', self)
        self.txtUserName.setText(staff.getUserName())
        self.loadCategoryToCbx()
        self.loadListProduct()
        # Bắt sự kiện click button search
        self.btnSearch.clicked.connect(self.handleSearch)
        # Bắt sự kiện click 1 dòng trong table
        self.tblPro.cellClicked.connect(self.handleCellClicked)
        # Bắt sự kiện click button add
        self.btnAdd.clicked.connect(self.handleAddProduct)
        # Bắt sự kiện click button update
        self.btnEdit.clicked.connect(self.handleUpdateProduct)
        # Bắt sự kiện click button delete
        self.btnDelete.clicked.connect(self.handleDeleteProduct)
        # Bắt sự kiện click button reset
        self.btnReset.clicked.connect(self.handleResetProduct)
        # Bắt sự kiện click button reload
        self.btnReload.clicked.connect(self.handleReload)

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
        self.tblPro.setColumnWidth(0, 100)
        self.tblPro.setColumnWidth(1, 300)
        self.tblPro.setColumnWidth(2, 130)
        self.tblPro.setColumnWidth(3, 180)
        self.tblPro.setColumnWidth(4, 207)
        for row, pro in enumerate(listProduct):
            self.tblPro.setItem(
                row, 0, QTableWidgetItem(str(pro.getProductID())))
            self.tblPro.setItem(row, 1, QTableWidgetItem(
                str(pro.getProductName())))
            self.tblPro.setItem(row, 2, QTableWidgetItem(str(pro.getAmount())))
            self.tblPro.setItem(row, 3, QTableWidgetItem(str(pro.getPrice())))
            self.tblPro.setItem(
                row, 4, QTableWidgetItem(str(CategoryBLL.CategoryBLL().getNameCategoryByID(pro.getCategoryID()))))

            
    # Load dữ liệu search
    def loadListProductSearch(self, listProductSearch):
        self.tblPro.clearContents()
        self.tblPro.setColumnCount(5)
        self.tblPro.setRowCount(20)
        self.tblPro.setHorizontalHeaderLabels(
            ['ProductID', 'ProductName', 'Amount', 'Price', 'Category'])
        self.tblPro.verticalHeader().setVisible(False)
        self.tblPro.resizeColumnsToContents()
        self.tblPro.setColumnWidth(0, 100)
        self.tblPro.setColumnWidth(1, 300)
        self.tblPro.setColumnWidth(2, 130)
        self.tblPro.setColumnWidth(3, 180)
        self.tblPro.setColumnWidth(4, 207)
        for row, pro in enumerate(listProductSearch):
            self.tblPro.setItem(
                row, 0, QTableWidgetItem(str(pro.getProductID())))
            self.tblPro.setItem(row, 1, QTableWidgetItem(
                str(pro.getProductName())))
            self.tblPro.setItem(row, 2, QTableWidgetItem(str(pro.getAmount())))
            self.tblPro.setItem(row, 3, QTableWidgetItem(str(pro.getPrice())))
            self.tblPro.setItem(
                row, 4, QTableWidgetItem(str(CategoryBLL.CategoryBLL().getNameCategoryByID(pro.getCategoryID()))))


    # Xử lý sử kiện click 1 dòng trong table
    def handleCellClicked(self, row, column):
        id = self.tblPro.item(row, 0).text()
        name = self.tblPro.item(row, 1).text()
        amount = self.tblPro.item(row, 2).text()
        price = self.tblPro.item(row, 3).text()
        categoryName = self.tblPro.item(row, 4).text()

        self.txtProID.setReadOnly(True)
        self.txtProID.setText(id)
        self.txtProName.setText(name)
        self.txtProAmount.setText(amount)
        self.txtProPrice.setText(price)

        i=0
        while(True):
            cat = self.cbxCatPro.itemData(i,UserRole)
            if(cat.getCategoryName() == categoryName):
                self.cbxCatPro.setCurrentIndex(i)
                break
            i=i+1

    # Xử lý thêm mới sản phẩm
    def handleAddProduct(self):
        id = self.txtProID.text()
        name = self.txtProName.text()
        price = self.txtProPrice.text()
        catId = self.cbxCatPro.currentData().getCategoryID()
        if(ProductBLL.ProductBLL().checkDuplicateId(id) == True):
            QMessageBox.information(self, "Thông báo!", "Mã sản phẩm đã tồn tại")
        else:
            if (id == "" or name=="" or price==""):
                QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin sản phẩm")
            else:
                product =Product.Product()
                product.setProductID(id)
                product.setProductName(name)
                product.setPrice(price) 
                product.setCategoryID(catId)

                msgBox = QMessageBox()
                msgBox.setText("Bạn có muốn thêm mới sản phẩm?")
                msgBox.setWindowTitle("Xác nhận")
                msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                buttonClicked = msgBox.exec()
                # ProductBLL.ProductBLL().insertProduct(product)
                if buttonClicked == QMessageBox.StandardButton.Yes:
                    if(ProductBLL.ProductBLL().insertProduct(product) == True):
                        QMessageBox.information(self, "Thông báo!", "Thêm mới sản phẩm thành công")
                        self.loadListProduct()
                    else:
                        QMessageBox.information(self, "Thông báo!", "Thêm thất bại")

        

    # Xử lý cập nhật sản phẩm
    def handleUpdateProduct(self):
        id = self.txtProID.text()
        name = self.txtProName.text()
        price = self.txtProPrice.text()
        catId = self.cbxCatPro.currentData().getCategoryID()
        if (id == "" or name=="" or price==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin sản phẩm")
        else:
            product =Product.Product()
            product.setProductID(id)
            product.setProductName(name)
            product.setPrice(price) 
            product.setCategoryID(catId)

            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn cập nhật lại sản phẩm?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
                # ProductBLL.ProductBLL().insertProduct(product)                
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(ProductBLL.ProductBLL().updateProduct(product) == True):
                    QMessageBox.information(self, "Thông báo!", "Cập nhật sản phẩm thành công")
                    self.loadListProduct()
                else:
                    QMessageBox.information(self, "Thông báo!", "Cập nhật thất bại")



    # Xử lý xóa sản phẩm
    def handleDeleteProduct(self):
        id = self.txtProID.text()
        if (id == "" or self.txtProName.text() =="" or self.txtProPrice.text()==""):
            pass
        else:
            msgBox = QMessageBox()
            msgBox.setText("Bạn có chắc muốn xóa hay không?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()            
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(ProductBLL.ProductBLL().deleteProduct(id) == True):
                    QMessageBox.information(self, "Thông báo!", "Xóa sản phẩm thành công")
                    self.loadListProduct()                    
                else:
                    QMessageBox.information(self, "Thông báo!", "Xóa thất bại")



    # Xử lý reset ô nhập liệu
    def handleResetProduct(self):
        self.txtProID.setReadOnly(False)
        self.txtProID.setText("")
        self.txtProName.setText("")
        self.txtProPrice.setText("")
        self.txtProAmount.setText("")


    def handleReload(self):
        self.loadListProduct()

    # Xử lý sự kiện tìm kiếm sản phẩm
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
