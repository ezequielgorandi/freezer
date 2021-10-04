from datetime import datetime
import pytz
import os
import errno


class Log ():
    """Creates a log file in a folder named log.
    It's created at the address from which the program is running.
    Its name is [YYYY-MM-DD] .txt.
    It Receives reports of different program events and save them in a
    comma-separated file
    """

    def __init__(self, zone):
        self.time = pytz.timezone(zone)
        try:
            os.mkdir('log')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        file = self.open_file("a")
        file.close()
        self.DOOR_OPEN_EVT = "do"
        self.DOOR_CLOSE_EVT = "dc"
        self.DOOR_LOCKED_EVT = "dl"
        self.DOOR_UNLOCKED_EVT = "du"
        self.TAG_READ_EVT = "tr"

    def open_file(self, access):
        try:
            file = open(
                "log/"+datetime.now(self.time).strftime('%Y-%m-%d')+".txt", access)
        except IOError:
            print("ERROR: Unable to create file")
        return file

    def save_data(self, text):
        file = self.open_file("a")
        file.write(datetime.now(self.time).strftime('%H:%M:%S')+","+text+"\n")
        file.close()

    def read(self):
        print("Log:")
        print("-----------------------")
        file = self.open_file("r")
        mensaje = file.read()
        print(mensaje)
        file.close()

    def read_substracted(self):
        file = self.open_file("r")
        print("Items taken from stock:")
        print("-----------------------")
        for line in file:
            line = line.split(',')
            if line[1] == self.TAG_READ_EVT:
                line.pop(1)
                print(','.join(line).rstrip('\n'))
        file.close()
        print("")
# Events

    def door_open(self):
        self.save_data(self.DOOR_OPEN_EVT)

    def door_close(self):
        self.save_data(self.DOOR_CLOSE_EVT)

    def door_locked(self):
        self.save_data(self.DOOR_LOCKED_EVT)

    def door_unlocked(self):
        self.save_data(self.DOOR_UNLOCKED_EVT)

    def tag_read(self, tag):
        self.save_data(self.TAG_READ_EVT+","+tag)
