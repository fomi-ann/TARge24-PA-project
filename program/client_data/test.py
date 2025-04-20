import client_data
import client_db_mgmt

if __name__ == '__main__':
    client_data.user_operation_check()
    first_name, middle_name, last_name = client_data.create_name()
    print(first_name, middle_name, last_name)
    bank_acc = client_data.get_user_bank_account()
    print(bank_acc)

