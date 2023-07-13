class DeleteData():
    def __init__(self, cursor, contact_id):
        result = cursor.execute(f"SELECT contact_id FROM ContactTable WHERE contact_id = '{contact_id}'").fetchone()
        if result is None:
            print('Cannot DELETE the contact !!! The contact does not exist in your system !!!\n')
        else:
            delete_user_query = f"DELETE FROM ContactTable WHERE contact_id = '{contact_id}'"
            cursor.execute(delete_user_query)
            cursor.commit()
            print(f"\n*********** Details deleted for the contact ***********")