try:
    numero = input('Digite um numero: ')
    divisao = 10 / numero
except TypeError as e:
    print('Divisão por 0!')

