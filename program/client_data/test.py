import client_data
import client_db_mgmt
import csv
from program.client_data.registeredClient import RegisteredClient

if __name__ == '__main__':
    with open("registeredClientsTest.csv", "a", newline="") as db:
        csv_file = csv.writer(db,delimiter=":")
        trg = RegisteredClient("739201856473928501","Kevin", "Randla")
        trg.client_id = "newId"
        print([trg.client_id,trg.bank_account,trg.get_full_name(), trg.completed_orders, trg.pending_orders])
        csv_file.writerows([trg.client_id,trg.bank_account,trg.get_full_name(), trg.completed_orders, trg.pending_orders])
    # print(client_db_mgmt.read_db())
    # client_data.user_operation_check()

