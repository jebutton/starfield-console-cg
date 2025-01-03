"""
    A module contain classes for menus.
"""
from abc import abstractmethod
import sys
from os import path as OSPATH
from os import system as OSSYS
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
sys.path.insert(0, OSPATH.abspath(OSPATH.join(OSPATH.dirname(__file__), './')))
from .data_file_reader import DataFileReader as DFR
import settings_io

class AutoCompleteList:
    """
        A class to simplify and standarize how the WordCompleter class
        is used in the project. 
    """

    def __init__(self, input_structure):
        """
        Initialize an AutoCompleteList object.

        :param input_structure: The data structure to be handled for auto completion
        """

        self.input_structure = input_structure

        if isinstance(self.input_structure, dict):
            self.completer = self.generate_wordcompleter_list(self.input_structure)
        elif isinstance(input_structure, list):
            self.completer = WordCompleter(self.duplicate_input(self.input_structure))
        else:
            raise TypeError(f"Invalid datastructure type. Type is {type(input_structure)}")

    def __repr__(self):
        """
        Return a str representation of the AutoCompleteList object.

        :return: A str representation of and AutoCompleteList object.
        """

        return f"AutoCompleteList(input_structure='{self.input_structure}')"

    def generate_wordcompleter_list(self, input_dict: dict):
        """
        Returns a WordCompleter Object for all the keys in the input_dict

        :param input_dict: A dict with the input data for the autocomplete list.
        :return: A WordCompleter object with all the items in the input_dict
        """

        keys_list = input_dict.keys()

        return WordCompleter(self.duplicate_input(keys_list))

    def duplicate_input(self, input_list: list):
        """
        Duplicates the input list.
        """
        result = [item.lower() for item in input_list] + \
            [item.capitalize() for item in input_list]
        return result

class BaseMenu():
    """
    Represents the most basic menu.
    """

    CHUNK_SIZE = 12

    def __init__(self, title: str):
        """
        The constructor.
        :param title: The str title for the menu.
        """

        self.title = title.strip()

    def clear_screen(self):
        """
        Clears the screen.
        """

        OSSYS("cls")

    def gen_horizontal_border(self):
        """
        Generates a horizontal border of dashes.
        
        :return: A str containing a border.
        """
        border = "-" * 80
        border = f"{border}"
        return border

    def print_title(self):
        """
        Prints a structured title
        """

        border = self.gen_horizontal_border()
        structured_title = f"| {self.title}{" " * (76 - len(self.title))} |"
        title_list = [border, structured_title, border]
        print("\n".join(title_list))

    def gen_structured_prompt(self, tgt_prompt: str):
        """
        Modifies a prompt to include a border at the top.
        
        :return: A str prompt containing a border up top.
        """

        new_prompt_list = [self.gen_horizontal_border(), tgt_prompt]
        return "\n".join(new_prompt_list)

    def get_amount(self):
        """
        Prompts and returns the amount chosen.
        """

        prompt_text = "How many items?> "

        return int(prompt(prompt_text))

    @abstractmethod
    def display_menu(self):
        """
            Display the Menu.
        """

class ItemMenu(BaseMenu):
    """
        This is a class to display a list of in-game items as a menu
        and provide a prompt for the user to choose them.
    """

    def __init__(self, input_dict: dict, title: str):
        """
        Initialize an ItemMenu object.

        :param input_dict: The dict of objects to be displayed for the menu.
        :param title: The str message to display when the menu loads.
        """

        super().__init__(title)
        self.input_dict = input_dict
        self.menu_items = self.get_menu_items()
        self.completer = AutoCompleteList(self.menu_items).completer
        self.display_chunks = self.split_menu_items()
        self.amount = 0

    def __repr__(self):
        """
        Return a str representation of the ItemMenu object.

        :return: A str representation of the ItemMenu object.
        """

        return f"ItemMenu(input_dict='{self.input_dict}')"

    def get_menu_items(self):
        """
        Return a list of all the menu items to select from

        :return: A list of all the menu items to select from.
        """

        return [item[1].get_name() for item in self.input_dict.items()]

    def split_menu_items(self):
        """
        Return a list containing all of the menu items split into chunks.

        :return: A list of all the menu items split into str chunks with linebreaks.
        """

        # pylint: disable=too-many-branches
        # pylint: disable=unused-variable

        output_list = []
        items_len = len(self.menu_items)
        if items_len > self.CHUNK_SIZE:

            if items_len % self.CHUNK_SIZE == 0:
                segment_counter = 0
                temp_segment = ""

                for segment in range(int(items_len / self.CHUNK_SIZE)):
                    if segment_counter <= self.CHUNK_SIZE:
                        temp_segment = self.menu_items[segment_counter:
                                                       segment_counter + self.CHUNK_SIZE]
                        segment_counter += self.CHUNK_SIZE
                        output_list.append("\n".join(temp_segment))

                    elif segment_counter <= items_len:
                        temp_segment = self.menu_items[segment_counter:segment_counter
                                                        + self.CHUNK_SIZE]
                        segment_counter += self.CHUNK_SIZE
                        output_list.append("\n".join(temp_segment))

            elif items_len / self.CHUNK_SIZE > 1.0:
                loop_length = int((items_len - items_len % self.CHUNK_SIZE) \
                                   / self.CHUNK_SIZE)
                segment_counter = 0
                temp_segment = ""

                for segment in range(loop_length):
                    if segment_counter <= self.CHUNK_SIZE:
                        temp_segment = self.menu_items[segment_counter:
                                                       segment_counter + self.CHUNK_SIZE]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.CHUNK_SIZE

                    elif items_len - segment_counter >= self.CHUNK_SIZE:
                        temp_segment = self.menu_items[segment_counter:segment_counter
                                                        + self.CHUNK_SIZE]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.CHUNK_SIZE

                temp_segment = self.menu_items[segment_counter: items_len]
                output_list.append("\n".join(temp_segment))

        else:
            temp_segment = self.menu_items[:items_len]
            output_list.append("\n".join(temp_segment))

        return output_list

    def display_menu(self):
        """
        Generate a visual menu list of items to select.
        
        :return: The selected menu item str name or "end" if the user wants to exit.
        """

        # pylint: disable=too-many-branches

        finished = False
        result = (False, 0)
        self.clear_screen()
        while finished is not True:
            for chunk in self.display_chunks:
                if chunk != self.display_chunks[-1]:
                    valid_input = False
                    while valid_input is not True:
                        self.print_title()
                        print(chunk)
                        new_prompt = self.gen_structured_prompt("Type Item name or \
type next to continue> ")
                        user_input = prompt(new_prompt,
                                        completer=self.completer).lower()
                        if user_input in self.input_dict:
                            valid_input = True
                            finished = True
                            amount = self.get_amount()
                            result = (user_input, amount)
                        elif user_input == "next":
                            self.clear_screen()
                            valid_input = True
                        else:
                            self.clear_screen()
                            print("Incorrect User Input.")
                    if finished is True:
                        break
                else:
                    valid_input = False
                    while valid_input is not True:
                        self.print_title()
                        print(chunk)
                        new_prompt = self.gen_structured_prompt("Type Item name, repeat to \
continue, or end to finish> ")
                        user_input = prompt(new_prompt,
                                            completer=self.completer).lower()
                        if user_input in self.input_dict:
                            finished = True
                            valid_input = True
                            amount = self.get_amount()
                            result = (user_input, amount)
                        elif user_input == "end":
                            finished = True
                            valid_input = True
                            result = ("end",0)
                            break
                        elif user_input == "repeat":
                            self.clear_screen()
                            valid_input = True
                        else:
                            self.clear_screen()
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
        
        :param menu_items: The list of menu items to display.
        :param title: The str message to display when the menu loads.
        :param text_prompt: The str text of the prompt at the bottom of the menu.
        """

        super().__init__(title)

        self.menu_items = [item.lower() for item in menu_items]
        self.completer = AutoCompleteList(self.menu_items).completer
        self.text_prompt = text_prompt

    def __repr__(self):
        """
        Return a str representation of the NavMenu object.

        :return: A str representation of a NavMenu object.
        """

        return_str = f"NavMenu(menu_items='{self.menu_items}', completer={self.completer},"
        return_str += f" title='{self.title}', prompt='{self.text_prompt}')"
        return return_str

    def display_menu(self):
        """
        Generate a visual menu list of items to select
        
        :return: The selected menu item name or "quit" if the user quits
        """

        menu_str = "\n".join([item.capitalize() for item in self.menu_items])
        finished = False
        result = ""
        self.clear_screen()
        while finished is not True:
            valid_input = False
            while valid_input is not True:
                self.print_title()
                print(menu_str)
                new_prompt = self.gen_structured_prompt(self.text_prompt)
                user_input = prompt(new_prompt,
                                completer=self.completer)
                if user_input.lower() in self.menu_items:
                    valid_input = True
                    finished = True
                    result = user_input
                elif user_input.lower() == "quit":
                    valid_input = True
                    finished = True
                    result = "quit"
                else:
                    self.clear_screen()
                    print("Incorrect User Input.")

        return result

class StatusModMenu(BaseMenu):
    """
        This is a class to display a list of in-game mods as a menu
        and provide a prompt for the user to choose them.
    """
    def __init__(self, input_dict: dict, title: str):
        """
        Initialize an StatusModMenu object.

        :param input_dict: The dict of objects to be displayed for the menu.
        :param title: The str message to display when the menu loads.
        """

        super().__init__(title)
        self.input_dict = input_dict

        if isinstance(self.input_dict, dict) is not True:
            raise TypeError(f"input_dict is not a dict. input_dict is type {type(input_dict)}")

        self.menu_items = self.get_menu_items()
        self.completers = (AutoCompleteList(
                                [self.trim_menu_selection(item) for \
                                 item in self.menu_items[0]]).completer,
                           AutoCompleteList(
                                [self.trim_menu_selection(item) for \
                                 item in self.menu_items[1]]).completer,
                           AutoCompleteList(
                                [self.trim_menu_selection(item) for \
                                 item in self.menu_items[2]]).completer)
        self.display_chunks = (self.split_menu_items(self.menu_items[0]),
                               self.split_menu_items(self.menu_items[1]),
                               self.split_menu_items(self.menu_items[2]))
        self.amount = 0

    def __repr__(self):
        """
        Return a str representation of the StatusModMenu object.

        :return: A str representation of the StatusModMenu object.
        """

        return f"StatusModMenu(input_dict='{self.input_dict}')"

    def alt_title_print(self, counter: int):
        """
        Prints a structured title with a counter

        :param counter: An int with a counter value.
        """
        border = self.gen_horizontal_border()
        new_title = f"{self.title} {counter}"
        structured_title = f"| {new_title}{" " * (76 - len(new_title))} |"
        title_list = [border, structured_title, border]
        print("\n".join(title_list))

    def get_menu_items(self):
        """
        Return a list of all the menu items to select from

        :return: A list of all the menu items to select from.
        """
        output_list_one = [f"{item.get_name()}: {item.get_description()}" for item in \
                            DFR.get_status_mods_by_mod_slot(1, self.input_dict).values()]
        output_list_two = [f"{item.get_name()}: {item.get_description()}" for item in \
                           DFR.get_status_mods_by_mod_slot(2, self.input_dict).values()]
        output_list_three = [f"{item.get_name()}: {item.get_description()}" for item in \
                             DFR.get_status_mods_by_mod_slot(3, self.input_dict).values()]
        return (output_list_one, output_list_two, output_list_three)

    def split_menu_items(self, tgt_list: list):
        """
        Return a list containing all of the menu items split into chunks.

        :return: A list of all the menu items split into str chunks with linebreaks.
        """

        # pylint: disable=unused-variable
        # pylint: disable=too-many-statements
        # pylint: disable=too-many-branches

        output_list = []
        items_len = len(tgt_list)
        if items_len > self.CHUNK_SIZE:

            if items_len % self.CHUNK_SIZE == 0:
                segment_counter = 0
                temp_segment = ""

                for segment in range(int(items_len / self.CHUNK_SIZE)):
                    if segment_counter <= self.CHUNK_SIZE:
                        temp_segment = tgt_list[segment_counter:
                                                       segment_counter + self.CHUNK_SIZE]
                        segment_counter += self.CHUNK_SIZE
                        output_list.append("\n".join(temp_segment))

                    elif segment_counter <= items_len:
                        temp_segment = tgt_list[segment_counter:segment_counter
                                                        + self.CHUNK_SIZE]
                        segment_counter += self.CHUNK_SIZE
                        output_list.append("\n".join(temp_segment))

            elif items_len / self.CHUNK_SIZE > 1.0:
                loop_length = int((items_len - items_len % self.CHUNK_SIZE)\
                                   / self.CHUNK_SIZE)
                segment_counter = 0
                temp_segment = ""

                for segment in range(loop_length):
                    if segment_counter <= self.CHUNK_SIZE:
                        temp_segment = tgt_list[segment_counter:
                                                       segment_counter + self.CHUNK_SIZE]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.CHUNK_SIZE

                    elif items_len - segment_counter >= self.CHUNK_SIZE:
                        temp_segment = tgt_list[segment_counter:segment_counter
                                                        + self.CHUNK_SIZE]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.CHUNK_SIZE

                temp_segment = tgt_list[segment_counter: items_len]
                output_list.append("\n".join(temp_segment))

        else:
            temp_segment = tgt_list[:items_len]
            output_list.append("\n".join(temp_segment))

        return output_list

    def trim_menu_selection(self, selection: str):
        """
        Removes the description from the menu option.

        :param selection: A str reprensenting a menu selection

        :return: A str of just the menu option
        """
        output_str = ""
        for char in selection:
            if char != ":":
                output_str += char
            else:
                break

        return output_str

    def display_menu(self):
        """
        Generate a visual menu list of mods to select.
        
        :return: The selected mod str names in a tuple or "end" if the user wants to exit.
        """

        # pylint: disable=unused-variable
        # pylint: disable=too-many-statements
        # pylint: disable=too-many-branches
        # pylint: disable=too-many-nested-blocks

        finished = False
        result_list = ["", "", ""]
        counter = 0
        while finished is not True:
            if counter < 3:
                for chunk in self.display_chunks[counter]:
                    self.clear_screen()
                    if chunk != self.display_chunks[counter][-1]:
                        valid_input = False
                        while valid_input is not True:
                            self.alt_title_print(counter + 1)
                            print(chunk)
                            new_prompt = self.gen_structured_prompt("Type Mod name or type \
next to continue> ")
                            user_input = prompt(new_prompt,
                                            completer=self.completers[counter]).lower()
                            if self.trim_menu_selection(user_input) in self.input_dict:
                                valid_input = True
                                result = user_input
                                result_list[counter] = result
                                counter += 1
                                break
                            if user_input == "next":
                                valid_input = True
                            else:
                                self.clear_screen()
                                print("Incorrect User Input.")
                    else:
                        valid_input = False
                        while valid_input is not True:
                            self.alt_title_print(counter + 1)
                            print(chunk)
                            prompt_str = ""
                            if counter < 2:
                                prompt_str = f"Type Mod name for slot {counter + 1}\
,\n skip to move onto the next slot,\n or end to finish> "
                            else:
                                prompt_str = f"Type Mod name for slot {counter + 1}\
,\n repeat to continue,\n or end to finish> "
                            prompt_str = self.gen_structured_prompt(prompt_str)
                            user_input = prompt(prompt_str,
                                                completer=self.completers[counter]).lower()
                            if user_input in self.input_dict:
                                valid_input = True
                                result = user_input
                                result_list[counter] = result
                                counter += 1
                            elif user_input == "skip" and counter < 2:
                                valid_input = True
                                result = "skip"
                                result_list[counter] = result
                                counter += 1
                            elif user_input == "end":
                                valid_input = True
                                result = "end"
                                result_list[counter] = result
                                counter = 3
                                break
                            elif user_input == "repeat":
                                counter = 0
                                self.clear_screen()
                                valid_input = True
                            else:
                                self.clear_screen()
                                print("Incorrect User Input.")
            else:
                finished = True

        return result_list

class QualityMenu(BaseMenu):
    """
    A menu to handle quality mods.
    """

    def __init__(self, input_dict: dict, title: str, text_prompt: str):
        """
        Initialize an QualityMenu object.

        :param input_dict: The dict of objects to be displayed for the menu.
        :param title: The str message to display when the menu loads.
        :param text_prompt: The str message to display as a prompt.
        """

        super().__init__(title)
        self.input_dict = input_dict
        self.text_prompt = text_prompt

        self.menu_items = self.get_menu_items()
        self.completer = AutoCompleteList(self.menu_items).completer

    def get_menu_items(self):
        """
        Return a list of all the menu items to select from

        :return: A list of all the menu items to select from.
        """

        return [item[1].get_name() for item in self.input_dict.items()]

    def display_menu(self):
        """
        Generate a visual menu list of items to select
        
        :return: The selected menu item name or "quit" if the user quits
        """

        menu_str = "\n".join(self.menu_items)
        finished = False
        result = ""
        self.clear_screen()
        while finished is not True:
            valid_input = False
            while valid_input is not True:
                self.print_title()
                print(menu_str)
                new_prompt = self.gen_structured_prompt(self.text_prompt)
                user_input = prompt(new_prompt,
                                completer=self.completer).lower()
                if user_input in self.input_dict:
                    valid_input = True
                    finished = True
                    result = user_input
                elif user_input.lower() == "quit":
                    valid_input = True
                    finished = True
                    result = "quit"
                else:
                    self.clear_screen()
                    print("Incorrect User Input.")

        return result

class SettingsMenu(BaseMenu):
    """
    A menu to handle settings.
    """

    def __init__(self, title: str):
        """
            A class to create a menu to handle setting all settings.
            :param title: The str title for the menu.
        """

        super().__init__(title)
        self.input_dict = {}
        self.input_dict["dlc_load_order"] = settings_io.global_settings.settings["dlc_load_order"]
        self.menu_items = self.get_menu_items()
        self.completer = AutoCompleteList(self.menu_items).completer
        self.display_chunks = self.split_menu_items()

    def get_menu_items(self):
        """
        Return a list of all the menu items to select from

        :return: A list of all the menu items to select from.
        """

        return list(self.input_dict.keys())

    def split_menu_items(self):
        """
        Return a list containing all of the menu items split into chunks.

        :return: A list of all the menu items split into str chunks with linebreaks.
        """

        # pylint: disable=too-many-branches
        # pylint: disable=unused-variable

        output_list = []
        items_len = len(self.menu_items)
        if items_len > self.CHUNK_SIZE:

            if items_len % self.CHUNK_SIZE == 0:
                segment_counter = 0
                temp_segment = ""

                for segment in range(int(items_len / self.CHUNK_SIZE)):
                    if segment_counter <= self.CHUNK_SIZE:
                        temp_segment = self.menu_items[segment_counter:
                                                       segment_counter + self.CHUNK_SIZE]
                        segment_counter += self.CHUNK_SIZE
                        output_list.append("\n".join(temp_segment))

                    elif segment_counter <= items_len:
                        temp_segment = self.menu_items[segment_counter:segment_counter
                                                        + self.CHUNK_SIZE]
                        segment_counter += self.CHUNK_SIZE
                        output_list.append("\n".join(temp_segment))

            elif items_len / ItemMenu.CHUNK_SIZE > 1.0:
                loop_length = int((items_len - items_len % self.CHUNK_SIZE) \
                                   / self.CHUNK_SIZE)
                segment_counter = 0
                temp_segment = ""

                for segment in range(loop_length):
                    if segment_counter <= self.CHUNK_SIZE:
                        temp_segment = self.menu_items[segment_counter:
                                                       segment_counter + self.CHUNK_SIZE]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.CHUNK_SIZE

                    elif items_len - segment_counter >= self.CHUNK_SIZE:
                        temp_segment = self.menu_items[segment_counter:segment_counter
                                                        + self.CHUNK_SIZE]
                        output_list.append("\n".join(temp_segment))
                        segment_counter += self.CHUNK_SIZE

                temp_segment = self.menu_items[segment_counter: items_len]
                output_list.append("\n".join(temp_segment))

        else:
            temp_segment = self.menu_items[:items_len]
            output_list.append("\n".join(temp_segment))

        return output_list

    def __repr__(self):
        """
        Return a str representation of the SettingsMenu object.

        :return: A str representation of a SettingsMenu object.
        """

        return_str = f"SettingsMenu(menu_items='{self.menu_items}', completer={self.completer},\
title='{self.title}')"

        return return_str

    def display_menu(self):
        """
        Generate a visual menu list of settings to select.
        
        :return: A tuple of (True, True) if the result is successful.
        """

        # pylint: disable=too-many-branches
        # pylint: disable=too-many-nested-blocks

        finished = False
        result = ()
        self.clear_screen()
        while finished is not True:
            for chunk in self.display_chunks:
                if chunk != self.display_chunks[-1]:
                    valid_input = False
                    while valid_input is not True:
                        self.print_title()
                        print(chunk)
                        new_prompt = self.gen_structured_prompt("Type Setting name \
or type next to continue> ")
                        user_input = prompt(new_prompt,
                                        completer=self.completer).lower()
                        if user_input in self.input_dict:
                            new_prompt = self.gen_structured_prompt("Type the new value \
for the setting or end to exit> ")
                            result = self.process_settings_result((user_input, \
                                                                   prompt(new_prompt)))
                            finished = result[0]
                            valid_input = result[1]
                        else:
                            result = self.process_settings_result((user_input, ""))
                            finished = result[0]
                            valid_input = result[1]
                    if finished is True:
                        break
                else:
                    valid_input = False
                    while valid_input is not True:
                        self.print_title()
                        print(chunk)
                        new_prompt = self.gen_structured_prompt("Type Setting name,\
repeat to continue, or end to finish> ")
                        user_input = prompt(new_prompt,
                                            completer=self.completer).lower()
                        if user_input in self.input_dict:
                            new_prompt = self.gen_structured_prompt("Type the new \
value for the setting or end to exit> ")
                            result = self.process_settings_result((user_input, \
                                                                   prompt(new_prompt)))
                            finished = result[0]
                            valid_input = result[1]
                        else:
                            result = self.process_settings_result((user_input, ""))
                            finished = result[0]
                            valid_input = result[1]
                    if finished is True:
                        break
        return result

    def process_settings_result(self, selection: tuple):
        """
        Handles the logic for settings validation and processing.

        :param result: A tuple of the result from the menu.
        :return: A tuple with two bools with the first value being \
True if "finished" should be true and the second value being True \
if the input is valid.
        """

        if selection[0] == "end" or selection[1] == "end":
            result = (True, True)
        elif selection[0] == "repeat":
            result = (False, True)
        elif selection[0] == "dlc_load_order":
            try:
                settings_io.global_settings.set_dlc_load_order(selection[1])
                result = (True, True)
            except ValueError:
                result = (False, False)
                self.clear_screen()
                print("DLC Load order must be only two characters \
long and valid hex.")
        else:
            self.clear_screen()
            print("Incorrect User Input.")
            result = (False, False)
        return result
