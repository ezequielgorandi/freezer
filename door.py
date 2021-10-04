import time
from threading import Thread, Timer
from setup import *


class Door ():
    """Allows door management.
    Peripherals: Magnetic sensor and lock.
    Periodically check the magnetic sensor to detect if the door has been
    opened or closed.
    Allow to lock or unlock the door. Avoid locking the door if it is
    open.
    When unlocking the door, it activates a timer to work after a certain time.
    Generate reports when opening, closing, locking and unlocking the door.
    """

    def __init__(self, magnetic_sensor, locker, log):
        self.log = log
        self.unlock_timeout = AUTO_LOCK_DOOR_TIME
        # I/O variables
        self.magnetic_sensor = magnetic_sensor
        self.locker = locker
        # Status variable   s
        self._open = False
        self._lock = False
        # Magnetic sensor thread
        self.DOOR_TIME = 0.25  # Checks magnetic sensor every 2 seconds
        self.t_door_sensor = Thread(target=self.read_sensor, name='magnetic_s')
        self.t_door_sensor.start()
        # Timer to automatically lock the door
        self.lock_timer = Timer(self.unlock_timeout, self.set_lock)
# Actions

    def set_lock(self):
        if self._lock is False:
            self.locker.on()
            self._lock = True
            self.log.door_locked()
        if self.open is True:
            print('ERROR: Door is open')

    def set_unlock(self):
        if self._lock is True:
            self.locker.off()
            self._lock = False
            self.log.door_unlocked()
        # When the function is called again, the previous thread is deleted
        # and a new one is created.
        self.lock_timer.cancel()
        self.lock_timer = Timer(self.unlock_timeout, self.set_lock)
        self.lock_timer.start()

# Events
    def open_evt(self):
        self._open = True
        self.log.door_open()

    def close_evt(self):
        self.log.door_close()
        self._open = False

# Check status
    def read_sensor(self):
        """Use a thread to read the magnetic sensor every DOOR_TIME seconds 
        """
        while (True):
            if self.open is False and not self.magnetic_sensor.is_pressed:
                self.open_evt()
            elif self.open is True and self.magnetic_sensor.is_pressed:
                self.close_evt()
            time.sleep(self.DOOR_TIME)

    @property
    def open(self):
        return self._open

    @property
    def lock(self):
        return self._lock
