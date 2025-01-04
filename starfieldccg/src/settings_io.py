"""
A module to write and contain settings
"""
import json
import string
from os import path as OSPATH


class SCCGSettings():
    """
    A class holding all of the settings information.
    """

    def __init__(self, settings_file_path: str):
        """
        Create a SCCGSettings object.

        :param settings_file_path: A JSON object with the settings data
        """

        self.settings_file_path = settings_file_path
        # self.dlc_load_order = "FF"
        self.settings = {}
        self.load_settings()


    def set_dlc_load_order(self, load_order: str):
        """
        Sets the load order and auto-saves the settings.

        :param load_order: a str of the load order for the dlc. 
        """
        if len(load_order) == 2 and load_order[0] in string.hexdigits \
        and load_order[1] in string.hexdigits:
            self.settings["dlc_load_order"] = load_order
            self.save_settings()
        else:
            raise ValueError("DLC Load order must be only two characters long and valid hex.")


    def to_dict(self):
        """
        Convert the SCCGSettings object to a dict.

        :return: A dict representation of the SCCGSettings object.
        """

        return {
            "name": "SCCGSettings Class",
            "settings": self.settings
        }

    def save_settings(self):
        """
        Saves the settings to a file.
        """

        with open(self.settings_file_path, "w", 1, "UTF-8") as settings_file:
            output_json = json.dumps(self.to_dict())
            settings_file.write(output_json)

        settings_file.close()

    def load_settings(self):
        """
        Loads the settings from the settings file.
        """

        with open(self.settings_file_path, "r", 1, "UTF-8") as settings_file:
            file_data = json.load(settings_file)

            #self.dlc_load_order = file_data["dlc_load_order"]
            self.settings["dlc_load_order"] = file_data["settings"]["dlc_load_order"]

        settings_file.close()

global_settings = SCCGSettings(OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__),
                                                  '../data/settings_data.json')))
