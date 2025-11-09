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


class Bytes(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(data:list=None) -> GLib.Bytes
        new_take(data:list=None) -> GLib.Bytes
    """
    def compare(self, bytes2): # real signature unknown; restored from __doc__
        """ compare(self, bytes2:GLib.Bytes) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, bytes2): # real signature unknown; restored from __doc__
        """ equal(self, bytes2:GLib.Bytes) -> bool """
        return False

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> list or None """
        return []

    def get_region(self, element_size, offset, n_elements): # real signature unknown; restored from __doc__
        """ get_region(self, element_size:int, offset:int, n_elements:int) """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def new(self, data=None): # real signature unknown; restored from __doc__
        """ new(data:list=None) -> GLib.Bytes """
        pass

    def new_from_bytes(self, offset, length): # real signature unknown; restored from __doc__
        """ new_from_bytes(self, offset:int, length:int) -> GLib.Bytes """
        pass

    def new_take(self, data=None): # real signature unknown; restored from __doc__
        """ new_take(data:list=None) -> GLib.Bytes """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Bytes """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def unref_to_array(self): # real signature unknown; restored from __doc__
        """ unref_to_array(self) -> list """
        return []

    def unref_to_data(self): # real signature unknown; restored from __doc__
        """ unref_to_data(self) -> list """
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
        """ new(data:list=None) -> GLib.Bytes """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Bytes), '__module__': 'gi.repository.GLib', '__gtype__': <GType GBytes (155712240)>, '__dict__': <attribute '__dict__' of 'Bytes' objects>, '__weakref__': <attribute '__weakref__' of 'Bytes' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'new_take': gi.FunctionInfo(new_take, bound=None), 'compare': gi.FunctionInfo(compare, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'get_data': gi.FunctionInfo(get_data, bound=None), 'get_region': gi.FunctionInfo(get_region, bound=None), 'get_size': gi.FunctionInfo(get_size, bound=None), 'hash': gi.FunctionInfo(hash, bound=None), 'new_from_bytes': gi.FunctionInfo(new_from_bytes, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), 'unref_to_array': gi.FunctionInfo(unref_to_array, bound=None), 'unref_to_data': gi.FunctionInfo(unref_to_data, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000002830be60720>})"
    __gtype__ = None # (!) real value is '<GType GBytes (155712240)>'
    __info__ = StructInfo(Bytes)


