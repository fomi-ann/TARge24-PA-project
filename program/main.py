from program.client_data import client_db_mgmt
from client_data import client_data
from client_data import Client

if __name__ == '__main__':
    client_db_mgmt.read_db()
    client_data.user_operation_check()