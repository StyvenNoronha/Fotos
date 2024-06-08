from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from core.models import Usuario
class FormLogin():
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")


class FormCriarConta():
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuario", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("Corfirmação de senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao =  SubmitField("Criar Conta")
    
    
    def Validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("emailk ja cadastrado ")
        
        
#10:35        