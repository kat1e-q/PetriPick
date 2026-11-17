""" This file defines all custom errors that may be raised in the
picking process. We send additional debug data for each error to
help with debugging and tracking down issues. """

# https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
# https://www.geeksforgeeks.org/python/define-custom-exceptions-in-python/

# Error picking up a pipette tip
class tipNotPickedError(Exception):
    def __init__(self, message, tip_id):
        super().__init__(message)
        self.message = message
        self.tip_id = tip_id

    def __str__(self):
        return f"{self.message} for tip {self.tip_id}"

# Tip dropped error
class tipDroppedError(Exception):
    def __init__(self, tip_id):
        super().__init__(f"Tip {tip_id} has been dropped!")
        self.tip_id = tip_id

    def __str__(self):
        return f"Tip {self.tip_id} has been dropped!"

# No touch on colony error
class noTouchOnColonyError(Exception):
    def __init__(self, colony:Colony):
        super().__init__(f"No touch detected on colony {colony.id}!")
        self.colony_id = colony.id
        colony.status = Status.FAILED

    def __str__(self):
        return f"No touch detected on colony {self.colony_id}"

# Communication error
class communicationError(Exception):
    def __init__(self, device, message="Communication error"):
        super().__init__(message)
        self.message = message
        self.device = device

    def __str__(self):
        return f"{self.message} with device {self.device}"

# E-Stop error
class eStop(Exception):
    def __init__(self, device, message="E-Stop pressed"):
        super().__init__(message)
        self.message = message
        self.device = device

    def __str__(self):
        return f"{self.message}. Device: {self.device}"

# Job cancelled error
class jobCancelled(Exception):
    def __init__(self, device, message="Job cancelled"):
        super().__init__(message)
        self.message = message
        self.device = device

    def __str__(self):
        return f"{self.message}. Device: {self.device}"