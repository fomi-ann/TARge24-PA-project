import client_data
import client_db_mgmt
import csv
from program.client_data.registeredClient import RegisteredClient

if __name__ == '__main__':
    with open("registeredClientsTest.csv", "a", newline="") as db:
        csv_file = csv.writer(db,delimiter=":")
        trg = RegisteredClient("739201856473928501","Kevin", "Randla")
        trg.id = "newId"
        print(trg.get_client_data())
        csv_file.writerow(trg.get_client_data())
    # print(client_db_mgmt.read_db())
    # client_data.user_operation_check()

