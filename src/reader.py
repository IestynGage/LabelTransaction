import csv
import sys

from labeler import Labeler
from transactions import Transactions
from colorama import Fore, Style, init

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

def deleteLastLine(n=1): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE) 

class Reader:
    def __init__(self) -> None:
        self.transactions = Transactions()
        init()

    def readCSV(self, filename, valueType):
        labeller = Labeler()
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                rowLabel = labeller.checkLabels(row["Description"])

                if(rowLabel!="" or row["Value"]!=''):
                    value = float(row["Value"]) * valueType
                    
                    if(labeller.checkLabels(row["Description"])==""):
                        rowLabel = self.manualLabel(row["Date"], row["Description"], value)
                    
                    self.transactions.addTransaction(row['Date'], row["Description"], value, rowLabel)
    
    def manualLabel(self, date:str, desc:str, value:float):
        print("=======================================================")
        print("Date: " + date)
        print("Desc: " + desc)
        if(value < 0):
            print("Value: " + Fore.RED + value + Style.RESET_ALL)
        else:
            print("Value: " + Fore.GREEN + value + Style.RESET_ALL)
        print("Please enter label")
        rowLabel = input()
        deleteLastLine(6)
        return rowLabel