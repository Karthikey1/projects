# components/FileUpload.py

import tkinter as tk
from tkinter import filedialog


class FileUpload:
    def __init__(self, master):
        self.master = master
        self.file_path = None

        self.label = tk.Label(master, text="Upload CSV/Excel File for Placeholders:")
        self.label.pack(pady=10)

        self.upload_button = tk.Button(master, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=10)

    def upload_file(self):
        """Open file dialog to upload CSV/Excel file."""
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )
        if self.file_path:
            print(f"Uploaded file: {self.file_path}")
        else:
            print("No file selected.")