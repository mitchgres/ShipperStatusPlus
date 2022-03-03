from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root_widget_ims_check_in_package = Tk()
root_widget_ims_check_in_package.title("ShipperStatusPlus - User IMS Check-In")
root_widget_ims_check_in_package.iconbitmap("logo_icon_ssp.ico")
root_widget_ims_check_in_package.geometry()

admin_package_ims_check_in_frame = Frame(root_widget_ims_check_in_package, padx=30, pady=30, background="#31117A")
admin_package_ims_check_in_frame.pack(fill=BOTH, expand=YES)
text_box_frame = Frame(admin_package_ims_check_in_frame, padx=10, pady=7, background="#31117A")
text_box_frame.grid(row=2, column=0, rowspan=4)

logo_image_init = Image.open("logo_picture_200_ssp.png")
image_resized = logo_image_init.resize((50, 50))
logo_image = ImageTk.PhotoImage(image_resized)
logo_image_label = Label(admin_package_ims_check_in_frame, image=logo_image)
title_label = Label(admin_package_ims_check_in_frame, text="User Inventory Management System Check-In", font='Helvetica 18 bold',
                    background="#31117A", foreground="#f2f2f2")
logo_image_label.grid(row=0, column=0, columnspan=2)

ims_check_in_package_label = Label(text_box_frame, text="Please Enter Location Of The Package In The IMS:", pady=7, background="#31117A",
                            foreground="#f2f2f2")
title_label.grid(row=1, column=0, columnspan=2, pady=10)

ims_check_in_package_label.grid(row=1, column=0, sticky="e", padx=5)

ims_package_check_in_package_entry= Entry(text_box_frame, width=50)
ims_package_check_in_package_entry.insert(0, "e.g. A6")

ims_package_check_in_package_entry.grid(row=1, column=1)

ims_check_in_package_database_button = Button(admin_package_ims_check_in_frame, padx=35, pady=0, text="Submit Information",
                                    background="#f2f2f2")
ims_check_in_package_database_button.grid(row=7, column=0, columnspan=2, pady=20)
root_widget_ims_check_in_package.mainloop()