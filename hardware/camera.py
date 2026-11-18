import time
import threading
import serial
from foundation.models import Point3D
from foundation.errors import HardwareConnectionError, EmergencyStopError
from hardware.base import BaseMotionController