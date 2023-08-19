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


class CMYK(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        CMYK()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_uchar(self): # real signature unknown; restored from __doc__
        """ get_uchar(self) -> cyan:int, magenta:int, yellow:int, black:int """
        pass

    def set(self, cyan, magenta, yellow, black): # real signature unknown; restored from __doc__
        """ set(self, cyan:float, magenta:float, yellow:float, black:float) """
        pass

    def set_uchar(self, cyan, magenta, yellow, black): # real signature unknown; restored from __doc__
        """ set_uchar(self, cyan:int, magenta:int, yellow:int, black:int) """
        pass

    def to_rgb(self): # real signature unknown; restored from __doc__
        """ to_rgb(self) -> rgb:Gimp.RGB """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def _get_uchar(self): # real signature unknown; restored from __doc__
        """ _get_uchar(self) -> cyan:int, magenta:int, yellow:int, black:int, alpha:int """
        pass

    def _set(self, cyan, magenta, yellow, black, alpha): # real signature unknown; restored from __doc__
        """ _set(self, cyan:float, magenta:float, yellow:float, black:float, alpha:float) """
        pass

    def _set_uchar(self, cyan, magenta, yellow, black, alpha): # real signature unknown; restored from __doc__
        """ _set_uchar(self, cyan:int, magenta:int, yellow:int, black:int, alpha:int) """
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

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    c = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    k = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    m = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CMYK), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpCMYK (769166592)>, '__dict__': <attribute '__dict__' of 'CMYK' objects>, '__weakref__': <attribute '__weakref__' of 'CMYK' objects>, '__doc__': None, 'c': <property object at 0x000001e82e2bc8b0>, 'm': <property object at 0x000001e82e2bc9a0>, 'y': <property object at 0x000001e82e2bca90>, 'k': <property object at 0x000001e82e2bcb80>, 'a': <property object at 0x000001e82e2bcc70>, '_get_uchar': gi.FunctionInfo(_get_uchar, bound=None), '_set': gi.FunctionInfo(_set, bound=None), '_set_uchar': gi.FunctionInfo(_set_uchar, bound=None), 'get_uchar': gi.FunctionInfo(get_uchar, bound=None), 'set': gi.FunctionInfo(set, bound=None), 'set_uchar': gi.FunctionInfo(set_uchar, bound=None), 'to_rgb': gi.FunctionInfo(to_rgb, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GimpCMYK (769166592)>'
    __info__ = StructInfo(CMYK)


