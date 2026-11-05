from enum import Enum

""" This file stores all necessary definitions.
Every file can import it, it holds no logic, 
and only defines our data structures/enums. """

# EXAMPLES:
# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# functional syntax
Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

# Define a new enum for status of colonies
# Used to track if a colony has been picked or other
class Status(Enum):
    PICKED = 0
    PENDING = 1
    IN_PROGRESS = 2
    SKIPPED = 3
    FAILED = 4

Status = Enum('Status', [('PICKED', 0), ('PENDING', 1), ('IN_PROGRESS', 2), ('SKIPPED', 3), ('FAILED', 4)])