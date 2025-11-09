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


class Tag(__gobject.GEnum):
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


    AGREEMENT = 60
    AGREEMENT_SECTION = 61
    ARCH = 32
    ARCHITECTURES = 31
    BINARY = 66
    BUNDLE = 42
    CAPTION = 24
    CATEGORIES = 10
    CATEGORY = 11
    CHECKSUM = 46
    COMPONENT = 2
    COMPONENTS = 1
    COMPULSORY_FOR_DESKTOP = 22
    CONTENT_ATTRIBUTE = 50
    CONTENT_RATING = 49
    CUSTOM = 58
    DBUS = 68
    DESCRIPTION = 7
    DEVELOPER_NAME = 36
    EXTENDS = 35
    FONT = 67
    ICON = 9
    ID = 3
    IMAGE = 21
    KEYWORD = 13
    KEYWORDS = 12
    KUDO = 38
    KUDOS = 37
    LANG = 26
    LANGUAGES = 25
    LAUNCHABLE = 59
    LI = 63
    LIBRARY = 70
    LOCATION = 45
    METADATA = 27
    METADATA_LICENSE = 33
    MIMETYPE = 15
    MIMETYPES = 14
    MODALIAS = 69
    NAME = 5
    OL = 65
    P = 62
    PERMISSION = 44
    PERMISSIONS = 43
    PKGNAME = 4
    PRIORITY = 23
    PROJECT_GROUP = 16
    PROJECT_LICENSE = 17
    PROVIDES = 34
    RELEASE = 30
    RELEASES = 29
    REQUIRES = 57
    REVIEW = 53
    REVIEWER_ID = 55
    REVIEWER_NAME = 54
    REVIEWS = 52
    SCREENSHOT = 18
    SCREENSHOTS = 19
    SIZE = 47
    SOURCE_PKGNAME = 39
    SUGGESTS = 56
    SUMMARY = 6
    TRANSLATION = 48
    UL = 64
    UNKNOWN = 0
    UPDATE_CONTACT = 20
    URL = 8
    VALUE = 28
    VERSION = 51
    VETO = 41
    VETOS = 40
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.AppStreamGlib', '__dict__': <attribute '__dict__' of 'Tag' objects>, '__doc__': None, '__gtype__': <GType PyAppStreamGlibTag (3157403360)>, '__enum_values__': {0: <enum AS_TAG_UNKNOWN of type AppStreamGlib.Tag>, 1: <enum AS_TAG_COMPONENTS of type AppStreamGlib.Tag>, 2: <enum AS_TAG_COMPONENT of type AppStreamGlib.Tag>, 3: <enum AS_TAG_ID of type AppStreamGlib.Tag>, 4: <enum AS_TAG_PKGNAME of type AppStreamGlib.Tag>, 5: <enum AS_TAG_NAME of type AppStreamGlib.Tag>, 6: <enum AS_TAG_SUMMARY of type AppStreamGlib.Tag>, 7: <enum AS_TAG_DESCRIPTION of type AppStreamGlib.Tag>, 8: <enum AS_TAG_URL of type AppStreamGlib.Tag>, 9: <enum AS_TAG_ICON of type AppStreamGlib.Tag>, 10: <enum AS_TAG_CATEGORIES of type AppStreamGlib.Tag>, 11: <enum AS_TAG_CATEGORY of type AppStreamGlib.Tag>, 12: <enum AS_TAG_KEYWORDS of type AppStreamGlib.Tag>, 13: <enum AS_TAG_KEYWORD of type AppStreamGlib.Tag>, 14: <enum AS_TAG_MIMETYPES of type AppStreamGlib.Tag>, 15: <enum AS_TAG_MIMETYPE of type AppStreamGlib.Tag>, 16: <enum AS_TAG_PROJECT_GROUP of type AppStreamGlib.Tag>, 17: <enum AS_TAG_PROJECT_LICENSE of type AppStreamGlib.Tag>, 18: <enum AS_TAG_SCREENSHOT of type AppStreamGlib.Tag>, 19: <enum AS_TAG_SCREENSHOTS of type AppStreamGlib.Tag>, 20: <enum AS_TAG_UPDATE_CONTACT of type AppStreamGlib.Tag>, 21: <enum AS_TAG_IMAGE of type AppStreamGlib.Tag>, 22: <enum AS_TAG_COMPULSORY_FOR_DESKTOP of type AppStreamGlib.Tag>, 23: <enum AS_TAG_PRIORITY of type AppStreamGlib.Tag>, 24: <enum AS_TAG_CAPTION of type AppStreamGlib.Tag>, 25: <enum AS_TAG_LANGUAGES of type AppStreamGlib.Tag>, 26: <enum AS_TAG_LANG of type AppStreamGlib.Tag>, 27: <enum AS_TAG_METADATA of type AppStreamGlib.Tag>, 28: <enum AS_TAG_VALUE of type AppStreamGlib.Tag>, 29: <enum AS_TAG_RELEASES of type AppStreamGlib.Tag>, 30: <enum AS_TAG_RELEASE of type AppStreamGlib.Tag>, 31: <enum AS_TAG_ARCHITECTURES of type AppStreamGlib.Tag>, 32: <enum AS_TAG_ARCH of type AppStreamGlib.Tag>, 33: <enum AS_TAG_METADATA_LICENSE of type AppStreamGlib.Tag>, 34: <enum AS_TAG_PROVIDES of type AppStreamGlib.Tag>, 35: <enum AS_TAG_EXTENDS of type AppStreamGlib.Tag>, 36: <enum AS_TAG_DEVELOPER_NAME of type AppStreamGlib.Tag>, 37: <enum AS_TAG_KUDOS of type AppStreamGlib.Tag>, 38: <enum AS_TAG_KUDO of type AppStreamGlib.Tag>, 39: <enum AS_TAG_SOURCE_PKGNAME of type AppStreamGlib.Tag>, 40: <enum AS_TAG_VETOS of type AppStreamGlib.Tag>, 41: <enum AS_TAG_VETO of type AppStreamGlib.Tag>, 42: <enum AS_TAG_BUNDLE of type AppStreamGlib.Tag>, 43: <enum AS_TAG_PERMISSIONS of type AppStreamGlib.Tag>, 44: <enum AS_TAG_PERMISSION of type AppStreamGlib.Tag>, 45: <enum AS_TAG_LOCATION of type AppStreamGlib.Tag>, 46: <enum AS_TAG_CHECKSUM of type AppStreamGlib.Tag>, 47: <enum AS_TAG_SIZE of type AppStreamGlib.Tag>, 48: <enum AS_TAG_TRANSLATION of type AppStreamGlib.Tag>, 49: <enum AS_TAG_CONTENT_RATING of type AppStreamGlib.Tag>, 50: <enum AS_TAG_CONTENT_ATTRIBUTE of type AppStreamGlib.Tag>, 51: <enum AS_TAG_VERSION of type AppStreamGlib.Tag>, 52: <enum AS_TAG_REVIEWS of type AppStreamGlib.Tag>, 53: <enum AS_TAG_REVIEW of type AppStreamGlib.Tag>, 54: <enum AS_TAG_REVIEWER_NAME of type AppStreamGlib.Tag>, 55: <enum AS_TAG_REVIEWER_ID of type AppStreamGlib.Tag>, 56: <enum AS_TAG_SUGGESTS of type AppStreamGlib.Tag>, 57: <enum AS_TAG_REQUIRES of type AppStreamGlib.Tag>, 58: <enum AS_TAG_CUSTOM of type AppStreamGlib.Tag>, 59: <enum AS_TAG_LAUNCHABLE of type AppStreamGlib.Tag>, 60: <enum AS_TAG_AGREEMENT of type AppStreamGlib.Tag>, 61: <enum AS_TAG_AGREEMENT_SECTION of type AppStreamGlib.Tag>, 62: <enum AS_TAG_P of type AppStreamGlib.Tag>, 63: <enum AS_TAG_LI of type AppStreamGlib.Tag>, 64: <enum AS_TAG_UL of type AppStreamGlib.Tag>, 65: <enum AS_TAG_OL of type AppStreamGlib.Tag>, 66: <enum AS_TAG_BINARY of type AppStreamGlib.Tag>, 67: <enum AS_TAG_FONT of type AppStreamGlib.Tag>, 68: <enum AS_TAG_DBUS of type AppStreamGlib.Tag>, 69: <enum AS_TAG_MODALIAS of type AppStreamGlib.Tag>, 70: <enum AS_TAG_LIBRARY of type AppStreamGlib.Tag>}, '__info__': gi.EnumInfo(Tag), 'UNKNOWN': <enum AS_TAG_UNKNOWN of type AppStreamGlib.Tag>, 'COMPONENTS': <enum AS_TAG_COMPONENTS of type AppStreamGlib.Tag>, 'COMPONENT': <enum AS_TAG_COMPONENT of type AppStreamGlib.Tag>, 'ID': <enum AS_TAG_ID of type AppStreamGlib.Tag>, 'PKGNAME': <enum AS_TAG_PKGNAME of type AppStreamGlib.Tag>, 'NAME': <enum AS_TAG_NAME of type AppStreamGlib.Tag>, 'SUMMARY': <enum AS_TAG_SUMMARY of type AppStreamGlib.Tag>, 'DESCRIPTION': <enum AS_TAG_DESCRIPTION of type AppStreamGlib.Tag>, 'URL': <enum AS_TAG_URL of type AppStreamGlib.Tag>, 'ICON': <enum AS_TAG_ICON of type AppStreamGlib.Tag>, 'CATEGORIES': <enum AS_TAG_CATEGORIES of type AppStreamGlib.Tag>, 'CATEGORY': <enum AS_TAG_CATEGORY of type AppStreamGlib.Tag>, 'KEYWORDS': <enum AS_TAG_KEYWORDS of type AppStreamGlib.Tag>, 'KEYWORD': <enum AS_TAG_KEYWORD of type AppStreamGlib.Tag>, 'MIMETYPES': <enum AS_TAG_MIMETYPES of type AppStreamGlib.Tag>, 'MIMETYPE': <enum AS_TAG_MIMETYPE of type AppStreamGlib.Tag>, 'PROJECT_GROUP': <enum AS_TAG_PROJECT_GROUP of type AppStreamGlib.Tag>, 'PROJECT_LICENSE': <enum AS_TAG_PROJECT_LICENSE of type AppStreamGlib.Tag>, 'SCREENSHOT': <enum AS_TAG_SCREENSHOT of type AppStreamGlib.Tag>, 'SCREENSHOTS': <enum AS_TAG_SCREENSHOTS of type AppStreamGlib.Tag>, 'UPDATE_CONTACT': <enum AS_TAG_UPDATE_CONTACT of type AppStreamGlib.Tag>, 'IMAGE': <enum AS_TAG_IMAGE of type AppStreamGlib.Tag>, 'COMPULSORY_FOR_DESKTOP': <enum AS_TAG_COMPULSORY_FOR_DESKTOP of type AppStreamGlib.Tag>, 'PRIORITY': <enum AS_TAG_PRIORITY of type AppStreamGlib.Tag>, 'CAPTION': <enum AS_TAG_CAPTION of type AppStreamGlib.Tag>, 'LANGUAGES': <enum AS_TAG_LANGUAGES of type AppStreamGlib.Tag>, 'LANG': <enum AS_TAG_LANG of type AppStreamGlib.Tag>, 'METADATA': <enum AS_TAG_METADATA of type AppStreamGlib.Tag>, 'VALUE': <enum AS_TAG_VALUE of type AppStreamGlib.Tag>, 'RELEASES': <enum AS_TAG_RELEASES of type AppStreamGlib.Tag>, 'RELEASE': <enum AS_TAG_RELEASE of type AppStreamGlib.Tag>, 'ARCHITECTURES': <enum AS_TAG_ARCHITECTURES of type AppStreamGlib.Tag>, 'ARCH': <enum AS_TAG_ARCH of type AppStreamGlib.Tag>, 'METADATA_LICENSE': <enum AS_TAG_METADATA_LICENSE of type AppStreamGlib.Tag>, 'PROVIDES': <enum AS_TAG_PROVIDES of type AppStreamGlib.Tag>, 'EXTENDS': <enum AS_TAG_EXTENDS of type AppStreamGlib.Tag>, 'DEVELOPER_NAME': <enum AS_TAG_DEVELOPER_NAME of type AppStreamGlib.Tag>, 'KUDOS': <enum AS_TAG_KUDOS of type AppStreamGlib.Tag>, 'KUDO': <enum AS_TAG_KUDO of type AppStreamGlib.Tag>, 'SOURCE_PKGNAME': <enum AS_TAG_SOURCE_PKGNAME of type AppStreamGlib.Tag>, 'VETOS': <enum AS_TAG_VETOS of type AppStreamGlib.Tag>, 'VETO': <enum AS_TAG_VETO of type AppStreamGlib.Tag>, 'BUNDLE': <enum AS_TAG_BUNDLE of type AppStreamGlib.Tag>, 'PERMISSIONS': <enum AS_TAG_PERMISSIONS of type AppStreamGlib.Tag>, 'PERMISSION': <enum AS_TAG_PERMISSION of type AppStreamGlib.Tag>, 'LOCATION': <enum AS_TAG_LOCATION of type AppStreamGlib.Tag>, 'CHECKSUM': <enum AS_TAG_CHECKSUM of type AppStreamGlib.Tag>, 'SIZE': <enum AS_TAG_SIZE of type AppStreamGlib.Tag>, 'TRANSLATION': <enum AS_TAG_TRANSLATION of type AppStreamGlib.Tag>, 'CONTENT_RATING': <enum AS_TAG_CONTENT_RATING of type AppStreamGlib.Tag>, 'CONTENT_ATTRIBUTE': <enum AS_TAG_CONTENT_ATTRIBUTE of type AppStreamGlib.Tag>, 'VERSION': <enum AS_TAG_VERSION of type AppStreamGlib.Tag>, 'REVIEWS': <enum AS_TAG_REVIEWS of type AppStreamGlib.Tag>, 'REVIEW': <enum AS_TAG_REVIEW of type AppStreamGlib.Tag>, 'REVIEWER_NAME': <enum AS_TAG_REVIEWER_NAME of type AppStreamGlib.Tag>, 'REVIEWER_ID': <enum AS_TAG_REVIEWER_ID of type AppStreamGlib.Tag>, 'SUGGESTS': <enum AS_TAG_SUGGESTS of type AppStreamGlib.Tag>, 'REQUIRES': <enum AS_TAG_REQUIRES of type AppStreamGlib.Tag>, 'CUSTOM': <enum AS_TAG_CUSTOM of type AppStreamGlib.Tag>, 'LAUNCHABLE': <enum AS_TAG_LAUNCHABLE of type AppStreamGlib.Tag>, 'AGREEMENT': <enum AS_TAG_AGREEMENT of type AppStreamGlib.Tag>, 'AGREEMENT_SECTION': <enum AS_TAG_AGREEMENT_SECTION of type AppStreamGlib.Tag>, 'P': <enum AS_TAG_P of type AppStreamGlib.Tag>, 'LI': <enum AS_TAG_LI of type AppStreamGlib.Tag>, 'UL': <enum AS_TAG_UL of type AppStreamGlib.Tag>, 'OL': <enum AS_TAG_OL of type AppStreamGlib.Tag>, 'BINARY': <enum AS_TAG_BINARY of type AppStreamGlib.Tag>, 'FONT': <enum AS_TAG_FONT of type AppStreamGlib.Tag>, 'DBUS': <enum AS_TAG_DBUS of type AppStreamGlib.Tag>, 'MODALIAS': <enum AS_TAG_MODALIAS of type AppStreamGlib.Tag>, 'LIBRARY': <enum AS_TAG_LIBRARY of type AppStreamGlib.Tag>})"
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
        62: 62,
        63: 63,
        64: 64,
        65: 65,
        66: 66,
        67: 67,
        68: 68,
        69: 69,
        70: 70,
    }
    __gtype__ = None # (!) real value is '<GType PyAppStreamGlibTag (3157403360)>'
    __info__ = gi.EnumInfo(Tag)


