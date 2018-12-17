import pickle
from Contacts import *
from mypackages.input_getter import *


menue = 'Main Page\n1-New Contact\n2-Find Contact\n3-Edit Contact\n4-Exit\n'
file_name = 'contacts.pickle'
options = 4



def save_contacts(file_name, data):
    with open(file_name, 'wb') as output_file:
        pickle.dump(data, output_file)


def load_contacts(file_name):
    global contacts
    with open(file_name, 'rb') as input_file:
        contacts = pickle.load(input_file)


try:
    load_contacts(file_name=file_name)
except:
    contacts = Contacts()


def find_contact(name):
    try:
        contact = contacts.find_contact(name)
        return contact
    except Exception as error:
        print(error)
        return None
        

def edit_contact(name):
        contact = find_contact(name)
        if contact is None:
            return 
        print('Name = {}'.format(contact.name))
        tmp = GetText('Enter new name or . to keep the old value: \n>')
        if tmp != '.':
            contact.name = tmp
            print('Updated the name to {}'.format(contact.name))
        print('Address = {}'.format(contact.address))
        tmp = GetText('Enter new address or . to keep the old value: \n>')
        if tmp != '.':
            contact.address = tmp
            print('Updated the address to {}'.format(contact.address))
        print('Telephone = {}'.format(contact.telephone))
        tmp = GetText('Enter telephone name or . to keep the old value:\n> ')
        if tmp != '.':
            contact.telephone = tmp
            print('Updated the telephone to {}'.format(contact.telephone))


while True:
    print(menue)
    command = GetInt('>',1,options)
    if command == 1:
        result = contacts.add_contact()
        print(result)
    elif command == 2:
        contact = find_contact(GetText('Who are you looking for?\n>'))
        if contact != None:
            print('{}   address:{}    Phone:{}\n'.format(contact.name, contact.address, contact.telephone))
    elif command == 3:
       edit_contact(GetText('What is the name of the contact you are trying to edit?\n>'))
    elif command == 4:
        save_contacts(file_name=file_name, data=contacts)
        break



