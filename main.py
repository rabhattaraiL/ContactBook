from dbconnect import DBConnectHelper
from insert import InsertData
from delete import DeleteData
from update import UpdateData
from validation import ValidationFields
import re
import msvcrt


def main():
    records_obj = DBConnectHelper()
    records_cursor = records_obj.conn.cursor()
    

    while True:
        print("""\n\nPlease select an option:\nPress '1' to add a new contact person\nPress '2' to update an existing user\nPress '3' to delete an exisitng user\nPress '4' to search an existing user\nPress '5' to view all contact detiails\nPress '6' to exit the system \n\n****************************** \n""")
        option_input = msvcrt.getwch()
        try:
            option = int(option_input)
            if option == 1:
                add_contact(records_cursor)
            elif option == 2:
                update_contact(records_cursor)
            elif option == 3:
                delete_contact(records_cursor)
            elif option == 4:
                search_contact(records_cursor)
            elif option == 5:
                display_contact(records_cursor)
            elif option == 6:
                exit()
            else:
                print('\nIncorrect input !!! Please enter valid number from the given options...')
        except ValueError:
            print('\nIncorrect input !!! Please enter valid number from the given options...')


def add_contact(cursor):
    print('\nYou can add a new contact !!!')

    first_name = input('\nEnter first name of contact: ').replace("'", "''").capitalize()
    if len(first_name) > 100:
        print("\nLength exceeds 100 characters !!! Please enter name within 100 characters")
        first_name = input('\nEnter first name of contact: ').capitalize()

    last_name = input('Enter last name of contact: ').replace("'", "''").capitalize()
    if len(last_name) > 100:
        print("\nLength exceeds 100 characters !!! Please enter name within 100 characters")
        last_name = input('\nEnter last name of contact: ').capitalize()

    email = ValidationFields.email_validation()

    phone_number = input('Enter phone number of contact: ')
    if phone_number:
        while not re.match('^\d{10}$', phone_number):
            print('\nInvalid phone number!!! The phone number should be 10 digits')
            phone_number = input('\nEnter phone number of contact: ')

    # Object of type InsertData
    InsertData(cursor = cursor, first_name=first_name, last_name=last_name, email=email, phone_number= phone_number)
    print(f"\n*********** Details saved for the contact ***********\n\n")

# Update a contact
def update_contact(cursor):    
    print("\nYou can update an existing contact person !!!")
    
    cursor.execute("SELECT contact_id, first_name, last_name FROM ContactTable")
    for row in cursor.fetchall():
        print(f"Contact id: {row[0]} || Name: {row[1]} {row[2]} ")
    
    update_contactid = int(input("\nWhich contact information do you want to update ? Please provide contact id and select 'enter': "))
    result = cursor.execute(f"SELECT contact_id FROM ContactTable WHERE contact_id = '{update_contactid}'").fetchone()
    
    if result is None:
        print('\nThe contact does not exist !!! Please enter an existing contact id')
    else:
        print('\nContact Details\n**********************')
        cursor.execute(f"SELECT * FROM ContactTable WHERE contact_id = '{update_contactid}'")
        for row in cursor.fetchall():
            ValidationFields.display_records(row, 'ContactTable')
        
        print('\nAddress Details\n**********************')
        cursor.execute(f"SELECT * FROM AddressBook WHERE contact_id = '{update_contactid}'")
        for row in cursor.fetchall():
            ValidationFields.display_records(row, 'AddressBook')
        
        print('\nNote Details\n**********************')
        cursor.execute(f"SELECT * FROM NoteTable WHERE contact_id = '{update_contactid}'")
        for row in cursor.fetchall():
            ValidationFields.display_records(row, 'NoteTable')

        while True:
            print("\nWhich information do you want to update ?\n1. Press 1 for changing Contact detail.\n2. Press 2 for changing Address detail.\n3. Press 3 for changing note detail.\n4. Press any other key to return.\n\n**********************\n")
            update_record_field = int(msvcrt.getwch())
            if update_record_field == 1:
                update_contact_detail(cursor, update_contactid)
            elif update_record_field == 2:
                update_address_detail(cursor, update_contactid)
            elif update_record_field == 3:
                update_note_detail(cursor, update_contactid)
            else:
                break

def update_contact_detail(cursor, contact_id):
    table_to_update = 'ContactTable'
    print('\nWhich value would you like to change ?\n1. Press 1 to change first name.\n2. Press 2 to change last name.\n3. Press 3 to change email address.\n4. Press 4 to change phone number.\n\n****************************** \n')
    update_contact_detail = int(msvcrt.getwch())
    while True:
        if update_contact_detail == 1:
            first_name = input('\nEnter first name of contact: ').replace("'", "''").capitalize()
            UpdateData(cursor, contact_id, first_name, 'first_name', table_to_update)
            break
        elif update_contact_detail == 2:
            last_name = input('\nEnter last name of contact: ').replace("'", "''").capitalize()
            UpdateData(cursor, contact_id, last_name, 'last_name', table_to_update)
            break
        elif update_contact_detail == 3:
            email = ValidationFields.email_validation()
            UpdateData(cursor, contact_id, email, 'email', table_to_update)
            break
        elif update_contact_detail == 4:
            phone_number = input('\nEnter phone number of contact: ')
            UpdateData(cursor, contact_id, phone_number, 'phone_number', table_to_update)
            break  
        else:
            print('\nPlease enter a valid option from the list !!!')
            break

def update_address_detail(cursor, contact_id):
    table_to_update = 'AddressBook'
    print('\nWhich value would you like to change ?\n1. Press 1 to change street name.\n2. Press 2 to change city name.\n3. Press 3 to change state name.\n4. Press 4 to change postal code.\n5. Press 5 to change country name\n')
    update_address_detail = int(msvcrt.getwch())
    while True:
        if update_address_detail == 1:
            street = input('\nEnter street name of contact: ').replace("'", "''").capitalize()
            UpdateData(cursor, contact_id, street, 'street_address', table_to_update)
            break
        elif update_address_detail == 2:
            city = input('\nEnter city name of contact: ').replace("'", "''").capitalize()
            UpdateData(cursor, contact_id, city, 'city', table_to_update)
            break
        elif update_address_detail == 3:
            state = input('\nEnter state of contact: ').replace("'", "''").capitalize()
            UpdateData(cursor, contact_id, state, 'state', table_to_update)
            break
        elif update_address_detail == 4:
            postal_code = input('\nEnter postal code of contact: ').replace("'", "''")
            UpdateData(cursor, contact_id, postal_code, 'postal_code', table_to_update)
            break
        elif update_address_detail == 5:
            country = input('\nEnter country name of contact: ').replace("'", "''").capitalize()
            UpdateData(cursor, contact_id, country, 'country', table_to_update)
            break
        else:
            print('\nPlease enter a valid option from the list !!!')
            break

def update_note_detail(cursor, contact_id):
    table_to_update = 'NoteTable'
    note = input('\nEnter some notes: ').replace("'", "''")
    UpdateData(cursor, contact_id, note, 'note', table_to_update)

# Delete a contact
def delete_contact(cursor):
    print("\nYou can delete an existing contact person !!!\nRecords currently present:")
    ValidationFields.display_records_in_tabular_form(cursor)
    contact_id = int(input("\nEnter the contact id of user you want to delete and select 'enter': "))
    DeleteData(cursor, contact_id)

# Search for a specific contact
def search_contact(cursor):
    print("\nYou can search for an existing contact person !!!")
    view_contact_name = input("\nEnter the contact first name: ").capitalize()
    result = cursor.execute(f"SELECT first_name FROM ContactTable WHERE first_name = '{view_contact_name}'").fetchone()
    
    if result is None:
        print('The contact does not exist !!! Please enter an existing contact person name.')
    else:
        print('\nContact Details\n**********************')
        cursor.execute(f"SELECT * FROM ContactTable WHERE first_name LIKE '{view_contact_name}%'")
        for row in cursor.fetchall():
            ValidationFields.display_records(row, 'ContactTable')

        print('\nAddress Details\n**********************')
        cursor.execute(f"""SELECT ab.address_id, ab.contact_id, ab.street_address, ab.city, 
                            ab.state, ab.postal_code, ab.country
                            FROM AddressBook ab 
                            INNER JOIN ContactTable ct 
                            ON ab.contact_id = ct.contact_id 
                            WHERE first_name LIKE '{view_contact_name}%'""")
        for row in cursor.fetchall():
            ValidationFields.display_records(row, 'AddressBook')
        
        print('\nNote Details\n**********************')
        cursor.execute(f"""SELECT nt.note_id, nt.contact_id, nt.note 
                            FROM NoteTable nt 
                            INNER JOIN ContactTable ct 
                            ON nt.contact_id = ct.contact_id 
                            WHERE first_name LIKE '{view_contact_name}%'""")
        for row in cursor.fetchall():
            ValidationFields.display_records(row, 'NoteTable')
    
# Display all contacts
def display_contact(cursor):
    print('\nRecords of all existing users')
    ValidationFields.display_records_in_tabular_form(cursor)

if __name__ == "__main__":
    main()     