"""
    A module contain classes for menus.
"""
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

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
        if type(input_structure) is dict:
            self.completer = self.generate_wordcompleter_list(input_structure)
        elif type(input_structure) is list:
            self.completer = WordCompleter(input_structure)
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


class ItemMenu():
    """
        This is a class to display a list of in-game items as a menu
        and provide a prompt for the user to choose them.
    """
    def __init__(self, input_dict: dict, msg: str):
        """
        Initialize an ItemMenu object.

        :param input_dict the dictionary of objects to be displayed for the menu
        :param msg the message to display when the menu loads
        """
        self.input_dict = input_dict
        self.msg = msg
        self.chunk_size = 8
        self.menu_items = self.get_menu_items()
        self.completer = AutoCompleteList(self.menu_items).completer
        self.display_chunks = self.split_menu_items()
        self.completer = AutoCompleteList(self.input_dict).completer
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

                for segment in range(items_len / 8):

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
        while finished is not True:
            print(self.msg)
            for chunk in self.display_chunks:

                if chunk != self.display_chunks[-1]:
                    valid_input = False
                    while valid_input is not True:
                        print(chunk)
                        user_input = prompt("Type Item name or type next to continue>",
                                        completer=self.completer).lower()
                        if user_input in self.input_dict:
                            valid_input = True
                            finished = True
                            return user_input
                        if user_input == "next":
                            valid_input = True
                        else:
                            print("Incorrect User Input.")

                else:
                    valid_input = False

                    while valid_input is not True:
                        print(chunk)
                        user_input = prompt("Type Item name, repeat to continue, or end to finish>",
                                            completer=self.completer).lower()
                        if user_input in self.input_dict:
                            finished = True
                            valid_input = True
                            return user_input
                        if user_input == "end":
                            finished = True
                            valid_input = True
                            return "end"
                        if user_input == "repeat":
                            valid_input = True
                        else:
                            print("Incorrect User Input.")


class NavMenu():
    """
        This is a class to display a list of navigation options as a menu
        and provide a prompt for the user to choose them.
    """
    def __init__(self, menu_items: list, msg: str):
        """
        Initialize an NavMenu object.
        """
        self.menu_items = [item.lower() for item in menu_items]
        self.completer = AutoCompleteList(self.menu_items).completer
        self.msg = msg

    def __repr__(self):
        """
        Return a string representation of the NavMenu object.
        """
        return "ItemMenu(menu_options='{}')".format(self.menu_items)

    def display_menu(self):
        """
        Generate a visual menu list of items to select
        
        :return: The selected menu item name or "quit" if the user quits
        """
        menu_str = "\n".join([item.capitalize() for item in self.menu_items])
        finished = False

        while finished is not True:
            valid_input = False
            print(self.msg)

            while valid_input is not True:

                print(menu_str)
                user_input = prompt("Type a Menu Option to type 'quit' to exit>",
                                completer=self.completer)
                if user_input.lower() in self.menu_items:
                    valid_input = True
                    finished = True
                    return user_input
                if user_input.lower() == "quit":
                    valid_input = True
                    return "quit"
                else:
                    print("Incorrect User Input.")