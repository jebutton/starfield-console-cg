"""
    A module containg classes to read from the datasheet
    and store that information as datastructures for the rest
    of the program.
"""
import pandas as pd
from .data_objects import AmmoItem, SpacesuitItem, PackItem, HelmetItem
from .data_objects import SpacesuitSetItem, WeaponItem, ResourceItem

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
            "Spacesuit_Sets", "Weapons", "Ammo", "Armor_Status_Mods", "Weapon_Status_Mods"
        ]
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

        # To be implemented
        self.armor_status_mods_data = {}
        self.weapon_status_mods_data = {}
        self.armor_quality_mods_data = {}
        self.weapon_quality_mods_data = {}

    def read_sheets(self):
        """
        Read the specified sheets from the Excel file.

        :return: A dict where keys are sheet names and values are DataFrames.
        """

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

    def get_ammo_data(self):
        """
        Return a dict containing all of the Ammo page data.

        :return: A dict with all of the Ammo page data.
        """

        # TODO: Handle DLC Items

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

        # TODO: Handle DLC Items

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

        # TODO: Handle DLC Items

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

        # TODO: Handle DLC Items

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

        # TODO: Handle DLC Items

        num_rows = self.datasheets["Spacesuit_Sets"].shape[0]
        output_dict = {}

        for row in range(num_rows):
            temp_row = self.datasheets["Spacesuit_Sets"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()

            temp_value = SpacesuitSetItem(temp_row.iloc[0].strip(),
                                    str(temp_row.iloc[5]).strip())
            # print(pd.isna(temp_row.iloc[1]))

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

        # TODO: Handle DLC Items
        num_rows = self.datasheets["Weapons"].shape[0]
        output_dict = {}
        for row in range(num_rows):
            temp_row = self.datasheets["Weapons"].loc[row]
            temp_key = temp_row.iloc[0].strip().lower()
            temp_value = WeaponItem(temp_row.iloc[0].strip(),
                                  str(temp_row.iloc[1]).strip(),
                                  bool(temp_row.iloc[2]),
                                  bool(temp_row.iloc[3]))
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
