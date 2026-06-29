from abc import ABC, abstractmethod


class BaseETL(ABC):

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def report(self):
        pass

    def run(self):
        print("=" * 50)
        print("Starting Sales ETL Pipeline")
        print("=" * 50)

        self.extract()
        self.validate()
        self.transform()
        self.report()

        print("=" * 50)
        print("Pipeline Completed")
        print("=" * 50)