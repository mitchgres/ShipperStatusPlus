"""
Program Title: ShipperStatusPlus
Program Author: Mitchell M. Gresham
Program Purpose: To allow an admin to manage a database of employees that are able to see where their packages
are in their organization.
Last Date Modified: 3/15/20
"""
from tkinter import *
from PIL import ImageTk
from PIL import Image
import database_interaction
from os import path
from tkinter import messagebox


#  Imports ness. lib. including a file that is local to the project.

class ShipperStatusPlus:
    """
    Class which contains the GUI for the application.
    """

    def __init__(self, root_widget):
        """
        Init. the root widget that will be used throughout the application and sets it to self.
        :param root_widget:
        """
        self.root_widget = root_widget
        if path.exists("setup_complete.txt"):  # Checks if the path to this text file exists, since that file is
            #  only created if the user had set up the application in the past if it is there it means everything
            #  has already been set up.
            self.login_screen()  # Go to log in screen if everything has already been set up.
        else:
            self.admin_setup_screen()  # If you haven't set up before go to the set-up screen.

    def admin_setup_screen(self):
        """
        Set up screen for the first person on the application who are admin by default.
        :return:
        """
        global image  # Refers to the global image since if not referred to globally then it won't show up.
        for value in self.root_widget.winfo_children():  # Deletes all other windows that may have been opened from
            #  the ShipperStatusPlus application.
            value.destroy()
        admin_setup = Frame(self.root_widget)  # Sets up a frame inside the root widget to be used.
        admin_setup.pack()
        self.root_widget.title("ShipperStatusPlus - Admin Setup Screen")  # Sets page title.
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets the logo to the page icon.

        admin_setup_frame = Frame(admin_setup, padx=30, pady=30, background="#31117A")  # Sets up another frame inside
        #  the previously declared admin_setup frame.
        admin_setup_frame.pack(fill=BOTH, expand=YES)  # Yes the frame can expand to fill the frame that it is in.
        text_box_frame = Frame(admin_setup_frame, padx=10, background="#31117A")  # Sets up a text box frame which will
        #  hold text inside the admin_set_up frame.
        text_box_frame.grid(row=2, column=0, rowspan=4)  # Fits text_box_frame into the grid.

        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png"))  # Sets up the main image on the page.
        logo_image_label = Label(admin_setup_frame, image=image, text="ShipperStatusPlus Logo")
        title_label = Label(admin_setup_frame, text="ShipperStatusPlus Admin Setup Screen", font='Helvetica 18 bold',
                            background="#31117A", foreground="#f2f2f2")  # Sets up the title on the page.
        f_name_label = Label(text_box_frame, text="Please Enter First Name:", pady=7, background="#31117A",
                             foreground="#f2f2f2")  # Label describing what to enter in the first name entry.
        l_name_label = Label(text_box_frame, text="Please Enter Last Name:", pady=7, background="#31117A",
                             foreground="#f2f2f2")  # Label describing what to enter in the last name entry.
        user_id_label = Label(text_box_frame, text="Please Enter Company ID Number:", pady=7, background="#31117A",
                              foreground="#f2f2f2")  # Label describing what to enter in the ID entry.
        office_loc_label = Label(text_box_frame, text="Please Enter Your Office's Location:", pady=7,
                                 background="#31117A", foreground="#f2f2f2")  # Label describing what to enter in the
        # location entry.
        logo_image_label.grid(row=0, column=0, columnspan=2)  # Sets widgets to their respective position in the grid.
        title_label.grid(row=1, column=0, columnspan=2, pady=10)
        f_name_label.grid(row=1, column=0, sticky="e")  # Also sets them to stick to the right side of the screen.
        l_name_label.grid(row=2, column=0, sticky="e")
        user_id_label.grid(row=3, column=0, sticky="e")
        office_loc_label.grid(row=4, column=0, sticky="e")

        f_name_entry = Entry(admin_setup_frame,
                             width=50)  # Sets up entires which are described by the labels and are where
        #  the user can enter the values.
        l_name_entry = Entry(admin_setup_frame, width=50)
        user_id_entry = Entry(admin_setup_frame, width=50)
        office_loc_entry = Entry(admin_setup_frame, width=50)
        f_name_entry.grid(row=2, column=1)  # Applies these entries to the grid.
        l_name_entry.grid(row=3, column=1)
        user_id_entry.grid(row=4, column=1)
        office_loc_entry.grid(row=5, column=1)

        def change_to_login():
            """
            Changes the page to the login pack and setups up the application using the values that were passed into
            the entry boxes.
            :return:
            """
            database_interaction.setup_app(database_connection="ShipperStatusPlus.db",  # Makes the first user, and
                                           #  creates the database.
                                           name=f"{f_name_entry.get()} {l_name_entry.get()}",
                                           id=user_id_entry.get(),
                                           location=office_loc_entry.get(),
                                           packages=database_interaction.package_defaults())
            self.login_screen()  # Goes to the login page.
            return None  # Just used to signal the end of the function declaration.

        admin_setup_button = Button(admin_setup_frame, padx=35, pady=0, text="Finish Setup", background="#f2f2f2",
                                    command=change_to_login)
        #  Button which is used to activate the setup and apply the values passed into the entries.
        admin_setup_button.grid(row=6, column=0, columnspan=2, pady=20)

    def login_screen(self):
        """
        Login screen for both users and admins.
        :return:
        """
        global image  # Refers to the global image for the image on the page.
        for value in self.root_widget.winfo_children():  # Destroys all other windows.
            value.destroy()
        self.root_widget.title("ShipperStatusPlus - Login")  # Sets title
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets icon.

        user_login_frame = Frame(self.root_widget, padx=30, pady=30, background="#31117A")  # Declares frame which
        #  all the content will go in.
        user_login_frame.pack(fill=BOTH, expand=YES)  # Yes it'll fill the root widget
        text_box_frame = Frame(user_login_frame, padx=10, background="#31117A")  # Text box frame for some text
        #  content on the page.
        text_box_frame.grid(row=2, column=0, rowspan=4)

        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png"))  # Declares and sets the image to a
        #  label widget.
        logo_image_label = Label(user_login_frame, image=image, text="ShipperStatusPlus Logo")
        """
        The following labels are used to describe the entry widgets which are located to the right of them. 
        """
        title_label = Label(user_login_frame, text="ShipperStatusPlus Login", font='Helvetica 18 bold',
                            background="#31117A", foreground="#f2f2f2")
        f_name_label = Label(text_box_frame, text="Please Enter First Name:", pady=7, background="#31117A",
                             foreground="#f2f2f2")
        l_name_label = Label(text_box_frame, text="Please Enter Last Name:", pady=7, background="#31117A",
                             foreground="#f2f2f2")
        user_id_label = Label(text_box_frame, text="Please Enter Company ID Number:", pady=7, background="#31117A",
                              foreground="#f2f2f2")
        office_loc_label = Label(text_box_frame, text="Please Enter Your Office's Location:", pady=7,
                                 background="#31117A", foreground="#f2f2f2")
        logo_image_label.grid(row=0, column=0, columnspan=2)  # Formats the widgets in the grid in the frame.
        title_label.grid(row=1, column=0, columnspan=2, pady=10)
        f_name_label.grid(row=1, column=0, sticky="e")
        l_name_label.grid(row=2, column=0, sticky="e")
        user_id_label.grid(row=3, column=0, sticky="e")
        office_loc_label.grid(row=4, column=0, sticky="e")

        """
        Declares the entries that are used to take input from the user for their login. 
        """
        f_name_entry = Entry(user_login_frame, width=50)
        l_name_entry = Entry(user_login_frame, width=50)
        user_id_entry = Entry(user_login_frame, width=50)
        office_loc_entry = Entry(user_login_frame, width=50)
        f_name_entry.grid(row=2, column=1)  # Formats the entries in the grid.
        l_name_entry.grid(row=3, column=1)
        user_id_entry.grid(row=4, column=1)
        office_loc_entry.grid(row=5, column=1)

        def not_auth_warning():
            """
            Called when the values which the user has entered don't match those in the database
            :return:
            """
            # Message box which notifies the user the values they've entered are incorrect.
            messagebox.showwarning("ShipperStatusPlus - Not Authorized User",
                                   "The password or name you entered is incorrect. Please try again.")

            self.login_screen()  # Reloads the login screen.

        def check_user_input():
            """
            Checks if the inputs from the user match those that are in the database, and then redirect to the
            appropriate page depending on if they're admin or user.
            :return:
            """
            global m_user_id  # Global variable of the id of the user, which will be referenced through the app.
            global m_user_status  # Global variable of the status of the user which will determine the privileges
            #  of the user in the app.
            if database_interaction.check_user_auth(
                    database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                    id=user_id_entry.get(), name=f"{f_name_entry.get()} {l_name_entry.get()}"):
                #  Checks if the user id and name match.
                if database_interaction.check_if_admin(
                        database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                        id=user_id_entry.get()):
                    #  Checks if the user is an admin, and gets admin privileges.
                    m_user_id = user_id_entry.get()  # If the user is admin update status and id to reflect that.
                    m_user_status = "Admin"
                    self.admin_selection()  # Redirect to the admin selection page.
                else:  # If the user isn't an admin...
                    """
                    If any of the values in the database are null it returns a value even though it shouldn't the series
                    of if-else statements prevents any of the entry boxes to go unfilled. 
                    """
                    if f_name_entry.get() == "":
                        not_auth_warning()  # Calls to tell the user their entry is wrong and reloads app.
                    elif l_name_entry.get() == "":
                        not_auth_warning()
                    elif user_id_entry.get() == "":
                        not_auth_warning()
                    else:  # If nothing isn't filled...
                        m_user_id = user_id_entry.get()  # Then authenticate the user as a user and set id and status.
                        m_user_status = "User"
                        self.user_selection()  # Redirect to the user selection page.
            else:  # If the user's name and ID don't match then they are notified and then app reloads.
                not_auth_warning()

        user_login_button = Button(user_login_frame, padx=35, pady=0, text="Login", background="#f2f2f2",
                                   command=check_user_input)  # Submits the entry data.
        user_login_button.grid(row=6, column=0, columnspan=2, pady=20)

    def admin_selection(self):
        """
        The page reserved for admins which is meant to be a menu for the rest of the pages of the applications.
        :return:
        """
        global image  # Sets the scope for the var. image to global
        global m_user_id  # Sets the scope of the var. user id, and status to global which were declared in the login.
        global m_user_status
        for value in self.root_widget.winfo_children():  # Destroys all other windows of the application.
            value.destroy()
        self.root_widget.title("ShipperStatusPlus - Admin Selection Screen")  # Sets title
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets the icon to the logo.

        #  Sets the frame by which all the content in the page will go in.
        admin_selection_frame = Frame(self.root_widget, padx=30, pady=30, background="#31117A")
        admin_selection_frame.pack(fill=BOTH, expand=YES)  # Yes the frame can fill the root widget.

        # Declares the logo to be used on the page, though resizes the image to take up less space (50x50)
        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png").resize((50, 50)))
        logo_image_label = Label(admin_selection_frame, image=image, text="ShipperStatusPlus Logo")

        # Declares the title label which has the title for the application page.
        title_label = Label(admin_selection_frame, text="ShipperStatusPlus Admin Selection", font='Helvetica 18 bold',
                            background="#31117A", foreground="#f2f2f2", pady=15)
        # Declares another label which shows the information to the user about their status and ID.
        user_id_information = Label(admin_selection_frame, text=f"ADMIN ID: {m_user_id}", background="#31117A",
                                    foreground="#f2f2f2", pady=15)
        # Declares a label which instructs the user what to do on the page.
        instruct_text = Label(admin_selection_frame, text="Please Select From One Of The Options Below",
                              background="#31117A", foreground="#f2f2f2", pady=5)

        # Variable used to store the value of the radio buttons and by default is set to exit the application.
        admin_radio_input = StringVar()
        admin_radio_input.set("Exit")

        """
        The following are radio buttons in the frame which represent the various actions which someone with admin
        privileges can do. 
        """
        check_package_status_radio = Radiobutton(admin_selection_frame, text="Check Package Status",
                                                 variable=admin_radio_input, value="Check", width=50, pady=7,
                                                 background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold',
                                                 selectcolor="#393d3d")
        update_package_status_radio = Radiobutton(admin_selection_frame, text="Update Package Status",
                                                  variable=admin_radio_input, value="Status", width=50, pady=7,
                                                  background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold',
                                                  selectcolor="#393d3d")
        edit_user_radio = Radiobutton(admin_selection_frame, text="Edit User Information", variable=admin_radio_input,
                                      value="Edit User", width=50, pady=7, background="#31117A", foreground="#f2f2f2",
                                      font='Helvetica 11 bold', selectcolor="#393d3d")
        exit_application_radio = Radiobutton(admin_selection_frame, text="Exit Application", variable=admin_radio_input,
                                             value="Exit", width=50, pady=7, background="#31117A", foreground="#f2f2f2",
                                             font='Helvetica 11 bold', selectcolor="#393d3d")

        def application_is_closing():
            """
            Notified the user through a message box that the application is about to close and then does that.
            :return:
            """
            messagebox.showwarning("ShipperStatusPlus - Action Required", "Application is now closing.")
            self.root_widget.destroy()

        def next_page():
            """
            Moves the admin to the next page which they selected in the radio button which they chose.
            :return:
            """
            if admin_radio_input.get() == "Check":
                self.admin_check_package_status()
            elif admin_radio_input.get() == "Status":
                self.user_update_package_status()
            elif admin_radio_input.get() == "Edit User":
                self.admin_user_selection()
            elif admin_radio_input.get() == "Exit":
                application_is_closing()

        submit_button = Button(admin_selection_frame, text="Submit", padx=35, pady=0, background="#f2f2f2",
                               command=next_page)  # Button which moves the user to the page which they selected.

        """
        The following formats the widgets previously declared in a grid format on the frame. 
        """
        logo_image_label.grid(row=0, column=0)
        title_label.grid(row=1, column=0)
        user_id_information.grid(row=2, column=0)
        instruct_text.grid(row=3, column=0)
        check_package_status_radio.grid(row=4, column=0)
        update_package_status_radio.grid(row=5, column=0)
        edit_user_radio.grid(row=6, column=0)
        exit_application_radio.grid(row=7, column=0)
        submit_button.grid(row=8, column=0, pady=15)

    def admin_check_package_status(self):
        """
        Page which the admin can use to check the status of any user in the database as requested.
        :return:
        """
        global image  # Global image so that can be displayed, since can't be referenced locally.
        global m_user_status  # Global of the users status and their id for display.
        global m_user_id
        for value in self.root_widget.winfo_children():  # Destroys the previous screens.
            value.destroy()
        self.root_widget.title("ShipperStatusPlus - User Check Package Screen")  # Sets title
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets icon to logo.

        """
        The following declares three frames, the first one has all content in the page and can fill the root widget, 
        the second displays the return list of all of packages for a user in a database, and the last one holds the 
        label and entry for the input from the user. 
        """
        admin_user_check_package_frame = Frame(self.root_widget, padx=30, pady=30, background="#31117A")
        admin_user_check_package_frame.pack(fill=BOTH, expand=YES)
        check_status_label_frame = Frame(admin_user_check_package_frame, pady=10, padx=10, background="#31117A")
        label_and_entry_frame = Frame(admin_user_check_package_frame, padx=10, pady=10, background="#31117A")

        #  Sets the logo to an image in the app being resized to look good.
        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png").resize((50, 50)))
        logo_image_label = Label(admin_user_check_package_frame, image=image)

        #  Title which describes the general purpose of the application page.
        title_label = Label(admin_user_check_package_frame, text="ShipperStatusPlus User Check Package Status",
                            font='Helvetica 18 bold', background="#31117A", foreground="#f2f2f2", pady=15)

        #  Label which displays the user's status and id.
        user_id_information = Label(admin_user_check_package_frame, text=f"{m_user_status} ID: {m_user_id}",
                                    background="#31117A", foreground="#f2f2f2", pady=15)

        #  Sets a label to describe what to do in the entry box, both of which are in the label and entry frame.
        package_id_search_label = Label(label_and_entry_frame, text="Please Enter ID You Want To Search For: ",
                                        background="#31117A", foreground="#f2f2f2", pady=15, padx=50)
        package_id_search_entry = Entry(label_and_entry_frame, width=50)
        package_id_search_label.grid(row=0, column=0,
                                     padx=7)  # Formats the label and entry in the label and entry frame.
        package_id_search_entry.grid(row=0, column=1)

        def back_to_selection_admin():
            """
            Returns to the admin selection screen once finished on this page.
            :return:
            """
            self.admin_selection()

        #  Button which returns the user back to the admin selection page.
        back_to_selection_screen_button = Button(admin_user_check_package_frame, text="Back To Selection Screen",
                                                 padx=35,
                                                 pady=0, background="#f2f2f2", command=back_to_selection_admin)

        def generate_user_packages():
            """
            Generates the list of pacakges for a user in the frame for displaying the packages, and also formats them.
            :return:
            """
            global back_to_selection_screen_button  # Global reference to the selection screen button so it can be used
            #  outside its scope above.
            try:  # Checks if the user exists and then if it does return if there are package or not, and then prints
                #  the list to the frame.
                for values in database_interaction.get_package_from_id(
                        # Goes through all packages in the database which
                        #  are registered to that user and see if any of those are 000000 which indicates that there are no packages,
                        #  though if not then it prints the packages.
                        database_interaction.create_database("ShipperStatusPlus.db"),
                        id_search=package_id_search_entry.get()):
                    if values == "000000":
                        package_return = Label(check_status_label_frame, text="No Packages Assigned To This User")
                        package_return.pack()
                        submit_id_button["state"] = "disabled"  # So you can't submit again and mess it up.
                        break
                    else:
                        #  Updates the frame so that it contains the list of values of packages that are ass. with that user.
                        package_return = Label(check_status_label_frame,
                                               text=f"Package ID {values}, Expected Arrival Date: {database_interaction.get_package_arrival_date(database_interaction.create_database('ShipperStatusPlus.db'), package_id=values)} Package IMS Location: {database_interaction.get_package_location_ims(database_connection=database_interaction.create_database('ShipperStatusPlus.db'), package_id=values)}")
                        package_return.pack()
            except IndexError:  # If there is an IndexError it means that the user doesn't exist in the database, and
                #  in that case then notify the user though the message box and allow them to try again.
                messagebox.showwarning("ShipperStatusPlus - Action Required",
                                       "The user you've entered doesn't exist please try again.")

        #  Submits button which activates the function which prints the user's packages.
        submit_id_button = Button(admin_user_check_package_frame, text="Find Packages", padx=35, pady=0,
                                  background="#f2f2f2", command=generate_user_packages)

        """
        The following formats the various widgets in a grid pattern in the frame. 
        """
        logo_image_label.grid(row=0, column=0, columnspan=2)
        title_label.grid(row=1, column=0, columnspan=2)
        user_id_information.grid(row=2, column=0, columnspan=2)
        label_and_entry_frame.grid(row=3, column=0, columnspan=2)
        check_status_label_frame.grid(row=4, column=0, columnspan=2)
        submit_id_button.grid(row=5, column=0, columnspan=2, pady=5)
        back_to_selection_screen_button.grid(row=6, column=0, columnspan=2)

    def user_update_package_status(self):
        """
        Application page which updates the status of the package, which can be access by both the admin and the user
        since both have the ability to check in packages to the IMS.
        :return:
        """
        global image  # Global reference to image which is the logo that is used in the app page
        global m_user_id  # ID and Status which are used to check privileges if applicable.
        global m_user_status
        global m_package_to_check_in  # Global reference to the package which the used is going to check in on this
        # page.
        for value in self.root_widget.winfo_children():
            value.destroy()  # Destroys other pages of app.
        self.root_widget.title("ShipperStatusPlus - User Package Check-In Screen")  # Sets title
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets logo as icon

        # Declares a frame which holds all the content on the page and says that it should fill the root.
        admin_user_check_in_package_frame = Frame(self.root_widget, padx=30, pady=30,
                                                  background="#31117A")
        admin_user_check_in_package_frame.pack(fill=BOTH, expand=YES)
        #  Frame to hold content that relates to the check in package label.
        check_in_package_label_frame = Frame(admin_user_check_in_package_frame, pady=10, padx=10, background="#31117A")

        # Declares the image to be used in the application.
        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png").resize((50, 50)))
        logo_image_label = Label(admin_user_check_in_package_frame, image=image)

        # Var. which is referenced to determine the value of the radio buttons, and sets the default to none.
        # which has no value in the application.
        package_status_update_input = StringVar()
        package_status_update_input.set("None")

        # Declare a label which describes the purpose of the page as a title.
        title_label = Label(admin_user_check_in_package_frame, text="ShipperStatusPlus User Check In Package",
                            font='Helvetica 18 bold', background="#31117A", foreground="#f2f2f2", pady=15)

        # Displays to the user their status and is number to ensure it's correct.
        user_id_information = Label(admin_user_check_in_package_frame, text=f"{m_user_status} ID: {m_user_id}",
                                    background="#31117A", foreground="#f2f2f2", pady=15)

        # Displays all the undelivered packages in the database, and asks the user to select one to check in. It'll
        # display these values as radio button to select by the user.
        for values in database_interaction.get_all_undelivered_packages(
                database_connection=database_interaction.create_database("ShipperStatusPlus.db")):
            Radiobutton(check_in_package_label_frame, variable=package_status_update_input, value=values,
                        text=f"Package ID {values}, Expected Arrival Date: {database_interaction.get_package_arrival_date(database_interaction.create_database('ShipperStatusPlus.db'), package_id=values)} Package IMS Location: {database_interaction.get_package_location_ims(database_connection=database_interaction.create_database('ShipperStatusPlus.db'), package_id=values)}"
                        , pady=7, background="#31117A", foreground="#f2f2f2", selectcolor="#393d3d").pack()

        def check_in_package():
            """
            Sets the value of the package which the user wants to check in the global reference of the package.
            :return:
            """
            global m_package_to_check_in
            m_package_to_check_in = package_status_update_input.get()
            self.user_inventory_check_in()  # Goes to the next page to check in package.

        # Declares the button which is used to set the value of the package selected to the global reference of
        # that value.
        check_package_in_button = Button(admin_user_check_in_package_frame,
                                         text=f"Check Package Into IMS System", padx=35, pady=0,
                                         background="#f2f2f2", command=check_in_package)

        """
        Formats widgets onto the frame in the page. 
        """
        logo_image_label.grid(row=0, column=0)
        title_label.grid(row=1, column=0)
        user_id_information.grid(row=2, column=0)
        check_in_package_label_frame.grid(row=3, column=0)
        check_package_in_button.grid(row=4, column=0)

    def user_inventory_check_in(self):
        """
        Page which checks the package that is a global var. to a new value in the IMS system, updating status, and
        the expected arrival date.
        :return:
        """
        global image  # Global reference to the image logo that is used throughout the program
        global m_package_to_check_in  # Global reference to the package which was selected on the previous page.
        for value in self.root_widget.winfo_children():
            value.destroy()  # Destroy all other windows in the application.
        self.root_widget.title("ShipperStatusPlus - User IMS Check-In")  # Sets title.
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets icon to logo

        # Declares frame which all the content in the page is going to be in, and it can fill the entire root.
        admin_package_ims_check_in_frame = Frame(self.root_widget, padx=30, pady=30,
                                                 background="#31117A")
        admin_package_ims_check_in_frame.pack(fill=BOTH, expand=YES)

        # Declares another frame which is a text box to hold the labels for the entry.
        text_box_frame = Frame(admin_package_ims_check_in_frame, padx=10, pady=7, background="#31117A")
        text_box_frame.grid(row=2, column=0, rowspan=4)

        # Declares the image to be used in the page.
        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png").resize((50, 50)))
        logo_image_label = Label(admin_package_ims_check_in_frame, image=image)

        # Title label which declares the general purpose of the page.
        title_label = Label(admin_package_ims_check_in_frame, text="User Inventory Management System Check-In",
                            font='Helvetica 18 bold',
                            background="#31117A", foreground="#f2f2f2")
        logo_image_label.grid(row=0, column=0, columnspan=2)  # Formats the logo

        # Declares a label that describes the purpose of the entry box that is next to it.
        ims_check_in_package_label = Label(text_box_frame, text="Please Enter Location Of The Package In The IMS:",
                                           pady=7, background="#31117A",
                                           foreground="#f2f2f2")
        title_label.grid(row=1, column=0, columnspan=2, pady=10)  # Formats title

        # Formats the label
        ims_check_in_package_label.grid(row=1, column=0, sticky="e", padx=5)

        # Declares the entry box that is used to enter the new location of the package.
        ims_package_check_in_package_entry = Entry(text_box_frame, width=50)
        # Inserts an example to show the user what effective use of the IMS looks like.
        ims_package_check_in_package_entry.insert(0, "e.g. A6")
        # Formats the entry
        ims_package_check_in_package_entry.grid(row=1, column=1)

        def check_package_in():
            """
            If values other than null and default are entered then it'll set the new status of the package to arrived
            and update the location in the IMS system.
            :return:
            """
            if ims_package_check_in_package_entry.get() != " " and ims_package_check_in_package_entry.get() != "e.g. A6":
                # If it isn't the values that were given as example or null...
                # then update the database to reflect that the package has arrived.
                database_interaction.set_package_arrival_date(
                    database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                    package_id=m_package_to_check_in, new_arrival_date="Arrived")
                database_interaction.set_package_location_ims(
                    database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                    package_id=m_package_to_check_in, new_location=ims_package_check_in_package_entry.get())
                # Message box which notifies the user that their changes have been made, and they are being taken back
                # to the login page.
                messagebox.showwarning("ShipperStatusPlus - Action Required",
                                       "Updates have been made, redirecting to the previous page.")
                self.login_screen()
            else:
                # Else if the values aren't anything new then reload the page after notifying the user.
                messagebox.showwarning("ShipperStatusPlus - Action Required",
                                       "The values which you've entered are null, please enter a correct location")
                self.user_inventory_check_in()

        # Declares button which is used to update the database with the new information.
        ims_check_in_package_database_button = Button(admin_package_ims_check_in_frame, padx=35, pady=0,
                                                      text="Submit Information",
                                                      background="#f2f2f2", command=check_package_in)
        ims_check_in_package_database_button.grid(row=7, column=0, columnspan=2, pady=20)  # Formats the button

    def admin_user_selection(self):
        """
        Page reserved for admins where they can select things which they are able to users in the database.
        :return:
        """
        global image  # Refers to global image that is the logo that is used on the page.
        for value in self.root_widget.winfo_children():
            value.destroy()  # Destroys all the previous windows.
        self.root_widget.title("ShipperStatusPlus - Admin User Selection Screen")  # Sets title
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets icon to the logo

        # Frame which contains all the content for the page that can fill the root that it's in.
        admin_user_selection_frame = Frame(self.root_widget, padx=30, pady=30, background="#31117A")
        admin_user_selection_frame.pack(fill=BOTH, expand=YES)

        # Sets the logo to a label that is an image on the page.
        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png").resize((50, 50)))
        logo_image_label = Label(admin_user_selection_frame, image=image)

        # Title which describes the purpose of this page.
        title_label = Label(admin_user_selection_frame, text="ShipperStatusPlus Admin User Selection",
                            font='Helvetica 18 bold', background="#31117A", foreground="#f2f2f2", pady=15)

        # Label which contains information about the user
        user_id_information = Label(admin_user_selection_frame, text="User ID: ADMIN ID", background="#31117A",
                                    foreground="#f2f2f2", pady=15)

        # Instructional text which tells the user what to do on the page.
        instruct_text = Label(admin_user_selection_frame, text="Please Select From One Of The Options Below",
                              background="#31117A", foreground="#f2f2f2", pady=5)

        # Variable which is used to get the value of the radio buttons, though it's default is to leave the app.
        admin_radio_input = StringVar()
        admin_radio_input.set("Exit")

        """
        The following are radio buttons which represent the options that the admin has to do on the page. 
        """
        update_user_info_radio = Radiobutton(admin_user_selection_frame, text="Update Current User Information",
                                             variable=admin_radio_input, value="Update", width=50, pady=7,
                                             background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold',
                                             selectcolor="#393d3d")
        delete_user_radio = Radiobutton(admin_user_selection_frame, text="Delete Current User",
                                        variable=admin_radio_input, value="Delete", width=50, pady=7,
                                        background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold',
                                        selectcolor="#393d3d")
        add_new_user_radio = Radiobutton(admin_user_selection_frame, text="Add New User", variable=admin_radio_input,
                                         value="Add", width=50, pady=7, background="#31117A", foreground="#f2f2f2",
                                         font='Helvetica 11 bold', selectcolor="#393d3d")
        exit_application_radio = Radiobutton(admin_user_selection_frame, text="Exit Application",
                                             variable=admin_radio_input, value="Exit", width=50, pady=7,
                                             background="#31117A", foreground="#f2f2f2", font='Helvetica 11 bold',
                                             selectcolor="#393d3d")

        def application_is_closing():
            """
            Notifies the user though a message box that the application is closing and then destroys the root.
            :return:
            """
            messagebox.showwarning("ShipperStatusPlus - Action Required", "Application is now closing.")
            self.root_widget.destroy()

        def next_page():
            """
            Moves the admin on the next page which they've selected in the radio buttons.
            :return:
            """
            if admin_radio_input.get() == "Update":
                self.admin_update_user()
            elif admin_radio_input.get() == "Delete":
                self.admin_delete_user()
            elif admin_radio_input.get() == "Add":
                self.admin_add_user()
            elif admin_radio_input.get() == "Exit":
                application_is_closing()

        # Submit button which is used to move the user onto the next page.
        submit_button = Button(admin_user_selection_frame, text="Submit", padx=35, pady=0, background="#f2f2f2",
                               command=next_page)

        """
        The following formats all of the widgets onto the frame in a grid system. 
        """
        logo_image_label.grid(row=0, column=0)
        title_label.grid(row=1, column=0)
        user_id_information.grid(row=2, column=0)
        instruct_text.grid(row=3, column=0)
        update_user_info_radio.grid(row=4, column=0)
        delete_user_radio.grid(row=5, column=0)
        add_new_user_radio.grid(row=6, column=0)
        exit_application_radio.grid(row=7, column=0)
        submit_button.grid(row=8, column=0, pady=15)

    def admin_update_user(self):
        """
        Page which provides the admin to update the name and location of the user and ID is constant.
        :return:
        """
        global image  # Global reference to the image which is the logo for the application.
        for value in self.root_widget.winfo_children():
            value.destroy()  # Destroys all the previous widgets in the application.
        self.root_widget.title("ShipperStatusPlus - Admin User Information Update Screen")  # Sets title
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets logo to the icon.

        """
        First frame declared is the frame which all content in the page is in and fills the root that it is in 
        and the second one is used for grouping text elements together. 
        """
        admin_user_update_frame = Frame(self.root_widget, padx=30, pady=30, background="#31117A")
        admin_user_update_frame.pack(fill=BOTH, expand=YES)
        text_box_frame = Frame(admin_user_update_frame, padx=10, pady=7, background="#31117A")
        text_box_frame.grid(row=2, column=0, rowspan=4)

        # Logo image put onto the page.
        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png").resize((50, 50)))
        logo_image_label = Label(admin_user_update_frame, image=image)
        # Title which describes the purpose of the page.
        title_label = Label(admin_user_update_frame, text="Admin User Information Update", font='Helvetica 18 bold',
                            background="#31117A", foreground="#f2f2f2")
        logo_image_label.grid(row=0, columnspan=2, column=0)  # Formats the title
        # Label which describes the instruct. for the entry next to it.
        query_user_id_label = Label(text_box_frame, text="Please Enter User's Current ID:", pady=7,
                                    background="#31117A",
                                    foreground="#f2f2f2", font='Helvetica 9 bold')
        """
        The following describe the instructions for the entries the to them. 
        """
        update_user_first_name_label = Label(text_box_frame, text="Update User First Name:", pady=7,
                                             background="#31117A",
                                             foreground="#f2f2f2")
        update_user_last_name_label = Label(text_box_frame, text="Update User Last Name:", pady=7, background="#31117A",
                                            foreground="#f2f2f2")
        update_user_loc_label = Label(text_box_frame, text="Update User Office Location:", pady=7, background="#31117A",
                                      foreground="#f2f2f2")
        # Formats the widgets so far.
        logo_image_label.grid(row=0, column=0, columnspan=2)
        title_label.grid(row=1, column=0, columnspan=2, pady=10)

        query_user_id_label.grid(row=1, column=0, sticky="e", padx=5)
        update_user_first_name_label.grid(row=2, column=0, sticky="e", padx=5)
        update_user_last_name_label.grid(row=3, column=0, sticky="e", padx=5)
        update_user_loc_label.grid(row=5, column=0, sticky="e", padx=5)

        """
        Declares entries which are used to take user input as instructed by the labels next to them and also
        disables the last three until a database query is provided.
        """
        query_user_id_entry = Entry(text_box_frame, width=50)
        update_user_first_name_entry = Entry(text_box_frame, width=50, state="disabled")
        update_user_last_name_entry = Entry(text_box_frame, width=50, state="disabled")
        update_user_loc_entry = Entry(text_box_frame, width=50, state="disabled")

        def query_database_for_id():
            """
            Searches the database for ids that match the values given then display those values in the entry boxes.
            :return:
            """
            search_id_value = query_user_id_entry.get()
            if database_interaction.get_ids(  # If not values match then tell user.
                    database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                    id=search_id_value)[0] == "No Matching Values":
                messagebox.showwarning("ShipperStatusPlus - Action Required",
                                       "The ID which you've entered is not in the database please try again")
                self.admin_update_user()
            else:  # Other than that update the entries so the admin can set new value to the user.
                update_user_first_name_entry["state"] = "normal"
                update_user_last_name_entry["state"] = "normal"
                update_user_loc_entry["state"] = "normal"
                query_user_id_entry["state"] = "disabled"
                update_user_first_name_entry.insert(0,
                                                    f"{database_interaction.get_names(database_connection=database_interaction.create_database('ShipperStatusPlus.db'), id=search_id_value)[0][0].split()[0]}")
                update_user_last_name_entry.insert(0,
                                                   f"{database_interaction.get_names(database_connection=database_interaction.create_database('ShipperStatusPlus.db'), id=search_id_value)[0][0].split()[1]}")
                update_user_loc_entry.insert(0,
                                             f"{(database_interaction.get_locations(database_connection=database_interaction.create_database('ShipperStatusPlus.db'), id=search_id_value))[0][0]}")
                check_user_database_button.destroy()
                update_user_database_button = Button(admin_user_update_frame, padx=35, pady=0, text="Push To Database",
                                                     background="#f2f2f2",
                                                     command=lambda: pop_up_to_confirm(search_id_value))
                update_user_database_button.grid(row=7, column=0, columnspan=2, pady=20)

        def pop_up_to_confirm(search_id_value):
            """
            Popup as an message box that asks if you want to set the values which you've entered to the user and
            if you say yes then the database is updated to reflect those changes.
            :param search_id_value:
            :return:
            """
            return_value = messagebox.askyesno("ShipperStatusPlus - Add User To Database Question",
                                               "Are you sure that you want to update this user's profile in the database?")
            if return_value == 1:
                database_interaction.set_name_from_id(
                    database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                    search_id=search_id_value,
                    name=f"{update_user_first_name_entry.get()} {update_user_last_name_entry.get()}")
                database_interaction.set_location_from_id(
                    database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                    search_id=search_id_value, location=update_user_loc_entry.get())
                messagebox.showwarning("ShipperStatusPlus - Action Required",
                                       "You're being redirected to the selection screen.")
                self.admin_selection()

        # Formats the widgets
        query_user_id_entry.grid(row=1, column=1)
        update_user_first_name_entry.grid(row=2, column=1)
        update_user_last_name_entry.grid(row=3, column=1)
        update_user_loc_entry.grid(row=5, column=1)

        # Declares button which is used to submit values to the database.
        check_user_database_button = Button(admin_user_update_frame, padx=35, pady=0, text="Search Database",
                                            background="#f2f2f2", command=query_database_for_id)
        # Formats button.
        check_user_database_button.grid(row=7, column=0, columnspan=2, pady=20)

    def admin_delete_user(self):
        """
        Page only accessible by the admin and lets them delete any user in the database.
        :return:
        """
        global image  # Global reference to the image which is the logo
        for value in self.root_widget.winfo_children():
            value.destroy()  # Destroys all of the windows that were open
        self.root_widget.title("ShipperStatusPlus - Admin User Information Delete Screen")  # Sets title
        self.root_widget.iconbitmap("logo_icon_ssp.ico")  # Sets icon to the logo

        # Declares frame that will be used to hold all the content on the page and can fill the entire root.
        admin_user_delete_frame = Frame(self.root_widget, padx=30, pady=30, background="#31117A")
        admin_user_delete_frame.pack(fill=BOTH, expand=YES)
        # Frame which holds text content on the page.
        text_box_frame = Frame(admin_user_delete_frame, padx=10, pady=7, background="#31117A")
        text_box_frame.grid(row=2, column=0, rowspan=4)  # Formats this widget

        # Declares the image on the page.
        image = ImageTk.PhotoImage(Image.open("logo_picture_200_ssp.png").resize((50, 50)))
        logo_image_label = Label(admin_user_delete_frame, image=image)

        # Declares the title which describes the purpose of the page.
        title_label = Label(admin_user_delete_frame, text="Admin User Information Delete", font='Helvetica 18 bold',
                            background="#31117A", foreground="#f2f2f2")
        logo_image_label.grid(row=0, column=0, columnspan=2)  # Formats title

        # Label which describes what the user should do.
        delete_user_id_label = Label(text_box_frame, text="Please Enter The User ID You Want To Delete:", pady=7,
                                     background="#31117A",
                                     foreground="#f2f2f2")
        title_label.grid(row=1, column=0, columnspan=2, pady=10)  # Formats title

        delete_user_id_label.grid(row=1, column=0, sticky="e", padx=5)  # Formats the instuct. label

        delete_user_id_entry = Entry(text_box_frame,
                                     width=50)  # Declares the entry widget which allows for user input.

        def pop_up_to_confirm():
            """
            Popup in the form of a message box that actually deletes the user's profiles from the database
            and returns them to the selection page.
            :return:
            """
            messagebox.askyesno("ShipperStatusPlus - Delete User To Database Question",
                                "Are you sure that you want to delete this user's profile in the database?")
            database_interaction.delete_user(
                database_connection=database_interaction.create_database("ShipperStatusPlus.db"),
                id=delete_user_id_entry.get())
            messagebox.showwarning("ShipperStatusPlus - Action Required",
                                   "You're being redirected to the selection screen, your changes have been made.")
            self.admin_selection()

        delete_user_id_entry.grid(row=1, column=1)  # Formats label

        # Declares button which submits information and deletes the user.
        delete_user_database_button = Button(admin_user_delete_frame, padx=35, pady=0, text="Delete User Profile",
                                             background="#f2f2f2", command=pop_up_to_confirm)
        delete_user_database_button.grid(row=7, column=0, columnspan=2, pady=20)  # Formats the button


root = Tk()  # Declares the main root
ShipperStatusPlus(root)  # Passes in root to the application class
root.mainloop()  # Puts the root in the main root.
