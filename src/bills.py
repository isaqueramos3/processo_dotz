from utils.utils import file_to_df
from utils.treatment import Treat
from utils.mysql import Mysql
import pandas as pd

def Bills():
    # columns
    str_columns = ["tube_assembly_id", "component_id_1", "component_id_2", "component_id_3", "component_id_4", "component_id_5", "component_id_6", "component_id_7", "component_id_8"]
    int_columns = ["quantity_1", "quantity_2", "quantity_3", "quantity_4", "quantity_5", "quantity_5", "quantity_7", "quantity_8"]
    float_columns = [""]

    # read df from download
    prefix = "bills/"
    df = file_to_df(prefix)

    # treatment
    treatment_class = Treat(df, int_columns, float_columns, str_columns)
    df_bills = treatment_class.df

    # to sql
    database_connection = Mysql()
    df_bills.to_sql(con=database_connection, name='bills_of_materials', if_exists='append')

if __name__=="__main__":
    Bills()