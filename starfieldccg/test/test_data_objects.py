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

    test_obj = DO.WeaponItem("Test DLC Weapon", "XX000001", True, True, "gun")

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_process_id_one():
    """
    Test that the DLC handling function works for invalid values.
    """

    test_obj = DO.WeaponItem("Test DLC Weapon", "XX0000001", True, True, "gun")

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_process_id_two():
    """
    Test that the DLC handling function works for invalid values.
    """

    test_obj = DO.WeaponItem("Test DLC Weapon", "XX00001", True, True, "gun")

    assert test_obj.get_id() == SIO.global_settings.settings["dlc_load_order"] \
    + "000001"

def test_valid_weapon_type_one():
    """
    Tests that the first known weapon type works
    """

    test_obj = DO.WeaponItem("Test Gun Weapon", "00000001", False, False, "gun")

    test_str = "WeaponItem(weapon_name='Test Gun Weapon', \
          weapon_id='00000001', dlc=False, unique=False, type='gun')"
    assert str(test_obj) == test_str

def test_valid_weapon_type_two():
    """
    Tests that the second known weapon type works
    """

    test_obj = DO.WeaponItem("Test Melee Weapon", "00000001", False, False, "melee")

    test_str = "WeaponItem(weapon_name='Test Melee Weapon', \
          weapon_id='00000001', dlc=False, unique=False, type='melee')"
    assert str(test_obj) == test_str

def test_valid_weapon_type_three():
    """
    Tests that the first known weapon type works
    """

    test_obj = DO.WeaponItem("Test Thrown Weapon", "00000001", False, False, "thrown")

    test_str = "WeaponItem(weapon_name='Test Thrown Weapon', \
          weapon_id='00000001', dlc=False, unique=False, type='thrown')"
    assert str(test_obj) == test_str

def test_invalid_weapon_type_one():
    """
    Tests what happens when you get an invalid weapon type.
    """

    # pylint: disable=unused-variable

    with pytest.raises(ValueError) as ve:
        bad_weapon = DO.WeaponItem("Bad Weapon",
                                              "FFFFFFFF",
                                              False,
                                              False,
                                              "invalid")

def test_weapon_str_unique_one():
    """
    Tests that the weapon __repr___ function is correct for
    a unique weapon.
    """

    test_obj = DO.WeaponItem("Test Unique Weapon", "00000001", False, True, "thrown")

    test_str = "WeaponItem(weapon_name='Test Unique Weapon', \
          weapon_id='00000001', dlc=False, unique=True, type='thrown')"
    assert str(test_obj) == test_str

def test_weapon_str_unique_two():
    """
    Tests that the weapon __repr___ function is correct for
    a non-unique weapon.
    """

    test_obj = DO.WeaponItem("Test Non-Unique Weapon", "00000001", False, False, "thrown")

    test_str = "WeaponItem(weapon_name='Test Non-Unique Weapon', \
          weapon_id='00000001', dlc=False, unique=False, type='thrown')"
    assert str(test_obj) == test_str

def test_weapon_id_length_one():
    """
    Tests that a weapon's id length is 8 characters
    even if it is initially supplied as less than 8.
    """

    test_obj = DO.WeaponItem("Test Weapon", "1", False, False, "gun")
    assert len(test_obj.get_id()) == 8

def test_weapon_id_length_two():
    """
    Tests that a weapon's id is correct
    even if it is initially supplied as less than 8 characters.
    """

    test_obj = DO.WeaponItem("Test Weapon", "1", False, False, "gun")
    assert test_obj.get_id() == "00000001"

def test_weapon_id_length_three():
    """
    Tests that a weapon's id length is 8 characters
    even if it is initially supplied as more than 8.
    """

    test_obj = DO.WeaponItem("Test Weapon", "AAAAAAAA1", False, False, "gun")
    assert len(test_obj.get_id()) == 8

def test_weapon_id_length_four():
    """
    Tests that a weapon's id is correct
    even if it is initially supplied as more than 8 characters.
    """

    test_obj = DO.WeaponItem("Test Weapon", "AAAAAAAA1", False, False, "gun")
    assert test_obj.get_id() == "AAAAAAA1"

def test_helmet_id_length_one():
    """
    Tests that a helmet's id length is 8 characters
    even if it is initially supplied as less than 8.
    """

    test_obj = DO.HelmetItem("Test Helmet", "1", False)
    assert len(test_obj.get_id()) == 8

def test_helmet_id_length_two():
    """
    Tests that a helmet's id is correct
    even if it is initially supplied as less than 8 characters.
    """

    test_obj = DO.HelmetItem("Test Helmet", "1", False)
    assert test_obj.get_id() == "00000001"

def test_helmet_id_length_three():
    """
    Tests that a helmet's id length is 8 characters
    even if it is initially supplied as more than 8.
    """

    test_obj = DO.HelmetItem("Test Helmet", "AAAAAAAA1", False)
    assert len(test_obj.get_id()) == 8

def test_helmet_id_length_four():
    """
    Tests that a helmet's id is correct
    even if it is initially supplied as more than 8 characters.
    """

    test_obj = DO.HelmetItem("Test Helmet", "AAAAAAAA1", False)
    assert test_obj.get_id() == "AAAAAAA1"

def test_spacesuit_id_length_one():
    """
    Tests that a spacesuit's id length is 8 characters
    even if it is initially supplied as less than 8.
    """

    test_obj = DO.SpacesuitItem("Test Spacesuit", "1", False)
    assert len(test_obj.get_id()) == 8

def test_spacesuit_id_length_two():
    """
    Tests that a spacesuit's id is correct
    even if it is initially supplied as less than 8 characters.
    """

    test_obj = DO.SpacesuitItem("Test Spacesuit", "1", False)
    assert test_obj.get_id() == "00000001"

def test_spacesuit_id_length_three():
    """
    Tests that a spacesuit's id length is 8 characters
    even if it is initially supplied as more than 8.
    """

    test_obj = DO.SpacesuitItem("Test Spacesuit", "AAAAAAAA1", False)
    assert len(test_obj.get_id()) == 8

def test_spacesuit_id_length_four():
    """
    Tests that a spacesuit's id is correct
    even if it is initially supplied as more than 8 characters.
    """

    test_obj = DO.SpacesuitItem("Test Spacesuit", "AAAAAAAA1", False)
    assert test_obj.get_id() == "AAAAAAA1"
def test_pack_id_length_one():
    """
    Tests that a pack's id length is 8 characters
    even if it is initially supplied as less than 8.
    """

    test_obj = DO.PackItem("Test Pack", "1", False)
    assert len(test_obj.get_id()) == 8

def test_pack_id_length_two():
    """
    Tests that a pack's id is correct
    even if it is initially supplied as less than 8 characters.
    """

    test_obj = DO.PackItem("Test Pack", "1", False)
    assert test_obj.get_id() == "00000001"

def test_pack_id_length_three():
    """
    Tests that a pack's id length is 8 characters
    even if it is initially supplied as more than 8.
    """

    test_obj = DO.PackItem("Test Pack", "AAAAAAAA1", False)
    assert len(test_obj.get_id()) == 8

def test_pack_id_length_four():
    """
    Tests that a pack's id is correct
    even if it is initially supplied as more than 8 characters.
    """

    test_obj = DO.PackItem("Test Pack", "AAAAAAAA1", False)
    assert test_obj.get_id() == "AAAAAAA1"
def test_resource_id_length_one():
    """
    Tests that a resource's id length is 8 characters
    even if it is initially supplied as less than 8.
    """

    test_obj = DO.ResourceItem("Test Resource", "1")
    assert len(test_obj.get_id()) == 8

def test_resource_id_length_two():
    """
    Tests that a resource's id is correct
    even if it is initially supplied as less than 8 characters.
    """

    test_obj = DO.ResourceItem("Test Resource", "1")
    assert test_obj.get_id() == "00000001"

def test_resource_id_length_three():
    """
    Tests that a resource's id length is 8 characters
    even if it is initially supplied as more than 8.
    """

    test_obj = DO.ResourceItem("Test Resource", "AAAAAAAA1")
    assert len(test_obj.get_id()) == 8

def test_resource_id_length_four():
    """
    Tests that a resource's id is correct
    even if it is initially supplied as more than 8 characters.
    """

    test_obj = DO.ResourceItem("Test Resource", "AAAAAAAA1")
    assert test_obj.get_id() == "AAAAAAA1"

def test_spacesuit_set_id_one():
    """
    Tests that a spacesuit's set id is correct with valid input.
    """

    test_spacesuit = DO.SpacesuitItem("Test Spacesuit", "00000001", False)
    test_helmet = DO.HelmetItem("Test Helmet", "00000002", False)
    test_pack = DO.PackItem("Test Pack", "00000003", False)

    test_spacesuit_set = DO.SpacesuitSetItem("Test Spacesuit Set", False)
    test_spacesuit_set.set_helmet(test_helmet)
    test_spacesuit_set.set_pack(test_pack)
    test_spacesuit_set.set_spacesuit(test_spacesuit)

    assert test_spacesuit_set.get_id()[0] == "00000001"
    assert test_spacesuit_set.get_id()[1] == "00000002"
    assert test_spacesuit_set.get_id()[2] == "00000003"

def test_spacesuit_set_id_two():
    """
    Tests that a spacesuit's set id is correct with
    all components having two short of ids.
    """

    test_spacesuit = DO.SpacesuitItem("Test Spacesuit", "0000001", False)
    test_helmet = DO.HelmetItem("Test Helmet", "0000002", False)
    test_pack = DO.PackItem("Test Pack", "0000003", False)

    test_spacesuit_set = DO.SpacesuitSetItem("Test Spacesuit Set", False)
    test_spacesuit_set.set_helmet(test_helmet)
    test_spacesuit_set.set_pack(test_pack)
    test_spacesuit_set.set_spacesuit(test_spacesuit)

    assert test_spacesuit_set.get_id()[0] == "00000001"
    assert test_spacesuit_set.get_id()[1] == "00000002"
    assert test_spacesuit_set.get_id()[2] == "00000003"

def test_spacesuit_set_id_three():
    """
    Tests that a spacesuit's set id is correct with
    all components having two short of ids.
    """

    test_spacesuit = DO.SpacesuitItem("Test Spacesuit", "000000001", False)
    test_helmet = DO.HelmetItem("Test Helmet", "000000002", False)
    test_pack = DO.PackItem("Test Pack", "000000003", False)

    test_spacesuit_set = DO.SpacesuitSetItem("Test Spacesuit Set", False)
    test_spacesuit_set.set_helmet(test_helmet)
    test_spacesuit_set.set_pack(test_pack)
    test_spacesuit_set.set_spacesuit(test_spacesuit)

    assert test_spacesuit_set.get_id()[0] == "00000001"
    assert test_spacesuit_set.get_id()[1] == "00000002"
    assert test_spacesuit_set.get_id()[2] == "00000003"

def test_apparel_id_length_one():
    """
    Tests that an apparel's id length is 8 characters
    even if it is initially supplied as less than 8.
    """

    test_obj = DO.ApparelItem("Test Apparel", "1", False)
    assert len(test_obj.get_id()) == 8

def test_apparel_id_length_two():
    """
    Tests that an apparel's id is correct
    even if it is initially supplied as less than 8 characters.
    """

    test_obj = DO.ApparelItem("Test Apparel", "1", False)
    assert test_obj.get_id() == "00000001"

def test_apparel_id_length_three():
    """
    Tests that an apparel's id length is 8 characters
    even if it is initially supplied as more than 8.
    """

    test_obj = DO.ApparelItem("Test Apparel", "AAAAAAAA1", False)
    assert len(test_obj.get_id()) == 8

def test_apparel_id_length_four():
    """
    Tests that an apparel's id is correct
    even if it is initially supplied as more than 8 characters.
    """

    test_obj = DO.ApparelItem("Test Apparel", "AAAAAAAA1", False)
    assert test_obj.get_id() == "AAAAAAA1"

def test_aid_id_length_one():
    """
    Tests that an aid's id length is 8 characters
    even if it is initially supplied as less than 8.
    """

    test_obj = DO.AidItem("Test Aid", "1", False)
    assert len(test_obj.get_id()) == 8

def test_aid_id_length_two():
    """
    Tests that an aid's id is correct
    even if it is initially supplied as less than 8 characters.
    """

    test_obj = DO.AidItem("Test Aid", "1", False)
    assert test_obj.get_id() == "00000001"

def test_aid_id_length_three():
    """
    Tests that an aid's id length is 8 characters
    even if it is initially supplied as more than 8.
    """

    test_obj = DO.AidItem("Test Aid", "AAAAAAAA1", False)
    assert len(test_obj.get_id()) == 8

def test_aid_id_length_four():
    """
    Tests that an aid's id is correct
    even if it is initially supplied as more than 8 characters.
    """

    test_obj = DO.AidItem("Test Aid", "AAAAAAAA1", False)
    assert test_obj.get_id() == "AAAAAAA1"
