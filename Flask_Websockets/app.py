from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from models.payment import Payment
from payments.pix import Pix
from flask_socketio import SocketIO

from datetime import datetime, timedelta

app = Flask(__name__)

# Configuração do Websocket
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'minha_secret_key'

# flask shell => db.create_all()

db.init_app(app)

# Criação de um pagamento Pix
@app.route('/payments/pix', methods = ['POST'])
def create_payment_pix():
    data = request.get_json()

    # Validações
    if 'value' not in data:
        return jsonify({ "message": "Invalid value" }), 400
    
    expiration_date = datetime.now() + timedelta(minutes = 30) # Data atual + 30 minutos

    new_payment = Payment(value = data['value'], expiration_date = expiration_date)

    # Simula a criação de um Pix em uma instituição financeira
    pix_payment = Pix()
    pix_payment_data = pix_payment.create_payment()

    new_payment.bank_payment_id = pix_payment_data['bank_payment_id']
    new_payment.qr_code = pix_payment_data['qrcode_path']

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({ "message": "The payment has been created", "payment": new_payment.to_dict() })

# Envio de imagens pela API
@app.route('/payments/pix/qrcode/<file_name>', methods = ['GET'])
def get_img(file_name):
    return send_file(f'static/img/{file_name}.png', mimetype='image/png')

# Visualização do pagamento
@app.route('/payments/pix/<int:payment_id>', methods = ['GET'])
def payment_pix_page(payment_id):
    payment = Payment.query.get(payment_id) # Obtendo o pagamento pelo id

    if not payment:
        return render_template('404.html')
    
    host = request.host_url # Obtendo o host do servidor para carregamento da imagem do qrcode

    if payment.paid:
        return render_template('confirmed_payment.html', payment=payment, host=host)
    
    return render_template('payment.html', payment=payment, host=host)

@app.route('/payments/pix/confirmation', methods = ['POST'])
def pix_confirmation():
    data = request.get_json()

    if "bank_payment_id" not in data or "value" not in data:
        return jsonify({ "message": "Invalid payment data" }), 400
    
    payment = Payment.query.filter_by(bank_payment_id = data.get('bank_payment_id')).first() # Filtra um pagamento pelo bank_payment_id

    if not payment:
        return jsonify({ "message": "Payment not found" }), 404
    
    if data.get('value') != payment.value: # Pagamento recebido não pode ser diferente do valor da cobrança
        return jsonify({ "message": "Invalid payment data" }), 400

    payment.paid = True
    db.session.commit()

    socketio.emit(f'payment-confirmed-{payment.id}')

    return jsonify({ "message": "The payment has been confirmed" })

# Websockets
@socketio.on('connect')
def handle_connect():
    print('Client connected to the server')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client has been disconnected to the server')

if __name__ == '__main__':
    socketio.run(app, debug=True)