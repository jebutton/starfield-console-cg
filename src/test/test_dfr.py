"""
    Tests the data_file_reader module.
"""
import os
from .context import data_file_reader as DFR


def test_dfr_get_cell_value():
    """
        Tests the get_cell_value() method of DataFileReader Class
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    resources_data = test_reader.datasheets.get("Resources")
    id_a = resources_data.at[resources_data["Resource_Name"]
                             .array.tolist().index("Water"), "Resource_ID"]
    id_b = test_reader.get_cell_value(resources_data,
                                      "Resource_Name", "Water",
                                      "Resource_ID")
    assert id_a == id_b

def test_resources_sheet_load():
    """
        Tests that the resources sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    resources_data = test_reader.datasheets.get("Resources")
    test_value = test_reader.get_cell_value(resources_data,
                                            "Resource_Name", "Titanium",
                                            "Resource_ID").strip()
    assert test_value == "556D"

def test_spacesuits_sheet_load():
    """
        Tests that the spacesuits sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Spacesuits")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Suit_Name", 
                                            "UC Wardog Spacesuit", 
                                            "Suit_ID").strip()
    assert test_value == "0025780A"

def test_helmets_sheet_load():
    """
        Tests that the helmets sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Helmets")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Helmet_Name", 
                                            "UC Urbanwar Space Helmet",
                                            "Helmet_ID").strip()
    assert test_value == "0021A86B"

def test_packs_sheet_load():
    """
        Tests that the packs sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Packs")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Pack_Name",
                                            "UC Shock Armor Skip Pack",
                                            "Pack_ID").strip()
    assert test_value == "021A86C"

def test_spacesuit_sets_sheet_load():
    """
        Tests that the spacesuits_sets sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Spacesuit_Sets")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Set_Name", "Deimos",
                                            "Suit_Name").strip()
    assert test_value == "Deimos Spacesuit"

def test_weapons_sheet_load():
    """
        Tests that the weapons sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Weapons")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Weapon_Name", "AA-99",
                                            "Weapon_ID").strip()
    assert test_value == "002BF65B"

def test_ammo_sheet_load():
    """
        Tests that the ammo sheet loads without errors.
    """
    print(os.getcwd())
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Ammo")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Ammo_Name",
                                            ".43 Ultramag",
                                            "Ammo_ID").strip()
    assert test_value == "02B5599"

def test_armor_status_mods_sheet_load():
    """
        Tests that the armor_status_mods sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Armor_Status_Mods")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Armor_Status_Mod_Name",
                                            "Ablative",
                                            "Armor_Status_Mod_ID").strip()
    assert test_value == "0013369C"

def test_weapon_status_mods_sheet_load():
    """
        Tests that the weapon_status_mods sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_data = test_reader.datasheets.get("Weapon_Status_Mods")
    test_value = test_reader.get_cell_value(spacesuits_data,
                                            "Weapon_Status_Mod_Name",
                                            "Berserker",
                                            "Weapon_Status_Mod_ID").strip()
    assert test_value == "000F437E"
