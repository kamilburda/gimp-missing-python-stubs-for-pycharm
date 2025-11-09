# encoding: utf-8
# module gi.repository.Pango
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Pango-1.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class Matrix(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Matrix()
    """
    def concat(self, new_matrix): # real signature unknown; restored from __doc__
        """ concat(self, new_matrix:Pango.Matrix) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.Matrix or None """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_font_scale_factor(self): # real signature unknown; restored from __doc__
        """ get_font_scale_factor(self) -> float """
        return 0.0

    def get_font_scale_factors(self): # real signature unknown; restored from __doc__
        """ get_font_scale_factors(self) -> xscale:float, yscale:float """
        pass

    def get_slant_ratio(self): # real signature unknown; restored from __doc__
        """ get_slant_ratio(self) -> float """
        return 0.0

    def rotate(self, degrees): # real signature unknown; restored from __doc__
        """ rotate(self, degrees:float) """
        pass

    def scale(self, scale_x, scale_y): # real signature unknown; restored from __doc__
        """ scale(self, scale_x:float, scale_y:float) """
        pass

    def transform_distance(self, dx, dy): # real signature unknown; restored from __doc__
        """ transform_distance(self, dx:float, dy:float) -> dx:float, dy:float """
        pass

    def transform_pixel_rectangle(self, rect, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ transform_pixel_rectangle(self, rect:Pango.Rectangle=<optional>) -> rect:Pango.Rectangle """
        pass

    def transform_point(self, x, y): # real signature unknown; restored from __doc__
        """ transform_point(self, x:float, y:float) -> x:float, y:float """
        pass

    def transform_rectangle(self, rect, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ transform_rectangle(self, rect:Pango.Rectangle=<optional>) -> rect:Pango.Rectangle """
        pass

    def translate(self, tx, ty): # real signature unknown; restored from __doc__
        """ translate(self, tx:float, ty:float) """
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

    x0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Matrix), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoMatrix (4081764416)>, '__dict__': <attribute '__dict__' of 'Matrix' objects>, '__weakref__': <attribute '__weakref__' of 'Matrix' objects>, '__doc__': None, 'xx': <property object at 0x00000213f6078c20>, 'xy': <property object at 0x00000213f6078d10>, 'yx': <property object at 0x00000213f6078e00>, 'yy': <property object at 0x00000213f6078ef0>, 'x0': <property object at 0x00000213f6078fe0>, 'y0': <property object at 0x00000213f60790d0>, 'concat': gi.FunctionInfo(concat, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_font_scale_factor': gi.FunctionInfo(get_font_scale_factor, bound=None), 'get_font_scale_factors': gi.FunctionInfo(get_font_scale_factors, bound=None), 'get_slant_ratio': gi.FunctionInfo(get_slant_ratio, bound=None), 'rotate': gi.FunctionInfo(rotate, bound=None), 'scale': gi.FunctionInfo(scale, bound=None), 'transform_distance': gi.FunctionInfo(transform_distance, bound=None), 'transform_pixel_rectangle': gi.FunctionInfo(transform_pixel_rectangle, bound=None), 'transform_point': gi.FunctionInfo(transform_point, bound=None), 'transform_rectangle': gi.FunctionInfo(transform_rectangle, bound=None), 'translate': gi.FunctionInfo(translate, bound=None)})"
    __gtype__ = None # (!) real value is '<GType PangoMatrix (4081764416)>'
    __info__ = StructInfo(Matrix)


