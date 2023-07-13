CREATE PROCEDURE spCreateTableContactTable
AS
BEGIN
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='ContactTable')
    CREATE TABLE ContactTable (
        contact_id INT IDENTITY(1,1) PRIMARY KEY,
        first_name NVARCHAR(20), 
        last_name NVARCHAR(20),
		email NVARCHAR(50),
		phone_number NVARCHAR(15)
    )
END

CREATE PROCEDURE spCreateTableAddressBook
AS
BEGIN
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='AddressBook')
    CREATE TABLE AddressBook (
        address_id INT IDENTITY(1,1) PRIMARY KEY,
		contact_id INT FOREIGN KEY REFERENCES ContactTable(contact_id) ON DELETE CASCADE,
        street_address NVARCHAR(20), 
        city NVARCHAR(20),
		state NVARCHAR(50),
		postal_code NVARCHAR(15),
		country NVARCHAR(20),
    )
END

CREATE PROCEDURE spCreateTableNoteTable
AS
BEGIN
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='NoteTable')
    CREATE TABLE NoteTable (
        note_id INT IDENTITY(1,1) PRIMARY KEY,
        contact_id INT FOREIGN KEY REFERENCES ContactTable(contact_id) ON DELETE CASCADE,
        note NVARCHAR(100)
    )
END
