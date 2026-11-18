from abc import ABC, abstractmethod
import numpy as np
from foundation.models import Point3D

""" This file defines the basic skeleton for every device
used in the system (printer, cameras, end effector)"""

class BaseDevice(ABC):
    """Every physical device (camera, printer, effector) must follow these rules."""
    
    @abstractmethod
    def connect(self) -> None:
        """Open the connection to the hardware."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Safely close the connection."""
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """Return True if the device is ready to receive commands."""
        pass


class BaseMotionController(BaseDevice):
    """Rules for anything that moves the gantry (Real Printer or Mock Printer)."""

    @abstractmethod
    def home_all(self) -> None:
        """Move X, Y, and Z axes to their limit switches (0, 0, 0)."""
        pass

    @abstractmethod
    def move_to(self, pos: Point3D, feedrate: float) -> None:
        """Move to an exact (X, Y, Z) coordinate in millimeters."""
        pass

    @abstractmethod
    def wait_for_moves(self) -> None:
        """Pause Python until the physical motors have completely stopped moving."""
        pass

    @abstractmethod
    def emergency_stop(self) -> None:
        """Kill all motors immediately."""
        pass


class BaseEffector(BaseDevice):
    """Rules for the picking toolhead (tip ejector, sensors, lights)."""

    @abstractmethod
    def eject_tip(self) -> None:
        pass

    @abstractmethod
    def is_tip_present(self) -> bool:
        pass

    @abstractmethod
    def is_agar_contacted(self) -> bool:
        pass


class BaseCamera(BaseDevice):
    """Rules for any camera (Pi Ribbon Camera or USB Webcam)."""

    @abstractmethod
    def capture_frame(self) -> np.ndarray:
        """Take one picture and return it as an OpenCV image array."""
        pass