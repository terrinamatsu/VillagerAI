import Peep.peep
class Tr_Tree(object):
    """description of class"""

    def __init__(s, peep, name="Node"):
        s.name = name
        s.peep = peep
        s.isRunning = False

    def AddChild(self, child):
        assert isinstance(child, Tr_Tree)
        self.children.append(child)

    def Call(s):
        print(s.name)
        """ Finds the next node
            Returns:    -1 if failure
                        0 if running
                        1 if success """
        s.isRunning = False
        return -1
