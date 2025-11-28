
from wtforms import Form, IntegerField, SubmitField, StringField, PasswordField, EmailField, BooleanField
from wtforms import validators

class userform(Form):
    
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message='El campo es requerido')
    ])

    nombre = StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')
    ])
    
    apellido = StringField("Apellido", [
        validators.DataRequired(message='El campo es requerido')
    ])

    email = EmailField("Correo", [
        validators.DataRequired(message='El campo es requerido'),
        validators.Email(message='Ingresa un correo electrónico válido') 
    ])
 