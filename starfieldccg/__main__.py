"""
    Execution part of the program.
"""
from os import path as OSPATH
import sys
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), './')))
# pylint: disable=wrong-import-position
from .src.menu_views import ItemMenu, NavMenu
from .src.data_file_reader import DataFileReader as DFR

items_workbook = DFR(OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  './data/Starfield_Datatable.xls')))
print("Datasheets Loaded!")

def handle_ammo():
    """
        Handles the ammo menu.
    """

    ammo_menu = ItemMenu(items_workbook.ammo_data,
                              "Select Ammo Type:")
    menu_result = ammo_menu.display_menu()
    ammo_choice = menu_result[0]
    ammo_amount = menu_result[1]

    if ammo_choice != "end":
        print(items_workbook.ammo_data[ammo_choice]
              .get_command(ammo_amount))

    return True

def handle_spacesuits():
    """
        Handles the spacesuit menu.
    """

    spacesuit_menu = ItemMenu(items_workbook.spacesuit_data,
                              "Select Spacesuit Type:")
    menu_result = spacesuit_menu.display_menu()
    spacesuit_choice = menu_result[0]
    spacesuit_amount = menu_result[1]

    if spacesuit_choice != "end":
        print(items_workbook.spacesuit_data[spacesuit_choice]
              .get_command(spacesuit_amount))

    return True

def handle_packs():
    """
        Handles the pack menu.
    """

    pack_menu = ItemMenu(items_workbook.pack_data,
                              "Select Pack Type:")
    menu_result = pack_menu.display_menu()
    pack_choice = menu_result[0]
    pack_amount = menu_result[1]

    if pack_choice != "end":
        print(items_workbook.pack_data[pack_choice]
              .get_command(pack_amount))

    return True

def handle_helmets():
    """
        Handles the helmet menu.
    """

    helmet_menu = ItemMenu(items_workbook.helmet_data,
                              "Select Helmet Type:")
    menu_result = helmet_menu.display_menu()
    helmet_choice = menu_result[0]
    helmet_amount = menu_result[1]

    if helmet_choice != "end":
        print(items_workbook.helmet_data[helmet_choice]
              .get_command(helmet_amount))

    return True

def handle_spacesuit_sets():
    """
        Handles the spacesuit_set menu.
    """

    spacesuit_set_menu = ItemMenu(items_workbook.spacesuit_set_data,
                              "Select Spacesuit Set Type:")
    menu_result = spacesuit_set_menu.display_menu()
    spacesuit_set_choice = menu_result[0]
    spacesuit_set_amount = menu_result[1]

    if spacesuit_set_choice != "end":
        print(items_workbook.spacesuit_set_data[spacesuit_set_choice]
              .get_command(spacesuit_set_amount))

    return True

def handle_weapons():
    """
        Handles the weapons menu.
    """

    weapon_menu = ItemMenu(items_workbook.weapon_data,
                              "Select Weapon Type:")
    menu_result = weapon_menu.display_menu()
    weapon_choice = menu_result[0]
    weapon_amount = menu_result[1]

    if weapon_choice != "end":
        print(items_workbook.weapon_data[weapon_choice]
              .get_command(weapon_amount))

    return True

def main():
    """
        Main loop of program.
    """

    exited = False
    not_built_str = "Option Not Built Yet. Try another."

    while exited is False:
        main_menu = NavMenu(sorted(items_workbook.sheet_names),
                            "Main Menu:", "Select an option or type quit to exit>")
        menu_selection = main_menu.display_menu().lower()

        if menu_selection == "quit":
            exited = True
        elif menu_selection == "ammo":
            exited = handle_ammo()
        elif menu_selection == "spacesuits":
            exited = handle_spacesuits()
        elif menu_selection == "packs":
            exited = handle_packs()
        elif menu_selection == "helmets":
            exited = handle_helmets()
        elif menu_selection == "resources":
            print(not_built_str)
        elif menu_selection == "weapons":
            exited = handle_weapons()
        elif menu_selection == "spacesuit_sets":
            exited = handle_spacesuit_sets()
        elif menu_selection == "armor_status_mods":
            print(not_built_str)
        elif menu_selection == "weapon_status_mods":
            print(not_built_str)

main()
