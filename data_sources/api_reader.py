import requests
import pandas as pd

from data_sources.base_reader import DataSource


class APIReader(DataSource):

    def load_data(self, url):

        try:
            response = requests.get(url)

            response.raise_for_status()

            data = response.json()

            return pd.DataFrame(data)

        except Exception as e:
            print(f"API Error: {e}")
            return None