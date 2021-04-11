from tkinter import *
from tkinter import messagebox
import pyperclip
import pandas
import random
import json
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(letters) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
        website_data = website_input.get()
        email_data = email_input.get()
        password_data = password_input.get()
        new_data = {
            website_data:
                {
            "email": email_data,
            "password":password_data
        }
        }

        if len(password_data) == 0 or len(website_data) == 0:
            messagebox.showinfo(title="Error", message="Please fill all fields")
        else:
            try:
                 with open("data.json", "r") as data_file:
                        # Reading old data
                        data = json.load(data_file)
                        # Updating old data with new data
            except FileNotFoundError :
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                 website_input.delete(0, END)
                 password_input.delete(0, END)

def search():
    website_data = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error", message="No Data Exist")
    else:
          for key in data:
              if key == website_data:
                  email = data[key]["email"]
                  password = data[key]["password"]
                  messagebox.showinfo(title="Search result",message="emai - "f"{email} ,f{password}")
                  break;
              else:
                  messagebox.showinfo(title="Error", message="Search is unsuccessfull")
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #





canvas  = Canvas(width = 200, height = 200)
logo_lg = PhotoImage(file = "logo.png")
canvas.create_image(100, 100,image=logo_lg)
canvas.grid(row = 0, column = 1)

website = Label(text="Website :")
website.grid(row =1, column = 0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row = 1, column = 1)

search_button = Button()
search_button.config(text="Search", command=search)
search_button.grid(row = 1, column = 2)

email = Label(text = "Email/Username :")
email.grid(row = 2, column = 0)
email_input = Entry(width=35)
email_input.insert(0, "farhan786abdullah@gmail.com")
email_input.grid(row = 2, column = 1, columnspan= 2)



password = Label(text ="Password :")
password.grid(row = 3, column = 0)
password_input = Entry(width = 21)
password_input.grid(row = 3, column = 1)

generate_button = Button()
generate_button.config(text = "Generate Password",command = generate_password)
generate_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width=36,command = save)
add_button.grid(row=4, column=1, columnspan=2, )




window.mainloop()