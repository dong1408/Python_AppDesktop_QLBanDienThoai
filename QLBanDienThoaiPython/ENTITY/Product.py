class Product:

    def __init__(self, ProductID="", ProductName="", Amount="", Price="", ImageURL="", CategoryID=""):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.Amount = Amount
        self.Price = Price
        self.ImageURL = ImageURL
        self.CategoryID = CategoryID

    def getProductID(self):
        return self.ProductID

    def setProductID(self, productId):
        self.ProductID = productId

    def getProductName(self):
        return self.ProductName

    def setProductName(self, productName):
        self.ProductName = productName

    def getAmount(self):
        return self.Amount

    def setAmount(self, amount):
        self.Amount = amount

    def getPrice(self):
        return self.Price

    def setPrice(self, price):
        self.Price = price

    def getImageURL(self):
        return self.ImageURL

    def setImageURL(self, imageUrl):
        self.ImageURL = imageUrl

    def getCategoryID(self):
        return self.CategoryID

    def setCategoryID(self, categoryId):
        self.CategoryID = categoryId

    def toString(self):
        print(f"ID: {self.ProductID} ProductName: {self.ProductName} Amount: {self.Amount} Price: {self.Price} ImageUrl: {self.ImageURL} CategoryID: {self.CategoryID}")
