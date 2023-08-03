from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
sys.path.append('./QLBanDienThoaiPython/BLL')
import Category
import CategoryBLL

# Cua so test
class DanhMucGUI(QMainWindow):
    def __init__(self, staff):
        self.staff = staff
        super(DanhMucGUI,self).__init__()
        uic.loadUi('./QLBanDienThoaiPython/GUI/DanhMucSanPham.ui',self)
        self.loadListCategory()
        self.txtUserName.setText(staff.getUserName())
        # Bắt sự kiện click button search
        self.btnSearch.clicked.connect(self.handleSearch)
        # Bắt sự kiện click 1 dòng trong table
        self.tblCategory.cellClicked.connect(self.handleCellClicked)
        # Bắt sự kiện click button add
        self.btnAdd.clicked.connect(self.handleAddCategory)
        # Bắt sự kiện click button update
        self.btnEdit.clicked.connect(self.handleUpdateCategory)
        # Bắt sự kiện click button delete
        self.btnDelete.clicked.connect(self.handleDeleteCategory)
        # Bắt sự kiện click button reset
        self.btnReset.clicked.connect(self.handleResetCategory)
        # Bắt sự kiện click button reload
        self.btnReload.clicked.connect(self.handleReload)

    
    # Load dữ liệu lên table Category
    def loadListCategory(self):
        listCategory = CategoryBLL.CategoryBLL().getListCategory()
        self.tblCategory.clearContents()
        self.tblCategory.setColumnCount(2)
        self.tblCategory.setRowCount(10)
        self.tblCategory.setHorizontalHeaderLabels(['CategoryID', 'CategoryName'])
        self.tblCategory.verticalHeader().setVisible(False)
        self.tblCategory.resizeColumnsToContents()
        self.tblCategory.setColumnWidth(0, 170)
        self.tblCategory.setColumnWidth(1, 460)
        for row, cat in enumerate(listCategory):
            self.tblCategory.setItem(row, 0, QTableWidgetItem(str(cat.getCategoryID())))
            self.tblCategory.setItem(row, 1, QTableWidgetItem(str(cat.getCategoryName())))
        
    # Load dữ liệu search
    def loadListCategorySearch(self, listCategorySearch):
        self.tblCategory.clearContents()
        self.tblCategory.setColumnCount(2)
        self.tblCategory.setRowCount(10)
        self.tblCategory.setHorizontalHeaderLabels(['CategoryID', 'CategoryName'])
        self.tblCategory.verticalHeader().setVisible(False)
        self.tblCategory.resizeColumnsToContents()
        self.tblCategory.setColumnWidth(0, 170)
        self.tblCategory.setColumnWidth(1, 460)
        for row, cat in enumerate(listCategorySearch):
            self.tblCategory.setItem(row, 0, QTableWidgetItem(str(cat.getCategoryID())))
            self.tblCategory.setItem(row, 1, QTableWidgetItem(str(cat.getCategoryName())))


    # Xử lý sử kiện click 1 dòng trong table
    def handleCellClicked(self, row, column):
        id = self.tblCategory.item(row, 0).text()
        name = self.tblCategory.item(row, 1).text()
        self.txtID.setText(id)
        self.txtName.setText(name)
   

    # Xử lý thêm mới danh mục
    def handleAddCategory(self):
        name = self.txtName.text()
        if (name==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin")
        else:
            cat =Category.Category()
            cat.setCategoryName(name)
            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn thêm mới danh mục?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(CategoryBLL.CategoryBLL().insertCategory(cat) == True):
                    QMessageBox.information(self, "Thông báo!", "Thêm thành công")
                    self.loadListCategory()
                else:
                    QMessageBox.information(self, "Thông báo!", "Thêm thất bại")

        

    # Xử lý cập nhật danh mục
    def handleUpdateCategory(self):
        id = self.txtID.text()
        name = self.txtName.text()
        if (name=="" or id ==""):
            QMessageBox.information(self, "Thông báo!", "Vui lòng điền đầy đủ thông tin")
        else:
            cat =Category.Category()
            cat.setCategoryID(id)
            cat.setCategoryName(name)
            msgBox = QMessageBox()
            msgBox.setText("Bạn có muốn cập nhật danh mục?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(CategoryBLL.CategoryBLL().updateCategory(cat) == True):
                    QMessageBox.information(self, "Thông báo!", "Cập nhật thành công")
                    self.loadListCategory()
                else:
                    QMessageBox.information(self, "Thông báo!", "Cập nhật thất bại")



    # Xử lý xóa danh mục
    def handleDeleteCategory(self):
        id = self.txtID.text()
        name = self.txtName.text()
        if (name=="" or id ==""):
            pass
        else:
            msgBox = QMessageBox()
            msgBox.setText("Bạn có chắc muốn xóa hay không?")
            msgBox.setWindowTitle("Xác nhận")
            msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            buttonClicked = msgBox.exec()            
            if buttonClicked == QMessageBox.StandardButton.Yes:
                if(CategoryBLL.CategoryBLL().deleteCategory(id) == True):
                    QMessageBox.information(self, "Thông báo!", "Xóa danh mục thành công")
                    self.loadListCategory()
                    self.handleResetCategory()                   
                else:
                    QMessageBox.information(self, "Thông báo!", "Xóa thất bại")



    # Xử lý reset ô nhập liệu
    def handleResetCategory(self):
        self.txtID.setText("")
        self.txtName.setText("")

    # Xử lý reload dữ liệu table
    def handleReload(self):
        self.loadListCategory()

    # Xử lý sự kiện tìm kiếm danh mục
    def handleSearch(self):
        if self.cbxFilter.currentText() == "Search By Code":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listCategorySearch = CategoryBLL.CategoryBLL().getCategorySearchByCode(keySearch)
                if(len(listCategorySearch) == 0):
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListCategorySearch(listCategorySearch)
                else:
                    self.loadListCategorySearch(listCategorySearch)
        elif self.cbxFilter.currentText() == "Search By Name":
            keySearch = self.txtSearch.text()
            if(keySearch==""):
                pass
            else:
                listCategorySearch = CategoryBLL.CategoryBLL().getCategorySearchByName(keySearch)
                if(len(listCategorySearch) == 0):                    
                    QMessageBox.information(self, "Thông báo!", "Không có dữ liệu")
                    self.loadListCategorySearch(listCategorySearch)
                else:
                    self.loadListCategorySearch(listCategorySearch)