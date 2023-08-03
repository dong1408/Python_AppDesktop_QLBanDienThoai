class Customer:

    def __init__(self, CustomerID="", CustomerName="", PhoneNumber="", Email="", Address=""):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Address = Address

    def getCustomerID(self):
        return self.CustomerID
    
    def setCustomerID(self, customerId):    
        self.CustomerID = customerId

    def getCustomerName(self):
        return self.CustomerName
    
    def setCustomerName(self, customerName):
        self.CustomerName = customerName
    
    def getPhoneNumber(self):
        return self.PhoneNumber
    
    def setPhoneNumber(self, phoneNumber):
        self.PhoneNumber = phoneNumber

    def getEmail(self):
        return self.Email

    def setEmail(self, email):
        self.Email = email

    def getAddress(self):
        return self.Address
    
    def setAddress(self, address):
        self.Address = address
