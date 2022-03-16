"""
Program Title: Test Program For Database In ShipperStatusPlus Project
"""
import json
from tkinter import *
import sqlite3


def merge_dictionaries(dictionary1, dictionary2):
    """
    Merges two dictionaries that are passed in.
    :param dictionary1:
    :param dictionary2:
    :return:
    """
    return_dictionary = dictionary1 | dictionary2
    return return_dictionary


def create_database(database):
    """
    Creates the database for ShipperStatusPlus if it doesn't already exist, and then return this connection to it.
    :param database:
    :return:
    """
    create_database_connection = sqlite3.connect(database)
    create_database_cursor = create_database_connection.cursor()
    create_database_cursor.execute("""CREATE TABLE IF NOT EXISTS employee_information (
        employee_name text,
        employee_id text,
        employee_location text,
        employee_status text,
        employee_packages blob
    );""")
    return create_database_connection


def json_conversion(value):
    """
    Converts to json value and returns.
    :param value:
    :return:
    """
    return json.dumps(value)


def json_dict_conversion(value):
    """
    Returns a dict. that was a json, specific to the format of the ShipperStatusPlus database.
    :param value:
    :return:
    """
    json_value = value[4]
    actual_json = json.loads(json_value)
    return actual_json


def add_new_user(database_connection, name, id, location, packages, status):
    """
    Adds a new user to the database, along with default packages.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :param packages:
    :param status:
    :return:
    """
    add_new_user_cursor = database_connection.cursor()
    add_new_user_cursor.execute("""INSERT INTO employee_information VALUES (:employee_name, :employee_id,
    :employee_location, :employee_status, :employee_packages)""", {
        "employee_name": name,
        "employee_id": id,
        "employee_location": location,
        "employee_packages": packages,
        "employee_status": status
    })
    database_connection.commit()


def add_first_user(database_connection, name, id, location, packages, status="Admin"):
    """
    Adds the first user to the database, though because they are they first user, they are auto. admin.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :param packages:
    :param status:
    :return:
    """
    add_new_user_cursor = database_connection.cursor()
    add_new_user_cursor.execute("""INSERT INTO employee_information VALUES (:employee_name, :employee_id,
    :employee_location, :employee_status, :employee_packages)""", {
        "employee_name": name,
        "employee_id": id,
        "employee_location": location,
        "employee_packages": packages,
        "employee_status": status
    })
    database_connection.commit()


def delete_duplicates(database_input):
    """
    Takes values directly from the database converts that to a list, then returns a list without duplicate values
    :param database_input:
    :return:
    """
    index_value = 0
    list_database = list(database_input)
    return_list = []
    for element in list_database:
        if element not in return_list:
            return_list.append(element)
    return return_list


def database_format_to_normal_str(value):
    """
    Converts the format from the ShipperStatusPlus database to a str. value that can be used
    :param value:
    :return:
    """
    clean_list = delete_duplicates(value)
    index = 0
    return_list = []
    for values in clean_list:
        return_list.append(values[index])
        index + 1
    return return_list[0]


def get_names(database_connection, name=None, id=None, location=None, status=None):
    """
    Gets the name of the person, when given one of the attributes of the user, this returns a list of these values,
    though only a select number can actually have more than one value.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :param status:
    :return:
    """
    if name != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_name FROM employee_information WHERE employee_name = "{name}"')
        returned_names = get_name_cursor.fetchall()
        if returned_names == []:
            return "No Matching Values"
        else:
            return returned_names
    elif id != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_name FROM employee_information WHERE employee_id = "{id}"')
        returned_ids = get_name_cursor.fetchall()
        if returned_ids == []:
            return "No Matching Values"
        else:
            return returned_ids
    elif location != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(
            f'SELECT employee_name FROM employee_information WHERE employee_location = "{location}"')
        returned_locations = get_name_cursor.fetchall()
        if returned_locations == []:
            return "No Matching Values"
        else:
            return returned_locations
    if status != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_name FROM employee_information WHERE employee_status = "{status}"')
        returned_status = get_name_cursor.fetchall()
        if returned_status == []:
            return "No Matching Values"
        else:
            return returned_status


def get_ids(database_connection, name=None, id=None, location=None, status=None):
    """
    Gets the ids of the person, when given one of the attributes of the user, this returns a list of these values,
    though only a select number can actually have more than one value.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :param status:
    :return:
    """
    if name != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_id FROM employee_information WHERE employee_name = "{name}"')
        returned_names = get_name_cursor.fetchall()
        if returned_names == []:
            return "No Matching Values"
        else:
            return returned_names
    elif id != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_id FROM employee_information WHERE employee_id = "{id}"')
        returned_ids = get_name_cursor.fetchall()
        if returned_ids == []:
            return "No Matching Values"
        else:
            return returned_ids
    elif location != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_id FROM employee_information WHERE employee_location = "{location}"')
        returned_locations = get_name_cursor.fetchall()
        if returned_locations == []:
            return "No Matching Values"
        else:
            return returned_locations
    if status != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_id FROM employee_information WHERE employee_status = "{status}"')
        returned_status = get_name_cursor.fetchall()
        if returned_status == []:
            return "No Matching Values"
        else:
            return returned_status


def get_locations(database_connection, name=None, id=None, location=None, status=None):
    """
    Gets the location of the person, when given one of the attributes of the user, this returns a list of these values,
    though only a select number can actually have more than one value.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :param status:
    :return:
    """
    if name != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_location FROM employee_information WHERE employee_name = "{name}"')
        returned_names = get_name_cursor.fetchall()
        if returned_names == []:
            return "No Matching Values"
        else:
            return returned_names
    elif id != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_location FROM employee_information WHERE employee_id = "{id}"')
        returned_ids = get_name_cursor.fetchall()
        if returned_ids == []:
            return "No Matching Values"
        else:
            return returned_ids
    elif location != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(
            f'SELECT employee_location FROM employee_information WHERE employee_location = "{location}"')
        returned_locations = get_name_cursor.fetchall()
        if returned_locations == []:
            return "No Matching Values"
        else:
            return returned_locations
    if status != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(
            f'SELECT employee_location FROM employee_information WHERE employee_status = "{status}"')
        returned_status = get_name_cursor.fetchall()
        if returned_status == []:
            return "No Matching Values"
        else:
            return returned_status


def get_statuses(database_connection, name=None, id=None, location=None, status=None):
    """
    Gets the status of the person, when given one of the attributes of the user, this returns a list of these values,
    though only a select number can actually have more than one value.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :param status:
    :return:
    """
    if name != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_status FROM employee_information WHERE employee_name = "{name}"')
        returned_names = get_name_cursor.fetchall()
        if returned_names == []:
            return "No Matching Values"
        else:
            return returned_names
    elif id != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_status FROM employee_information WHERE employee_id = "{id}"')
        returned_ids = get_name_cursor.fetchall()
        if returned_ids == []:
            return "No Matching Values"
        else:
            return returned_ids
    elif location != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(
            f'SELECT employee_status FROM employee_information WHERE employee_location = "{location}"')
        returned_locations = get_name_cursor.fetchall()
        if returned_locations == []:
            return "No Matching Values"
        else:
            return returned_locations
    if status != None:
        get_name_cursor = database_connection.cursor()
        get_name_cursor.execute(f'SELECT employee_status FROM employee_information WHERE employee_status = "{status}"')
        returned_status = get_name_cursor.fetchall()
        if returned_status == []:
            return "No Matching Values"
        else:
            return returned_status


def get_id_from_package(database_connection, package_search):
    """
    Returns ID when asked for a certain package.
    :param database_connection:
    :param package_search:
    :return:
    """
    get_id_from_package_cursor = database_connection.cursor()
    get_id_from_package_cursor.execute('SELECT * FROM employee_information')
    returned_packages = get_id_from_package_cursor.fetchall()
    id_value = ''
    json_value = None
    search_package = package_search
    for values in returned_packages:
        actual_json_packages = json_dict_conversion(values)
        if search_package in actual_json_packages:
            return (values[1])


def get_package_from_id(database_connection, id_search):
    """
    Returns Dictionary of Values After Given A User ID
    :param database_connection:
    :param id_search:
    :return:
    """
    get_package_from_id_cursor = database_connection.cursor()
    get_package_from_id_cursor.execute('SELECT * FROM employee_information')
    returned_values = get_package_from_id_cursor.fetchall()
    package_values = None
    search_id = id_search
    return_list = []
    for values in returned_values:
        if values[1] == id_search:
            return_list.append(values)
    return json_dict_conversion(return_list[0])


def set_name_from_id(database_connection, search_id, name):
    """
    Sets a new name for the user when an is passed in to update it. It returns True if it has been updates, and false if
    it couldn't be updated because the id doesn't exist.
    :param database_connection:
    :param search_id:
    :param name:
    :return:
    """
    current_cursor = database_connection.cursor()
    try:
        current_cursor.execute(
            'UPDATE employee_information SET employee_name = (:employee_name) WHERE employee_id = (:employee_id)',
            {
                "employee_name": name,
                "employee_id": search_id
            }
        )
        return True
    except:
        return False


def set_location_from_id(database_connection, search_id, location):
    """
    Sets a new location for the user when an is passed in to update it. It returns True if it has been updates, and false if
    it couldn't be updated because the id doesn't exist.
    :param database_connection:
    :param search_id:
    :param location:
    :return:
    """
    current_cursor = database_connection.cursor()
    current_cursor.execute(
        'UPDATE employee_information SET employee_location = (:employee_location) WHERE employee_id = (:employee_id)',
        {
            "employee_location": location,
            "employee_id": search_id
        }
    )
    database_connection.commit()


def set_status_from_id(database_connection, search_id, status):
    """
    Sets a new status for the user when an is passed in to update it. It returns True if it has been updates, and false if
    it couldn't be updated because the id doesn't exist.
    :param database_connection:
    :param search_id:
    :param status:
    :return:
    """
    current_cursor = database_connection.cursor()
    try:
        current_cursor.execute(
            'UPDATE employee_information SET employee_status = (:employee_status) WHERE employee_id = (:employee_id)',
            {
                "employee_status": status,
                "employee_id": search_id
            }
        )
        return True
    except:
        return False


def set_package_location_ims(database_connection, package_id, new_location):
    """
    Sets the location of a package in the IMS system.
    :param database_connection:
    :param package_id:
    :param new_location:
    :return:
    """
    current_cursor = database_connection.cursor()
    package = get_package_from_id(database_connection=database_connection,
                                  id_search=get_id_from_package(database_connection=database_connection,
                                                                package_search=package_id))
    if package_id in package:
        package[package_id]["package_ims_location"] = new_location
        user_id = get_id_from_package(database_connection, package_id)
        current_cursor.execute(
            'UPDATE employee_information SET employee_packages = (:employee_packages) WHERE employee_id = (:employee_id)',
            {
                "employee_packages": json_conversion(package),
                "employee_id": user_id
            }
        )
    database_connection.commit()


def get_package_location_ims(database_connection, package_id):
    """
    Gets the location of a package passed in, in the IMS System
    :param database_connection:
    :param package_id:
    :return:
    """
    package = get_package_from_id(database_connection=database_connection,
                                  id_search=get_id_from_package(database_connection=database_connection,
                                                                package_search=package_id))
    if package_id in package:
        return package[package_id]["package_ims_location"]


def get_package_arrival_date(database_connection, package_id):
    """
    Gets the arrival date of the package that is passed in.
    :param database_connection:
    :param package_id:
    :return:
    """
    package = get_package_from_id(database_connection=database_connection,
                                  id_search=get_id_from_package(database_connection=database_connection,
                                                                package_search=package_id))
    if package_id in package:
        return package[package_id]["package_arrival_date"]


def set_package_arrival_date(database_connection, package_id, new_arrival_date):
    current_cursor = database_connection.cursor()
    package = get_package_from_id(database_connection=database_connection,
                                  id_search=get_id_from_package(database_connection=database_connection,
                                                                package_search=package_id))
    if package_id in package:
        package[package_id]["package_arrival_date"] = new_arrival_date
        user_id = get_id_from_package(database_connection, package_id)
        current_cursor.execute(
            'UPDATE employee_information SET employee_packages = (:employee_packages) WHERE employee_id = (:employee_id)',
            {
                "employee_packages": json_conversion(package),
                "employee_id": user_id
            }
        )
    database_connection.commit()


def add_new_package(database_connection, package_id, location_ims, arrival_date, user_id):
    """
    Adds a new package to the id of a user that is passed in.
    :param database_connection:
    :param package_id:
    :param location_ims:
    :param arrival_date:
    :param user_id:
    :return:
    """
    current_cursor = database_connection.cursor()
    packages = get_package_from_id(database_connection, user_id)
    new_package = {package_id: {"package_ims_location": location_ims, "package_arrival_date": arrival_date}}
    packages.update(new_package)
    current_cursor.execute(
        'UPDATE employee_information SET employee_packages = (:employee_packages) WHERE employee_id = (:employee_id)',
        {
            "employee_packages": json_conversion(packages),
            "employee_id": user_id
        }
    )
    database_connection.commit()


def add_first_package(database_connection, package_id, location_ims, arrival_date, user_id):
    """
    Adds the first package for a user, which involves removing the placeholder #000000 package number.
    :param database_connection:
    :param package_id:
    :param location_ims:
    :param arrival_date:
    :param user_id:
    :return:
    """
    current_cursor = database_connection.cursor()
    new_package = {package_id: {"package_ims_location": location_ims, "package_arrival_date": arrival_date}}
    current_cursor.execute(
        'UPDATE employee_information SET employee_packages = (:employee_packages) WHERE employee_id = (:employee_id)',
        {
            "employee_packages": json_conversion(new_package),
            "employee_id": user_id
        }
    )
    database_connection.commit()

def package_defaults():
    """
    Returns the default values to init the packages, though this is later deleted when the first package is added to
    an account.
    :return:
    """
    packages_default = {"000000": {
        "package_ims_location": "NO PACKAGE",
        "package_arrival_date": "NO PACKAGE"
    }
    }
    return packages_default


def setup_app(database_connection, name, id, location, packages):
    """
    Called when the application is opened for the first time and gives the first user admin and then creates the
    database that will be used through the application.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :param packages:
    :return:
    """
    add_first_user(create_database(database_connection), name, id, location, json_conversion(packages))
    file_object = open("setup_complete.txt", "x")  # After setup complete will make a file in the same directory that
    # will be checked at the beginning of the application to see if this is the first time the application has been
    # set up.


def check_user_auth(database_connection, name, id):
    """
    Method which checks to see if the name and id value match each other and return False if they don't. It doesn't
    include location because knowing the location of a company is quite easy.
    :param database_connection:
    :param name:
    :param id:
    :param location:
    :return:
    """
    try:
        if id in get_ids(database_connection=database_connection, name=name)[0][0]:
            return True
        else:
            return False
    except:  # Get Ids returns a str if there isn't a matching value, and also this is just in case anything goes
        # wrong, it'll always return false to not let the user in.
        return False

def check_if_admin(database_connection, id):
    """
    Checks if the user has admin privileges.
    :param database_connection:
    :param id:
    :return:
    """
    if get_statuses(database_connection=database_connection, id=id)[0][0] == "Admin":
        return True
    else:
        return False

def delete_user(database_connection, id):
    """
    Deletes a user from the database, that is passed in.
    :param database_connection:
    :param id:
    :return:
    """
    current_cursor = database_connection.cursor()
    current_cursor.execute('DELETE FROM employee_information WHERE employee_id = (:employee_id)',
                           {
                               "employee_id":id
                           })

def get_all_undelivered_packages(database_connection):
    """
    Returns all of the undelivered packages in an organization.
    :param database_connection:
    :return:
    """
    current_cursor = database_connection.cursor()
    current_cursor.execute('SELECT employee_packages FROM employee_information')
    all_packages = current_cursor.fetchall()
    undelivered_list = []
    for values in all_packages:
        for packages in values:
            for element in json.loads(packages):
                if get_package_location_ims(database_connection, element) == "Not Arrived":
                    undelivered_list.append(element)
                else:
                    continue
    return undelivered_list


def main():
    """
    Used for debugging
    :return:
    """
    database_connection = create_database("ShipperStatusPlus.db")
    main_database_cursor = database_connection.cursor()
    add_new_user(database_connection, "Evil Mitchell", "25", "Bloomington", json_conversion(package_defaults()), "User")
if __name__ == "__main__":
    main()
