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


class NotebookClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        NotebookClass()
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

    change_current_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_tab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_focus_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_reordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reorder_tab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    select_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    switch_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NotebookClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NotebookClass' objects>, '__weakref__': <attribute '__weakref__' of 'NotebookClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000002eceac1fec0>, 'switch_page': <property object at 0x000002eceac1ffb0>, 'select_page': <property object at 0x000002eceac240e0>, 'focus_tab': <property object at 0x000002eceac241d0>, 'change_current_page': <property object at 0x000002eceac242c0>, 'move_focus_out': <property object at 0x000002eceac243b0>, 'reorder_tab': <property object at 0x000002eceac244a0>, 'insert_page': <property object at 0x000002eceac24590>, 'create_window': <property object at 0x000002eceac24680>, 'page_reordered': <property object at 0x000002eceac24770>, 'page_removed': <property object at 0x000002eceac24860>, 'page_added': <property object at 0x000002eceac24950>, '_gtk_reserved1': <property object at 0x000002eceac24a40>, '_gtk_reserved2': <property object at 0x000002eceac24b30>, '_gtk_reserved3': <property object at 0x000002eceac24c20>, '_gtk_reserved4': <property object at 0x000002eceac24d10>, '_gtk_reserved5': <property object at 0x000002eceac24e00>, '_gtk_reserved6': <property object at 0x000002eceac24ef0>, '_gtk_reserved7': <property object at 0x000002eceac24fe0>, '_gtk_reserved8': <property object at 0x000002eceac250d0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NotebookClass)


