from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root_widget_user_check_in_package = Tk()
root_widget_user_check_in_package.title("ShipperStatusPlus - User Package Check-In Screen")
root_widget_user_check_in_package.iconbitmap("logo_icon_ssp.ico")
root_widget_user_check_in_package.geometry()

admin_user_check_in_package_frame = Frame(root_widget_user_check_in_package, padx=30, pady=30, background="#31117A")
admin_user_check_in_package_frame.pack(fill=BOTH, expand=YES)
check_in_package_label_frame = Frame(admin_user_check_in_package_frame, pady=10, padx=10, background="#31117A")

logo_image_init = Image.open("logo_picture_200_ssp.png")
logo_image_resized = logo_image_init.resize((50, 50))
logo_image = ImageTk.PhotoImage(logo_image_resized)
logo_image_label = Label(admin_user_check_in_package_frame, image=logo_image)

# Return info from database on current packages registered as not delivered yet for this user ID.
# It'll be returned in this format.
"""
TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Mushroom", "Mushroom"),
	("Onion", "Onion"),
]
"""
EXAMPLE_DATABASE_REPLY = [
    ("#5376765", "02/13/2022", "Not Arrived"),
    ("#9786087", "02/15/2022", "Not Arrived"),
    ("#4543578", "03/17/2022", "Not Arrived")
]
package_status_update_input = StringVar()

title_label = Label(admin_user_check_in_package_frame, text="ShipperStatusPlus User Check In Package", font='Helvetica 18 bold', background="#31117A", foreground="#f2f2f2", pady=15)
user_id_information = Label(admin_user_check_in_package_frame, text="User ID: PLACEHOLDER TEXT", background="#31117A", foreground="#f2f2f2", pady=15)
for package_id, date_arrival, arrival_status in EXAMPLE_DATABASE_REPLY:
    Radiobutton(check_in_package_label_frame, variable=package_status_update_input, value=f"{package_id}", text=f"Package ID: {package_id}, Expected Arrival Date: {date_arrival}, Status: {arrival_status}", pady=7, background="#31117A", foreground="#f2f2f2").pack()
back_to_selection_screen_button = Button(admin_user_check_in_package_frame, text=f"Please Deliver to John Doe's Office", padx=35, pady=0, background="#f2f2f2")


logo_image_label.grid(row=0, column=0)
title_label.grid(row=1, column=0)
user_id_information.grid(row=2, column=0)
check_in_package_label_frame.grid(row=3, column=0)
back_to_selection_screen_button.grid(row=4, column=0)

root_widget_user_check_in_package.mainloop()