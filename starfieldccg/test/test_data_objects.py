"""
    Tests the data_objects module.
"""
import pytest
from .context import DO
from .context import SIO


def test_status_mod_slot_exception():
    """
    Tests that the StatusModType throws a ValueError Exception
    when you supply it with an incorrect mod_slot value.
    """

    # pylint: disable=unused-variable

    with pytest.raises(ValueError) as ve:
        bad_mod_slot_status_mod = DO.StatusModType("bad_slot",
                                              "FFFFFFFF",
                                              "Test StatusModType with a bad slot value",
                                              4)

def test_status_mod_str():
    """
    Tests that a StatusModType object returns the correct str
    version of itself.
    """

    test_status_mod_type = DO.StatusModType("test_name",
                                                        "FFFFFFFF",
                                                        "test_mod_desc",
                                                        1)
    assert str(test_status_mod_type) == \
          "StatusModType(status_mod_name='test_name', \
            status_mod_id='FFFFFFFF', \
            status_mod_desc='test_mod_desc', \
            mod_slot=1)"

def test_status_mod_command():
    """
    Tests that a StatusModType object returns the correct str
    of its command.
    """

    test_status_mod_type = DO.StatusModType("test_name",
                                                        "FFFFFFFF",
                                                        "test_mod_desc",
                                                        1)
    assert test_status_mod_type.get_command() == \
    ".amod FFFFFFFF"

def test_quality_mod_command():
    """
    Verifies that the QualityModType object has the correct format
    .get_command() function return.
    """

    test_quality_mod_type = DO.QualityModType("test_name",
                                              "FFFFFFFF")
    assert test_quality_mod_type.get_command() == \
    ".amod FFFFFFFF"

def test_quality_mod_str():
    """
    Verifies that the QualityModType object has the correct format
    __repr__ function.
    """

    test_quality_mod_type = DO.QualityModType("test_name",
                                              "FFFFFFFF")
    assert str(test_quality_mod_type) == "QualityModType(mod_name='test_name', \
mod_id='FFFFFFFF')"

def test_spacesuit_dlc_one():
    """
    Test that the DLC handling function works for spacesuits.
    """

    test_spacesuit = DO.SpacesuitItem("Test DLC Suit", "XX000001", True)

    assert test_spacesuit.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_helmet_dlc_one():
    """
    Test that the DLC handling function works for helmets.
    """

    test_obj = DO.HelmetItem("Test DLC Helmet", "XX000001", True)

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_pack_dlc_one():
    """
    Test that the DLC handling function works for helmets.
    """

    test_obj = DO.PackItem("Test DLC Boost Pack", "XX000001", True)

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_weapon_dlc_one():
    """
    Test that the DLC handling function works for weapons.
    """

    test_obj = DO.WeaponItem("Test DLC Weapon", "XX000001", True, True)

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_process_id_one():
    """
    Test that the DLC handling function works for invalid values.
    """

    test_obj = DO.WeaponItem("Test DLC Weapon", "XX0000001", True, True)

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_process_id_two():
    """
    Test that the DLC handling function works for invalid values.
    """

    test_obj = DO.WeaponItem("Test DLC Weapon", "XX00001", True, True)

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"
