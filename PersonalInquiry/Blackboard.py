from WorldObject import WorldObject
import Peep.peep
import Actions.Tree

class Blackboard(object):
    """ The Blackboard that contains all world objects and information
        to be used by each peep and action. 
        
        Also all the peeps currently available to socialise. """


    def __init__(s, peeps=None, time=400, day=83, year=2020, isPlaying=False):
        s.time = time
        s.day = day
        s.year = year
        s.isPlaying = isPlaying

        s.bin = WorldObject(name="Bin", tickEffects=[])

        s.peeps = []

        if peeps is not None:
            for peep in peeps:
                s.addPeep(peep)

    def initRndPeeps(s, peepNo = 1):
        for i in range(0, peepNo - 1):
            p = Peep.peep.Peep(s)
            s.addPeep(p) 


    def addPeep(s, peep):
        #assert isinstance(peep, peep.Peep)
        s.peeps.append(peep)

    def tick(s):
        s.time += 1
        if s.time == 1440:
            s.time=0
            s.day += 1
            if s.day == 84:
                s.day = 0
                s.year += 1
        for peep in s.peeps:
            peep.tick(s.time)