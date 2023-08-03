class Order:

    def __init__(self, OrderID = "", StaffID="", CustomerID="", CreatAt="", Amount="", Total=""):
        self.OrderID = OrderID
        self.StaffID = StaffID
        self.CustomerID = CustomerID
        self.CreatAt = CreatAt
        self.Amount = Amount
        self.Total = Total

    def getOrderID(self):
        return self.OrderID
    
    def setOrderID(self, orderId):
        self.OrderID = orderId

    def getStaffID(self):
        return self.StaffID
    
    def setStaffID(self, staffId):
        self.StaffID = staffId

    def getCustomerID(self):
        return self.CustomerID
    
    def setCustomerID(self, customerId):
        self.CustomerID = customerId

    def getCreateAt(self):
        return self.CreatAt
    
    def setCreateAt(self, createAt):
        self.CreatAt = createAt
    
    def getAmount(self):
        return self.Amount
    
    def setAmount(self, amount):
        self.Amount = amount

    def getTotal(self):
        return self.Total
    
    def setTotal(self, total):
        self.Total = total