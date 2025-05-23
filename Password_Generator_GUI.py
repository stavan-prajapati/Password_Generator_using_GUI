from tkinter import Tk,Label,Button,messagebox,Entry,Frame
import random
import string

root=Tk()
root.title("Password Generetor")
root.state("zoomed")
def password_recommendations_msg():
    messagebox.showinfo("Password recommendations","""
For secure and reliable passwords, follow these recommendations:

- 8 to 12 Characters: Suitable for general accounts like social media, shopping websites, and personal apps. Recommended to include:
  - 2-3 Uppercase letters
  - 3-4 Lowercase letters
  - 2 Digits
  - 1-2 Special Characters

- 12 to 16 Characters: Ideal for sensitive accounts such as emails, financial services, and business platforms. Strongly recommended to include:
  - 3-5 Uppercase letters
  - 4-6 Lowercase letters
  - 3-4 Digits
  - 2-3 Special Characters""")
    
Digits=string.digits
Uppercase=string.ascii_uppercase
Lowercase=string.ascii_lowercase
special_chars = "!@#$%^&*()_-+"

def clear():
    try:
        num_of_digits.delete(0, 'end')
        num_of_uppercase.delete(0, 'end')
        num_of_lowercase.delete(0, 'end')
        num_of_special_character.delete(0, 'end')
        show_password.config(text="")
        password_generete_btn.config(state="normal")
    except:
        messagebox.showwarning("Warning", "Nothing To Clear.")

def exit():
    root.destroy()

def copy_to_clipboard():
    password=show_password.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No Password To Copy.")

def password_generating():
    global show_password
    try:
        num_of_digits_val = int(num_of_digits.get())
        num_of_uppercase_val = int(num_of_uppercase.get())
        num_of_lowercase_val = int(num_of_lowercase.get())
        num_of_special_character_val = int(num_of_special_character.get())

        total_lenght = num_of_digits_val + num_of_lowercase_val + num_of_uppercase_val + num_of_special_character_val

        if total_lenght == 0:
            messagebox.showwarning("Warning", "Enter at least one character count.")
        elif total_lenght > 16:
            messagebox.showwarning("Warning", "Maximum 16 characters allowed.")
        else:
            password = (
                random.choices(Digits, k=num_of_digits_val) +
                random.choices(Uppercase, k=num_of_uppercase_val) +
                random.choices(Lowercase, k=num_of_lowercase_val) +
                random.choices(special_chars, k=num_of_special_character_val)
            )
            random.shuffle(password)
            password_generete_btn.config(state="disabled")
            show_password = Label(pass_generator_btn_label_frame, text=f"{"".join(password)}", font="consolas 15 bold", fg="black")
            show_password.pack(side="left", padx=10)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

welcome_frame=Frame(root,)
welcome_frame.grid(row=0,column=0)
welcome_label=Label(welcome_frame,text="Password Generator !!",font="consolas 40 bold")
welcome_label.pack(side="left",padx=30,pady=30)
password_recommendations_btn=Button(welcome_frame,text="Password Recommendations",font="consolas 20 bold ",command=password_recommendations_msg,bg="#28a745",fg="white",activebackground="#1e7e34",activeforeground="white",relief="raised",bd=5)
password_recommendations_btn.pack(side="left",pady=10)
clear_btn=Button(welcome_frame,text="Clear All",font="consolas 20 bold",command=clear, bg="#0275d8",fg="white",activebackground="#025aa5",activeforeground="white",relief="raised",bd=5)
clear_btn.pack(side="left",padx=30)
exit_btn=Button(welcome_frame,text="Exit",font="consolas 20 bold",command=exit,bg="#d9534f",fg="white", activebackground="#c9302c",  activeforeground="white",relief="raised",bd=5)
exit_btn.pack(side="right",padx=50)

input_uppercase_frame=Frame(root,)
input_uppercase_frame.grid(row=2,column=0)
num_of_uppercase_label=Label(input_uppercase_frame,text="How Many Uppercase Characters : ",font="consolas 20 bold",)
num_of_uppercase_label.pack(side="left",pady=15)
num_of_uppercase=Entry(input_uppercase_frame,font="consolas 20 bold", bg="#000000", fg="#FFFFFF", bd=5, relief="groove",insertbackground="white")
num_of_uppercase.pack(side="left")

input_lowercase_frame=Frame(root,)
input_lowercase_frame.grid(row=3,column=0)
num_of_lowercase_label=Label(input_lowercase_frame,text="How Many Lowercase Characters : ",font="consolas 20 bold")
num_of_lowercase_label.pack(side="left",pady=15)
num_of_lowercase=Entry(input_lowercase_frame,font="consolas 20 bold",bg="#000000", fg="#FFFFFF", bd=5, relief="groove",insertbackground="white")
num_of_lowercase.pack(side="left")

input_special_character_frame=Frame(root,)
input_special_character_frame.grid(row=4,column=0)
num_of_special_character_label=Label(input_special_character_frame,text="   How Many Special character : ",font="consolas 20 bold")
num_of_special_character_label.pack(side="left",pady=15)
num_of_special_character=Entry(input_special_character_frame,font="consolas 20 bold",bg="#000000", fg="#FFFFFF", bd=5, relief="groove",insertbackground="white")
num_of_special_character.pack(side="left")

input_digits_frame=Frame(root,)
input_digits_frame.grid(row=5,column=0)
num_of_digits_label=Label(input_digits_frame,text="\t      How Many Digits : ",font="consolas 20 bold")
num_of_digits_label.pack(side="left",pady=15)
num_of_digits=Entry(input_digits_frame,font="consolas 20 bold",bg="#000000", fg="#FFFFFF", bd=5, relief="groove",insertbackground="white")
num_of_digits.pack(side="left")

pass_generator_btn_label_frame=Frame(root,)
pass_generator_btn_label_frame.grid(row=6,column=0)
password_generete_btn=Button(pass_generator_btn_label_frame,text="Generate Password ",font="consolas 20 bold",command=password_generating,bg="#007bff",fg="white",activebackground="#0056b3",activeforeground="white",relief="raised",bd=5,disabledforeground="white")
password_generete_btn.pack(side="left",pady=20)

copy_btn_frame=Frame(root,)
copy_btn_frame.grid(row=7,column=0)
copy_password_btn=Button(copy_btn_frame,text="Copy password",font="consolas 20 bold",command=copy_to_clipboard, bg="#28a745",fg="white",activebackground="#1e7e34",activeforeground="white",relief="raised",bd=5)
copy_password_btn.pack(side="left",padx=50)

root.mainloop()