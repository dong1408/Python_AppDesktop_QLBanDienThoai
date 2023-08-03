import ConnectDAL
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
import Category

class CategoryDAL:

    def getListCategory(self):
        sql = "SELECT * FROM category"
        conn = ConnectDAL.ConnectDAL().getConnect()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        listCategory = []
        while row is not None:
            category = Category.Category(row[0], row[1])
            listCategory.append(category)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listCategory

    def getCategoryByID(self, id):
        sql = "SELECT * FROM category WHERE category.CategoryID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        category = Category.Category(row[0], row[1])
        cursor.close()
        conn.close()
        return category
    
    def getNameCategoryByID(self, id):
        sql = "SELECT cat.CategoryName FROM category AS cat WHERE cat.CategoryID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        nameCat = row[0]
        cursor.close()
        conn.close()
        return nameCat
    
    def getCategorySearchByName(self, keySearch):
        sql = "SELECT * FROM category WHERE category.CategoryName like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listCategory = []
        while row is not None:
            cat = Category.Category(row[0], row[1])
            listCategory.append(cat)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listCategory

    def getCategorySearchByCode(self, keySearch):
        sql = "SELECT * FROM category WHERE category.CategoryID like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listCategory = []
        while row is not None:
            cat = Category.Category(row[0], row[1])
            listCategory.append(cat)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listCategory

    def insertCategory(self, category):
        sql = "INSERT INTO `category` (`CategoryID`,`CategoryName`) VALUES (NULL, %s)"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (category.getCategoryName(),)
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
    
    def updateCategory(self, category):
        sql = "UPDATE category SET category.CategoryName = %s WHERE category.CategoryID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (category.getCategoryName(), category.getCategoryID())
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

    def deleteCategory(self, id):
        sql = "DELETE FROM category WHERE category.CategoryID = %s"
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

# categoryDAL = CategoryDAL()
# listCat = categoryDAL.getListCategory()
# for cat in listCat:
#     print(cat.getCategoryID())


