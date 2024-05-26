# file_access.py

import tkinter as tk
from tkinter import filedialog
import os
import docx
from PyPDF2 import PdfReader

def read_text_from_pdf(file_path):
    """
    Read text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The contents of the PDF file.
    """
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text.strip()

def browse_and_print_text():
    """
    Open a file dialog to allow the user to select a text file, Word document, or PDF,
    then read and print the contents of the selected file.
    """
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("Word documents", "*.docx"), ("PDF files", "*.pdf")]
        )
        if file_path:
            if file_path.endswith(".txt"):
                text = read_text_from_txt(file_path)
                print("File contents:")
                print(text)
            elif file_path.endswith(".docx"):
                text = read_text_from_docx(file_path)
                print("Document contents:")
                print(text)
            elif file_path.endswith(".pdf"):
                text = read_text_from_pdf(file_path)
                print("PDF contents:")
                print(text)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    browse_and_print_text()

if __name__ == "__main__":
    main()
