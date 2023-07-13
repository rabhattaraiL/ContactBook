class InsertData():
    # Insert data into the ContactTable
    def __init__(self, cursor, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        
        insert_query_ContactTable = f"INSERT INTO ContactTable VALUES ('{self.first_name}', '{self.last_name}', '{self.email}', '{self.phone_number}')"
        cursor.execute(insert_query_ContactTable)
        cursor.commit()

        contact_id = cursor.execute("SELECT SCOPE_IDENTITY()").fetchone()[0]
        
        addressbook_input = ''
        while addressbook_input not in ['y', 'n']:
            addressbook_input = input("\nDo you want to add the contact person address ? If 'yes' enter 'y', If 'no' enter 'n': ")
            if addressbook_input not in ['y', 'n']:
                print('Invalid input !!! Please enter from given option')
            
            
        if addressbook_input.lower()  == 'y':
            street_address = input('Enter street address of contact: ').replace("'", "''").capitalize()
            city = input('Enter city of contact: ').replace("'", "''").capitalize()
            state = input('Enter state of contact: ').replace("'", "''").capitalize()
            postal_code = input('Enter postal code of contact: ').replace("'", "''")
            country = input('Enter country of contact: ').replace("'", "''").capitalize()
            self.insert_data_into_AddressBook(cursor= cursor, contact_id=contact_id, street_address=street_address, city=city, state=state, postal_code=postal_code, country=country)
        
        elif addressbook_input.lower()  == 'n':
            self.insert_data_into_AddressBook(cursor= cursor, contact_id=contact_id, street_address='', city='', state='', postal_code='', country='')

        notetable_input = ''
        while notetable_input not in ['y', 'n']:
            notetable_input = input("\nDo you want to add some notes of the contact person ? If 'yes' enter 'y', If 'no' enter 'n': ")        
            if notetable_input not in ['y', 'n']:
                print('Invalid input !!! Please enter from given option')
        
        if notetable_input.lower()  == 'y':
            note = input('Enter some notes: ').replace("'", "''")
            self.insert_data_into_NoteTable(cursor= cursor, contact_id=contact_id, note=note)
        
        elif notetable_input.lower()  == 'n':
            self.insert_data_into_NoteTable(cursor= cursor, contact_id=contact_id, note='')
        

    # Insert data into the AddressBook
    def insert_data_into_AddressBook(self, cursor, contact_id, street_address, city, state, postal_code, country):
        insert_query_addressbook = f"INSERT INTO AddressBook VALUES ('{contact_id}', '{street_address}', '{city}', '{state}', '{postal_code}', '{country}')"
        cursor.execute(insert_query_addressbook)
        cursor.commit()

    # Insert data into the NoteTable
    def insert_data_into_NoteTable(self, cursor, contact_id, note):
        insert_query_notetable = f"INSERT INTO NoteTable VALUES ('{contact_id}', '{note}')"
        cursor.execute(insert_query_notetable)
        cursor.commit()
        