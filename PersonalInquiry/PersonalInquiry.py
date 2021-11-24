"""
    Village NPC AI Version 0.0.11

    07 May 2020 ; 27 July 2020

    By Jacob Worgan
"""

import Peep.peep
from MainWindow import MainWindow
from MainMenu import MainMenu
import Blackboard

class Handler():
    ''' class that handles the main gameplay loop '''
    def __init__(self):
        # initialise the main menu
        
        self.mainMenu = MainMenu()

        # initialises the game
        self.blackboard = Blackboard.Blackboard()
        self.a = [Peep.peep.Peep(self.blackboard)]
        self.blackboard.initRndPeeps(20)
        self.a = self.blackboard.peeps

        self.main = MainWindow(self.a, self.blackboard)

''' main program '''
if __name__=="__main__":
    # start game
    main = Handler()