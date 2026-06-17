import matplotlib.pyplot as plt

class ChartGenerator:

    def sales_by_category_chart(self, category_sales):

        plt.figure(figsize=(8, 5))

        category_sales.plot(kind="bar")

        plt.title("Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")

        plt.tight_layout()

        plt.savefig("sales_by_category.png")

        plt.close()

        print("Chart saved successfully!")