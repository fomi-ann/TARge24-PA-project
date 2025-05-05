import random
import csv
import json
import pandas as pd

<<<<<<< Updated upstream:program/client_data/client_db_mgmt.py
from program.client_data.Client import Client
from program.client_data.guestClient import GuestClient
from program.client_data.registeredClient import RegisteredClient
=======
from program.clientData import Client
from program.clientData.guestClient import GuestClient
from program.clientData.registeredClient import RegisteredClient
>>>>>>> Stashed changes:program/clientData/client_db_mgmt.py

client_db = None


def database_init_check():
    """
    Checks if the client_db is a None type and exits the program if it is.
    """
    global client_db
    if client_db is None:
        print("Database failed to initialise. Ending program.")
        exit()


def read_db():
    """
    Reads the existing database into a variable.
    Returns nothing.
    Should be used at the start of a program.
    """
    global client_db
    with open("client_data/registeredClients.csv", "r") as db:
        client_db = list(csv.reader(db, delimiter=":"))
        # return client_db
    # with open("registeredClientsTest.csv", "r") as db:
    #     client_db = list(csv.reader(db, delimiter=":"))


def save_client_to_db(client: RegisteredClient):
    """Saves client information to database"""
    with open("client_data/registeredClients.csv", "a", newline="") as db:
        csv_file = csv.writer(db, delimiter=":")
        csv_file.writerow(client.get_client_data())


def load_user_data_from_db(user_id):
    """Returns a list of all the saved user data."""
    global client_db
    database_init_check()

    for client_data in client_db:
        if user_id in client_data:
            return client_data


def remove_client_from_db(client_id):
    """Removes the registered client from the database."""
    df = pd.read_csv('client_data/registeredClients.csv', delimiter=":")
    for n in range(len(df)):
        if df.iloc[n]['client_id'] == client_id:
            df.drop(df.index[n], inplace=True)
            df.to_csv('client_data/registeredClients.csv', index= False, sep=":")
            break


def init_client(user_data: list = None, user_id=None):
    """Creates a client subclass for the current program session and returns it.
    1. If the method recieves only a list of values, it initiates a guest client class.
    2. If it recieves only the user_id then it initialises the user from the database.
    3. If it recieves both, it initialises a new registered user for the session.
    """
    ### HAS TO RETURN THE CLIENT CLASS VALUES ###
    if user_id is None and user_data is not None:
        # Guest client initiation
        client = GuestClient(*user_data)
        return client
    elif user_id is not None and user_data is None:
        # Registered user initiation from database
        read_db()
        client_data = load_user_data_from_db(user_id)
        # Converts strings in client data to lists.
        for x in range(len(client_data)):
            try:
                client_data[x] = json.loads(client_data[x])
            except TypeError:
                pass
            except json.decoder.JSONDecodeError:
                pass

        # Checks if the user has a middle name
        split_name = client_data[1].split()
        print(split_name)
        if len(split_name) > 2:
            first_name = split_name[0]
            middle_name = split_name[1]
            last_name = split_name[2]
        else:
            first_name = split_name[0]
            middle_name = ""
            last_name = split_name[1]

        client = RegisteredClient(str(client_data[2]), first_name, last_name, middle_name)

        client.set_client_id(user_id)
        client.init_orders(client_data[3], client_data[4])

        return client
    else:
        # 1. New registered user initiation
        # 2. save to database
        # 3. print user_id for user
        client = RegisteredClient(*user_data)
        client.set_client_id(user_id)
        print(f"Your new id is: {client.get_client_id()}")
        save_client_to_db(client)
        return client


def create_client_id() -> str:
    """
    Creates a random string 8 characters long.
    1. Creates 8 random single digit numbers
    2. Adds them together as a string
    3. Checks if string is in registeredClients.csv(database is loaded at the start of the program)
    4. If string is in file, runs the function again
    5. Returns the string if it is not in file
    """
    global client_db

    new_id = ""
    for x in range(0, 8):
        new_id += str(random.randint(0, 9))

    database_init_check()

    if any(new_id in db for db in client_db):
        new_id = create_client_id()
        return new_id
    else:
        return new_id
