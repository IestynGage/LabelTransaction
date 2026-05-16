from typing import List

from models import Transaction
import json
from pathlib import Path
import re
from typing import Dict


class Rules():

  def __init__(self):
    self.income_labels = self.load_labels("income_labels.json")
    self.cost_labels = self.load_labels("cost_labels.json")
    pass

  def load_labels(self, labels_file_json: str) -> dict[str, str]:
    """Loads the JSON file labels into a dictionary {regex: label}"""

    path = Path(labels_file_json)

    if not path.exists():
        raise FileNotFoundError(f"{labels_file_json} not found")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert list of dicts -> {regex: label}
    return {
        item["regex"]: item["label"]
        for item in data
    }
  
  def apply(self, transactions: List[Transaction]):
    labeled_transactions = []
    
    for transaction in transactions:
      if transaction.label != "":
        labeled_transactions.append(transaction)
      elif transaction.value > 0:
        labeled_transactions.append(self.apply_label(transaction, self.income_labels))
      elif transaction.value < 1:
        labeled_transactions.append(self.apply_label(transaction, self.cost_labels))
      else:
        labeled_transactions.append(transaction)

    return labeled_transactions;

  def apply_label(self, transaction, labels: Dict[str, str]):
    """
    Takes a transaction and dict {regex: label}
    Returns the transaction with label applied if matched.
    """
    description = transaction.desc.lower()

    for pattern, label in labels.items():
      if re.search(pattern, description):
        transaction.label = label
        break  # stop at first match

    return transaction
  
def filter_by_month(transactions: List[Transaction], month: str) -> List[Transaction]:
  """
  Filters a list of transactions by a 3-letter month string (e.g., 'jan', 'nov').
  Assumes transaction.date is in the format 'DD MMM YYYY'.
  """
  # Normalize the input (e.g., "Jan " -> "jan")
  target_month = month.lower()
  
  filtered_transactions = []
  for t in transactions:
    try:
      # Split '24 Nov 2025' by spaces -> ['24', 'Nov', '2025']
      # Index 1 is the month ('Nov')
      # tx_month =  t.date.split()[0].lower()
      
      if target_month in t.date.lower():
        filtered_transactions.append(t)
    except IndexError:
      # Skips any transactions with malformed or missing dates 
      # to prevent the app from crashing
      continue
          
  return filtered_transactions