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


class Rectangle(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Rectangle()
        new(x:int, y:int, width:int, height:int) -> Gegl.Rectangle
    """
    def align(self, rectangle, tile, alignment): # real signature unknown; restored from __doc__
        """ align(self, rectangle:Gegl.Rectangle, tile:Gegl.Rectangle, alignment:Gegl.RectangleAlignment) -> bool """
        return False

    def align_to_buffer(self, rectangle, buffer, alignment): # real signature unknown; restored from __doc__
        """ align_to_buffer(self, rectangle:Gegl.Rectangle, buffer:Gegl.Buffer, alignment:Gegl.RectangleAlignment) -> bool """
        return False

    def bounding_box(self, source1, source2): # real signature unknown; restored from __doc__
        """ bounding_box(self, source1:Gegl.Rectangle, source2:Gegl.Rectangle) """
        pass

    def contains(self, child): # real signature unknown; restored from __doc__
        """ contains(self, child:Gegl.Rectangle) -> bool """
        return False

    def copy(self, source): # real signature unknown; restored from __doc__
        """ copy(self, source:Gegl.Rectangle) """
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gegl.Rectangle """
        pass

    def equal(self, rectangle2): # real signature unknown; restored from __doc__
        """ equal(self, rectangle2:Gegl.Rectangle) -> bool """
        return False

    def equal_coords(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ equal_coords(self, x:int, y:int, width:int, height:int) -> bool """
        return False

    def infinite_plane(self): # real signature unknown; restored from __doc__
        """ infinite_plane() -> Gegl.Rectangle """
        pass

    def intersect(self, src1, src2): # real signature unknown; restored from __doc__
        """ intersect(self, src1:Gegl.Rectangle, src2:Gegl.Rectangle) -> bool """
        return False

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def is_infinite_plane(self): # real signature unknown; restored from __doc__
        """ is_infinite_plane(self) -> bool """
        return False

    def new(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ new(x:int, y:int, width:int, height:int) -> Gegl.Rectangle """
        pass

    def set(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ set(self, x:int, y:int, width:int, height:int) """
        pass

    def subtract(self, minuend, subtrahend): # real signature unknown; restored from __doc__
        """ subtract(self, minuend:Gegl.Rectangle, subtrahend:Gegl.Rectangle) -> int """
        return 0

    def subtract_bounding_box(self, minuend, subtrahend): # real signature unknown; restored from __doc__
        """ subtract_bounding_box(self, minuend:Gegl.Rectangle, subtrahend:Gegl.Rectangle) -> bool """
        return False

    def xor(self, source1, source2): # real signature unknown; restored from __doc__
        """ xor(self, source1:Gegl.Rectangle, source2:Gegl.Rectangle) -> int """
        return 0

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

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Rectangle), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglRectangle (420741248)>, '__dict__': <attribute '__dict__' of 'Rectangle' objects>, '__weakref__': <attribute '__weakref__' of 'Rectangle' objects>, '__doc__': None, 'x': <property object at 0x000002761b908ea0>, 'y': <property object at 0x000002761b908f90>, 'width': <property object at 0x000002761b909080>, 'height': <property object at 0x000002761b909170>, 'new': gi.FunctionInfo(new, bound=None), 'align': gi.FunctionInfo(align, bound=None), 'align_to_buffer': gi.FunctionInfo(align_to_buffer, bound=None), 'bounding_box': gi.FunctionInfo(bounding_box, bound=None), 'contains': gi.FunctionInfo(contains, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'dump': gi.FunctionInfo(dump, bound=None), 'dup': gi.FunctionInfo(dup, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'equal_coords': gi.FunctionInfo(equal_coords, bound=None), 'intersect': gi.FunctionInfo(intersect, bound=None), 'is_empty': gi.FunctionInfo(is_empty, bound=None), 'is_infinite_plane': gi.FunctionInfo(is_infinite_plane, bound=None), 'set': gi.FunctionInfo(set, bound=None), 'subtract': gi.FunctionInfo(subtract, bound=None), 'subtract_bounding_box': gi.FunctionInfo(subtract_bounding_box, bound=None), 'xor': gi.FunctionInfo(xor, bound=None), 'infinite_plane': gi.FunctionInfo(infinite_plane, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GeglRectangle (420741248)>'
    __info__ = StructInfo(Rectangle)


