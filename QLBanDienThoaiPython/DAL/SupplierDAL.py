import ConnectDAL
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
import Supplier

class SupplierDAL:

    def getListSupplier(self):
        sql = "SELECT * FROM supplier"
        conn = ConnectDAL.ConnectDAL().getConnect()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        listSupplier = []
        while row is not None:
            supplier = Supplier.Supplier(row[0], row[1], row[2],
                                         row[3], row[4])
            listSupplier.append(supplier)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listSupplier

    def getSupplierByID(self, id):
        sql = "SELECT * FROM supplier WHERE supplier.SupplierID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        supplier = Supplier.Supplier(row[0], row[1], row[2],
                                  row[3], row[4])
        cursor.close()
        conn.close()
        return supplier

    def insertSupplier(self, supplier):
        sql = "INSERT INTO `supplier` (`SupplierID`,`SupplierName`,`Email`,`Address`,`PhoneNumber`) VALUES (NULL, %s, %s, %s, %s)"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (supplier.getSupplierName(), supplier.getEmail(), supplier.getPassword(), supplier.getPhoneNumber())
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

    def updateSupplier(self, supplier):
        sql = "UPDATE `supplier` SET `SupplierName` = %s, `PhoneNumber` = %s, `Email` = %s, `Address` = %s WHERE `SupplierID` = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (supplier.getSupplierName(), supplier.getPhoneNumber(), supplier.getEmail(), supplier.getAddress(), supplier.getSupplierID())
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

    def deleteSupplier(self, id):
        sql = "DELETE FROM supplier WHERE supplier.SupplierID = %s"
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
