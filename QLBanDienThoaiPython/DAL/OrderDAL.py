import ConnectDAL
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
import Order

class OrderDAL:

    def getListOrder(self):
        sql = "SELECT * FROM orders"
        conn = ConnectDAL.ConnectDAL().getConnect()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        listOrder = []
        while row is not None:
            order = Order.Order(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
            listOrder.append(order)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listOrder
    
    def getOrderByID(self, id):
        sql = "SELECT * FROM orders WHERE orders.OrderID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listOrder = []
        while row is not None:
            order = Order.Order(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
            listOrder.append(order)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listOrder
    
    def getOrderByCustomerName(self, cusName):
        sql = "SELECT * FROM orders, customer WHERE orders.CustomerID = customer.CustomerID AND customer.CustomerName like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(cusName)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listOrder = []
        while row is not None:
            order = Order.Order(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
            listOrder.append(order)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listOrder
    
    def getOrderByPrice(self, priceFrom, priceTo):
        sql = "SELECT * FROM orders WHERE orders.Total >= %s  AND orders.Total <=  %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (priceFrom, priceTo)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listOrder = []
        while row is not None:
            order = Order.Order(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
            listOrder.append(order)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listOrder
    
    def getOrderByDate(self, dateFrom, dateTo):
        sql = "SELECT * FROM orders WHERE orders.CreateAt >= %s  AND orders.CreateAt <=  %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (dateFrom, dateTo)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listOrder = []
        while row is not None:
            order = Order.Order(row[0], row[1], row[2],
                                         row[3], row[4], row[5])
            listOrder.append(order)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listOrder

    # def getSupplierByID(self, id):
    #     sql = "SELECT * FROM supplier WHERE supplier.SupplierID = %s"
    #     conn = ConnectDAL.ConnectDAL().getConnect()
    #     val = (id,)
    #     cursor = conn.cursor()
    #     cursor.execute(sql, val)
    #     row = cursor.fetchone()
    #     if row is None:
    #         return None
    #     supplier = Supplier.Supplier(row[0], row[1], row[2],
    #                               row[3], row[4])
    #     cursor.close()
    #     conn.close()
    #     return supplier

    def createOrder(self, order):
        sql = "INSERT INTO `orders` (`OrderID`,`StaffID`,`CustomerID`,`CreateAt`,`Amount`, `Total`) VALUES (NULL, %s, %s, %s, %s, %s)"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (order.getStaffID(), order.getCustomerID(), order.getCreateAt(), order.getAmount(), order.getTotal())
        cursor = conn.cursor()
        cursor.execute(sql, val)
        conn.commit()
        idOrder = cursor.lastrowid  # Lấy idOrder vừa tạo
        cursor.close()
        conn.close()
        return idOrder
    
    def statisticalOrderByQuarterlyOne(self, year):
        sql = "SELECT o.OrderID, cus.CustomerName, o.CreateAt, o.Total FROM orders AS o, customer AS cus WHERE o.CustomerID = cus.CustomerID AND o.CreateAt >= %s AND o.CreateAt <= %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (str(year)+"-01-01", str(year)+"-03-31")
        cursor = conn.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def statisticalOrderByQuarterlyTwo(self, year):
        sql = "SELECT o.OrderID, cus.CustomerName, o.CreateAt, o.Total FROM orders AS o, customer AS cus WHERE o.CustomerID = cus.CustomerID AND o.CreateAt >= %s AND o.CreateAt <= %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (str(year)+"-01-04", str(year)+"-06-30")
        cursor = conn.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def statisticalOrderByQuarterlyThree(self, year):
        sql = "SELECT o.OrderID, cus.CustomerName, o.CreateAt, o.Total FROM orders AS o, customer AS cus WHERE o.CustomerID = cus.CustomerID AND o.CreateAt >= %s AND o.CreateAt <= %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (str(year)+"-07-01", str(year)+"-09-30")
        cursor = conn.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def statisticalOrderByQuarterlyFour(self, year):
        sql = "SELECT o.OrderID, cus.CustomerName, o.CreateAt, o.Total FROM orders AS o, customer AS cus WHERE o.CustomerID = cus.CustomerID AND o.CreateAt >= %s AND o.CreateAt <= %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (str(year)+"-10-01", str(year)+"-12-31")
        cursor = conn.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result 
    
    def statisticalOrderByMonth(self, dateFrom, dateTo):
        sql = "SELECT o.OrderID, cus.CustomerName, o.CreateAt, o.Total FROM orders AS o, customer AS cus WHERE o.CustomerID = cus.CustomerID AND o.CreateAt >= %s AND o.CreateAt <= %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (dateFrom, dateTo)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result       

    def statisticalProductByCategory(self, idCat):
        sql = "SELECT SUM(od.Amount) AS sumAmount, pro.ProductName, pro.ProductID, pro.Price FROM orderdetail AS od, product AS pro WHERE od.ProductID = pro.ProductID AND pro.CategoryID = %s GROUP BY od.ProductID"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (idCat,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result   
    
    def statisticalProductByMonth(self, dateFrom, dateTo):
        sql = "SELECT SUM(od.Amount) AS sumAmount, pro.ProductName, pro.ProductID, pro.Price FROM orderdetail AS od, product AS pro, orders AS o WHERE o.OrderID = od.OrderID AND o.CreateAt >= %s AND o.CreateAt <= %s AND od.ProductID = pro.ProductID GROUP BY od.ProductID"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (dateFrom, dateTo)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result        
