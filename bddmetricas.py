
import psycopg2

db = psycopg2.connect(host="localhost", database="metricas", user="postgres", password="1234")
#### ingreso de metricas ####################


def ayudalinea(num):

    #insertar el registro

    sql1="insert into entendibilidad (nayudas, npagacc, nmensajeserror, tiempopaginas) values ('"+str(num)+"',0,0,0);"
    cursor = db.cursor()
    cursor.execute(sql1)
    db.commit()








