# encoding: utf-8
# module gi.repository.HarfBuzz
# from C:/Program Files/GIMP 3/lib/girepository-1.0\HarfBuzz-0.0.typelib
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


class unicode_combining_class_t(__gobject.GEnum):
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


    ABOVE = 230
    ABOVE_LEFT = 228
    ABOVE_RIGHT = 232
    ATTACHED_ABOVE = 214
    ATTACHED_ABOVE_RIGHT = 216
    ATTACHED_BELOW = 202
    ATTACHED_BELOW_LEFT = 200
    BELOW = 220
    BELOW_LEFT = 218
    BELOW_RIGHT = 222
    CCC10 = 10
    CCC103 = 103
    CCC107 = 107
    CCC11 = 11
    CCC118 = 118
    CCC12 = 12
    CCC122 = 122
    CCC129 = 129
    CCC13 = 13
    CCC130 = 130
    CCC132 = 132
    CCC14 = 14
    CCC15 = 15
    CCC16 = 16
    CCC17 = 17
    CCC18 = 18
    CCC19 = 19
    CCC20 = 20
    CCC21 = 21
    CCC22 = 22
    CCC23 = 23
    CCC24 = 24
    CCC25 = 25
    CCC26 = 26
    CCC27 = 27
    CCC28 = 28
    CCC29 = 29
    CCC30 = 30
    CCC31 = 31
    CCC32 = 32
    CCC33 = 33
    CCC34 = 34
    CCC35 = 35
    CCC36 = 36
    CCC84 = 84
    CCC91 = 91
    DOUBLE_ABOVE = 234
    DOUBLE_BELOW = 233
    INVALID = 255
    IOTA_SUBSCRIPT = 240
    KANA_VOICING = 8
    LEFT = 224
    NOT_REORDERED = 0
    NUKTA = 7
    OVERLAY = 1
    RIGHT = 226
    VIRAMA = 9
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.HarfBuzz', '__dict__': <attribute '__dict__' of 'unicode_combining_class_t' objects>, '__doc__': None, '__gtype__': <GType PyHarfBuzzunicode_combining_class_t (2667605088)>, '__enum_values__': {0: <enum HB_UNICODE_COMBINING_CLASS_NOT_REORDERED of type HarfBuzz.unicode_combining_class_t>, 1: <enum HB_UNICODE_COMBINING_CLASS_OVERLAY of type HarfBuzz.unicode_combining_class_t>, 7: <enum HB_UNICODE_COMBINING_CLASS_NUKTA of type HarfBuzz.unicode_combining_class_t>, 8: <enum HB_UNICODE_COMBINING_CLASS_KANA_VOICING of type HarfBuzz.unicode_combining_class_t>, 9: <enum HB_UNICODE_COMBINING_CLASS_VIRAMA of type HarfBuzz.unicode_combining_class_t>, 10: <enum HB_UNICODE_COMBINING_CLASS_CCC10 of type HarfBuzz.unicode_combining_class_t>, 11: <enum HB_UNICODE_COMBINING_CLASS_CCC11 of type HarfBuzz.unicode_combining_class_t>, 12: <enum HB_UNICODE_COMBINING_CLASS_CCC12 of type HarfBuzz.unicode_combining_class_t>, 13: <enum HB_UNICODE_COMBINING_CLASS_CCC13 of type HarfBuzz.unicode_combining_class_t>, 14: <enum HB_UNICODE_COMBINING_CLASS_CCC14 of type HarfBuzz.unicode_combining_class_t>, 15: <enum HB_UNICODE_COMBINING_CLASS_CCC15 of type HarfBuzz.unicode_combining_class_t>, 16: <enum HB_UNICODE_COMBINING_CLASS_CCC16 of type HarfBuzz.unicode_combining_class_t>, 17: <enum HB_UNICODE_COMBINING_CLASS_CCC17 of type HarfBuzz.unicode_combining_class_t>, 18: <enum HB_UNICODE_COMBINING_CLASS_CCC18 of type HarfBuzz.unicode_combining_class_t>, 19: <enum HB_UNICODE_COMBINING_CLASS_CCC19 of type HarfBuzz.unicode_combining_class_t>, 20: <enum HB_UNICODE_COMBINING_CLASS_CCC20 of type HarfBuzz.unicode_combining_class_t>, 21: <enum HB_UNICODE_COMBINING_CLASS_CCC21 of type HarfBuzz.unicode_combining_class_t>, 22: <enum HB_UNICODE_COMBINING_CLASS_CCC22 of type HarfBuzz.unicode_combining_class_t>, 23: <enum HB_UNICODE_COMBINING_CLASS_CCC23 of type HarfBuzz.unicode_combining_class_t>, 24: <enum HB_UNICODE_COMBINING_CLASS_CCC24 of type HarfBuzz.unicode_combining_class_t>, 25: <enum HB_UNICODE_COMBINING_CLASS_CCC25 of type HarfBuzz.unicode_combining_class_t>, 26: <enum HB_UNICODE_COMBINING_CLASS_CCC26 of type HarfBuzz.unicode_combining_class_t>, 27: <enum HB_UNICODE_COMBINING_CLASS_CCC27 of type HarfBuzz.unicode_combining_class_t>, 28: <enum HB_UNICODE_COMBINING_CLASS_CCC28 of type HarfBuzz.unicode_combining_class_t>, 29: <enum HB_UNICODE_COMBINING_CLASS_CCC29 of type HarfBuzz.unicode_combining_class_t>, 30: <enum HB_UNICODE_COMBINING_CLASS_CCC30 of type HarfBuzz.unicode_combining_class_t>, 31: <enum HB_UNICODE_COMBINING_CLASS_CCC31 of type HarfBuzz.unicode_combining_class_t>, 32: <enum HB_UNICODE_COMBINING_CLASS_CCC32 of type HarfBuzz.unicode_combining_class_t>, 33: <enum HB_UNICODE_COMBINING_CLASS_CCC33 of type HarfBuzz.unicode_combining_class_t>, 34: <enum HB_UNICODE_COMBINING_CLASS_CCC34 of type HarfBuzz.unicode_combining_class_t>, 35: <enum HB_UNICODE_COMBINING_CLASS_CCC35 of type HarfBuzz.unicode_combining_class_t>, 36: <enum HB_UNICODE_COMBINING_CLASS_CCC36 of type HarfBuzz.unicode_combining_class_t>, 84: <enum HB_UNICODE_COMBINING_CLASS_CCC84 of type HarfBuzz.unicode_combining_class_t>, 91: <enum HB_UNICODE_COMBINING_CLASS_CCC91 of type HarfBuzz.unicode_combining_class_t>, 103: <enum HB_UNICODE_COMBINING_CLASS_CCC103 of type HarfBuzz.unicode_combining_class_t>, 107: <enum HB_UNICODE_COMBINING_CLASS_CCC107 of type HarfBuzz.unicode_combining_class_t>, 118: <enum HB_UNICODE_COMBINING_CLASS_CCC118 of type HarfBuzz.unicode_combining_class_t>, 122: <enum HB_UNICODE_COMBINING_CLASS_CCC122 of type HarfBuzz.unicode_combining_class_t>, 129: <enum HB_UNICODE_COMBINING_CLASS_CCC129 of type HarfBuzz.unicode_combining_class_t>, 130: <enum HB_UNICODE_COMBINING_CLASS_CCC130 of type HarfBuzz.unicode_combining_class_t>, 132: <enum HB_UNICODE_COMBINING_CLASS_CCC132 of type HarfBuzz.unicode_combining_class_t>, 200: <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_BELOW_LEFT of type HarfBuzz.unicode_combining_class_t>, 202: <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_BELOW of type HarfBuzz.unicode_combining_class_t>, 214: <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_ABOVE of type HarfBuzz.unicode_combining_class_t>, 216: <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_ABOVE_RIGHT of type HarfBuzz.unicode_combining_class_t>, 218: <enum HB_UNICODE_COMBINING_CLASS_BELOW_LEFT of type HarfBuzz.unicode_combining_class_t>, 220: <enum HB_UNICODE_COMBINING_CLASS_BELOW of type HarfBuzz.unicode_combining_class_t>, 222: <enum HB_UNICODE_COMBINING_CLASS_BELOW_RIGHT of type HarfBuzz.unicode_combining_class_t>, 224: <enum HB_UNICODE_COMBINING_CLASS_LEFT of type HarfBuzz.unicode_combining_class_t>, 226: <enum HB_UNICODE_COMBINING_CLASS_RIGHT of type HarfBuzz.unicode_combining_class_t>, 228: <enum HB_UNICODE_COMBINING_CLASS_ABOVE_LEFT of type HarfBuzz.unicode_combining_class_t>, 230: <enum HB_UNICODE_COMBINING_CLASS_ABOVE of type HarfBuzz.unicode_combining_class_t>, 232: <enum HB_UNICODE_COMBINING_CLASS_ABOVE_RIGHT of type HarfBuzz.unicode_combining_class_t>, 233: <enum HB_UNICODE_COMBINING_CLASS_DOUBLE_BELOW of type HarfBuzz.unicode_combining_class_t>, 234: <enum HB_UNICODE_COMBINING_CLASS_DOUBLE_ABOVE of type HarfBuzz.unicode_combining_class_t>, 240: <enum HB_UNICODE_COMBINING_CLASS_IOTA_SUBSCRIPT of type HarfBuzz.unicode_combining_class_t>, 255: <enum HB_UNICODE_COMBINING_CLASS_INVALID of type HarfBuzz.unicode_combining_class_t>}, '__info__': gi.EnumInfo(unicode_combining_class_t), 'NOT_REORDERED': <enum HB_UNICODE_COMBINING_CLASS_NOT_REORDERED of type HarfBuzz.unicode_combining_class_t>, 'OVERLAY': <enum HB_UNICODE_COMBINING_CLASS_OVERLAY of type HarfBuzz.unicode_combining_class_t>, 'NUKTA': <enum HB_UNICODE_COMBINING_CLASS_NUKTA of type HarfBuzz.unicode_combining_class_t>, 'KANA_VOICING': <enum HB_UNICODE_COMBINING_CLASS_KANA_VOICING of type HarfBuzz.unicode_combining_class_t>, 'VIRAMA': <enum HB_UNICODE_COMBINING_CLASS_VIRAMA of type HarfBuzz.unicode_combining_class_t>, 'CCC10': <enum HB_UNICODE_COMBINING_CLASS_CCC10 of type HarfBuzz.unicode_combining_class_t>, 'CCC11': <enum HB_UNICODE_COMBINING_CLASS_CCC11 of type HarfBuzz.unicode_combining_class_t>, 'CCC12': <enum HB_UNICODE_COMBINING_CLASS_CCC12 of type HarfBuzz.unicode_combining_class_t>, 'CCC13': <enum HB_UNICODE_COMBINING_CLASS_CCC13 of type HarfBuzz.unicode_combining_class_t>, 'CCC14': <enum HB_UNICODE_COMBINING_CLASS_CCC14 of type HarfBuzz.unicode_combining_class_t>, 'CCC15': <enum HB_UNICODE_COMBINING_CLASS_CCC15 of type HarfBuzz.unicode_combining_class_t>, 'CCC16': <enum HB_UNICODE_COMBINING_CLASS_CCC16 of type HarfBuzz.unicode_combining_class_t>, 'CCC17': <enum HB_UNICODE_COMBINING_CLASS_CCC17 of type HarfBuzz.unicode_combining_class_t>, 'CCC18': <enum HB_UNICODE_COMBINING_CLASS_CCC18 of type HarfBuzz.unicode_combining_class_t>, 'CCC19': <enum HB_UNICODE_COMBINING_CLASS_CCC19 of type HarfBuzz.unicode_combining_class_t>, 'CCC20': <enum HB_UNICODE_COMBINING_CLASS_CCC20 of type HarfBuzz.unicode_combining_class_t>, 'CCC21': <enum HB_UNICODE_COMBINING_CLASS_CCC21 of type HarfBuzz.unicode_combining_class_t>, 'CCC22': <enum HB_UNICODE_COMBINING_CLASS_CCC22 of type HarfBuzz.unicode_combining_class_t>, 'CCC23': <enum HB_UNICODE_COMBINING_CLASS_CCC23 of type HarfBuzz.unicode_combining_class_t>, 'CCC24': <enum HB_UNICODE_COMBINING_CLASS_CCC24 of type HarfBuzz.unicode_combining_class_t>, 'CCC25': <enum HB_UNICODE_COMBINING_CLASS_CCC25 of type HarfBuzz.unicode_combining_class_t>, 'CCC26': <enum HB_UNICODE_COMBINING_CLASS_CCC26 of type HarfBuzz.unicode_combining_class_t>, 'CCC27': <enum HB_UNICODE_COMBINING_CLASS_CCC27 of type HarfBuzz.unicode_combining_class_t>, 'CCC28': <enum HB_UNICODE_COMBINING_CLASS_CCC28 of type HarfBuzz.unicode_combining_class_t>, 'CCC29': <enum HB_UNICODE_COMBINING_CLASS_CCC29 of type HarfBuzz.unicode_combining_class_t>, 'CCC30': <enum HB_UNICODE_COMBINING_CLASS_CCC30 of type HarfBuzz.unicode_combining_class_t>, 'CCC31': <enum HB_UNICODE_COMBINING_CLASS_CCC31 of type HarfBuzz.unicode_combining_class_t>, 'CCC32': <enum HB_UNICODE_COMBINING_CLASS_CCC32 of type HarfBuzz.unicode_combining_class_t>, 'CCC33': <enum HB_UNICODE_COMBINING_CLASS_CCC33 of type HarfBuzz.unicode_combining_class_t>, 'CCC34': <enum HB_UNICODE_COMBINING_CLASS_CCC34 of type HarfBuzz.unicode_combining_class_t>, 'CCC35': <enum HB_UNICODE_COMBINING_CLASS_CCC35 of type HarfBuzz.unicode_combining_class_t>, 'CCC36': <enum HB_UNICODE_COMBINING_CLASS_CCC36 of type HarfBuzz.unicode_combining_class_t>, 'CCC84': <enum HB_UNICODE_COMBINING_CLASS_CCC84 of type HarfBuzz.unicode_combining_class_t>, 'CCC91': <enum HB_UNICODE_COMBINING_CLASS_CCC91 of type HarfBuzz.unicode_combining_class_t>, 'CCC103': <enum HB_UNICODE_COMBINING_CLASS_CCC103 of type HarfBuzz.unicode_combining_class_t>, 'CCC107': <enum HB_UNICODE_COMBINING_CLASS_CCC107 of type HarfBuzz.unicode_combining_class_t>, 'CCC118': <enum HB_UNICODE_COMBINING_CLASS_CCC118 of type HarfBuzz.unicode_combining_class_t>, 'CCC122': <enum HB_UNICODE_COMBINING_CLASS_CCC122 of type HarfBuzz.unicode_combining_class_t>, 'CCC129': <enum HB_UNICODE_COMBINING_CLASS_CCC129 of type HarfBuzz.unicode_combining_class_t>, 'CCC130': <enum HB_UNICODE_COMBINING_CLASS_CCC130 of type HarfBuzz.unicode_combining_class_t>, 'CCC132': <enum HB_UNICODE_COMBINING_CLASS_CCC132 of type HarfBuzz.unicode_combining_class_t>, 'ATTACHED_BELOW_LEFT': <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_BELOW_LEFT of type HarfBuzz.unicode_combining_class_t>, 'ATTACHED_BELOW': <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_BELOW of type HarfBuzz.unicode_combining_class_t>, 'ATTACHED_ABOVE': <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_ABOVE of type HarfBuzz.unicode_combining_class_t>, 'ATTACHED_ABOVE_RIGHT': <enum HB_UNICODE_COMBINING_CLASS_ATTACHED_ABOVE_RIGHT of type HarfBuzz.unicode_combining_class_t>, 'BELOW_LEFT': <enum HB_UNICODE_COMBINING_CLASS_BELOW_LEFT of type HarfBuzz.unicode_combining_class_t>, 'BELOW': <enum HB_UNICODE_COMBINING_CLASS_BELOW of type HarfBuzz.unicode_combining_class_t>, 'BELOW_RIGHT': <enum HB_UNICODE_COMBINING_CLASS_BELOW_RIGHT of type HarfBuzz.unicode_combining_class_t>, 'LEFT': <enum HB_UNICODE_COMBINING_CLASS_LEFT of type HarfBuzz.unicode_combining_class_t>, 'RIGHT': <enum HB_UNICODE_COMBINING_CLASS_RIGHT of type HarfBuzz.unicode_combining_class_t>, 'ABOVE_LEFT': <enum HB_UNICODE_COMBINING_CLASS_ABOVE_LEFT of type HarfBuzz.unicode_combining_class_t>, 'ABOVE': <enum HB_UNICODE_COMBINING_CLASS_ABOVE of type HarfBuzz.unicode_combining_class_t>, 'ABOVE_RIGHT': <enum HB_UNICODE_COMBINING_CLASS_ABOVE_RIGHT of type HarfBuzz.unicode_combining_class_t>, 'DOUBLE_BELOW': <enum HB_UNICODE_COMBINING_CLASS_DOUBLE_BELOW of type HarfBuzz.unicode_combining_class_t>, 'DOUBLE_ABOVE': <enum HB_UNICODE_COMBINING_CLASS_DOUBLE_ABOVE of type HarfBuzz.unicode_combining_class_t>, 'IOTA_SUBSCRIPT': <enum HB_UNICODE_COMBINING_CLASS_IOTA_SUBSCRIPT of type HarfBuzz.unicode_combining_class_t>, 'INVALID': <enum HB_UNICODE_COMBINING_CLASS_INVALID of type HarfBuzz.unicode_combining_class_t>})"
    __enum_values__ = {
        0: 0,
        1: 1,
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
        84: 84,
        91: 91,
        103: 103,
        107: 107,
        118: 118,
        122: 122,
        129: 129,
        130: 130,
        132: 132,
        200: 200,
        202: 202,
        214: 214,
        216: 216,
        218: 218,
        220: 220,
        222: 222,
        224: 224,
        226: 226,
        228: 228,
        230: 230,
        232: 232,
        233: 233,
        234: 234,
        240: 240,
        255: 255,
    }
    __gtype__ = None # (!) real value is '<GType PyHarfBuzzunicode_combining_class_t (2667605088)>'
    __info__ = gi.EnumInfo(unicode_combining_class_t)


