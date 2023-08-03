import sys
sys.path.append('./QLBanDienThoaiPython/DAL')
import OrderDAL

class OrderBLL:

    def getListOrder(self):
        return OrderDAL.OrderDAL().getListOrder() 
    
    def getOrderByID(self, id):
        return OrderDAL.OrderDAL().getOrderByID(id)
    
    def getOrderByCustomerName(self, cusName):
        return OrderDAL.OrderDAL().getOrderByCustomerName(cusName)
    
    def getOrderByPrice(self, priceFrom, priceTo):
        return OrderDAL.OrderDAL().getOrderByPrice(priceFrom, priceTo)
    
    def getOrderByDate(self, dateFrom, dateTo):
        return OrderDAL.OrderDAL().getOrderByDate(dateFrom, dateTo)

    def createOrder(self, order):
        return OrderDAL.OrderDAL().createOrder(order)
    
    def statisticalOrderByQuarterlyOne(self, year):
        return OrderDAL.OrderDAL().statisticalOrderByQuarterlyOne(year)
    
    def statisticalOrderByQuarterlyTwo(self, year):
        return OrderDAL.OrderDAL().statisticalOrderByQuarterlyTwo(year)
    
    def statisticalOrderByQuarterlyThree(self, year):
        return OrderDAL.OrderDAL().statisticalOrderByQuarterlyThree(year)
    
    def statisticalOrderByQuarterlyFour(self, year):
        return OrderDAL.OrderDAL().statisticalOrderByQuarterlyFour(year)
    
    def statisticalOrderByMonth(self, dateFrom, dateTo):
        return OrderDAL.OrderDAL().statisticalOrderByMonth(dateFrom, dateTo) 
    
    def statisticalProductByCategory(self, idCat):
        return OrderDAL.OrderDAL().statisticalProductByCategory(idCat)
    
    def statisticalProductByMonth(self, dateFrom, dateTo):
        return OrderDAL.OrderDAL().statisticalProductByMonth(dateFrom, dateTo)