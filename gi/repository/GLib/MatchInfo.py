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


class MatchInfo(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def expand_references(self, string_to_expand): # real signature unknown; restored from __doc__
        """ expand_references(self, string_to_expand:str) -> str or None """
        return ""

    def fetch(self, match_num): # real signature unknown; restored from __doc__
        """ fetch(self, match_num:int) -> str or None """
        return ""

    def fetch_all(self): # real signature unknown; restored from __doc__
        """ fetch_all(self) -> list """
        return []

    def fetch_named(self, name): # real signature unknown; restored from __doc__
        """ fetch_named(self, name:str) -> str or None """
        return ""

    def fetch_named_pos(self, name): # real signature unknown; restored from __doc__
        """ fetch_named_pos(self, name:str) -> bool, start_pos:int, end_pos:int """
        return False

    def fetch_pos(self, match_num): # real signature unknown; restored from __doc__
        """ fetch_pos(self, match_num:int) -> bool, start_pos:int, end_pos:int """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_match_count(self): # real signature unknown; restored from __doc__
        """ get_match_count(self) -> int """
        return 0

    def get_regex(self): # real signature unknown; restored from __doc__
        """ get_regex(self) -> GLib.Regex """
        pass

    def get_string(self): # real signature unknown; restored from __doc__
        """ get_string(self) -> str """
        return ""

    def is_partial_match(self): # real signature unknown; restored from __doc__
        """ is_partial_match(self) -> bool """
        return False

    def matches(self): # real signature unknown; restored from __doc__
        """ matches(self) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.MatchInfo """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MatchInfo), '__module__': 'gi.repository.GLib', '__gtype__': <GType GMatchInfo (163508912)>, '__dict__': <attribute '__dict__' of 'MatchInfo' objects>, '__weakref__': <attribute '__weakref__' of 'MatchInfo' objects>, '__doc__': None, 'expand_references': gi.FunctionInfo(expand_references, bound=None), 'fetch': gi.FunctionInfo(fetch, bound=None), 'fetch_all': gi.FunctionInfo(fetch_all, bound=None), 'fetch_named': gi.FunctionInfo(fetch_named, bound=None), 'fetch_named_pos': gi.FunctionInfo(fetch_named_pos, bound=None), 'fetch_pos': gi.FunctionInfo(fetch_pos, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_match_count': gi.FunctionInfo(get_match_count, bound=None), 'get_regex': gi.FunctionInfo(get_regex, bound=None), 'get_string': gi.FunctionInfo(get_string, bound=None), 'is_partial_match': gi.FunctionInfo(is_partial_match, bound=None), 'matches': gi.FunctionInfo(matches, bound=None), 'next': gi.FunctionInfo(next, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'unref': gi.FunctionInfo(unref, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GMatchInfo (163508912)>'
    __info__ = StructInfo(MatchInfo)


