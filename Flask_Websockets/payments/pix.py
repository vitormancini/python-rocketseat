import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self, base_dir=''):
        # Criar o pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())
        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make(hash_payment)
        img.save(f'{base_dir}static/img/qrcode_payment_{bank_payment_id}.png')

        return { 'bank_payment_id': bank_payment_id, 'qrcode_path': f'qrcode_payment_{bank_payment_id}' }