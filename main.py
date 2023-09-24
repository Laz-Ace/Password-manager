
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    pas_entry.delete(0, END)
    pas_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = web_entry.get()
    email = user_entry.get()
    password = pas_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("Day_29/data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Day_29/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("Day_29/data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pas_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    
    website = web_entry.get()

    try:
            with open("Day_29/data.json", "r") as data_file:
                # Loading json data
                data = json.load(data_file)
                email = data[website]["email"]
                searched_pass = data[website]["password"]
    except FileNotFoundError:
        messagebox.showwarning(title= "Warning", message= "Looks like there is no data on this computer")
    except KeyError:
        messagebox.showwarning(title= "Warning", message= "There is no data for that website")
    else:
        messagebox.showinfo(title= "Website Info", message= f"Email: {email} \nPassword: {searched_pass}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(height= 200, width= 200)
lock_image = PhotoImage(file= "/home/laz/Desktop/100Days/Day_29/logo.png")
canvas.create_image(100, 100, image= lock_image)
canvas.grid(row= 0, column= 1)

web_label = Label(text= "Website:")
web_label.grid(row= 1, column=0)

user_label = Label(text= "Email/Username:  ")
user_label.grid(row= 2, column= 0)

pas_label = Label(text= "Password:")
pas_label.grid(row= 3, column= 0)

web_entry = Entry(width= 27)
web_entry.grid(row= 1, column= 1)
web_entry.focus()

user_entry = Entry(width= 47)
user_entry.grid(row= 2, column= 1, columnspan= 2)
user_entry.insert(0, "Lazace1516@gmail.com")

pas_entry = Entry(width= 27)
pas_entry.grid(row= 3, column= 1)

gen_button = Button(text= "Generate password", command= generate_password, width= 16)
gen_button.grid(row= 3, column= 2)

add_button = Button(text= "Add", width= 44, command= save)
add_button.grid(row= 4, column= 1, columnspan=2)

search_button = Button(text= "Search", width= 16, command= find_password)
search_button.grid(row= 1, column=2)

window.mainloop()