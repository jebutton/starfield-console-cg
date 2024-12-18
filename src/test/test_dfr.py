"""
    Tests the data_file_reader module.
"""
import pytest
from .context import SCCGTestContext as STC

AMMO_COUNT = 22 # Total Expec. Types of Ammo.
SPACESUITS_COUNT = 64   # Total Expec. Types of Spacesuits.
HELMETS_COUNT = 48  # Total Expec. Types of Helmets.
PACKS_COUNT = 43    # Total Expec. Types of Boost Packs.
SPACESUIT_SETS_COUNT = 86   # Total Expec. Types of Spacesuit Sets.
WEAPONS_COUNT = 132 # Total Expec. Types of Weapons.
RESOURCES_COUNT = 108   # Total Expec. Types of Resources.
ARMOR_STATUS_MODS_COUNT = 32    # Total Expec. Armor Status Mods.
WEAPON_STATUS_MODS_COUNT = 29   # Total Expec. Weapon Status Mods.
ARMOR_QUALITY_MODS_COUNT = 5    # Total Expec. Armor Quality Mods.
WEAPON_QUALITY_MODS_COUNT = 4   # Total Expec. Weapon Quality Mods.
EXPECTED_SHEETS_COUNT = 11  # Total Expected Sheet Counts.



def test_dfr_get_cell_value():
    """
        Tests the get_cell_value() method of DataFileReader Class
    """
    test_reader = STC.get_a_dfr()
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
    test_reader = STC.get_a_dfr()
    resources_data = test_reader.datasheets.get("Resources")
    test_value = test_reader.get_cell_value(resources_data,
                                            "Resource_Name", "Titanium",
                                            "Resource_ID").strip()
    assert test_value == "556D"

def test_spacesuits_sheet_load():
    """
        Tests that the spacesuits sheet loads without errors.
    """
    test_reader = STC.get_a_dfr()
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
    test_reader = STC.get_a_dfr()
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
    test_reader = STC.get_a_dfr()
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
    test_reader = STC.get_a_dfr()
    spacesuits_sets_data = test_reader.datasheets.get("Spacesuit_Sets")
    test_value = test_reader.get_cell_value(spacesuits_sets_data,
                                            "Set_Name", "Deimos 1",
                                            "Suit_Name").strip()
    assert test_value == "Deimos Spacesuit"

def test_weapons_sheet_load():
    """
        Tests that the weapons sheet loads without errors.
    """
    test_reader = STC.get_a_dfr()
    weapons_data = test_reader.datasheets.get("Weapons")
    test_value = test_reader.get_cell_value(weapons_data,
                                            "Weapon_Name", "AA-99",
                                            "Weapon_ID").strip()
    assert test_value == "002BF65B"

def test_ammo_sheet_load():
    """
        Tests that the ammo sheet loads without errors.
    """
    test_reader = STC.get_a_dfr()
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
    test_reader = STC.get_a_dfr()
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
    test_reader = STC.get_a_dfr()
    weapon_status_mods_data = test_reader.datasheets.get("Weapon_Status_Mods")
    test_value = test_reader.get_cell_value(weapon_status_mods_data,
                                            "Weapon_Status_Mod_Name",
                                            "Berserker",
                                            "Weapon_Status_Mod_ID").strip()
    assert test_value == "000F437E"

@pytest.mark.xfail
def test_expected_sheet_names_count():
    """
        Tests that the expected number of sheets are being tracked.
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.sheet_names) == EXPECTED_SHEETS_COUNT

def test_ammo_item_count():
    """
        Tests that the expected amount of Ammo Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.ammo_data) == AMMO_COUNT

def test_spacesuits_item_count():
    """
        Tests that the expected amount of Spacesuit Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.spacesuit_data) == SPACESUITS_COUNT

def test_packs_item_count():
    """
        Tests that the expected amount of Boost Pack Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.pack_data) == PACKS_COUNT

def test_helmets_item_count():
    """
        Tests that the expected amount of Helmet Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.helmet_data) == HELMETS_COUNT

@pytest.mark.xfail
def test_weapons_item_count():
    """
        Tests that the expected amount of Weapon Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.weapon_data) == WEAPONS_COUNT

def test_spacesuit_sets_item_count():
    """
        Tests that the expected amount of Spacesuit Set Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.spacesuit_set_data) == SPACESUIT_SETS_COUNT

@pytest.mark.xfail
def test_resources_count():
    """
        Tests that the expected amount of Resource Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.resource_data) == RESOURCES_COUNT

@pytest.mark.xfail
def test_armor_status_mods_count():
    """
        Tests that the expected amount of Armor Status Mod
        Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.armor_status_mods_data) == ARMOR_STATUS_MODS_COUNT

@pytest.mark.xfail
def test_weapons_status_mods_count():
    """
        Tests that the expected amount of Weapon Status Mod
        Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.weapon_status_mods_data) == WEAPON_STATUS_MODS_COUNT

@pytest.mark.xfail
def test_armor_quality_mods_count():
    """
        Tests that the expected amount of Armor Quality Mod
        Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.armor_quality_mods_data) == ARMOR_STATUS_MODS_COUNT

@pytest.mark.xfail
def test_weapons_quality_mods_count():
    """
        Tests that the expected amount of Weapon Quality Mod
        Types is present. 
    """
    test_reader = STC.get_a_dfr()
    assert len(test_reader.weapon_quality_mods_data) == WEAPON_QUALITY_MODS_COUNT
