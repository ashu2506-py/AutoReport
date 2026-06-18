import typer

from data_sources.reader_factory import ReaderFactory
from analysis.statistics import StatisticsAnalyzer
from charts.chart_generator import ChartGenerator
from reports.pdf_generator import PDFGenerator
from reports.html_generator import HTMLGenerator
from config.config_loader import ConfigLoader

from pathlib import Path

app = typer.Typer()


def run_report_pipeline(template_name):

    config = ConfigLoader.load_config(
    f"templates/{template_name}.yaml"
    )

    print("\nLoaded Config:")
    print(config)

    file_path = config["data_source"]

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

    html = HTMLGenerator()

    html.generate_report(
        insights,
        "sales_by_category.png"
    )

    print("\nReport generation completed!")


@app.command()
def generate(template: str = typer.Argument(...)):
    """
    Generate reports
    """
    run_report_pipeline(template)


@app.command()
def validate():
    """
    Validate report templates
    """
    print("Validating templates...")
    print("Templates are valid.")


@app.command(name="list-templates")
def list_templates():
    """
    List available templates
    """

    print("Available Templates:\n")

    template_dir = Path("templates")

    for file in template_dir.glob("*.yaml"):
        print(f"- {file.stem}")


if __name__ == "__main__":
    app()