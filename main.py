from data_sources.csv_reader import CSVReader
from analysis.statistics import StatisticsAnalyzer
from charts.chart_generator import ChartGenerator
from reports.pdf_generator import PDFGenerator

reader = CSVReader()
df = reader.load_data("sample_data/sales.csv")

analyzer = StatisticsAnalyzer()

summary = analyzer.generate_summary(df)

print("\n===== SUMMARY =====")

for key, value in summary.items():
    print(f"\n{key.upper()}")
    print(value)

print("\n===== SALES BY CATEGORY =====")

category_sales = analyzer.sales_by_category(df)

print(category_sales)

chart = ChartGenerator()

chart.sales_by_category_chart(category_sales)

pdf = PDFGenerator()

pdf.generate_report(
    summary,
    "sales_by_category.png"
)

from data_sources.reader_factory import ReaderFactory


file_path = "sample_data/sales.db"

reader = ReaderFactory.get_reader(
    file_path   
)

df = reader.load_data(file_path)

print(df.head())

# import sqlite3
# import pandas as pd

# df = pd.read_csv("sample_data/sales.csv")

# conn = sqlite3.connect("sample_data/sales.db")

# df.to_sql(
#     "sales",
#     conn,
#     if_exists="replace",
#     index=False
# )

# conn.close()

# print("Database created!")  