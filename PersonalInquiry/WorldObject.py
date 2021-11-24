class WorldObject(object):
    """These are the objects that exist in the world that are needed for certain actions to take place."""

    def __init__(s, name="", tickEffects=[]):
        s.inUse = False
        
        if tickEffects is not None:
            for effect in tickEffects:
                assert isinstance(effect, tuple)
                s.tickEffects.append(effect)


    def tick(s, objList):
        return