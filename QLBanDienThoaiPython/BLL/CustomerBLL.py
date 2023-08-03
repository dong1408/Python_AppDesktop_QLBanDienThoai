import sys
sys.path.append('./QLBanDienThoaiPython/DAL')
import CustomerDAL

class CustomerBLL:

    def getListCustomer(self):
        return CustomerDAL.CustomerDAL().getListCustomer()
    
    def getCustomerByID(id):
        return CustomerDAL.CustomerDAL().getCustomerByID(id)
    
    def getNameCustomerByID(self, id):
        return CustomerDAL.CustomerDAL().getNameCustomerByID(id)
    
    def getCustomerSearchByCode(self, keySearch):
        return CustomerDAL.CustomerDAL().getCustomerSearchByCode(keySearch)

    def getCustomerSearchByName(self, keySearch):
        return CustomerDAL.CustomerDAL().getCustomerSearchByName(keySearch)
    
    def getCustomerSearchByPhone(self, keySearch):
        return CustomerDAL.CustomerDAL().getCustomerSearchByPhone(keySearch)

    def insertCustomer(self, cus):
        return CustomerDAL.CustomerDAL().insertCustomer(cus)

    def updateCustomer(self, cus):
        return CustomerDAL.CustomerDAL().updateCustomer(cus)

    def deleteCustomer(self, id):
        return CustomerDAL.CustomerDAL().deleteCustomer(id)
    