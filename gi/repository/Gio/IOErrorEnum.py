# encoding: utf-8
# module gi.repository.Gio
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class IOErrorEnum(__gobject.GEnum):
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


    ADDRESS_IN_USE = 33
    ALREADY_MOUNTED = 17
    BROKEN_PIPE = 44
    BUSY = 26
    CANCELLED = 19
    CANT_CREATE_BACKUP = 22
    CLOSED = 18
    CONNECTION_CLOSED = 44
    CONNECTION_REFUSED = 39
    DBUS_ERROR = 36
    DESTINATION_UNSET = 48
    EXISTS = 2
    FAILED = 0
    FAILED_HANDLED = 30
    FILENAME_TOO_LONG = 9
    HOST_NOT_FOUND = 28
    HOST_UNREACHABLE = 37
    INVALID_ARGUMENT = 13
    INVALID_DATA = 35
    INVALID_FILENAME = 10
    IS_DIRECTORY = 3
    MESSAGE_TOO_LARGE = 46
    NETWORK_UNREACHABLE = 38
    NOT_CONNECTED = 45
    NOT_DIRECTORY = 4
    NOT_EMPTY = 5
    NOT_FOUND = 1
    NOT_INITIALIZED = 32
    NOT_MOUNTABLE_FILE = 8
    NOT_MOUNTED = 16
    NOT_REGULAR_FILE = 6
    NOT_SUPPORTED = 15
    NOT_SYMBOLIC_LINK = 7
    NO_SPACE = 12
    NO_SUCH_DEVICE = 47
    PARTIAL_INPUT = 34
    PENDING = 20
    PERMISSION_DENIED = 14
    PROXY_AUTH_FAILED = 41
    PROXY_FAILED = 40
    PROXY_NEED_AUTH = 42
    PROXY_NOT_ALLOWED = 43
    READ_ONLY = 21
    TIMED_OUT = 24
    TOO_MANY_LINKS = 11
    TOO_MANY_OPEN_FILES = 31
    WOULD_BLOCK = 27
    WOULD_MERGE = 29
    WOULD_RECURSE = 25
    WRONG_ETAG = 23
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gio', '__dict__': <attribute '__dict__' of 'IOErrorEnum' objects>, '__doc__': None, '__gtype__': <GType GIOErrorEnum (2466384240)>, '__enum_values__': {0: <enum G_IO_ERROR_FAILED of type Gio.IOErrorEnum>, 1: <enum G_IO_ERROR_NOT_FOUND of type Gio.IOErrorEnum>, 2: <enum G_IO_ERROR_EXISTS of type Gio.IOErrorEnum>, 3: <enum G_IO_ERROR_IS_DIRECTORY of type Gio.IOErrorEnum>, 4: <enum G_IO_ERROR_NOT_DIRECTORY of type Gio.IOErrorEnum>, 5: <enum G_IO_ERROR_NOT_EMPTY of type Gio.IOErrorEnum>, 6: <enum G_IO_ERROR_NOT_REGULAR_FILE of type Gio.IOErrorEnum>, 7: <enum G_IO_ERROR_NOT_SYMBOLIC_LINK of type Gio.IOErrorEnum>, 8: <enum G_IO_ERROR_NOT_MOUNTABLE_FILE of type Gio.IOErrorEnum>, 9: <enum G_IO_ERROR_FILENAME_TOO_LONG of type Gio.IOErrorEnum>, 10: <enum G_IO_ERROR_INVALID_FILENAME of type Gio.IOErrorEnum>, 11: <enum G_IO_ERROR_TOO_MANY_LINKS of type Gio.IOErrorEnum>, 12: <enum G_IO_ERROR_NO_SPACE of type Gio.IOErrorEnum>, 13: <enum G_IO_ERROR_INVALID_ARGUMENT of type Gio.IOErrorEnum>, 14: <enum G_IO_ERROR_PERMISSION_DENIED of type Gio.IOErrorEnum>, 15: <enum G_IO_ERROR_NOT_SUPPORTED of type Gio.IOErrorEnum>, 16: <enum G_IO_ERROR_NOT_MOUNTED of type Gio.IOErrorEnum>, 17: <enum G_IO_ERROR_ALREADY_MOUNTED of type Gio.IOErrorEnum>, 18: <enum G_IO_ERROR_CLOSED of type Gio.IOErrorEnum>, 19: <enum G_IO_ERROR_CANCELLED of type Gio.IOErrorEnum>, 20: <enum G_IO_ERROR_PENDING of type Gio.IOErrorEnum>, 21: <enum G_IO_ERROR_READ_ONLY of type Gio.IOErrorEnum>, 22: <enum G_IO_ERROR_CANT_CREATE_BACKUP of type Gio.IOErrorEnum>, 23: <enum G_IO_ERROR_WRONG_ETAG of type Gio.IOErrorEnum>, 24: <enum G_IO_ERROR_TIMED_OUT of type Gio.IOErrorEnum>, 25: <enum G_IO_ERROR_WOULD_RECURSE of type Gio.IOErrorEnum>, 26: <enum G_IO_ERROR_BUSY of type Gio.IOErrorEnum>, 27: <enum G_IO_ERROR_WOULD_BLOCK of type Gio.IOErrorEnum>, 28: <enum G_IO_ERROR_HOST_NOT_FOUND of type Gio.IOErrorEnum>, 29: <enum G_IO_ERROR_WOULD_MERGE of type Gio.IOErrorEnum>, 30: <enum G_IO_ERROR_FAILED_HANDLED of type Gio.IOErrorEnum>, 31: <enum G_IO_ERROR_TOO_MANY_OPEN_FILES of type Gio.IOErrorEnum>, 32: <enum G_IO_ERROR_NOT_INITIALIZED of type Gio.IOErrorEnum>, 33: <enum G_IO_ERROR_ADDRESS_IN_USE of type Gio.IOErrorEnum>, 34: <enum G_IO_ERROR_PARTIAL_INPUT of type Gio.IOErrorEnum>, 35: <enum G_IO_ERROR_INVALID_DATA of type Gio.IOErrorEnum>, 36: <enum G_IO_ERROR_DBUS_ERROR of type Gio.IOErrorEnum>, 37: <enum G_IO_ERROR_HOST_UNREACHABLE of type Gio.IOErrorEnum>, 38: <enum G_IO_ERROR_NETWORK_UNREACHABLE of type Gio.IOErrorEnum>, 39: <enum G_IO_ERROR_CONNECTION_REFUSED of type Gio.IOErrorEnum>, 40: <enum G_IO_ERROR_PROXY_FAILED of type Gio.IOErrorEnum>, 41: <enum G_IO_ERROR_PROXY_AUTH_FAILED of type Gio.IOErrorEnum>, 42: <enum G_IO_ERROR_PROXY_NEED_AUTH of type Gio.IOErrorEnum>, 43: <enum G_IO_ERROR_PROXY_NOT_ALLOWED of type Gio.IOErrorEnum>, 44: <enum G_IO_ERROR_BROKEN_PIPE of type Gio.IOErrorEnum>, 45: <enum G_IO_ERROR_NOT_CONNECTED of type Gio.IOErrorEnum>, 46: <enum G_IO_ERROR_MESSAGE_TOO_LARGE of type Gio.IOErrorEnum>, 47: <enum G_IO_ERROR_NO_SUCH_DEVICE of type Gio.IOErrorEnum>, 48: <enum G_IO_ERROR_DESTINATION_UNSET of type Gio.IOErrorEnum>}, '__info__': gi.EnumInfo(IOErrorEnum), 'FAILED': <enum G_IO_ERROR_FAILED of type Gio.IOErrorEnum>, 'NOT_FOUND': <enum G_IO_ERROR_NOT_FOUND of type Gio.IOErrorEnum>, 'EXISTS': <enum G_IO_ERROR_EXISTS of type Gio.IOErrorEnum>, 'IS_DIRECTORY': <enum G_IO_ERROR_IS_DIRECTORY of type Gio.IOErrorEnum>, 'NOT_DIRECTORY': <enum G_IO_ERROR_NOT_DIRECTORY of type Gio.IOErrorEnum>, 'NOT_EMPTY': <enum G_IO_ERROR_NOT_EMPTY of type Gio.IOErrorEnum>, 'NOT_REGULAR_FILE': <enum G_IO_ERROR_NOT_REGULAR_FILE of type Gio.IOErrorEnum>, 'NOT_SYMBOLIC_LINK': <enum G_IO_ERROR_NOT_SYMBOLIC_LINK of type Gio.IOErrorEnum>, 'NOT_MOUNTABLE_FILE': <enum G_IO_ERROR_NOT_MOUNTABLE_FILE of type Gio.IOErrorEnum>, 'FILENAME_TOO_LONG': <enum G_IO_ERROR_FILENAME_TOO_LONG of type Gio.IOErrorEnum>, 'INVALID_FILENAME': <enum G_IO_ERROR_INVALID_FILENAME of type Gio.IOErrorEnum>, 'TOO_MANY_LINKS': <enum G_IO_ERROR_TOO_MANY_LINKS of type Gio.IOErrorEnum>, 'NO_SPACE': <enum G_IO_ERROR_NO_SPACE of type Gio.IOErrorEnum>, 'INVALID_ARGUMENT': <enum G_IO_ERROR_INVALID_ARGUMENT of type Gio.IOErrorEnum>, 'PERMISSION_DENIED': <enum G_IO_ERROR_PERMISSION_DENIED of type Gio.IOErrorEnum>, 'NOT_SUPPORTED': <enum G_IO_ERROR_NOT_SUPPORTED of type Gio.IOErrorEnum>, 'NOT_MOUNTED': <enum G_IO_ERROR_NOT_MOUNTED of type Gio.IOErrorEnum>, 'ALREADY_MOUNTED': <enum G_IO_ERROR_ALREADY_MOUNTED of type Gio.IOErrorEnum>, 'CLOSED': <enum G_IO_ERROR_CLOSED of type Gio.IOErrorEnum>, 'CANCELLED': <enum G_IO_ERROR_CANCELLED of type Gio.IOErrorEnum>, 'PENDING': <enum G_IO_ERROR_PENDING of type Gio.IOErrorEnum>, 'READ_ONLY': <enum G_IO_ERROR_READ_ONLY of type Gio.IOErrorEnum>, 'CANT_CREATE_BACKUP': <enum G_IO_ERROR_CANT_CREATE_BACKUP of type Gio.IOErrorEnum>, 'WRONG_ETAG': <enum G_IO_ERROR_WRONG_ETAG of type Gio.IOErrorEnum>, 'TIMED_OUT': <enum G_IO_ERROR_TIMED_OUT of type Gio.IOErrorEnum>, 'WOULD_RECURSE': <enum G_IO_ERROR_WOULD_RECURSE of type Gio.IOErrorEnum>, 'BUSY': <enum G_IO_ERROR_BUSY of type Gio.IOErrorEnum>, 'WOULD_BLOCK': <enum G_IO_ERROR_WOULD_BLOCK of type Gio.IOErrorEnum>, 'HOST_NOT_FOUND': <enum G_IO_ERROR_HOST_NOT_FOUND of type Gio.IOErrorEnum>, 'WOULD_MERGE': <enum G_IO_ERROR_WOULD_MERGE of type Gio.IOErrorEnum>, 'FAILED_HANDLED': <enum G_IO_ERROR_FAILED_HANDLED of type Gio.IOErrorEnum>, 'TOO_MANY_OPEN_FILES': <enum G_IO_ERROR_TOO_MANY_OPEN_FILES of type Gio.IOErrorEnum>, 'NOT_INITIALIZED': <enum G_IO_ERROR_NOT_INITIALIZED of type Gio.IOErrorEnum>, 'ADDRESS_IN_USE': <enum G_IO_ERROR_ADDRESS_IN_USE of type Gio.IOErrorEnum>, 'PARTIAL_INPUT': <enum G_IO_ERROR_PARTIAL_INPUT of type Gio.IOErrorEnum>, 'INVALID_DATA': <enum G_IO_ERROR_INVALID_DATA of type Gio.IOErrorEnum>, 'DBUS_ERROR': <enum G_IO_ERROR_DBUS_ERROR of type Gio.IOErrorEnum>, 'HOST_UNREACHABLE': <enum G_IO_ERROR_HOST_UNREACHABLE of type Gio.IOErrorEnum>, 'NETWORK_UNREACHABLE': <enum G_IO_ERROR_NETWORK_UNREACHABLE of type Gio.IOErrorEnum>, 'CONNECTION_REFUSED': <enum G_IO_ERROR_CONNECTION_REFUSED of type Gio.IOErrorEnum>, 'PROXY_FAILED': <enum G_IO_ERROR_PROXY_FAILED of type Gio.IOErrorEnum>, 'PROXY_AUTH_FAILED': <enum G_IO_ERROR_PROXY_AUTH_FAILED of type Gio.IOErrorEnum>, 'PROXY_NEED_AUTH': <enum G_IO_ERROR_PROXY_NEED_AUTH of type Gio.IOErrorEnum>, 'PROXY_NOT_ALLOWED': <enum G_IO_ERROR_PROXY_NOT_ALLOWED of type Gio.IOErrorEnum>, 'BROKEN_PIPE': <enum G_IO_ERROR_BROKEN_PIPE of type Gio.IOErrorEnum>, 'CONNECTION_CLOSED': <enum G_IO_ERROR_BROKEN_PIPE of type Gio.IOErrorEnum>, 'NOT_CONNECTED': <enum G_IO_ERROR_NOT_CONNECTED of type Gio.IOErrorEnum>, 'MESSAGE_TOO_LARGE': <enum G_IO_ERROR_MESSAGE_TOO_LARGE of type Gio.IOErrorEnum>, 'NO_SUCH_DEVICE': <enum G_IO_ERROR_NO_SUCH_DEVICE of type Gio.IOErrorEnum>, 'DESTINATION_UNSET': <enum G_IO_ERROR_DESTINATION_UNSET of type Gio.IOErrorEnum>})"
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
    }
    __gtype__ = None # (!) real value is '<GType GIOErrorEnum (2466384240)>'
    __info__ = gi.EnumInfo(IOErrorEnum)


