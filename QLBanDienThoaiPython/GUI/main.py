from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import sys
import test123
import NhanVienGUI
import SanPhamGUI
import DanhMucSanPhamGUI
import BanHangGUI
import HoaDonGUI
import KhachHangGUI
import ThongKeBaoCaoGUI
import NhapHangGUI


class MainWindow(QMainWindow):

    def __init__(self,staff):
        self.staff = staff
        super().__init__()

        # Tạo một QStackedWidget để chứa các widget con
        self.stacked_main_widget = QStackedWidget()
        # self.stacked_main_widget.setStyleSheet("border: 1px solid black")

        # Tạo các widget con
        # self.widget1 = QWidget()
        # self.widget1.setStyleSheet("background-color: green")
        # self.label1 = QLabel('This is widget 1')
        # layout1 = QVBoxLayout()
        # layout1.addWidget(self.label1)
        # self.widget1.setLayout(layout1)

        self.widget2 = QWidget()
        self.widget2.setStyleSheet("background-color: red")
        self.label2 = QLabel('This is widget 2')
        layout2 = QVBoxLayout(self.widget2)
        layout2.addWidget(self.label2)

        # self.widget3 = test123.test_w() 
        self.NhanVienF = NhanVienGUI.NhanVienGUI(staff)
        self.SanPhamF = SanPhamGUI.SanPhamGUI(staff)
        self.DanhMucF = DanhMucSanPhamGUI.DanhMucGUI(staff)
        self.BanHangF = BanHangGUI.BanHangGUI(staff)
        self.HoaDonF = HoaDonGUI.HoaDonGUI(staff)
        self.KhachHangF = KhachHangGUI.KhachHangGUI(staff)
        self.ThongKeBaoCaoF = ThongKeBaoCaoGUI.ThongKeBaoCaoGUI(staff)
        self.NhapHangF = NhapHangGUI.NhapHangGUI(staff)

        # Thêm các widget con vào QStackedWidget
        # self.stacked_main_widget.addWidget(self.widget1)
        # self.stacked_main_widget.addWidget(self.widget2)
        # self.stacked_main_widget.addWidget(self.widget3)
        self.stacked_main_widget.addWidget(self.NhanVienF)
        self.stacked_main_widget.addWidget(self.SanPhamF)
        self.stacked_main_widget.addWidget(self.DanhMucF)
        self.stacked_main_widget.addWidget(self.BanHangF)
        self.stacked_main_widget.addWidget(self.HoaDonF)
        self.stacked_main_widget.addWidget(self.KhachHangF)
        self.stacked_main_widget.addWidget(self.ThongKeBaoCaoF)
        self.stacked_main_widget.addWidget(self.NhapHangF)

        # Đặt QStackedWidget làm nội dung chính của cửa sổ chính
        self.setCentralWidget(self.stacked_main_widget)

        # Tạo các nút để chuyển đổi giữa các widget con
        self.button1 = QPushButton('Bán Hàng', self)
        self.button1.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.BanHangF))
        self.button1.setFixedHeight(35)

        self.button2 = QPushButton('Khách Hàng', self)
        self.button2.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.KhachHangF))
        self.button2.setFixedHeight(35)

        self.button3 = QPushButton('Nhân Viên', self)
        self.button3.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.NhanVienF))
        self.button3.setFixedHeight(35)
        
        self.button4 = QPushButton('Sản Phẩm', self)
        self.button4.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.SanPhamF))
        self.button4.setFixedHeight(35)

        self.button5 = QPushButton('Danh Mục Sản Phẩm', self)
        self.button5.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.DanhMucF))
        self.button5.setFixedHeight(35)

        self.button6 = QPushButton('Hóa Đơn', self)
        self.button6.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.HoaDonF))
        self.button6.setFixedHeight(35)

        self.button7 = QPushButton('Nhập Hàng', self)
        self.button7.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.NhapHangF))
        self.button7.setFixedHeight(35)

        self.button8 = QPushButton('Thống Kê', self)
        self.button8.clicked.connect(lambda: self.stacked_main_widget.setCurrentWidget(self.ThongKeBaoCaoF))
        self.button8.setFixedHeight(35)

        # Tạo ảnh main project
        self.imageMain = QLabel()
        self.imageMain.setFixedHeight(150)
        self.imageMain.setFixedWidth(133)

        # Tạo layout để chứa các nút
        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.imageMain)
        menu_layout.addWidget(self.button1)
        menu_layout.addWidget(self.button2)
        menu_layout.addWidget(self.button3)
        menu_layout.addWidget(self.button4)
        menu_layout.addWidget(self.button5)
        menu_layout.addWidget(self.button6)
        menu_layout.addWidget(self.button7) 
        menu_layout.addWidget(self.button8)
        menu_layout.setContentsMargins(10,0,10,0)
        menu_layout.setSpacing(5)

        # Tạo widget để chứa menu_layout
        self.menu_widget = QWidget()

        self.menu_widget.setLayout(menu_layout)
        self.menu_widget.setStyleSheet("border: 1px solid black")
        self.menu_widget.setFixedWidth(150)

        # Thêm widget chứa các nút vào cửa sổ chính
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.menu_widget)
        main_layout.addWidget(self.stacked_main_widget)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        # main_widget.setFixedHeight(600)
        # main_widget.setFixedWidth(1250)
        self.setGeometry(150,50,1250,730)   

        self.setCentralWidget(main_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
