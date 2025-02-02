"""
    Makes it so that the tests have the context of the ../src directory.
"""

import sys
from os import path as OSPATH
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), '../.')))
# pylint: disable=wrong-import-position
# pylint: disable=import-error
# pylint: disable=unused-import
import src.data_file_reader as DFR
import src.data_objects as DO
import src.menu_views as MV
import src.settings_io as SIO

# pylint: disable=too-few-public-methods
class SCCGTestContext():
    """
        A class to handle all of the contextual information that the test classes need.
    """

    def __init__(self):
        """
        This class is just to be able to share certain resources between test classes.
        """
        self.known_datasheet_path = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  '../data/Starfield_Datatable.xls'))

    def get_a_dfr(self):
        """
        Static Method, returns a DataFileReader object that uses the correct path 
        to the datasheet.

        :return: A DataFileReader object that likely works.
        """
        return DFR.DataFileReader(self.known_datasheet_path)
