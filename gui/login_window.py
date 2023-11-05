import tkinter as tk
from tkinter import messagebox
from database.user_manager import authenticate_user

class LoginWindow:
    def __init__(self, root):
        self.root = root
        root.title("User Authentication")

        # Calculate window position
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Required app size
        APP_WIDTH = 720
        APP_HEIGHT = 480

        # Calculate middle position
        x = (screen_width / 2) - (APP_WIDTH / 2)
        y = (screen_height / 2) - (APP_HEIGHT / 2)

        # Set window size and position
        root.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{int(x)}+{int(y)}")
        root.minsize(APP_WIDTH, APP_HEIGHT)

        # Create a parent frame for grouping all the widgets
        parentFrame = tk.Frame(root)
        parentFrame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create a label and entry for username field
        tk.Label(parentFrame, text="Username:", font=("helvetica", "18")).grid(row=0, column=0)
        self.userEntry = tk.Entry(parentFrame, font=("Courier", "16"))
        self.userEntry.grid(row=0, column=1)

        # Create a spacer frame for additional space
        tk.Frame(parentFrame, height=3).grid(row=1, column=0, columnspan=2)

        # Create a label and entry for password field
        tk.Label(parentFrame, text="Password:", font=("helvetica", "18")).grid(row=2, column=0)
        self.pwdEntry = tk.Entry(parentFrame, show="*", font=("Courier", "16"))
        self.pwdEntry.grid(row=2, column=1)

        # Create a spacer frame for additional space
        tk.Frame(parentFrame, height=13).grid(row=3, column=0, columnspan=2)

        # Create a login button and place it at bottom right
        loginButton = tk.Button(parentFrame, text="Log In", font=("helvetica", "10"),
                               padx=20, pady=5, command=self.login)
        loginButton.grid(row=4, column=1, sticky="e")

    def login(self):
        # Get entry values from both the fields
        username = self.userEntry.get().strip()
        password = self.pwdEntry.get().strip()

        # Check for the validity of credentials
        if authenticate_user(username, password):
            self.show_message("Login Successful!", True)
        else:
            self.show_message("Invalid Username/password", False)

    def show_message(self, message, success):
        if success:
            # Show success message
            messagebox.showinfo("Success!", "Authentication Successful")
        else:
            # Show error message for failed authentication
            messagebox.showerror("Failure!", "Authentication Failed. Invalid Username or password")

