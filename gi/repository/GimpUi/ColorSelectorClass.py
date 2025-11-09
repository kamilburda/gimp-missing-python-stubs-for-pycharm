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


class ColorSelectorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ColorSelectorClass()
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

    channel_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    help_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model_visible_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_model_visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_show_alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_simulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_toggles_sensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_toggles_visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ColorSelectorClass), '__module__': 'gi.repository.GimpUi', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ColorSelectorClass' objects>, '__weakref__': <attribute '__weakref__' of 'ColorSelectorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000001eeb74d8810>, 'name': <property object at 0x000001eeb74d8900>, 'help_id': <property object at 0x000001eeb74d89f0>, 'icon_name': <property object at 0x000001eeb74d8ae0>, 'set_toggles_visible': <property object at 0x000001eeb74d8bd0>, 'set_toggles_sensitive': <property object at 0x000001eeb74d8cc0>, 'set_show_alpha': <property object at 0x000001eeb74d8db0>, 'set_color': <property object at 0x000001eeb74d8ea0>, 'set_channel': <property object at 0x000001eeb74d8f90>, 'set_model_visible': <property object at 0x000001eeb74d9080>, 'set_config': <property object at 0x000001eeb74d9170>, 'set_format': <property object at 0x000001eeb74d9260>, 'set_simulation': <property object at 0x000001eeb74d9350>, 'color_changed': <property object at 0x000001eeb74d9440>, 'channel_changed': <property object at 0x000001eeb74d9530>, 'model_visible_changed': <property object at 0x000001eeb74d9620>, 'simulation': <property object at 0x000001eeb74d9710>, '_gimp_reserved0': <property object at 0x000001eeb74d9800>, '_gimp_reserved1': <property object at 0x000001eeb74d98f0>, '_gimp_reserved2': <property object at 0x000001eeb74d99e0>, '_gimp_reserved3': <property object at 0x000001eeb74d9ad0>, '_gimp_reserved4': <property object at 0x000001eeb74d9bc0>, '_gimp_reserved5': <property object at 0x000001eeb74d9cb0>, '_gimp_reserved6': <property object at 0x000001eeb74d9da0>, '_gimp_reserved7': <property object at 0x000001eeb74d9e90>, '_gimp_reserved8': <property object at 0x000001eeb74d9f80>, '_gimp_reserved9': <property object at 0x000001eeb74da070>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ColorSelectorClass)


