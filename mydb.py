#pip install pymysql (Instalando pacote pymysql no arquivo pela bash)

#Importando pacote para conexão com MySQL
import pymysql

#Fazendo a conexão

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='12345'
)

#Criando Cursor
cursorObject = dataBase.cursor()

#Comandos SQL para criação do BancodeDados
cursorObject.execute("CREATE DATABASE AcmeCO")
print("DataBase Criada!")
