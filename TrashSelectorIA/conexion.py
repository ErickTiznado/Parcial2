<<<<<<< HEAD
import mysql.connector

class conexion:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='12345',
            database='login'
        )
        if self.db.is_connected():
            print("Conexion establecida con exito")
        else:
            print("Error en la conexion")
    def consultar(self, sql):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()

    def ejecutar_consulta(self, sql, val):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, val)
            self.db.commit()
            return "ok"
        except Exception as e:
=======
import mysql.connector

class conexion:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='12345',
            database='login'
        )
        if self.db.is_connected():
            print("Conexion establecida con exito")
        else:
            print("Error en la conexion")
    def consultar(self, sql):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(sql)
        return cursor.fetchall()

    def ejecutar_consulta(self, sql, val):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, val)
            self.db.commit()
            return "ok"
        except Exception as e:
>>>>>>> d06c0a8f61607f100151d1ccb1b885cb1333365d
            return str(e)