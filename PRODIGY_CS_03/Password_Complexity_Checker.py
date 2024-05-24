import tkinter as tk
from tkinter import messagebox
import re

def check_password_complexity(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess the strength of the password based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password!"
    else:
        feedback = "Weak password. Consider the following improvements:\n"
        if not length_criteria:
            feedback += "- Ensure the password is at least 8 characters long\n"
        if not uppercase_criteria:
            feedback += "- Include at least one uppercase letter\n"
        if not lowercase_criteria:
            feedback += "- Include at least one lowercase letter\n"
        if not digit_criteria:
            feedback += "- Include at least one digit\n"
        if not special_char_criteria:
            feedback += "- Include at least one special character (!@#$%^&*(),.?\":{}|<>)\n"

        return feedback

def check_password():
    password = entry_password.get()
    result = check_password_complexity(password)
    messagebox.showinfo("Password Complexity", result)

# Create the main window
root = tk.Tk()
root.title("Password Complexity Checker")

# Create and place widgets
label_password = tk.Label(root, text="Enter your password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", width=40)  # Increased width here
entry_password.pack(pady=5)

button_check = tk.Button(root, text="Check Password", command=check_password)
button_check.pack(pady=5)

# Run the application
root.mainloop()
