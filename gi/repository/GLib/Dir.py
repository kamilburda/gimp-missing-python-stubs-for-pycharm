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


class Dir(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        open(path:str, flags:int) -> GLib.Dir
    """
    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def make_tmp(self, tmpl=None): # real signature unknown; restored from __doc__
        """ make_tmp(tmpl:str=None) -> str """
        return ""

    def open(self, path, flags): # real signature unknown; restored from __doc__
        """ open(path:str, flags:int) -> GLib.Dir """
        pass

    def read_name(self): # real signature unknown; restored from __doc__
        """ read_name(self) -> str """
        return ""

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Dir """
        pass

    def rewind(self): # real signature unknown; restored from __doc__
        """ rewind(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Dir), '__module__': 'gi.repository.GLib', '__gtype__': <GType GDir (155715824)>, '__dict__': <attribute '__dict__' of 'Dir' objects>, '__weakref__': <attribute '__weakref__' of 'Dir' objects>, '__doc__': None, 'open': gi.FunctionInfo(open, bound=None), 'close': gi.FunctionInfo(close, bound=None), 'read_name': gi.FunctionInfo(read_name, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'rewind': gi.FunctionInfo(rewind, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), 'make_tmp': gi.FunctionInfo(make_tmp, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GDir (155715824)>'
    __info__ = StructInfo(Dir)


