import models.py

""" This file defines all custom errors that may be raised in the
picking process. We send additional debug data for each error to
help with debugging and tracking down issues. """

# https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
# https://www.geeksforgeeks.org/python/define-custom-exceptions-in-python/

# EXAMPLE ON DEFINING, RAISING, HANDLING:
class FileProcessingError(Exception):
    def __init__(self, message, filename, lineno):
        super().__init__(message)
        self.message = message
        self.filename = filename
        self.lineno = lineno

    def __str__(self):
        return f"{self.message} in {self.filename} at line {self.lineno}"

# this goes in another file, when we raise the error
try:
    raise FileProcessingError("Syntax error", "example.txt", 13)
except FileProcessingError as e:
    print(f"Caught an error: {e}")