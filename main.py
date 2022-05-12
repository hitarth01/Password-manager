from tkinter import *
from tkinter import messagebox
import random
import json
from typing import final
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 11)
    nr_symbols = random.randint(2, 5)
    nr_numbers = random.randint(2, 6)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()\
    
    new_dict = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please complete all the fields!")
    else:
        validated = messagebox.askokcancel(title=website, message="Are you sure you want to make these changes?")
        if validated:
            try:
                with open("data.json", mode="r") as data: 
                    # to READ json data :
                    d = json.load(data)
                    # updating old data
            except FileNotFoundError:
                with open("data.json", mode="w") as d:
                    json.dump(new_dict, d, indent=4)  
            else:
                d.update(new_dict)
                with open("data.json", mode="w") as data:
                    json.dump(d, data, indent=4)  

            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)  

# ---------------------------- Find Password -------------------------- #

def find_details():
    website = website_input.get()
    try:

        with open("data.json") as data:
            d = json.load(data)
        # d is a python a dictionary here
    except:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in d:
            email = d[website]["email"]
            password = d[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data for {website} in data file")
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries

website_input = Entry(width=27)
website_input.grid(column=1, row=1, columnspan=1)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "srivastavahitarth19@gmail.com")

password_input = Entry(width=27)
password_input.grid(column=1, row=3)

#Buttons

password_gen = Button(text="Generate Password", command=gen_password)
password_gen.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=12, command=find_details)
search_button.grid(column=2, row=1)


window.mainloop()