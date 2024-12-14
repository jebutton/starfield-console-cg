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
            "Ammo_Name": self.ammo_name,
            "Ammo_ID": self.ammo_id
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
