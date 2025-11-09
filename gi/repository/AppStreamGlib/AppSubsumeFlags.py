# encoding: utf-8
# module gi.repository.AppStreamGlib
# from C:/Program Files/GIMP 3/lib/girepository-1.0\AppStreamGlib-1.0.typelib
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


class AppSubsumeFlags(__gobject.GFlags):
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


    AGREEMENTS = 0
    BOTH_WAYS = 2
    BRANCH = 536870912
    BUNDLES = 32
    CATEGORIES = 512
    COMMENT = 4194304
    COMPULSORY = 4096
    CONTENT_RATINGS = 32768
    DESCRIPTION = 16777216
    DEVELOPER_NAME = 8388608
    EXTENDS = 2048
    FORMATS = 268435456
    ICONS = 131072
    KEYWORDS = 134217728
    KIND = 8
    KUDOS = 256
    LANGUAGES = 1048576
    LAUNCHABLES = 0
    METADATA = 33554432
    METADATA_LICENSE = 2147483648
    MIMETYPES = 262144
    NAME = 2097152
    NONE = 0
    NO_OVERWRITE = 1
    ORIGIN = 1073741824
    PERMISSIONS = 1024
    PROJECT_GROUP = 0
    PROJECT_LICENSE = 0
    PROVIDES = 65536
    RELEASES = 128
    REPLACE = 4
    REVIEWS = 16384
    SCREENSHOTS = 8192
    SOURCE_KIND = 0
    STATE = 16
    SUGGESTS = 0
    TRANSLATIONS = 64
    URL = 67108864
    VETOS = 524288
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.AppStreamGlib', '__dict__': <attribute '__dict__' of 'AppSubsumeFlags' objects>, '__doc__': None, '__gtype__': <GType PyAppStreamGlibAppSubsumeFlags (3189448816)>, '__flags_values__': {0: <flags 0 of type AppStreamGlib.AppSubsumeFlags>, 1: <flags AS_APP_SUBSUME_FLAG_NO_OVERWRITE of type AppStreamGlib.AppSubsumeFlags>, 2: <flags AS_APP_SUBSUME_FLAG_BOTH_WAYS of type AppStreamGlib.AppSubsumeFlags>, 4: <flags AS_APP_SUBSUME_FLAG_REPLACE of type AppStreamGlib.AppSubsumeFlags>, 8: <flags AS_APP_SUBSUME_FLAG_KIND of type AppStreamGlib.AppSubsumeFlags>, 16: <flags AS_APP_SUBSUME_FLAG_STATE of type AppStreamGlib.AppSubsumeFlags>, 32: <flags AS_APP_SUBSUME_FLAG_BUNDLES of type AppStreamGlib.AppSubsumeFlags>, 64: <flags AS_APP_SUBSUME_FLAG_TRANSLATIONS of type AppStreamGlib.AppSubsumeFlags>, 128: <flags AS_APP_SUBSUME_FLAG_RELEASES of type AppStreamGlib.AppSubsumeFlags>, 256: <flags AS_APP_SUBSUME_FLAG_KUDOS of type AppStreamGlib.AppSubsumeFlags>, 512: <flags AS_APP_SUBSUME_FLAG_CATEGORIES of type AppStreamGlib.AppSubsumeFlags>, 1024: <flags AS_APP_SUBSUME_FLAG_PERMISSIONS of type AppStreamGlib.AppSubsumeFlags>, 2048: <flags AS_APP_SUBSUME_FLAG_EXTENDS of type AppStreamGlib.AppSubsumeFlags>, 4096: <flags AS_APP_SUBSUME_FLAG_COMPULSORY of type AppStreamGlib.AppSubsumeFlags>, 8192: <flags AS_APP_SUBSUME_FLAG_SCREENSHOTS of type AppStreamGlib.AppSubsumeFlags>, 16384: <flags AS_APP_SUBSUME_FLAG_REVIEWS of type AppStreamGlib.AppSubsumeFlags>, 32768: <flags AS_APP_SUBSUME_FLAG_CONTENT_RATINGS of type AppStreamGlib.AppSubsumeFlags>, 65536: <flags AS_APP_SUBSUME_FLAG_PROVIDES of type AppStreamGlib.AppSubsumeFlags>, 131072: <flags AS_APP_SUBSUME_FLAG_ICONS of type AppStreamGlib.AppSubsumeFlags>, 262144: <flags AS_APP_SUBSUME_FLAG_MIMETYPES of type AppStreamGlib.AppSubsumeFlags>, 524288: <flags AS_APP_SUBSUME_FLAG_VETOS of type AppStreamGlib.AppSubsumeFlags>, 1048576: <flags AS_APP_SUBSUME_FLAG_LANGUAGES of type AppStreamGlib.AppSubsumeFlags>, 2097152: <flags AS_APP_SUBSUME_FLAG_NAME of type AppStreamGlib.AppSubsumeFlags>, 4194304: <flags AS_APP_SUBSUME_FLAG_COMMENT of type AppStreamGlib.AppSubsumeFlags>, 8388608: <flags AS_APP_SUBSUME_FLAG_DEVELOPER_NAME of type AppStreamGlib.AppSubsumeFlags>, 16777216: <flags AS_APP_SUBSUME_FLAG_DESCRIPTION of type AppStreamGlib.AppSubsumeFlags>, 33554432: <flags AS_APP_SUBSUME_FLAG_METADATA of type AppStreamGlib.AppSubsumeFlags>, 67108864: <flags AS_APP_SUBSUME_FLAG_URL of type AppStreamGlib.AppSubsumeFlags>, 134217728: <flags AS_APP_SUBSUME_FLAG_KEYWORDS of type AppStreamGlib.AppSubsumeFlags>, 268435456: <flags AS_APP_SUBSUME_FLAG_FORMATS of type AppStreamGlib.AppSubsumeFlags>, 536870912: <flags AS_APP_SUBSUME_FLAG_BRANCH of type AppStreamGlib.AppSubsumeFlags>, 1073741824: <flags AS_APP_SUBSUME_FLAG_ORIGIN of type AppStreamGlib.AppSubsumeFlags>, 2147483648: <flags AS_APP_SUBSUME_FLAG_METADATA_LICENSE of type AppStreamGlib.AppSubsumeFlags>}, '__info__': gi.EnumInfo(AppSubsumeFlags), 'NONE': <flags 0 of type AppStreamGlib.AppSubsumeFlags>, 'NO_OVERWRITE': <flags AS_APP_SUBSUME_FLAG_NO_OVERWRITE of type AppStreamGlib.AppSubsumeFlags>, 'BOTH_WAYS': <flags AS_APP_SUBSUME_FLAG_BOTH_WAYS of type AppStreamGlib.AppSubsumeFlags>, 'REPLACE': <flags AS_APP_SUBSUME_FLAG_REPLACE of type AppStreamGlib.AppSubsumeFlags>, 'KIND': <flags AS_APP_SUBSUME_FLAG_KIND of type AppStreamGlib.AppSubsumeFlags>, 'STATE': <flags AS_APP_SUBSUME_FLAG_STATE of type AppStreamGlib.AppSubsumeFlags>, 'BUNDLES': <flags AS_APP_SUBSUME_FLAG_BUNDLES of type AppStreamGlib.AppSubsumeFlags>, 'TRANSLATIONS': <flags AS_APP_SUBSUME_FLAG_TRANSLATIONS of type AppStreamGlib.AppSubsumeFlags>, 'RELEASES': <flags AS_APP_SUBSUME_FLAG_RELEASES of type AppStreamGlib.AppSubsumeFlags>, 'KUDOS': <flags AS_APP_SUBSUME_FLAG_KUDOS of type AppStreamGlib.AppSubsumeFlags>, 'CATEGORIES': <flags AS_APP_SUBSUME_FLAG_CATEGORIES of type AppStreamGlib.AppSubsumeFlags>, 'PERMISSIONS': <flags AS_APP_SUBSUME_FLAG_PERMISSIONS of type AppStreamGlib.AppSubsumeFlags>, 'EXTENDS': <flags AS_APP_SUBSUME_FLAG_EXTENDS of type AppStreamGlib.AppSubsumeFlags>, 'COMPULSORY': <flags AS_APP_SUBSUME_FLAG_COMPULSORY of type AppStreamGlib.AppSubsumeFlags>, 'SCREENSHOTS': <flags AS_APP_SUBSUME_FLAG_SCREENSHOTS of type AppStreamGlib.AppSubsumeFlags>, 'REVIEWS': <flags AS_APP_SUBSUME_FLAG_REVIEWS of type AppStreamGlib.AppSubsumeFlags>, 'CONTENT_RATINGS': <flags AS_APP_SUBSUME_FLAG_CONTENT_RATINGS of type AppStreamGlib.AppSubsumeFlags>, 'PROVIDES': <flags AS_APP_SUBSUME_FLAG_PROVIDES of type AppStreamGlib.AppSubsumeFlags>, 'ICONS': <flags AS_APP_SUBSUME_FLAG_ICONS of type AppStreamGlib.AppSubsumeFlags>, 'MIMETYPES': <flags AS_APP_SUBSUME_FLAG_MIMETYPES of type AppStreamGlib.AppSubsumeFlags>, 'VETOS': <flags AS_APP_SUBSUME_FLAG_VETOS of type AppStreamGlib.AppSubsumeFlags>, 'LANGUAGES': <flags AS_APP_SUBSUME_FLAG_LANGUAGES of type AppStreamGlib.AppSubsumeFlags>, 'NAME': <flags AS_APP_SUBSUME_FLAG_NAME of type AppStreamGlib.AppSubsumeFlags>, 'COMMENT': <flags AS_APP_SUBSUME_FLAG_COMMENT of type AppStreamGlib.AppSubsumeFlags>, 'DEVELOPER_NAME': <flags AS_APP_SUBSUME_FLAG_DEVELOPER_NAME of type AppStreamGlib.AppSubsumeFlags>, 'DESCRIPTION': <flags AS_APP_SUBSUME_FLAG_DESCRIPTION of type AppStreamGlib.AppSubsumeFlags>, 'METADATA': <flags AS_APP_SUBSUME_FLAG_METADATA of type AppStreamGlib.AppSubsumeFlags>, 'URL': <flags AS_APP_SUBSUME_FLAG_URL of type AppStreamGlib.AppSubsumeFlags>, 'KEYWORDS': <flags AS_APP_SUBSUME_FLAG_KEYWORDS of type AppStreamGlib.AppSubsumeFlags>, 'FORMATS': <flags AS_APP_SUBSUME_FLAG_FORMATS of type AppStreamGlib.AppSubsumeFlags>, 'BRANCH': <flags AS_APP_SUBSUME_FLAG_BRANCH of type AppStreamGlib.AppSubsumeFlags>, 'ORIGIN': <flags AS_APP_SUBSUME_FLAG_ORIGIN of type AppStreamGlib.AppSubsumeFlags>, 'METADATA_LICENSE': <flags AS_APP_SUBSUME_FLAG_METADATA_LICENSE of type AppStreamGlib.AppSubsumeFlags>, 'PROJECT_LICENSE': <flags 0 of type AppStreamGlib.AppSubsumeFlags>, 'PROJECT_GROUP': <flags 0 of type AppStreamGlib.AppSubsumeFlags>, 'SOURCE_KIND': <flags 0 of type AppStreamGlib.AppSubsumeFlags>, 'SUGGESTS': <flags 0 of type AppStreamGlib.AppSubsumeFlags>, 'LAUNCHABLES': <flags 0 of type AppStreamGlib.AppSubsumeFlags>, 'AGREEMENTS': <flags 0 of type AppStreamGlib.AppSubsumeFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        128: 128,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        4096: 4096,
        8192: 8192,
        16384: 16384,
        32768: 32768,
        65536: 65536,
        131072: 131072,
        262144: 262144,
        524288: 524288,
        1048576: 1048576,
        2097152: 2097152,
        4194304: 4194304,
        8388608: 8388608,
        16777216: 16777216,
        33554432: 33554432,
        67108864: 67108864,
        134217728: 134217728,
        268435456: 268435456,
        536870912: 536870912,
        1073741824: 1073741824,
        2147483648: 2147483648,
    }
    __gtype__ = None # (!) real value is '<GType PyAppStreamGlibAppSubsumeFlags (3189448816)>'
    __info__ = gi.EnumInfo(AppSubsumeFlags)


