class Staff:

    def __init__(self, StaffID="", FullName="", UserName="", Password="", Email="", Address="", PhoneNumber="", Gender=""):
        self.StaffID = StaffID
        self.FullName = FullName
        self.UserName = UserName
        self.Password = Password
        self.Email = Email
        self.Address = Address
        self.PhoneNumber = PhoneNumber
        self.Gender = Gender

    def getStaffID(self):
        return self.StaffID

    def setStaffID(self, staffID):
        self.StaffID = staffID

    def getFullName(self):
        return self.FullName

    def setFullName(self, fullName):
        self.FullName = fullName

    def getUserName(self):
        return self.UserName

    def setUserName(self, userName):
        self.UserName = userName

    def getPassword(self):
        return self.Password

    def setPassword(self, password):
        self.Password = password

    def getEmail(self):
        return self.Email

    def setEmail(self, email):
        self.Email = email

    def getAddress(self):
        return self.Address

    def setAddress(self, address):
        self.Address = address

    def getPhoneNumber(self):
        return self.PhoneNumber

    def setPhoneNumber(self, phoneNumber):
        self.PhoneNumber = phoneNumber

    def getGender(self):
        return self.Gender

    def setGender(self, gender):
        self.Gender = gender

    def toString(self):
        print(f"ID: {self.StaffID} Fullname: {self.FullName} Username: {self.UserName} Email: {self.Email} Address: {self.Address} PhoneNumber: {self.PhoneNumber} Gender: {self.Gender} ")
