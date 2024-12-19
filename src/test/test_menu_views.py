"""
    Tests the data_file_reader module.
"""
# pylint: disable=unused-import
import pytest
from .context import data_file_reader as DFR
from .context import menu_views as MV

def test_autocompletelist_repr():
    """
        Tests the __repr__ function of the NavMenu class
        to make sure it matches the old .format() method.
    """
    # pylint: disable=consider-using-f-string

    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
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

    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
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

    test_reader = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    test_navmenu = MV.NavMenu(sorted(test_reader.sheet_names),
                            "Main Menu:", "Test Menu")
    expected_str = "NavMenu(menu_items='{}', completer={}, title='{}', prompt='{}')".format(
            test_navmenu.menu_items, test_navmenu.completer, test_navmenu.title,
            test_navmenu.text_prompt)
    assert str(test_navmenu) == expected_str
