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


class BidiType(__gobject.GEnum):
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

    def for_unichar(self, ch): # real signature unknown; restored from __doc__
        """ for_unichar(ch:str) -> Pango.BidiType """
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


    AL = 4
    AN = 11
    B = 15
    BN = 14
    CS = 12
    EN = 8
    ES = 9
    ET = 10
    FSI = 21
    L = 0
    LRE = 1
    LRI = 19
    LRO = 2
    NSM = 13
    ON = 18
    PDF = 7
    PDI = 22
    R = 3
    RLE = 5
    RLI = 20
    RLO = 6
    S = 16
    WS = 17
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Pango', '__dict__': <attribute '__dict__' of 'BidiType' objects>, '__doc__': None, '__gtype__': <GType PangoBidiType (4081758144)>, '__enum_values__': {0: <enum PANGO_BIDI_TYPE_L of type Pango.BidiType>, 1: <enum PANGO_BIDI_TYPE_LRE of type Pango.BidiType>, 2: <enum PANGO_BIDI_TYPE_LRO of type Pango.BidiType>, 3: <enum PANGO_BIDI_TYPE_R of type Pango.BidiType>, 4: <enum PANGO_BIDI_TYPE_AL of type Pango.BidiType>, 5: <enum PANGO_BIDI_TYPE_RLE of type Pango.BidiType>, 6: <enum PANGO_BIDI_TYPE_RLO of type Pango.BidiType>, 7: <enum PANGO_BIDI_TYPE_PDF of type Pango.BidiType>, 8: <enum PANGO_BIDI_TYPE_EN of type Pango.BidiType>, 9: <enum PANGO_BIDI_TYPE_ES of type Pango.BidiType>, 10: <enum PANGO_BIDI_TYPE_ET of type Pango.BidiType>, 11: <enum PANGO_BIDI_TYPE_AN of type Pango.BidiType>, 12: <enum PANGO_BIDI_TYPE_CS of type Pango.BidiType>, 13: <enum PANGO_BIDI_TYPE_NSM of type Pango.BidiType>, 14: <enum PANGO_BIDI_TYPE_BN of type Pango.BidiType>, 15: <enum PANGO_BIDI_TYPE_B of type Pango.BidiType>, 16: <enum PANGO_BIDI_TYPE_S of type Pango.BidiType>, 17: <enum PANGO_BIDI_TYPE_WS of type Pango.BidiType>, 18: <enum PANGO_BIDI_TYPE_ON of type Pango.BidiType>, 19: <enum PANGO_BIDI_TYPE_LRI of type Pango.BidiType>, 20: <enum PANGO_BIDI_TYPE_RLI of type Pango.BidiType>, 21: <enum PANGO_BIDI_TYPE_FSI of type Pango.BidiType>, 22: <enum PANGO_BIDI_TYPE_PDI of type Pango.BidiType>}, '__info__': gi.EnumInfo(BidiType), 'L': <enum PANGO_BIDI_TYPE_L of type Pango.BidiType>, 'LRE': <enum PANGO_BIDI_TYPE_LRE of type Pango.BidiType>, 'LRO': <enum PANGO_BIDI_TYPE_LRO of type Pango.BidiType>, 'R': <enum PANGO_BIDI_TYPE_R of type Pango.BidiType>, 'AL': <enum PANGO_BIDI_TYPE_AL of type Pango.BidiType>, 'RLE': <enum PANGO_BIDI_TYPE_RLE of type Pango.BidiType>, 'RLO': <enum PANGO_BIDI_TYPE_RLO of type Pango.BidiType>, 'PDF': <enum PANGO_BIDI_TYPE_PDF of type Pango.BidiType>, 'EN': <enum PANGO_BIDI_TYPE_EN of type Pango.BidiType>, 'ES': <enum PANGO_BIDI_TYPE_ES of type Pango.BidiType>, 'ET': <enum PANGO_BIDI_TYPE_ET of type Pango.BidiType>, 'AN': <enum PANGO_BIDI_TYPE_AN of type Pango.BidiType>, 'CS': <enum PANGO_BIDI_TYPE_CS of type Pango.BidiType>, 'NSM': <enum PANGO_BIDI_TYPE_NSM of type Pango.BidiType>, 'BN': <enum PANGO_BIDI_TYPE_BN of type Pango.BidiType>, 'B': <enum PANGO_BIDI_TYPE_B of type Pango.BidiType>, 'S': <enum PANGO_BIDI_TYPE_S of type Pango.BidiType>, 'WS': <enum PANGO_BIDI_TYPE_WS of type Pango.BidiType>, 'ON': <enum PANGO_BIDI_TYPE_ON of type Pango.BidiType>, 'LRI': <enum PANGO_BIDI_TYPE_LRI of type Pango.BidiType>, 'RLI': <enum PANGO_BIDI_TYPE_RLI of type Pango.BidiType>, 'FSI': <enum PANGO_BIDI_TYPE_FSI of type Pango.BidiType>, 'PDI': <enum PANGO_BIDI_TYPE_PDI of type Pango.BidiType>, 'for_unichar': gi.FunctionInfo(for_unichar, bound=None)})"
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
    }
    __gtype__ = None # (!) real value is '<GType PangoBidiType (4081758144)>'
    __info__ = gi.EnumInfo(BidiType)


