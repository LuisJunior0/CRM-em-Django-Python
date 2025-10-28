import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='12345'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE AcmeCO")
print("DataBase Criada!")
