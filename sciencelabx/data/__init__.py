import pandas as pd

class Data:

    def __init__(self, data: pd.DataFrame, show_info: bool = True):
        self.data = data
        if data is not None:
            self._numerical_cols = data.select_dtypes(include=["int", "float"]).columns.tolist()
            self._categorical_cols = data.select_dtypes(include=["object"]).columns.tolist()
        else:
            print("No data provided")

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


    def summary_data():
        pass
