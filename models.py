from enum import Enum
from constants import *

""" This file stores all necessary definitions.
Every file can import it, it holds no logic, 
and only defines our data structures/enums. """

# Define a new enum for status of colonies
# Used to track if a colony has been picked or other
class Status(Enum):
    PICKED = 0
    PENDING = 1
    IN_PROGRESS = 2
    SKIPPED = 3
    FAILED = 4

# Define a DishDefinition Enum, to differentiate between source and target dishes
class DishDefinition(Enum):
    SOURCE = 0
    TARGET = 1

# Define a DishType Enum, to differentiate between types of dishes
class DishType(Enum):
    PETRI = 0
    NINETY_SIX_WELL = 1

# Defines a Point class, to define (x,y) on the bed
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Defines a Colony class, represents a single colony in a dish
class Colony:
    def __init__(self, id, position:Point, status=Status.PENDING):
        self.id = id
        self.status = status
        self.dish = None
        self.position = position
        self.x = position.x
        self.y = position.y

    def __str__(self):
        return f"Colony {self.id} is {self.status.name}"

    def checkPicked(self):
        if self.status == Status.PICKED:
            return True
        else:
            return False

# Define a Dish class
class Dish:
    def __init__(self, id, dish_def:DishDefinition, dish_type:DishType):
        self.id = id
        self.type = dish_def
        self.dish_type = dish_type
        self.colonies = []

    def __str__(self):
            return f"Dish {self.id} has {len(self.colonies)} colonies"

    def add_colony(self, colony):
        self.colonies.append(colony)
        colony.dish = self

# Define a TipRack class, represents a pipette tip rack
class TipRack:
    def __init__(self, rows=TIP_RACK_ROWS, columns=TIP_RACK_COLUMNS):
        self.rows = rows
        self.columns = columns
        self.tips = []

    def __str__(self):
        return f"TipRack {self.id} has {len(self.tips)} tips"

# Define a Tip class, represents a single pipette tip
class Tip:
    def __init__(self, id, position:Point, used=False):
        self.id = id
        self.position = position
        self.x = position.x
        self.y = position.y
        self.used = used

    def __str__(self):
        return f"Tip {self.id} at {self.position} is {'contaminated' if self.used else 'clean'}"

# Define a Printer class, represents the 3D printer
class Printer:
    def __init__(self, port=None):
        self.com_port = port

# Define a camera class, the camera for the vision system
class Camera:
    def __init__(self, port=None):
        self.com_port = port