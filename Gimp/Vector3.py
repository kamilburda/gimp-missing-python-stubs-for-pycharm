# encoding: utf-8
# module gi.repository.Gimp
# from C:\Program Files\GIMP 2.99\lib\girepository-1.0\Gimp-3.0.typelib
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


class Vector3(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Vector3()
        new(x:float, y:float, z:float) -> Gimp.Vector3
    """
    def add(self, vector1, vector2): # real signature unknown; restored from __doc__
        """ add(vector1:Gimp.Vector3, vector2:Gimp.Vector3) -> result:Gimp.Vector3 """
        pass

    def add_val(self, vector2): # real signature unknown; restored from __doc__
        """ add_val(self, vector2:Gimp.Vector3) -> Gimp.Vector3 """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def cross_product(self, vector2): # real signature unknown; restored from __doc__
        """ cross_product(self, vector2:Gimp.Vector3) -> Gimp.Vector3 """
        pass

    def cross_product_val(self, vector2): # real signature unknown; restored from __doc__
        """ cross_product_val(self, vector2:Gimp.Vector3) -> Gimp.Vector3 """
        pass

    def inner_product(self, vector2): # real signature unknown; restored from __doc__
        """ inner_product(self, vector2:Gimp.Vector3) -> float """
        return 0.0

    def inner_product_val(self, vector2): # real signature unknown; restored from __doc__
        """ inner_product_val(self, vector2:Gimp.Vector3) -> float """
        return 0.0

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def length_val(self): # real signature unknown; restored from __doc__
        """ length_val(self) -> float """
        return 0.0

    def mul(self, factor): # real signature unknown; restored from __doc__
        """ mul(self, factor:float) """
        pass

    def mul_val(self, factor): # real signature unknown; restored from __doc__
        """ mul_val(self, factor:float) -> Gimp.Vector3 """
        pass

    def neg(self): # real signature unknown; restored from __doc__
        """ neg(self) """
        pass

    def neg_val(self): # real signature unknown; restored from __doc__
        """ neg_val(self) -> Gimp.Vector3 """
        pass

    def new(self, x, y, z): # real signature unknown; restored from __doc__
        """ new(x:float, y:float, z:float) -> Gimp.Vector3 """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def normalize_val(self): # real signature unknown; restored from __doc__
        """ normalize_val(self) -> Gimp.Vector3 """
        pass

    def rotate(self, alpha, beta, gamma): # real signature unknown; restored from __doc__
        """ rotate(self, alpha:float, beta:float, gamma:float) """
        pass

    def rotate_val(self, alpha, beta, gamma): # real signature unknown; restored from __doc__
        """ rotate_val(self, alpha:float, beta:float, gamma:float) -> Gimp.Vector3 """
        pass

    def set(self, x, y, z): # real signature unknown; restored from __doc__
        """ set(self, x:float, y:float, z:float) """
        pass

    def sub(self, vector1, vector2): # real signature unknown; restored from __doc__
        """ sub(vector1:Gimp.Vector3, vector2:Gimp.Vector3) -> result:Gimp.Vector3 """
        pass

    def sub_val(self, vector2): # real signature unknown; restored from __doc__
        """ sub_val(self, vector2:Gimp.Vector3) -> Gimp.Vector3 """
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

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Vector3), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpVector3 (814712000)>, '__dict__': <attribute '__dict__' of 'Vector3' objects>, '__weakref__': <attribute '__weakref__' of 'Vector3' objects>, '__doc__': None, 'x': <property object at 0x000002073166a660>, 'y': <property object at 0x000002073166a750>, 'z': <property object at 0x000002073166a840>, 'new': gi.FunctionInfo(new, bound=None), 'add_val': gi.FunctionInfo(add_val, bound=None), 'cross_product': gi.FunctionInfo(cross_product, bound=None), 'cross_product_val': gi.FunctionInfo(cross_product_val, bound=None), 'inner_product': gi.FunctionInfo(inner_product, bound=None), 'inner_product_val': gi.FunctionInfo(inner_product_val, bound=None), 'length': gi.FunctionInfo(length, bound=None), 'length_val': gi.FunctionInfo(length_val, bound=None), 'mul': gi.FunctionInfo(mul, bound=None), 'mul_val': gi.FunctionInfo(mul_val, bound=None), 'neg': gi.FunctionInfo(neg, bound=None), 'neg_val': gi.FunctionInfo(neg_val, bound=None), 'normalize': gi.FunctionInfo(normalize, bound=None), 'normalize_val': gi.FunctionInfo(normalize_val, bound=None), 'rotate': gi.FunctionInfo(rotate, bound=None), 'rotate_val': gi.FunctionInfo(rotate_val, bound=None), 'set': gi.FunctionInfo(set, bound=None), 'sub_val': gi.FunctionInfo(sub_val, bound=None), 'add': gi.FunctionInfo(add, bound=None), 'sub': gi.FunctionInfo(sub, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GimpVector3 (814712000)>'
    __info__ = StructInfo(Vector3)


