from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

root_widget_login = Tk()
root_widget_login.title("ShipperStatusPlus - Admin User Information Update Screen")
root_widget_login.iconbitmap("logo_icon_ssp.ico")
root_widget_login.geometry()

admin_user_edit_frame = Frame(root_widget_login, padx=30, pady=30, background="#31117A")
admin_user_edit_frame.pack(fill=BOTH, expand=YES)
text_box_frame = Frame(admin_user_edit_frame, padx=10, pady=7, background="#31117A")
text_box_frame.grid(row=2, column=0, rowspan=4)

logo_image_init = Image.open("logo_picture_200_ssp.png")
image_resized = logo_image_init.resize((50, 50))
logo_image = ImageTk.PhotoImage(image_resized)
logo_image_label = Label(admin_user_edit_frame, image=logo_image)
title_label = Label(admin_user_edit_frame, text="Admin User Information Update", font='Helvetica 18 bold',
                    background="#31117A", foreground="#f2f2f2")

query_user_id_label = Label(text_box_frame, text="Please Enter User's Current ID:", pady=7, background="#31117A",
                            foreground="#f2f2f2", font='Helvetica 9 bold')
update_user_first_name_label = Label(text_box_frame, text="Update User First Name:", pady=7, background="#31117A",
                                     foreground="#f2f2f2")
update_user_last_name_label = Label(text_box_frame, text="Update User Last Name:", pady=7, background="#31117A",
                                    foreground="#f2f2f2")
update_user_id_label = Label(text_box_frame, text="Update User Company ID:", pady=7, background="#31117A",
                             foreground="#f2f2f2")
update_user_loc_label = Label(text_box_frame, text="Update User Office Location:", pady=7, background="#31117A",
                              foreground="#f2f2f2")
logo_image_label.grid(row=0, column=0, columnspan=2)
title_label.grid(row=1, column=0, columnspan=2, pady=10)

query_user_id_label.grid(row=1, column=0, sticky="e", padx=5)
update_user_first_name_label.grid(row=2, column=0, sticky="e", padx=5)
update_user_last_name_label.grid(row=3, column=0, sticky="e", padx=5)
update_user_id_label.grid(row=4, column=0, sticky="e", padx=5)
update_user_loc_label.grid(row=5, column=0, sticky="e", padx=5)

query_user_id_entry = Entry(text_box_frame, width=50)
update_user_first_name_entry = Entry(text_box_frame, width=50, state="disabled")
update_user_last_name_entry = Entry(text_box_frame, width=50, state="disabled")
update_user_id_entry = Entry(text_box_frame, width=50, state="disabled")
update_user_loc_entry = Entry(text_box_frame, width=50, state="disabled")


def query_database_for_id():
    update_user_first_name_entry["state"] = "normal"
    update_user_last_name_entry["state"] = "normal"
    update_user_id_entry["state"] = "normal"
    update_user_loc_entry["state"] = "normal"
    query_user_id_entry["state"] = "disabled"
    update_user_first_name_entry.insert(0, "CURRENT NAME PLACEHOLDER")
    update_user_last_name_entry.insert(0, "CURRENT NAME PLACEHOLDER")
    update_user_id_entry.insert(0, "CURRENT USER ID PLACEHOLDER")
    update_user_loc_entry.insert(0, "CURRENT OFFICE LOCATION PLACEHOLDER")
    check_user_database_button.destroy()
    update_user_database_button = Button(admin_user_edit_frame, padx=35, pady=0, text="Push To Database",
                                         background="#f2f2f2", command=pop_up_to_confirm)
    update_user_database_button.grid(row=7, column=0, columnspan=2, pady=20)

def pop_up_to_confirm():
    messagebox.askyesno("ShipperStatusPlus - Add User To Database Question", "Are you sure that you want to update this user's profile in the database?")

query_user_id_entry.grid(row=1, column=1)
update_user_first_name_entry.grid(row=2, column=1)
update_user_last_name_entry.grid(row=3, column=1)
update_user_id_entry.grid(row=4, column=1)
update_user_loc_entry.grid(row=5, column=1)

check_user_database_button = Button(admin_user_edit_frame, padx=35, pady=0, text="Search Database",
                                    background="#f2f2f2", command=query_database_for_id)
check_user_database_button.grid(row=7, column=0, columnspan=2, pady=20)
root_widget_login.mainloop()
