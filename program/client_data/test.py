import client_data
import client_db_mgmt
import csv

from program.client_data.client_db_mgmt import init_client
from program.client_data.registeredClient import RegisteredClient

if __name__ == '__main__':
    client_db_mgmt.read_db()
    print(client_db_mgmt.client_db)
    print(client_db_mgmt.client_db == None)
    client_data.user_operation_check()

