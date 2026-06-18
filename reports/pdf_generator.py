from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


class PDFGenerator:

    def generate_report(self, summary,insights, chart_path):

        doc = SimpleDocTemplate("sales_report.pdf")

        styles = getSampleStyleSheet()

        content = []
        
        content.append(
        Paragraph(
        f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
        styles["BodyText"]
                )
        )

        content.append(Spacer(1, 15))

        content.append(
            Paragraph("Sales Analytics Report", styles["Title"])
        )

        content.append(Spacer(1, 20))

        content.append(
        Paragraph(
        "Executive Summary",
        styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                f"""
                Total Sales: ₹{insights['total_sales']}<br/>
                Average Sales: ₹{insights['average_sales']:.2f}<br/>
                Top Category: {insights['top_category']}
                """,
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 15))

        content.append(
            Paragraph("Statistical Summary", styles["Heading2"])
        )

        for metric, value in summary.items():

            content.append(
                Paragraph(
                    f"<b>{metric.upper()}</b>:<br/>{value.to_string()}",
                    styles["BodyText"]
                )
            )

            content.append(Spacer(1, 10))

        content.append(
            Paragraph("Sales By Category Chart", styles["Heading2"])
        )

        content.append(Image(chart_path, width=400, height=250))

        doc.build(content)

        print("PDF Report Generated Successfully!")