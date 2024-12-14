"""
    A module containing clases representing different types of objects.
"""
from abc import ABC, abstractmethod

class ItemType(ABC):
    """
        A abstract class to ensure all of the item classes
        have the minimum fields to make the menus work.
    """
    @abstractmethod
    def get_name(self):
        """
        Return the item name, used for display purposes.
        """
        pass
    @abstractmethod
    def get_id(self):
        """
        Return the item id, used for console code purposes.
        """
        pass


class AmmoItem(ItemType):
    """
        A class representing the data needed to deal with
        an ammo object without costly pandas overhead.
    """

    def __init__(self, ammo_name: str, ammo_id: int):
        """
        Initialize an AmmoItem object.

        :param ammo_name: The name of the ammunition.
        :param ammo_id: The ID of the ammunition.
        """
        self.ammo_name = ammo_name
        self.ammo_id = ammo_id

    def __repr__(self):
        """
        Return a str representation of the AmmoItem object.
        :return: str version of AmmoItem
        """

        return f"AmmoItem(ammo_name='{self.ammo_name}', ammo_id={self.ammo_id})"

    def to_dict(self):
        """
        Convert the AmmoItem object to a dictionary.

        :return: A dictionary representation of the AmmoItem object.
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
        :param dlc: whether the item is a DLC item or not 
        # TODO: Handle DLC Items
        """
        self.spacesuit_name = spacesuit_name
        self.spacesuit_id = spacesuit_id
        self.dlc = dlc

    def __repr__(self):
        """
        Return a str representation of the SpacesuitItem object.
        :return: str version of AmmoItem
        """

        return f"SpacesuitItem(spacesuit_name='{self.ammo_name}', spacesuit_id={self.ammo_id}, dlc={self.dlc})"

    def to_dict(self):
        """
        Convert the SpacesuitItem object to a dictionary.

        :return: A dictionary representation of the SpacesuitItem object.
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
