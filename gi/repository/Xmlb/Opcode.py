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


class Opcode(__gi.Struct):
    # no doc
    def cmp_str(self): # real signature unknown; restored from __doc__
        """ cmp_str(self) -> bool """
        return False

    def cmp_val(self): # real signature unknown; restored from __doc__
        """ cmp_val(self) -> bool """
        return False

    def func_init(self, func): # real signature unknown; restored from __doc__
        """ func_init(self, func:int) """
        pass

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> Xmlb.OpcodeKind """
        pass

    def get_str(self): # real signature unknown; restored from __doc__
        """ get_str(self) -> str """
        return ""

    def get_val(self): # real signature unknown; restored from __doc__
        """ get_val(self) -> int """
        return 0

    def integer_init(self, val): # real signature unknown; restored from __doc__
        """ integer_init(self, val:int) """
        pass

    def kind_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ kind_from_string(str:str) -> Xmlb.OpcodeKind """
        pass

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:Xmlb.OpcodeKind) -> str """
        return ""

    def text_init(self, p_str): # real signature unknown; restored from __doc__
        """ text_init(self, str:str) """
        pass

    def text_init_static(self, p_str): # real signature unknown; restored from __doc__
        """ text_init_static(self, str:str) """
        pass

    def text_init_steal(self, p_str): # real signature unknown; restored from __doc__
        """ text_init_steal(self, str:str) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Opcode), '__module__': 'gi.repository.Xmlb', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Opcode' objects>, '__weakref__': <attribute '__weakref__' of 'Opcode' objects>, '__doc__': None, 'cmp_str': gi.FunctionInfo(cmp_str), 'cmp_val': gi.FunctionInfo(cmp_val), 'func_init': gi.FunctionInfo(func_init), 'get_kind': gi.FunctionInfo(get_kind), 'get_str': gi.FunctionInfo(get_str), 'get_val': gi.FunctionInfo(get_val), 'integer_init': gi.FunctionInfo(integer_init), 'text_init': gi.FunctionInfo(text_init), 'text_init_static': gi.FunctionInfo(text_init_static), 'text_init_steal': gi.FunctionInfo(text_init_steal), 'to_string': gi.FunctionInfo(to_string), 'kind_from_string': <staticmethod(gi.FunctionInfo(kind_from_string))>, 'kind_to_string': <staticmethod(gi.FunctionInfo(kind_to_string))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Opcode)


