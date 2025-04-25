import client_data
import client_db_mgmt

if __name__ == '__main__':
    print(client_db_mgmt.read_db())
    client_data.user_operation_check()

