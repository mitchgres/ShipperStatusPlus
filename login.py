from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root_widget_login = Tk()
root_widget_login.title("ShipperStatusPlus - User Login")
root_widget_login.iconbitmap("logo_icon_ssp.ico")
root_widget_login.geometry()

user_login_frame = Frame(root_widget_login, padx=30, pady=30, background="#31117A")
user_login_frame.pack(fill=BOTH, expand=YES)
text_box_frame =Frame(user_login_frame, padx=10, background="#31117A")
text_box_frame.grid(row=2, column=0, rowspan=4)

logo_image_init = Image.open("logo_picture_200_ssp.png")
logo_image = ImageTk.PhotoImage(logo_image_init)
logo_image_label = Label(user_login_frame, image=logo_image)
title_label = Label(user_login_frame, text="ShipperStatusPlus User Login", font='Helvetica 18 bold', background="#31117A", foreground="#f2f2f2")
f_name_label = Label(text_box_frame, text="Please Enter First Name:", pady=7, background="#31117A", foreground="#f2f2f2")
l_name_label = Label(text_box_frame, text="Please Enter Last Name:", pady=7, background="#31117A", foreground="#f2f2f2")
user_id_label = Label(text_box_frame, text="Please Enter Company ID Number:", pady=7, background="#31117A", foreground="#f2f2f2")
office_loc_label = Label(text_box_frame, text="Please Enter Your Office's Location:", pady=7, background="#31117A", foreground="#f2f2f2")
logo_image_label.grid(row=0, column=0, columnspan=2)
title_label.grid(row=1, column=0, columnspan=2, pady=10)
f_name_label.grid(row=1, column=0, sticky="e")
l_name_label.grid(row=2, column=0, sticky="e")
user_id_label.grid(row=3, column=0, sticky="e")
office_loc_label.grid(row=4, column=0, sticky="e")

f_name_entry = Entry(user_login_frame, width=50)
l_name_entry = Entry(user_login_frame, width=50)
user_id_entry = Entry(user_login_frame, width=50)
office_loc_entry = Entry(user_login_frame, width=50)
f_name_entry.grid(row=2, column=1)
l_name_entry.grid(row=3, column=1)
user_id_entry.grid(row=4, column=1)
office_loc_entry.grid(row=5, column=1)

user_login_button = Button(user_login_frame, padx=35, pady=0, text="Login", background="#f2f2f2")
user_login_button.grid(row=6, column=0, columnspan=2, pady=20)
root_widget_login.mainloop()

