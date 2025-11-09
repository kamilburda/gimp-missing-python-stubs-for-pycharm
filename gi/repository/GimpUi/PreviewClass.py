# encoding: utf-8
# module gi.repository.GimpUi
# from C:/Program Files/GIMP 3/lib/girepository-1.0\GimpUi-3.0.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gimp as __gi_repository_Gimp
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class PreviewClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PreviewClass()
    """
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

    draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_thumb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invalidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    untransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PreviewClass), '__module__': 'gi.repository.GimpUi', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PreviewClass' objects>, '__weakref__': <attribute '__weakref__' of 'PreviewClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000001eeb74f39c0>, 'draw': <property object at 0x000001eeb74f3ab0>, 'draw_thumb': <property object at 0x000001eeb74f3ba0>, 'draw_buffer': <property object at 0x000001eeb74f3c90>, 'set_cursor': <property object at 0x000001eeb74f3d80>, 'transform': <property object at 0x000001eeb74f3e70>, 'untransform': <property object at 0x000001eeb74f3f60>, 'invalidated': <property object at 0x000001eeb7518090>, '_gimp_reserved0': <property object at 0x000001eeb7518180>, '_gimp_reserved1': <property object at 0x000001eeb7518270>, '_gimp_reserved2': <property object at 0x000001eeb7518360>, '_gimp_reserved3': <property object at 0x000001eeb7518450>, '_gimp_reserved4': <property object at 0x000001eeb7518540>, '_gimp_reserved5': <property object at 0x000001eeb7518630>, '_gimp_reserved6': <property object at 0x000001eeb7518720>, '_gimp_reserved7': <property object at 0x000001eeb7518810>, '_gimp_reserved8': <property object at 0x000001eeb7518900>, '_gimp_reserved9': <property object at 0x000001eeb75189f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PreviewClass)


