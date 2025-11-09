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


class TextIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TextIface()
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

    add_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_bounded_ranges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_caret_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_character_at_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_character_extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_default_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_selections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_offset_at_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_range_extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_run_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_string_at_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text_after_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text_at_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text_before_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_substring_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_substring_to_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_caret_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_attributes_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_caret_moved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_selection_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextIface), '__module__': 'gi.repository.Atk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TextIface' objects>, '__weakref__': <attribute '__weakref__' of 'TextIface' objects>, '__doc__': None, 'parent': <property object at 0x00000173381331f0>, 'get_text': <property object at 0x00000173381332e0>, 'get_text_after_offset': <property object at 0x00000173381333d0>, 'get_text_at_offset': <property object at 0x00000173381334c0>, 'get_character_at_offset': <property object at 0x00000173381335b0>, 'get_text_before_offset': <property object at 0x00000173381336a0>, 'get_caret_offset': <property object at 0x0000017338133790>, 'get_run_attributes': <property object at 0x0000017338133880>, 'get_default_attributes': <property object at 0x0000017338133970>, 'get_character_extents': <property object at 0x0000017338133a60>, 'get_character_count': <property object at 0x0000017338133b50>, 'get_offset_at_point': <property object at 0x0000017338133c40>, 'get_n_selections': <property object at 0x0000017338133d30>, 'get_selection': <property object at 0x0000017338133e20>, 'add_selection': <property object at 0x0000017338133f10>, 'remove_selection': <property object at 0x000001733812c040>, 'set_selection': <property object at 0x000001733812c130>, 'set_caret_offset': <property object at 0x000001733812c220>, 'text_changed': <property object at 0x000001733812c310>, 'text_caret_moved': <property object at 0x000001733812c400>, 'text_selection_changed': <property object at 0x000001733812c4f0>, 'text_attributes_changed': <property object at 0x000001733812c5e0>, 'get_range_extents': <property object at 0x000001733812c6d0>, 'get_bounded_ranges': <property object at 0x000001733812c7c0>, 'get_string_at_offset': <property object at 0x000001733812c8b0>, 'scroll_substring_to': <property object at 0x000001733812c9a0>, 'scroll_substring_to_point': <property object at 0x000001733812cae0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TextIface)


