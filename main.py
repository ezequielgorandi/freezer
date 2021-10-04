from gpiozero import DigitalOutputDevice, Button, LED
import RPi.GPIO as gpio

from door import Door
from log import Log
from menu import Menu
from setup import *
"""Freezer monitoring
Door:
    Allows door management and monitoring.
    Peripherals: Magnetic sensor and lock.
    Periodically check the magnetic sensor to detect if the door has been
    opened or closed.
    Allows the user to lock or unlock the door. Avoid locking the door if it is
    open.
    When unlocking the door, it activates a timer to work after a certain time.

Log:
    Generates reports when opening, closing, locking and unlocking the door
    and when an RFid is read
    
    Creates a log file in a folder named log. t's created at the address 
    from which the program is running. Its name is [YYYY-MM-DD].txt.
    
    zReceives reports of different program events and save them in a
    comma-separated file. New york time is used.

Menu:
    This screen shows the status of the door 
    (closed / open, locked / unlocked) and prints a menu.

    Options:
        1.Unlock door
        2.Lock door
        3.Rfid input
        4.Print log
        5.Print subtracted inventory

    The menu does not refresh automatically, so it will be necessary to press
    enter to see the changes in the door status.
"""


log = Log('America/New_York')
magnetic_sensor = Button(MAGNETIC_SENSOR_PIN, True)
locker = DigitalOutputDevice(LOCKER_PIN, LOCKER_ON, False)
door = Door(magnetic_sensor, locker, log)
menu = Menu(door, log)
while True:
    menu.select()
