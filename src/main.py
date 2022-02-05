import csv
import sys

from labeler import Labeler
from transactions import Transactions
from colorama import Fore, Style, init

CREDIT_ACCOUNT = -1
CURRENT_ACCOUNT = 1

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

def deleteLastLine(n=1): 
    for _ in range(n): 
        sys.stdout.write(CURSOR_UP_ONE) 
        sys.stdout.write(ERASE_LINE) 

class LabelTransaction:
    def __init__(self) -> None:
        self.transactions = Transactions()
        self.labeler = Labeler('labels.json')
        init()

    def mainMenu(self):
        menu = True
        while(menu):
            print("Please enter an option")
            print("    1 - Input Account")
            print("    2 - Export list")
            print("    3 - Quit")
            option = int(input("Please enter an option"))
            match option:
                case 1:
                    deleteLastLine(5)
                    self.stripAccount()
                    
                case 2:
                    self.exportList()

                case 3:
                    print("Quit")
                    menu = False
                    sys.exit(0)

                case _:
                    print("Did not recongise option")

    def stripAccount(self):
        print("Importing account")
        print("Enter filename")
        fileName = input()
        deleteLastLine(3)
        print("Importing: " + fileName)
        print("Please enter account type:")
        print("1. Current Account")
        print("2. Credit Account")
        accountType = int(input())
        deleteLastLine(4)
        if(accountType == 1):
            self.stripCurrentAcount(fileName)
        elif (accountType == 2):
            self.stripCreditAccount(fileName)
        deleteLastLine(1)
        print("Imported: " + fileName)

    def stripCurrentAcount(self, fileName):
        self.readCSV(fileName + ".csv", CURRENT_ACCOUNT)

    def stripCreditAccount(self, fileName):
        self.readCSV(fileName + ".csv", CREDIT_ACCOUNT)

    def exportList(self):
        print("Exporting list")
        self.transactions.convertToExcel()

    def readCSV(self, filename, valueType):
        labeller = self.labeler

        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                rowLabel = labeller.checkLabels(row["Description"])
                if(rowLabel!="" or row["Value"]!=''):
                    value = float(row["Value"]) * valueType
                    if(labeller.checkLabels(row["Description"])==""):
                        print("=======================================================")
                        print("Date: " + row["Date"])
                        print("Desc: " + row["Description"])
                        if(value < 0):
                            print("Value: " + Fore.RED + row["Value"] + Style.RESET_ALL)
                        else:
                            print("Value: " + Fore.GREEN + row["Value"] + Style.RESET_ALL)
                        print("Please enter label")
                        rowLabel = input()
                        deleteLastLine(6)
                    
                    self.transactions.addTransaction(row['Date'], row["Description"], value, rowLabel)
            

if __name__ == "__main__":
    labelTransaction = LabelTransaction()
    labelTransaction.mainMenu()
