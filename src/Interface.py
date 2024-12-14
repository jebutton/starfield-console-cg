from data_file_reader import DataFileReader as DFR
from menu_views import ItemMenu, NavMenu

items_workbook = DFR("./data/Starfield_Datatable.xls")
print("Datasheets Loaded!")

def handle_ammo():
    ammo_menu = ItemMenu(items_workbook.ammo_data,
                              "Select Ammo Type:")
    menu_result = ammo_menu.display_menu()
    ammo_choice = menu_result[0]
    ammo_amount = menu_result[1]
    if ammo_choice != "end":
        tgt_id = items_workbook.ammo_data[ammo_choice].ammo_id
        print("player.additem {} {}".format(tgt_id, ammo_amount))
    return True

def handle_spacesuits():
    spacesuit_menu = ItemMenu(items_workbook.spacesuit_data,
                              "Select Spacesuit Type:")
    menu_result = spacesuit_menu.display_menu()
    spacesuit_choice = menu_result[0]
    spacesuit_amount = menu_result[1]
    if spacesuit_choice != "end":
        tgt_id = items_workbook.spacesuit_data[spacesuit_choice].spacesuit_id
        print("player.additem {} {}".format(tgt_id, spacesuit_amount))
    return True


# Main Loop
exited = False
while exited is not True:
    main_menu = NavMenu(sorted(items_workbook.sheet_names),
                        "Main Menu:", "Select an option or type quit to exit>")
    menu_selection = main_menu.display_menu().lower()
    if menu_selection == "quit":
        exited = True
    elif menu_selection == "ammo":
            exited = handle_ammo()
    elif menu_selection == "spacesuits":
            exited = handle_spacesuits()
    else:
        exited = True

