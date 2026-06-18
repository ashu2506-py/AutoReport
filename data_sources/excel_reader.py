import pandas as pd

from data_sources.base_reader import DataSource


class ExcelReader(DataSource):

    def load_data(self, file_path):

        try:
            return pd.read_excel(file_path)

        except Exception as e:
            print(f"Excel Error: {e}")
            return None