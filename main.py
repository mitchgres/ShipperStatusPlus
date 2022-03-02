from tkinter import *
import sqlite3



root_widget = Tk()
root_widget.title("ShipperStatusPlus - Development Version")
root_widget.iconbitmap()  # FILL
root_widget.geometry()  # FILL
connect_database = sqlite3.connect("ShipperStatusPlus.db")
current_cursor = connect_database.cursor()
try:
    current_cursor.execute("""CREATE TABLE employee_information (
            first_name text,
            last_name text,
            employee_id_number text,
            office_location text
            )""")
except:
    print("File 'employee_information' Already Exists Continuing w/ Program Execution")
def employee_submit():
    """
    Again Only Used By Admins & Adds A New Entry To The Database
    :return:
    """
    connect_database = sqlite3.connect("ShipperStatusPlus.db")
    current_cursor = connect_database.cursor()
    current_cursor.execute("INSERT INTO employee_information VALUES (:first_name, :last_name, :employee_id_number, :office_location)",
        {
            "first_name": first_name_input.get(),
            "last_name": last_name_input.get(),
            "employee_id_number": employee_id_number_input.get(),
            "office_location": office_location_input.get()
        })
    connect_database.commit()
    connect_database.close()
def employee_query():
    """
    Will Be Used To Confirm If The User Is The Member Of Organization
    :return:
    """
    connect_database = sqlite3.connect("ShipperStatusPlus.db")
    current_cursor = connect_database.cursor()
    current_cursor.execute("SELECT * FROM employee_information")
    print(current_cursor.fetchall())
    all_records = current_cursor.fetchall()
    for record in all_records:
        print_records = record
    connect_database.commit()
    connect_database.close()

first_name_input = Entry(root_widget, width=50, borderwidth=5)
first_name_input.grid(row=0, column=1)
last_name_input = Entry(root_widget, width=50, borderwidth=5)
last_name_input.grid(row=1, column=1)
employee_id_number_input = Entry(root_widget, width=50, borderwidth=5)
employee_id_number_input.grid(row=2, column=1)
office_location_input = Entry(root_widget, width=50, borderwidth=5)
office_location_input.grid(row=3, column=1)

first_name_input_label = Label(root_widget, padx=10, pady=10, text="FIRST NAME")
first_name_input_label.grid(row=0, column=0)
last_name_input_label = Label(root_widget, padx=10, pady=10, text="LAST NAME")
last_name_input_label.grid(row=1, column=0)
employee_id_number_input_label = Label(root_widget, padx=10, pady=10, text="EMPLOYEE ID NUMBER")
employee_id_number_input_label.grid(row=2, column=0)
office_location_input_label = Label(root_widget, padx=10, pady=10, text="OFFICE LOCATION")
office_location_input_label.grid(row=3, column=0)

submit_button = Button(root_widget, text="ADD RECORDS TO DATABASE", command=employee_submit)
query_button = Button(root_widget, text="PRINT RECORDS", command=employee_query)
submit_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
query_button.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
connect_database.commit()
connect_database.close()
root_widget.mainloop()


