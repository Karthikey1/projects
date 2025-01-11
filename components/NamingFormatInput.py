# components/NamingFormatInput.py

import tkinter as tk

class NamingFormatInput:
    def __init__(self, master):
        self.master = master
        self.naming_format = ""

        self.label = tk.Label(master, text="Enter Naming Format (e.g., a1_cell_a2):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=10)

        # Hint for placeholders
        self.hint_label = tk.Label(
            master,
            text="Use placeholders like a1, a2, etc., which will be replaced automatically.",
            fg="gray"
        )
        self.hint_label.pack(pady=5)

    def get_naming_format(self):
        """Return the naming format entered by the user."""
        self.naming_format = self.entry.get()
        return self.naming_format
