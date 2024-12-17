"""
    Tests the data_file_reader module.
"""

from .context import data_file_reader as DFR

AMMO_COUNT = 22 # Total Expected Types of Ammo
SPACESUITS_COUNT = 64   # Total Expected Types of Spacesuits
HELMETS_COUNT = 48  # Total Expected Types of Helmets
PACKS_COUNT = 43    # Total Expected Types of Boost Packs


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
    helmets_data = test_reader.datasheets.get("Helmets")
    test_value = test_reader.get_cell_value(helmets_data,
                                            "Helmet_Name", 
                                            "UC Urbanwar Space Helmet",
                                            "Helmet_ID").strip()
    assert test_value == "0021A86B"

def test_packs_sheet_load():
    """
        Tests that the packs sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    packs_data = test_reader.datasheets.get("Packs")
    test_value = test_reader.get_cell_value(packs_data,
                                            "Pack_Name",
                                            "UC Shock Armor Skip Pack",
                                            "Pack_ID").strip()
    assert test_value == "021A86C"

def test_spacesuit_sets_sheet_load():
    """
        Tests that the spacesuits_sets sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    spacesuits_sets_data = test_reader.datasheets.get("Spacesuit_Sets")
    test_value = test_reader.get_cell_value(spacesuits_sets_data,
                                            "Set_Name", "Deimos",
                                            "Suit_Name").strip()
    assert test_value == "Deimos Spacesuit"

def test_weapons_sheet_load():
    """
        Tests that the weapons sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    weapons_data = test_reader.datasheets.get("Weapons")
    test_value = test_reader.get_cell_value(weapons_data,
                                            "Weapon_Name", "AA-99",
                                            "Weapon_ID").strip()
    assert test_value == "002BF65B"

def test_ammo_sheet_load():
    """
        Tests that the ammo sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    ammo_data = test_reader.datasheets.get("Ammo")
    test_value = test_reader.get_cell_value(ammo_data,
                                            "Ammo_Name",
                                            ".43 Ultramag",
                                            "Ammo_ID").strip()
    assert test_value == "02B5599"

def test_armor_status_mods_sheet_load():
    """
        Tests that the armor_status_mods sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    armor_status_mods_data = test_reader.datasheets.get("Armor_Status_Mods")
    test_value = test_reader.get_cell_value(armor_status_mods_data,
                                            "Armor_Status_Mod_Name",
                                            "Ablative",
                                            "Armor_Status_Mod_ID").strip()
    assert test_value == "0013369C"

def test_weapon_status_mods_sheet_load():
    """
        Tests that the weapon_status_mods sheet loads without errors.
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    weapon_status_mods_data = test_reader.datasheets.get("Weapon_Status_Mods")
    test_value = test_reader.get_cell_value(weapon_status_mods_data,
                                            "Weapon_Status_Mod_Name",
                                            "Berserker",
                                            "Weapon_Status_Mod_ID").strip()
    assert test_value == "000F437E"

def test_ammo_item_count():
    """
        Tests that the expected amount of Ammo Types is present. 
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    assert len(test_reader.ammo_data) == AMMO_COUNT

def test_spacesuit_item_count():
    """
        Tests that the expected amount of Spacesuit Types is present. 
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    assert len(test_reader.spacesuit_data) == SPACESUITS_COUNT

def test_packs_item_count():
    """
        Tests that the expected amount of Boost Pack Types is present. 
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    assert len(test_reader.pack_data) == PACKS_COUNT


def test_helmets_item_count():
    """
        Tests that the expected amount of Helmet Types is present. 
    """
    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    assert len(test_reader.helmet_data) == HELMETS_COUNT
