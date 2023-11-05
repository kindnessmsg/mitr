import tkinter as tk
from gui.login_window import LoginWindow
from database.db_init import initialize_database

if __name__ == "__main__":
    # Initialize the database (create tables, populate with sample data if needed)
    initialize_database()

    # Create the main application window
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()