class Levels(object):
    """description of class"""

    def __init__(self, name, value, xp=0, lvl=0, progressType=0, maxlvl=100):
        self.name = name
        self.value = value
        self.xp = xp
        self.lvl = lvl
        self.progressType = progressType
        self.maxlvl = maxlvl
        self.xpDefNext()

    def xpUp(self, xp):
        self.xp += xp
        if((self.xpNext) < xp and (self.lvl < self.maxlvl)):
            self.lvl += 1
            self.xpDefNext()

    def xpDefNext(self):
        if(self.progressType == 0):
            self.xpNext = self.lvl * self.lvl * self.lvl
        elif(self.progressType == 1):
            self.xpNext = self.lvl

    def toString(self):
        return str(self.name) + ' ' + str(self.lvl) + ' ' + str(self.xp) + '/' + str(self.xpNext)