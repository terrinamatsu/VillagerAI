from Actions.Tr_Tree import Tr_Tree
class Tr_Decorator(Tr_Tree):
    """description of class"""
    
    def __init__(s, child:Tr_Tree, name="Decorator"):
        self.name=name
               
        self.children=child


    def Call(s):
        print(s.name)
        return -1