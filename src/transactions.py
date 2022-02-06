from openpyxl import Workbook

class Transactions:
    def __init__(self):
        self.labels = []
        self.wb = Workbook()

    def addTransaction(self, date:str, desc:str, value:int, label:str):
        self.labels.append(Transaction(date, desc, value, label))

    def addTransactions(self, transactions):
        self.labels.append(transactions)

    def convertToExcel(self):
        ws = self.wb.active
        for transaction in self.labels:
            ws.append([transaction.date, transaction.desc, transaction.value, transaction.label])
 
        self.wb.save("spending.xlsx")
        print("Export spending.xlsx succesfull")

class Transaction:
    def __init__(self, date:str, desc:str, value:int, label:str):
        self.date = date
        self.desc = desc
        self.value = value
        self.label = label
