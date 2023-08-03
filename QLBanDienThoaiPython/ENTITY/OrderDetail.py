class OrderDetail:

    def __init__(self, OrderDetailID="", OrderID="", ProductID="", Amount="", Price="", SubTotal=""):
        self.OrderDetailID = OrderDetailID
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.Amount = Amount
        self.Price = Price
        self.SubTotal = SubTotal

    def getOrderDetailID(self):
        return self.OrderDetailID

    def setOrderDetailID(self, orderDetailId):
        self.OrderDetailID = orderDetailId

    def getOrderID(self):
        return self.OrderID

    def setOrderID(self, orderId):
        self.OrderID = orderId

    def getProductID(self):
        return self.ProductID

    def setProductID(self, productId):
        self.ProductID = productId

    def getAmount(self):
        return self.Amount

    def setAmount(self, amount):
        self.Amount = amount

    def getPrice(self):
        return self.Price

    def setPrice(self, price):
        self.Price = price

    def getSubTotal(self):
        return self.SubTotal

    def setSubTotal(self, subTotal):
        self.SubTotal = subTotal
