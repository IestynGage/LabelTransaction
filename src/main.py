import sys

from labeler import Labeler
from reader import Reader
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
        self.reader = Reader()
        self.labeler = Labeler('labels.json')
        init()

    def mainMenu(self):
        menu = True
        while(menu):
            print("Please enter an option")
            print("    1 - Input Account")
            print("    2 - Export list")
            option = int(input("Please enter an option"))
            deleteLastLine(4)
            match option:
                case 1:
                    self.stripAccount()
                    
                case 2:
                    self.exportList()
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
        transactions = self.reader.readCSV(fileName + ".csv", self.labeler, CURRENT_ACCOUNT)
        self.transactions.addTransactions(transactions)

    def stripCreditAccount(self, fileName):
        transactions = self.reader.readCSV(fileName + ".csv", self.labeler, CREDIT_ACCOUNT)
        self.transactions.addTransactions(transactions)

    def exportList(self):
        print("Exporting list")
        self.transactions.convertToExcel()
            

if __name__ == "__main__":
    labelTransaction = LabelTransaction()
    labelTransaction.mainMenu()
