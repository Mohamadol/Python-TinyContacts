from mypackages.input_getter import *

class Contact:

    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        if len(name) < 3:
            raise Exception('The name must be atleast 3 characters. Please enter again')
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self,address):
        self.__address = address

    @address.deleter
    def address(self):
        self.__address = None

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self,phone):
        self.__telephone = phone

    @telephone.deleter
    def telephone(self):
        self.__telephone = None


       





class Contacts:

    def __init__(self):
        self.contacts = []
        

    def add_contact(self):

        ''''Prompts the user for the name, address and new contact. 
            Creates a new contact class with the user entered value and 
            appends to the list of contacts'''

        name = GetText('Enter the name:\n>')
        address = GetText('Enter the address:\n>')
        telephone = GetText('Enter the telephone number:\n>')
        #This line will raise an exception if less than 2 characters were entered for name
        self.contacts.append(Contact(name,address,telephone))
        return('{} was succesfully added'.format(name))


    def find_contact(self, entered_name):
        '''Accepts a name and search through the list of contacts 
            for a contact with a matching name
            Will raise exception if the contact does not exist'''
        entered_name = entered_name.strip()
        entered_name = entered_name.lower()
        found = None
        for contact in self.contacts:
            contact_name = ((contact.name).strip()).lower()
            if entered_name == contact_name :
                found = contact
                break
        if found is None:
            raise Exception('The contact does not exist')
        return found


    

