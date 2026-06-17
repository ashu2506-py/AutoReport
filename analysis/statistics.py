import pandas as pd

class StatisticsAnalyzer:

    def generate_summary(self, df):

        numeric_columns = df.select_dtypes(include='number')

        summary = {
            "mean": numeric_columns.mean(),
            "median": numeric_columns.median(),
            "std": numeric_columns.std(),
            "min": numeric_columns.min(),
            "max": numeric_columns.max()
        }
        
        return summary
        
    def sales_by_category(self, df):

        result = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

        return result

        