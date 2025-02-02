# starfield-console-cg
A Python-based tool to generate console commands for items, resources, and modifiers for The ZeniMax Media video game Starfield.

Initially created as an exercise to practice handling Microsoft Excel Files but has grown more complex over development.

_All game data and item names copyright ZeniMax Media.

Built using python 3.12.8

**Version 0.1.0**

## To Run:

1. Run _run.ps1_ in PowerShell to start the program and install the prerequisites if they don't exist.
2. Navigate the menus by typing options from them.
3. Copy the resulting console commands and paste them into Starfield's console via the tilde (`) key.

## Updates:

- Version 0.0.11: 
    - Support for Ammo, Spacesuits, and Boost Packs.

- Version 0.0.12: 
    - Support for Helmets introduced.
    - Additional test coverage has been added.

- Version 0.0.13: 
    - Support for Spacesuit Sets has been added.
    - Additional test coverage has been created.

- Version 0.0.14:
    - Extensive Code Cleanup via linting was done.
    - Additional test coverage has been created.
    - Extensive work was done for moving to a proper release package.

- Version 0.0.15: 
    - Weapon support added.

- Version 0.0.16:
    - Resources support added.
    - Fixed a bug in the ItemMenu class so that menus now chunk correctly.
    - Additional tests were created to address and help prevent future menu chunking bugs.

- Version 0.0.17:
    - Weapon Status Mods support added.
    - Additional test coverage created.
    - _README.md_ was structured better and new information was added to it.

- Version 0.0.18:
    - Armor Status Mods support added.
    - Armor Quality Mods support added.
    - Weapon Quality Mods support added.
    - Fixed menu bugs and removed underscores from main menu.

- Version 0.1.0:
    - Added support for settings saved as JSON.
    - Added DLC support for Weapons, Helmets, Spacesuits, and Packs.
    - Updated the main menu with a new "settings" option.
    - More tests added, and more bug fixes.
    - Menus now have better text separation.
    - Extensively changed how the program is run so that it is easier for people to use it.
    - Restructured the way that console commands are printed the user so that they're standardized.

