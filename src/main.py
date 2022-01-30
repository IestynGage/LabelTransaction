import csv

class LabelTransaction:

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
                case default:
                    print("Did not recongise option")

    def stripAccount(self):
        print("Enter filename")
        fileName = input()
        print("Please enter account type:")
        print("1. Current Account")
        print("2. Credit Account")
        accountType = int(input())
        if(accountType == 1):
            self.stripCurrentAcount(fileName)
        elif (accountType == 2):
            self.stripCreditAccount(fileName)

    def stripCurrentAcount(self, fileName):
        print("Strip Current Account")

    def stripCreditAccount(self, fileName):
        print("Strip Current Account")

    def labelList(self):
        print("Please create the food list")

    def exportList(self):
        print("Please create the food list")

def readCSV(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print("ls")

if __name__ == "__main__":
    labelTransaction = LabelTransaction()
    labelTransaction.mainMenu()
