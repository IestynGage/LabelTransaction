from excel_connector import open_excel_file
from exporter import export_transactions
from models import Transaction
from parser import parse_csv_files, parse_excel

from rules import Rules, filter_by_month
from tui.CSVCategorizer import CsvCategorizer
from tui.ExtracMonth import MonthSelectorApp
from tui.existing import continue_with_existing

# TUIs to select remaining categories.

# exporter

def main():
    existing_transactions:list[Transaction] = parse_excel('transactions.xlsx')

    transactions:list[Transaction] = []
    if continue_with_existing(existing_transactions):
        transactions = existing_transactions
    else:
        csv_files = CsvCategorizer().run()
        month = MonthSelectorApp(csv_files).run().split()[0]
        print(month)
        csv_transactions = parse_csv_files(csv_files)
        print(len(csv_transactions))
        transactions = filter_by_month(csv_transactions, month)
        print(len(transactions))
    
    labeled_transactions = Rules().apply(transactions)
    export_transactions(labeled_transactions)
    open_excel_file()

if __name__ == "__main__":
    main()

# Continue with existing t 