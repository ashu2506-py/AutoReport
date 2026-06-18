from data_sources.csv_reader import CSVReader


def test_csv_reader_loads_data():

    reader = CSVReader()

    df = reader.load_data(
        "sample_data/sales.csv"
    )

    assert df is not None
    assert len(df) > 0

def test_csv_contains_sales_column():

    reader = CSVReader()

    df = reader.load_data(
        "sample_data/sales.csv"
    )

    assert "Sales" in df.columns