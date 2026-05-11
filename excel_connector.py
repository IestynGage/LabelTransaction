import os
import platform
import subprocess


def open_excel_file(filepath: str = "transactions.xlsx"):
    """
    Open an Excel file in Microsoft Excel.

    Args:
        filepath: Path to the .xlsx file
    """

    filepath = os.path.abspath(filepath)

    system = platform.system()

    if system == "Windows":
        os.startfile(filepath)

    elif system == "Darwin":
        # macOS
        subprocess.run(["open", "-a", "Microsoft Excel", filepath])

    elif system == "Linux":
        # Linux (requires libreoffice or excel alternative)
        subprocess.run(["xdg-open", filepath])

    else:
        raise OSError(f"Unsupported operating system: {system}")