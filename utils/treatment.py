class Treat:
    def __init__(self, df, int_columns, float_columns, str_columns):
        """
        simple class to change columns to respect datatypes
        """
        self.df = df
        self.int_columns = int_columns
        self.float_columns = float_columns
        self.str_columns = str_columns
        self.treat_int_columns()
        self.treat_str_columns()
        self.treat_float_columns()

    def treat_int_columns(self):
        for i in self.int_columns:
            if i in self.df.columns:  
                if self.df[i].dtype == int:
                    pass
                else:
                    self.df[i] = self.df[i].fillna(0)
                    self.df[i] = self.df[i].astype(int)
            else:
                pass
        
    def treat_str_columns(self):
        for i in self.str_columns:
            if i in self.df.columns:
                self.df[i] = self.df[i].astype(str)
                self.df[i] = self.df[i].str.lower()
            else: 
                pass

    def treat_float_columns(self):
        for i in self.float_columns:
            if i in self.df.columns:
                self.df[i] = self.df[i].fillna(0)
                self.df[i] = self.df[i].astype(float)
            else:
                pass
