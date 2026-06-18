from analysis.statistics import StatisticsAnalyzer
from data_sources.csv_reader import CSVReader


def test_summary_generation():

    reader = CSVReader()

    df = reader.load_data(
        "sample_data/sales.csv"
    )

    analyzer = StatisticsAnalyzer()

    summary = analyzer.generate_summary(df)

    assert summary is not None
    
def test_mean_exists():

    reader = CSVReader()

    df = reader.load_data(
        "sample_data/sales.csv"
    )

    analyzer = StatisticsAnalyzer()

    summary = analyzer.generate_summary(df)

    assert "mean" in summary

def test_generate_insights():

    reader = CSVReader()

    df = reader.load_data(
        "sample_data/sales.csv"
    )

    analyzer = StatisticsAnalyzer()

    insights = analyzer.generate_insights(df)

    assert insights["total_sales"] > 0

def test_sales_by_category():

    reader = CSVReader()

    df = reader.load_data(
        "sample_data/sales.csv"
    )

    analyzer = StatisticsAnalyzer()

    category_sales = analyzer.sales_by_category(df)

    assert len(category_sales) > 0