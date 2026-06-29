"""
sales_etl.py

Implements the Sales ETL Pipeline.
"""

import pandas as pd
import numpy as np

from src.base_etl import BaseETL
from src.report_generator import ReportGenerator
from src.csv_processor import CSVProcessor


class SalesETL(BaseETL):

    def __init__(self, file_path):
        super().__init__(file_path)

    # ---------------------------------------------------
    # Task 1 - Extract
    # ---------------------------------------------------

    def extract(self):
        """Load CSV file."""

        print("\nLoading sales data...\n")

        self.df = pd.read_csv(self.file_path)

        print("Data loaded successfully.")

    # ---------------------------------------------------
    # Task 1 - Validate
    # ---------------------------------------------------

    def validate(self):

        print("\n========== TASK 1 ==========")

        print("\nShape")
        print(self.df.shape)

        print("\nData Types")
        print(self.df.dtypes)

        print("\nNull Values")
        print(self.df.isnull().sum())

    # ---------------------------------------------------
    # Transform
    # ---------------------------------------------------

    def transform(self):

        self.calculate_final_price()

        self.comparison_filters()

        self.logical_filters()

        self.membership_filters()

        self.aggregation()

        self.string_operations()

        self.revenue_tier()

    # ---------------------------------------------------
    # Task 2
    # ---------------------------------------------------

    def calculate_final_price(self):

        print("\n========== TASK 2 ==========")

        self.df["final_price"] = (
            self.df["quantity"]
            * self.df["price"]
            * (1 - self.df["discount"])
        ).round(2)

        print(
            self.df[
                [
                    "order_id",
                    "customer",
                    "final_price"
                ]
            ]
        )

    # ---------------------------------------------------
    # Task 3
    # ---------------------------------------------------

# ---------------------------------------------------
# Task 3
# ---------------------------------------------------

def comparison_filters(self):

    print("\n" + "=" * 50)
    print("TASK 3 - COMPARISON OPERATORS")
    print("=" * 50)

    # final_price > 50000
    print("\n1. Orders with Final Price > 50000")

    high_value = self.df[self.df["final_price"] > 50000]

    print(high_value[
        [
            "order_id",
            "customer",
            "product",
            "final_price"
        ]
    ])

    # Region == South
    print("\n2. Orders from South Region")

    south_orders = self.df[self.df["region"] == "South"]

    print(south_orders[
        [
            "order_id",
            "customer",
            "region"
        ]
    ])

    # Quantity >=3 AND Electronics
    print("\n3. Electronics Orders with Quantity >= 3")

    electronics = self.df[
        (self.df["category"] == "Electronics")
        &
        (self.df["quantity"] >= 3)
    ]

    print(
        electronics[
            [
                "order_id",
                "customer",
                "product",
                "quantity"
            ]
        ]
    )

    # ---------------------------------------------------
    # Task 4
    # ---------------------------------------------------

# ---------------------------------------------------
# Task 4
# ---------------------------------------------------

def logical_filters(self):

    print("\n" + "=" * 50)
    print("TASK 4 - LOGICAL OPERATORS")
    print("=" * 50)

    # Electronics OR Furniture

    print("\n1. Electronics OR Furniture")

    data = self.df[
        (self.df["category"] == "Electronics")
        |
        (self.df["category"] == "Furniture")
    ]

    print(
        data[
            [
                "order_id",
                "product",
                "category"
            ]
        ]
    )

    # Discount NOT zero

    print("\n2. Discount NOT Zero")

    discount = self.df[
        self.df["discount"] != 0
    ]

    print(
        discount[
            [
                "order_id",
                "customer",
                "discount"
            ]
        ]
    )

    # Electronics AND (South OR East)

    print("\n3. Electronics in South/East with Discount")

    result = self.df[
        (self.df["category"] == "Electronics")
        &
        (
            (self.df["region"] == "South")
            |
            (self.df["region"] == "East")
        )
        &
        (self.df["discount"] > 0)
    ]

    print(
        result[
            [
                "order_id",
                "customer",
                "region",
                "discount"
            ]
        ]
    )

    # ---------------------------------------------------
    # Task 5
    # ---------------------------------------------------

  # ---------------------------------------------------
# Task 5
# ---------------------------------------------------

def membership_filters(self):

    print("\n" + "=" * 50)
    print("TASK 5 - MEMBERSHIP OPERATORS")
    print("=" * 50)

    # Customers

    print("\n1. Alice, Eve and Laura")

    customers = self.df[
        self.df["customer"].isin(
            [
                "Alice",
                "Eve",
                "Laura"
            ]
        )
    ]

    print(
        customers[
            [
                "order_id",
                "customer"
            ]
        ]
    )

    # NOT North or West

    print("\n2. NOT North or West")

    regions = self.df[
        ~self.df["region"].isin(
            [
                "North",
                "West"
            ]
        )
    ]

    print(
        regions[
            [
                "order_id",
                "customer",
                "region"
            ]
        ]
    )

    # ---------------------------------------------------
    # Task 6
    # ---------------------------------------------------

    def aggregation(self):
        pass

    # ---------------------------------------------------
    # Task 7
    # ---------------------------------------------------

    def string_operations(self):
        pass

    # ---------------------------------------------------
    # Task 8
    # ---------------------------------------------------

    def revenue_tier(self):
        pass

    # ---------------------------------------------------
    # Task 10
    # ---------------------------------------------------

    def report(self):

        report = ReportGenerator(self.df)

        report.print_summary()

        report.export_csv()

        report.plot_chart()

        csv_demo = CSVProcessor(self.file_path)

        csv_demo.walrus_operator()

        csv_demo.identity_operator()