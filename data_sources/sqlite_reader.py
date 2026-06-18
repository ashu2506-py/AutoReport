import sqlite3
import pandas as pd

from data_sources.base_reader import DataSource


class SQLiteReader(DataSource):

    def load_data(self, file_path):

        try:
            conn = sqlite3.connect(file_path)

            df = pd.read_sql_query(
                "SELECT * FROM sales",
                conn
            )

            conn.close()

            return df

        except Exception as e:
            print(f"SQLite Error: {e}")
            return None