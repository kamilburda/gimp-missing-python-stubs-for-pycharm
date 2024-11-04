# encoding: utf-8
# module gi.repository.Gimp
# from C:\Program Files\GIMP 3\lib\girepository-1.0\Gimp-3.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class ValueArray(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(n_prealloced:int) -> Gimp.ValueArray
        new_from_values(values:list) -> Gimp.ValueArray
    """
    def append(self, value=None): # real signature unknown; restored from __doc__
        """ append(self, value:GObject.Value=None) -> Gimp.ValueArray """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gimp.ValueArray """
        pass

    def get_color_array(self, index): # real signature unknown; restored from __doc__
        """ get_color_array(self, index:int) -> list """
        return []

    def get_core_object_array(self, index): # real signature unknown; restored from __doc__
        """ get_core_object_array(self, index:int) -> list """
        return []

    def index(self, index): # real signature unknown; restored from __doc__
        """ index(self, index:int) -> GObject.Value """
        pass

    def insert(self, index, value=None): # real signature unknown; restored from __doc__
        """ insert(self, index:int, value:GObject.Value=None) -> Gimp.ValueArray """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def new(self, n_prealloced): # real signature unknown; restored from __doc__
        """ new(n_prealloced:int) -> Gimp.ValueArray """
        pass

    def new_from_values(self, values): # real signature unknown; restored from __doc__
        """ new_from_values(values:list) -> Gimp.ValueArray """
        pass

    def prepend(self, value=None): # real signature unknown; restored from __doc__
        """ prepend(self, value:GObject.Value=None) -> Gimp.ValueArray """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gimp.ValueArray """
        pass

    def remove(self, index): # real signature unknown; restored from __doc__
        """ remove(self, index:int) -> Gimp.ValueArray """
        pass

    def truncate(self, n_values): # real signature unknown; restored from __doc__
        """ truncate(self, n_values:int) """
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
        """ Default object formatter. """
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
        """ new(n_prealloced:int) -> Gimp.ValueArray """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ValueArray), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpValueArray (1072257088)>, '__dict__': <attribute '__dict__' of 'ValueArray' objects>, '__weakref__': <attribute '__weakref__' of 'ValueArray' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'new_from_values': gi.FunctionInfo(new_from_values, bound=None), 'append': gi.FunctionInfo(append, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'get_color_array': gi.FunctionInfo(get_color_array, bound=None), 'get_core_object_array': gi.FunctionInfo(get_core_object_array, bound=None), 'index': gi.FunctionInfo(index, bound=None), 'insert': gi.FunctionInfo(insert, bound=None), 'length': gi.FunctionInfo(length, bound=None), 'prepend': gi.FunctionInfo(prepend, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'remove': gi.FunctionInfo(remove, bound=None), 'truncate': gi.FunctionInfo(truncate, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000001b6405f6c00>})"
    __gtype__ = None # (!) real value is '<GType GimpValueArray (1072257088)>'
    __info__ = StructInfo(ValueArray)


