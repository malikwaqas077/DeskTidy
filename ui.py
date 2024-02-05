import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from main import organize_folders, files_categories

def add_custom_extention(custom_categories):
    extenstions= simpledialog.askstring("Input", "Enter the Extention e.g., .txt")
    if extenstions:
        category = simpledialog.askstring("Input", "Enter the Category for this extention e.g., documents")
        if category:
            if category in custom_categories:
                custom_categories[category].append(extenstions)
            else:
                custom_categories[category] = extenstions
            messagebox.showinfo("Info", f"Added {extenstions} to {category} category")
def select_folder():
    folder_path = filedialog.askdirectory()
    organize_folders(folder_path, files_categories)
    messagebox.showinfo("Info", "Files Organized Successfully!")

def create_ui():
    window=tk.Tk()
    window.title("TidyDesk")

    custom_categories={}
    tk.Label(window, text="Click below to select a folder to organize:", font=("Arial", 12)).pack(pady=10)
    tk.Button(window, text="Select Folder", command=select_folder, font=("Arial", 12)).pack(pady=10)

    tk.Label(window, text="Add a custom file extension to categories:", font=("Arial", 12)).pack(pady=10)
    tk.Button(window, text="Add Custom Extension", command=lambda: add_custom_extention(custom_categories), font=("Arial", 12)).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_ui()
