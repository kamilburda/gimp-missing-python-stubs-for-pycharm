# encoding: utf-8
# module gi.repository.Gimp
# from C:\Program Files\GIMP 3\lib\girepository-1.0\Gimp-3.0.typelib
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


class ColorManagedInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ColorManagedInterface()
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

    base_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_color_profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_icc_profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_simulation_bpc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_simulation_intent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_simulation_profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    profile_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation_bpc_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation_intent_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation_profile_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ColorManagedInterface), '__module__': 'gi.repository.Gimp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ColorManagedInterface' objects>, '__weakref__': <attribute '__weakref__' of 'ColorManagedInterface' objects>, '__doc__': None, 'base_iface': <property object at 0x000001dcd90ad6c0>, 'get_icc_profile': <property object at 0x000001dcd90ad7b0>, 'profile_changed': <property object at 0x000001dcd90ad8a0>, 'simulation_profile_changed': <property object at 0x000001dcd90ad9e0>, 'simulation_intent_changed': <property object at 0x000001dcd90adad0>, 'simulation_bpc_changed': <property object at 0x000001dcd90adb70>, 'get_color_profile': <property object at 0x000001dcd90adc60>, 'get_simulation_profile': <property object at 0x000001dcd90add50>, 'get_simulation_intent': <property object at 0x000001dcd90ade40>, 'get_simulation_bpc': <property object at 0x000001dcd90adf30>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ColorManagedInterface)


