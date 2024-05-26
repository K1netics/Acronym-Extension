# main.py

import tkinter as tk
from file_access import browse_and_print_text

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    browse_and_print_text()

if __name__ == "__main__":
    main()
