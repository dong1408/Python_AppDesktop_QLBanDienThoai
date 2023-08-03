import mysql.connector

class ConnectDAL:

    myconn = None   

    def __init__(self):
        global myconn
        myconn = mysql.connector.connect(
            host="localhost", database="qldienthoai_python", user="root", passwd="")        

    def getConnect(self):
        global myconn
        return myconn

    def close(self):
        global myconn
        myconn.close()