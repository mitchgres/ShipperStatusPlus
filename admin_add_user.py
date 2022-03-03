from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

root_widget_login = Tk()
root_widget_login.title("ShipperStatusPlus - Admin User Information Add Screen")
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
title_label = Label(admin_user_edit_frame, text="Admin User Information Add", font='Helvetica 18 bold',
                    background="#31117A", foreground="#f2f2f2")

add_user_first_name_label = Label(text_box_frame, text="Add User's First Name:", pady=7, background="#31117A",
                                     foreground="#f2f2f2")
add_user_last_name_label = Label(text_box_frame, text="Add User's Last Name:", pady=7, background="#31117A",
                                    foreground="#f2f2f2")
add_user_id_label = Label(text_box_frame, text="Add User's Company ID:", pady=7, background="#31117A",
                             foreground="#f2f2f2")
add_user_loc_label = Label(text_box_frame, text="Add User's Office Location:", pady=7, background="#31117A",
                              foreground="#f2f2f2")
logo_image_label.grid(row=0, column=0, columnspan=2)
title_label.grid(row=1, column=0, columnspan=2, pady=10)

add_user_first_name_label.grid(row=1, column=0, sticky="e", padx=5)
add_user_last_name_label.grid(row=2, column=0, sticky="e", padx=5)
add_user_id_label.grid(row=3, column=0, sticky="e", padx=5)
add_user_loc_label.grid(row=4, column=0, sticky="e", padx=5)

add_user_first_name_entry = Entry(text_box_frame, width=50)
add_user_last_name_entry = Entry(text_box_frame, width=50)
add_user_id_entry = Entry(text_box_frame, width=50)
add_user_loc_entry = Entry(text_box_frame, width=50)


def pop_up_to_confirm():
    messagebox.askyesno("ShipperStatusPlus - Add User To Database Question", "Are you sure that you want to add this user to the database?")

add_user_first_name_entry.grid(row=1, column=1)
add_user_last_name_entry.grid(row=2, column=1)
add_user_id_entry.grid(row=3, column=1)
add_user_loc_entry.grid(row=4, column=1)

push_new_user_database_button = Button(admin_user_edit_frame, padx=35, pady=0, text="Push To Database",
                                    background="#f2f2f2", command=pop_up_to_confirm)
push_new_user_database_button.grid(row=7, column=0, columnspan=2, pady=20)
root_widget_login.mainloop()