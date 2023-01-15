import csv
import sys
import readline

from labeler import Labeler
from transactions import Transactions, INCOME, EXPENSE
from colorama import Fore, Style, init

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

def deleteLastLine(n=1): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE) 

class Reader:
    def __init__(self) -> None:
        words = ['dog','cat','rabbit','bird','slug','snail']
        init()

    def readCSV(self, filename:str, labeller:Labeler, accountType:int):
        transactions = Transactions()
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                rowLabel = labeller.matchesLabel(row["Description"])

                if(rowLabel!="" or row["Value"]!=''):
                    value = float(row["Value"]) * accountType
                    
                    if(labeller.matchesLabel(row["Description"])==""):
                        rowLabel = self.manualLabel(row["Date"], row["Description"], value, labeller)
                    transactionType = INCOME if value > 0 else EXPENSE

                    transactions.addTransaction(row['Date'], row["Description"], value, rowLabel, transactionType)

        return transactions
    
    def manualLabel(self, date:str, desc:str, value:float, labeller:Labeler):
        print("=======================================================")
        print("Date: " + date)
        print("Desc: " + desc)
        if(value < 0):
            print("Value: " + Fore.RED + str(value) + Style.RESET_ALL)
        else:
            print("Value: " + Fore.GREEN + str(value) + Style.RESET_ALL)
        print("Please enter label")
        validLabel = False
        while (validLabel == False):
            rowLabel =  input()
            if (labeller.isValidLabel(rowLabel)==False and rowLabel!=""):
                deleteLastLine(2)
                print(rowLabel + " isn't a valid label, please enter a label:")
            else:
                validLabel = True
        deleteLastLine(6)
        return rowLabel

readline.parse_and_bind("tab: complete")