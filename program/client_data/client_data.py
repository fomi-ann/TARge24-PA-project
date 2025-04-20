from Client import Client

def save_client(client:Client):
    """Saves client information to registeredClients.csv"""
    pass

def init_client(user_id):
    """Creates a registered client subclass for the current session."""
    pass

def create_client_id() -> str:
    """
    Creates a random string 8 characters long.
    1. Creates 8 random single digit numbers
    2. Adds them together as a string
    3. Checks if string is in registeredClients.csv
    4. If string is in file, runs the function again
    5. Returns the string if it is not in file
    """
    pass

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
                name.insert(0, "")
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

def get_user_bank_account():
    """Asks the user for a valid bank account and returns it."""
    bank_acc = input("Please insert your bank account numbers:")
    while True:
        if check_bank_acc_for_letters(bank_acc):
            bank_acc = input("Your bank account cannot contain letters or spaces. Please try again: ")
        elif not len(bank_acc) == 16:
            bank_acc = input("Your bank account must contain 16 numbers. Please insert your bank account again:")
        else:
            return bank_acc

