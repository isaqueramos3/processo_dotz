import sqlalchemy
import pandas as pd
from utils.utils import yamlConfig

def Mysql():
    """
    connect to mysql in gcp
    """
    fp = yamlConfig()
    username = fp["mysql"]["username"]
    password = fp["mysql"]["password"]
    ip = fp["mysql"]["database_ip"]
    database = fp["mysql"]["database"]

    database_username = username
    database_password = password
    database_ip       = ip
    database_name     = database
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                format(database_username, database_password, 
                                                        database_ip, database_name))
    return database_connection