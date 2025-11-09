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


class Queue(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Queue()
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_full(self, free_func=None): # real signature unknown; restored from __doc__
        """ clear_full(self, free_func:GLib.DestroyNotify=None) """
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:GLib.Func, user_data=None) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def free_full(self, free_func): # real signature unknown; restored from __doc__
        """ free_full(self, free_func:GLib.DestroyNotify) """
        pass

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def index(self, data=None): # real signature unknown; restored from __doc__
        """ index(self, data=None) -> int """
        return 0

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def insert_sorted(self, data=None, func, user_data=None): # real signature unknown; restored from __doc__
        """ insert_sorted(self, data=None, func:GLib.CompareDataFunc, user_data=None) """
        pass

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def peek_head(self): # real signature unknown; restored from __doc__
        """ peek_head(self) """
        pass

    def peek_nth(self, n): # real signature unknown; restored from __doc__
        """ peek_nth(self, n:int) """
        pass

    def peek_tail(self): # real signature unknown; restored from __doc__
        """ peek_tail(self) """
        pass

    def pop_head(self): # real signature unknown; restored from __doc__
        """ pop_head(self) """
        pass

    def pop_nth(self, n): # real signature unknown; restored from __doc__
        """ pop_nth(self, n:int) """
        pass

    def pop_tail(self): # real signature unknown; restored from __doc__
        """ pop_tail(self) """
        pass

    def push_head(self, data=None): # real signature unknown; restored from __doc__
        """ push_head(self, data=None) """
        pass

    def push_nth(self, data=None, n): # real signature unknown; restored from __doc__
        """ push_nth(self, data=None, n:int) """
        pass

    def push_tail(self, data=None): # real signature unknown; restored from __doc__
        """ push_tail(self, data=None) """
        pass

    def remove(self, data=None): # real signature unknown; restored from __doc__
        """ remove(self, data=None) -> bool """
        return False

    def remove_all(self, data=None): # real signature unknown; restored from __doc__
        """ remove_all(self, data=None) -> int """
        return 0

    def reverse(self): # real signature unknown; restored from __doc__
        """ reverse(self) """
        pass

    def sort(self, compare_func, user_data=None): # real signature unknown; restored from __doc__
        """ sort(self, compare_func:GLib.CompareDataFunc, user_data=None) """
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

    head = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Queue), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Queue' objects>, '__weakref__': <attribute '__weakref__' of 'Queue' objects>, '__doc__': None, 'head': <property object at 0x000002830bef54e0>, 'tail': <property object at 0x000002830bef55d0>, 'length': <property object at 0x000002830bef56c0>, 'clear': gi.FunctionInfo(clear, bound=None), 'clear_full': gi.FunctionInfo(clear_full, bound=None), 'foreach': gi.FunctionInfo(foreach, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'free_full': gi.FunctionInfo(free_full, bound=None), 'get_length': gi.FunctionInfo(get_length, bound=None), 'index': gi.FunctionInfo(index, bound=None), 'init': gi.FunctionInfo(init, bound=None), 'insert_sorted': gi.FunctionInfo(insert_sorted, bound=None), 'is_empty': gi.FunctionInfo(is_empty, bound=None), 'peek_head': gi.FunctionInfo(peek_head, bound=None), 'peek_nth': gi.FunctionInfo(peek_nth, bound=None), 'peek_tail': gi.FunctionInfo(peek_tail, bound=None), 'pop_head': gi.FunctionInfo(pop_head, bound=None), 'pop_nth': gi.FunctionInfo(pop_nth, bound=None), 'pop_tail': gi.FunctionInfo(pop_tail, bound=None), 'push_head': gi.FunctionInfo(push_head, bound=None), 'push_nth': gi.FunctionInfo(push_nth, bound=None), 'push_tail': gi.FunctionInfo(push_tail, bound=None), 'remove': gi.FunctionInfo(remove, bound=None), 'remove_all': gi.FunctionInfo(remove_all, bound=None), 'reverse': gi.FunctionInfo(reverse, bound=None), 'sort': gi.FunctionInfo(sort, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Queue)


