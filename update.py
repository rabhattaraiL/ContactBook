class UpdateData():
    def __init__(self, cursor, contact_id, update_field, column_to_update, table_to_update):
        update_user_query = f"UPDATE {table_to_update} SET {column_to_update} = '{update_field}' WHERE contact_id = '{contact_id}'"
        cursor.commit(update_user_query)
        print('\n***********Contact information has been updated !!! ***********')