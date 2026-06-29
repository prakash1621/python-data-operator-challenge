"""
csv_processor.py

Task 9:
Process CSV using Python csv module (No Pandas)
"""

import csv


class CSVProcessor:

    def __init__(self, file_path):
        self.file_path = file_path

    # ----------------------------------------
    # Walrus Operator (:=)
    # ----------------------------------------

    def walrus_operator(self):
        print("\n" + "=" * 50)
        print("TASK 9 - WALRUS OPERATOR")
        print("=" * 50)

        with open(self.file_path, newline="") as file:
            reader = csv.DictReader(file)

            high_value = [
                row for row in reader
                if (fp := float(row["quantity"]) * float(row["price"]) * (1 - float(row["discount"]))) > 50000
            ]

        print(f"\nHigh Value Orders : {len(high_value)}")

        for row in high_value:
            print(f"Order {row['order_id']} - {row['customer']}")

