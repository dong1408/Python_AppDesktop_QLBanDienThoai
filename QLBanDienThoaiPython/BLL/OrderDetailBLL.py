import sys
sys.path.append('./QLBanDienThoaiPython/DAL')
import OrderDetailDAL

class OrderDetailBLL:

    def getListOrderDetailByOrderID(self, id):
        return OrderDetailDAL.OrderDetailDAL().getListOrderDetailByOrderID(id)

    def createOrderDetail(self, orderDetail):
        OrderDetailDAL.OrderDetailDAL().createOrderDetail(orderDetail)