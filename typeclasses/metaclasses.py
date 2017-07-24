# -----------------------------------------------------------------
"""Metaclass defining module.

Implements singleton behavior.
"""
# -----------------------------------------------------------------

class Singleton(type):
    # -----------------------------------------------------------------
    """Singleton metaclass object.
    
    This object implements singleton behavior by taking a normal
    constructor and returning the singleton instance, if it already
    exists.
    """
    # -----------------------------------------------------------------
    
    def __init__(cls, name, bases, dic):
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None
    
    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance
