# components/FileRenamingButton.py

import tkinter as tk
from src.utils import rename_files
from components.FolderSelector import FolderSelector
from components.NamingFormatInput import NamingFormatInput


class FileRenamingButton:
    def __init__(self, master):
        self.master = master

        # Folder selection component
        self.folder_selector = FolderSelector(master)

        # Naming format input component
        self.naming_format_input = NamingFormatInput(master)

        # Rename button
        self.rename_button = tk.Button(master, text="Rename Files", command=self.rename_files)
        self.rename_button.pack(pady=20)

    def rename_files(self):
        folder_path = self.folder_selector.folder_path
        naming_format = self.naming_format_input.get_naming_format()

        if folder_path and naming_format:
            rename_files(folder_path, naming_format)
        else:
            print("Please select a folder and enter a naming format.")


