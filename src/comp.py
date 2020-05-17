from utils.utils import file_to_df
from utils.treatment import Treat
from utils.mysql import Mysql
import pandas as pd

def Comp():
    # columns
    str_columns = ["component_id", "component_type_id", "type", "connection_type_id", "outside_shape", "base_type", "groove","unique_feature","orientation"]
    int_columns = [""]
    float_columns = ["height_over_tube", "bolt_pattern_long", "bolt_pattern_wide", "base_diameter", "shoulder_diameter", "weight"]

    # read file from downloaded
    prefix = "comp/"
    df = file_to_df(prefix)
    # treatment
    treatment_class = Treat(df, int_columns, float_columns, str_columns)
    df_comp = treatment_class.df

    database_connection = Mysql()
    df_comp.to_sql(con=database_connection, name='comp_boss', if_exists='append')

if __name__=="__main__":
    Comp()