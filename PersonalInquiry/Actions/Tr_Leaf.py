from Actions.Tr_Tree import Tr_Tree
from peepBoard import peepBoard

class Tr_Leaf(Tr_Tree):
    """description of class"""
    def __init__(s, pBoard, action, name="Leaf", data=None, ticks=0):
        s.pBoard = pBoard
        s.action = action
        s.name=name
        s.isRunning = 1
        s.ticks = ticks
        s.currentTicks = s.ticks


        if data is not None:
            s.data = data


    def Call(s):
        

        # Check if leaf is continuing, setup tick if not.
        if abs(s.isRunning) == 1:
            s.isRunning = 0
            s.currentTicks = s.ticks

        # Decrement Ticks
        s.currentTicks-=1
        
        print(s.name + str(s.currentTicks))

        # Tick
        if s.currentTicks >= 0:
            s.pBoard.currentLeaf = s
            s.isRunning = 0
            s.action()
            #print(s.name)
        elif s.currentTicks == -1:
            s.isRunning = 1

        # Return
        return s.isRunning