"""
    Main Execution part of the program.
"""
# pylint: disable=wrong-import-position
from os import path as OSPATH
import sys
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), './')))
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), './src/')))
from .src.menu_views import ItemMenu, NavMenu, StatusModMenu, QualityMenu, SettingsMenu
from .src.data_file_reader import DataFileReader as DFR


items_workbook = DFR(OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  './data/Starfield_Datatable.xls')))
print("Datasheets Loaded!")

def handle_item_menu(data_dict: dict, title: str):
    """
    Handles a menu for an item type.

    :param data_dict: A dict containing item data.
    :param title: A str containing the title for the menu.

    :return: Returns True if the operation is successful.
    """

    item_menu = ItemMenu(data_dict,
                              title)
    menu_result = item_menu.display_menu()
    item_choice = menu_result[0]
    item_amount = menu_result[1]

    return_value = False
    if item_choice != "end":
        print("\n")
        pretty_print_command(data_dict[item_choice]
              .get_command(item_amount))
        return_value = True

    return return_value

def handle_status_mods(title: str, data_dict: dict):
    """
    Handles the Status Mods menu.

    :param title: A str with the title of the prompt.
    :param data_dict: A dict with the type of data to search through.

    :return: Returns True if the operation is successful.
    """

    status_menu = StatusModMenu(data_dict,
                              title)
    menu_result = status_menu.display_menu()
    mod_choices = menu_result
    return_value = False
    command = []
    if "end" not in mod_choices:
        print("\n")
        for i, choice in enumerate(mod_choices):
            if choice != "skip":
                command.append(data_dict[mod_choices[i]]
              .get_command())
        return_value = True
    pretty_print_command("\n".join(command))

    return return_value

def handle_quality_mods(title: str, prompt: str, data_dict: dict):
    """
    Handles a quality mod menu by passing a prompt to it.

    :param title: A str with the title of the prompt.
    :param prompt: A str with a prompt to display.
    :param data_dict: A dict with the type of data to search through.

    :return: Returns True if the operation is successful.
    """

    quality_menu = QualityMenu(data_dict, title,
                              prompt)
    menu_result = quality_menu.display_menu()
    mod_choice = menu_result
    return_value = False

    if mod_choice != "quit":
        print("\n")
        pretty_print_command(data_dict[mod_choice]
        .get_command())
        return_value = True

    return return_value

def handle_settings_menu():
    """
    Handles displaying the settings menu.
    
    :return: Returns True if the operation is successful.
    """
    settings_menu = SettingsMenu("Select Settings Type:")
    settings_menu.display_menu()
    print("\n")

    return True

def handle_weapons_menu():
    """
    Handles the weapons menu and splits weapons 
    between unique and not unique.
    """
    options_menu_selection = ["Unique Weapons", "Normal Weapons", \
                              "Melee Weapons", "Guns", "Thrown Weapons","All Weapons"]
    option_menu = NavMenu(options_menu_selection,"Select a Weapon Category",
                          "Select a category of Weapons or 'end' to return to the main menu> ")
    options_selection = option_menu.display_menu().lower()

    if options_selection == "unique weapons":
        result = handle_item_menu(items_workbook.get_weapons_by_unique(True),
                                  "Select a Weapon Type:")

    elif options_selection == "normal weapons":
        result = handle_item_menu(items_workbook.get_weapons_by_unique(False),
                                  "Select a Weapon Type:")

    elif options_selection == "all weapons":
        result = handle_item_menu(items_workbook.weapon_data, "Select a Weapon Type:")

    elif options_selection == "melee weapons":
        result = handle_item_menu(items_workbook.get_weapons_by_type("melee"),
                                  "Select a Weapon Type:")
    elif options_selection == "guns":
        result = handle_item_menu(items_workbook.get_weapons_by_type("gun"),
                                  "Select a Weapon Type:")

    elif options_selection == "thrown weapons":
        result = handle_item_menu(items_workbook.get_weapons_by_type("thrown"),
                                  "Select a Weapon Type:")

    else:
        result = False

    return result

def handle_subtype_menu(input_dict: dict, item_type_name: str):
    """
    Handles a menu where there are sub options based on subtypes of items.

    :param input_dict: A dict containing the items to display.
    :param item_type_name: A str containing the name of the item type.
    """

    menu_options = items_workbook.get_subtype_list(input_dict)

    option_menu = NavMenu(menu_options,f"Select a {item_type_name.capitalize()} Category",
                          f"Select a category of {item_type_name.capitalize()} or \
'end' to return to the main menu> ")
    options_selection = option_menu.display_menu().lower()

    items = items_workbook.get_item_by_subtype(input_dict, options_selection)

    result = handle_item_menu(items,
                                  f"Select the {item_type_name} Type:")

    return result

def pretty_print_command(command: str):
    """
    Standardizes how console commands are printed.
    
    :param command: A str for commands to print.
    """
    border = "=" * 60
    print(border)
    print("Copy and paste these commands into the Starfield Console:")
    print(border)
    print("\n")
    print(command)
    print("\n")
    print(f"{border}\n")



# pylint: disable=too-many-branches
def main():
    """
        Main loop of program.
    """

    exited = False
    menu_options = items_workbook.pretty_sheet_names
    menu_options.insert(0,"Settings")
    main_menu = NavMenu(menu_options,
                        "Main Menu:", "Select an option or type quit to exit> ")
    while exited is False:
        menu_selection = main_menu.display_menu().lower()

        if menu_selection == "quit":
            exited = True
        elif menu_selection == "exit":
            exited = True
        elif menu_selection == "settings":
            result = handle_settings_menu()
            if result is True:
                exited = False
            else:
                exited = True
        elif menu_selection == "ammo":
            exited = handle_item_menu(items_workbook.ammo_data,
                                          "Select an Ammo Type:")
        elif menu_selection == "spacesuits":
            exited = handle_item_menu(items_workbook.spacesuit_data,
                                      "Select a Spacesuit Type:")
        elif menu_selection == "packs":
            exited = handle_item_menu(items_workbook.pack_data,
                                      "Select a Pack Type:")
        elif menu_selection == "helmets":
            exited = handle_item_menu(items_workbook.helmet_data,
                                      "Select a Helmet Type:")
        elif menu_selection == "resources":
            exited = handle_item_menu(items_workbook.resource_data,
                                      "Select a Resource Type:")
        elif menu_selection == "weapons":
            exited = handle_weapons_menu()
        elif menu_selection == "spacesuit sets":
            exited = handle_item_menu(items_workbook.spacesuit_set_data,
                                      "Select a Spacesuit Set:")
        elif menu_selection == "armor status mods":
            exited = handle_status_mods("Select Armor Status Mod Type from Slot",
                                        items_workbook.armor_status_mods_data)
        elif menu_selection == "weapon status mods":
            exited = handle_status_mods("Select Weapon Status Mod Type from Slot",
                                        items_workbook.weapon_status_mods_data)
        elif menu_selection == "armor quality mods":
            exited = handle_quality_mods("Select Armor Quality Mod Level:",
                                         "Type Mod name or type 'end to \
return back to the main menu> ",
                                         items_workbook.armor_quality_mods_data)
        elif menu_selection == "weapon quality mods":
            exited = handle_quality_mods("Select Weapon Quality Mod Level:",
                                         "Type Mod name or type 'end' to \
return back to the main menu> ",
                                         items_workbook.weapon_quality_mods_data)
        elif menu_selection == "apparel":
            exited = handle_subtype_menu(items_workbook.apparel_data, "Apparel")
        elif menu_selection == "aid":
            exited = handle_subtype_menu(items_workbook.aid_data, "Aid")
main()
