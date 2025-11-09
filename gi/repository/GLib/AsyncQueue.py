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


class AsyncQueue(__gi.Struct):
    # no doc
    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def length_unlocked(self): # real signature unknown; restored from __doc__
        """ length_unlocked(self) -> int """
        return 0

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GLib.AsyncQueue """
        pass

    def new_full(self, item_free_func=None): # real signature unknown; restored from __doc__
        """ new_full(item_free_func:GLib.DestroyNotify=None) -> GLib.AsyncQueue """
        pass

    def pop(self): # real signature unknown; restored from __doc__
        """ pop(self) """
        pass

    def pop_unlocked(self): # real signature unknown; restored from __doc__
        """ pop_unlocked(self) """
        pass

    def push(self, data): # real signature unknown; restored from __doc__
        """ push(self, data) """
        pass

    def push_front(self, item): # real signature unknown; restored from __doc__
        """ push_front(self, item) """
        pass

    def push_front_unlocked(self, item): # real signature unknown; restored from __doc__
        """ push_front_unlocked(self, item) """
        pass

    def push_sorted(self, data, func, user_data=None): # real signature unknown; restored from __doc__
        """ push_sorted(self, data, func:GLib.CompareDataFunc, user_data=None) """
        pass

    def push_sorted_unlocked(self, data=None, func, user_data=None): # real signature unknown; restored from __doc__
        """ push_sorted_unlocked(self, data=None, func:GLib.CompareDataFunc, user_data=None) """
        pass

    def push_unlocked(self, data): # real signature unknown; restored from __doc__
        """ push_unlocked(self, data) """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.AsyncQueue """
        pass

    def ref_unlocked(self): # real signature unknown; restored from __doc__
        """ ref_unlocked(self) """
        pass

    def remove(self, item): # real signature unknown; restored from __doc__
        """ remove(self, item) -> bool """
        return False

    def remove_unlocked(self, item=None): # real signature unknown; restored from __doc__
        """ remove_unlocked(self, item=None) -> bool """
        return False

    def sort(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ sort(self, func:GLib.CompareDataFunc, user_data=None) """
        pass

    def sort_unlocked(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ sort_unlocked(self, func:GLib.CompareDataFunc, user_data=None) """
        pass

    def timed_pop(self, end_time): # real signature unknown; restored from __doc__
        """ timed_pop(self, end_time:GLib.TimeVal) """
        pass

    def timed_pop_unlocked(self, end_time): # real signature unknown; restored from __doc__
        """ timed_pop_unlocked(self, end_time:GLib.TimeVal) """
        pass

    def timeout_pop(self, timeout): # real signature unknown; restored from __doc__
        """ timeout_pop(self, timeout:int) """
        pass

    def timeout_pop_unlocked(self, timeout): # real signature unknown; restored from __doc__
        """ timeout_pop_unlocked(self, timeout:int) """
        pass

    def try_pop(self): # real signature unknown; restored from __doc__
        """ try_pop(self) """
        pass

    def try_pop_unlocked(self): # real signature unknown; restored from __doc__
        """ try_pop_unlocked(self) """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def unref_and_unlock(self): # real signature unknown; restored from __doc__
        """ unref_and_unlock(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AsyncQueue), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AsyncQueue' objects>, '__weakref__': <attribute '__weakref__' of 'AsyncQueue' objects>, '__doc__': None, 'length': gi.FunctionInfo(length, bound=None), 'length_unlocked': gi.FunctionInfo(length_unlocked, bound=None), 'lock': gi.FunctionInfo(lock, bound=None), 'pop': gi.FunctionInfo(pop, bound=None), 'pop_unlocked': gi.FunctionInfo(pop_unlocked, bound=None), 'push': gi.FunctionInfo(push, bound=None), 'push_front': gi.FunctionInfo(push_front, bound=None), 'push_front_unlocked': gi.FunctionInfo(push_front_unlocked, bound=None), 'push_sorted': gi.FunctionInfo(push_sorted, bound=None), 'push_sorted_unlocked': gi.FunctionInfo(push_sorted_unlocked, bound=None), 'push_unlocked': gi.FunctionInfo(push_unlocked, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'ref_unlocked': gi.FunctionInfo(ref_unlocked, bound=None), 'remove': gi.FunctionInfo(remove, bound=None), 'remove_unlocked': gi.FunctionInfo(remove_unlocked, bound=None), 'sort': gi.FunctionInfo(sort, bound=None), 'sort_unlocked': gi.FunctionInfo(sort_unlocked, bound=None), 'timed_pop': gi.FunctionInfo(timed_pop, bound=None), 'timed_pop_unlocked': gi.FunctionInfo(timed_pop_unlocked, bound=None), 'timeout_pop': gi.FunctionInfo(timeout_pop, bound=None), 'timeout_pop_unlocked': gi.FunctionInfo(timeout_pop_unlocked, bound=None), 'try_pop': gi.FunctionInfo(try_pop, bound=None), 'try_pop_unlocked': gi.FunctionInfo(try_pop_unlocked, bound=None), 'unlock': gi.FunctionInfo(unlock, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), 'unref_and_unlock': gi.FunctionInfo(unref_and_unlock, bound=None), 'new': gi.FunctionInfo(new, bound=None), 'new_full': gi.FunctionInfo(new_full, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AsyncQueue)


