import tkinter as tk
import re
root = tk.Tk()
root.geometry("640x400")
root.configure(bg="#b0c4de")

entry = tk.Entry(root,width=30,show="*")
entry.pack(pady=10)
strength_label=tk.Label(root,text="Enter your password",font =("Helevetica",12),
                        bg="#e6e6fa" , fg="#000000" )
strength_label.pack(pady=5)

def check_password():
    password =entry.get()
    length_error = len(password)<8 
    digit_error = re.search(r"\d",password) is None
    uppercase_error = re.search(r"[A-Z]",password) is None
    lowercase_error = re.search(r"[a-z]",password) is None
    symbol_error = re.search(r"[@#$%*!&]",password) is None

    error_list = [length_error,digit_error, uppercase_error, lowercase_error, symbol_error]
    total_error = sum(error_list)

    if total_error == 0:
        strength_label.config(text="Password Strength: strong", fg = "green")
    elif total_error <=2:
        strength_label.config(text="Password Strength: moderate", fg = "orange")
    else:
        strength_label.config(text="Password Strength: weak", fg = "red")

check_btn = tk.Button(root, text="Check Strength", command=check_password)
check_btn.pack(pady=10)
root.mainloop()

#PASSWORD STRENGTH CHECKER BY YASHIHII
#PROUDLY BUILT IN ONE DAY1!!!