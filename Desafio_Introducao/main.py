contacts = []

def show_menu():
    print('********************************')
    print('*                              *')
    print('*      LISTA DE CONTATOS       *')
    print('*                              *')
    print('*  1 - Visualizar contatos     *')
    print('*  2 - Visualizar favoritos    *')
    print('*  3 - Adicionar contato       *')
    print('*  4 - Editar contato          *')
    print('*  5 - Excluir contato         *')
    print('*                              *')
    print('********************************\n')

    option = int(input('Escolha uma opção: '))

    if option == 1:
        show_all()
    elif option == 2:
        show_favorites()
    elif option == 3:
        create()
    elif option == 4:
        update_contact()
    elif option == 5:
        delete()

def delete():
    print('\n***** EXCLUIR CONTATO *****\n')
    try:
        pos = -1
        search_name = input('Informe o nome do contato: ')
        for index, contact in enumerate(contacts):
            for value in contact.values():
                if search_name == value:
                    pos = index
        if pos == -1:
            print('Contato não encontrado!')
        else:
            contacts.pop(pos)
            print('\nContato editado com sucesso!')

    except Exception as e:
        print('Ocorreu um erro ao editar contato!')


def show_all():
    if len(contacts) == 0:
        print('Nenhum contato registrado!')
    else:
        print('\n***** TODOS OS CONTATOS *****\n')
        for contact in contacts:
            print(f'Nome: {contact['name']}')
            print(f'Email: {contact['email']}')
            print(f'Telefone: {contact['phone']}')
            if contact['favorite']:
                print(f'Favorito: Sim')
            else:
                print(f'Favorito: Não')
            print('-----------------------------')

def show_favorites():
    print('\n***** Contatos favoritos *****')
    for contact in contacts:
        if contact['favorite']:
            print(f'Nome: {contact['name']}')
            print(f'Email: {contact['email']}')
            print(f'Telefone: {contact['phone']}')
            print('-----------------------------')

def update_contact():
    print('\n***** Editar contato *****')
    try:
        pos = -1
        search_name = input('Informe o nome do contato: ')
        for index, contact in enumerate(contacts):
            for value in contact.values():
                if search_name == value:
                    pos = index
        if pos == -1:
            print('Contato não encontrado!')
        else:
            print()
            contacts[pos]['name'] = input('Novo nome: ')
            contacts[pos]['email'] = input('Novo email: ')
            contacts[pos]['phone'] = input('Novo telefone: ')
            print('************************')
            print('*   1 = Favorito       *')
            print('*   0 = Não favorito   *')
            print('************************')
            contacts[pos]['favorite'] = bool(int(input('Favorito: ')))

            print('\nContato editado com sucesso!')

    except Exception as e:
        print('Ocorreu um erro ao editar contato!')
         

def create():
    print('\n***** Adicionar contato *****')

    try:
        name = input('Nome: ')
        phone = input('Telefone: ')
        email = input('Email: ')
        print('************************')
        print('*   1 = Favorito       *')
        print('*   0 = Não favorito   *')
        print('************************')
        favorite = bool(int(input('Favorito: ')))

        contact = {
            'name': name,
            'email': email,
            'phone': phone,
            'favorite': favorite
        }

        contacts.append(contact)

    except Exception as e:
        print('Ocorreu um erro!')

if __name__ == '__main__':
    while True:
        show_menu()


