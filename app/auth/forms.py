from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms import ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from ..models import tblUser


class LoginForm(FlaskForm):
    username = StringField('UserName', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('UserName', validators=[Required(),Length(1,64), Regexp(
        '^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, '
        'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
    Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_username(self, field): # 验证用户名是否已存在的函数，根据函数名称自动调用。
        if tblUser.query.filter_by(name=field.data).first():
            raise ValidationError('Username already in use.')

