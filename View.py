﻿import Text


def menu() -> int:
    print(Text.main_menu[0])
    for i in range(1, len(Text.main_menu)):
        print(f'\t{i}. {Text.main_menu[i]}')

    while True:
        select = input(Text.select_menu)
        if select.isdigit() and 0 < int (select) < int(len(Text.main_menu)):
            return int(select)
        print(Text.input_error)


def show_contacts(book: dict[int: dict[str, str]], message):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for contact in book.values():
            max_name.append(len(contact.get('name')))
            max_phone.append(len(contact.get('phone')))
            max_comment.append(len(contact.get('comment')))

        size_name = max(max_name)
        size_phone = max(max_phone)
        size_comment = max(max_comment)
        print('\n' + '=' * (size_name + size_phone + size_comment + 7))
        for index, contact in book.items():
            print(f'{index:>3}. {contact.get("name"):<{size_name}} {contact.get("phone"):<{size_phone}} {contact.get("comment"):<{size_comment}}')
        print('=' * (size_name + size_phone + size_comment + 7) + '\n')
    else:
        print_message(message)
def show_del(book: dict[int: dict[str, str]], message):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for contact in book.values():
            max_name.append(len(contact.get('name')))
            max_phone.append(len(contact.get('phone')))
            max_comment.append(len(contact.get('comment')))

        size_name = max(max_name)
        size_phone = max(max_phone)
        size_comment = max(max_comment)
        print('\n' + '=' * (size_name + size_phone + size_comment + 7))
        for index, contact in book.items():
            print(f'Контакт {index:>3}. {contact.get("name"):<{size_name}} {contact.get("phone"):<{size_phone}} {contact.get("comment"):<{size_comment}} был удален')
        print( '=' * (size_name + size_phone + size_comment + 7) + '\n')
    else:
        print_message(message)
def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')
             
def add_contact():
    new = {}
    for key, value in Text.new_contact.items():
        new[key] = input(value)
    return new


def search_word() -> str:
    return input(Text.search_word)
