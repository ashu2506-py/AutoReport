import pandas as pd

from data_sources.base_reader import DataSource


class JSONReader(DataSource):

    def load_data(self, file_path):

        try:
            return pd.read_json(file_path)

        except Exception as e:
            print(f"JSON Error: {e}")
            return None