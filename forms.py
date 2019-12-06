#coding: utf-8
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, TextField)
from wtforms.validators import DataRequired, Length, Email

class CadastrarForm(FlaskForm):
    usuario = StringField('Usuário', validators = [DataRequired(), Length(min = 8, max = 80)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    senha = PasswordField('Password', validators = [DataRequired()])
    sobre = TextField('Sobre você', validators = [DataRequired()])
    submit = SubmitField('Cadastrar')

class EntrarForm(FlaskForm):
    usuario = StringField('Usuário', validators = [DataRequired(), Length(min = 8, max = 80)])
    senha = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Cadastrar')

class CadastrarForm(FlaskForm):
    usuario = StringField('Usuário', validators = [DataRequired(), Length(min = 8, max = 80)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    senha = PasswordField('Password', validators = [DataRequired()])
    sobre = TextField('Sobre você', validators = [DataRequired()])
    submit = SubmitField('Cadastrar')