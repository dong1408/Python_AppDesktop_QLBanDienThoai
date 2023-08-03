import sys
sys.path.append('./QLBanDienThoaiPython/DAL')
import StaffDAL

class StaffBLL:

    def getListStaff(self):
        return StaffDAL.StaffDAL().getListStaff()

    def getStaffByID(self, id):
        return StaffDAL.StaffDAL().getStaffByID(id)
    
    def getNameStaffByID(self, id):
        return StaffDAL.StaffDAL().getNameStaffByID(id)
    
    def getStaffSearchByName(self, keySearch):
        return StaffDAL.StaffDAL().getStaffSearchByName(keySearch)
    
    def getStaffSearchByCode(self, keySearch):
        return StaffDAL.StaffDAL().getStaffSearchByCode(keySearch)
    
    def insertStaff(self, staff):
        return StaffDAL.StaffDAL().insertStaff(staff)

    def updateStaff(self,staff):
        return StaffDAL.StaffDAL().updateStaff(staff)

    def deleteStaff(self, id):
        return StaffDAL.StaffDAL().deleteStaff(id)
    
    def checkLogin(self, userName, password):
        return StaffDAL.StaffDAL().checkLogin(userName, password)
