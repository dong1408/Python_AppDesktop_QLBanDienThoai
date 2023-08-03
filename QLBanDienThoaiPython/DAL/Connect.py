# Vị trí import package
from mysql.connector import MySQLConnection, Error
# import mysql.connector
 
# Hàm kết nối
def connect():
    """ Kết nối MySQL bằng module MySQLConnection """
    db_config = {
        'host': 'localhost',
        'database': 'qldienthoai_python',
        'user': 'root',
        'password': ''
    }
 
    # Biến lưu trữ kết nối
    conn = None
 
    try:
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            return conn
 
    except Error as error:
        print(error)
 
    return conn
 
# Test thử
conn = connect()
print(conn)

def getListStaffTest():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM staff")
        row = cursor.fetchone()
        while row is not None:    
            print(row)
            row = cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        # Đóng kết nối
        cursor.close()
        conn.close()

getListStaffTest()