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


class Matrix3(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Matrix3()
    """
    def affine(self, a, b, c, d, e, f): # real signature unknown; restored from __doc__
        """ affine(self, a:float, b:float, c:float, d:float, e:float, f:float) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def equal(self, matrix2): # real signature unknown; restored from __doc__
        """ equal(self, matrix2:Gimp.Matrix3) -> bool """
        return False

    def identity(self): # real signature unknown; restored from __doc__
        """ identity(self) """
        pass

    def invert(self): # real signature unknown; restored from __doc__
        """ invert(self) """
        pass

    def is_affine(self): # real signature unknown; restored from __doc__
        """ is_affine(self) -> bool """
        return False

    def is_diagonal(self): # real signature unknown; restored from __doc__
        """ is_diagonal(self) -> bool """
        return False

    def is_identity(self): # real signature unknown; restored from __doc__
        """ is_identity(self) -> bool """
        return False

    def is_simple(self): # real signature unknown; restored from __doc__
        """ is_simple(self) -> bool """
        return False

    def mult(self, right): # real signature unknown; restored from __doc__
        """ mult(self, right:Gimp.Matrix3) """
        pass

    def rotate(self, theta): # real signature unknown; restored from __doc__
        """ rotate(self, theta:float) """
        pass

    def scale(self, x, y): # real signature unknown; restored from __doc__
        """ scale(self, x:float, y:float) """
        pass

    def transform_point(self, x, y, newx, newy): # real signature unknown; restored from __doc__
        """ transform_point(self, x:float, y:float, newx:float, newy:float) """
        pass

    def translate(self, x, y): # real signature unknown; restored from __doc__
        """ translate(self, x:float, y:float) """
        pass

    def xshear(self, amount): # real signature unknown; restored from __doc__
        """ xshear(self, amount:float) """
        pass

    def yshear(self, amount): # real signature unknown; restored from __doc__
        """ yshear(self, amount:float) """
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

    coeff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Matrix3), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpMatrix3 (815079296)>, '__dict__': <attribute '__dict__' of 'Matrix3' objects>, '__weakref__': <attribute '__weakref__' of 'Matrix3' objects>, '__doc__': None, 'coeff': <property object at 0x0000020731632c50>, 'affine': gi.FunctionInfo(affine, bound=None), 'determinant': gi.FunctionInfo(determinant, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'identity': gi.FunctionInfo(identity, bound=None), 'invert': gi.FunctionInfo(invert, bound=None), 'is_affine': gi.FunctionInfo(is_affine, bound=None), 'is_diagonal': gi.FunctionInfo(is_diagonal, bound=None), 'is_identity': gi.FunctionInfo(is_identity, bound=None), 'is_simple': gi.FunctionInfo(is_simple, bound=None), 'mult': gi.FunctionInfo(mult, bound=None), 'rotate': gi.FunctionInfo(rotate, bound=None), 'scale': gi.FunctionInfo(scale, bound=None), 'transform_point': gi.FunctionInfo(transform_point, bound=None), 'translate': gi.FunctionInfo(translate, bound=None), 'xshear': gi.FunctionInfo(xshear, bound=None), 'yshear': gi.FunctionInfo(yshear, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GimpMatrix3 (815079296)>'
    __info__ = StructInfo(Matrix3)


