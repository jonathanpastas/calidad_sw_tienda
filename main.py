from flask import Flask, render_template
import hashlib

app = Flask(__name__)


@app.route('/')
def index() -> 'html':
    result = hashlib.md5(b'1234')
    print('equivale', result.digest())
    return render_template('index.html', titulo='Tienda de Ropa Cracks')


@app.route('/login')
def login() -> 'html':
    return render_template('login.html', titulo='Iniciar Sesión')


app.run(debug=True)
