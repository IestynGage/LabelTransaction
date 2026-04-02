from models import Transaction
import pandas as pd
from typing import List

def load_transactions(csv_path: str, account_type:str) -> List[Transaction]:
    # Read CSV
    df = pd.read_csv(csv_path)

    # Ensure expected columns exist
    required_columns = [
        "Date",
        "Type",
        "Description",
        "Value",
        "Balance",
        "Account Name",
        "Account Number",
    ]
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Optional: Clean and normalize
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

    transactions = []

    for _, row in df.iterrows():
        transaction = Transaction(
            date=row["Date"],
            desc=row["Description"],
            value=row["Value"],
            account_type=account_type,
            label="",
            transactionType=""
        )
        transactions.append(transaction)

    return transactions