import sys
sys.path.append('./QLBanDienThoaiPython/DAL')
import CategoryDAL

class CategoryBLL:

    def getListCategory(self):
        return CategoryDAL.CategoryDAL().getListCategory()
    
    def getCategoryByID(self, id):
        return CategoryDAL.CategoryDAL().getCategoryByID()

    def getNameCategoryByID(self, id):
        return CategoryDAL.CategoryDAL().getNameCategoryByID(id)
    
    def getCategorySearchByName(self, keySearch):
        return CategoryDAL.CategoryDAL().getCategorySearchByName(keySearch)
    
    def getCategorySearchByCode(self, keySearch):
        return CategoryDAL.CategoryDAL().getCategorySearchByCode(keySearch)
    
    def insertCategory(self, category):
        return CategoryDAL.CategoryDAL().insertCategory(category)

    def updateCategory(self, category):
        return CategoryDAL.CategoryDAL().updateCategory(category)
        
    def deleteCategory(self, id):
        return CategoryDAL.CategoryDAL().deleteCategory(id)