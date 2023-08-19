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


class Status(__gobject.GEnum):
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
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
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


    CLIP_NOT_REPRESENTABLE = 22
    DEVICE_ERROR = 35
    DEVICE_FINISHED = 37
    DEVICE_TYPE_MISMATCH = 34
    FILE_NOT_FOUND = 18
    FONT_TYPE_MISMATCH = 25
    INVALID_CLUSTERS = 29
    INVALID_CONTENT = 15
    INVALID_DASH = 19
    INVALID_DSC_COMMENT = 20
    INVALID_FORMAT = 16
    INVALID_INDEX = 21
    INVALID_MATRIX = 5
    INVALID_MESH_CONSTRUCTION = 36
    INVALID_PATH_DATA = 9
    INVALID_POP_GROUP = 3
    INVALID_RESTORE = 2
    INVALID_SIZE = 32
    INVALID_SLANT = 30
    INVALID_STATUS = 6
    INVALID_STRIDE = 24
    INVALID_STRING = 8
    INVALID_VISUAL = 17
    INVALID_WEIGHT = 31
    JBIG2_GLOBAL_MISSING = 38
    NEGATIVE_COUNT = 28
    NO_CURRENT_POINT = 4
    NO_MEMORY = 1
    NULL_POINTER = 7
    PATTERN_TYPE_MISMATCH = 14
    READ_ERROR = 10
    SUCCESS = 0
    SURFACE_FINISHED = 12
    SURFACE_TYPE_MISMATCH = 13
    TEMP_FILE_ERROR = 23
    USER_FONT_ERROR = 27
    USER_FONT_IMMUTABLE = 26
    USER_FONT_NOT_IMPLEMENTED = 33
    WRITE_ERROR = 11
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.cairo', '__dict__': <attribute '__dict__' of 'Status' objects>, '__doc__': None, '__gtype__': <GType cairo_status_t (3504590080)>, '__enum_values__': {0: <enum CAIRO_STATUS_SUCCESS of type cairo.Status>, 1: <enum CAIRO_STATUS_NO_MEMORY of type cairo.Status>, 2: <enum CAIRO_STATUS_INVALID_RESTORE of type cairo.Status>, 3: <enum CAIRO_STATUS_INVALID_POP_GROUP of type cairo.Status>, 4: <enum CAIRO_STATUS_NO_CURRENT_POINT of type cairo.Status>, 5: <enum CAIRO_STATUS_INVALID_MATRIX of type cairo.Status>, 6: <enum CAIRO_STATUS_INVALID_STATUS of type cairo.Status>, 7: <enum CAIRO_STATUS_NULL_POINTER of type cairo.Status>, 8: <enum CAIRO_STATUS_INVALID_STRING of type cairo.Status>, 9: <enum CAIRO_STATUS_INVALID_PATH_DATA of type cairo.Status>, 10: <enum CAIRO_STATUS_READ_ERROR of type cairo.Status>, 11: <enum CAIRO_STATUS_WRITE_ERROR of type cairo.Status>, 12: <enum CAIRO_STATUS_SURFACE_FINISHED of type cairo.Status>, 13: <enum CAIRO_STATUS_SURFACE_TYPE_MISMATCH of type cairo.Status>, 14: <enum CAIRO_STATUS_PATTERN_TYPE_MISMATCH of type cairo.Status>, 15: <enum CAIRO_STATUS_INVALID_CONTENT of type cairo.Status>, 16: <enum CAIRO_STATUS_INVALID_FORMAT of type cairo.Status>, 17: <enum CAIRO_STATUS_INVALID_VISUAL of type cairo.Status>, 18: <enum CAIRO_STATUS_FILE_NOT_FOUND of type cairo.Status>, 19: <enum CAIRO_STATUS_INVALID_DASH of type cairo.Status>, 20: <enum CAIRO_STATUS_INVALID_DSC_COMMENT of type cairo.Status>, 21: <enum CAIRO_STATUS_INVALID_INDEX of type cairo.Status>, 22: <enum CAIRO_STATUS_CLIP_NOT_REPRESENTABLE of type cairo.Status>, 23: <enum CAIRO_STATUS_TEMP_FILE_ERROR of type cairo.Status>, 24: <enum CAIRO_STATUS_INVALID_STRIDE of type cairo.Status>, 25: <enum CAIRO_STATUS_FONT_TYPE_MISMATCH of type cairo.Status>, 26: <enum CAIRO_STATUS_USER_FONT_IMMUTABLE of type cairo.Status>, 27: <enum CAIRO_STATUS_USER_FONT_ERROR of type cairo.Status>, 28: <enum CAIRO_STATUS_NEGATIVE_COUNT of type cairo.Status>, 29: <enum CAIRO_STATUS_INVALID_CLUSTERS of type cairo.Status>, 30: <enum CAIRO_STATUS_INVALID_SLANT of type cairo.Status>, 31: <enum CAIRO_STATUS_INVALID_WEIGHT of type cairo.Status>, 32: <enum CAIRO_STATUS_INVALID_SIZE of type cairo.Status>, 33: <enum CAIRO_STATUS_USER_FONT_NOT_IMPLEMENTED of type cairo.Status>, 34: <enum CAIRO_STATUS_DEVICE_TYPE_MISMATCH of type cairo.Status>, 35: <enum CAIRO_STATUS_DEVICE_ERROR of type cairo.Status>, 36: <enum CAIRO_STATUS_INVALID_MESH_CONSTRUCTION of type cairo.Status>, 37: <enum CAIRO_STATUS_DEVICE_FINISHED of type cairo.Status>, 38: <enum CAIRO_STATUS_JBIG2_GLOBAL_MISSING of type cairo.Status>, 39: <enum CAIRO_STATUS_PNG_ERROR of type cairo.Status>, 40: <enum CAIRO_STATUS_FREETYPE_ERROR of type cairo.Status>, 45: <enum CAIRO_STATUS_LAST_STATUS of type cairo.Status>, 41: <enum CAIRO_STATUS_WIN32_GDI_ERROR of type cairo.Status>}, '__info__': gi.EnumInfo(Status), 'SUCCESS': <enum CAIRO_STATUS_SUCCESS of type cairo.Status>, 'NO_MEMORY': <enum CAIRO_STATUS_NO_MEMORY of type cairo.Status>, 'INVALID_RESTORE': <enum CAIRO_STATUS_INVALID_RESTORE of type cairo.Status>, 'INVALID_POP_GROUP': <enum CAIRO_STATUS_INVALID_POP_GROUP of type cairo.Status>, 'NO_CURRENT_POINT': <enum CAIRO_STATUS_NO_CURRENT_POINT of type cairo.Status>, 'INVALID_MATRIX': <enum CAIRO_STATUS_INVALID_MATRIX of type cairo.Status>, 'INVALID_STATUS': <enum CAIRO_STATUS_INVALID_STATUS of type cairo.Status>, 'NULL_POINTER': <enum CAIRO_STATUS_NULL_POINTER of type cairo.Status>, 'INVALID_STRING': <enum CAIRO_STATUS_INVALID_STRING of type cairo.Status>, 'INVALID_PATH_DATA': <enum CAIRO_STATUS_INVALID_PATH_DATA of type cairo.Status>, 'READ_ERROR': <enum CAIRO_STATUS_READ_ERROR of type cairo.Status>, 'WRITE_ERROR': <enum CAIRO_STATUS_WRITE_ERROR of type cairo.Status>, 'SURFACE_FINISHED': <enum CAIRO_STATUS_SURFACE_FINISHED of type cairo.Status>, 'SURFACE_TYPE_MISMATCH': <enum CAIRO_STATUS_SURFACE_TYPE_MISMATCH of type cairo.Status>, 'PATTERN_TYPE_MISMATCH': <enum CAIRO_STATUS_PATTERN_TYPE_MISMATCH of type cairo.Status>, 'INVALID_CONTENT': <enum CAIRO_STATUS_INVALID_CONTENT of type cairo.Status>, 'INVALID_FORMAT': <enum CAIRO_STATUS_INVALID_FORMAT of type cairo.Status>, 'INVALID_VISUAL': <enum CAIRO_STATUS_INVALID_VISUAL of type cairo.Status>, 'FILE_NOT_FOUND': <enum CAIRO_STATUS_FILE_NOT_FOUND of type cairo.Status>, 'INVALID_DASH': <enum CAIRO_STATUS_INVALID_DASH of type cairo.Status>, 'INVALID_DSC_COMMENT': <enum CAIRO_STATUS_INVALID_DSC_COMMENT of type cairo.Status>, 'INVALID_INDEX': <enum CAIRO_STATUS_INVALID_INDEX of type cairo.Status>, 'CLIP_NOT_REPRESENTABLE': <enum CAIRO_STATUS_CLIP_NOT_REPRESENTABLE of type cairo.Status>, 'TEMP_FILE_ERROR': <enum CAIRO_STATUS_TEMP_FILE_ERROR of type cairo.Status>, 'INVALID_STRIDE': <enum CAIRO_STATUS_INVALID_STRIDE of type cairo.Status>, 'FONT_TYPE_MISMATCH': <enum CAIRO_STATUS_FONT_TYPE_MISMATCH of type cairo.Status>, 'USER_FONT_IMMUTABLE': <enum CAIRO_STATUS_USER_FONT_IMMUTABLE of type cairo.Status>, 'USER_FONT_ERROR': <enum CAIRO_STATUS_USER_FONT_ERROR of type cairo.Status>, 'NEGATIVE_COUNT': <enum CAIRO_STATUS_NEGATIVE_COUNT of type cairo.Status>, 'INVALID_CLUSTERS': <enum CAIRO_STATUS_INVALID_CLUSTERS of type cairo.Status>, 'INVALID_SLANT': <enum CAIRO_STATUS_INVALID_SLANT of type cairo.Status>, 'INVALID_WEIGHT': <enum CAIRO_STATUS_INVALID_WEIGHT of type cairo.Status>, 'INVALID_SIZE': <enum CAIRO_STATUS_INVALID_SIZE of type cairo.Status>, 'USER_FONT_NOT_IMPLEMENTED': <enum CAIRO_STATUS_USER_FONT_NOT_IMPLEMENTED of type cairo.Status>, 'DEVICE_TYPE_MISMATCH': <enum CAIRO_STATUS_DEVICE_TYPE_MISMATCH of type cairo.Status>, 'DEVICE_ERROR': <enum CAIRO_STATUS_DEVICE_ERROR of type cairo.Status>, 'INVALID_MESH_CONSTRUCTION': <enum CAIRO_STATUS_INVALID_MESH_CONSTRUCTION of type cairo.Status>, 'DEVICE_FINISHED': <enum CAIRO_STATUS_DEVICE_FINISHED of type cairo.Status>, 'JBIG2_GLOBAL_MISSING': <enum CAIRO_STATUS_JBIG2_GLOBAL_MISSING of type cairo.Status>})"
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
        45: 45,
    }
    __gtype__ = None # (!) real value is '<GType cairo_status_t (3504590080)>'
    __info__ = gi.EnumInfo(Status)


