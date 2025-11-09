# encoding: utf-8
# module gi.repository.Gtk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class TreeViewClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TreeViewClass()
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

    columns_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expand_collapse_cursor_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_activated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_collapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_expanded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    select_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    select_cursor_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    select_cursor_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_interactive_search = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    test_collapse_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    test_expand_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    toggle_cursor_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unselect_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TreeViewClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TreeViewClass' objects>, '__weakref__': <attribute '__weakref__' of 'TreeViewClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000002ece9b52930>, 'row_activated': <property object at 0x000002ece9b52a20>, 'test_expand_row': <property object at 0x000002ece9b52b10>, 'test_collapse_row': <property object at 0x000002ece9b52c00>, 'row_expanded': <property object at 0x000002ece9b52cf0>, 'row_collapsed': <property object at 0x000002ece9b52de0>, 'columns_changed': <property object at 0x000002ece9b52ed0>, 'cursor_changed': <property object at 0x000002ece9b52fc0>, 'move_cursor': <property object at 0x000002ece9b530b0>, 'select_all': <property object at 0x000002ece9b531a0>, 'unselect_all': <property object at 0x000002ece9b53290>, 'select_cursor_row': <property object at 0x000002ece9b53380>, 'toggle_cursor_row': <property object at 0x000002ece9b53470>, 'expand_collapse_cursor_row': <property object at 0x000002ece9b535b0>, 'select_cursor_parent': <property object at 0x000002ece9b536a0>, 'start_interactive_search': <property object at 0x000002ece9b537e0>, '_gtk_reserved1': <property object at 0x000002ece9b538d0>, '_gtk_reserved2': <property object at 0x000002ece9b539c0>, '_gtk_reserved3': <property object at 0x000002ece9b53ab0>, '_gtk_reserved4': <property object at 0x000002ece9b53ba0>, '_gtk_reserved5': <property object at 0x000002ece9b53c90>, '_gtk_reserved6': <property object at 0x000002ece9b53d80>, '_gtk_reserved7': <property object at 0x000002ece9b53e70>, '_gtk_reserved8': <property object at 0x000002ece9b53f60>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TreeViewClass)


