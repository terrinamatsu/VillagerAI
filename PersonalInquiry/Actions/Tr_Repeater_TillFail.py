from Actions.Tr_Decorator import Tr_Decorator
class Tr_Repeater_TillFail(Tr_Decorator):
    """A type of decorator Tree Node that repeats the child interaction until it returns fail."""
   
    def executePath(self):
        check = 0
        while check != -1:
            check = self.child.Call()

        return check