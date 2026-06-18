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
