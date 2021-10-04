from os import system


class Menu ():
    """This screen shows the status of the door
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
    def __init__(self, door, log):
        self.door = door
        self.log = log
        system("clear")

    def option(self, opt):
        print("")
        if opt == "":
            return
        elif opt == "1":
            self.door.set_unlock()
        elif opt == "2":
            self.door.set_lock()
        elif opt == "3":
            tag = input("Insert tag to read: ")
            self.log.tag_read(tag)
        elif opt == "4":
            self.log.read()
        elif opt == "5":
            self.log.read_substracted()
        else:
            print("Invalid Option")
        input("Press enter...")

    def select(self):
        system("clear")
        print("Press enter to refresh")
        print("Door:", "OPEN!" if self.door.open else "Close",
              "and", "Locked" if self.door.lock else "Unlocked")

        choice = input(
            "\n1.Unlock door\n2.Lock door\n3.Rfid input\n4.Print log"
            + "\n5.Print subtracted inventory\nEnter your Choice: ")
        self.option(choice)
