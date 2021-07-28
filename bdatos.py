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

        if email == user and contrasenia == contra:
            return True
        else:
            return False

def existeuser(id):
    sql = "select exists(select 1 from clientes where cedula='"+str(id)+"');"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        dato = row[0]


    return dato



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
    #print(sql)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    #print(data)

    for row in data:
        cat = row[5]


    return data,cat

def mprodcat(categoria,id):

    sql = "select * from productos where tipo='" + str(categoria) + "' and id_producto<>"+id
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data


def nuevocliente(cedula,nombre,apellido,telefono,direccion,correo,clave):
    try:
        sql="INSERT INTO CLIENTES (cedula,id_perfil,nombre,apellido,telefono,direccion,correo,clave) values " \
             "('"+str(cedula)+"','1','"+str(nombre)+"','"+str(apellido)+"','"+str(telefono)+"','"+str(direccion)+"','"+str(correo)+"','"+str(clave)+"');"
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return True
    except:
        return False


def verprocompara(id):

    sql = "SELECT nombreprod,caracteristicas,imagen FROM PRODUCTOS where id_producto="+id
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data

def agcarrito(cedula,nite,idpro):

    try:
        sql = "INSERT INTO carro (id_producto,cedula,cantidad) values " \
          "('" + str(idpro) + "','" + str(cedula) + "','" + str(nite) + "');"
        #print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return True

    except:
        return False



def visualcarrito(cedula):

    sql = "SELECT CARRO.ID_CARRITO,PRODUCTOS.NOMBREPROD,PRODUCTOS.IMAGEN,CARRO.CANTIDAD,(PRODUCTOS.PRECIO*CARRO.CANTIDAD) " \
          "AS SUBTOTAL FROM CARRO,PRODUCTOS WHERE CARRO.ID_PRODUCTO = PRODUCTOS.ID_PRODUCTO AND CARRO.CEDULA='"+str(cedula)+"';"
    #print("visual"+sql)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data

def vsubtotal(cedula):
    sql = "SELECT SUM(PRODUCTOS.PRECIO*CARRO.CANTIDAD) FROM CARRO,PRODUCTOS WHERE CARRO.ID_PRODUCTO = PRODUCTOS.ID_PRODUCTO AND CARRO.CEDULA='" + str(
        cedula) + "';"

    cursor = db.cursor()
    cursor.execute(sql)
    data1 = cursor.fetchall()
    for row in data1:
        stotal = row[0]

    return stotal

def prodgoogle():

    sql="select * from productos where tipo='G'"
    sql1 = "select * from productos where tipo='A'"
    sql2 = "select * from productos where tipo='X'"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    cursor1 = db.cursor()
    cursor1.execute(sql1)
    data1 = cursor1.fetchall()

    cursor2 = db.cursor()
    cursor2.execute(sql2)
    data2 = cursor2.fetchall()
    return data,data1,data2

#######metodos para conteo ###############

def numerogeneralpro():

    sql = "select count(*)as registros from productos;"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        data = row[0]

    return data

def numerogeneralprog():

    sql = "select count(*)as registros from productos where tipo='G';"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        data = row[0]

    return data

def numerogeneralproa():

    sql = "select count(*)as registros from productos where tipo='A';"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        data = row[0]

    return data

def numerogeneralprox():

    sql = "select count(*)as registros from productos where tipo='X';"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        data = row[0]

    return data

def cantidadcarrito(id):

    sql="SELECT count(*) from carro where cedula='"+str(id)+"';"
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        data = row[0]

    return data


def eliminarcarrito(id,cedula):
    try:
        sql="delete from carro where id_carrito='"+str(id)+"' and cedula='"+str(cedula)+"';"
        #print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return True
    except:
        return False


def factura(cedula,nump,subtotal,total,fecha):

    try:
        sql = "INSERT INTO factura (cedula,numproductos,subtotal,total,fecha) values " \
          "('" + str(cedula) + "','" + str(nump) + "','" + str(subtotal) + "','"+str(total)+"','"+str(fecha)+"');"
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return True

    except:
        return False

def carritoel(cedula):
    try:
        sql="delete from carro where cedula='"+str(cedula)+"'"
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        return True
    except:
        return False


def verfacturas(cedula):

    sql = "SELECT * FROM FACTURA WHERE CEDULA='"+str(cedula)+"';"
    print("visual"+sql)
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    return data


#select * from factura where cedula='1234567890'

