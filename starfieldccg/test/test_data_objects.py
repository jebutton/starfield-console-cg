"""
    Tests the data_objects module.
"""
import pytest
from .context import DO


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
