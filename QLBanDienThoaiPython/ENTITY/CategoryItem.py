from PyQt6.QtGui import QStandardItem

class CategoryItem(QStandardItem):
    def __init__(self, category):
        super(CategoryItem, self).__init__(category.CategoryName)
        self.category = category