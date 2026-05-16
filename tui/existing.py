from typing import List

from models import Transaction


def continue_with_existing(transactions: List[Transaction]) -> bool:
  if not transactions or len(transactions) == 0:
    return False

  month = transactions[0].date.split()[1]
  total_transactions = len(transactions)
  transactions_with_label = sum(1 for t in transactions if t.label)

  print(f"\nFound {total_transactions} transactions for {month} ({transactions_with_label} labelled).")
  user_choice = input("Do you wish to continue? [y/N]: ").strip().lower()

  if user_choice in ['y', 'yes']:
      return True

  return False