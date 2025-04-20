import client_data
import client_database_mgmt

if __name__ == '__main__':
    first_name, middle_name, last_name = client_data.create_name()
    print(first_name, middle_name, last_name)
    bank_acc = client_data.get_user_bank_account()
    print(bank_acc)

