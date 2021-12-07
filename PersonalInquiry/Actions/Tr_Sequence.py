from Actions.Tr_Tree import Tr_Tree
class Tr_Sequence(Tr_Tree):
    """description of class"""


    def __init__(s, name="Sequence", children=None):
        s.name=name
        s.nodeNo = 0
        s.isRunning = False

        s.children=[]

        if children is not None:
            for child in children:
                s.AddChild(child)

    def Call(s):
        if s.isRunning:
            print("Continuing")
            a = s.children[s.nodeNo].Call()
            if a == 1 or a == -1 : 
                s.isRunning = False
            return a
        else:
            while s.nodeNo < (len(s.children) - 1):
                a = s.children[s.nodeNo].Call()
                s.nodeNo += 1
                if a == -1:
                    s.isRunning = False
                    return -1
                elif a == 0:
                    s.isRunning == True
                    return 0
                s.isRunning = False
                return 1
            s.nodeNo = 0
            return 1

                
        """
        s.isRunning = False
        while nodeNo < len(s.children):
            for i in range(0, len(self.children) - 1):
                a = s.children[i].Call()
                if a == -1:
                    return -1
                elif a == 0:
                    s.isRunning == True
                    return 0
            return 1"""