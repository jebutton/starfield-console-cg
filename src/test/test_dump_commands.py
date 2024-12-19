"""
    This is a module for outputting all of the console commands for a
    specific tab in the datatable. This is for verifying accurate Item ids.

"""
import pytest
from .context import data_file_reader as DFR


def output_all_of_object_dict(object_dict: dict):
    """
        Intended for tests for accuracy of datatable objects.
    """
    for data_object in object_dict.values():
        print(data_object.get_command(1))

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_ammo():
    """
        Prints all ammo data commands for testing.
    """
    items_workbook = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    output_all_of_object_dict(items_workbook.ammo_data)

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_spacesuits():
    """
        Prints all spacesuit data commands for testing.
    """
    items_workbook = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    output_all_of_object_dict(items_workbook.spacesuit_data)

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_packs():
    """
        Prints all pack data commands for testing.
    """
    items_workbook = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    output_all_of_object_dict(items_workbook.pack_data)

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_spacesuit_sets():
    """
        Prints all spacesuit set data commands for testing.
    """
    items_workbook = DFR.DataFileReader("./data/Starfield_Datatable.xls")
    output_all_of_object_dict(items_workbook.spacesuit_set_data)
