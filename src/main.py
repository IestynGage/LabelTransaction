from cProfile import label
import csv
from fileinput import filename

from labeler import Label, Labeler
from transactions import Transaction

class LabelTransaction:
    def __init__(self) -> None:
        self.transactions = Transaction()

    def mainMenu(self):
        menu = True
        while(menu):
            option = int(input("Please enter an option"))
            match option:
                case 0:
                    print("Inputting file")
                    self.stripAccount()
                    
                case 1:
                    print("Outputting file")

                case 2:
                    print("Quit")
                    menu = False

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
        self.readCSV("current.csv")

    def stripCreditAccount(self, fileName):
        self.readCSV("credit.csv")

    def labelList(self):
        print("Please create the food list")

    def exportList(self):
        print("Please create the food list")

    def readCSV(self, filename):
        labeller = Labeler()
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                rowLabel = labeller.checkLabels(row["Description"])
                if(labeller.checkLabels(row["Description"])==""):
                    print(row)
                    print("Please enter label")
                    label = input()

                self.transactions.addTransaction(row['date'], row["Description"], row["value"], rowLabel)
            

if __name__ == "__main__":
    labelTransaction = LabelTransaction()
    labelTransaction.mainMenu()
