from client_data import *
import client_db_mgmt
import csv
import pandas as pd

from program.clientData.client_db_mgmt import init_client
from program.clientData.registeredClient import RegisteredClient

if __name__ == '__main__':
    # df = pd.read_csv('registeredClientsTest.csv', delimiter=":")
    # for n in range(len(df)):
    #     print(df.iloc[n])
    #     if df.iloc[n]['client_id'] == "67752728":
    #         df.drop(df.index[n], inplace=True)
    #         df.to_csv('registeredClientsTest.csv', index= False, sep=":")
    #         break
    #
    # # print(df.loc[0])
    # # df.drop(df.index[2], inplace=True)
    # # df.to_csv('registeredClientsTest.csv', index = False)
    user_operation_check()

