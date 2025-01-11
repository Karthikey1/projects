# components/FolderSelector.py

import tkinter as tk
from tkinter import filedialog

class FolderSelector:
    def __init__(self, master):
        self.master = master
        self.folder_path = ""

        self.label = tk.Label(master, text="Selected Folder: None")
        self.label.pack(pady=20)

        self.select_button = tk.Button(master, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

    def select_folder(self):
        """Open a dialog for the user to select a folder."""
        self.folder_path = filedialog.askdirectory(title="Select Folder")
        if self.folder_path:
            self.label.config(text=f"Selected Folder: {self.folder_path}")
        else:
            self.label.config(text="No folder selected!")
