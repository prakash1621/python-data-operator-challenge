# Python Data Operator Challenge

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python and Pandas. The goal is to clean, transform, analyze, and summarize a sales dataset while demonstrating the use of different Python operators in a real-world data engineering scenario.

The project covers:

* Python Operators
* Pandas DataFrame operations
* NumPy conditional operations
* CSV processing using Python's built-in `csv` module
* Object-Oriented Programming (OOP)
* Data aggregation and reporting
* Data visualization using Matplotlib

---

## Project Structure

```text
python-data-operator-challenge/
│
├── solution.py
├── sales.csv
├── README.md
├── requirements.txt
│
├── src/
│   ├── sales_etl.py
│   ├── csv_processor.py
│   └── chart_generator.py
│
├── output/
│   ├── report.csv
│   └── revenue_chart.png
│
└── screenshots/
```

---

## Technologies Used

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* CSV Module

---

# Task-wise Approach

## Task 1 – Load and Inspect Data

* Loaded the dataset using `pandas.read_csv()`.
* Displayed the shape of the dataset.
* Displayed column data types.
* Checked for missing values using `isnull().sum()`.

---

## Task 2 – Calculate Final Price

Created a new column called `final_price` using arithmetic operators.

Formula:

```
final_price = quantity × price × (1 - discount)
```

Rounded the result to two decimal places.

---

## Task 3 – Comparison Operators

Used comparison operators to filter data.

Implemented:

* Orders with `final_price > 50000`
* Orders from South region
* Electronics products with quantity greater than or equal to 3

Operators used:

* >
* ==
* > =

---

## Task 4 – Logical Operators

Used Pandas logical operators.

Implemented:

* Electronics OR Furniture
* Discount NOT equal to zero
* Electronics in South OR East with discount greater than zero

Operators used:

* &
* |
* ~

---

## Task 5 – Membership Operators

Used the `isin()` method.

Implemented:

* Customers Alice, Eve and Laura
* Orders NOT in North or West regions

---

## Task 6 – Aggregation

Performed aggregation using `groupby()`.

Calculated:

* Total revenue by category
* Average discount by region
* Maximum and minimum final price by category

Functions used:

* sum()
* mean()
* max()
* min()

---

## Task 7 – String Operators

Performed string manipulation using Pandas string methods.

Implemented:

* Converted product names to uppercase
* Found customers whose names start with vowels
* Counted products containing the letter 'a'

Methods used:

* str.upper()
* str.startswith()
* str.contains()

---

## Task 8 – Conditional Column

Created a new column called `revenue_tier` using `numpy.where()`.

Rules:

* High → Final Price ≥ 100000
* Medium → Final Price ≥ 20000
* Low → Otherwise

---

## Task 9 – Identity and Walrus Operators

Used Python's built-in `csv` module without Pandas.

Implemented:

* Loaded CSV using `csv.DictReader`
* Used Walrus Operator (`:=`) to calculate and filter high-value orders
* Used Identity Operators (`is None` and `is not None`) to check for missing values

---

## Task 10 – Sales Summary Report

Generated a formatted report containing:

* Total Orders
* Total Revenue
* Top Category
* Top Region
* Highest Order
* Discount Saved
* High Value Orders

The report is printed to the console using formatted f-strings.

---

## Bonus Features

* Exported summary as `report.csv`
* Generated Revenue by Category bar chart using Matplotlib
* Used formatted f-strings for readable console output

---

## How to Run

1. Clone the repository.

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Run the project.

```bash
python solution.py
```

---

## Output

The application generates:

* Console summary report
* report.csv
* revenue_chart.png

---

## Python Concepts Demonstrated

* Classes and Objects
* Constructors (`__init__`)
* Encapsulation
* Object-Oriented Programming
* Arithmetic Operators
* Comparison Operators
* Logical Operators
* Membership Operators
* Identity Operators
* Walrus Operator
* Pandas DataFrame Operations
* NumPy
* CSV Module
* Matplotlib Visualization

---

## Author

Prakash
