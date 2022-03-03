from tkinter import *
import sqlite3
from PIL import ImageTk, Image

root_widget_user_selection = Tk()
root_widget_user_selection.title("ShipperStatusPlus - User Selection Screen")
root_widget_user_selection.iconbitmap("logo_icon_ssp.ico")
root_widget_user_selection.geometry()

user_selection_frame = Frame(root_widget_user_selection, padx=30, pady=30, background="#31117A")
user_selection_frame.pack(fill=BOTH, expand=YES)

logo_image_init = Image.open("logo_picture_200_ssp.png")
logo_image_resized = logo_image_init.resize((50, 50))
logo_image = ImageTk.PhotoImage(logo_image_resized)
logo_image_label = Label(user_selection_frame, image=logo_image)

title_label = Label(user_selection_frame, text="ShipperStatusPlus User Selection", font='Helvetica 18 bold', background="#31117A", foreground="#f2f2f2", pady=15)
user_id_information = Label(user_selection_frame, text="User ID: PLACEHOLDER TEXT", background="#31117A", foreground="#f2f2f2", pady=15)
instruct_text = Label(user_selection_frame, text="Please Select From One Of The Options Below", background="#31117A", foreground="#f2f2f2", pady=5)

user_radio_input = StringVar()
user_radio_input.set("Exit")

check_package_status_radio = Radiobutton(user_selection_frame, text="Check Package Status", variable=user_radio_input, value="Check", width=50, pady=7, background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold')
update_package_status_radio = Radiobutton(user_selection_frame, text="Update Package Status", variable=user_radio_input, value="Status", width=50, pady=7, background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold')
add_new_package_radio = Radiobutton(user_selection_frame, text="Add New Package", variable=user_radio_input, value="Add", width=50, pady=7, background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold')
exit_application_radio = Radiobutton(user_selection_frame, text="Exit Application", variable=user_radio_input, value="Exit", width=50, pady=7, background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold')

submit_button = Button(user_selection_frame, text="Submit", padx=35, pady=0, background="#f2f2f2")

logo_image_label.grid(row=0, column=0)
title_label.grid(row=1, column=0)
user_id_information.grid(row=2, column=0)
instruct_text.grid(row=3, column=0)
check_package_status_radio.grid(row=4, column=0)
update_package_status_radio.grid(row=5, column=0)
add_new_package_radio.grid(row=6, column=0)
exit_application_radio.grid(row=7, column=0)
submit_button.grid(row=8, column=0, pady=15)

root_widget_user_selection.mainloop()