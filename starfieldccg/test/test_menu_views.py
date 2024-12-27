"""
    Tests the data_file_reader module.
"""
# pylint: disable=unused-import
import pytest
from .context import MV
from .context import SCCGTestContext as STC
from .context import DO

@staticmethod
def generate_fake_data_for_item_menus(num_items: int):
    """
        Generates a fake dataset for use in testing menu chunking.

        :param num_items: The size of the values to generate.
        :return: A dict of fake data.
    """
    test_data = {}
    for counter in range (1, num_items + 1):
        fake_item = DO.AmmoItem(f"fake {counter}", f"ZZ{counter}")
        #print(fake_item)
        test_data[f"fake {counter}"] = fake_item
    #print(test_data)
    return test_data

def test_autocompletelist_repr():
    """
        Tests the __repr__ function of the NavMenu class
        to make sure it matches the old .format() method.
    """
    # pylint: disable=consider-using-f-string

    test_reader = STC.get_a_dfr()
    spacesuits_data = test_reader.spacesuit_data
    test_itemmenu = MV.ItemMenu(spacesuits_data, "Test Menu")
    test_autocompletelist = MV.AutoCompleteList(test_itemmenu.input_dict)
    expected_str = "AutoCompleteList(input_structure='{}')".format(
        test_autocompletelist.input_structure)
    assert str(test_autocompletelist) == expected_str

def test_autocompletelist_wrong_input():
    """
        Tests the error_handling logic of the AutoCompleteList class's
        checks for inputs to make sure it matches the old .format() method.
    """
    # pylint: disable=consider-using-f-string

    wrong_input = ("test1", "test2", "test3")
    test_autocompletelist = MV.AutoCompleteList(wrong_input)
    expected_str = "Invalid datastructure type. Type is {}".format(
        str(type(wrong_input)))
    assert test_autocompletelist.wrong_input_str == expected_str

def test_itemmenu_repr():
    """
        Tests the __repr__ function of the ItemMenu class
        to make sure it matches the old .format() method.
    """
    # pylint: disable=consider-using-f-string

    test_reader = STC.get_a_dfr()
    spacesuits_data = test_reader.spacesuit_data
    test_itemmenu = MV.ItemMenu(spacesuits_data, "Test Menu")

    expected_str = "ItemMenu(input_dict='{}')".format(str(test_itemmenu.input_dict))
    assert str(test_itemmenu) == expected_str

def test_navmenu_repr():
    """
        Tests the __repr__ function of the NavMenu class
        to make sure it matches the old .format() method.
    """
    # pylint: disable=consider-using-f-string

    test_reader = STC.get_a_dfr()
    test_navmenu = MV.NavMenu(sorted(test_reader.sheet_names),
                            "Main Menu:", "Test Menu")
    expected_str = "NavMenu(menu_items='{}', completer={}, title='{}', prompt='{}')".format(
            test_navmenu.menu_items, test_navmenu.completer, test_navmenu.title,
            test_navmenu.text_prompt)
    assert str(test_navmenu) == expected_str

def test_itemmenu_chunks_resources():
    """
        Verifies that the resources menu is split into the correct number of chunks
    """
    test_reader = STC.get_a_dfr()
    resources_menu = MV.ItemMenu(test_reader.resource_data,
                                  "Test Menu")

    assert len(resources_menu.display_chunks) == 9

def test_itemmenu_chunks_spacesuits():
    """
        Verifies that the spacesuits menu is split into the correct number of chunks
    """
    test_reader = STC.get_a_dfr()
    spacesuits_menu = MV.ItemMenu(test_reader.spacesuit_data,
                                  "Test Menu")

    assert len(spacesuits_menu.display_chunks) == 6

def test_itemmenu_chunks_helmets():
    """
        Verifies that the helmets menu is split into the correct number of chunks
    """
    test_reader = STC.get_a_dfr()
    helmets_menu = MV.ItemMenu(test_reader.helmet_data,
                                "Test Menu")

    assert len(helmets_menu.display_chunks) == 4

def test_itemmenu_chunks_packs():
    """
        Verifies that the packs menu is split into the correct number of chunks
    """
    test_reader = STC.get_a_dfr()
    packs_menu = MV.ItemMenu(test_reader.pack_data,
                                  "Test Menu")

    assert len(packs_menu.display_chunks) == 4

def test_itemmenu_chunks_spacesuit_sets():
    """
        Verifies that the spacesuit_sets menu is split into the correct number of chunks
    """
    test_reader = STC.get_a_dfr()
    spacesuit_sets_menu = MV.ItemMenu(test_reader.spacesuit_set_data,
                                  "Test Menu")

    assert len(spacesuit_sets_menu.display_chunks) == 8

def test_itemmenu_chunks_weapons():
    """
        Verifies that the weapons menu is split into the correct number of chunks
    """
    test_reader = STC.get_a_dfr()
    weapons_menu = MV.ItemMenu(test_reader.weapon_data,
                                  "Test Menu")

    assert len(weapons_menu.display_chunks) == 12

def test_itemmenu_chunks_one():
    """
        Verifies that a hypothetical ItemMenu with a list size of one
        has the correct chunking.
    """

    test_itemmenu = MV.ItemMenu(generate_fake_data_for_item_menus(1), "Test Menu")
    assert len(test_itemmenu.display_chunks) == 1
    assert test_itemmenu.display_chunks[0][5] == "1"


def test_itemmenu_chunks_two():
    """
        Verifies that a hypothetical ItemMenu with a list size of one
        has the correct chunking.
    """

    test_itemmenu = MV.ItemMenu(generate_fake_data_for_item_menus(2), "Test Menu")
    assert len(test_itemmenu.display_chunks) == 1
    assert test_itemmenu.display_chunks[0][12] == "2"

def test_itemmenu_chunks_chunksize():
    """
        Verifies that a hypothetical ItemMenu with a list size of one
        has the correct chunking.
    """
    chunk_size = MV.ItemMenu.CHUNK_SIZE
    test_itemmenu = MV.ItemMenu(generate_fake_data_for_item_menus(chunk_size),
                                 "Test Menu")
    assert len(test_itemmenu.display_chunks) == 1
    assert test_itemmenu.display_chunks[0][5:7] == "1\n"
    assert test_itemmenu.display_chunks[0][84:86] == "12"


def test_itemmenu_chunks_size_two():
    """
        Verifies that a hypothetical ItemMenu with a list size of one
        has the correct chunking.
    """
    chunk_size = MV.ItemMenu.CHUNK_SIZE * 2
    test_itemmenu = MV.ItemMenu(generate_fake_data_for_item_menus(chunk_size),
                                 "Test Menu")
    assert len(test_itemmenu.display_chunks) == 2
    assert test_itemmenu.display_chunks[0][5:7] == "1\n"
    assert test_itemmenu.display_chunks[1][5:8] == "13\n"

def test_itemmenu_chunks_size_two_half():
    """
        Verifies that a hypothetical ItemMenu with a list size of one
        has the correct chunking.
    """
    chunk_size = int(MV.ItemMenu.CHUNK_SIZE * 2.5)
    test_itemmenu = MV.ItemMenu(generate_fake_data_for_item_menus(chunk_size),
                                 "Test Menu")
    # print(f"len: {len(test_itemmenu.menu_items)} items: {test_itemmenu.menu_items}")
    # print(test_itemmenu.display_chunks)
    assert len(test_itemmenu.display_chunks) == 3
    assert test_itemmenu.display_chunks[0][5:7] == "1\n"
    assert test_itemmenu.display_chunks[1][5:8] == "13\n"
    assert test_itemmenu.display_chunks[2][5:8] == "25\n"

def test_itemmenu_chunks_size_3_half():
    """
        Verifies that a hypothetical ItemMenu with a list size of one
        has the correct chunking.
    """
    chunk_size = int(MV.ItemMenu.CHUNK_SIZE * 3.5)
    test_itemmenu = MV.ItemMenu(generate_fake_data_for_item_menus(chunk_size),
                                 "Test Menu")
    # print(f"len: {len(test_itemmenu.menu_items)} items: {test_itemmenu.menu_items}")
    # print(test_itemmenu.display_chunks)
    assert len(test_itemmenu.display_chunks) == 4
    assert test_itemmenu.display_chunks[0][5:7] == "1\n"
    assert test_itemmenu.display_chunks[1][5:8] == "13\n"
    assert test_itemmenu.display_chunks[2][5:8] == "25\n"
    assert test_itemmenu.display_chunks[3][5:8] == "37\n"

def test_statusmodmenu_weapons_chunks_one():
    """
    Test that there should be three sets of chunks for a
    weapons status mod menu.
    """

    test_reader = STC.get_a_dfr()
    weapons_status_mod_menu = MV.StatusModMenu(test_reader.weapon_status_mods_data,
                                  "Test Menu")
    assert len(weapons_status_mod_menu.display_chunks) == 3

def test_statusmodmenu_weapons_chunks_two():
    """
    Test that each chunk sof a StatusModMenu for 
    weapon status mods has the correct item for the first item
    """

    test_reader = STC.get_a_dfr()
    weapons_status_mod_menu = MV.StatusModMenu(test_reader.weapon_status_mods_data,
                                  "Test Menu")

    command_one = weapons_status_mod_menu.input_dict[weapons_status_mod_menu. \
    trim_menu_selection(weapons_status_mod_menu.display_chunks[0][0]).lower()].get_command()
    command_two = weapons_status_mod_menu.input_dict[weapons_status_mod_menu. \
    trim_menu_selection(weapons_status_mod_menu.display_chunks[1][0]).lower()].get_command()
    command_three = weapons_status_mod_menu.input_dict[weapons_status_mod_menu. \
    trim_menu_selection(weapons_status_mod_menu.display_chunks[2][0]).lower()].get_command()

    assert command_one == ".amod 000FF442"
    assert command_two == ".amod 0008AB47"
    assert command_three == ".amod 000FBD3C"

def test_statusmodmenu_weapons_chunks_three():
    """
    Test that each chunk list of a StatusModMenu for 
    weapon status mods has the correct number of chunks.
    """

    test_reader = STC.get_a_dfr()
    weapons_status_mod_menu = MV.StatusModMenu(test_reader.weapon_status_mods_data,
                                  "Test Menu")

    assert len(weapons_status_mod_menu.display_chunks[0]) == 1
    assert len(weapons_status_mod_menu.display_chunks[1]) == 1
    assert len(weapons_status_mod_menu.display_chunks[2]) == 1

def test_qualitymenu_options_weapons():
    """
    Tests that the quality menu has the right amount of options
    for weapon quality options
    """

    test_reader = STC.get_a_dfr()
    weapons_quality_menu = MV.QualityMenu(test_reader.weapon_quality_mods_data,
                                          "Test Weapons Quality","Test Prompt")
    assert len(weapons_quality_menu.menu_items) == 3

def test_qualitymenu_options_armor():
    """
    Tests that the quality menu has the right amount of options
    for armor quality options
    """

    test_reader = STC.get_a_dfr()
    armor_quality_menu = MV.QualityMenu(test_reader.armor_quality_mods_data,
                                          "Test Armor Quality","Test Prompt")
    assert len(armor_quality_menu.menu_items) == 4
