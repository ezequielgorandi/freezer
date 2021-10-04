# Freezer

## Platform

This is a **Python 3** software for **Raspberry Pi3B**

## Description

### Door:

    Allows door management and monitoring.
        
    Peripherals: Magnetic sensor and lock.

    Periodically check the magnetic sensor to detect if the door has been opened or closed.
        
    Allows the user to lock or unlock the door. Avoid locking the door if it is open.
        
    When unlocking the door, it activates a timer to work after a certain time.

### Log:
    Generates reports when opening, closing, locking, and unlocking the door and when an RFID is read
    
    Creates a log file in a folder named log. It's created at the address from which the program is running. The file name is [YYYY-MM-DD].txt.
    
    Receives reports of different program events and saves them in a comma-separated file. New York time is used.

### Menu:
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

## Installation

It is best to update Linux first.

`sudo apt-get update`
`sudo apt-get dist-upgrade`

Install this package:

`pip3 install pytz`
`pip3 install RPi.GPIO`
`pip3 install gpiozero`


## Hardware
The pins used for the peripherals can be configured in setup.py.
By default, this configuration is used

- Magnetic sensor: Pin11 as input.
- Solenoid Lock DC 12V: Pin12 as output.

**Warning** A relay module is required to managing the solenoid.


## Author ✒️

* **Ezequiel Gorandi** 