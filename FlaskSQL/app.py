from flask import Flask, request, jsonify
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models.user import User

app = Flask(__name__)

app.config['SECRET_KEY'] ='minha_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

""" login_manager.login_view = 'login' """

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) 

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    if username and password:
        user = User.query.filter_by(username = username).first()

        if user and user.password == password:
            login_user(user)
            print(f'Usuário autenticado: {current_user.is_authenticated}')
            return jsonify({ 'message': 'Usuário autenticado'})


    return jsonify({ 'message': 'Usuário ou senha inválidos'}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({ 'message': 'Logout realizado com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)