class Category():

    def __init__(self, CategoryID ="", CategoryName = ""):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
    
    def getCategoryID(self):
        return self.CategoryID
        
    def setCategoryID(self, categoryId):
        self.CategoryID = categoryId
    
    def getCategoryName(self):
        return self.CategoryName
    
    def setCategoryName(self, categoryName):
        self.CategoryName = categoryName

    # def __str__(self):
    #     return self.CategoryName