from parser import load_transactions

# TUI to select CSVs and their type

# Select Month

# Parse transcations and 'rules'.

# TUIs to select remaining categories.

# exporter

def main():
    list = load_transactions('./credit.csv', 'credit')
    print(len(list))

if __name__ == "__main__":
    main()
