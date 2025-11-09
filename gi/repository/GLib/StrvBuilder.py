# encoding: utf-8
# module gi.repository.GLib
# from C:/Program Files/GIMP 3/lib/girepository-1.0\GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # C:\Program Files\GIMP 3\lib\python3.12\site-packages\gi\_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class StrvBuilder(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> GLib.StrvBuilder
    """
    def add(self, value): # real signature unknown; restored from __doc__
        """ add(self, value:str) """
        pass

    def addv(self, value): # real signature unknown; restored from __doc__
        """ addv(self, value:list) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> list """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GLib.StrvBuilder """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.StrvBuilder """
        pass

    def take(self, value): # real signature unknown; restored from __doc__
        """ take(self, value:str) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def unref_to_strv(self): # real signature unknown; restored from __doc__
        """ unref_to_strv(self) -> list """
        return []

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
        """ new() -> GLib.StrvBuilder """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StrvBuilder), '__module__': 'gi.repository.GLib', '__gtype__': <GType GStrvBuilder (163506560)>, '__dict__': <attribute '__dict__' of 'StrvBuilder' objects>, '__weakref__': <attribute '__weakref__' of 'StrvBuilder' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'add': gi.FunctionInfo(add, bound=None), 'addv': gi.FunctionInfo(addv, bound=None), 'end': gi.FunctionInfo(end, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'take': gi.FunctionInfo(take, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), 'unref_to_strv': gi.FunctionInfo(unref_to_strv, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000002830be60720>})"
    __gtype__ = None # (!) real value is '<GType GStrvBuilder (163506560)>'
    __info__ = StructInfo(StrvBuilder)


