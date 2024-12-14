from data_file_reader import DataFileReader as DFR
from menu_views import ItemMenu, NavMenu

items_workbook = DFR("./data/Starfield_Datatable.xls")
print("Datasheets Loaded!")

# Main Loop
exited = False
while exited is not True:
    main_menu = NavMenu(sorted(items_workbook.sheet_names),
                        "Main Menu:", "Select an option or type quit to exit>")
    menu_selection = main_menu.display_menu()
    print("Menu Selection: {}".format(menu_selection))
    if menu_selection.lower() == "quit":
        exited = True
    elif menu_selection.lower() == "ammo":
        ammo_menu = ItemMenu(items_workbook.ammo_data,
                              "Select Ammo Type:")
        ammo_choice = ammo_menu.display_menu()
        if ammo_choice != "end":
            tgt_id = items_workbook.ammo_data[ammo_choice].ammo_id
            print("player.additem {}".format(tgt_id))
            exited = True
    else:
        exited = True