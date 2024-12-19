"""
    Makes it so that the tests have the context of the ../src directory.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
# pylint: disable=wrong-import-position
# pylint: disable=import-error
# pylint: disable=unused-import
import data_file_reader
import data_objects
import menu_views
