from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

root_widget = Tk()
root_widget.title("ShipperStatusPlus - Admin User Information Delete Screen")
root_widget.iconbitmap("logo_icon_ssp.ico")
root_widget.geometry()

admin_user_delete_frame = Frame(root_widget, padx=30, pady=30, background="#31117A")
admin_user_delete_frame.pack(fill=BOTH, expand=YES)
text_box_frame = Frame(admin_user_delete_frame, padx=10, pady=7, background="#31117A")
text_box_frame.grid(row=2, column=0, rowspan=4)

logo_image_init = Image.open("logo_picture_200_ssp.png")
image_resized = logo_image_init.resize((50, 50))
logo_image = ImageTk.PhotoImage(image_resized)
logo_image_label = Label(admin_user_delete_frame, image=logo_image)
title_label = Label(admin_user_delete_frame, text="Admin User Information Delete", font='Helvetica 18 bold',
                    background="#31117A", foreground="#f2f2f2")
logo_image_label.grid(row=0, column=0, columnspan=2)

delete_user_id_label = Label(text_box_frame, text="Please Enter The User ID You Want To Delete:", pady=7, background="#31117A",
                            foreground="#f2f2f2")
title_label.grid(row=1, column=0, columnspan=2, pady=10)

delete_user_id_label.grid(row=1, column=0, sticky="e", padx=5)

delete_user_id_entry= Entry(text_box_frame, width=50)

def pop_up_to_confirm():
    messagebox.askyesno("ShipperStatusPlus - Add User To Database Question", "Are you sure that you want to delete this user's profile in the database?")

delete_user_id_entry.grid(row=1, column=1)

delete_user_database_button = Button(admin_user_delete_frame, padx=35, pady=0, text="Delete User Profile",
                                    background="#f2f2f2", command=pop_up_to_confirm)
delete_user_database_button.grid(row=7, column=0, columnspan=2, pady=20)
root_widget.mainloop()