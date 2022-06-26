import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def add_task():
    if task.get() != "":
        tasks_treeview.insert(parent="", index="end", values=(task.get().replace(" ", "\ ")))
        entry_field.delete(0, tk.END)
    else:
        print("Bitte einen Task eingeben...")

def delete_selected_task():
    selected_task = tasks_treeview.selection()
    if selected_task != ():
        tasks_treeview.delete(selected_task)
    else:
        print("Bitte einen Task markieren...")

def save_file():
    file_name = filedialog.asksaveasfilename(defaultextension=(".txt"), initialdir="C:/Users/fkotu/Desktop/todo", title="Datei speichern")
    if file_name:
        file = open(file_name, "w")
        for line in tasks_treeview.get_children():
            for value in tasks_treeview.item(line)["values"]:
                file.write(value + "\n")
        file.close()


def open_file():
    file_name = filedialog.askopenfilename(initialdir="C:/Users/fkotu/Desktop/todo", title="Datei öffnen")
    if file_name:
        file = open(file_name, "r")
        for line in file.readlines():
            tasks_treeview.insert(parent="", index=tk.END, values=(line.replace(" ", "\ ")))
        file.close()

root = tk.Tk()
root.geometry("700x340")
root.title("ToDo-Liste")
root.resizable(False, False)
root.columnconfigure(0, weight=1)

theme_style = ttk.Style()
theme_style.theme_use("clam")

task = tk.StringVar()

# Input Frame
input_frame = ttk.Frame(root, padding=5)
input_frame.grid(column=0, row=0)

task_label = ttk.Label(input_frame, text="Task:", font=("Roboto", 10), padding=5)
task_label.grid(column=0, row=0)

entry_field = ttk.Entry(input_frame, width=106, justify="left", textvariable=task)
entry_field.grid(column=1, row=0)

add_task_button = ttk.Button(input_frame, text="Task hinzufügen", command=add_task)
add_task_button.grid(column=0, row=1, columnspan=2, sticky="ew")

# Output Frame
output_frame = ttk.Frame(root, padding=5)
output_frame.grid(column=0, row=1)

tasks_treeview = ttk.Treeview(output_frame, selectmode="browse")
tasks_treeview.grid(column=0, row=0, sticky="ew")
tasks_treeview.configure(columns=("Tasks"))
tasks_treeview.column("Tasks", width=670)
tasks_treeview.column("#0", width=0, stretch=tk.NO)
tasks_treeview.heading("Tasks", text="Tasks")

tasks_scrollbar = ttk.Scrollbar(output_frame, orient="vertical", command=tasks_treeview.yview)
tasks_scrollbar.grid(column=1, row=0, sticky="ns")
tasks_treeview.configure(yscrollcommand=tasks_scrollbar.set)

delete_selected_task_button = ttk.Button(output_frame, width=106, text="Markierten Task entfernen", command=delete_selected_task)
delete_selected_task_button.grid(column=0, row=1, columnspan=2, sticky="ew")

#Menu mit Speichermechanismus
application_menu = tk.Menu(root)
root.configure(menu=application_menu)

file_menu = tk.Menu(application_menu)
file_menu.add_command(label="Datei speichern", command=save_file)
file_menu.add_command(label="Datei öffnen", command=open_file)

application_menu.add_cascade(label="Datei", menu=file_menu)

root.mainloop()