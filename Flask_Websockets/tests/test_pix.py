import pytest
import os, sys

sys.path.append('../')

from payments.pix import Pix



def test_pix_create_payment():
    payment = Pix()
    payment_info = payment.create_payment(base_dir='../')
    
    assert 'bank_payment_id' in payment_info
    assert 'qrcode_path' in payment_info
    assert os.path.isfile(f'../static/img/{payment_info['qrcode_path']}.png')
