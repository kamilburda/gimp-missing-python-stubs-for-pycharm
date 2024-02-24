# encoding: utf-8
# module gi.repository.cairo
# from C:\Program Files\GIMP 2.99\lib\girepository-1.0\cairo-1.0.typelib
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
import gobject as __gobject


class Operator(__gobject.GEnum):
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
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.  Default
            is length 1.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.  Default is to use 'big'.
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


    ADD = 12
    ATOP = 5
    CLEAR = 0
    COLOR_BURN = 20
    COLOR_DODGE = 19
    DARKEN = 17
    DEST = 6
    DEST_ATOP = 10
    DEST_IN = 8
    DEST_OUT = 9
    DEST_OVER = 7
    DIFFERENCE = 23
    EXCLUSION = 24
    HARD_LIGHT = 21
    HSL_COLOR = 27
    HSL_HUE = 25
    HSL_LUMINOSITY = 28
    HSL_SATURATION = 26
    IN = 3
    LIGHTEN = 18
    MULTIPLY = 14
    OUT = 4
    OVER = 2
    OVERLAY = 16
    SATURATE = 13
    SCREEN = 15
    SOFT_LIGHT = 22
    SOURCE = 1
    XOR = 11
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.cairo', '__dict__': <attribute '__dict__' of 'Operator' objects>, '__doc__': None, '__gtype__': <GType cairo_operator_t (804005664)>, '__enum_values__': {0: <enum CAIRO_OPERATOR_CLEAR of type cairo.Operator>, 1: <enum CAIRO_OPERATOR_SOURCE of type cairo.Operator>, 2: <enum CAIRO_OPERATOR_OVER of type cairo.Operator>, 3: <enum CAIRO_OPERATOR_IN of type cairo.Operator>, 4: <enum CAIRO_OPERATOR_OUT of type cairo.Operator>, 5: <enum CAIRO_OPERATOR_ATOP of type cairo.Operator>, 6: <enum CAIRO_OPERATOR_DEST of type cairo.Operator>, 7: <enum CAIRO_OPERATOR_DEST_OVER of type cairo.Operator>, 8: <enum CAIRO_OPERATOR_DEST_IN of type cairo.Operator>, 9: <enum CAIRO_OPERATOR_DEST_OUT of type cairo.Operator>, 10: <enum CAIRO_OPERATOR_DEST_ATOP of type cairo.Operator>, 11: <enum CAIRO_OPERATOR_XOR of type cairo.Operator>, 12: <enum CAIRO_OPERATOR_ADD of type cairo.Operator>, 13: <enum CAIRO_OPERATOR_SATURATE of type cairo.Operator>, 14: <enum CAIRO_OPERATOR_MULTIPLY of type cairo.Operator>, 15: <enum CAIRO_OPERATOR_SCREEN of type cairo.Operator>, 16: <enum CAIRO_OPERATOR_OVERLAY of type cairo.Operator>, 17: <enum CAIRO_OPERATOR_DARKEN of type cairo.Operator>, 18: <enum CAIRO_OPERATOR_LIGHTEN of type cairo.Operator>, 19: <enum CAIRO_OPERATOR_COLOR_DODGE of type cairo.Operator>, 20: <enum CAIRO_OPERATOR_COLOR_BURN of type cairo.Operator>, 21: <enum CAIRO_OPERATOR_HARD_LIGHT of type cairo.Operator>, 22: <enum CAIRO_OPERATOR_SOFT_LIGHT of type cairo.Operator>, 23: <enum CAIRO_OPERATOR_DIFFERENCE of type cairo.Operator>, 24: <enum CAIRO_OPERATOR_EXCLUSION of type cairo.Operator>, 25: <enum CAIRO_OPERATOR_HSL_HUE of type cairo.Operator>, 26: <enum CAIRO_OPERATOR_HSL_SATURATION of type cairo.Operator>, 27: <enum CAIRO_OPERATOR_HSL_COLOR of type cairo.Operator>, 28: <enum CAIRO_OPERATOR_HSL_LUMINOSITY of type cairo.Operator>}, '__info__': gi.EnumInfo(Operator), 'CLEAR': <enum CAIRO_OPERATOR_CLEAR of type cairo.Operator>, 'SOURCE': <enum CAIRO_OPERATOR_SOURCE of type cairo.Operator>, 'OVER': <enum CAIRO_OPERATOR_OVER of type cairo.Operator>, 'IN': <enum CAIRO_OPERATOR_IN of type cairo.Operator>, 'OUT': <enum CAIRO_OPERATOR_OUT of type cairo.Operator>, 'ATOP': <enum CAIRO_OPERATOR_ATOP of type cairo.Operator>, 'DEST': <enum CAIRO_OPERATOR_DEST of type cairo.Operator>, 'DEST_OVER': <enum CAIRO_OPERATOR_DEST_OVER of type cairo.Operator>, 'DEST_IN': <enum CAIRO_OPERATOR_DEST_IN of type cairo.Operator>, 'DEST_OUT': <enum CAIRO_OPERATOR_DEST_OUT of type cairo.Operator>, 'DEST_ATOP': <enum CAIRO_OPERATOR_DEST_ATOP of type cairo.Operator>, 'XOR': <enum CAIRO_OPERATOR_XOR of type cairo.Operator>, 'ADD': <enum CAIRO_OPERATOR_ADD of type cairo.Operator>, 'SATURATE': <enum CAIRO_OPERATOR_SATURATE of type cairo.Operator>, 'MULTIPLY': <enum CAIRO_OPERATOR_MULTIPLY of type cairo.Operator>, 'SCREEN': <enum CAIRO_OPERATOR_SCREEN of type cairo.Operator>, 'OVERLAY': <enum CAIRO_OPERATOR_OVERLAY of type cairo.Operator>, 'DARKEN': <enum CAIRO_OPERATOR_DARKEN of type cairo.Operator>, 'LIGHTEN': <enum CAIRO_OPERATOR_LIGHTEN of type cairo.Operator>, 'COLOR_DODGE': <enum CAIRO_OPERATOR_COLOR_DODGE of type cairo.Operator>, 'COLOR_BURN': <enum CAIRO_OPERATOR_COLOR_BURN of type cairo.Operator>, 'HARD_LIGHT': <enum CAIRO_OPERATOR_HARD_LIGHT of type cairo.Operator>, 'SOFT_LIGHT': <enum CAIRO_OPERATOR_SOFT_LIGHT of type cairo.Operator>, 'DIFFERENCE': <enum CAIRO_OPERATOR_DIFFERENCE of type cairo.Operator>, 'EXCLUSION': <enum CAIRO_OPERATOR_EXCLUSION of type cairo.Operator>, 'HSL_HUE': <enum CAIRO_OPERATOR_HSL_HUE of type cairo.Operator>, 'HSL_SATURATION': <enum CAIRO_OPERATOR_HSL_SATURATION of type cairo.Operator>, 'HSL_COLOR': <enum CAIRO_OPERATOR_HSL_COLOR of type cairo.Operator>, 'HSL_LUMINOSITY': <enum CAIRO_OPERATOR_HSL_LUMINOSITY of type cairo.Operator>})"
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
    }
    __gtype__ = None # (!) real value is '<GType cairo_operator_t (804005664)>'
    __info__ = gi.EnumInfo(Operator)


