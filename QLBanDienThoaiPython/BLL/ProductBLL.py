import sys
sys.path.append('./QLBanDienThoaiPython/DAL')
import ProductDAL

class ProductBLL:

    def getListProduct(self):
        return ProductDAL.ProductDAL().getListProduct()
    
    def getProductById(self, id):
        return ProductDAL.ProductDAL().getProductByID(id)
    
    def insertProduct(self, pro):
        return ProductDAL.ProductDAL().insertProduct(pro)

    def updateProduct(self, pro):
        return ProductDAL.ProductDAL().updateProduct(pro)

    def deleteProduct(self, id):
        return ProductDAL.ProductDAL().deleteProduct(id)
    
    def checkDuplicateId(self, id):
        return ProductDAL.ProductDAL().checkDuplicateId(id)
    
    def getProductSearchByName(self, keySearch):
        return ProductDAL.ProductDAL().getProductSearchByName(keySearch)

    def getProductSearchByCode(self, keySearch):
        return ProductDAL.ProductDAL().getProductSearchByCode(keySearch) 
    
    def getProductSearchByPrice(self, priceFrom, priceTo):
        return ProductDAL.ProductDAL().getProductSearchByPrice(priceFrom, priceTo)
    
    def getProductSearchByCategory(self, keySearch):
        return ProductDAL.ProductDAL().getProductSearchByCategory(keySearch)
    
    def getNameProductByID(self, id):
        return ProductDAL.ProductDAL().getNameProductByID(id)
    
    def getAmountProductByID(self, id):
        return ProductDAL.ProductDAL().getAmountProductByID(id)
    
    def updateAmountProduct(self, id, amount):
        return ProductDAL.ProductDAL().updateAmountProduct(id, amount)
        
