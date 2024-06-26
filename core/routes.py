from flask import render_template, url_for, redirect
from core import app, db, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from core.form import FormLogin, FormCriarConta
from core.models import Usuario, Fotos
@app.route("/", methods=["GET","POST"])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", usuario=usuario.username))
    return render_template("homepage.html", form = formlogin)


@app.route("/criarconta", methods=["GET","POST"])
def criarconta(): 
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data,senha=senha,email=formcriarconta.email.data)
        db.session.add(usuario)
        db.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", usuario=usuario.username))
    return render_template("criarconta.html", form = formcriarconta)


@app.route("/perfil/<usuario>", methods=["GET","POST"])
@login_required
def perfil(usuario):
    return render_template("perfil.html",usuario=usuario)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))