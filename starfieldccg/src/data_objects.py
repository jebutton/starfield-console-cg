"""
    A module containing classes representing different types of items.
"""
from abc import abstractmethod
import sys
from os import path as OSPATH
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), './')))
import settings_io

class ItemType():
    """
        A class to ensure all of the item classes
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
        
        :return: A str of the item id
        """

    @abstractmethod
    def get_command(self, number: int):
        """
        Return the console command to be generated.
        
        :param number: A int of how many items you want to generate.
            
        :return: A str of the console command.
        """

    def process_id(self, dlc: bool):
        """
        Takes an id and modifies it so it works with the correct DLC
        and it is the correct length.

        :param dlc: A bool representing whether or not the item is from a DLC.

        :return: A str with a processed id value.
        """
        temp_id_list = list(self.get_id())
        dlc_prefix = settings_io.global_settings.settings["dlc_load_order"]

        if len(temp_id_list) != 8:
            # Replace placeholder chars with zeros
            for i, char in enumerate(temp_id_list):
                if char.lower() == "x":
                    temp_id_list[i] = "0"

            # Strip the leading zeros if there are too many.
            if len(temp_id_list) > 8:
                while len(temp_id_list) > 8:
                    temp_id_list.pop(0)

            # Pad the string to left with zeros if there are too few.
            while len(temp_id_list) < 8:
                temp_id_list.insert(0, "0")

        if dlc is True:
            # Replace the first two characters in the id with the load order.
            temp_id_list[0] = dlc_prefix[0]
            temp_id_list[1] = dlc_prefix[1]

        return "".join(temp_id_list)


class AmmoItem(ItemType):
    """
        A class representing the data needed to deal with
        an ammo object without costly pandas overhead.
    """

    def __init__(self, ammo_name: str, ammo_id: int):
        """
        The constructor for the AmmoItem Class

        :param ammo_name: The name of the ammunition.
        :param ammo_id: The id of the ammunition.

        to_dict(): Convert the AmmoItem object to a dict.
        get_name(): Return the name of the ammunition.
        get_id(): Get the id of the ammunition.
        get_command(): Get the console command to add the item in game.
        """

        self.ammo_name = ammo_name
        self.ammo_id = ammo_id
        self.ammo_id = self.process_id(False)

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
        Return the id code of the ammunition.
        
        :return: A str of the ammo id.
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
        Initialize a SpacesuitItem object.

        :param spacesuit_name: The name of the spacesuit.
        :param spacesuit_id: The id of the spacesuit.
        :param dlc: A bool of whether the item is a DLC item or not.
        """
        self.spacesuit_name = spacesuit_name
        self.spacesuit_id = spacesuit_id
        self.dlc = dlc
        self.spacesuit_id = self.process_id(dlc)

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
        Return the id code of the spacesuit.
        
        :return: A str of the spacesuit id.
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
        Initialize a PackItem object.

        :param pack_name: The name of the pack.
        :param pack_id: The id of the pack.
        :param dlc: A bool of whether the item is a DLC item or not.
        """

        self.pack_name = pack_name
        self.pack_id = pack_id
        self.dlc = dlc
        self.pack_id = self.process_id(dlc)

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
        Return the id code of the pack.
        
        :return: A str of the pack id.
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
        Initialize a helmetItem object.

        :param helmet_name: The name of the helmet.
        :param helmet_id: The id of the helmet.
        :param dlc: A bool of whether the item is a DLC item or not. 
        """

        self.helmet_name = helmet_name
        self.helmet_id = helmet_id
        self.dlc = dlc
        self.helmet_id = self.process_id(dlc)

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
        Return the id code of the helmet.
        
        :return: A str of the helmet id.
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
        Initialize a SpacesuitSetItem object.

        :param spacesuit_set_name: The name of the spacesuit_set.
        :param dlc: A bool of whether the item is a DLC item or not.
        """

        self.spacesuit_set_name = spacesuit_set_name
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
        Return the id code of all of the 
        items in the spacesuit_set.
        
        :return: A str of the spacesuit_set id.
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

    def __init__(self, weapon_name: str, weapon_id: int, dlc: bool, unique: bool, weapon_type: str):
        """
        Initialize a WeaponItem object.

        :param weapon_name: The name of the weapon.
        :param weapon_id: The id of the weapon.
        :param dlc: A bool of whether the item is a DLC item or not. 
        :param unique: A bool of whether the item is a unique weapon or not.
        """
        # pylint: disable=too-many-positional-arguments
        # pylint: disable=too-many-arguments

        self.weapon_name = weapon_name
        self.weapon_id = weapon_id
        self.dlc = dlc
        self.weapon_id = self.process_id(dlc)
        self.unique = unique

        if weapon_type.lower() not in self.get_valid_weapon_types():
            raise ValueError("Invalid Type")

        self.weapon_type = weapon_type.lower()

    def __repr__(self):
        """
        Return a str representation of the WeaponItem object.

        :return: A str version of WeaponItem
        """

        return f"WeaponItem(weapon_name='{self.weapon_name}', \
          weapon_id='{self.weapon_id}', dlc={self.dlc}, unique={self.unique}, \
type='{self.weapon_type}')"

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
        Return the id code of the weapon.
        
        :return: A str of the weapon id.
        """

        return self.weapon_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.

        :return: A str of the console command.
        """
        return f"player.additem {self.weapon_id} {number}"

    @staticmethod
    def get_valid_weapon_types():
        """
        Allows other classes to get the known valid weapon types
        to check against without having to create an instance
        of the class.
        """
        valid_weapon_types = ["gun", "melee", "thrown"]
        return valid_weapon_types

class ResourceItem(ItemType):
    """
        A class representing the data needed to deal with
        a ResourceItem object without costly pandas overhead.
    """

    def __init__(self, resource_name: str, resource_id: int):
        """
        Initialize a ResourceItem object.

        :param resource_name: The name of the resource.
        :param resource_id: The id of the resource. 
        """

        self.resource_name = resource_name
        self.resource_id = resource_id
        self.resource_id = self.process_id(False)


    def __repr__(self):
        """
        Return a str representation of the ResourceItem object.

        :return: A str version of ResourceItem
        """

        return f"ResourceItem(resource_name='{self.resource_name}', \
          resource_id={self.resource_id})"

    def to_dict(self):
        """
        Convert the ResourceItem object to a dict.

        :return: A dict representation of the ResourceItem object.
        """

        return {
            "resource_name": self.resource_name,
            "resource_id": self.resource_id
        }

    def get_name(self):
        """
        Return the name of the resource.
        
        :return: A str of the resource name.
        """

        return self.resource_name

    def get_id(self):
        """
        Return the id code of the resource.
        
        :return: A str of the resource id.
        """

        return self.resource_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.

        :return: A str of the console command.
        """

        return f"player.additem {self.resource_id} {number}"

class StatusModType():
    """
    A class representing the data needed to deal with
    a StatusModType object without costly pandas overhead.
    """

    def __init__(self, status_mod_name: str, status_mod_id: int,
                 status_mod_desc: str, mod_slot: int):
        """
        Initialize a StatusModType object.

        :param status_mod_name: The name of the weapon status mod.
        :param status_mod_id: The id of the weapon status mod.
        :param status_mod_desc: The description of the weapon status mod.
        :param mod_slot: The slot for the mod (one of three) 
        """

        self.status_mod_name = status_mod_name
        self.status_mod_id = status_mod_id
        self.status_mod_desc = status_mod_desc
        self.mod_slot = mod_slot

        if self.mod_slot not in [1,2,3]:
            raise ValueError(f"Invalid mod_slot value: {self.mod_slot} is not in list \
                      [1,2,3]")

    def __repr__(self):
        """
        Return a str representation of the WeaponStatusModType object.

        :return: A str version of StatusModType
        """

        return f"StatusModType(status_mod_name='{self.status_mod_name}', \
            status_mod_id='{self.status_mod_id}', \
            status_mod_desc='{self.status_mod_desc}', \
            mod_slot={self.mod_slot})"

    def to_dict(self):
        """
        Convert the StatusModType object to a dict.

        :return: A dict representation of the StatusModType object.
        """

        return {
            "status_mod_name": self.status_mod_name,
            "status_mod_id": self.status_mod_id,
            "status_mod_desc": self.status_mod_id,
            "mod_slot": self.mod_slot
        }

    def get_name(self):
        """
        Return the name of the StatusModType.
        
        :return: A str of the StatusModType name.
        """

        return self.status_mod_name

    def get_id(self):
        """
        Return the id code of the status_mod.
        
        :return: A str of the status_mod id.
        """

        return self.status_mod_id

    def get_description(self):
        """
        Returns the description of the mod.

        :return: A str of the mod description
        """
        return self.status_mod_desc

    def get_mod_slot(self):
        """
        Returns the mod slot

        :return: An int of the mod slot.
        """

        return self.mod_slot

    def get_command(self):
        """
        Return the console command to be generated.

        :return: A str of the console command.
        """

        return f".amod {self.status_mod_id}"

class QualityModType():
    """
    Represents a Quality mod for weapons or armor.
    """

    def __init__(self, mod_name: str, mod_id: str):
        """
        Creates a QualityModType object for storing quality mods.

        :param mod_name A str representing the name of the mod.
        :param mod_id A str representing the id of the mod.
        """

        self.mod_name = mod_name
        self.mod_id = mod_id

    def __repr__(self):
        """
        Return a str representation of the QualityModType object.

        :return: A str version of QualityModType
        """

        return f"QualityModType(mod_name='{self.mod_name}', \
mod_id='{self.mod_id}')"

    def get_name(self):
        """
        Return the name of the QualityModType.
        
        :return: A str of the QualityModType name.
        """

        return self.mod_name

    def get_id(self):
        """
        Return the id code of the QualityModType.
        
        :return: A str of the QualityModType id.
        """

        return self.mod_id

    def get_command(self):
        """
        Return the console command to be generated.

        :return: A str of the console command.
        """

        return f".amod {self.mod_id}"

class ApparelItem(ItemType):
    """
        A class representing the data needed to deal with
        a ApparelItem object.
    """

    def __init__(self, apparel_name: str, apparel_id: int, dlc: bool):
        """
        Initialize a apparelItem object.

        :param apparel_name: The name of the apparel.
        :param apparel_id: The id of the apparel.
        :param dlc: A bool of whether the item is a DLC item or not. 
        """

        self.apparel_name = apparel_name
        self.apparel_id = apparel_id
        self.dlc = dlc
        self.apparel_id = self.process_id(dlc)

    def __repr__(self):
        """
        Return a str representation of the ApparelItem object.

        :return: A str version of ApparelItem
        """

        return f"ApparelItem(apparel_name='{self.apparel_name}', \
          apparel_id={self.apparel_id}, dlc={self.dlc})"

    def to_dict(self):
        """
        Convert the ApparelItem object to a dict.

        :return: A dict representation of the ApparelItem object.
        """

        return {
            "apparel_name": self.apparel_name,
            "apparel_id": self.apparel_id,
            "dlc": self.dlc
        }

    def get_name(self):
        """
        Return the name of the apparel.
        
        :return: A str of the apparel name.
        """

        return self.apparel_name

    def get_id(self):
        """
        Return the id code of the apparel.
        
        :return: A str of the apparel id.
        """

        return self.apparel_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.

        :return: A str of the console command.
        """

        return f"player.additem {self.apparel_id} {number}"

class AidItem(ItemType):
    """
        A class representing the data needed to deal with
        a AidItem object.
    """

    def __init__(self, aid_name: str, aid_id: int, dlc: bool):
        """
        Initialize a aidItem object.

        :param aid_name: The name of the aid.
        :param aid_id: The id of the aid.
        :param dlc: A bool of whether the item is a DLC item or not. 
        """

        self.aid_name = aid_name
        self.aid_id = aid_id
        self.dlc = dlc
        self.aid_id = self.process_id(dlc)

    def __repr__(self):
        """
        Return a str representation of the AidItem object.

        :return: A str version of AidItem
        """

        return f"AidItem(aid_name='{self.aid_name}', \
          aid_id={self.aid_id}, dlc={self.dlc})"

    def to_dict(self):
        """
        Convert the AidItem object to a dict.

        :return: A dict representation of the AidItem object.
        """

        return {
            "aid_name": self.aid_name,
            "aid_id": self.aid_id,
            "dlc": self.dlc
        }

    def get_name(self):
        """
        Return the name of the aid.
        
        :return: A str of the aid name.
        """

        return self.aid_name

    def get_id(self):
        """
        Return the id code of the aid.
        
        :return: A str of the aid id.
        """

        return self.aid_id

    def get_command(self, number: int):
        """
        Return the console command to be generated.

        :param number: A int of how many items you want to generate.

        :return: A str of the console command.
        """

        return f"player.additem {self.aid_id} {number}"
