from flask import Flask, request, jsonify
from database import db
from datetime import datetime
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models.user import User
from models.meal import Meal

# Cria o banco: db.create_all(), db.session.commit()
# db.session.add(user)

app = Flask(__name__)

app.config['SECRET_KEY'] ='minha_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
login_manager = LoginManager()

login_manager.init_app(app)

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

        if user:
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

# Cadastro de refeição
@app.route('/meals', methods=['POST'])
@login_required
def create_meal():
    data = request.json
    name = data['name']
    datetime = data['date_time']
    in_diet = data['in_diet']
    
    meal = Meal(name = name, in_diet = in_diet, datetime = datetime)
    db.session.add(meal)
    db.session.commit()

    return jsonify({ 'message': 'Refeição rgistrada com sucesso!' }) 

# Todas refeições
@app.route('/meals', methods=['GET'])
@login_required
def get_meals():
    meals = Meal.query.all()
    all_meals = [meal.name for meal in meals]

    print(type(all_meals))

    return jsonify({'meals': all_meals, 'total': len(all_meals)})

# Única refeição
@app.route('/meals/<int:id>', methods=['GET'])
@login_required
def get_meal(id):
    meal = Meal.query.get(id)

    if meal:
        return jsonify({ 'message': meal.name })  
    
    return jsonify({ 'message': 'Refeição não encontrada' })  

# Atualiza refeição
@app.route('/meals/<int:id>', methods=['PUT'])
@login_required
def update_meal(id):
    meal = Meal.query.get(id)
    data = request.json
    name = data['name']
    datetime = data['datetime']
    in_diet = data['in_diet']

    if not meal:
        return jsonify({ 'message': 'Refeição não encontrada' })  
    
    meal.name = name
    meal.datetime = datetime
    meal.in_diet = in_diet

    db.session.commit()
    return jsonify({ 'message': 'Refeição atualizada' })

    
# Exclui refeição
@app.route('/meals/<int:id>', methods=['DELETE'])
@login_required
def delete_meal(id): 
    meal = Meal.query.get(id)

    if not meal:
        return jsonify({ 'message': 'Refeição não encontrada' })
    
    db.session.delete(meal)
    db.session.commit()

    return jsonify({ 'message': 'Refeição excluída' })

if __name__ == '__main__':
    app.run(debug=True)
