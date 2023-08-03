class Supplier:

    def __init__(self, SupplierID="", SupplierName="", Email="", Address="", PhoneNumber=""):
        self.SupplierID = SupplierID
        self.SupplierName = SupplierName
        self.PhoneNumber = PhoneNumber
        self.Email = Email
        self.Address = Address

    def getSupplierID(self):
        return self.SupplierID

    def setSupplierID(self, supplierId):
        self.SupplierID = supplierId

    def getSupplierName(self):
        return self.SupplierName

    def setSupplierName(self, supplierName):
        self.SupplierName = supplierName

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
