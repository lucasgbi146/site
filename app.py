from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import CadastrarForm, EntrarForm, ComentForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ED.db'
app.config['SECRET_KEY'] = 'sdlsjehfslirjrnbd'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(12), unique=True, nullable=False)
    senha = db.Column(db.String(80), nullable=False)
    sobre = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.usuario

@app.route('/')
def inicio():

    return render_template('inicio.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastrarForm()
    if request.method == 'POST':
        user = User()
        usuario = request.form['usuario']
        email = request.form['email']
        senha = request.form['senha']
        sobre = request.form['sobre']
        user = User.query.filter_by(usuario=request.form['usuario']).first() or User.query.filter_by(email=request.form['email']).first()
        if user:
            #flash("Dados inválios")
            return redirect(url_for('cadastro'))

        user = User(usuario=usuario, email=email, senha=senha, sobre=sobre)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('cadastro.html', form = form)

@app.route('/login')
def login():
    form = EntrarForm()
    
    return render_template('login.html', form=form)

@app.route('/ocupações')
def ocupações():

    return render_template('ocupações.html')

@app.route('/comentarios')
def comentarios():
    form = ComentForm()

    return render_template('comentarios.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)