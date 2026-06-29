"""
chart_generator.py

Generates revenue charts using matplotlib.
"""

import os
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self, df):
        self.df = df

    # ----------------------------------------
    # Revenue by Category
    # ----------------------------------------

    def revenue_by_category(self):

        # Create output folder if it doesn't exist
        os.makedirs("output", exist_ok=True)

        revenue = (
            self.df.groupby("category")["final_price"]
            .sum()
        )

        plt.figure(figsize=(8, 5))

        revenue.plot(kind="bar")

        plt.title("Revenue by Category")

        plt.xlabel("Category")

        plt.ylabel("Revenue")

        plt.tight_layout()

        plt.savefig("output/revenue_chart.png")

        plt.close()

        print("\nRevenue chart saved to output/revenue_chart.png")