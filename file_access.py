import tkinter as tk
from tkinter import filedialog
from docx import Document
from PyPDF2 import PdfReader
import mimetypes
import pandas as pd
from lxml import etree

def read_text_from_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def read_text_from_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs]).strip()

def read_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text.strip()

def read_text_from_xml(file_path):
    with open(file_path, 'r') as file:
        tree = etree.parse(file)
        root = tree.getroot()
        return etree.tostring(root, pretty_print=True, encoding='unicode').strip()

def read_text_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string(index=False)

def read_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type == 'text/plain':
        return read_text_from_txt(file_path)
    elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return read_text_from_docx(file_path)
    elif mime_type == 'application/pdf':
        return read_text_from_pdf(file_path)
    elif mime_type == 'application/xml' or mime_type == 'text/xml':
        return read_text_from_xml(file_path)
    elif mime_type == 'text/csv':
        return read_text_from_csv(file_path)
    else:
        return "Unsupported file format"

def browse_and_print_text():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("All files", "*.*")]
        )
        if file_path:
            text = read_file(file_path)
            print("File contents:")
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
