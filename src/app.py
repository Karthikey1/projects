# src/app.py

import tkinter as tk
from components.FileRenamingButton import FileRenamingButton
from components.FileUpload import FileUpload
from components.FolderSelector import FolderSelector
from components.NamingFormatInput import NamingFormatInput
from src.utils import load_data, rename_files_with_mapping

def run_app():
    root = tk.Tk()
    root.title("Advanced File Renamer Tool")
    root.geometry("600x500")

    # Folder Selector
    folder_selector = FolderSelector(root)

    # Naming Format Input
    naming_format_input = NamingFormatInput(root)

    # File Upload
    file_upload = FileUpload(root)

    # Rename Button
    def rename_files():
        folder_path = folder_selector.folder_path
        naming_format = naming_format_input.get_naming_format()
        data_file = file_upload.file_path

        if folder_path and naming_format and data_file:
            data = load_data(data_file)
            rename_files_with_mapping(folder_path, naming_format, data)
        else:
            print("Please complete all fields (folder, naming format, and data file).")

    rename_button = tk.Button(root, text="Rename Files", command=rename_files)
    rename_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    run_app()
