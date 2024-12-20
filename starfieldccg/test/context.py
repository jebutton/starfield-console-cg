"""
    Makes it so that the tests have the context of the ../src directory.
"""

import sys
from os import path as OSPATH
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), '../.')))
print(OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), '../src')))
# sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), '../..')))
# pylint: disable=wrong-import-position
# pylint: disable=import-error
# pylint: disable=unused-import
import src.data_file_reader as DFR
import src.data_objects as DO
import src.menu_views as MV

class SCCGTestContext():
    """
        A class to handle all of the contextual information that the test classes need.
    """
    PATH_TO_DATASHEET = OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  '../src/data/Starfield_Datatable.xls'))
    @staticmethod
    def get_a_dfr():
        """
        Static Method, returns a DataFileReader object that uses the correct path 
        to the datasheet.

        :return: A DataFileReader object that likely works.
        """
        return DFR.DataFileReader(SCCGTestContext.PATH_TO_DATASHEET)
