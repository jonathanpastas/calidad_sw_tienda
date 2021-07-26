from flask import Flask, render_template, request, session, redirect, url_for, flash
from bdatos import *
from bddmetricas import *
import time

app = Flask(__name__)
app.secret_key = 'jsp1234'

##variables globales




################# METODOS DONDE SE RENDERIZAN PAGINAS WEB ##################
@app.route('/')
def index() -> 'html':
    return render_template('index.html', titulo='HomeSmart')


@app.route('/login')
def login() -> 'html':
    return render_template('login.html', titulo='Iniciar Sesión')


@app.route('/registro')
def cuentanueva() -> 'html':
    return render_template('registrarse.html', titulo='Crear una Cuenta Nueva')


@app.route('/verproductos')
def listaproductos() -> 'html':
    lista = listaproductosg()
    numero = numerogeneralpro()
    nug = numerogeneralprog()
    nua = numerogeneralproa()
    nux = numerogeneralprox()
    prog, proa, progx = prodgoogle();
    return render_template('productosbase.html', titulo='Lista de Productos', lstp=lista, np=numero, ng=nug, na=nua,
                           nx=nux, go=prog, am=proa, xi=progx)


@app.route('/productod', methods=['GET'])
def productogeneral() -> 'html':
    prod = request.args.get('id')

    datpro, cat = mostrarproducto(prod)
    daca = mprodcat(cat, prod)
    print(datpro)

    return render_template('detallep.html', titulo="HomeSmart", pr=datpro, pc=daca)


####Internacionalizacion
@app.route('/en')
def englishpage() -> 'html':
    return render_template('indexen.html', titulo='Welcome HomeSmart')


@app.route('/al')
def germanpage() -> 'html':
    return render_template('indexal.html', titulo='herzlich willkommen HomeSmart')


@app.route('/ru')
def rusianpage() -> 'html':
    return render_template('indexru.html', titulo='Добро пожаловать HomeSmart')


#################METODOS PRINCIPALES DE FUNCIONAMIENTO DEL SITIO ##################
# Metodo para Ingresar a la Sesion,Valida el Cliente

@app.route('/ingresar', methods=['POST'])
def ingreso() -> 'html':
    user = request.form['correo']
    clave1 = request.form['contrasenia']
    validar = queryDatos(user, clave1)
    print(validar)

    if validar == True:
        perfilu = perfiluser(user)
        nombre = nombreuser(user)
        cedula = ciuser(user)
        session['username'] = user
        session['pass'] = clave1
        session['perfiluser'] = perfilu
        session['nombre'] = nombre
        session['ci'] = cedula

        return redirect(url_for('paginicio'))
    else:
        flash(
            '<div class="alert alert-danger" role="alert"> <center><b> Correo Electronico o Contraseña son Incorrectos</b></center> </div>')
        return redirect(url_for('login'))


# Metodo que redirige a la pagina de inicio del cliente
@app.route('/inicio')
def paginicio() -> 'html':
    if 'username' in session:
        print("true")
        # menu=menuopciones(str(session['perfiluser']))
        usuario = session['username']
        nom = str(session['nombre'])
        ced = str(session['ci'])
        session['tiempo'] = time.time()
        session['nayudas'] = 0
        lista = listaproductosg()
        numero = numerogeneralpro()
        nug = numerogeneralprog()
        nua = numerogeneralproa()
        nux = numerogeneralprox()
        prog, proa, progx = prodgoogle()
        cpro = cantidadcarrito(ced)
        return render_template('cliente.html', titulo="HomeSmart", lstp=lista, nomb=nom, np=numero, ng=nug, na=nua,
                               nx=nux, go=prog, am=proa, xi=progx, cant=cpro)


    else:
        return redirect(url_for('login'))


@app.route('/producto', methods=['GET'])
def mostrarprod() -> 'html':
    if 'username' in session:
        print("true")
        # menu=menuopciones(str(session['perfiluser']))
        usuario = session['username']
        ced = str(session['ci'])
        cpro = cantidadcarrito(ced)
        nom = str(session['nombre'])
        prod = request.args.get('id')

        #metrica de cuanto tiempo necesita el usuario para pasar de una pagina a otra
        times=float(session['tiempo'])
        print("tiempo entre cliente y producto es ",round(time.time()-times))
        ##############################################################################
        datpro, cat = mostrarproducto(prod)
        daca = mprodcat(cat, prod)
        #print(datpro)

        return render_template('producto.html', titulo="HomeSmart", nomb=nom, pr=datpro, pc=daca, cant=cpro)


    else:
        return redirect(url_for('index'))


@app.route('/ingresarclie', methods=['POST'])
def ingusuario() -> 'html':
    cedula = request.form['cedula']
    apellido = request.form['apellido']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    direccion = request.form['domicilio']
    correo = request.form['correo']
    clave = request.form['contrasenia']
    existe = existeuser(cedula);

    print(existe)
    if existe == True:
        print("si existe pero no kcho")
        flash('<div class="alert alert-danger" role="alert"> <center><b> EL USUARIO YA EXISTE</b></center> </div>')
        return redirect(url_for('cuentanueva'))
    else:
        ingresar = nuevocliente(cedula, nombre, apellido, telefono, direccion, correo, clave)

    if ingresar == True:
        flash(
            '<div class="alert alert-success" role="alert"> <center><b> Cuenta Creada Exitosamente </b></center> </div>')
        return redirect(url_for('login'))
    else:
        flash(
            '<div class="alert alert-danger" role="alert"> <center><b> Se ha producido un error al crear la cuenta. Porfavor Intente Nuevamente</b></center> </div>')
        return redirect(url_for('cuentanueva'))


@app.route('/comparar')
def vcomparar() -> 'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        listap = listaproductosg()
        ced = str(session['ci'])
        cpro = cantidadcarrito(ced)
        return render_template('comparacion.html', titulo='Comparación de Productos', nomb=nom, prod=listap, cant=cpro)

    else:
        return redirect(url_for('index'))


@app.route('/pcomparar', methods=['POST'])
def comparaciones() -> 'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        p1 = request.form['prod1']
        p2 = request.form['prod2']
        proa = verprocompara(p1)
        prob = verprocompara(p2)
        ced = str(session['ci'])
        cpro = cantidadcarrito(ced)
        return render_template('vercomparaciones.html', titulo='Comparación de Productos', nomb=nom, pa=proa, pb=prob,
                               cant=cpro)

    else:
        return redirect(url_for('index'))


@app.route('/ayuda')
def ayudasclie() -> 'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        ced = str(session['ci'])
        cpro = cantidadcarrito(ced)
        #metrica veces que el usuario accede a ayudas en linea
        ar=int(session['nayudas'])
        session['nayudas']=ar+1


        return render_template('ayudaclie.html', titulo='Comparación de Productos', nomb=nom, cant=cpro)

    else:
        return redirect(url_for('index'))


@app.route('/agcarrito', methods=['POST'])
def carritoag() -> 'html':
    if 'username' in session:
        cedula = session['ci']
        usuario = session['username']
        nom = str(session['nombre'])
        npro = request.form['numc']
        idpro = request.form['prodId']
        print(npro)

        if npro =="0" :

            flash('<div class="alert alert-danger" role="alert"> <center><b> Escoga una cantidad del Producto </b></center> </div>')
            return redirect("/producto?id="+idpro)


        ingresar = agcarrito(cedula, npro, idpro);

        if ingresar == True:
            flash(
                '<div class="alert alert-success" role="alert"> <center><b> Producto Añadido a su Carrito Exitosamente </b></center> </div>')
            return redirect(url_for('vcarritocompra'))
        else:
            flash(
                '<div class="alert alert-danger" role="alert"> <center><b> Error al Añadir su Producto por favor verifique si existe existencias.</b></center> </div>')
            return redirect(url_for('vcarritocompra'))


@app.route('/vercarrito')
def vcarritocompra() -> 'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        cedula = session['ci']
        valores, sub = visualcarrito(cedula)
        ced = str(session['ci'])
        cpro = cantidadcarrito(ced)
        return render_template('vercarrito.html', titulo='Carrito de Compras', nomb=nom, carpro=valores, sto=sub,
                               cant=cpro)

    else:
        return redirect(url_for('index'))


@app.route('/eliminarcar', methods=['GET'])
def eliminarcar() -> 'html':
    if 'username' in session:

        ced = str(session['ci'])
        pr = request.args.get('prod')

        eliminar = eliminarcarrito(pr, ced)

        if eliminar == True:
            flash(
                '<div class="alert alert-success" role="alert"> <center><b> Producto Eliminado del Carrito de Compras</b></center> </div>')
            return redirect(url_for('vcarritocompra'))
        else:
            flash(
                '<div class="alert alert-danger" role="alert"> <center><b> No se ha podido eliminar el producto de su carrito por favor comuniquese con ayuda al cliente.</b></center> </div>')
            return redirect(url_for('vcarritocompra'))

    else:
        return redirect(url_for('index'))


@app.route('/confirmapago',methods=['POST'])
def pagarproductos() -> 'html':
    if 'username' in session:
        cedula = session['ci']
        usuario = session['username']
        nom = str(session['nombre'])
        tarjet = str(request.form['tarjeta'])
        mes = str(request.form['mes'])
        anio=str(request.form['anio'])
        subtotal=str(request.form['total'])
        clave=str(request.form['clave'])
        cpro = cantidadcarrito(cedula)
        tot=float(subtotal)*0.12
        total=float(subtotal)+tot

        if tarjet=="" or mes=="" or anio=="" or clave=="":
            flash(
                '<div class="alert alert-danger" role="alert"> <center><b> Estimado Cliente por favor verifique que todos los campos de su tarjeta hayan sidos completados.</b></center> </div>')
            return redirect(url_for('vcarritocompra'))
        else:
            ingresar=factura(cedula,cpro,subtotal,total)
            e=carritoel(cedula)


        if ingresar == True:
            return render_template('compra.html', titulo='Compra',val=total)
        else:
            flash(
                '<div class="alert alert-danger" role="alert"> <center><b> Error al Generar su Pago </b></center> </div>')
            return redirect(url_for('vcarritocompra'))

    else:
        return redirect(url_for('index'))

@app.route('/compra')
def compraval() -> 'html':
    if 'username' in session:
        usuario = session['username']
        nom = str(session['nombre'])
        cedula = session['ci']
        valores, sub = visualcarrito(cedula)
        ced = str(session['ci'])
        cpro = cantidadcarrito(ced)
        return render_template('compra.html', titulo='Compra')

    else:
        return redirect(url_for('index'))


# Metodo para Cerrar la Sesion
@app.route('/cerrarsesion')
def salir() -> 'html':
    # metrica veces que el usuario accede a ayudas en linea
    ar=int(session['nayudas'])
    print(ar)


    session.clear()


    return redirect(url_for('index'))


###########FIN DEL PROGRAMA #################
app.run(debug=True)
