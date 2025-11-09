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


class HookList(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        HookList()
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def init(self, hook_size): # real signature unknown; restored from __doc__
        """ init(self, hook_size:int) """
        pass

    def invoke(self, may_recurse): # real signature unknown; restored from __doc__
        """ invoke(self, may_recurse:bool) """
        pass

    def invoke_check(self, may_recurse): # real signature unknown; restored from __doc__
        """ invoke_check(self, may_recurse:bool) """
        pass

    def marshal(self, may_recurse, marshaller, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal(self, may_recurse:bool, marshaller:GLib.HookMarshaller, marshal_data=None) """
        pass

    def marshal_check(self, may_recurse, marshaller, marshal_data=None): # real signature unknown; restored from __doc__
        """ marshal_check(self, may_recurse:bool, marshaller:GLib.HookCheckMarshaller, marshal_data=None) """
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

    dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    finalize_hook = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hooks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hook_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_setup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seq_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HookList), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'HookList' objects>, '__weakref__': <attribute '__weakref__' of 'HookList' objects>, '__doc__': None, 'seq_id': <property object at 0x000002830bf15760>, 'hook_size': <property object at 0x000002830bf15850>, 'is_setup': <property object at 0x000002830bf15940>, 'hooks': <property object at 0x000002830bf15a30>, 'dummy3': <property object at 0x000002830bf15b20>, 'finalize_hook': <property object at 0x000002830bf15c10>, 'dummy': <property object at 0x000002830bf15d00>, 'clear': gi.FunctionInfo(clear, bound=None), 'init': gi.FunctionInfo(init, bound=None), 'invoke': gi.FunctionInfo(invoke, bound=None), 'invoke_check': gi.FunctionInfo(invoke_check, bound=None), 'marshal': gi.FunctionInfo(marshal, bound=None), 'marshal_check': gi.FunctionInfo(marshal_check, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(HookList)


