idade = 17
acompanhado = True

if idade >= 18:
    print('Você é maior de idade. Pode entrar!')
elif idade < 18 or acompanhado:
    print('Você é menor de idade, mas está acompanhado. pode entrar!') # Bloco que será executado
else:
    print('Você é menor de idade. Não pode entrar!')

# conjunção (e) = and
# disjunção (ou) = or