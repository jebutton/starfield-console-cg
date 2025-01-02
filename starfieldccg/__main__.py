"""
    Execution part of the program.
"""
# pylint: disable=wrong-import-position
from os import path as OSPATH
import sys
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), './')))
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

    if item_choice != "end":
        print("\n")
        print(data_dict[item_choice]
              .get_command(item_amount))

    return True

def handle_status_mods(title: str, data_dict: dict):
    """
    Handles the Status Mods menu.

    :param title: A str with the title of the prompt.
    :param prompt: A str with a prompt to display.
    :param data_dict: A dict with the type of data to search through.

    :return: Returns True if the operation is successful.
    """

    status_menu = StatusModMenu(data_dict,
                              title)
    menu_result = status_menu.display_menu()
    mod_choices = menu_result

    if "end" not in mod_choices:
        print("\n")
        for i, choice in enumerate(mod_choices):
            if choice != "skip":
                print(data_dict[mod_choices[i]]
              .get_command())

    return True

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
    print(data_dict)
    menu_result = quality_menu.display_menu()
    mod_choice = menu_result

    if mod_choice != "quit":
        print("\n")
        print(data_dict[mod_choice]
        .get_command())

    return True

def handle_settings_menu():
    """
    Handles displaying the settings menu.
    
    :return: Returns True if the operation is successful.
    """
    settings_menu = SettingsMenu("Select Resource Type:")
    settings_menu.display_menu()

    return True

def main():
    """
        Main loop of program.
    """

    exited = False

    while exited is False:
        menu_options = items_workbook.pretty_sheet_names
        menu_options.insert(0,"Settings")
        main_menu = NavMenu(menu_options,
                            "Main Menu:", "Select an option or type quit to exit> ")
        menu_selection = main_menu.display_menu().lower()

        if menu_selection == "quit":
            exited = True
        elif menu_selection == "exit":
            exited = True
        elif menu_selection == "settings":
            exited = handle_settings_menu()
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
            exited = handle_item_menu(items_workbook.weapon_data,
                                      "Select a Weapon Type:")
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
                                         "Type Mod name or type quit to exit> ",
                                         items_workbook.armor_quality_mods_data)
        elif menu_selection == "weapon quality mods":
            exited = handle_quality_mods("Select Weapon Quality Mod Level:",
                                         "Type Mod name or type quit to exit> ",
                                         items_workbook.weapon_quality_mods_data)

main()
