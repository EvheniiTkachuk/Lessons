# Extend Phonebook application
# Functionality of Phonebook application:
# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program
# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application,
# else raise an error. After the user exits, all data should be saved to loaded JSON.



import json

default_phone_book = {
    '1': {'first_name': 'Bob', 'second_name': 'Fisher', 'city': 'Brussels'},
    '2': {'first_name': 'Peter', 'second_name': 'Griffin', 'city': 'Quahog'},
    '3': {'first_name': 'Bob', 'second_name': 'Fisher_1', 'city': 'Brussels_1'},
    '4': {'first_name': 'Bob', 'second_name': 'Fisher_1', 'city': 'Brussels_2'}
}

phone_book = default_phone_book.copy()

global_file_name = 'phone_book.json'


def add_record(file_name=global_file_name):
    try:
        print('Please Enter for record:')
        phone_number = input('Phone number: ')
        first_name = input('First name: ').title()
        second_name = input('Second name: ').title()
        city = input('City: ').title()
        phone_book[phone_number] = {'first_name': first_name, 'second_name': second_name, 'city': city}
        file_open_for_write(file_name)
        return True
    except:
        return False


def dell_record(file_name=global_file_name):
    try:
        print('Please Enter for delete:')
        key = input('Phone number: ')
        phone_book.pop(key)
        file_open_for_write(file_name)
        return True
    except:
        return False


def update_record(file_name=global_file_name):
    try:
        temp = dict(file_open_for_read())
        print('Please Enter for update:')
        phone_number = input('Phone number: ')
        first_name = input('First name: ').title()
        second_name = input('Second name: ').title()
        city = input('City: ').title()
        phone_book[phone_number] = {'first_name': first_name, 'second_name': second_name, 'city': city}
        file_open_for_write(file_name)
        return True
    except:
        return False


def search_by_first_name():
    search_name = input('Please, enter first name for search: ').title()
    temp = dict(file_open_for_read())
    search = dict()
    for key, val in phone_book.items():
        if val['first_name'] == search_name:
            search[key] = val
    if search:
        return search
    else:
        print('Phone number not found')
        return None


def search_by_second_name():
    search_second_name = input('Please, enter second name for search: ').title()
    temp = dict(file_open_for_read())
    search = dict()
    for key, val in phone_book.items():
        if val['second_name'] == search_second_name:
            search[key] = val
    if search:
        return search
    else:
        print('Phone number not found')
        return None


def search_by_full_name():
    search_name = input('Please, enter first name for search: ').title()
    search_second_name = input('Please, enter second name for search: ').title()
    temp = dict(file_open_for_read())
    search = dict()
    for key, val in default_phone_book.items():
        if val['first_name'] == search_name and val['second_name'] == search_second_name:
            search[key] = val
    if search:
        return search
    else:
        print('Phone number not found')
        return None


def search_by_telephone_number():
    search_number = input('Please, enter phone number for search: ')
    temp = dict(file_open_for_read())
    search = dict()
    if temp.get(search_number):
        search[search_number] = phone_book[search_number]
        return search
    else:
        print('Phone number not found')
        return search


def search_by_city():
    search_city = input('Please, enter city for search: ').title()
    temp = dict(file_open_for_read())
    search = dict()
    for key, val in default_phone_book.items():
        if val['city'] == search_city:
            search[key] = val
    if search:
        return search
    else:
        print('Phone number not found')
        return None


def exit_the_program():
    file_open_for_write()
    pass


def file_open_for_write(file_name='phone_book.json', create_dict=phone_book):
    with open(file_name, "w") as write_file:
        json.dump(create_dict, write_file)


def file_open_for_read(file_name='phone_book.json'):
    with open(file_name, "r") as read_file:
        temp = json.load(read_file)
    return temp


def print_all_items_in_dict():
    external = dict(file_open_for_read(global_file_name))
    print(f'\nFile name: {global_file_name}\n\nPhone:\t\t\tData:\n')
    print_external_item(external)


def print_external_item(external):
    for key_external, val_external in external.items():
        print(f'{key_external}: ', end='')
        print_inner_item(val_external)


def print_inner_item(val_external):
    flage = False
    for key_inner, val_inner in val_external.items():
        if flage:
            print(f'\t{key_inner}: {val_inner}')
        else:
            print(f'\t{key_inner}: {val_inner}')
        flage = True
    print('')


def print_res_search(search):
    try:
        print(f'Result search:')
        print_external_item(search)
    except AttributeError:
        print('Nothing found')


def print_switch(switch):
    print('')
    for key, val in switch.items():
        print(f'{key} - {val}')


def switch_menu_main(option):
    if option == '1':
        print_all_items_in_dict()
        input('Press any key for return to main menu...')
        return option
    elif option == '2':
        switch_search(option)
    elif option == '3':
        switch_edit_recording(option)
    elif option == '4':
        if input('\nWarning!!! All changes will be lost!!!\nAre you sure for set default dictionary? (Y/any key): ').upper() == 'Y':
            file_open_for_write()
            print('Dictionary is default')
        else:
            pass
    elif option == '5':
        print('\n\nThank you for use ◕‿◕\n')
        return 1


def switch_search(option):
    switcher_search = {
        1: 'Search by first name',
        2: 'Search by last name',
        3: 'Search by full name',
        4: 'Search by telephone number',
        5: 'Search by city or state',
        6: 'Back'
    }
    while True:
        print_switch(switcher_search)
        choice = input('\nEnter option >>> ')
        switch_extended_search(choice)
        if not switch_extended_edit(choice):
            return 0
        if input('\nFind something else? (Y/any key): ').upper() == 'Y':
            continue
        else:
            return 0


def switch_extended_search(option):
    if option == '1':
        print_res_search(search_by_first_name())
    elif option == '2':
        print_res_search(search_by_second_name())
    elif option == '3':
        print_res_search(search_by_full_name())
    elif option == '4':
        print_res_search(search_by_telephone_number())
    elif option == '5':
        print_res_search(search_by_city())
    elif option == '6':
        return 0


def check_successful_operation(result):
    if result:
        print('...Operation successful...')
    else:
        print('Error')


def switch_extended_edit(option):
    if option == '1':
        check_successful_operation(add_record())
    elif option == '2':
        check_successful_operation(dell_record())
    elif option == '3':
        check_successful_operation(update_record())
    elif option == '4':
        print_all_items_in_dict()
    elif option == '5':
        return 0


def switch_edit_recording(option):
    switcher_edit = {
        1: 'Add new entries',
        2: 'Delete a record for a given telephone number',
        3: 'Update a record for a given telephone number',
        4: 'Show phone book',
        5: 'Back'
    }
    while True:
        print_switch(switcher_edit)
        choice = input('\nEnter option >>> ')
        if not switch_extended_edit(choice):
            break
        if input('\nMore changes? (Y/any key): ').upper() == 'Y':
            continue
        else:
            break


def menu_main():
    switcher_main = {
        1: 'Show phone book',
        2: 'Search into phone book',
        3: 'Edit recordings',
        4: 'Set default dictionary',
        5: 'Close the program'
    }
    while True:
        print('\n\nMain menu:')
        print_switch(switcher_main)
        choice = input('\nEnter option >>> ')
        option = switch_menu_main(choice)
        if option:
            break


menu_main()

