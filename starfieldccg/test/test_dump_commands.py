"""
    This is a module for outputting all of the console commands for a
    specific tab in the datatable. This is for verifying accurate Item ids.

"""

from os import path as OSPATH
from os import makedirs as MAKEDIRS
import pytest
from .context import SCCGTestContext as STC



def output_all_of_object_dict(object_dict: dict, filename: str):
    """
        Intended for tests for accuracy of datatable objects.
    """
    output = []
    debug_folder = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), \
                                                  "./debug_output"))
    if OSPATH.exists(debug_folder) is not True:
        MAKEDIRS(debug_folder)

    filepath = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  f"./debug_output/{filename}"))
    for data_object in object_dict.values():
        output.append(data_object.get_command(1))

    output = "\n".join(output)
    with open(filepath, "w+", 1, "UTF-8") as dump_file:
        dump_file.write(output)

    dump_file.close()

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_ammo():
    """
        Prints all ammo data commands for testing.
    """

    items_workbook = STC.get_a_dfr()
    output_all_of_object_dict(items_workbook.ammo_data, "ammo_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_spacesuits():
    """
        Prints all spacesuit data commands for testing.
    """

    items_workbook = STC.get_a_dfr()
    output_all_of_object_dict(items_workbook.spacesuit_data, "spacesuit_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_packs():
    """
        Prints all pack data commands for testing.
    """

    items_workbook = STC.get_a_dfr()
    output_all_of_object_dict(items_workbook.pack_data, "pack_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_helmets():
    """
        Prints all pack data commands for testing.
    """

    items_workbook = STC.get_a_dfr()
    output_all_of_object_dict(items_workbook.helmet_data, "helmet_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_spacesuit_sets():
    """
        Prints all spacesuit set data commands for testing.
    """

    items_workbook = STC.get_a_dfr()
    output_all_of_object_dict(items_workbook.spacesuit_set_data, "spacesuit_set_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_resources():
    """
        Prints all resource data commands for testing.
    """

    items_workbook = STC.get_a_dfr()
    output_all_of_object_dict(items_workbook.resource_data, "resource_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_weapons():
    """
        Prints all weapons data commands for testing.
    """

    items_workbook = STC.get_a_dfr()
    output_all_of_object_dict(items_workbook.weapon_data, "weapons_commands.txt")
