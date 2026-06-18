from jinja2 import Environment
from jinja2 import FileSystemLoader


class HTMLGenerator:

    def generate_report(
        self,
        insights,
        chart_path
    ):

        env = Environment(
            loader=FileSystemLoader("templates")
        )

        template = env.get_template(
            "report_template.html"
        )

        html = template.render(
            insights=insights,
            chart_path=chart_path
        )

        with open(
            "sales_report.html",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        print("HTML Report Generated Successfully!")