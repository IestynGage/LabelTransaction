import sys
import os

from labeler import Labeler
from reader import Reader
from transactions import Transactions
from colorama import Fore, Style, init
import subprocess

CREDIT_ACCOUNT = -1
CURRENT_ACCOUNT = 1

CURSOR_UP_ONE = "\x1b[1A"
ERASE_LINE = "\x1b[2K"


def deleteLastLine(n=1):
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)

def openDirectory():
    directory = os.getcwd()
    if sys.platform == "darwin":
        subprocess.call(["open", directory])
    else:
        subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')

class LabelTransaction:
    def __init__(self) -> None:
        self.transactions = Transactions()
        self.reader = Reader()
        self.labeler = Labeler("labels.json")
        self.computedFiles = []
        init()

    def mainList(self):
        moreFiles = True
        while moreFiles:
            print("Looking for csv files...")
            files = [f for f in os.listdir(".") if os.path.isfile(f)]
            totalFiles = 0
            for f in files:
                if f.endswith(".csv"):
                    totalFiles = totalFiles + 1
                    if f in self.computedFiles:
                        print(
                            "("
                            + Fore.GREEN
                            + Style.BRIGHT
                            + "X"
                            + Style.RESET_ALL
                            + ") "
                            + f
                        )
                    else:
                        print(f)
            print("What file would you like to add next? (Enter nothing to export)")
            nextfile = input()
            deleteLastLine(3 + totalFiles)
            if nextfile != "":
                self.stripAccount(nextfile)
                self.computedFiles.append(nextfile + ".csv")
            else:
                moreFiles = False
                self.exportList()
                openDirectory()

    def stripAccount(self, fileName):
        print("Importing: " + Style.BRIGHT + fileName + Style.RESET_ALL)
        print("Please enter account type:")
        print("1. Current Account")
        print("2. Credit Account")
        accountType = int(input())
        deleteLastLine(4)
        if accountType == 1:
            self.stripCurrentAcount(fileName)
        elif accountType == 2:
            self.stripCreditAccount(fileName)
        deleteLastLine(1)
        print("Imported: " + fileName)

    def stripCurrentAcount(self, fileName):
        transactions = self.reader.readCSV(
            fileName + ".csv", self.labeler, CURRENT_ACCOUNT
        )
        self.transactions.addTransactions(transactions)

    def stripCreditAccount(self, fileName):
        transactions = self.reader.readCSV(
            fileName + ".csv", self.labeler, CREDIT_ACCOUNT
        )
        self.transactions.addTransactions(transactions)

    def exportList(self):
        print("Exporting list")
        self.transactions.convertToExcel()


if __name__ == "__main__":
    labelTransaction = LabelTransaction()
    labelTransaction.mainList()
