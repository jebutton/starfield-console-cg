"""
    A module containing clases representing different types of objects.
"""
from abc import ABC, abstractmethod

class ItemType(ABC):
    """
        An abstract class to ensure all of the item classes
        have the minimum fields to make the menus work.
    """
    @abstractmethod
    def get_name(self):
        """
        Return the item name, used for display purposes.
        
        :return: A str of the item name.
        """

    @abstractmethod
    def get_id(self):
        """
        Return the item id, used for console code purposes.
        
        :return: A str of the item ID
        """

    @abstractmethod
    def get_command(self, number: int):
        """
        Return the console command to be generated.
        
        :param number: A int of how many items you want to generate.
            
        :return: A str of the console command.
        """

class AmmoItem(ItemType):
    """
        A class representing the data needed to deal with
        an ammo object without costly pandas overhead.
    """

    def __init__(self, ammo_name: str, ammo_id: int):
        """
        The constructor for the AmmoItem Class

        :param ammo_name: The name of the ammunition.
        :param ammo_id: The ID of the ammunition.

        to_dict(): Convert the AmmoItem object to a dict.
        get_name(): Return the name of the ammunition.
        get_id(): Get the ID of the ammunition.
        get_command(): Get the console command to add the item in game.
        """

        self.ammo_name = ammo_name
        self.ammo_id = ammo_id

    def __repr__(self):
        """
        Return a str representation of the AmmoItem object.

        :return: A str version of AmmoItem.
        """

        return f"AmmoItem(ammo_name='{self.ammo_name}', ammo_id={self.ammo_id})"

    def to_dict(self):
        """
        Convert the AmmoItem object to a dict.

        :return: A dict representation of the AmmoItem object.
        """

        return {
            "ammo_name": self.ammo_name,
            "ammo_id": self.ammo_id
        }

    def get_name(self):
        """
        Return the name of the ammunition.
        
        :return: A str of the ammo name.
        """

        return self.ammo_name

    def get_id(self):
        """
        Return the ID code of the ammunition.
        
        :return: A str of the ammo ID.
        """

        return self.ammo_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.
        
        :param number: A int of how many items you want to generate.
            
        :return: A str of the console command.
        """

        return f"player.additem {self.ammo_id} {number}"

class SpacesuitItem(ItemType):
    """
        A class representing the data needed to deal with
        a SpacesuitItem object without costly pandas overhead.
    """

    def __init__(self, spacesuit_name: str, spacesuit_id: int, dlc: bool):
        """
        Initialize an SpacesuitItem object.

        :param spacesuit_name: The name of the spacesuit.
        :param spacesuit_id: The ID of the spacesuit.
        :param dlc: A bool of whether the item is a DLC item or not.
        """
        self.spacesuit_name = spacesuit_name
        self.spacesuit_id = spacesuit_id

        # TODO: Handle DLC Items
        self.dlc = dlc

    def __repr__(self):
        """
        Return a str representation of the SpacesuitItem object.

        :return: A str version of SpacesuitItem.
        """

        return f"SpacesuitItem(spacesuit_name='{self.spacesuit_name}', \
          spacesuit_id={self.spacesuit_id}, dlc={self.dlc})"

    def to_dict(self):
        """
        Convert the SpacesuitItem object to a dict.

        :return: A dict representation of the SpacesuitItem object.
        """

        return {
            "spacesuit_name": self.spacesuit_name,
            "spacesuit_id": self.spacesuit_id,
            "dlc": self.dlc
        }

    def get_name(self):
        """
        Return the name of the spacesuit.
        
        :return: A str of the spacesuit name.
        """

        return self.spacesuit_name

    def get_id(self):
        """
        Return the ID code of the spacesuit.
        
        :return: A str of the spacesuit ID.
        """

        return self.spacesuit_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.
            
        :return: A str of the console command.
        """

        return f"player.additem {self.spacesuit_id} {number}"

class PackItem(ItemType):
    """
        A class representing the data needed to deal with
        a PackItem object without costly pandas overhead.
    """

    def __init__(self, pack_name: str, pack_id: int, dlc: bool):
        """
        Initialize an PackItem object.

        :param pack_name: The name of the pack.
        :param pack_id: The ID of the pack.
        :param dlc: A bool of whether the item is a DLC item or not.
        """

        self.pack_name = pack_name
        self.pack_id = pack_id

        # TODO: Handle DLC Items
        self.dlc = dlc

    def __repr__(self):
        """
        Return a str representation of the PackItem object.

        :return: A str version of PackItem.
        """

        return f"PackItem(pack_name='{self.pack_name}', \
          pack_id={self.pack_id}, dlc={self.dlc})"

    def to_dict(self):
        """
        Convert the PackItem object to a dict.

        :return: A dict representation of the PackItem object.
        """

        return {
            "pack_name": self.pack_name,
            "pack_id": self.pack_id,
            "dlc": self.dlc
        }

    def get_name(self):
        """
        Return the name of the pack.
        
        :return: A str of the pack name.
        """

        return self.pack_name

    def get_id(self):
        """
        Return the ID code of the pack.
        
        :return: A str of the pack ID.
        """

        return self.pack_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.
           
        :return: A str of the console command.
        """

        return f"player.additem {self.pack_id} {number}"

class HelmetItem(ItemType):
    """
        A class representing the data needed to deal with
        a HelmetItem object without costly pandas overhead.
    """

    def __init__(self, helmet_name: str, helmet_id: int, dlc: bool):
        """
        Initialize an HelmetItem object.

        :param helmet_name: The name of the helmet.
        :param helmet_id: The ID of the helmet.
        :param dlc: A bool of whether the item is a DLC item or not. 
        """

        self.helmet_name = helmet_name
        self.helmet_id = helmet_id

        # TODO: Handle DLC Items
        self.dlc = dlc

    def __repr__(self):
        """
        Return a str representation of the HelmetItem object.

        :return: A str version of HelmetItem
        """

        return f"HelmetItem(helmet_name='{self.helmet_name}', \
          helmet_id={self.helmet_id}, dlc={self.dlc})"

    def to_dict(self):
        """
        Convert the HelmetItem object to a dict.

        :return: A dict representation of the HelmetItem object.
        """

        return {
            "helmet_name": self.helmet_name,
            "helmet_id": self.helmet_id,
            "dlc": self.dlc
        }

    def get_name(self):
        """
        Return the name of the helmet.
        
        :return: A str of the helmet name.
        """

        return self.helmet_name

    def get_id(self):
        """
        Return the ID code of the helmet.
        
        :return: A str of the helmet ID.
        """

        return self.helmet_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.

        :return: A str of the console command.
        """


        return f"player.additem {self.helmet_id} {number}"

class SpacesuitSetItem(ItemType):
    """
        A class representing the data needed to deal with
        a SpacesuitSetItem object without costly pandas overhead.
    """

    def __init__(self, spacesuit_set_name: str, dlc: bool):
        """
        Initialize an SpacesuitSetItem object.

        :param spacesuit_set_name: The name of the spacesuit_set.
        :param dlc: A bool of whether the item is a DLC item or not.
        """

        self.spacesuit_set_name = spacesuit_set_name

        # TODO: Handle DLC Items
        self.dlc = dlc

        self.spacesuit = None
        self.helmet = None
        self.pack = None
        self.faction = None
        self.spacesuit_set_id = None

    def __repr__(self):
        """
        Return a str representation of the Spacesuit_SetItem object.

        :return: A str version of SpaceSuitItem.
        """

        return f"SpacesuitSetItem(spacesuit_set_name='{self.spacesuit_set_name}', \
          spacesuit={self.spacesuit}, helmet= {self.helmet}, pack={self.pack}, \
            dlc={self.dlc}, faction={self.faction})"

    def to_dict(self):
        """
        Convert the SpacesuitSetItem object to a dict.

        :return: A dict representation of the SpacesuitSetItem object.
        """

        return {
            "spacesuit_set_name": self.spacesuit_set_name,
            "spacesuit": self.spacesuit,
            "helmet": self.helmet,
            "pack": self.pack,
            "dlc": self.dlc,
            "faction": self.faction
        }

    def set_id(self):
        """
            Sets the spacesuit_set_id value based on internal values.
        """

        self.spacesuit_set_id = self.get_id()

    def set_spacesuit(self, spacesuit: SpacesuitItem):
        """
            Sets the spacesuit.

            :param spacesuit: A SpacesuitItem for the spacesuit in the set.
        """

        self.spacesuit = spacesuit
        self.set_id()

    def set_helmet(self, helmet: HelmetItem):
        """
            Sets the helmet.
        
            :param helmet: A HelmetItem for the helmet in the set.
        """

        self.helmet = helmet
        self.set_id()

    def set_pack(self, pack: PackItem):
        """
            Sets the pack.

            :param pack: A PackItem for the Helmet in the set.
        """

        self.pack = pack
        self.set_id()

    def set_faction(self, faction: str):
        """
            Sets the faction.
            :param faction: A str for the name of the faction in the set.
        """

        self.faction = faction

    def get_name(self):
        """
        Return the name of the SpacesuitSetItem.
        
        :return: A str of the SpacesuitSetItem name.
        """

        return self.spacesuit_set_name

    def get_id(self):
        """
        Return the ID code of all of the 
        items in the spacesuit_set.
        
        :return: A str of the spacesuit_set ID.
        """

        if self.spacesuit is not None:
            spacesuit_id = self.spacesuit.spacesuit_id
        else:
            spacesuit_id = None
        if self.helmet is not None:
            helmet_id = self.helmet.helmet_id
        else:
            helmet_id = None
        if self.pack is not None:
            pack_id = self.pack.pack_id
        else:
            pack_id = None

        return (spacesuit_id,
                helmet_id,
                pack_id)

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.

        :return: A str of the console command.
        """

        output_str_list = []
        for item_id in self.get_id():
            if item_id is not None:
                output_str_list.append(f"player.additem {item_id} {number}")
        output_str = "\n".join(output_str_list)

        return output_str

class WeaponItem(ItemType):
    """
        A class representing the data needed to deal with
        a WeaponItem object without costly pandas overhead.
    """

    def __init__(self, weapon_name: str, weapon_id: int, dlc: bool, unique: bool):
        """
        Initialize an WeaponItem object.

        :param weapon_name: The name of the weapon.
        :param weapon_id: The ID of the weapon.
        :param dlc: A bool of whether the item is a DLC item or not. 
        :param unique: A bool of whether the item is a unique weapon or not.
        """

        self.weapon_name = weapon_name
        self.weapon_id = weapon_id

        # TODO: Handle DLC Items
        self.dlc = dlc

        # TODO: Handle unique weapons.
        self.unique = unique

    def __repr__(self):
        """
        Return a str representation of the WeaponItem object.

        :return: A str version of WeaponItem
        """

        return f"WeaponItem(weapon_name='{self.weapon_name}', \
          weapon_id={self.weapon_id}, dlc={self.dlc})"

    def to_dict(self):
        """
        Convert the WeaponItem object to a dict.

        :return: A dict representation of the WeaponItem object.
        """

        return {
            "weapon_name": self.weapon_name,
            "weapon_id": self.weapon_id,
            "dlc": self.dlc,
            "unique": self.unique
        }

    def get_name(self):
        """
        Return the name of the weapon.
        
        :return: A str of the weapon name.
        """

        return self.weapon_name

    def get_id(self):
        """
        Return the ID code of the weapon.
        
        :return: A str of the weapon ID.
        """

        return self.weapon_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.

        :return: A str of the console command.
        """


        return f"player.additem {self.weapon_id} {number}"
