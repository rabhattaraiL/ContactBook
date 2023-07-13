USE python
GO
CREATE PROCEDURE spCreateTableAddressBook
AS
BEGIN
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name='AddressBook')
    CREATE TABLE AddressBook (
        id INT IDENTITY(1,1) PRIMARY KEY,
        first_name NVARCHAR(20), 
        last_name NVARCHAR(20)
    )
END
