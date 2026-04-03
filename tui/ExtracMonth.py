import csv
from datetime import datetime
from pathlib import Path
from typing import List, Set

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Label
from textual.containers import Container


# -----------------------------
# CONFIGURE YOUR CSV FILES HERE
# -----------------------------
CSV_FILES = [
    "credit.csv",
    "current.csv",
    # add more here
]


def extract_months_from_csv(files: List[str]) -> List[str]:
    """Extract unique months in format 'Mon YYYY' from CSV files."""
    months: Set[str] = set()

    for file_path in files:
        path = Path(file_path)
        if not path.exists():
            print('could not find')
            continue

        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if "Date" not in reader.fieldnames:
                continue

            for row in reader:
                date_str = row["Date"].strip()
                try:
                    dt = datetime.strptime(date_str, "%d %b %Y")
                    month_label = dt.strftime("%b %Y")
                    months.add(month_label)
                except ValueError:
                    continue

    print("hello")
    print(months)
    # Sort chronologically
    return sorted(
        months,
        key=lambda m: datetime.strptime(m, "%b %Y")
    )

class MonthSelectorApp(App):


    def __init__(self, files: List[str]):
        super().__init__()
        self.files = files
        self.months: List[str] = []
        self.selected_month: str | None = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(id="month_list")  # empty here
        yield Footer()

    def on_mount(self):
        """Called after widgets are mounted. Safe to add ListItems here."""
        list_view = self.query_one(ListView)
        months = extract_months_from_csv(self.files)
        for month in months:
            item = ListItem(Label(month))
            item.month = month  # store value here
            list_view.append(item)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.selected_month = event.item.month
        self.exit(result=self.selected_month)

if __name__ == "__main__":
    app = MonthSelectorApp(["current.csv", 'credit.csv'])
    month = app.run()

    print("\nReturned Data:")
    print(month)
