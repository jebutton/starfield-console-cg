"""
    A module containing classes to read from the datasheet
    and store that information as datastructures for the rest
    of the program.
"""
import pandas as pd
from .data_objects import AmmoItem, SpacesuitItem, PackItem, HelmetItem
from .data_objects import SpacesuitSetItem, WeaponItem, ResourceItem, StatusModType
from .data_objects import QualityModType

# pylint: disable=too-many-instance-attributes
class DataFileReader:
    """
        Handles the reading of all of the sheets in the datasheet.
    """

    def __init__(self, file_path: str):
        """
        Initialize the DataFileReader with the file path.

        :param file_path: The str filepath to the data table.
        """

        self.file_path = file_path
        self.sheet_names = [
            "Resources", "Spacesuits", "Helmets", "Packs",
            "Spacesuit_Sets", "Weapons", "Ammo", "Armor_Status_Mods", "Weapon_Status_Mods",
            "Armor_Quality_Mods", "Weapon_Quality_Mods"
        ]

        self.pretty_sheet_names = [name.replace("_", " ") for name in self.sheet_names]
        self.datasheets = self.read_sheets()
        self.ammo_data = self.get_ammo_data()
        self.spacesuit_data = self.get_spacesuit_data()
        self.pack_data = self.get_pack_data()
        self.helmet_data = self.get_helmet_data()
        self.spacesuit_set_data = self.get_spacesuit_set_data(self.spacesuit_data,
                                                                self.helmet_data,
                                                                self.pack_data)
        self.weapon_data = self.get_weapon_data()
        self.resource_data = self.get_resource_data()
        self.weapon_status_mods_data = self.get_status_mod_data("Weapon_Status_Mods")
        self.armor_status_mods_data = self.get_status_mod_data("Armor_Status_Mods")
        self.armor_quality_mods_data = self.get_quality_mod_data("Armor_Quality_Mods")
        self.weapon_quality_mods_data = self.get_quality_mod_data("Weapon_Quality_Mods")

    def read_sheets(self):
        """
        Read the specified sheets from the Excel file.

        :return: A dict where keys are sheet names and values are DataFrames.
        """

        # pylint: disable=broad-exception-caught

        data = {}
        try:
            for sheet in self.sheet_names:
                # print(sheet)
                data[sheet] = pd.read_excel(self.file_path, sheet_name=sheet)

        except Exception as e:
            print(f"Error reading Excel file: {e}")

        return data

    def get_row_index(self, dataframe_ref: pd.DataFrame, search_column_name: str,
                      search_column_val: str):
        """
        Return the row index of particular value in a particular sheet given the DataFrame ref,
        the name of the column, and the value you're searching for.
        
        :param dataframe_ref: A pandas.DataFrame reference to the dataframe name.
        :param search_column_name: A str Column Name to search for.
        :param search_column_val: A str the value in that column to search to get the row number.

        :return: an integer with the row number for pandas.
        """

        return dataframe_ref[search_column_name].array.tolist().index(search_column_val)

    def get_cell_value(self, dataframe_ref: pd.DataFrame,
                       search_column_name: str, search_column_value: str,
                       tgt_column_name: str):
        """
        Return a cell's value based on a DataFrame ref, a column name to search in, a value
        in that column to search for, and the name of the column you want to return.

        :param dataframe_ref: A pandas.DataFrame reference to the dataframe name.
        :param search_column_name: A str Column Name to search for.
        :param search_column_val: A str the value in that column to search to get the row number.
        :param target_column_name: A str The column name to pull the actual value from.
        
        :return: A str with that cells's data.
        """

        return dataframe_ref.at[self.get_row_index(
            dataframe_ref, search_column_name, search_column_value), tgt_column_name]

    @staticmethod
    def get_status_mods_by_mod_slot(slot: int, mod_dict: dict):
        """
        Return a dict containing all a StatusModType objects with 
        a specific mod_slot value

        :param slot: An int value for the target slot.
        :param mod_dict: A dict containing the status mods.

        :return: A dict with a subset of a StatusModType dict containing \
only items with a specific mod slot.
        """

        output_dict = {}
        for status_mod in mod_dict.values():
            if status_mod.get_mod_slot() == slot:
                output_dict[status_mod.get_name().lower()] = status_mod
        return output_dict

    def get_weapons_by_unique(self, want_unique: bool):
        """
        Selects a subset of weapons based on whether they're unique or not.
        
        :param want_unique: A bool of whether you want unique weapons or not unique weapons.
        """

        data_dict = {}
        for weapon in list(self.weapon_data.values()):
            if weapon.unique is want_unique:
                data_dict[weapon.get_name().lower()] = weapon

        return data_dict

    def get_weapons_by_type(self, tgt_weapon_type: str):
        """
        Selects a subset of weapons based on type.
        
        :param tgt_weapon_type: A str of the weapon type to select for.
        """

        data_dict = {}
        if tgt_weapon_type not in WeaponItem.get_valid_weapon_types():
            raise ValueError("Invalid Weapon Type")
        for weapon in list(self.weapon_data.values()):
            if weapon.weapon_type == tgt_weapon_type:
                data_dict[weapon.get_name().lower()] = weapon

        return data_dict

    def get_ammo_data(self):
        """
        Return a dict containing all of the Ammo page data.

        :return: A dict with all of the Ammo page data.
        """

        num_rows = self.datasheets["Ammo"].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets["Ammo"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = AmmoItem(temp_row.iloc[0].strip(), temp_row.iloc[1].strip())
            output_dict[temp_key] = temp_value

        return output_dict

    def get_spacesuit_data(self):
        """
        Return a dict containing all of the Spacesuit page data.

        :return: A dict with all of the Spacesuit page data.
        """

        num_rows = self.datasheets["Spacesuits"].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets["Spacesuits"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = SpacesuitItem(temp_row.iloc[0].strip(),
                                  str(temp_row.iloc[1]).strip(),
                                  bool(temp_row.iloc[2]))
            output_dict[temp_key] = temp_value

        return output_dict

    def get_pack_data(self):
        """
        Return a dict containing all of the Pack page data.

        :return: A dict with all of the Pack page data.
        """

        num_rows = self.datasheets["Packs"].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets["Packs"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = PackItem(temp_row.iloc[0].strip(),
                                  str(temp_row.iloc[1]).strip(),
                                  bool(temp_row.iloc[2]))
            output_dict[temp_key] = temp_value

        return output_dict

    def get_helmet_data(self):
        """
        Return a dict containing all of the Helmet page data.

        :return: A dict with all of the Helmet page data.
        """

        num_rows = self.datasheets["Helmets"].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets["Helmets"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = HelmetItem(temp_row.iloc[0].strip(),
                                  str(temp_row.iloc[1]).strip(),
                                  bool(temp_row.iloc[2]))
            output_dict[temp_key] = temp_value

        return output_dict

    def get_spacesuit_set_data(self, spacesuits: dict,
                                helmets: dict, packs: dict):
        """
        Return a dict of all of the spacesuit sets

        :param spacesuits: A dict The dict with all of the SpacesuitItem objects in it.
        :param helmets: A dict The dict with all of the HelmetItem objects in it.
        :param packs: A dict The dict with all of the PackItem objects in it.

        :return: A dict with all of the spacesuit sets.
        """

        num_rows = self.datasheets["Spacesuit_Sets"].shape[0]
        output_dict = {}

        for row in range(num_rows):
            temp_row = self.datasheets["Spacesuit_Sets"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()

            temp_value = SpacesuitSetItem(temp_row.iloc[0].strip(),
                                    str(temp_row.iloc[5]).strip())

            if pd.isna(temp_row.iloc[1]) is not True:
                temp_value.set_spacesuit(spacesuits[str(temp_row.iloc[1]).strip().lower()])
            if pd.isna(temp_row.iloc[2]) is not True:
                temp_value.set_helmet(helmets[str(temp_row.iloc[2]).strip().lower()])
            if pd.isna(temp_row.iloc[3]) is not True:
                temp_value.set_pack(packs[str(temp_row.iloc[3]).strip().lower()])
            if pd.isna(temp_row.iloc[4]) is not True:
                temp_value.set_faction(str(temp_row.iloc[4]).strip().lower())
            output_dict[temp_key] = temp_value

        return output_dict

    def get_weapon_data(self):
        """
        Return a dict containing all of the Weapon page data.

        :return: A dict with all of the Weapon page data.
        """

        num_rows = self.datasheets["Weapons"].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets["Weapons"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = WeaponItem(str(temp_row.iloc[0]).strip(),
                                  str(temp_row.iloc[1]).strip(),
                                  bool(temp_row.iloc[2]),
                                  bool(temp_row.iloc[3]),
                                  str(temp_row.iloc[4]).strip())
            output_dict[temp_key] = temp_value

        return output_dict

    def get_resource_data(self):
        """
        Return a dict containing all of the Resource page data.

        :return: A dict with all of the Resource page data.
        """

        num_rows = self.datasheets["Resources"].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets["Resources"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = ResourceItem(temp_row.iloc[0].strip(), temp_row.iloc[1].strip())
            output_dict[temp_key] = temp_value

        return output_dict

    def get_status_mod_data(self, sheet_name: str):
        """
        Return a dict containing all of the Weapon_Status_Mods page data.
        
        :param sheet_name: The str of the name of the sheet to pull the data from.

        :return: A dict with all of the Weapon_Status_Mods page data
        """

        num_rows = self.datasheets[sheet_name].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets[sheet_name].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = StatusModType(temp_row.iloc[0].strip(),
                                        temp_row.iloc[1].strip(),
                                        temp_row.iloc[2].strip(),
                                        temp_row.iloc[3])
            output_dict[temp_key] = temp_value
        return output_dict

    def get_quality_mod_data(self, sheet_name: str):
        """
        Return a dict containing all of the data for a quality mod.

        :param sheet_name: The str of the name of the sheet to pull the data from.
        :return: A dict with all of a quality mod page's data.
        """

        num_rows = self.datasheets[sheet_name].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets[sheet_name].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = QualityModType(temp_row.iloc[0].strip(),
                                        temp_row.iloc[1].strip())
            output_dict[temp_key] = temp_value
        return output_dict
