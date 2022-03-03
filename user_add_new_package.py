from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image

root_widget_user_add_new_package = Tk()
root_widget_user_add_new_package.title("ShipperStatusPlus - User Package Add Screen")
root_widget_user_add_new_package.iconbitmap("logo_icon_ssp.ico")
root_widget_user_add_new_package.geometry()

def pop_up_to_confirm():
    messagebox_respon = messagebox.askyesno("ShipperStatusPlus - Add User To Database Question", "Are you sure that you want to add this package to the database?")
    if messagebox_respon == 0:
        messagebox.showwarning("ShipperStatusPlus - Redirecting Back To Menu", "You are being returned to the selection window.")

admin_user_new_package_frame = Frame(root_widget_user_add_new_package, padx=30, pady=30, background="#31117A")
admin_user_new_package_frame.pack(fill=BOTH, expand=YES)

logo_image_init = Image.open("logo_picture_200_ssp.png")
image_resized = logo_image_init.resize((50, 50))
logo_image = ImageTk.PhotoImage(image_resized)
logo_image_label = Label(admin_user_new_package_frame, image=logo_image)
title_label = Label(admin_user_new_package_frame, text="User New Package Add", font='Helvetica 18 bold',
                    background="#31117A", foreground="#f2f2f2")

add_shipping_id_label = Label(admin_user_new_package_frame, text="Enter Shipping ID Of Your Package:", pady=7, background="#31117A",
                                     foreground="#f2f2f2")
add_estimated_arrival_date_label = Label(admin_user_new_package_frame, text="Enter The Expected Arrival Date Of Your Package:", pady=7, background="#31117A",
                                    foreground="#f2f2f2")

select_dropoff_location_label = Label(admin_user_new_package_frame, text="Plese Select Where You Want You Package To Arrive", pady=7, background="#31117A",
                              foreground="#f2f2f2")

user_dropoff_input = StringVar()
user_dropoff_input.set("IMS")

dropoff_location_select_ims_radio = Radiobutton(admin_user_new_package_frame, text="Local Inventory Management System", variable=user_dropoff_input, value="IMS", width=50, pady=7, background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold')
dropoff_location_select_office_radio = Radiobutton(admin_user_new_package_frame, text="Personal Office Space", variable=user_dropoff_input, value="POS", width=50, pady=7, background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold')

add_shipping_id_entry = Entry(admin_user_new_package_frame, width=50)
add_estimated_arrival_date_entry = Entry(admin_user_new_package_frame, width=50)

add_estimated_arrival_date_entry.insert(0, "00/00/0000")

add_package_database_button = Button(admin_user_new_package_frame, padx=35, pady=0, text="Add To Database",
                                    background="#f2f2f2", command=pop_up_to_confirm)

logo_image_label.grid(row=0, column=0, columnspan=2)
title_label.grid(row=1, column=0, columnspan=2, pady=10)

add_shipping_id_label.grid(row=2, column=0, sticky="e", padx=5)
add_estimated_arrival_date_label.grid(row=3, column=0, sticky="e", padx=5)

add_shipping_id_entry.grid(row=2, column=1)
add_estimated_arrival_date_entry.grid(row=3, column=1)

select_dropoff_location_label.grid(row=4, columnspan=2, column=0, pady=10)
dropoff_location_select_ims_radio.grid(row=5, columnspan=2, column=0)
dropoff_location_select_office_radio.grid(row=6, columnspan=2, column=0)

add_package_database_button.grid(row=7, column=0, columnspan=2, pady=20)


root_widget_user_add_new_package.mainloop()