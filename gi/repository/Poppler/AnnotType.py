# encoding: utf-8
# module gi.repository.Poppler
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Poppler-0.18.typelib
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
import gobject as __gobject


class AnnotType(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return a pair of integers, whose ratio is equal to the original int.
        
        The ratio is in lowest terms and has a positive denominator.
        
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

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Returns True. Exists for duck type compatibility with float.is_integer. """
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
        """ Convert to a string according to format_spec. """
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


    3D = 25
    CARET = 14
    CIRCLE = 6
    FILE_ATTACHMENT = 17
    FREE_TEXT = 3
    HIGHLIGHT = 9
    INK = 15
    LINE = 4
    LINK = 2
    MOVIE = 19
    POLYGON = 7
    POLY_LINE = 8
    POPUP = 16
    PRINTER_MARK = 22
    SCREEN = 21
    SOUND = 18
    SQUARE = 5
    SQUIGGLY = 11
    STAMP = 13
    STRIKE_OUT = 12
    TEXT = 1
    TRAP_NET = 23
    UNDERLINE = 10
    UNKNOWN = 0
    WATERMARK = 24
    WIDGET = 20
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Poppler', '__dict__': <attribute '__dict__' of 'AnnotType' objects>, '__doc__': None, '__gtype__': <GType PopplerAnnotType (3984429456)>, '__enum_values__': {0: <enum POPPLER_ANNOT_UNKNOWN of type Poppler.AnnotType>, 1: <enum POPPLER_ANNOT_TEXT of type Poppler.AnnotType>, 2: <enum POPPLER_ANNOT_LINK of type Poppler.AnnotType>, 3: <enum POPPLER_ANNOT_FREE_TEXT of type Poppler.AnnotType>, 4: <enum POPPLER_ANNOT_LINE of type Poppler.AnnotType>, 5: <enum POPPLER_ANNOT_SQUARE of type Poppler.AnnotType>, 6: <enum POPPLER_ANNOT_CIRCLE of type Poppler.AnnotType>, 7: <enum POPPLER_ANNOT_POLYGON of type Poppler.AnnotType>, 8: <enum POPPLER_ANNOT_POLY_LINE of type Poppler.AnnotType>, 9: <enum POPPLER_ANNOT_HIGHLIGHT of type Poppler.AnnotType>, 10: <enum POPPLER_ANNOT_UNDERLINE of type Poppler.AnnotType>, 11: <enum POPPLER_ANNOT_SQUIGGLY of type Poppler.AnnotType>, 12: <enum POPPLER_ANNOT_STRIKE_OUT of type Poppler.AnnotType>, 13: <enum POPPLER_ANNOT_STAMP of type Poppler.AnnotType>, 14: <enum POPPLER_ANNOT_CARET of type Poppler.AnnotType>, 15: <enum POPPLER_ANNOT_INK of type Poppler.AnnotType>, 16: <enum POPPLER_ANNOT_POPUP of type Poppler.AnnotType>, 17: <enum POPPLER_ANNOT_FILE_ATTACHMENT of type Poppler.AnnotType>, 18: <enum POPPLER_ANNOT_SOUND of type Poppler.AnnotType>, 19: <enum POPPLER_ANNOT_MOVIE of type Poppler.AnnotType>, 20: <enum POPPLER_ANNOT_WIDGET of type Poppler.AnnotType>, 21: <enum POPPLER_ANNOT_SCREEN of type Poppler.AnnotType>, 22: <enum POPPLER_ANNOT_PRINTER_MARK of type Poppler.AnnotType>, 23: <enum POPPLER_ANNOT_TRAP_NET of type Poppler.AnnotType>, 24: <enum POPPLER_ANNOT_WATERMARK of type Poppler.AnnotType>, 25: <enum POPPLER_ANNOT_3D of type Poppler.AnnotType>}, '__info__': gi.EnumInfo(AnnotType), 'UNKNOWN': <enum POPPLER_ANNOT_UNKNOWN of type Poppler.AnnotType>, 'TEXT': <enum POPPLER_ANNOT_TEXT of type Poppler.AnnotType>, 'LINK': <enum POPPLER_ANNOT_LINK of type Poppler.AnnotType>, 'FREE_TEXT': <enum POPPLER_ANNOT_FREE_TEXT of type Poppler.AnnotType>, 'LINE': <enum POPPLER_ANNOT_LINE of type Poppler.AnnotType>, 'SQUARE': <enum POPPLER_ANNOT_SQUARE of type Poppler.AnnotType>, 'CIRCLE': <enum POPPLER_ANNOT_CIRCLE of type Poppler.AnnotType>, 'POLYGON': <enum POPPLER_ANNOT_POLYGON of type Poppler.AnnotType>, 'POLY_LINE': <enum POPPLER_ANNOT_POLY_LINE of type Poppler.AnnotType>, 'HIGHLIGHT': <enum POPPLER_ANNOT_HIGHLIGHT of type Poppler.AnnotType>, 'UNDERLINE': <enum POPPLER_ANNOT_UNDERLINE of type Poppler.AnnotType>, 'SQUIGGLY': <enum POPPLER_ANNOT_SQUIGGLY of type Poppler.AnnotType>, 'STRIKE_OUT': <enum POPPLER_ANNOT_STRIKE_OUT of type Poppler.AnnotType>, 'STAMP': <enum POPPLER_ANNOT_STAMP of type Poppler.AnnotType>, 'CARET': <enum POPPLER_ANNOT_CARET of type Poppler.AnnotType>, 'INK': <enum POPPLER_ANNOT_INK of type Poppler.AnnotType>, 'POPUP': <enum POPPLER_ANNOT_POPUP of type Poppler.AnnotType>, 'FILE_ATTACHMENT': <enum POPPLER_ANNOT_FILE_ATTACHMENT of type Poppler.AnnotType>, 'SOUND': <enum POPPLER_ANNOT_SOUND of type Poppler.AnnotType>, 'MOVIE': <enum POPPLER_ANNOT_MOVIE of type Poppler.AnnotType>, 'WIDGET': <enum POPPLER_ANNOT_WIDGET of type Poppler.AnnotType>, 'SCREEN': <enum POPPLER_ANNOT_SCREEN of type Poppler.AnnotType>, 'PRINTER_MARK': <enum POPPLER_ANNOT_PRINTER_MARK of type Poppler.AnnotType>, 'TRAP_NET': <enum POPPLER_ANNOT_TRAP_NET of type Poppler.AnnotType>, 'WATERMARK': <enum POPPLER_ANNOT_WATERMARK of type Poppler.AnnotType>, '3D': <enum POPPLER_ANNOT_3D of type Poppler.AnnotType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PopplerAnnotType (3984429456)>'
    __info__ = gi.EnumInfo(AnnotType)


