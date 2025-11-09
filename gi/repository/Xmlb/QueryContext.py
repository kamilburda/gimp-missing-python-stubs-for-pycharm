# encoding: utf-8
# module gi.repository.Xmlb
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Xmlb-2.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject


class QueryContext(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        QueryContext()
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Xmlb.QueryContext """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_bindings(self): # real signature unknown; restored from __doc__
        """ get_bindings(self) -> Xmlb.ValueBindings """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Xmlb.QueryFlags """
        pass

    def get_limit(self): # real signature unknown; restored from __doc__
        """ get_limit(self) -> int """
        return 0

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Xmlb.QueryFlags) """
        pass

    def set_limit(self, limit): # real signature unknown; restored from __doc__
        """ set_limit(self, limit:int) """
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

    dummy0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dummy3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(QueryContext), '__module__': 'gi.repository.Xmlb', '__gtype__': <GType XbQueryContext (844629904)>, '__dict__': <attribute '__dict__' of 'QueryContext' objects>, '__weakref__': <attribute '__weakref__' of 'QueryContext' objects>, '__doc__': None, 'dummy0': <property object at 0x0000015434714630>, 'dummy1': <property object at 0x0000015434714720>, 'dummy2': <property object at 0x0000015434714810>, 'dummy3': <property object at 0x0000015434714900>, 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_bindings': gi.FunctionInfo(get_bindings), 'get_flags': gi.FunctionInfo(get_flags), 'get_limit': gi.FunctionInfo(get_limit), 'init': gi.FunctionInfo(init), 'set_flags': gi.FunctionInfo(set_flags), 'set_limit': gi.FunctionInfo(set_limit)})"
    __gtype__ = None # (!) real value is '<GType XbQueryContext (844629904)>'
    __info__ = StructInfo(QueryContext)


