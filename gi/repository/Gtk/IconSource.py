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


class IconSource(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Gtk.IconSource
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.IconSource """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_direction_wildcarded(self): # real signature unknown; restored from __doc__
        """ get_direction_wildcarded(self) -> bool """
        return False

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_pixbuf(self) -> GdkPixbuf.Pixbuf """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_size_wildcarded(self): # real signature unknown; restored from __doc__
        """ get_size_wildcarded(self) -> bool """
        return False

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateType """
        pass

    def get_state_wildcarded(self): # real signature unknown; restored from __doc__
        """ get_state_wildcarded(self) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.IconSource """
        pass

    def set_direction(self, direction): # real signature unknown; restored from __doc__
        """ set_direction(self, direction:Gtk.TextDirection) """
        pass

    def set_direction_wildcarded(self, setting): # real signature unknown; restored from __doc__
        """ set_direction_wildcarded(self, setting:bool) """
        pass

    def set_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_filename(self, filename:str) """
        pass

    def set_icon_name(self, icon_name=None): # real signature unknown; restored from __doc__
        """ set_icon_name(self, icon_name:str=None) """
        pass

    def set_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ set_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
        pass

    def set_size_wildcarded(self, setting): # real signature unknown; restored from __doc__
        """ set_size_wildcarded(self, setting:bool) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gtk.StateType) """
        pass

    def set_state_wildcarded(self, setting): # real signature unknown; restored from __doc__
        """ set_state_wildcarded(self, setting:bool) """
        pass

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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Gtk.IconSource """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IconSource), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkIconSource (3923978912)>, '__dict__': <attribute '__dict__' of 'IconSource' objects>, '__weakref__': <attribute '__weakref__' of 'IconSource' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_direction': gi.FunctionInfo(get_direction, bound=None), 'get_direction_wildcarded': gi.FunctionInfo(get_direction_wildcarded, bound=None), 'get_filename': gi.FunctionInfo(get_filename, bound=None), 'get_icon_name': gi.FunctionInfo(get_icon_name, bound=None), 'get_pixbuf': gi.FunctionInfo(get_pixbuf, bound=None), 'get_size': gi.FunctionInfo(get_size, bound=None), 'get_size_wildcarded': gi.FunctionInfo(get_size_wildcarded, bound=None), 'get_state': gi.FunctionInfo(get_state, bound=None), 'get_state_wildcarded': gi.FunctionInfo(get_state_wildcarded, bound=None), 'set_direction': gi.FunctionInfo(set_direction, bound=None), 'set_direction_wildcarded': gi.FunctionInfo(set_direction_wildcarded, bound=None), 'set_filename': gi.FunctionInfo(set_filename, bound=None), 'set_icon_name': gi.FunctionInfo(set_icon_name, bound=None), 'set_pixbuf': gi.FunctionInfo(set_pixbuf, bound=None), 'set_size': gi.FunctionInfo(set_size, bound=None), 'set_size_wildcarded': gi.FunctionInfo(set_size_wildcarded, bound=None), 'set_state': gi.FunctionInfo(set_state, bound=None), 'set_state_wildcarded': gi.FunctionInfo(set_state_wildcarded, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000002ece8827880>})"
    __gtype__ = None # (!) real value is '<GType GtkIconSource (3923978912)>'
    __info__ = StructInfo(IconSource)


