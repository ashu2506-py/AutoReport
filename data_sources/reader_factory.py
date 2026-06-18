from data_sources.csv_reader import CSVReader
from data_sources.excel_reader import ExcelReader
from data_sources.json_reader import JSONReader
from data_sources.sqlite_reader import SQLiteReader
from data_sources.api_reader import APIReader


class ReaderFactory:

    @staticmethod
    def get_reader(file_path):

        if file_path.endswith(".csv"):
            return CSVReader()

        elif file_path.endswith(".xlsx"):
            return ExcelReader()
        
        elif file_path.endswith(".json"):
            return JSONReader()

        
        elif file_path.endswith(".db"):
            return SQLiteReader()
        
        elif file_path.startswith("http"):
            return APIReader()

        else:
            raise ValueError(
                f"Unsupported file type: {file_path}"
            )