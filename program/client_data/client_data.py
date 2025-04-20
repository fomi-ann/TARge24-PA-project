import client_db_mgmt


def check_numbers_in_name(name):
    """Checks if there are numbers in name."""
    return any(char.isdigit() for char in name)


def join_middle_names(name) -> list:
    """Joins multiple middle names.
    1. Saves all the string before last string and after first one
    2. Creates a new list containing the first name, empty string and last name
    3. Loops through and adds all the middle names into the value in the middle list
        Separates middle names with a - delimiter
    4. Removes the last delimiter
    :returns List of names
    """
    middle_names = name[1:-1]
    name_list = [name[0], "", name[-1]]
    for n in middle_names:
        name_list[1] += n + "-"
    name_list[1] = name_list[1][:-1]
    return name_list


def create_name():
    """Separates a user inputted name
    1. Takes input
    2. If there are numbers in the name or if the provided name is singular
        it asks the user for a valid input
    3. If the amount of inputted names are 2, the string is split and an empty string
        is put inside the 2nd index to account for no middle name input
    4. If the name amount is 3, the string is split and sent back
    5. If the name amount is more than 3, the string middle name is sent to join_middle_names method.
    """
    name = input("Please insert your name: ")
    while True:
        name_length_check = len(name.split())
        # name_check = name.split()
        # print(name_check, name_length_check , check_numbers_in_name(name), name_length_check < 1)
        if not check_numbers_in_name(name) and name_length_check > 1:
            if name_length_check == 2:
                name = name.split()
                print(name)
                name.insert(1, "")
                print(name)
            elif name_length_check == 3:
                name = name.split()
            else:
                name = name.split()
                name = join_middle_names(name)
            break
        else:
            name = input("Please enter a valid name: ")

    return name[0], name[1], name[2]


def check_bank_acc_for_letters(bank_acc):
    """Checks if the user inputted bank account has letters."""
    for digit in bank_acc:
        try:
            int(digit)
        except ValueError:
            return True
    return False


def get_user_bank_acc():
    """Asks the user for a valid bank account and returns it."""
    bank_acc = input("Please insert your bank account numbers:")
    while True:
        if check_bank_acc_for_letters(bank_acc):
            bank_acc = input("Your bank account cannot contain letters or spaces. Please try again: ")
        elif not len(bank_acc) == 16:
            bank_acc = input("Your bank account must contain 16 numbers. Please insert your bank account again:")
        else:
            return bank_acc


def get_user_data():
    """
    Asks the user their bank account and name.
    Returns a list with the following order [bank_account, first_name, middle_name, last_name]
    """
    first_name, middle_name, last_name = create_name()
    bank_acc = get_user_bank_acc()
    return [bank_acc, first_name, middle_name, last_name]


def user_input_control(user_input: str, correct_inputs: list) -> bool:
    """Checks if the user made a correct input from preset options."""
    if user_input in correct_inputs:
        return True
    return False

def user_operation_check() -> None:
    """Checks if the user wants to log in, register or continue as a guest."""
    correct_inputs = ["r", "register", "l", "login", "continue", "c"]
    while True:
        user_input = input("Do you want to register,login or continue as a guest?(r/l/c):").lower()
        if user_input_control(user_input, correct_inputs):
            ### RETURN VALUES HAVE TO BE CLIENT CLASS ###
            if user_input == correct_inputs[0:1]:
                # Client registration
                new_id = client_db_mgmt.create_client_id()
                client_db_mgmt.init_client(get_user_data(), new_id)
                return
            elif user_input == correct_inputs[2:3]:
                # Client login
                client_db_mgmt.init_client()
                return
            else:
                # Guest session
                client_db_mgmt.init_client(get_user_data())
                return
        else:
            print("You have inserted an invalid operation. Please select a valid one.")
