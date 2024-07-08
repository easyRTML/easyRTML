import pandas as pd

class Processor:
    def __init__(self, **kwargs):
        """
        Initialize Processor class.
        Arguments:
        - file_name: str, name of the CSV file to process
        """
        self.df = pd.read_csv(kwargs.get('file_name'))
        self.calculate_feature_info(**kwargs)

    def clean_column(self, **kwargs):
        """
        Clean a column by converting to numeric and filling NaNs with mean.
        Arguments:
        - col_data: pd.Series, column data to clean
        Returns:
        - pd.Series, cleaned column data
        """
        col_data = pd.to_numeric(kwargs.get('col_data'), errors='coerce')
        col_data.fillna(col_data.mean(), inplace=True)
        return col_data

    def clean_data(self, **kwargs):
        """
        Clean all columns in the dataframe except 'label' and 'label_name'.
        Arguments:
        - kwargs: keyword arguments containing dataframe
        """
        for col_name in kwargs.get('columns', self.df.columns):
            if col_name not in kwargs.get('exclude', ['label', 'label_name']):
                self.df[col_name] = self.clean_column(col_data=self.df[col_name])


    def normalize_data(self, **kwargs):
        """
        Normalize the dataframe using calculated feature info.
        Arguments:
        - kwargs: keyword arguments containing dataframe and feature info
        Returns:
        - pd.DataFrame, normalized dataframe
        """
        normalized_df = pd.DataFrame({
            'label': self.df['label'], 
            'label_name': self.df['label_name']
        })
        for col_name in kwargs.get('columns', self.df.columns):
            if col_name not in kwargs.get('exclude', ['label', 'label_name']):
                A = self.feature_info[col_name]['A']
                B = self.feature_info[col_name]['B']
                normalized_df[col_name] = (self.df[col_name] - A) * B
        return normalized_df


  
