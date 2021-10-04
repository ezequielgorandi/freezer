HIGH = True
LOW = False

"""Hardware Configuration"""
MAGNETIC_SENSOR_PIN = 'BOARD11'  # Set a generic I/O pin
LOCKER_PIN = 'BOARD12'  # Set a generic I/O pin
LOCKER_ON = HIGH  # Can be HIGH or LOW


#  After unlocking, the door will lock automatically after this time. 
#  If the door is open, nothing will happen.
AUTO_LOCK_DOOR_TIME = 60 # [s]
