# encoding: utf-8
# module gi.repository.Gio
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Icon(__gobject.GInterface):
    # no doc
    def deserialize(self, value): # real signature unknown; restored from __doc__
        """ deserialize(value:GLib.Variant) -> Gio.Icon or None """
        pass

    def equal(self, icon2=None): # real signature unknown; restored from __doc__
        """ equal(self, icon2:Gio.Icon=None) -> bool """
        return False

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def new_for_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_for_string(str:str) -> Gio.Icon """
        pass

    def serialize(self): # real signature unknown; restored from __doc__
        """ serialize(self) -> GLib.Variant or None """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str or None """
        return ""

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

    def __init__(self, *args, **kwargs): # real signature unknown
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Icon), '__module__': 'gi.repository.Gio', '__gtype__': <GType GIcon (2435161936)>, '__dict__': <attribute '__dict__' of 'Icon' objects>, '__weakref__': <attribute '__weakref__' of 'Icon' objects>, '__doc__': None, '__gsignals__': {}, 'deserialize': gi.FunctionInfo(deserialize, bound=None), 'new_for_string': gi.FunctionInfo(new_for_string, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'hash': gi.FunctionInfo(hash, bound=None), 'serialize': gi.FunctionInfo(serialize, bound=None), 'to_string': gi.FunctionInfo(to_string, bound=None)})"
    __gdoc__ = 'Interface GIcon\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GIcon (2435161936)>'
    __info__ = InterfaceInfo(Icon)


