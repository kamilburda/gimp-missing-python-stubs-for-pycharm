# encoding: utf-8
# module gi.repository.GLib
# from C:/Program Files/GIMP 3/lib/girepository-1.0\GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # C:\Program Files\GIMP 3\lib\python3.12\site-packages\gi\_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class UnicodeType(__gobject.GEnum):
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


    CLOSE_PUNCTUATION = 18
    CONNECT_PUNCTUATION = 16
    CONTROL = 0
    CURRENCY_SYMBOL = 23
    DASH_PUNCTUATION = 17
    DECIMAL_NUMBER = 13
    ENCLOSING_MARK = 11
    FINAL_PUNCTUATION = 19
    FORMAT = 1
    INITIAL_PUNCTUATION = 20
    LETTER_NUMBER = 14
    LINE_SEPARATOR = 27
    LOWERCASE_LETTER = 5
    MATH_SYMBOL = 25
    MODIFIER_LETTER = 6
    MODIFIER_SYMBOL = 24
    NON_SPACING_MARK = 12
    OPEN_PUNCTUATION = 22
    OTHER_LETTER = 7
    OTHER_NUMBER = 15
    OTHER_PUNCTUATION = 21
    OTHER_SYMBOL = 26
    PARAGRAPH_SEPARATOR = 28
    PRIVATE_USE = 3
    SPACE_SEPARATOR = 29
    SPACING_MARK = 10
    SURROGATE = 4
    TITLECASE_LETTER = 8
    UNASSIGNED = 2
    UPPERCASE_LETTER = 9
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'UnicodeType' objects>, '__doc__': None, '__gtype__': <GType GUnicodeType (163509472)>, '__enum_values__': {0: <enum G_UNICODE_CONTROL of type GLib.UnicodeType>, 1: <enum G_UNICODE_FORMAT of type GLib.UnicodeType>, 2: <enum G_UNICODE_UNASSIGNED of type GLib.UnicodeType>, 3: <enum G_UNICODE_PRIVATE_USE of type GLib.UnicodeType>, 4: <enum G_UNICODE_SURROGATE of type GLib.UnicodeType>, 5: <enum G_UNICODE_LOWERCASE_LETTER of type GLib.UnicodeType>, 6: <enum G_UNICODE_MODIFIER_LETTER of type GLib.UnicodeType>, 7: <enum G_UNICODE_OTHER_LETTER of type GLib.UnicodeType>, 8: <enum G_UNICODE_TITLECASE_LETTER of type GLib.UnicodeType>, 9: <enum G_UNICODE_UPPERCASE_LETTER of type GLib.UnicodeType>, 10: <enum G_UNICODE_SPACING_MARK of type GLib.UnicodeType>, 11: <enum G_UNICODE_ENCLOSING_MARK of type GLib.UnicodeType>, 12: <enum G_UNICODE_NON_SPACING_MARK of type GLib.UnicodeType>, 13: <enum G_UNICODE_DECIMAL_NUMBER of type GLib.UnicodeType>, 14: <enum G_UNICODE_LETTER_NUMBER of type GLib.UnicodeType>, 15: <enum G_UNICODE_OTHER_NUMBER of type GLib.UnicodeType>, 16: <enum G_UNICODE_CONNECT_PUNCTUATION of type GLib.UnicodeType>, 17: <enum G_UNICODE_DASH_PUNCTUATION of type GLib.UnicodeType>, 18: <enum G_UNICODE_CLOSE_PUNCTUATION of type GLib.UnicodeType>, 19: <enum G_UNICODE_FINAL_PUNCTUATION of type GLib.UnicodeType>, 20: <enum G_UNICODE_INITIAL_PUNCTUATION of type GLib.UnicodeType>, 21: <enum G_UNICODE_OTHER_PUNCTUATION of type GLib.UnicodeType>, 22: <enum G_UNICODE_OPEN_PUNCTUATION of type GLib.UnicodeType>, 23: <enum G_UNICODE_CURRENCY_SYMBOL of type GLib.UnicodeType>, 24: <enum G_UNICODE_MODIFIER_SYMBOL of type GLib.UnicodeType>, 25: <enum G_UNICODE_MATH_SYMBOL of type GLib.UnicodeType>, 26: <enum G_UNICODE_OTHER_SYMBOL of type GLib.UnicodeType>, 27: <enum G_UNICODE_LINE_SEPARATOR of type GLib.UnicodeType>, 28: <enum G_UNICODE_PARAGRAPH_SEPARATOR of type GLib.UnicodeType>, 29: <enum G_UNICODE_SPACE_SEPARATOR of type GLib.UnicodeType>}, '__info__': gi.EnumInfo(UnicodeType), 'CONTROL': <enum G_UNICODE_CONTROL of type GLib.UnicodeType>, 'FORMAT': <enum G_UNICODE_FORMAT of type GLib.UnicodeType>, 'UNASSIGNED': <enum G_UNICODE_UNASSIGNED of type GLib.UnicodeType>, 'PRIVATE_USE': <enum G_UNICODE_PRIVATE_USE of type GLib.UnicodeType>, 'SURROGATE': <enum G_UNICODE_SURROGATE of type GLib.UnicodeType>, 'LOWERCASE_LETTER': <enum G_UNICODE_LOWERCASE_LETTER of type GLib.UnicodeType>, 'MODIFIER_LETTER': <enum G_UNICODE_MODIFIER_LETTER of type GLib.UnicodeType>, 'OTHER_LETTER': <enum G_UNICODE_OTHER_LETTER of type GLib.UnicodeType>, 'TITLECASE_LETTER': <enum G_UNICODE_TITLECASE_LETTER of type GLib.UnicodeType>, 'UPPERCASE_LETTER': <enum G_UNICODE_UPPERCASE_LETTER of type GLib.UnicodeType>, 'SPACING_MARK': <enum G_UNICODE_SPACING_MARK of type GLib.UnicodeType>, 'ENCLOSING_MARK': <enum G_UNICODE_ENCLOSING_MARK of type GLib.UnicodeType>, 'NON_SPACING_MARK': <enum G_UNICODE_NON_SPACING_MARK of type GLib.UnicodeType>, 'DECIMAL_NUMBER': <enum G_UNICODE_DECIMAL_NUMBER of type GLib.UnicodeType>, 'LETTER_NUMBER': <enum G_UNICODE_LETTER_NUMBER of type GLib.UnicodeType>, 'OTHER_NUMBER': <enum G_UNICODE_OTHER_NUMBER of type GLib.UnicodeType>, 'CONNECT_PUNCTUATION': <enum G_UNICODE_CONNECT_PUNCTUATION of type GLib.UnicodeType>, 'DASH_PUNCTUATION': <enum G_UNICODE_DASH_PUNCTUATION of type GLib.UnicodeType>, 'CLOSE_PUNCTUATION': <enum G_UNICODE_CLOSE_PUNCTUATION of type GLib.UnicodeType>, 'FINAL_PUNCTUATION': <enum G_UNICODE_FINAL_PUNCTUATION of type GLib.UnicodeType>, 'INITIAL_PUNCTUATION': <enum G_UNICODE_INITIAL_PUNCTUATION of type GLib.UnicodeType>, 'OTHER_PUNCTUATION': <enum G_UNICODE_OTHER_PUNCTUATION of type GLib.UnicodeType>, 'OPEN_PUNCTUATION': <enum G_UNICODE_OPEN_PUNCTUATION of type GLib.UnicodeType>, 'CURRENCY_SYMBOL': <enum G_UNICODE_CURRENCY_SYMBOL of type GLib.UnicodeType>, 'MODIFIER_SYMBOL': <enum G_UNICODE_MODIFIER_SYMBOL of type GLib.UnicodeType>, 'MATH_SYMBOL': <enum G_UNICODE_MATH_SYMBOL of type GLib.UnicodeType>, 'OTHER_SYMBOL': <enum G_UNICODE_OTHER_SYMBOL of type GLib.UnicodeType>, 'LINE_SEPARATOR': <enum G_UNICODE_LINE_SEPARATOR of type GLib.UnicodeType>, 'PARAGRAPH_SEPARATOR': <enum G_UNICODE_PARAGRAPH_SEPARATOR of type GLib.UnicodeType>, 'SPACE_SEPARATOR': <enum G_UNICODE_SPACE_SEPARATOR of type GLib.UnicodeType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType GUnicodeType (163509472)>'
    __info__ = gi.EnumInfo(UnicodeType)


