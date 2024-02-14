from flask import Flask, request, jsonify
import bcrypt
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

# Rota de login
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

        if user and bcrypt.checkpw(str.encode(password), user.password):
            login_user(user)
            print(f'Usuário autenticado: {current_user.is_authenticated}')
            return jsonify({ 'message': 'Usuário autenticado'})


    return jsonify({ 'message': 'Usuário ou senha inválidos'}), 400

# Rota de logout
@app.route('/logout', methods=['GET'])
@login_required # Apenas acessa esta rota usuários autenticados
def logout():
    logout_user()
    return jsonify({ 'message': 'Logout realizado com sucesso'})

# Rota de cadastro de usuários
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data['username']
    password = data['password']

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt()) # Criptografando a senha
        user = User(username = username, password = hashed_password, role = 'user')
        db.session.add(user)
        db.session.commit()

        return jsonify({ 'message': 'Usuário cadastrado com sucesso!' }) 
    
    return jsonify({ 'message': 'Dados inválidos' }), 400

# Leitura dos usuários cadastrados
@app.route('/users', methods=['GET'])
@login_required
def get_users():
    users = User.query.all()
    all_users = [user.username for user in users]
    return jsonify({
        'users': all_users,
        'total': len(all_users)
        })

# Leitura de um usuário
@app.route('/users/<int:id>', methods=['GET'])
@login_required
def get_user(id):
    user = User.query.get(id)

    if user:
        return { 'username': user.username}

    return jsonify({'message': 'Usuário não encontrado'}), 404

# Update de usuário
@app.route('/users/<int:id>', methods=['PUT'])
@login_required
def update_user(id):
    user = User.query.get(id)
    data = request.json
    password = data['password'] # Atualiza apenas a senha para não correr problemas com a autenticação do Flask

    # Um usuário apenas pode alterar informações dele própio. Um adm pode alterar informações de qualquer usuário
    if id != current_user.id and current_user.role == 'user':
        return jsonify({'message': 'Operação não permitida'}), 403

    if user and password:
        user.password = password
        db.session.commit()
        return jsonify({'message': 'Usuário alterado com sucesso!'})
    
    return jsonify({'message': 'Usuário não encontrado!'}), 404

# Exclusão de usuário
@app.route('/users/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)

    if user and id != current_user.id:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Usuário excluído com sucesso!'})
    
    return jsonify({'message': 'Usuário não encontrado!'}), 404
    

if __name__ == '__main__':
    app.run(debug=True)