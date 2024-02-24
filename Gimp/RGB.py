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


class RGB(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        RGB()
    """
    def add(self, rgb2): # real signature unknown; restored from __doc__
        """ add(self, rgb2:Gimp.RGB) """
        pass

    def clamp(self): # real signature unknown; restored from __doc__
        """ clamp(self) """
        pass

    def composite(self, color2, mode): # real signature unknown; restored from __doc__
        """ composite(self, color2:Gimp.RGB, mode:Gimp.RGBCompositeMode) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def distance(self, rgb2): # real signature unknown; restored from __doc__
        """ distance(self, rgb2:Gimp.RGB) -> float """
        return 0.0

    def gamma(self, gamma): # real signature unknown; restored from __doc__
        """ gamma(self, gamma:float) """
        pass

    def get_pixel(self, format): # real signature unknown; restored from __doc__
        """ get_pixel(self, format:Babl.Object) -> pixel """
        pass

    def get_uchar(self): # real signature unknown; restored from __doc__
        """ get_uchar(self) -> red:int, green:int, blue:int """
        pass

    def list_names(self): # real signature unknown; restored from __doc__
        """ list_names() -> names:list, colors:list """
        pass

    def luminance(self): # real signature unknown; restored from __doc__
        """ luminance(self) -> float """
        return 0.0

    def luminance_uchar(self): # real signature unknown; restored from __doc__
        """ luminance_uchar(self) -> int """
        return 0

    def max(self): # real signature unknown; restored from __doc__
        """ max(self) -> float """
        return 0.0

    def min(self): # real signature unknown; restored from __doc__
        """ min(self) -> float """
        return 0.0

    def multiply(self, factor): # real signature unknown; restored from __doc__
        """ multiply(self, factor:float) """
        pass

    def parse_css(self, css): # real signature unknown; restored from __doc__
        """ parse_css(self, css:list) -> bool """
        return False

    def parse_hex(self, hex): # real signature unknown; restored from __doc__
        """ parse_hex(self, hex:list) -> bool """
        return False

    def parse_name(self, name): # real signature unknown; restored from __doc__
        """ parse_name(self, name:list) -> bool """
        return False

    def set(self, red, green, blue): # real signature unknown; restored from __doc__
        """ set(self, red:float, green:float, blue:float) """
        pass

    def set_alpha(self, alpha): # real signature unknown; restored from __doc__
        """ set_alpha(self, alpha:float) """
        pass

    def set_pixel(self, format, pixel=None): # real signature unknown; restored from __doc__
        """ set_pixel(self, format:Babl.Object, pixel=None) """
        pass

    def set_uchar(self, red, green, blue): # real signature unknown; restored from __doc__
        """ set_uchar(self, red:int, green:int, blue:int) """
        pass

    def subtract(self, rgb2): # real signature unknown; restored from __doc__
        """ subtract(self, rgb2:Gimp.RGB) """
        pass

    def to_cmyk(self, pullout): # real signature unknown; restored from __doc__
        """ to_cmyk(self, pullout:float) -> cmyk:Gimp.CMYK """
        pass

    def to_hsl(self): # real signature unknown; restored from __doc__
        """ to_hsl(self) -> hsl:Gimp.HSL """
        pass

    def to_hsv(self): # real signature unknown; restored from __doc__
        """ to_hsv(self) -> hsv:Gimp.HSV """
        pass

    def _add(self, rgba2): # real signature unknown; restored from __doc__
        """ _add(self, rgba2:Gimp.RGB) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def _distance(self, rgba2): # real signature unknown; restored from __doc__
        """ _distance(self, rgba2:Gimp.RGB) -> float """
        return 0.0

    def _get_pixel(self, format): # real signature unknown; restored from __doc__
        """ _get_pixel(self, format:Babl.Object) -> pixel """
        pass

    def _get_uchar(self): # real signature unknown; restored from __doc__
        """ _get_uchar(self) -> red:int, green:int, blue:int, alpha:int """
        pass

    def _multiply(self, factor): # real signature unknown; restored from __doc__
        """ _multiply(self, factor:float) """
        pass

    def _parse_css(self, css): # real signature unknown; restored from __doc__
        """ _parse_css(self, css:list) -> bool """
        return False

    def _set(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ _set(self, red:float, green:float, blue:float, alpha:float) """
        pass

    def _set_pixel(self, format, pixel=None): # real signature unknown; restored from __doc__
        """ _set_pixel(self, format:Babl.Object, pixel=None) """
        pass

    def _set_uchar(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ _set_uchar(self, red:int, green:int, blue:int, alpha:int) """
        pass

    def _subtract(self, rgba2): # real signature unknown; restored from __doc__
        """ _subtract(self, rgba2:Gimp.RGB) """
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

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    r = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RGB), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpRGB (814716480)>, '__dict__': <attribute '__dict__' of 'RGB' objects>, '__weakref__': <attribute '__weakref__' of 'RGB' objects>, '__doc__': None, 'r': <property object at 0x0000020731661b70>, 'g': <property object at 0x0000020731661c60>, 'b': <property object at 0x0000020731661d50>, 'a': <property object at 0x0000020731661e40>, '_add': gi.FunctionInfo(_add, bound=None), '_distance': gi.FunctionInfo(_distance, bound=None), '_get_pixel': gi.FunctionInfo(_get_pixel, bound=None), '_get_uchar': gi.FunctionInfo(_get_uchar, bound=None), '_multiply': gi.FunctionInfo(_multiply, bound=None), '_parse_css': gi.FunctionInfo(_parse_css, bound=None), '_set': gi.FunctionInfo(_set, bound=None), '_set_pixel': gi.FunctionInfo(_set_pixel, bound=None), '_set_uchar': gi.FunctionInfo(_set_uchar, bound=None), '_subtract': gi.FunctionInfo(_subtract, bound=None), 'add': gi.FunctionInfo(add, bound=None), 'clamp': gi.FunctionInfo(clamp, bound=None), 'composite': gi.FunctionInfo(composite, bound=None), 'distance': gi.FunctionInfo(distance, bound=None), 'gamma': gi.FunctionInfo(gamma, bound=None), 'get_pixel': gi.FunctionInfo(get_pixel, bound=None), 'get_uchar': gi.FunctionInfo(get_uchar, bound=None), 'luminance': gi.FunctionInfo(luminance, bound=None), 'luminance_uchar': gi.FunctionInfo(luminance_uchar, bound=None), 'max': gi.FunctionInfo(max, bound=None), 'min': gi.FunctionInfo(min, bound=None), 'multiply': gi.FunctionInfo(multiply, bound=None), 'parse_css': gi.FunctionInfo(parse_css, bound=None), 'parse_hex': gi.FunctionInfo(parse_hex, bound=None), 'parse_name': gi.FunctionInfo(parse_name, bound=None), 'set': gi.FunctionInfo(set, bound=None), 'set_alpha': gi.FunctionInfo(set_alpha, bound=None), 'set_pixel': gi.FunctionInfo(set_pixel, bound=None), 'set_uchar': gi.FunctionInfo(set_uchar, bound=None), 'subtract': gi.FunctionInfo(subtract, bound=None), 'to_cmyk': gi.FunctionInfo(to_cmyk, bound=None), 'to_hsl': gi.FunctionInfo(to_hsl, bound=None), 'to_hsv': gi.FunctionInfo(to_hsv, bound=None), 'list_names': gi.FunctionInfo(list_names, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GimpRGB (814716480)>'
    __info__ = StructInfo(RGB)


