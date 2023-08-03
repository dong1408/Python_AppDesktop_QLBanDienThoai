import ConnectDAL
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
import OrderDetail

class OrderDetailDAL:

    def getListOrderDetailByOrderID(self, id):
        sql = "SELECT * FROM orderdetail WHERE orderdetail.OrderID = %s "
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql,val)
        row = cursor.fetchone()
        listOrderDetail = []
        while row is not None:
            orderDetail = OrderDetail.OrderDetail(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
            listOrderDetail.append(orderDetail)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listOrderDetail

    def createOrderDetail(self, orderDetail):
        sql = "INSERT INTO `orderdetail` (`OrderDetailID`,`OrderID`,`ProductID`,`Amount`,`Price`,`SubTotal`) VALUES (NULL, %s, %s, %s, %s, %s)"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (orderDetail.getOrderID(), orderDetail.getProductID(), orderDetail.getAmount(), orderDetail.getPrice(), orderDetail.getSubTotal())
        cursor = conn.cursor()
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()
        conn.close()
