"""
    This is a module for outputting all of the console commands for a
    specific tab in the datatable. This is for verifying accurate Item ids.

"""

from os import path as OSPATH
from os import makedirs as MAKEDIRS
import pytest
from .context import SCCGTestContext as STC

TEST_DFR = STC().get_a_dfr() # Global DataFileReader instance because we're testing the datasheet.

def output_all_of_object_dict(object_dict: dict, filename: str):
    """
        Intended for tests for accuracy of datatable objects.

        :param object_dict: A dict containing item data.
        :param filename: A str for the file name.
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

def output_all_of_status_mods(mod_dict: dict, type_name: str):
    """
        Intended for tests for accuracy of status mods in the datatable.

        :param mod_dict: A dict containing mod data.
        :param type_name: A str for the type of status mods.
    """

    debug_folder = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), \
                                                  "./debug_output"))
    if OSPATH.exists(debug_folder) is not True:
        MAKEDIRS(debug_folder)

    counter = 0
    complete = [False, False, False]
    slot_one_list = list(TEST_DFR.get_status_mods_by_mod_slot(1, mod_dict).values())
    slot_two_list = list(TEST_DFR.get_status_mods_by_mod_slot(2, mod_dict).values())
    slot_three_list = list(TEST_DFR.get_status_mods_by_mod_slot(3, mod_dict).values())

    while complete != [True, True, True]:
        output = []
        filepath = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  f"./debug_output/{type_name}\
_statusmod_{counter}.txt"))

        if counter < len(slot_one_list):
            output.append(slot_one_list[counter].get_command())
        else:
            complete[0] = True
        if counter < len(slot_two_list):
            output.append(slot_two_list[counter].get_command())
        else:
            complete[1] = True
        if counter < len(slot_three_list):
            output.append(slot_three_list[counter].get_command())
        else:
            complete[2] = True

        counter += 1
        output_text = "\n".join(output)

        if complete != [True, True, True]:
            with open(filepath, "w+", 1, "UTF-8") as dump_file:
                dump_file.write(output_text)

                dump_file.close()

def output_all_of_quality_mods(mod_dict: dict, type_name: str):
    """
        Intended for tests for accuracy of quality mods in the datatable.

        :param mod_dict: A dict containing mod data.
        :param type_name: A str for the type of status mods.
    """

    debug_folder = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), \
                                                  "./debug_output"))
    if OSPATH.exists(debug_folder) is not True:
        MAKEDIRS(debug_folder)

    counter = 0
    mod_list = list(mod_dict.values())


    while counter < len(mod_list):

        filepath = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  f"./debug_output/{type_name}\
_qualitymod_{counter}.txt"))

        output = mod_list[counter].get_command()
        counter += 1

        with open(filepath, "w+", 1, "UTF-8") as dump_file:
            dump_file.write(output)

            dump_file.close()

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_ammo():
    """
        Prints to a file all ammo data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.ammo_data, "ammo_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_spacesuits():
    """
        Prints to a file all spacesuit data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.spacesuit_data, "spacesuit_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_packs():
    """
        Prints to a file all pack data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.pack_data, "pack_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_helmets():
    """
        Prints to a file all pack data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.helmet_data, "helmet_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_spacesuit_sets():
    """
        Prints to a file all spacesuit set data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.spacesuit_set_data, "spacesuit_set_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_resources():
    """
        Prints to a file all resource data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.resource_data, "resource_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_weapons():
    """
        Prints to a file all weapons data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.weapon_data, "weapons_commands.txt")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_weapon_status_mods():
    """
        Prints to a file all weapon status mods commands for testing.
    """

    output_all_of_status_mods(TEST_DFR.weapon_status_mods_data, "weapon")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_armor_status_mods():
    """
        Prints to a file all armor status mods commands for testing.
    """

    output_all_of_status_mods(TEST_DFR.armor_status_mods_data, "armor")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_weapon_quality_mods():
    """
        Prints to a file all weapon quality commands for testing.
    """

    output_all_of_quality_mods(TEST_DFR.weapon_quality_mods_data, "weapon")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_armor_quality_mods():
    """
        Prints to a file all armor quality commands for testing.
    """

    output_all_of_quality_mods(TEST_DFR.armor_quality_mods_data, "armor")

@pytest.mark.skip(reason="only needs to be run sparingly for testing datasheet accuracy")
def test_dump_apparel():
    """
        Prints to a file all apparel data commands for testing.
    """

    output_all_of_object_dict(TEST_DFR.apparel_data, "apparel_commands.txt")