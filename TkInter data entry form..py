import tkinter
from tkinter import ttk #module that allow user to create modern application
from tkinter import messagebox 
import os
import openpyxl #library commonly used for different excel tools using python

#define enter_data command
def enter_data():
    accepted = accept_var.get()

    if accepted=="Accepted":
        #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            #Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numcourses_spinbox.get()

            print("Fist name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")

            filepath = "/Users/isfanfajarsukarno/Downloads/Data.xlsx"
            # - excel files stored place

            if not os.path.exists(filepath):
             # - create excel file using python
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["First Name", "Last Name", "Title", "Age", "Nationality",
                            "# Courses", "# Semesters", "Registration status"]
                sheet.append(heading)
                workbook.save(filepath)
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([firstname, lastname, title, age, nationality, numcourses,
                          numsemesters, registration_status])
            workbook.save(filepath)
                    
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

#Saving User Information in 1st label frame
user_info_frame =tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10) 
#pad or padding is used to create space around an element's content, inside any defined borders.

# - widget in 1st row (row 0 and row 1)
 # - widget label inside label frame at Saving User Information frame
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
 # - entries feature label
first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1) 
 # - widget label inside label frame at Saving User Information
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
 # - combobox allow users to choose from a selection from the values
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

# - widget in 2nd row (row 2 and row 3)
 # - use spinbox to count age
age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=0, to='infinity') # spinbox used as a counter for Age
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antartica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

# - configure each grid space in user_info_frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#saving Course info in 2nd label frame
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10) 
# - word "news" means expanded in every direction north, east, west, south.
# - then used padding as same as previous frame
# - A sticky element is anything that stays in 
#     a fixed position within the browser viewport 
#     as someone scrolls down a page.

#create registered label in 2nd label frame
registered_label = tkinter.Label(courses_frame, text="Registration Status")

# - widget label frame inside 2nd label frame saving at 2nd frame
reg_status_var = tkinter.StringVar(value="Not Registered") 
                                    # - Default value of reg_status_var is "Not Registered"
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", 
                                        variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
                                        # - "onvalue" when registration status button checked
                                        # - "offvalue" when registration status are unchecked
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

# - spinbox allow users to count the # Completed Courses
numcourses_label = tkinter.Label(courses_frame, text= "# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

# - spinbox allow users to count the # Completed Courses
numsemesters_label = tkinter.Label(courses_frame, text= "# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

# - configure each grid space in courses_frame
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept terms in 3rd label frame named terms_frame
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept terms and conditions.",
                                variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Button
button = tkinter.Button(frame, text="Enter data", command=enter_data) #command property mean that when click enter data button's go excecute function enter data
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()