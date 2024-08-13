# MrJ
# Desktop Dashboard
# 7/25/2024


import tkinter as tk
from tkinter import messagebox, font
import requests
import time
import datetime
import os

TODO_FILE = "todo_list.txt"
LOCATION_FILE = "location.txt"


# Function to get weather data from wttr.in
def get_weather(location):
    try:
        url = f"https://wttr.in/{location}?format=%C+%t"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Error fetching weather data"
    except:
        weather_label.config(text="Error loading weather")


# Function to update time and date
def update_time_date():
    current_time = time.strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%m-%d-%Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time_date)


# Function to add a task to the to-do list
def add_task():
    task = task_entry.get()
    if task != "":
        todo_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


# Function to delete a selected task from the to-do list
def delete_task():
    try:
        selected_task_index = todo_list.curselection()[0]
        todo_list.delete(selected_task_index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")


# Function to move a task up
def move_up():
    try:
        selected_task_index = todo_list.curselection()[0]
        if selected_task_index != 0:
            task = todo_list.get(selected_task_index)
            todo_list.delete(selected_task_index)
            todo_list.insert(selected_task_index - 1, task)
            todo_list.selection_set(selected_task_index - 1)
            save_tasks()
    except:
        messagebox.showwarning("Warning", "You must select a task to move.")


# Function to move a task down
def move_down():
    try:
        selected_task_index = todo_list.curselection()[0]
        if selected_task_index != todo_list.size() - 1:
            task = todo_list.get(selected_task_index)
            todo_list.delete(selected_task_index)
            todo_list.insert(selected_task_index + 1, task)
            todo_list.selection_set(selected_task_index + 1)
            save_tasks()
    except:
        messagebox.showwarning("Warning", "You must select a task to move.")


# Function to update the weather
def update_weather():
    try:
        location = location_entry.get()
        if location:
            weather = get_weather(location)
            weather_label.config(text=weather)
            save_location(location)
        root.after(600000, update_weather)  # Update weather every 10 minutes
    except:
        weather_label.config(text="Error loading weather")


# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                todo_list.insert(tk.END, task.strip())


# Function to save tasks to the file
def save_tasks():
    tasks = todo_list.get(0, tk.END)
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Function to load location from the file
def load_location():
    if os.path.exists(LOCATION_FILE):
        with open(LOCATION_FILE, "r") as file:
            location = file.read().strip()
            return location
    return ""


# Function to save location to the file
def save_location(location):
    with open(LOCATION_FILE, "w") as file:
        file.write(location)


def about_click():
    messagebox.showinfo(
        "About",
        "TimeWise - A Simple To-Do Dashboard\n"
        f"\tCreated by MrJ\n\t         2024©"
    )


def help_click():
    messagebox.showinfo(
        "How To Use",
        "Enter your location to display the weather. Ensure it is in the following format: City, ST. "
        "For example, Los Angeles, CA. For international, follow the city with the two letter country code.\n\n"
        "Your location is automatically saved and loaded upon startup.\n\n"
        "Add to-do items to TimeWise by entering information below and clicking the \"Add Task\" button.\n\n"
        "Remove to-do items from TimeWise by selecting the item and clicking the \"Delete Task\" button.\n\n"
        "To move an item up on the list, select the item and click the \"Move Up\" button.\n\n"
        "To move an item down on the list, select the item and click the \"Move Down\" button.\n\n"
        "Your to-do list is automatically saved and loaded upon startup.\n\n"
        "To quit, use the file menu or the \"X\" button."
    )


def change_font_size(size):
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=size)

    location_label.config(font=default_font)
    location_entry.config(font=default_font)
    update_weather_button.config(font=default_font)
    todo_list.config(font=default_font)
    task_entry.config(font=default_font)
    add_button.config(font=default_font)
    delete_button.config(font=default_font)
    up_button.config(font=default_font)
    down_button.config(font=default_font)


def change_font_style(style):
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family=style)

    location_label.config(font=default_font)
    location_entry.config(font=default_font)
    update_weather_button.config(font=default_font)
    todo_list.config(font=default_font)
    task_entry.config(font=default_font)
    add_button.config(font=default_font)
    delete_button.config(font=default_font)
    up_button.config(font=default_font)
    down_button.config(font=default_font)

    time_label.config(font=(style, 48))
    date_label.config(font=(style, 24))
    weather_label.config(font=(style, 18))


def change_theme(theme):
    if theme == 'light':
        root.config(bg='white')
        menu.config(bg='white', fg='black')
        time_label.config(bg='white', fg='black')
        date_label.config(bg='white', fg='black')
        weather_frame.configure(bg='white')
        location_label.config(bg='white', fg='black')
        location_entry.config(bg='white', fg='black')
        update_weather_button.config(bg='white', fg='black')
        weather_label.config(bg='white', fg='black')
        todo_frame.configure(bg='white')
        todo_list.config(bg='white', fg='black')
        task_entry.config(bg='white', fg='black')
        add_button.config(bg='white', fg='black')
        delete_button.config(bg='white', fg='black')
        up_button.config(bg='white', fg='black')
        down_button.config(bg='white', fg='black')
    elif theme == 'dark':
        root.config(bg='#2e2e2e')
        menu.config(bg='#2e2e2e', fg='white')
        time_label.config(bg='#2e2e2e', fg='white')
        date_label.config(bg='#2e2e2e', fg='white')
        weather_frame.configure(bg='#2e2e2e')
        location_label.config(bg='#2e2e2e', fg='white')
        location_entry.config(bg='#2e2e2e', fg='white')
        update_weather_button.config(bg='#2e2e2e', fg='white')
        weather_label.config(bg='#2e2e2e', fg='white')
        todo_frame.configure(bg='#2e2e2e')
        todo_list.config(bg='#2e2e2e', fg='white')
        task_entry.config(bg='#2e2e2e', fg='white')
        add_button.config(bg='#2e2e2e', fg='white')
        delete_button.config(bg='#2e2e2e', fg='white')
        up_button.config(bg='#2e2e2e', fg='white')
        down_button.config(bg='#2e2e2e', fg='white')


# Main application window
root = tk.Tk()
root.title("TimeWise")

# Time label
time_label = tk.Label(root)
time_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Date label
date_label = tk.Label(root)
date_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Weather label and entry
weather_frame = tk.Frame(root)
weather_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

location_label = tk.Label(weather_frame, text="\t\tEnter Location:")
location_label.grid(row=0, column=0, padx=5, sticky="ew")

location_entry = tk.Entry(weather_frame)
location_entry.grid(row=0, column=1, padx=5)

update_weather_button = tk.Button(weather_frame, text="Update Weather", command=update_weather)
update_weather_button.grid(row=0, column=2, padx=5)

weather_label = tk.Label(weather_frame, text="")
weather_label.grid(row=1, column=0, columnspan=4, pady=5, sticky="nsew")

# To-do list
todo_frame = tk.Frame(root)
todo_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

todo_list = tk.Listbox(todo_frame, selectmode=tk.SINGLE, width=70, height=20)
todo_list.grid(row=0, column=0, columnspan=4, sticky="ew")

task_entry = tk.Entry(todo_frame, width=35)
task_entry.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

add_button = tk.Button(todo_frame, text="Add Task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

delete_button = tk.Button(todo_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

up_button = tk.Button(todo_frame, text="Move Up", command=move_up)
up_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

down_button = tk.Button(todo_frame, text="Move Down", command=move_down)
down_button.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

theme_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Themes", menu=theme_menu)
theme_menu.add_command(label="Light Theme", command=lambda: change_theme('light'))
theme_menu.add_command(label="Dark Theme", command=lambda: change_theme('dark'))

format_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Format", menu=format_menu)

# Font size submenu
font_size_menu = tk.Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font Size", menu=font_size_menu)
font_size_menu.add_command(label="Small", command=lambda: change_font_size(10))
font_size_menu.add_command(label="Medium", command=lambda: change_font_size(12))
font_size_menu.add_command(label="Large", command=lambda: change_font_size(14))

# Font style submenu
font_style_menu = tk.Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font Style", menu=font_style_menu)
font_style_menu.add_command(label="Arial", command=lambda: change_font_style("Arial"))
font_style_menu.add_command(label="Courier New", command=lambda: change_font_style("Courier New"))
font_style_menu.add_command(label="Helvetica", command=lambda: change_font_style("Helvetica"))
font_style_menu.add_command(
    label="Times New Roman",
    command=lambda: change_font_style("Times New Roman")
)
font_style_menu.add_command(label="Verdana", command=lambda: change_font_style("Verdana"))

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help", command=help_click)
help_menu.add_separator()
help_menu.add_command(label="About TimeWise", command=about_click)

# Load Default Settings
change_font_style("Arial")
change_font_size(12)
change_theme("light")

# Load tasks and location from files
load_tasks()
location = load_location()
if location:
    location_entry.insert(0, location)
    update_weather()

# Start the clock
update_time_date()

root.mainloop()
