from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

root_widget_delete_package = Tk()
root_widget_delete_package.title("ShipperStatusPlus - Admin Package Delete Screen")
root_widget_delete_package.iconbitmap("logo_icon_ssp.ico")
root_widget_delete_package.geometry()

admin_package_delete_frame = Frame(root_widget_delete_package, padx=30, pady=30, background="#31117A")
admin_package_delete_frame.pack(fill=BOTH, expand=YES)
text_box_frame = Frame(admin_package_delete_frame, padx=10, pady=7, background="#31117A")
text_box_frame.grid(row=2, column=0, rowspan=4)

logo_image_init = Image.open("logo_picture_200_ssp.png")
image_resized = logo_image_init.resize((50, 50))
logo_image = ImageTk.PhotoImage(image_resized)
logo_image_label = Label(admin_package_delete_frame, image=logo_image)
title_label = Label(admin_package_delete_frame, text="Admin Package Delete", font='Helvetica 18 bold',
                    background="#31117A", foreground="#f2f2f2")
logo_image_label.grid(row=0, column=0, columnspan=2)

delete_package_label = Label(text_box_frame, text="Please Enter The Package ID You Want To Delete:", pady=7, background="#31117A",
                            foreground="#f2f2f2")
title_label.grid(row=1, column=0, columnspan=2, pady=10)

delete_package_label.grid(row=1, column=0, sticky="e", padx=5)

delete_package_entry= Entry(text_box_frame, width=50)
delete_package_entry.insert(0, "#000000")

def pop_up_to_confirm():
    messagebox.askyesno("ShipperStatusPlus - Delete Package Database Question", "Are you sure that you want to delete this package in the database?")

delete_package_entry.grid(row=1, column=1)

delete_package_database_button = Button(admin_package_delete_frame, padx=35, pady=0, text="Delete Package",
                                    background="#f2f2f2", command=pop_up_to_confirm)
delete_package_database_button.grid(row=7, column=0, columnspan=2, pady=20)
root_widget_delete_package.mainloop()