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


class unicode_general_category_t(__gobject.GEnum):
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.HarfBuzz', '__dict__': <attribute '__dict__' of 'unicode_general_category_t' objects>, '__doc__': None, '__gtype__': <GType PyHarfBuzzunicode_general_category_t (2667611472)>, '__enum_values__': {0: <enum HB_UNICODE_GENERAL_CATEGORY_CONTROL of type HarfBuzz.unicode_general_category_t>, 1: <enum HB_UNICODE_GENERAL_CATEGORY_FORMAT of type HarfBuzz.unicode_general_category_t>, 2: <enum HB_UNICODE_GENERAL_CATEGORY_UNASSIGNED of type HarfBuzz.unicode_general_category_t>, 3: <enum HB_UNICODE_GENERAL_CATEGORY_PRIVATE_USE of type HarfBuzz.unicode_general_category_t>, 4: <enum HB_UNICODE_GENERAL_CATEGORY_SURROGATE of type HarfBuzz.unicode_general_category_t>, 5: <enum HB_UNICODE_GENERAL_CATEGORY_LOWERCASE_LETTER of type HarfBuzz.unicode_general_category_t>, 6: <enum HB_UNICODE_GENERAL_CATEGORY_MODIFIER_LETTER of type HarfBuzz.unicode_general_category_t>, 7: <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_LETTER of type HarfBuzz.unicode_general_category_t>, 8: <enum HB_UNICODE_GENERAL_CATEGORY_TITLECASE_LETTER of type HarfBuzz.unicode_general_category_t>, 9: <enum HB_UNICODE_GENERAL_CATEGORY_UPPERCASE_LETTER of type HarfBuzz.unicode_general_category_t>, 10: <enum HB_UNICODE_GENERAL_CATEGORY_SPACING_MARK of type HarfBuzz.unicode_general_category_t>, 11: <enum HB_UNICODE_GENERAL_CATEGORY_ENCLOSING_MARK of type HarfBuzz.unicode_general_category_t>, 12: <enum HB_UNICODE_GENERAL_CATEGORY_NON_SPACING_MARK of type HarfBuzz.unicode_general_category_t>, 13: <enum HB_UNICODE_GENERAL_CATEGORY_DECIMAL_NUMBER of type HarfBuzz.unicode_general_category_t>, 14: <enum HB_UNICODE_GENERAL_CATEGORY_LETTER_NUMBER of type HarfBuzz.unicode_general_category_t>, 15: <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_NUMBER of type HarfBuzz.unicode_general_category_t>, 16: <enum HB_UNICODE_GENERAL_CATEGORY_CONNECT_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 17: <enum HB_UNICODE_GENERAL_CATEGORY_DASH_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 18: <enum HB_UNICODE_GENERAL_CATEGORY_CLOSE_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 19: <enum HB_UNICODE_GENERAL_CATEGORY_FINAL_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 20: <enum HB_UNICODE_GENERAL_CATEGORY_INITIAL_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 21: <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 22: <enum HB_UNICODE_GENERAL_CATEGORY_OPEN_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 23: <enum HB_UNICODE_GENERAL_CATEGORY_CURRENCY_SYMBOL of type HarfBuzz.unicode_general_category_t>, 24: <enum HB_UNICODE_GENERAL_CATEGORY_MODIFIER_SYMBOL of type HarfBuzz.unicode_general_category_t>, 25: <enum HB_UNICODE_GENERAL_CATEGORY_MATH_SYMBOL of type HarfBuzz.unicode_general_category_t>, 26: <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_SYMBOL of type HarfBuzz.unicode_general_category_t>, 27: <enum HB_UNICODE_GENERAL_CATEGORY_LINE_SEPARATOR of type HarfBuzz.unicode_general_category_t>, 28: <enum HB_UNICODE_GENERAL_CATEGORY_PARAGRAPH_SEPARATOR of type HarfBuzz.unicode_general_category_t>, 29: <enum HB_UNICODE_GENERAL_CATEGORY_SPACE_SEPARATOR of type HarfBuzz.unicode_general_category_t>}, '__info__': gi.EnumInfo(unicode_general_category_t), 'CONTROL': <enum HB_UNICODE_GENERAL_CATEGORY_CONTROL of type HarfBuzz.unicode_general_category_t>, 'FORMAT': <enum HB_UNICODE_GENERAL_CATEGORY_FORMAT of type HarfBuzz.unicode_general_category_t>, 'UNASSIGNED': <enum HB_UNICODE_GENERAL_CATEGORY_UNASSIGNED of type HarfBuzz.unicode_general_category_t>, 'PRIVATE_USE': <enum HB_UNICODE_GENERAL_CATEGORY_PRIVATE_USE of type HarfBuzz.unicode_general_category_t>, 'SURROGATE': <enum HB_UNICODE_GENERAL_CATEGORY_SURROGATE of type HarfBuzz.unicode_general_category_t>, 'LOWERCASE_LETTER': <enum HB_UNICODE_GENERAL_CATEGORY_LOWERCASE_LETTER of type HarfBuzz.unicode_general_category_t>, 'MODIFIER_LETTER': <enum HB_UNICODE_GENERAL_CATEGORY_MODIFIER_LETTER of type HarfBuzz.unicode_general_category_t>, 'OTHER_LETTER': <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_LETTER of type HarfBuzz.unicode_general_category_t>, 'TITLECASE_LETTER': <enum HB_UNICODE_GENERAL_CATEGORY_TITLECASE_LETTER of type HarfBuzz.unicode_general_category_t>, 'UPPERCASE_LETTER': <enum HB_UNICODE_GENERAL_CATEGORY_UPPERCASE_LETTER of type HarfBuzz.unicode_general_category_t>, 'SPACING_MARK': <enum HB_UNICODE_GENERAL_CATEGORY_SPACING_MARK of type HarfBuzz.unicode_general_category_t>, 'ENCLOSING_MARK': <enum HB_UNICODE_GENERAL_CATEGORY_ENCLOSING_MARK of type HarfBuzz.unicode_general_category_t>, 'NON_SPACING_MARK': <enum HB_UNICODE_GENERAL_CATEGORY_NON_SPACING_MARK of type HarfBuzz.unicode_general_category_t>, 'DECIMAL_NUMBER': <enum HB_UNICODE_GENERAL_CATEGORY_DECIMAL_NUMBER of type HarfBuzz.unicode_general_category_t>, 'LETTER_NUMBER': <enum HB_UNICODE_GENERAL_CATEGORY_LETTER_NUMBER of type HarfBuzz.unicode_general_category_t>, 'OTHER_NUMBER': <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_NUMBER of type HarfBuzz.unicode_general_category_t>, 'CONNECT_PUNCTUATION': <enum HB_UNICODE_GENERAL_CATEGORY_CONNECT_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 'DASH_PUNCTUATION': <enum HB_UNICODE_GENERAL_CATEGORY_DASH_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 'CLOSE_PUNCTUATION': <enum HB_UNICODE_GENERAL_CATEGORY_CLOSE_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 'FINAL_PUNCTUATION': <enum HB_UNICODE_GENERAL_CATEGORY_FINAL_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 'INITIAL_PUNCTUATION': <enum HB_UNICODE_GENERAL_CATEGORY_INITIAL_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 'OTHER_PUNCTUATION': <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 'OPEN_PUNCTUATION': <enum HB_UNICODE_GENERAL_CATEGORY_OPEN_PUNCTUATION of type HarfBuzz.unicode_general_category_t>, 'CURRENCY_SYMBOL': <enum HB_UNICODE_GENERAL_CATEGORY_CURRENCY_SYMBOL of type HarfBuzz.unicode_general_category_t>, 'MODIFIER_SYMBOL': <enum HB_UNICODE_GENERAL_CATEGORY_MODIFIER_SYMBOL of type HarfBuzz.unicode_general_category_t>, 'MATH_SYMBOL': <enum HB_UNICODE_GENERAL_CATEGORY_MATH_SYMBOL of type HarfBuzz.unicode_general_category_t>, 'OTHER_SYMBOL': <enum HB_UNICODE_GENERAL_CATEGORY_OTHER_SYMBOL of type HarfBuzz.unicode_general_category_t>, 'LINE_SEPARATOR': <enum HB_UNICODE_GENERAL_CATEGORY_LINE_SEPARATOR of type HarfBuzz.unicode_general_category_t>, 'PARAGRAPH_SEPARATOR': <enum HB_UNICODE_GENERAL_CATEGORY_PARAGRAPH_SEPARATOR of type HarfBuzz.unicode_general_category_t>, 'SPACE_SEPARATOR': <enum HB_UNICODE_GENERAL_CATEGORY_SPACE_SEPARATOR of type HarfBuzz.unicode_general_category_t>})"
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
    __gtype__ = None # (!) real value is '<GType PyHarfBuzzunicode_general_category_t (2667611472)>'
    __info__ = gi.EnumInfo(unicode_general_category_t)


