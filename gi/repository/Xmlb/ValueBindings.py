# encoding: utf-8
# module gi.repository.Xmlb
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Xmlb-2.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject


class ValueBindings(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ValueBindings()
    """
    def bind_str(self, idx, p_str, destroy_func=None): # real signature unknown; restored from __doc__
        """ bind_str(self, idx:int, str:str, destroy_func:GLib.DestroyNotify=None) """
        pass

    def bind_val(self, idx, val): # real signature unknown; restored from __doc__
        """ bind_val(self, idx:int, val:int) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Xmlb.ValueBindings """
        pass

    def copy_binding(self, idx, dest, dest_idx): # real signature unknown; restored from __doc__
        """ copy_binding(self, idx:int, dest:Xmlb.ValueBindings, dest_idx:int) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def is_bound(self, idx): # real signature unknown; restored from __doc__
        """ is_bound(self, idx:int) -> bool """
        return False

    def lookup_opcode(self, idx): # real signature unknown; restored from __doc__
        """ lookup_opcode(self, idx:int) -> bool, opcode_out:Xmlb.Opcode """
        return False

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    dummy0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ValueBindings), '__module__': 'gi.repository.Xmlb', '__gtype__': <GType XbValueBindings (844625200)>, '__dict__': <attribute '__dict__' of 'ValueBindings' objects>, '__weakref__': <attribute '__weakref__' of 'ValueBindings' objects>, '__doc__': None, 'dummy0': <property object at 0x00000154347154e0>, 'dummy1': <property object at 0x00000154347155d0>, 'dummy2': <property object at 0x00000154347156c0>, 'dummy3': <property object at 0x00000154347157b0>, 'dummy4': <property object at 0x00000154347158a0>, 'dummy5': <property object at 0x0000015434715990>, 'dummy6': <property object at 0x0000015434715a80>, 'dummy7': <property object at 0x0000015434715b70>, 'dummy8': <property object at 0x0000015434715c60>, 'dummy9': <property object at 0x0000015434715d50>, 'dummy10': <property object at 0x0000015434715e40>, 'dummy11': <property object at 0x0000015434715f30>, 'dummy12': <property object at 0x0000015434716020>, 'bind_str': gi.FunctionInfo(bind_str), 'bind_val': gi.FunctionInfo(bind_val), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'copy_binding': gi.FunctionInfo(copy_binding), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init), 'is_bound': gi.FunctionInfo(is_bound), 'lookup_opcode': gi.FunctionInfo(lookup_opcode)})"
    __gtype__ = None # (!) real value is '<GType XbValueBindings (844625200)>'
    __info__ = StructInfo(ValueBindings)


