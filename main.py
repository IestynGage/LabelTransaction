from excel_connector import open_excel_file
from exporter import export_transactions
from parser import parse_csv_files

from rules import Rules
from tui.CSVCategorizer import CsvCategorizer
from tui.ExtracMonth import MonthSelectorApp

# TUIs to select remaining categories.

# exporter

def main():
    # TODO Load current progress of excel. 
    # Ask user continue loading excel thingy for month ... y/n
    # Assuming the scenario you already ran this once this month
    csv_files = CsvCategorizer().run()
    month = MonthSelectorApp(csv_files).run()
    transactions = parse_csv_files(csv_files)
    labeled_transactions = Rules().apply(transactions)
    export_transactions(labeled_transactions)
    open_excel_file()

if __name__ == "__main__":
    main()
