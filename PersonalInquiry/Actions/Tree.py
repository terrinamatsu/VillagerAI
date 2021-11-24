from Actions.action import action

class Tree(object):
    """Simple tree class, no child limit"""
   

    def __init__(self, name="node", data=None, children=None, value=0, min=60000):
        self.name=name
        self.value=value
        self.min = min

        if data is not None:
            self.data = data
        

        self.children=[]

        if children is not None:
            for child in children:
                self.AddChild(child)

    def __repr__(self):
        return self.name

    def AddChild(self, child):
        assert isinstance(child, Tree)
        self.children.append(child)

    def getFirstLeaf(self, branch=0):
        if self.children is not None:
            if len(self.children) > 0:
                return self.children[branch].getFirstLeaf()
        return self

    def executePath(self):
        #Return -1 fail, 0 in progress, 1 succeed
        if self.children is not None:
            if len(self.children) > 0:
                self.children[0].getFirstLeaf()

    def SortChildren(self):
        if self.children is not None:
            last = len(self.children)  - 1 
            # SORT HERE, usually in order so going to use bubble sort over, say, quicksort, sorrynotsorry
            for j in range(0, last):
                for i in range(last, j, -1):
                    if self.children[i].data.value > self.children[i - 1].data.value:
                        self.children[i],self.children[i-1] = self.children[i-1],self.children[i]
            

            for child in self.children:
                child.SortChildren()

    def ToString(self):
        tempStr = '(' + self.name
        
        for child in self.children:
            tempStr += child.ToString() + ','

        tempStr += ')'

        return tempStr