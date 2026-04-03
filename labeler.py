from enum import Enum, auto
from typing import List

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Input, Static
from textual.screen import ModalScreen
from textual.containers import Container


# -----------------------------
# Models
# -----------------------------

class Transaction:
    def __init__(
        self, date: str, desc: str, value: int,
        account_type: str, label: str, transactionType: str
    ):
        self.date = date
        self.desc = desc
        self.value = value
        self.account_type = account_type
        self.label = label
        self.transactionType = transactionType


class Category(Enum):
    SHOPPING = auto()
    CAFES = auto()
    UTILITY = auto()
    CAR = auto()
    TRANSPORT = auto()


# -----------------------------
# Autocomplete Modal
# -----------------------------

class LabelInputScreen(ModalScreen[str]):

    CSS = """
    Screen {
        align: center middle;
    }

    Container {
        width: 50%;
        height: 7;
        border: solid white;
        padding: 1;
    }
    """

    BINDINGS = [
        ("tab", "autocomplete", "Autocomplete"),
        ("escape", "cancel", "Cancel"),
    ]

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Enter Category:"),
            Input(placeholder="Start typing..."),
            Static("", id="suggestion"),
        )

    def on_input_changed(self, event: Input.Changed):
        typed = event.value.upper()
        suggestion_widget = self.query_one("#suggestion", Static)

        matches = [
            cat.name for cat in Category
            if cat.name.startswith(typed)
        ]

        if matches:
            suggestion_widget.update(f"Suggestion: {matches[0]}")
        else:
            suggestion_widget.update("")

    def action_autocomplete(self):
        input_widget = self.query_one(Input)
        typed = input_widget.value.upper()

        matches = [
            cat.name for cat in Category
            if cat.name.startswith(typed)
        ]

        if matches:
            input_widget.value = matches[0]

    def on_input_submitted(self, event: Input.Submitted):
        value = event.value.upper()
        if value in Category.__members__:
            self.dismiss(value)
        else:
            self.dismiss(None)

    def action_cancel(self):
        self.dismiss(None)


# -----------------------------
# Main App
# -----------------------------

class TransactionApp(App):

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("l", "label_selected", "Label Transaction"),
    ]

    CSS = """
    Screen {
        align: center middle;
    }

    DataTable {
        width: 95%;
        height: 85%;
    }
    """

    def __init__(self, transactions: List[Transaction]):
        super().__init__()
        self.transactions = transactions

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="table")
        yield Footer()

    def on_mount(self):
        table = self.query_one(DataTable)

        table.add_column("Date", key="date")
        table.add_column("Value", key="value")
        table.add_column("Description", key="desc")
        table.add_column("Label", key="label")

        for index, tx in enumerate(self.transactions):
            row_key = f"row_{index}"  # explicitly define row key

            table.add_row(
                tx.date,
                str(tx.value),
                tx.desc,
                tx.label or "[MISSING]",
                key=row_key
            )

            tx._row_key = row_key  # store string key

        table.cursor_type = "row"

    def action_label_selected(self):
        table = self.query_one(DataTable)
        row_index = table.cursor_row

        if row_index is None:
            return

        tx = self.transactions[row_index]

        def set_label(selected_label: str):
            if selected_label:
                tx.label = selected_label
                table.update_cell(tx._row_key, "label", selected_label)

        self.push_screen(LabelInputScreen(), set_label)

# -----------------------------
# Example Usage
# -----------------------------

if __name__ == "__main__":
    sample_transactions = [
        Transaction("24 Nov 2025", "Amazon Purchase", -50, "Debit", "", ""),
        Transaction("25 Nov 2025", "Cafe Nero", -8, "Debit", "", ""),
        Transaction("26 Nov 2025", "Electric Bill", -120, "Debit", "UTILITY", ""),
    ]

    app = TransactionApp(sample_transactions)
    app.run()