import pymysql

db = pymysql.connect(
    host='remotemysql.com',
    user='3LuICOPYq0',
    password="Fh6aYfHmFi",
    db='3LuICOPYq0',
)

db.ping()

def queryDatos(user, contra):
    sql = "SELECT * FROM clientes WHERE correo='"+str(user)+"'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:

        email=row[6]
        contrasenia=row[7]

        print(email)
        print(contrasenia)
        if email == user and contrasenia == contra:
            return True
        else:
            return False


def perfiluser(user):

    dato=0
    sql = "SELECT * FROM clientes WHERE correo='"+str(user)+"'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        dato = row[1]
    return dato

def nombreuser(user):
    sql = "SELECT * FROM clientes WHERE correo='" + str(user) + "'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        nombre = row[2]+" "+row[3]
    return nombre

def ciuser(user):
    sql = "SELECT * FROM clientes WHERE correo='" + str(user) + "'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        ci = row[0]
    return ci
