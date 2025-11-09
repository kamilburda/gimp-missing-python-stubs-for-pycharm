# encoding: utf-8
# module gi.repository.Gegl
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gegl-0.4.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Matrix3(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Matrix3()
        new() -> Gegl.Matrix3
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gegl.Matrix3 """
        pass

    def copy_into(self, src): # real signature unknown; restored from __doc__
        """ copy_into(self, src:Gegl.Matrix3) """
        pass

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def equal(self, matrix2): # real signature unknown; restored from __doc__
        """ equal(self, matrix2:Gegl.Matrix3) -> bool """
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

    def is_identity(self): # real signature unknown; restored from __doc__
        """ is_identity(self) -> bool """
        return False

    def is_scale(self): # real signature unknown; restored from __doc__
        """ is_scale(self) -> bool """
        return False

    def is_translate(self): # real signature unknown; restored from __doc__
        """ is_translate(self) -> bool """
        return False

    def multiply(self, right, product): # real signature unknown; restored from __doc__
        """ multiply(self, right:Gegl.Matrix3, product:Gegl.Matrix3) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gegl.Matrix3 """
        pass

    def originate(self, x, y): # real signature unknown; restored from __doc__
        """ originate(self, x:float, y:float) """
        pass

    def parse_string(self, string): # real signature unknown; restored from __doc__
        """ parse_string(self, string:str) """
        pass

    def round_error(self): # real signature unknown; restored from __doc__
        """ round_error(self) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def transform_point(self, x, y): # real signature unknown; restored from __doc__
        """ transform_point(self, x:float, y:float) """
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
        """ new() -> Gegl.Matrix3 """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Matrix3), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglMatrix3 (426594240)>, '__dict__': <attribute '__dict__' of 'Matrix3' objects>, '__weakref__': <attribute '__weakref__' of 'Matrix3' objects>, '__doc__': None, 'coeff': <property object at 0x000002761b94ecf0>, 'new': gi.FunctionInfo(new, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'copy_into': gi.FunctionInfo(copy_into, bound=None), 'determinant': gi.FunctionInfo(determinant, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'identity': gi.FunctionInfo(identity, bound=None), 'invert': gi.FunctionInfo(invert, bound=None), 'is_affine': gi.FunctionInfo(is_affine, bound=None), 'is_identity': gi.FunctionInfo(is_identity, bound=None), 'is_scale': gi.FunctionInfo(is_scale, bound=None), 'is_translate': gi.FunctionInfo(is_translate, bound=None), 'multiply': gi.FunctionInfo(multiply, bound=None), 'originate': gi.FunctionInfo(originate, bound=None), 'parse_string': gi.FunctionInfo(parse_string, bound=None), 'round_error': gi.FunctionInfo(round_error, bound=None), 'to_string': gi.FunctionInfo(to_string, bound=None), 'transform_point': gi.FunctionInfo(transform_point, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000002761b8a7880>})"
    __gtype__ = None # (!) real value is '<GType GeglMatrix3 (426594240)>'
    __info__ = StructInfo(Matrix3)


