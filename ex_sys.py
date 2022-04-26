from tkinter import *
from tkinter import ttk
import pandas as pd 

# our main data source aka knowledge base
data = pd.read_csv(r"resources/dept_alloc.csv")

# config root window
root = Tk()
root.title("Department Eligibility System")
root.iconbitmap(r"resources/student.ico")
root.geometry('500x500+450+100')

# title on root window
head = Label(root, text="Department Eligibility System", font=("Calibri", 20)).pack()

# program actually starts from here
top = Toplevel()
top.geometry("500x200+450+250")
label = Label(top, text="Want to start department eligibility process?").place(relx=0.3, rely=0.2)

button = Button(top, text="Proceed", padx=5, pady=5, command=lambda:[physics(), top.destroy()]).place(relx=0.4, rely=0.35)


# open a toplevel window
# ask ques 
# get answer
# update dataframe
# close toplevel window
# repeat

# button reference for options in toplevel window
# opt_1 = Button(root, text="Below 16", padx=10, pady=10).place(relx=0.2, rely=0.15)
# opt_2 = Button(root, text="Equal to or More than 16", padx=10, pady=10).place(relx=0.5, rely=0.15)


def physics():
    top = Toplevel()
    top.geometry("500x200+450+250") # positioning: width x height + distance from left & top of screen
    lbl = Label(top, text="What was your physics score in admission test?").place(relx=0.3, rely=0.2)
    
    opt_l = Button(top, text="Below 15", padx=5, pady=5, command=lambda: [update_physics(), top.destroy()]).place(relx=0.2, rely=0.35)
    opt_2 = Button(top, text="Equal to or More than 15", padx=5, pady=5, command=lambda: [chemistry(), top.destroy()]).place(relx=0.5, rely=0.35)

def update_physics():
    global data
    data.drop(data[data.condition == "phy>=15"].index, inplace=True)
    chemistry()

def chemistry():
    top = Toplevel()
    top.geometry("500x200+450+250")
    lbl = Label(top, text="What was your chemistry score in admission test?").place(relx=0.3, rely=0.2)
    
    opt_1 = Button(top, text="Below 12", padx=5, pady=5, command=lambda: [update_chemistry(), top.destroy()]).place(relx=0.2, rely=0.35)
    opt_2 = Button(top, text="Equal to or More than 12", padx=5, pady=5, command=lambda: [math(), top.destroy()]).place(relx=0.5, rely=0.35)

def update_chemistry():
    global data
    data.drop(data[data.condition == "chem>=12"].index, inplace=True)
    math()

def math():
    top = Toplevel()
    top.geometry("500x200+450+250")
    lbl = Label(top, text="What was your mathematics score in admission test?").place(relx=0.3, rely=0.2)
    
    opt_1 = Button(top, text="Below 15", padx=5, pady=5, command=lambda: [update_math(), top.destroy()]).place(relx=0.2, rely=0.35)
    opt_2 = Button(top, text="Equal to or More than 15", padx=5, pady=5, command=lambda: [final_output(), top.destroy()]).place(relx=0.5, rely=0.35)

def update_math():
    global data
    data.drop(data[data.condition == "math>=15"].index, inplace=True)
    final_output()

def final_output():
    
    global data
    # converting dataframe into a list of lists
    data_rows = data.values.tolist()

    if len(data_rows) == 0:
        # no suitable dept found
        prompt = Label(root, text="Sorry, You're NOT Eligible for Admission", font=("Calibri", 16))
        prompt.place(width=500, rely=0.1)

    else:
        # create TreeView widget
        tv = ttk.Treeview(root)
        tv.place(relheight=0.6, relwidth=0.6, relx=0.2, rely=0.2)

        # configure widget adding scrollbar and stuff
        treescrolly = Scrollbar(head, orient="vertical", command=tv.yview) # command means update the yaxis view of the widget
        treescrollx = Scrollbar(head, orient="horizontal", command=tv.xview) # command means update the xaxis view of the widget
        tv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
        treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
        treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

        # specifying which column(s) to print
        tv["column"] = ["Department"] 
        tv["show"] = "headings"
        tv.heading(column="Department", text="Department")

        prompt = Label(root, text="You're Eligible for These Departments:", font=("Calibri", 16))
        prompt.place(width=500, rely=0.1)

        for row in data_rows:
            tv.insert("", "end", values=row)

    return None # just a good practice


root.mainloop()