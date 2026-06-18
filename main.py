from data_sources.reader_factory import ReaderFactory
from analysis.statistics import StatisticsAnalyzer
from charts.chart_generator import ChartGenerator
from reports.pdf_generator import PDFGenerator

file_path = "sample_data/sales.db"

reader = ReaderFactory.get_reader(file_path)

df = reader.load_data(file_path)

analyzer = StatisticsAnalyzer()

summary = analyzer.generate_summary(df)

insights = analyzer.generate_insights(df)

print("\n===== INSIGHTS =====")
print(insights)

category_sales = analyzer.sales_by_category(df)

chart = ChartGenerator()
chart.sales_by_category_chart(category_sales)

pdf = PDFGenerator()

pdf.generate_report(
    summary,
    insights,
    "sales_by_category.png"
)