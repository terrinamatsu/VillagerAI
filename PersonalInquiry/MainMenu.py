#  IMPORTS
from tkinter import *


#  CLASS
class MainMenu(object):
    """ This is the Main Menu window that handles loading and selecting new games,
        as well as quiting and other game options. """


    def __init__(self):
        # Window Setup
        self.root = Tk()
        self.root.title('NPC AI')
        self.root.geometry("1400x1000")



        self.root.mainloop()