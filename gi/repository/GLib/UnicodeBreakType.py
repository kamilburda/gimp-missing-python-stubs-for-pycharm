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


class UnicodeBreakType(__gobject.GEnum):
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


    AFTER = 10
    AKSARA = 43
    AKSARA_PRE_BASE = 44
    AKSARA_START = 45
    ALPHABETIC = 23
    AMBIGUOUS = 27
    BEFORE = 11
    BEFORE_AND_AFTER = 12
    CARRIAGE_RETURN = 1
    CLOSE_PARANTHESIS = 36
    CLOSE_PARENTHESIS = 36
    CLOSE_PUNCTUATION = 16
    COMBINING_MARK = 3
    COMPLEX_CONTEXT = 26
    CONDITIONAL_JAPANESE_STARTER = 37
    CONTINGENT = 8
    EMOJI_BASE = 40
    EMOJI_MODIFIER = 41
    EXCLAMATION = 18
    HANGUL_LVT_SYLLABLE = 35
    HANGUL_LV_SYLLABLE = 34
    HANGUL_L_JAMO = 31
    HANGUL_T_JAMO = 33
    HANGUL_V_JAMO = 32
    HEBREW_LETTER = 38
    HYPHEN = 13
    IDEOGRAPHIC = 19
    INFIX_SEPARATOR = 21
    INSEPARABLE = 6
    LINE_FEED = 2
    MANDATORY = 0
    NEXT_LINE = 29
    NON_BREAKING_GLUE = 7
    NON_STARTER = 14
    NUMERIC = 20
    OPEN_PUNCTUATION = 15
    POSTFIX = 25
    PREFIX = 24
    QUOTATION = 17
    REGIONAL_INDICATOR = 39
    SPACE = 9
    SURROGATE = 4
    SYMBOL = 22
    UNKNOWN = 28
    VIRAMA = 47
    VIRAMA_FINAL = 46
    WORD_JOINER = 30
    ZERO_WIDTH_JOINER = 42
    ZERO_WIDTH_SPACE = 5
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'UnicodeBreakType' objects>, '__doc__': None, '__gtype__': <GType GUnicodeBreakType (163509360)>, '__enum_values__': {0: <enum G_UNICODE_BREAK_MANDATORY of type GLib.UnicodeBreakType>, 1: <enum G_UNICODE_BREAK_CARRIAGE_RETURN of type GLib.UnicodeBreakType>, 2: <enum G_UNICODE_BREAK_LINE_FEED of type GLib.UnicodeBreakType>, 3: <enum G_UNICODE_BREAK_COMBINING_MARK of type GLib.UnicodeBreakType>, 4: <enum G_UNICODE_BREAK_SURROGATE of type GLib.UnicodeBreakType>, 5: <enum G_UNICODE_BREAK_ZERO_WIDTH_SPACE of type GLib.UnicodeBreakType>, 6: <enum G_UNICODE_BREAK_INSEPARABLE of type GLib.UnicodeBreakType>, 7: <enum G_UNICODE_BREAK_NON_BREAKING_GLUE of type GLib.UnicodeBreakType>, 8: <enum G_UNICODE_BREAK_CONTINGENT of type GLib.UnicodeBreakType>, 9: <enum G_UNICODE_BREAK_SPACE of type GLib.UnicodeBreakType>, 10: <enum G_UNICODE_BREAK_AFTER of type GLib.UnicodeBreakType>, 11: <enum G_UNICODE_BREAK_BEFORE of type GLib.UnicodeBreakType>, 12: <enum G_UNICODE_BREAK_BEFORE_AND_AFTER of type GLib.UnicodeBreakType>, 13: <enum G_UNICODE_BREAK_HYPHEN of type GLib.UnicodeBreakType>, 14: <enum G_UNICODE_BREAK_NON_STARTER of type GLib.UnicodeBreakType>, 15: <enum G_UNICODE_BREAK_OPEN_PUNCTUATION of type GLib.UnicodeBreakType>, 16: <enum G_UNICODE_BREAK_CLOSE_PUNCTUATION of type GLib.UnicodeBreakType>, 17: <enum G_UNICODE_BREAK_QUOTATION of type GLib.UnicodeBreakType>, 18: <enum G_UNICODE_BREAK_EXCLAMATION of type GLib.UnicodeBreakType>, 19: <enum G_UNICODE_BREAK_IDEOGRAPHIC of type GLib.UnicodeBreakType>, 20: <enum G_UNICODE_BREAK_NUMERIC of type GLib.UnicodeBreakType>, 21: <enum G_UNICODE_BREAK_INFIX_SEPARATOR of type GLib.UnicodeBreakType>, 22: <enum G_UNICODE_BREAK_SYMBOL of type GLib.UnicodeBreakType>, 23: <enum G_UNICODE_BREAK_ALPHABETIC of type GLib.UnicodeBreakType>, 24: <enum G_UNICODE_BREAK_PREFIX of type GLib.UnicodeBreakType>, 25: <enum G_UNICODE_BREAK_POSTFIX of type GLib.UnicodeBreakType>, 26: <enum G_UNICODE_BREAK_COMPLEX_CONTEXT of type GLib.UnicodeBreakType>, 27: <enum G_UNICODE_BREAK_AMBIGUOUS of type GLib.UnicodeBreakType>, 28: <enum G_UNICODE_BREAK_UNKNOWN of type GLib.UnicodeBreakType>, 29: <enum G_UNICODE_BREAK_NEXT_LINE of type GLib.UnicodeBreakType>, 30: <enum G_UNICODE_BREAK_WORD_JOINER of type GLib.UnicodeBreakType>, 31: <enum G_UNICODE_BREAK_HANGUL_L_JAMO of type GLib.UnicodeBreakType>, 32: <enum G_UNICODE_BREAK_HANGUL_V_JAMO of type GLib.UnicodeBreakType>, 33: <enum G_UNICODE_BREAK_HANGUL_T_JAMO of type GLib.UnicodeBreakType>, 34: <enum G_UNICODE_BREAK_HANGUL_LV_SYLLABLE of type GLib.UnicodeBreakType>, 35: <enum G_UNICODE_BREAK_HANGUL_LVT_SYLLABLE of type GLib.UnicodeBreakType>, 36: <enum G_UNICODE_BREAK_CLOSE_PARANTHESIS of type GLib.UnicodeBreakType>, 37: <enum G_UNICODE_BREAK_CONDITIONAL_JAPANESE_STARTER of type GLib.UnicodeBreakType>, 38: <enum G_UNICODE_BREAK_HEBREW_LETTER of type GLib.UnicodeBreakType>, 39: <enum G_UNICODE_BREAK_REGIONAL_INDICATOR of type GLib.UnicodeBreakType>, 40: <enum G_UNICODE_BREAK_EMOJI_BASE of type GLib.UnicodeBreakType>, 41: <enum G_UNICODE_BREAK_EMOJI_MODIFIER of type GLib.UnicodeBreakType>, 42: <enum G_UNICODE_BREAK_ZERO_WIDTH_JOINER of type GLib.UnicodeBreakType>, 43: <enum G_UNICODE_BREAK_AKSARA of type GLib.UnicodeBreakType>, 44: <enum G_UNICODE_BREAK_AKSARA_PRE_BASE of type GLib.UnicodeBreakType>, 45: <enum G_UNICODE_BREAK_AKSARA_START of type GLib.UnicodeBreakType>, 46: <enum G_UNICODE_BREAK_VIRAMA_FINAL of type GLib.UnicodeBreakType>, 47: <enum G_UNICODE_BREAK_VIRAMA of type GLib.UnicodeBreakType>}, '__info__': gi.EnumInfo(UnicodeBreakType), 'MANDATORY': <enum G_UNICODE_BREAK_MANDATORY of type GLib.UnicodeBreakType>, 'CARRIAGE_RETURN': <enum G_UNICODE_BREAK_CARRIAGE_RETURN of type GLib.UnicodeBreakType>, 'LINE_FEED': <enum G_UNICODE_BREAK_LINE_FEED of type GLib.UnicodeBreakType>, 'COMBINING_MARK': <enum G_UNICODE_BREAK_COMBINING_MARK of type GLib.UnicodeBreakType>, 'SURROGATE': <enum G_UNICODE_BREAK_SURROGATE of type GLib.UnicodeBreakType>, 'ZERO_WIDTH_SPACE': <enum G_UNICODE_BREAK_ZERO_WIDTH_SPACE of type GLib.UnicodeBreakType>, 'INSEPARABLE': <enum G_UNICODE_BREAK_INSEPARABLE of type GLib.UnicodeBreakType>, 'NON_BREAKING_GLUE': <enum G_UNICODE_BREAK_NON_BREAKING_GLUE of type GLib.UnicodeBreakType>, 'CONTINGENT': <enum G_UNICODE_BREAK_CONTINGENT of type GLib.UnicodeBreakType>, 'SPACE': <enum G_UNICODE_BREAK_SPACE of type GLib.UnicodeBreakType>, 'AFTER': <enum G_UNICODE_BREAK_AFTER of type GLib.UnicodeBreakType>, 'BEFORE': <enum G_UNICODE_BREAK_BEFORE of type GLib.UnicodeBreakType>, 'BEFORE_AND_AFTER': <enum G_UNICODE_BREAK_BEFORE_AND_AFTER of type GLib.UnicodeBreakType>, 'HYPHEN': <enum G_UNICODE_BREAK_HYPHEN of type GLib.UnicodeBreakType>, 'NON_STARTER': <enum G_UNICODE_BREAK_NON_STARTER of type GLib.UnicodeBreakType>, 'OPEN_PUNCTUATION': <enum G_UNICODE_BREAK_OPEN_PUNCTUATION of type GLib.UnicodeBreakType>, 'CLOSE_PUNCTUATION': <enum G_UNICODE_BREAK_CLOSE_PUNCTUATION of type GLib.UnicodeBreakType>, 'QUOTATION': <enum G_UNICODE_BREAK_QUOTATION of type GLib.UnicodeBreakType>, 'EXCLAMATION': <enum G_UNICODE_BREAK_EXCLAMATION of type GLib.UnicodeBreakType>, 'IDEOGRAPHIC': <enum G_UNICODE_BREAK_IDEOGRAPHIC of type GLib.UnicodeBreakType>, 'NUMERIC': <enum G_UNICODE_BREAK_NUMERIC of type GLib.UnicodeBreakType>, 'INFIX_SEPARATOR': <enum G_UNICODE_BREAK_INFIX_SEPARATOR of type GLib.UnicodeBreakType>, 'SYMBOL': <enum G_UNICODE_BREAK_SYMBOL of type GLib.UnicodeBreakType>, 'ALPHABETIC': <enum G_UNICODE_BREAK_ALPHABETIC of type GLib.UnicodeBreakType>, 'PREFIX': <enum G_UNICODE_BREAK_PREFIX of type GLib.UnicodeBreakType>, 'POSTFIX': <enum G_UNICODE_BREAK_POSTFIX of type GLib.UnicodeBreakType>, 'COMPLEX_CONTEXT': <enum G_UNICODE_BREAK_COMPLEX_CONTEXT of type GLib.UnicodeBreakType>, 'AMBIGUOUS': <enum G_UNICODE_BREAK_AMBIGUOUS of type GLib.UnicodeBreakType>, 'UNKNOWN': <enum G_UNICODE_BREAK_UNKNOWN of type GLib.UnicodeBreakType>, 'NEXT_LINE': <enum G_UNICODE_BREAK_NEXT_LINE of type GLib.UnicodeBreakType>, 'WORD_JOINER': <enum G_UNICODE_BREAK_WORD_JOINER of type GLib.UnicodeBreakType>, 'HANGUL_L_JAMO': <enum G_UNICODE_BREAK_HANGUL_L_JAMO of type GLib.UnicodeBreakType>, 'HANGUL_V_JAMO': <enum G_UNICODE_BREAK_HANGUL_V_JAMO of type GLib.UnicodeBreakType>, 'HANGUL_T_JAMO': <enum G_UNICODE_BREAK_HANGUL_T_JAMO of type GLib.UnicodeBreakType>, 'HANGUL_LV_SYLLABLE': <enum G_UNICODE_BREAK_HANGUL_LV_SYLLABLE of type GLib.UnicodeBreakType>, 'HANGUL_LVT_SYLLABLE': <enum G_UNICODE_BREAK_HANGUL_LVT_SYLLABLE of type GLib.UnicodeBreakType>, 'CLOSE_PARANTHESIS': <enum G_UNICODE_BREAK_CLOSE_PARANTHESIS of type GLib.UnicodeBreakType>, 'CLOSE_PARENTHESIS': <enum G_UNICODE_BREAK_CLOSE_PARANTHESIS of type GLib.UnicodeBreakType>, 'CONDITIONAL_JAPANESE_STARTER': <enum G_UNICODE_BREAK_CONDITIONAL_JAPANESE_STARTER of type GLib.UnicodeBreakType>, 'HEBREW_LETTER': <enum G_UNICODE_BREAK_HEBREW_LETTER of type GLib.UnicodeBreakType>, 'REGIONAL_INDICATOR': <enum G_UNICODE_BREAK_REGIONAL_INDICATOR of type GLib.UnicodeBreakType>, 'EMOJI_BASE': <enum G_UNICODE_BREAK_EMOJI_BASE of type GLib.UnicodeBreakType>, 'EMOJI_MODIFIER': <enum G_UNICODE_BREAK_EMOJI_MODIFIER of type GLib.UnicodeBreakType>, 'ZERO_WIDTH_JOINER': <enum G_UNICODE_BREAK_ZERO_WIDTH_JOINER of type GLib.UnicodeBreakType>, 'AKSARA': <enum G_UNICODE_BREAK_AKSARA of type GLib.UnicodeBreakType>, 'AKSARA_PRE_BASE': <enum G_UNICODE_BREAK_AKSARA_PRE_BASE of type GLib.UnicodeBreakType>, 'AKSARA_START': <enum G_UNICODE_BREAK_AKSARA_START of type GLib.UnicodeBreakType>, 'VIRAMA_FINAL': <enum G_UNICODE_BREAK_VIRAMA_FINAL of type GLib.UnicodeBreakType>, 'VIRAMA': <enum G_UNICODE_BREAK_VIRAMA of type GLib.UnicodeBreakType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType GUnicodeBreakType (163509360)>'
    __info__ = gi.EnumInfo(UnicodeBreakType)


