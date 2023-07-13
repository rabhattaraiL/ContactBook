import re
from prettytable import PrettyTable

class ValidationFields:
    
    @staticmethod
    def email_validation():
        email = input('Enter email of contact (or leave blank): ')
        while email and not re.match('^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("Invalid email id !!! Please enter a valid email id")
            email = input('Enter email of contact (or leave blank): ')
        return email
    
    @staticmethod
    def display_records(row, details_to_show):
        if details_to_show == 'ContactTable':
            print('Contact id: ', row[0])
            print('First name: ', row[1])
            print('Last name: ', row[2])
            print('Email: ', row[3])
            print('Phone number: ', row[4])
        if details_to_show == 'AddressBook':
            print('Address id of contact: ', row[0])
            print('Contact id: ', row[1])
            print('Street address: ', row[2])
            print('City: ', row[3])
            print('State: ', row[4])
            print('Postal code: ', row[5])
            print('Country: ', row[6])
        if details_to_show == 'NoteTable':
            print('Note id of contact: ', row[0])
            print('Contact id: ', row[1])
            print('Note: ', row[2])

    @staticmethod
    def display_records_in_tabular_form(cursor, view_contact_name = None):
        cursor.execute(f"""
                               SELECT 
                                    ct.contact_id, ct.first_name, ct.last_name, ct.email, ct.phone_number,
                                    ab.street_address, ab.city, ab.state, ab.postal_code, ab.country,
                                    nt.note 
                               FROM ContactTable ct 
                               INNER JOIN NoteTable nt  
                               ON nt.contact_id = ct.contact_id 
                               INNER JOIN AddressBook ab
                               ON ab.contact_id = ct.contact_id
        """)
        column_names = [column[0] for column in cursor.description]
        table = PrettyTable(column_names)
        for row in cursor.fetchall():
            table.add_row(row)
        table.align = 'l'
        print(table)