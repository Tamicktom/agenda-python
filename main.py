"""
- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato
"""

from typing import List
from uuid import uuid4
from validations import format_cellphone


def random_uuid():
    return str(uuid4())


class Contact:
    id: str = random_uuid()
    name: str = ''
    phone: str = ''
    email: str = ''
    favorite: bool = False

    def __init__(self, name: str, phone: str, email: str, favorite=False):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite


contacts: List[Contact] = []


def create_contact():
    empty_space(2)
    print('Digite as informações do contato')
    name = input('Nome: ')
    phone = input('Telefone: ')
    email = input('Email: ')
    favorite = input('Favorito? (S/N): ').upper() == 'S'

    contact = Contact(name, phone, email, favorite)
    contact.phone = format_cellphone(contact.phone)
    contacts.append(contact)


def delete_contact(name):
    empty_space(2)
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        print('Contato removido com sucesso')
    else:
        print('Contato não encontrado')


def edit_contact(name):
    empty_space(2)
    contact = search_contact(name)
    if contact:
        print('Digite as informações do contato')
        contact.name = input(f'Nome ({contact.name}): ') or contact.name
        contact.phone = input(f'Telefone ({contact.phone}): ') or contact.phone
        contact.email = input(f'Email ({contact.email}): ') or contact.email
        contact.favorite = input(
            f'Favorito? (S/N) ({contact.favorite}): ').upper() == 'S'
        contact.phone = format_cellphone(contact.phone)
    else:
        print('Contato não encontrado')


def search_contact(name):
    for contact in contacts:
        if contact.name == name:
            return contact
    return None


def list_contacts():
    for contact in contacts:
        print(f'Nome: {contact.name}')
        print(f'Telefone: {contact.phone}')
        print(f'Email: {contact.email}')
        print(f'Favorito: {"Sim" if contact.favorite else "Não"}')
        print('---')


def list_favorites():
    for contact in contacts:
        if contact.favorite:
            print(f'Nome: {contact.name}')
            print(f'Telefone: {contact.phone}')
            print(f'Email: {contact.email}')
            print(f'Favorito: {"Sim" if contact.favorite else "Não"}')
            print('---')


def empty_space(lines: int = 1):
    for _ in range(lines):
        print()


def main():
    while True:
        empty_space(2)
        print('---' * 10)
        print('Agenda de contatos')
        print('1 - Adicionar contato')
        print('2 - Listar contatos')
        print('3 - Editar contato')
        print('4 - Marcar/desmarcar contato como favorito')
        print('5 - Listar favoritos')
        print('6 - Apagar contato')
        print('0 - Sair')

        choice = input('Escolha uma opção: ')

        if choice == '1':
            create_contact()
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            name = input('Digite o nome do contato: ')
            edit_contact(name)
        elif choice == '4':
            name = input('Digite o nome do contato: ')
            contact = search_contact(name)
            if contact:
                contact.favorite = not contact.favorite
            else:
                print('Contato não encontrado')
        elif choice == '5':
            list_favorites()
        elif choice == '6':
            name = input('Digite o nome do contato: ')
            delete_contact(name)
        elif choice == '0':
            break
        else:
            print('Opção inválida')


_main_ = main()

if __name__ == '__main__':
    main()
