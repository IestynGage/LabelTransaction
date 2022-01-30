import csv
import sys

from labeler import Labeler
from transactions import Transactions

class LabelTransaction:
    def __init__(self) -> None:
        self.transactions = Transactions()

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
        print("Enter filename")
        # fileName = input()
        fileName = "a"
        print("Please enter account type:")
        print("1. Current Account")
        print("2. Credit Account")
        accountType = int(input())
        if(accountType == 1):
            self.stripCurrentAcount(fileName)
        elif (accountType == 2):
            self.stripCreditAccount(fileName)

    def stripCurrentAcount(self, fileName):
        self.readCSV("current.csv", 1)

    def stripCreditAccount(self, fileName):
        self.readCSV("credit.csv", -1)

    def exportList(self):
        print("Exporting list")
        self.transactions.convertToExcel()

    def readCSV(self, filename, valueType):
        labeller = Labeler()
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                rowLabel = labeller.checkLabels(row["Description"])
                if(labeller.checkLabels(row["Description"])==""):
                    print(row)
                    print("Please enter label")
                    rowLabel = input()

                if(rowLabel!="" or row["Value"]!=''):
                    value = float(row["Value"]) * valueType
                    self.transactions.addTransaction(row['Date'], row["Description"], value, rowLabel)
            

if __name__ == "__main__":
    labelTransaction = LabelTransaction()
    labelTransaction.mainMenu()
