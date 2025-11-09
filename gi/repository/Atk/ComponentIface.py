# encoding: utf-8
# module gi.repository.Atk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Atk-1.0.typelib
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
import gobject as __gobject


class ComponentIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ComponentIface()
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

    add_focus_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bounds_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mdi_zorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_accessible_at_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_focus_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_to_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentIface), '__module__': 'gi.repository.Atk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ComponentIface' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentIface' objects>, '__doc__': None, 'parent': <property object at 0x000001733817d030>, 'add_focus_handler': <property object at 0x000001733817d120>, 'contains': <property object at 0x000001733817d210>, 'ref_accessible_at_point': <property object at 0x000001733817d300>, 'get_extents': <property object at 0x000001733817d3f0>, 'get_position': <property object at 0x000001733817d4e0>, 'get_size': <property object at 0x000001733817d5d0>, 'grab_focus': <property object at 0x000001733817d6c0>, 'remove_focus_handler': <property object at 0x000001733817d7b0>, 'set_extents': <property object at 0x000001733817d8a0>, 'set_position': <property object at 0x000001733817d990>, 'set_size': <property object at 0x000001733817da80>, 'get_layer': <property object at 0x000001733817db70>, 'get_mdi_zorder': <property object at 0x000001733817dc60>, 'bounds_changed': <property object at 0x000001733817dd50>, 'get_alpha': <property object at 0x000001733817de40>, 'scroll_to': <property object at 0x000001733817df30>, 'scroll_to_point': <property object at 0x000001733817e020>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ComponentIface)


