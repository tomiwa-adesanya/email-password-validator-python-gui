import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from turtle import bgcolor

# DEFAULTS
FONT = ("Helvetica", 12)
WIDTH = 300
HEIGHT = 200

# ROOT EVENT FUNCTION
def destroy_root(event) -> None:
    """
    Closes root window
    """
    root.destroy()

# MAIN FRAME EVENT FUNCTION
def clear_inputs(event) -> None:
    """
    Clears email and password entry inputs
    """
    email_var.set("")
    password_var.set("")

def validate(email: str, password: str) -> None:
    """
    Checks if email and password inputs are valid or invalid and displays a message box.
    """
    import re

    email_pattern = r"[a-z0-9\.]+[@]{1}[a-z0-9]+[.]{1}[a-z0-9]+" 
    password_pattern = r"[a-z0-9\!\ ]{7,}" 

    email_valid = True if (re.findall(email_pattern, email, re.IGNORECASE)) else False
    password_valid = True if (re.findall(password_pattern, password, re.IGNORECASE)) else False

    if (email_valid and password_valid): # Executes if both email and password inputs are valid
        msg = "Email Address and Password are valid!"
        showinfo(
            title="Validation",
            message=msg
        )
    elif ((email_valid is False) and (password_valid is False)): # Executes if both email and password inputs are invalid
        msg = "Both Email address and Password are invalid!!!"
        showerror(
            title="Validation",
            message=msg
        )
    
    elif (not email_valid): # Executes if only email input is invalid
        msg = "Email Address is invalid!!!"
        showerror(
            title="Validation",
            message=msg
        )
    
    elif (not password_valid): # Executes if only password input is invalid
        msg = "Password is invalid!!! Make sure it is at least 7 characters"
        showerror(
            title="Validation",
            message=msg
        )


# ROOT CONFIGURATION
root = tk.Tk() 
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("Validate")
root.resizable(False, False)
root.bind("<Control-KeyPress-w>", destroy_root, add="+") # Closes window if Ctrl+w in pressed
root.bind("<Control-KeyPress-W>", destroy_root, add="+") # Closes window if Ctrl+W in pressed
root.bind("<Control-Alt-KeyPress-c>", clear_inputs, add="+") # Clears all inputed values if Ctrl+Alt+c is pressed

# MAIN FRAME CONFIGURATION
main = ttk.Frame(root, borderwidth=5)
main.place(relheight=1, relwidth=1)

# EMAIL LABEL-ENTRY CONFIG
email_label = ttk.Label(main, text="EMAIL ADDRESS: ", font=FONT)
email_label.pack(fill="x")

email_var = tk.StringVar() # Stores email input value

email_entry = ttk.Entry(main, textvariable=email_var, font=FONT)
email_entry.focus() # Sets email entry to be able to receive inputs as soon as the root window is created
email_entry.pack(fill="x")

gap = ttk.Label(main, text=" ") # Empty label to create a gap beween email section and password section
gap.pack(pady=5, fill="x")

# PASSWORD LABEL-ENTRY CONFIG
password_label = ttk.Label(main, text="PASSWORD: ", font=FONT)
password_label.pack(fill="x")

password_var = tk.StringVar() # Stores password input value

password_entry = ttk.Entry(main, textvariable=password_var, font=FONT, show="*")
password_entry.bind("<Return>", lambda event: validate(email_var.get(), password_var.get()))
password_entry.pack(fill="x")

# VALIDATE BUTTON
validate_button = ttk.Button(main, text="validate", command=lambda: validate(email_var.get(), password_var.get()))
validate_button.pack(fill="x", side="bottom")

# LOOPING ROOT WINDOW
root.mainloop()