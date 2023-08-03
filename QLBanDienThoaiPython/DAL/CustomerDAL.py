import ConnectDAL
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
import Customer

class CustomerDAL:

    def getListCustomer(self):
        sql = "SELECT * FROM customer"
        conn = ConnectDAL.ConnectDAL().getConnect()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        listCustomer = []
        while row is not None:
            customer = Customer.Customer(row[0], row[1], row[2],
                                         row[3], row[4])
            listCustomer.append(customer)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listCustomer

    def getCustomerByID(self, id):
        sql = "SELECT * FROM customer WHERE customer.CustomerID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        staff = Customer.Customer(row[0], row[1], row[2],
                                  row[3], row[4])
        cursor.close()
        conn.close()
        return staff
    
    def getNameCustomerByID(self, id):
        sql = "SELECT CustomerName FROM customer WHERE customer.CustomerID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        nameCustomer = row[0]
        cursor.close()
        conn.close()
        return nameCustomer
    
    def getCustomerSearchByName(self, keySearch):
        sql = "SELECT * FROM customer WHERE customer.CustomerName like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listCustomer = []
        while row is not None:
            customer = Customer.Customer(row[0], row[1], row[2], row[3], row[4])
            listCustomer.append(customer)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listCustomer

    def getCustomerSearchByCode(self, keySearch):
        sql = "SELECT * FROM customer WHERE customer.CustomerID like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listCustomer = []
        while row is not None:
            customer = Customer.Customer(row[0], row[1], row[2], row[3], row[4])
            listCustomer.append(customer)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listCustomer
    
    def getCustomerSearchByPhone(self, keySearch):
        sql = "SELECT * FROM customer WHERE customer.PhoneNumber = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (keySearch,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listCustomer = []
        while row is not None:
            customer = Customer.Customer(row[0], row[1], row[2], row[3], row[4])
            listCustomer.append(customer)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listCustomer

    def insertCustomer(self, customer):
        sql = "INSERT INTO `customer` (`CustomerID`,`CustomerName`,`PhoneNumber`,`Email`,`Address`) VALUES (NULL, %s, %s, %s, %s)"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (customer.getCustomerName(), customer.getPhoneNumber(), customer.getEmail(), customer.getAddress())
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

    def updateCustomer(self, customer):
        sql = "UPDATE `customer` SET `CustomerName` = %s, `PhoneNumber` = %s, `Email` = %s, `Address` = %s WHERE `CustomerID` = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (customer.getCustomerName(), customer.getPhoneNumber(), customer.getEmail(), customer.getAddress(), customer.getCustomerID())
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

    def deleteCustomer(self, id):
        sql = "DELETE FROM customer WHERE customer.CustomerID = %s"
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
