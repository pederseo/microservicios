from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.auth_service import register, login

gateway_bp = Blueprint('gateway', __name__)


@gateway_bp.route('/')
def index():
    return render_template('index.html')

@gateway_bp.route('/register')
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user_register = register(username, password)
        if user_register:
            return render_template('dashboard.html')
    else:
        flash('nombre de usuario invalido')
        return render_template('register.html')

    return render_template('register.html')

@gateway_bp.route('/login')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_login = login(username,password)
    return render_template('login.html')

