import ConnectDAL
import sys
sys.path.append('./QLBanDienThoaiPython/ENTITY')
import Staff

class StaffDAL:

    # def getListStaff(self):
    #     sql = "SELECT * FROM staff"
    #     conn = ConnectDAL.ConnectDAL().getConnect()
    #     cursor = conn.cursor()
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     listStaff = []
    #     for row in result:
    #         staff = Staff.Staff(row[0], row[1], row[2],
    #                             row[3], row[4], row[5], row[6], row[7])
    #         listStaff.append(staff)
    #     cursor.close()
    #     conn.close()
    #     return listStaff

    def getListStaff(self):
        sql = "SELECT * FROM staff"
        conn = ConnectDAL.ConnectDAL().getConnect()
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        listStaff = []
        while row is not None:
            staff = Staff.Staff(row[0], row[1], row[2],
                                row[3], row[4], row[5], row[6], row[7])
            listStaff.append(staff)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listStaff

    def getStaffByID(self, id):
        sql = "SELECT * FROM staff WHERE staff.StaffID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        staff = Staff.Staff(row[0], row[1], row[2],
                            row[3], row[4], row[5], row[6], row[7])
        cursor.close()
        conn.close()
        return staff
    
    def getNameStaffByID(self, id):
        sql = "SELECT UserName FROM staff WHERE staff.StaffID = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (id,)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        nameStaff = row[0]
        cursor.close()
        conn.close()
        return nameStaff
    
    def getStaffSearchByName(self, keySearch):
        sql = "SELECT * FROM staff WHERE staff.FullName like %s or staff.UserName like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%", "%"+str(keySearch)+"%")
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listStaff = []
        while row is not None:
            staff = Staff.Staff(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            listStaff.append(staff)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listStaff

    def getStaffSearchByCode(self, keySearch):
        sql = "SELECT * FROM staff WHERE staff.StaffID like %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = ("%"+str(keySearch)+"%",)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        listStaff = []
        while row is not None:
            staff = Staff.Staff(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            listStaff.append(staff)
            row = cursor.fetchone()
        cursor.close()
        conn.close()
        return listStaff

    def insertStaff(self, staff):
        sql = "INSERT INTO `staff` (`StaffID`,`FullName`,`UserName`,`Password`,`Email`,`Address`,`PhoneNumber`,`Gender`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (staff.getFullName(), staff.getUserName(), staff.getPassword(), staff.getEmail(), staff.getAddress(), staff.getPhoneNumber(), staff.getGender())
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
    
    def updateStaff(self, staff):
        sql = "UPDATE `staff` SET `FullName` = %s, `UserName` = %s, `Email` = %s, `Address` = %s, `PhoneNumber` = %s, `Gender` = %s WHERE `StaffID` = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (staff.getFullName(), staff.getUserName(), staff.getEmail(), staff.getAddress(), staff.getPhoneNumber(), staff.getGender(), staff.getStaffID())
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

    def deleteStaff(self, id):
        sql = "DELETE FROM staff WHERE staff.StaffID = %s"
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
        
    # def checkLogin(self, userName, password):
    #     sql = "SELECT COUNT(*) FROM staff WHERE staff.UserName = %s AND staff.Password = %s"
    #     conn = ConnectDAL.ConnectDAL().getConnect()
    #     val = (userName, password)
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute(sql, val)
    #         row = cursor.fetchall()
    #         if(row[0][0] == 1):
    #             cursor.close()
    #             conn.close()
    #             return True
    #         else:
    #             cursor.close()
    #             conn.close()
    #             return False
    #     except:
    #         conn.rollback()
    #         cursor.close()
    #         conn.close()
    #         return False
        
    def checkLogin(self, userName, password):
        sql = "SELECT * FROM staff WHERE staff.UserName = %s AND staff.Password = %s"
        conn = ConnectDAL.ConnectDAL().getConnect()
        val = (userName, password)
        cursor = conn.cursor()
        cursor.execute(sql, val)
        row = cursor.fetchone()
        if row is None:
            return None
        staff = Staff.Staff(row[0], row[1], row[2],
                            row[3], row[4], row[5], row[6], row[7])
        cursor.close()
        conn.close()
        return staff


staffDAO = StaffDAL()

# listStaff = staffDAO.getListStaff()
# for item in listStaff:
#     item.toString()
# staff = Staff.Staff("1","abc","abc","abc","abc","nam dinh","098765443","Male")

# staff = Staff.Staff()
# staff.setFullName("abc")
# staff.setUserName("abc")
# staff.setPassword("abc")
# staff.setEmail("abc.com")
# staff.setAddress("Nam Dinh")
# staff.setPhoneNumber("0987654567")
# staff.setGender("Male")
# staffDAO.insertStaff(staff)

# staff = staffDAO.getStaffByID(1)
# staff.toString()

# staffDAO.deleteStaff(4)
