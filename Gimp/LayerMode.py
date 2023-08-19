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


class LayerMode(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_count(self): # real signature unknown; restored from __doc__
        """
        Number of ones in the binary representation of the absolute value of self.
        
        Also known as the population count.
        
        >>> bin(13)
        '0b1101'
        >>> (13).bit_count()
        3
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ADDITION = 33
    ADDITION_LEGACY = 7
    BEHIND = 29
    BEHIND_LEGACY = 2
    BURN = 43
    BURN_LEGACY = 17
    COLOR_ERASE = 57
    COLOR_ERASE_LEGACY = 22
    DARKEN_ONLY = 35
    DARKEN_ONLY_LEGACY = 9
    DIFFERENCE = 32
    DIFFERENCE_LEGACY = 6
    DISSOLVE = 1
    DIVIDE = 41
    DIVIDE_LEGACY = 15
    DODGE = 42
    DODGE_LEGACY = 16
    ERASE = 58
    EXCLUSION = 52
    GRAIN_EXTRACT = 46
    GRAIN_EXTRACT_LEGACY = 20
    GRAIN_MERGE = 47
    GRAIN_MERGE_LEGACY = 21
    HARDLIGHT = 44
    HARDLIGHT_LEGACY = 18
    HARD_MIX = 51
    HSL_COLOR = 39
    HSL_COLOR_LEGACY = 13
    HSV_HUE = 37
    HSV_HUE_LEGACY = 11
    HSV_SATURATION = 38
    HSV_SATURATION_LEGACY = 12
    HSV_VALUE = 40
    HSV_VALUE_LEGACY = 14
    LCH_CHROMA = 25
    LCH_COLOR = 26
    LCH_HUE = 24
    LCH_LIGHTNESS = 27
    LIGHTEN_ONLY = 36
    LIGHTEN_ONLY_LEGACY = 10
    LINEAR_BURN = 53
    LINEAR_LIGHT = 50
    LUMA_DARKEN_ONLY = 54
    LUMA_LIGHTEN_ONLY = 55
    LUMINANCE = 56
    MERGE = 59
    MULTIPLY = 30
    MULTIPLY_LEGACY = 3
    NORMAL = 28
    NORMAL_LEGACY = 0
    OVERLAY = 23
    OVERLAY_LEGACY = 5
    PASS_THROUGH = 61
    PIN_LIGHT = 49
    SCREEN = 31
    SCREEN_LEGACY = 4
    SOFTLIGHT = 45
    SOFTLIGHT_LEGACY = 19
    SPLIT = 60
    SUBTRACT = 34
    SUBTRACT_LEGACY = 8
    VIVID_LIGHT = 48
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gimp', '__dict__': <attribute '__dict__' of 'LayerMode' objects>, '__doc__': None, '__gtype__': <GType GimpLayerMode (770680320)>, '__enum_values__': {0: <enum GIMP_LAYER_MODE_NORMAL_LEGACY of type Gimp.LayerMode>, 1: <enum GIMP_LAYER_MODE_DISSOLVE of type Gimp.LayerMode>, 2: <enum GIMP_LAYER_MODE_BEHIND_LEGACY of type Gimp.LayerMode>, 3: <enum GIMP_LAYER_MODE_MULTIPLY_LEGACY of type Gimp.LayerMode>, 4: <enum GIMP_LAYER_MODE_SCREEN_LEGACY of type Gimp.LayerMode>, 5: <enum GIMP_LAYER_MODE_OVERLAY_LEGACY of type Gimp.LayerMode>, 6: <enum GIMP_LAYER_MODE_DIFFERENCE_LEGACY of type Gimp.LayerMode>, 7: <enum GIMP_LAYER_MODE_ADDITION_LEGACY of type Gimp.LayerMode>, 8: <enum GIMP_LAYER_MODE_SUBTRACT_LEGACY of type Gimp.LayerMode>, 9: <enum GIMP_LAYER_MODE_DARKEN_ONLY_LEGACY of type Gimp.LayerMode>, 10: <enum GIMP_LAYER_MODE_LIGHTEN_ONLY_LEGACY of type Gimp.LayerMode>, 11: <enum GIMP_LAYER_MODE_HSV_HUE_LEGACY of type Gimp.LayerMode>, 12: <enum GIMP_LAYER_MODE_HSV_SATURATION_LEGACY of type Gimp.LayerMode>, 13: <enum GIMP_LAYER_MODE_HSL_COLOR_LEGACY of type Gimp.LayerMode>, 14: <enum GIMP_LAYER_MODE_HSV_VALUE_LEGACY of type Gimp.LayerMode>, 15: <enum GIMP_LAYER_MODE_DIVIDE_LEGACY of type Gimp.LayerMode>, 16: <enum GIMP_LAYER_MODE_DODGE_LEGACY of type Gimp.LayerMode>, 17: <enum GIMP_LAYER_MODE_BURN_LEGACY of type Gimp.LayerMode>, 18: <enum GIMP_LAYER_MODE_HARDLIGHT_LEGACY of type Gimp.LayerMode>, 19: <enum GIMP_LAYER_MODE_SOFTLIGHT_LEGACY of type Gimp.LayerMode>, 20: <enum GIMP_LAYER_MODE_GRAIN_EXTRACT_LEGACY of type Gimp.LayerMode>, 21: <enum GIMP_LAYER_MODE_GRAIN_MERGE_LEGACY of type Gimp.LayerMode>, 22: <enum GIMP_LAYER_MODE_COLOR_ERASE_LEGACY of type Gimp.LayerMode>, 23: <enum GIMP_LAYER_MODE_OVERLAY of type Gimp.LayerMode>, 24: <enum GIMP_LAYER_MODE_LCH_HUE of type Gimp.LayerMode>, 25: <enum GIMP_LAYER_MODE_LCH_CHROMA of type Gimp.LayerMode>, 26: <enum GIMP_LAYER_MODE_LCH_COLOR of type Gimp.LayerMode>, 27: <enum GIMP_LAYER_MODE_LCH_LIGHTNESS of type Gimp.LayerMode>, 28: <enum GIMP_LAYER_MODE_NORMAL of type Gimp.LayerMode>, 29: <enum GIMP_LAYER_MODE_BEHIND of type Gimp.LayerMode>, 30: <enum GIMP_LAYER_MODE_MULTIPLY of type Gimp.LayerMode>, 31: <enum GIMP_LAYER_MODE_SCREEN of type Gimp.LayerMode>, 32: <enum GIMP_LAYER_MODE_DIFFERENCE of type Gimp.LayerMode>, 33: <enum GIMP_LAYER_MODE_ADDITION of type Gimp.LayerMode>, 34: <enum GIMP_LAYER_MODE_SUBTRACT of type Gimp.LayerMode>, 35: <enum GIMP_LAYER_MODE_DARKEN_ONLY of type Gimp.LayerMode>, 36: <enum GIMP_LAYER_MODE_LIGHTEN_ONLY of type Gimp.LayerMode>, 37: <enum GIMP_LAYER_MODE_HSV_HUE of type Gimp.LayerMode>, 38: <enum GIMP_LAYER_MODE_HSV_SATURATION of type Gimp.LayerMode>, 39: <enum GIMP_LAYER_MODE_HSL_COLOR of type Gimp.LayerMode>, 40: <enum GIMP_LAYER_MODE_HSV_VALUE of type Gimp.LayerMode>, 41: <enum GIMP_LAYER_MODE_DIVIDE of type Gimp.LayerMode>, 42: <enum GIMP_LAYER_MODE_DODGE of type Gimp.LayerMode>, 43: <enum GIMP_LAYER_MODE_BURN of type Gimp.LayerMode>, 44: <enum GIMP_LAYER_MODE_HARDLIGHT of type Gimp.LayerMode>, 45: <enum GIMP_LAYER_MODE_SOFTLIGHT of type Gimp.LayerMode>, 46: <enum GIMP_LAYER_MODE_GRAIN_EXTRACT of type Gimp.LayerMode>, 47: <enum GIMP_LAYER_MODE_GRAIN_MERGE of type Gimp.LayerMode>, 48: <enum GIMP_LAYER_MODE_VIVID_LIGHT of type Gimp.LayerMode>, 49: <enum GIMP_LAYER_MODE_PIN_LIGHT of type Gimp.LayerMode>, 50: <enum GIMP_LAYER_MODE_LINEAR_LIGHT of type Gimp.LayerMode>, 51: <enum GIMP_LAYER_MODE_HARD_MIX of type Gimp.LayerMode>, 52: <enum GIMP_LAYER_MODE_EXCLUSION of type Gimp.LayerMode>, 53: <enum GIMP_LAYER_MODE_LINEAR_BURN of type Gimp.LayerMode>, 54: <enum GIMP_LAYER_MODE_LUMA_DARKEN_ONLY of type Gimp.LayerMode>, 55: <enum GIMP_LAYER_MODE_LUMA_LIGHTEN_ONLY of type Gimp.LayerMode>, 56: <enum GIMP_LAYER_MODE_LUMINANCE of type Gimp.LayerMode>, 57: <enum GIMP_LAYER_MODE_COLOR_ERASE of type Gimp.LayerMode>, 58: <enum GIMP_LAYER_MODE_ERASE of type Gimp.LayerMode>, 59: <enum GIMP_LAYER_MODE_MERGE of type Gimp.LayerMode>, 60: <enum GIMP_LAYER_MODE_SPLIT of type Gimp.LayerMode>, 61: <enum GIMP_LAYER_MODE_PASS_THROUGH of type Gimp.LayerMode>}, '__info__': gi.EnumInfo(LayerMode), 'NORMAL_LEGACY': <enum GIMP_LAYER_MODE_NORMAL_LEGACY of type Gimp.LayerMode>, 'DISSOLVE': <enum GIMP_LAYER_MODE_DISSOLVE of type Gimp.LayerMode>, 'BEHIND_LEGACY': <enum GIMP_LAYER_MODE_BEHIND_LEGACY of type Gimp.LayerMode>, 'MULTIPLY_LEGACY': <enum GIMP_LAYER_MODE_MULTIPLY_LEGACY of type Gimp.LayerMode>, 'SCREEN_LEGACY': <enum GIMP_LAYER_MODE_SCREEN_LEGACY of type Gimp.LayerMode>, 'OVERLAY_LEGACY': <enum GIMP_LAYER_MODE_OVERLAY_LEGACY of type Gimp.LayerMode>, 'DIFFERENCE_LEGACY': <enum GIMP_LAYER_MODE_DIFFERENCE_LEGACY of type Gimp.LayerMode>, 'ADDITION_LEGACY': <enum GIMP_LAYER_MODE_ADDITION_LEGACY of type Gimp.LayerMode>, 'SUBTRACT_LEGACY': <enum GIMP_LAYER_MODE_SUBTRACT_LEGACY of type Gimp.LayerMode>, 'DARKEN_ONLY_LEGACY': <enum GIMP_LAYER_MODE_DARKEN_ONLY_LEGACY of type Gimp.LayerMode>, 'LIGHTEN_ONLY_LEGACY': <enum GIMP_LAYER_MODE_LIGHTEN_ONLY_LEGACY of type Gimp.LayerMode>, 'HSV_HUE_LEGACY': <enum GIMP_LAYER_MODE_HSV_HUE_LEGACY of type Gimp.LayerMode>, 'HSV_SATURATION_LEGACY': <enum GIMP_LAYER_MODE_HSV_SATURATION_LEGACY of type Gimp.LayerMode>, 'HSL_COLOR_LEGACY': <enum GIMP_LAYER_MODE_HSL_COLOR_LEGACY of type Gimp.LayerMode>, 'HSV_VALUE_LEGACY': <enum GIMP_LAYER_MODE_HSV_VALUE_LEGACY of type Gimp.LayerMode>, 'DIVIDE_LEGACY': <enum GIMP_LAYER_MODE_DIVIDE_LEGACY of type Gimp.LayerMode>, 'DODGE_LEGACY': <enum GIMP_LAYER_MODE_DODGE_LEGACY of type Gimp.LayerMode>, 'BURN_LEGACY': <enum GIMP_LAYER_MODE_BURN_LEGACY of type Gimp.LayerMode>, 'HARDLIGHT_LEGACY': <enum GIMP_LAYER_MODE_HARDLIGHT_LEGACY of type Gimp.LayerMode>, 'SOFTLIGHT_LEGACY': <enum GIMP_LAYER_MODE_SOFTLIGHT_LEGACY of type Gimp.LayerMode>, 'GRAIN_EXTRACT_LEGACY': <enum GIMP_LAYER_MODE_GRAIN_EXTRACT_LEGACY of type Gimp.LayerMode>, 'GRAIN_MERGE_LEGACY': <enum GIMP_LAYER_MODE_GRAIN_MERGE_LEGACY of type Gimp.LayerMode>, 'COLOR_ERASE_LEGACY': <enum GIMP_LAYER_MODE_COLOR_ERASE_LEGACY of type Gimp.LayerMode>, 'OVERLAY': <enum GIMP_LAYER_MODE_OVERLAY of type Gimp.LayerMode>, 'LCH_HUE': <enum GIMP_LAYER_MODE_LCH_HUE of type Gimp.LayerMode>, 'LCH_CHROMA': <enum GIMP_LAYER_MODE_LCH_CHROMA of type Gimp.LayerMode>, 'LCH_COLOR': <enum GIMP_LAYER_MODE_LCH_COLOR of type Gimp.LayerMode>, 'LCH_LIGHTNESS': <enum GIMP_LAYER_MODE_LCH_LIGHTNESS of type Gimp.LayerMode>, 'NORMAL': <enum GIMP_LAYER_MODE_NORMAL of type Gimp.LayerMode>, 'BEHIND': <enum GIMP_LAYER_MODE_BEHIND of type Gimp.LayerMode>, 'MULTIPLY': <enum GIMP_LAYER_MODE_MULTIPLY of type Gimp.LayerMode>, 'SCREEN': <enum GIMP_LAYER_MODE_SCREEN of type Gimp.LayerMode>, 'DIFFERENCE': <enum GIMP_LAYER_MODE_DIFFERENCE of type Gimp.LayerMode>, 'ADDITION': <enum GIMP_LAYER_MODE_ADDITION of type Gimp.LayerMode>, 'SUBTRACT': <enum GIMP_LAYER_MODE_SUBTRACT of type Gimp.LayerMode>, 'DARKEN_ONLY': <enum GIMP_LAYER_MODE_DARKEN_ONLY of type Gimp.LayerMode>, 'LIGHTEN_ONLY': <enum GIMP_LAYER_MODE_LIGHTEN_ONLY of type Gimp.LayerMode>, 'HSV_HUE': <enum GIMP_LAYER_MODE_HSV_HUE of type Gimp.LayerMode>, 'HSV_SATURATION': <enum GIMP_LAYER_MODE_HSV_SATURATION of type Gimp.LayerMode>, 'HSL_COLOR': <enum GIMP_LAYER_MODE_HSL_COLOR of type Gimp.LayerMode>, 'HSV_VALUE': <enum GIMP_LAYER_MODE_HSV_VALUE of type Gimp.LayerMode>, 'DIVIDE': <enum GIMP_LAYER_MODE_DIVIDE of type Gimp.LayerMode>, 'DODGE': <enum GIMP_LAYER_MODE_DODGE of type Gimp.LayerMode>, 'BURN': <enum GIMP_LAYER_MODE_BURN of type Gimp.LayerMode>, 'HARDLIGHT': <enum GIMP_LAYER_MODE_HARDLIGHT of type Gimp.LayerMode>, 'SOFTLIGHT': <enum GIMP_LAYER_MODE_SOFTLIGHT of type Gimp.LayerMode>, 'GRAIN_EXTRACT': <enum GIMP_LAYER_MODE_GRAIN_EXTRACT of type Gimp.LayerMode>, 'GRAIN_MERGE': <enum GIMP_LAYER_MODE_GRAIN_MERGE of type Gimp.LayerMode>, 'VIVID_LIGHT': <enum GIMP_LAYER_MODE_VIVID_LIGHT of type Gimp.LayerMode>, 'PIN_LIGHT': <enum GIMP_LAYER_MODE_PIN_LIGHT of type Gimp.LayerMode>, 'LINEAR_LIGHT': <enum GIMP_LAYER_MODE_LINEAR_LIGHT of type Gimp.LayerMode>, 'HARD_MIX': <enum GIMP_LAYER_MODE_HARD_MIX of type Gimp.LayerMode>, 'EXCLUSION': <enum GIMP_LAYER_MODE_EXCLUSION of type Gimp.LayerMode>, 'LINEAR_BURN': <enum GIMP_LAYER_MODE_LINEAR_BURN of type Gimp.LayerMode>, 'LUMA_DARKEN_ONLY': <enum GIMP_LAYER_MODE_LUMA_DARKEN_ONLY of type Gimp.LayerMode>, 'LUMA_LIGHTEN_ONLY': <enum GIMP_LAYER_MODE_LUMA_LIGHTEN_ONLY of type Gimp.LayerMode>, 'LUMINANCE': <enum GIMP_LAYER_MODE_LUMINANCE of type Gimp.LayerMode>, 'COLOR_ERASE': <enum GIMP_LAYER_MODE_COLOR_ERASE of type Gimp.LayerMode>, 'ERASE': <enum GIMP_LAYER_MODE_ERASE of type Gimp.LayerMode>, 'MERGE': <enum GIMP_LAYER_MODE_MERGE of type Gimp.LayerMode>, 'SPLIT': <enum GIMP_LAYER_MODE_SPLIT of type Gimp.LayerMode>, 'PASS_THROUGH': <enum GIMP_LAYER_MODE_PASS_THROUGH of type Gimp.LayerMode>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
        46: 46,
        47: 47,
        48: 48,
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
    }
    __gtype__ = None # (!) real value is '<GType GimpLayerMode (770680320)>'
    __info__ = gi.EnumInfo(LayerMode)


