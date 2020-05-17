from utils.utils import file_to_df
from utils.treatment import Treat
from utils.mysql import Mysql
import pandas as pd

def Price():
    # columns
    str_columns = ["tube_assembly_id", "supplier", "quote_date", "bracket_pricing"]
    int_columns = ["annual_usage", "min_order_quantity", "quantity"]
    float_columns = ["cost"]

    # read file from download
    prefix = "price/"
    df = file_to_df(prefix)

    # treatment
    treatment_class = Treat(df, int_columns, float_columns, str_columns)
    df_price = treatment_class.df

    database_connection = Mysql()
    df_price.to_sql(con=database_connection, name='price_quote', if_exists='append')

if __name__=="__main__":
    Price()