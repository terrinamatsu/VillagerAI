class action(object):
    """Defines each action that a peep can make on the action tree.
       Contains each thing it effects (eg. skills helps, needs it fills/depletes etc.)"""


    def __init__(s, 
                 name="", 
                 value=0, 
                 min=6500, 
                 interrupt = False,
                 needsFS=[0,0,0,0,0,0,0,0,0], 
                 secs=0, 
                 tickEffects=None, 
                 initEffects=None, 
                 afterEffects=None,
                 objectNeeded=None):
        #also: ticks to complete, can interupt,
        s.name = name
        s.value = value
        s.interrupt = interrupt
        s.min = min
        s.needsFulfill_Sec = needsFS
        s.secs = secs

        s.tickEffects=[]

        if tickEffects is not None:
            for effect in tickEffects:
                assert isinstance(effect, tuple)
                s.tickEffects.append(effect)

        
        s.initEffects=[]

        if initEffects is not None:
            for effect in initEffects:
                assert isinstance(effect, tuple)
                s.initEffects.append(effect)



        s.afterEffects=[]

        if afterEffects is not None:
            for effect in afterEffects:
                assert isinstance(effect, tuple)
                s.afterEffects.append(effect)

    def aboveMin(s):
        if s.value >= s.min:
            return True
        return False

    def valueUp(s, xp):
        s.value += xp
        if s.value < 0:
            s.value = 0
            return -1
        return 1