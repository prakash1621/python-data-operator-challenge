from src.sales_etl import SalesETL


def main():

    etl = SalesETL("sales.csv")

    etl.run()


if __name__ == "__main__":
    main()