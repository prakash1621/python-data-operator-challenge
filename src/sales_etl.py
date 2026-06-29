"""
sales_etl.py

Implements the Sales ETL Pipeline.
"""

import pandas as pd
import numpy as np
from src.chart_generator import ChartGenerator

from src.csv_processor import CSVProcessor


class SalesETL:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def run(self):
        print("=" * 60)
        print("Starting Sales ETL Pipeline")
        print("=" * 60)

        self.extract()
        self.validate()
        self.transform()
        self.report()

        print("=" * 60)
        print("Pipeline Completed Successfully")
        print("=" * 60)

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

        print(self.df[["order_id", "customer", "final_price"]])

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
        print(high_value[["order_id", "customer", "product", "final_price"]])

        # Region == South
        print("\n2. Orders from South Region")
        south_orders = self.df[self.df["region"] == "South"]
        print(south_orders[["order_id", "customer", "region"]])

        # Quantity >= 3 AND Electronics
        print("\n3. Electronics Orders with Quantity >= 3")
        electronics = self.df[
            (self.df["category"] == "Electronics") &
            (self.df["quantity"] >= 3)
        ]
        print(electronics[["order_id", "customer", "product", "quantity"]])

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
            (self.df["category"] == "Electronics") |
            (self.df["category"] == "Furniture")
        ]
        print(data[["order_id", "product", "category"]])

        # Discount NOT zero
        print("\n2. Discount NOT Zero")
        discount = self.df[self.df["discount"] != 0]
        print(discount[["order_id", "customer", "discount"]])

        # Electronics AND (South OR East) with Discount
        print("\n3. Electronics in South/East with Discount")
        result = self.df[
            (self.df["category"] == "Electronics") &
            (
                (self.df["region"] == "South") |
                (self.df["region"] == "East")
            ) &
            (self.df["discount"] > 0)
        ]
        print(result[["order_id", "customer", "region", "discount"]])

    # ---------------------------------------------------
    # Task 5
    # ---------------------------------------------------

    def membership_filters(self):
        print("\n" + "=" * 50)
        print("TASK 5 - MEMBERSHIP OPERATORS")
        print("=" * 50)

        # Specific customers
        print("\n1. Alice, Eve and Laura")
        customers = self.df[
            self.df["customer"].isin(["Alice", "Eve", "Laura"])
        ]
        print(customers[["order_id", "customer"]])

        # NOT North or West
        print("\n2. NOT North or West")
        regions = self.df[
            ~self.df["region"].isin(["North", "West"])
        ]
        print(regions[["order_id", "customer", "region"]])

    # ---------------------------------------------------
    # Task 6
    # ---------------------------------------------------

    def aggregation(self):
        print("\n" + "=" * 50)
        print("TASK 6 - AGGREGATION")
        print("=" * 50)

        # Total Revenue per Category
        print("\n1. Total Revenue per Category")
        self.category_revenue = self.df.groupby("category")["final_price"].sum()
        print(self.category_revenue)

        # Average Discount per Region
        print("\n2. Average Discount per Region")
        avg_discount = self.df.groupby("region")["discount"].mean()
        print(avg_discount)

        # Max & Min Final Price per Category
        print("\n3. Max and Min Final Price per Category")
        max_min = self.df.groupby("category")["final_price"].agg(["max", "min"])
        print(max_min)

    # ---------------------------------------------------
    # Task 7
    # ---------------------------------------------------

    def string_operations(self):
        print("\n" + "=" * 50)
        print("TASK 7 - STRING OPERATIONS")
        print("=" * 50)

        # Convert Product to Uppercase
        self.df["product_upper"] = self.df["product"].str.upper()
        print("\nProducts in Uppercase")
        print(self.df[["product", "product_upper"]])

        # Customers starting with vowel
        print("\nCustomers Starting with Vowel")
        vowels = self.df[
            self.df["customer"].str.startswith(("A", "E", "I", "O", "U"))
        ]
        print(vowels[["customer"]])

        # Products containing 'a'
        count = self.df["product"].str.contains("a", case=False).sum()
        print(f"\nProducts containing letter 'a': {count}")

    # ---------------------------------------------------
    # Task 8
    # ---------------------------------------------------

    def revenue_tier(self):
        print("\n" + "=" * 50)
        print("TASK 8 - REVENUE TIER")
        print("=" * 50)

        self.df["revenue_tier"] = np.where(
            self.df["final_price"] >= 100000,  "High",
            np.where( self.df["final_price"] >= 20000,  "Medium",   "Low"))

        print(self.df[["customer", "final_price", "revenue_tier"]])

    # ---------------------------------------------------
    # Task 10 - Report
    # ---------------------------------------------------

    def report(self):
        print( "\n" + "=" * 40 )
        print( "      SALES SUMMARY REPORT" )
        print( "=" * 40 )

        # Total Orders
        total_orders = len( self.df )

        # Total Revenue
        total_revenue = self.df["final_price"].sum()

        # Revenue by Category
        category_revenue = (
            self.df.groupby( "category" )["final_price"]
            .sum()
        )

        top_category = category_revenue.idxmax()
        top_category_revenue = category_revenue.max()

        # Revenue by Region
        region_revenue = (self.df.groupby( "region" )["final_price"].sum())

        top_region = region_revenue.idxmax()
        top_region_revenue = region_revenue.max()

        # Highest Order
        highest_order = self.df.loc[self.df["final_price"].idxmax()]



        # Discount Saved
        discount_saved = ( self.df["quantity"]  * self.df["price"]  * self.df["discount"] ).sum()

        # High Value Orders
        high_value_orders = len(  self.df[self.df["final_price"] > 50000]   )

        print( f"Total Orders       : {total_orders}" )
        print( f"Total Revenue      : ₹{total_revenue:,.2f}" )
        print(
            f"Top Category       : {top_category} "
            f"(₹{top_category_revenue:,.2f})"
        )
        print(
            f"Top Region         : {top_region} "
            f"(₹{top_region_revenue:,.2f})"
        )
        print(
            f"Highest Order      : "
            f"Order #{highest_order['order_id']} — "
            f"{highest_order['customer']} — "
            f"₹{highest_order['final_price']:,.2f}"
        )
        print( f"Discount Saved     : ₹{discount_saved:,.2f}" )
        print( f"High Value Orders  : {high_value_orders} orders above ₹50,000" )

        print( "=" * 40 )

        # Bonus: Generate chart
        from src.chart_generator import ChartGenerator
        chart = ChartGenerator( self.df )
        chart.revenue_by_category()

        # Task 9
        csv_demo = CSVProcessor( self.file_path )
        csv_demo.walrus_operator()
