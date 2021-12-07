from Actions.Tr_Tree import Tr_Tree
class Tr_Selector(Tr_Tree):
    """A tree node class that executes each child node 
       in sequence, stopping if any return false."""


    def __init__(s, selector, name="Selector", children=None):
        s.selector = selector
        s.name=name
        s.isRunning = False

        s.children=[]

        if children is not None:
            for child in children:
                s.AddChild(child)

    def Call(s):
        print(s.name)
        if s.isRunning:
            print("Continuing")
            a = s.children[s.tempVal].Call()
        else:
            if s.children is not None:
                if len(s.children) > 0:
                    s.tempVal = s.selector()

                    # Band selector's value to the range of children nodes
                    if s.tempVal >= len(s.children):
                        s.tempVal = len(s.children - 1)
                    elif s.tempVal < 0:
                        s.tempVal = 0

                    # Call the child node
                    a = s.children[s.tempVal].Call()
        
        # Check value of child
        if a == -1:
            s.isRunning = False
            return -1
        elif a == 0:
            s.isRunning == True
            return 0
        s.isRunning = False
        return 1
                