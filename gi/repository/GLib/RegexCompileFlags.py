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


class RegexCompileFlags(__gobject.GFlags):
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
        """ Helper for pickle. """
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

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ANCHORED = 16
    BSR_ANYCRLF = 8388608
    CASELESS = 1
    DEFAULT = 0
    DOLLAR_ENDONLY = 32
    DOTALL = 4
    DUPNAMES = 524288
    EXTENDED = 8
    FIRSTLINE = 262144
    JAVASCRIPT_COMPAT = 33554432
    MULTILINE = 2
    NEWLINE_ANYCRLF = 5242880
    NEWLINE_CR = 1048576
    NEWLINE_CRLF = 3145728
    NEWLINE_LF = 2097152
    NO_AUTO_CAPTURE = 4096
    OPTIMIZE = 8192
    RAW = 2048
    UNGREEDY = 512
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'RegexCompileFlags' objects>, '__doc__': None, '__gtype__': <GType PyGLibRegexCompileFlags (163505552)>, '__flags_values__': {0: <flags 0 of type GLib.RegexCompileFlags>, 1: <flags G_REGEX_CASELESS of type GLib.RegexCompileFlags>, 2: <flags G_REGEX_MULTILINE of type GLib.RegexCompileFlags>, 4: <flags G_REGEX_DOTALL of type GLib.RegexCompileFlags>, 8: <flags G_REGEX_EXTENDED of type GLib.RegexCompileFlags>, 16: <flags G_REGEX_ANCHORED of type GLib.RegexCompileFlags>, 32: <flags G_REGEX_DOLLAR_ENDONLY of type GLib.RegexCompileFlags>, 512: <flags G_REGEX_UNGREEDY of type GLib.RegexCompileFlags>, 2048: <flags G_REGEX_RAW of type GLib.RegexCompileFlags>, 4096: <flags G_REGEX_NO_AUTO_CAPTURE of type GLib.RegexCompileFlags>, 8192: <flags G_REGEX_OPTIMIZE of type GLib.RegexCompileFlags>, 262144: <flags G_REGEX_FIRSTLINE of type GLib.RegexCompileFlags>, 524288: <flags G_REGEX_DUPNAMES of type GLib.RegexCompileFlags>, 1048576: <flags G_REGEX_NEWLINE_CR of type GLib.RegexCompileFlags>, 2097152: <flags G_REGEX_NEWLINE_LF of type GLib.RegexCompileFlags>, 3145728: <flags G_REGEX_NEWLINE_CR | G_REGEX_NEWLINE_LF | G_REGEX_NEWLINE_CRLF of type GLib.RegexCompileFlags>, 5242880: <flags G_REGEX_NEWLINE_CR | G_REGEX_NEWLINE_ANYCRLF of type GLib.RegexCompileFlags>, 8388608: <flags G_REGEX_BSR_ANYCRLF of type GLib.RegexCompileFlags>, 33554432: <flags G_REGEX_JAVASCRIPT_COMPAT of type GLib.RegexCompileFlags>}, '__info__': gi.EnumInfo(RegexCompileFlags), 'DEFAULT': <flags 0 of type GLib.RegexCompileFlags>, 'CASELESS': <flags G_REGEX_CASELESS of type GLib.RegexCompileFlags>, 'MULTILINE': <flags G_REGEX_MULTILINE of type GLib.RegexCompileFlags>, 'DOTALL': <flags G_REGEX_DOTALL of type GLib.RegexCompileFlags>, 'EXTENDED': <flags G_REGEX_EXTENDED of type GLib.RegexCompileFlags>, 'ANCHORED': <flags G_REGEX_ANCHORED of type GLib.RegexCompileFlags>, 'DOLLAR_ENDONLY': <flags G_REGEX_DOLLAR_ENDONLY of type GLib.RegexCompileFlags>, 'UNGREEDY': <flags G_REGEX_UNGREEDY of type GLib.RegexCompileFlags>, 'RAW': <flags G_REGEX_RAW of type GLib.RegexCompileFlags>, 'NO_AUTO_CAPTURE': <flags G_REGEX_NO_AUTO_CAPTURE of type GLib.RegexCompileFlags>, 'OPTIMIZE': <flags G_REGEX_OPTIMIZE of type GLib.RegexCompileFlags>, 'FIRSTLINE': <flags G_REGEX_FIRSTLINE of type GLib.RegexCompileFlags>, 'DUPNAMES': <flags G_REGEX_DUPNAMES of type GLib.RegexCompileFlags>, 'NEWLINE_CR': <flags G_REGEX_NEWLINE_CR of type GLib.RegexCompileFlags>, 'NEWLINE_LF': <flags G_REGEX_NEWLINE_LF of type GLib.RegexCompileFlags>, 'NEWLINE_CRLF': <flags G_REGEX_NEWLINE_CR | G_REGEX_NEWLINE_LF | G_REGEX_NEWLINE_CRLF of type GLib.RegexCompileFlags>, 'NEWLINE_ANYCRLF': <flags G_REGEX_NEWLINE_CR | G_REGEX_NEWLINE_ANYCRLF of type GLib.RegexCompileFlags>, 'BSR_ANYCRLF': <flags G_REGEX_BSR_ANYCRLF of type GLib.RegexCompileFlags>, 'JAVASCRIPT_COMPAT': <flags G_REGEX_JAVASCRIPT_COMPAT of type GLib.RegexCompileFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        512: 512,
        2048: 2048,
        4096: 4096,
        8192: 8192,
        262144: 262144,
        524288: 524288,
        1048576: 1048576,
        2097152: 2097152,
        3145728: 3145728,
        5242880: 5242880,
        8388608: 8388608,
        33554432: 33554432,
    }
    __gtype__ = None # (!) real value is '<GType PyGLibRegexCompileFlags (163505552)>'
    __info__ = gi.EnumInfo(RegexCompileFlags)


