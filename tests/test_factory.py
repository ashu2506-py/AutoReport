from data_sources.reader_factory import ReaderFactory
from data_sources.csv_reader import CSVReader


def test_factory_returns_csv_reader():

    reader = ReaderFactory.get_reader(
        "sample_data/sales.csv"
    )

    assert isinstance(
        reader,
        CSVReader
    )

from data_sources.excel_reader import ExcelReader


def test_factory_returns_excel_reader():

    reader = ReaderFactory.get_reader(
        "sample_data/sales.xlsx"
    )

    assert isinstance(
        reader,
        ExcelReader
    )