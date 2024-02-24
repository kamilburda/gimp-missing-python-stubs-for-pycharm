# encoding: utf-8
# module gi.repository.Gimp
# from C:\Program Files\GIMP 2.99\lib\girepository-1.0\Gimp-3.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .object import object

class Unit(object):
    """
    :Constructors:
    
    ::
    
        Unit(**properties)
        new(identifier:str, factor:float, digits:int, symbol:str, abbreviation:str, singular:str, plural:str) -> Gimp.Unit
    """
    def format_string(self, format, unit): # real signature unknown; restored from __doc__
        """ format_string(format:str, unit:Gimp.Unit) -> str """
        return ""

    def get_abbreviation(self): # real signature unknown; restored from __doc__
        """ get_abbreviation(self) -> str """
        return ""

    def get_deletion_flag(self): # real signature unknown; restored from __doc__
        """ get_deletion_flag(self) -> bool """
        return False

    def get_digits(self): # real signature unknown; restored from __doc__
        """ get_digits(self) -> int """
        return 0

    def get_factor(self): # real signature unknown; restored from __doc__
        """ get_factor(self) -> float """
        return 0.0

    def get_identifier(self): # real signature unknown; restored from __doc__
        """ get_identifier(self) -> str """
        return ""

    def get_number_of_built_in_units(self): # real signature unknown; restored from __doc__
        """ get_number_of_built_in_units() -> int """
        return 0

    def get_number_of_units(self): # real signature unknown; restored from __doc__
        """ get_number_of_units() -> int """
        return 0

    def get_plural(self): # real signature unknown; restored from __doc__
        """ get_plural(self) -> str """
        return ""

    def get_scaled_digits(self, resolution): # real signature unknown; restored from __doc__
        """ get_scaled_digits(self, resolution:float) -> int """
        return 0

    def get_singular(self): # real signature unknown; restored from __doc__
        """ get_singular(self) -> str """
        return ""

    def get_symbol(self): # real signature unknown; restored from __doc__
        """ get_symbol(self) -> str """
        return ""

    def is_metric(self): # real signature unknown; restored from __doc__
        """ is_metric(self) -> bool """
        return False

    def new(self, identifier, factor, digits, symbol, abbreviation, singular, plural): # real signature unknown; restored from __doc__
        """ new(identifier:str, factor:float, digits:int, symbol:str, abbreviation:str, singular:str, plural:str) -> Gimp.Unit """
        pass

    def set_deletion_flag(self, deletion_flag): # real signature unknown; restored from __doc__
        """ set_deletion_flag(self, deletion_flag:bool) """
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
        """ Default object formatter. """
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Unit), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpUnit (814717376)>, '__dict__': <attribute '__dict__' of 'Unit' objects>, '__weakref__': <attribute '__weakref__' of 'Unit' objects>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'format_string': gi.FunctionInfo(format_string, bound=None), 'get_number_of_built_in_units': gi.FunctionInfo(get_number_of_built_in_units, bound=None), 'get_number_of_units': gi.FunctionInfo(get_number_of_units, bound=None), 'get_abbreviation': gi.FunctionInfo(get_abbreviation, bound=None), 'get_deletion_flag': gi.FunctionInfo(get_deletion_flag, bound=None), 'get_digits': gi.FunctionInfo(get_digits, bound=None), 'get_factor': gi.FunctionInfo(get_factor, bound=None), 'get_identifier': gi.FunctionInfo(get_identifier, bound=None), 'get_plural': gi.FunctionInfo(get_plural, bound=None), 'get_scaled_digits': gi.FunctionInfo(get_scaled_digits, bound=None), 'get_singular': gi.FunctionInfo(get_singular, bound=None), 'get_symbol': gi.FunctionInfo(get_symbol, bound=None), 'is_metric': gi.FunctionInfo(is_metric, bound=None), 'set_deletion_flag': gi.FunctionInfo(set_deletion_flag, bound=None)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpUnit (814717376)>'
    __info__ = ObjectInfo(Unit)


