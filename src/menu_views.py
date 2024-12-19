"""
    A module contain classes for menus.
"""
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from abc import ABC, abstractmethod
import os

class AutoCompleteList:
    """
        A class to simplify and standarize how the WordCompleter class
        is used in the project. 
    """

    def __init__(self, input_structure):
        """
        Initialize an AutoCompleteList object.

        :param input_structure the data structure to be handled for auto completion
        """
        self.input_structure = input_structure
        if isinstance(self.input_structure, dict):
            self.completer = self.generate_wordcompleter_list(self.input_structure)
        elif isinstance(input_structure, list):
            self.completer = WordCompleter(self.input_structure)
        else:
            # TODO handle exception properly
            print("invalid datastructure type. Type is {}".format(type(input_structure)))

    def __repr__(self):
        """
        Return a string representation of the AutoCompleteList object.
        """
        return "AutoCompleteList(input_structure='{}')".format(self.input_structure)

    def generate_wordcompleter_list(self, input_dict: dict):
        """
        Returns a WordCompleter Object for all the keys in the input_dict

        :return: a WordCompleter object with all the items in the input_dict
        """
        keys_list = input_dict.keys()
        return WordCompleter(keys_list)


class AmountPrompt():
    """
        This is a class to allow prompting for item amounts
    """
    def __init__(self):
        self.prompt_text = "How many items?>"
    def get_amount(self):
        """
            Prompts and returns the amount chosen.
        """
        return int(prompt(self.prompt_text))

class BaseMenu(ABC):
    """
        Represents the most basic menu.
    """
    def __init__(self, title: str):
        self.title = title

    def clear_screen(self):
        """
            Clears the screen
        """
        os.system("cls")

    @abstractmethod
    def display_menu(self):
        """
            Display the Menu
        """

class ItemMenu(BaseMenu):
    """
        This is a class to display a list of in-game items as a menu
        and provide a prompt for the user to choose them.
    """
    def __init__(self, input_dict: dict, title: str):
        """
        Initialize an ItemMenu object.

        :param input_dict the dictionary of objects to be displayed for the menu
        :param msg the message to display when the menu loads
        """
        super().__init__(title)
        self.input_dict = input_dict
        self.chunk_size = 12
        self.menu_items = self.get_menu_items()
        self.completer = AutoCompleteList(self.menu_items).completer
        self.display_chunks = self.split_menu_items()
        self.completer = AutoCompleteList(self.input_dict).completer
        self.amount = 0

    def __repr__(self):
        """
        Return a string representation of the ItemMenu object.
        """
        return "ItemMenu(input_dict='{}')".format(self.input_dict)

    def get_menu_items(self):
        """
        Return a list of all the menu items to select from

        :return: a list of all the menu items to select from.
        """
        return [item[1].get_name() for item in self.input_dict.items()]

    def split_menu_items(self):
        """
        Return a list containing all of the menu items split into chunks

        :return: a list of all the menu items split into string chunks with linebreaks.
        """
        output_list = []
        items_len = len(self.menu_items)
        if items_len > self.chunk_size:

            if items_len % self.chunk_size == 0:
                segment_counter = self.chunk_size
                temp_segment = ""

                for segment in range(int(items_len / 8)):

                    if segment_counter == self.chunk_size:
                        temp_segment = self.menu_items[:self.chunk_size]
                        segment_counter += self.chunk_size

                    else:
                        temp_segment = self.menu_items[segment_counter:segment_counter
                                                        + self.chunk_size]
                        segment_counter += self.chunk_size
                    output_list.append("\n".join(temp_segment))

            elif items_len / self.chunk_size > 1.0:
                loop_length = int((items_len - items_len % self.chunk_size) / 8)
                segment_counter = self.chunk_size
                temp_segment = ""

                for segment in range(loop_length):

                    if segment_counter == self.chunk_size:
                        temp_segment = self.menu_items[:self.chunk_size]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.chunk_size

                    elif items_len - segment_counter >= self.chunk_size:
                        temp_segment = self.menu_items[segment_counter:segment_counter
                                                        + self.chunk_size]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.chunk_size

                temp_segment = self.menu_items[segment_counter: items_len]
                output_list.append("\n".join(temp_segment))

        else:
            temp_segment = self.menu_items[:items_len]
            output_list.append("\n".join(temp_segment))
        return output_list

    def display_menu(self):
        """
        Generate a visual menu list of items to select
        
        :return: The selected menu item name or "end" if the user wants to exit.
        """
        finished = False
        result = (False, 0)
        while finished is not True:
            for chunk in self.display_chunks:
                self.clear_screen()
                print(self.title)
                if chunk != self.display_chunks[-1]:
                    valid_input = False
                    while valid_input is not True:
                        print(chunk)
                        user_input = prompt("Type Item name or type next to continue>",
                                        completer=self.completer).lower()
                        if user_input in self.input_dict:
                            valid_input = True
                            finished = True
                            amount = AmountPrompt().get_amount()
                            result = (user_input, amount)
                        elif user_input == "next":
                            valid_input = True
                        else:
                            print("Incorrect User Input.")
                    if finished is True:
                        break
                else:
                    valid_input = False
                    while valid_input is not True:
                        print(chunk)
                        user_input = prompt("Type Item name, repeat to continue, or end to finish>",
                                            completer=self.completer).lower()
                        if user_input in self.input_dict:
                            finished = True
                            valid_input = True
                            amount = AmountPrompt().get_amount()
                            result = (user_input, amount)
                        elif user_input == "end":
                            finished = True
                            valid_input = True
                            result = ("end",0)
                            break
                        elif user_input == "repeat":
                            valid_input = True
                        else:
                            print("Incorrect User Input.")
                    if finished is True:
                        break
        return result


class NavMenu(BaseMenu):
    """
        This is a class to display a list of navigation options as a menu
        and provide a prompt for the user to choose them.
    """
    def __init__(self, menu_items: list, title: str, text_prompt: str):
        """
        Initialize an NavMenu object.
        """
        super().__init__(title)
        self.menu_items = [item.lower() for item in menu_items]
        self.completer = AutoCompleteList(self.menu_items).completer
        self.text_prompt = text_prompt

    def __repr__(self):
        """
        Return a string representation of the NavMenu object.
        """
        return_str = "NavMenu(menu_items='{}', completer={}, title={}, prompt={})".format(
            self.menu_items, self.completer, self.title, self.text_prompt)

        return return_str
    def display_menu(self):
        """
        Generate a visual menu list of items to select
        
        :return: The selected menu item name or "quit" if the user quits
        """
        menu_str = "\n".join([item.capitalize() for item in self.menu_items])
        finished = False
        result = ""
        while finished is not True:
            valid_input = False
            while valid_input is not True:
                self.clear_screen()
                print(self.title)
                print(menu_str)
                user_input = prompt(self.text_prompt,
                                completer=self.completer)
                if user_input.lower() in self.menu_items:
                    valid_input = True
                    finished = True
                    result = user_input
                if user_input.lower() == "quit":
                    valid_input = True
                    finished = True
                    result = "quit"
                else:
                    print("Incorrect User Input.")
        return result
