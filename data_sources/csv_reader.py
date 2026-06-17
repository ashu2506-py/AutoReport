import pandas as pd

class CSVReader:

    def load_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            return df

        except Exception as e:
            print(f"Error reading CSV: {e}")
            return None