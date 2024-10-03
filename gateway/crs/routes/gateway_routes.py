from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.auth_service import registro_usuario, login_usuario, decode_token
from services.info_band import ver_datos

gateway_bp = Blueprint('gateway', __name__)


@gateway_bp.route('/')
def index():
    return render_template('index.html')

@gateway_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:

            response = registro_usuario(username,password)

            # Lógica para registrar el usuario en la base de datos o realizar alguna operación
            return render_template('login.html')

    return render_template('registro.html')

@gateway_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        token = login_usuario(username,password)
        print(token)
        verificacion = decode_token(token)
        if verificacion['username'] == username:
            return redirect(url_for('gateway.band_info'))
    return render_template('login.html')


@gateway_bp.route('/band_info', methods=['GET', 'POST'])
def band_info():
    eventos = ver_datos()
    print(eventos)
    return render_template('band_info.html', eventos=eventos)