import psycopg2

db = psycopg2.connect(host="localhost", database="proyecto", user="postgres", password="1234")



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

def listaproductosg():

    sql = "SELECT * FROM productos "
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data

def mostrarproducto(id):

    sql = "select * from productos where id_producto="+id
    print(sql)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

    for row in data:
        cat = row[5]


    return data,cat

def mprodcat(categoria,id):

    sql = "select * from productos where tipo='" + str(categoria) + "' and id_producto<>"+id
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data



