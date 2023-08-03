import ConnectDAL
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
import Product

class ProductDAL:

    def getListProduct(self):
        sql = "SELECT * FROM product"
        conn = ConnectDAL.ConnectDAL().getConnect()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        listProduct = []
        while row is not None:
            product = Product.Product(row[1], row[2], row[3],
                            row[4], row[5], row[6])
            listProduct.append(product)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listProduct

    def getProductByID(self, id):
        sql = "SELECT * FROM product WHERE product.ProductID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        product = Product.Product(row[1], row[2], row[3],
                            row[4], row[5], row[6])
        cursor.close()
        conn.close()
        return product
    
    def getProductSearchByName(self, keySearch):
        sql = "SELECT * FROM product WHERE product.ProductName like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listProduct = []
        while row is not None:
            product = Product.Product(row[1], row[2], row[3],
                            row[4], row[5], row[6])
            listProduct.append(product)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listProduct

    def getProductSearchByCode(self, keySearch):
        sql = "SELECT * FROM product WHERE product.ProductID like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listProduct = []
        while row is not None:
            product = Product.Product(row[1], row[2], row[3],
                            row[4], row[5], row[6])
            listProduct.append(product)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listProduct
    
    def getProductSearchByPrice(self, priceFrom, priceTo):
        sql = "SELECT * FROM product WHERE product.Price >= %s AND product.Price <= %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (priceFrom, priceTo)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listProduct = []
        while row is not None:
            product = Product.Product(row[1], row[2], row[3],
                            row[4], row[5], row[6])
            listProduct.append(product)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listProduct
    
    def getProductSearchByCategory(self, keySearch):
        sql = "SELECT * FROM product, category WHERE product.CategoryID = category.CategoryID AND category.CategoryName like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listProduct = []
        while row is not None:
            product = Product.Product(row[1], row[2], row[3],
                            row[4], row[5], row[6])
            listProduct.append(product)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listProduct
    
    def getNameProductByID(self, id):
        sql = "SELECT pro.ProductName FROM product AS pro WHERE pro.ProductID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        namePro = row[0]
        cursor.close()
        conn.close()
        return namePro
    
    def getAmountProductByID(self, id):
        sql = "SELECT pro.Amount FROM product AS pro WHERE pro.ProductID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        amount = row[0]
        cursor.close()
        conn.close()
        return amount

    def insertProduct(self, product):
        sql = "INSERT INTO `product` (`ProductID`,`ProductName`,`Price`,`ImageUrl`,`CategoryID`) VALUES (%s, %s, %s, %s, %s)"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (product.getProductID(), product.getProductName(), product.getPrice(), product.getImageURL(), product.getCategoryID())
        cursor = conn.cursor()
        try:
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            conn.rollback()
            cursor.close()
            conn.close()
            return False
    
    def updateProduct(self, product):
        sql = "UPDATE `product` SET `ProductName` = %s, `Price` = %s, `ImageURL` = %s, `CategoryID` = %s WHERE `ProductID` = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (product.getProductName(), product.getPrice(), product.getImageURL(), product.getCategoryID(), product.getProductID())
        cursor = conn.cursor()
        try:
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            conn.rollback()
            cursor.close()
            conn.close()
            return False
        
    def updateAmountProduct(self, id, amount):
        sql = "UPDATE `product` SET `Amount` = %s WHERE `ProductID` = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (amount, id)
        cursor = conn.cursor()
        try:
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            conn.rollback()
            cursor.close()
            conn.close()
            return False

    def deleteProduct(self, id):
        sql = "DELETE FROM product WHERE product.ProductID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        try:
            cursor.execute(sql, val)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except:
            conn.rollback()
            cursor.close()
            conn.close()
            return False
        
    def checkDuplicateId(self, id):
        sql ="SELECT COUNT(*) FROM product WHERE ProductID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val=(id,)
        cursor = conn.cursor()
        try:
            cursor.execute(sql, val)
            row = cursor.fetchall()
            if(int(row[0][0])>0):
                conn.rollback()
                cursor.close()
                conn.close()
                return True
            else:
                conn.rollback()
                cursor.close()
                conn.close() 
                return False
        except:
            conn.rollback()
            cursor.close()
            conn.close()
            return False



# productDAO = ProductDAL()
# listProduct = productDAO.getListProduct()
# for item in listProduct:
#     item.toString()
