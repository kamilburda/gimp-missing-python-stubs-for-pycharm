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


class Hook(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Hook()
    """
    def compare_ids(self, sibling): # real signature unknown; restored from __doc__
        """ compare_ids(self, sibling:GLib.Hook) -> int """
        return 0

    def destroy(self, hook_list, hook_id): # real signature unknown; restored from __doc__
        """ destroy(hook_list:GLib.HookList, hook_id:int) -> bool """
        return False

    def destroy_link(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ destroy_link(hook_list:GLib.HookList, hook:GLib.Hook) """
        pass

    def free(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ free(hook_list:GLib.HookList, hook:GLib.Hook) """
        pass

    def insert_before(self, hook_list, sibling=None, hook): # real signature unknown; restored from __doc__
        """ insert_before(hook_list:GLib.HookList, sibling:GLib.Hook=None, hook:GLib.Hook) """
        pass

    def insert_sorted(self, hook_list, hook, func): # real signature unknown; restored from __doc__
        """ insert_sorted(hook_list:GLib.HookList, hook:GLib.Hook, func:GLib.HookCompareFunc) """
        pass

    def prepend(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ prepend(hook_list:GLib.HookList, hook:GLib.Hook) """
        pass

    def unref(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ unref(hook_list:GLib.HookList, hook:GLib.Hook) """
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hook_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Hook), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Hook' objects>, '__weakref__': <attribute '__weakref__' of 'Hook' objects>, '__doc__': None, 'data': <property object at 0x000002830bf15030>, 'next': <property object at 0x000002830bf15120>, 'prev': <property object at 0x000002830bf15210>, 'ref_count': <property object at 0x000002830bf15300>, 'hook_id': <property object at 0x000002830bf153f0>, 'flags': <property object at 0x000002830bf154e0>, 'func': <property object at 0x000002830bf155d0>, 'destroy': gi.FunctionInfo(destroy, bound=None), 'compare_ids': gi.FunctionInfo(compare_ids, bound=None), 'destroy_link': gi.FunctionInfo(destroy_link, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'insert_before': gi.FunctionInfo(insert_before, bound=None), 'insert_sorted': gi.FunctionInfo(insert_sorted, bound=None), 'prepend': gi.FunctionInfo(prepend, bound=None), 'unref': gi.FunctionInfo(unref, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Hook)


