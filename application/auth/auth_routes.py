from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from .forms import LoginForm, RegisterForm  
from application.models.models import User, Role
from application import db, bcrypt


# Create a Blueprint for authentication
auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegisterForm()
    if form.validate_on_submit():
        default_role = Role.query.filter_by(name='guest').first()
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=hashed_password,
            name=form.name.data,
            lastname=form.lastname.data,
            role_id=default_role.id
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f"Registro exitoso! Has iniciado sesion como {user.username}", category='success')
        return redirect(url_for('main.home'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'Hubo un error creando el usuario: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter((User.username == form.username.data) |
                                 (User.email == form.username.data)).first()
        if attempted_user and bcrypt.check_password_hash(attempted_user.password_hash, form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Inicio de sesión fallido. Por favor, comprueba tu nombre de usuario y contraseña', 'danger')
    return render_template('login.html', title='Login', form=form)

@auth_blueprint.route('/logout')
def logout():
    logout_user()
    flash("Has cerrado sesión con éxito", 'info')
    return redirect(url_for('auth.login'))