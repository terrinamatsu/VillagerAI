"""
    Village NPC AI Version 1.0.1

    07 May 2020 ; 27 July 2020

    By Jacob Worgan
"""

import Peep.peep
from MainWindow import MainWindow
import Blackboard


''' main program '''
if __name__=="__main__":
    # start game
    blackboard = Blackboard.Blackboard()
    a = [Peep.peep.Peep(blackboard)]
    blackboard.initRndPeeps(2)

    main = MainWindow(blackboard)