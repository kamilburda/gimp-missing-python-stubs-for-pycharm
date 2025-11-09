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


class DBusError(__gobject.GEnum):
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

    def encode_gerror(self, error): # real signature unknown; restored from __doc__
        """ encode_gerror(error:error) -> str """
        return ""

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

    def get_remote_error(self, error): # real signature unknown; restored from __doc__
        """ get_remote_error(error:error) -> str or None """
        return ""

    def is_remote_error(self, error): # real signature unknown; restored from __doc__
        """ is_remote_error(error:error) -> bool """
        return False

    def new_for_dbus_error(self, dbus_error_name, dbus_error_message): # real signature unknown; restored from __doc__
        """ new_for_dbus_error(dbus_error_name:str, dbus_error_message:str) -> error """
        pass

    def quark(self): # real signature unknown; restored from __doc__
        """ quark() -> int """
        return 0

    def register_error(self, error_domain, error_code, dbus_error_name): # real signature unknown; restored from __doc__
        """ register_error(error_domain:int, error_code:int, dbus_error_name:str) -> bool """
        return False

    def register_error_domain(self, error_domain_quark_name, quark_volatile, entries): # real signature unknown; restored from __doc__
        """ register_error_domain(error_domain_quark_name:str, quark_volatile:int, entries:list) """
        pass

    def strip_remote_error(self, error): # real signature unknown; restored from __doc__
        """ strip_remote_error(error:error) -> bool """
        return False

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

    def unregister_error(self, error_domain, error_code, dbus_error_name): # real signature unknown; restored from __doc__
        """ unregister_error(error_domain:int, error_code:int, dbus_error_name:str) -> bool """
        return False

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


    ACCESS_DENIED = 9
    ADDRESS_IN_USE = 14
    ADT_AUDIT_DATA_UNKNOWN = 39
    AUTH_FAILED = 10
    BAD_ADDRESS = 6
    DISCONNECTED = 15
    FAILED = 0
    FILE_EXISTS = 18
    FILE_NOT_FOUND = 17
    INVALID_ARGS = 16
    INVALID_FILE_CONTENT = 37
    INVALID_SIGNATURE = 36
    IO_ERROR = 5
    LIMITS_EXCEEDED = 8
    MATCH_RULE_INVALID = 22
    MATCH_RULE_NOT_FOUND = 21
    NAME_HAS_NO_OWNER = 3
    NOT_SUPPORTED = 7
    NO_MEMORY = 1
    NO_NETWORK = 13
    NO_REPLY = 4
    NO_SERVER = 11
    OBJECT_PATH_IN_USE = 40
    PROPERTY_READ_ONLY = 44
    SELINUX_SECURITY_CONTEXT_UNKNOWN = 38
    SERVICE_UNKNOWN = 2
    SPAWN_CHILD_EXITED = 25
    SPAWN_CHILD_SIGNALED = 26
    SPAWN_CONFIG_INVALID = 29
    SPAWN_EXEC_FAILED = 23
    SPAWN_FAILED = 27
    SPAWN_FILE_INVALID = 33
    SPAWN_FORK_FAILED = 24
    SPAWN_NO_MEMORY = 34
    SPAWN_PERMISSIONS_INVALID = 32
    SPAWN_SERVICE_INVALID = 30
    SPAWN_SERVICE_NOT_FOUND = 31
    SPAWN_SETUP_FAILED = 28
    TIMED_OUT = 20
    TIMEOUT = 12
    UNIX_PROCESS_ID_UNKNOWN = 35
    UNKNOWN_INTERFACE = 42
    UNKNOWN_METHOD = 19
    UNKNOWN_OBJECT = 41
    UNKNOWN_PROPERTY = 43
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gio', '__dict__': <attribute '__dict__' of 'DBusError' objects>, '__doc__': None, '__gtype__': <GType GDBusError (2472614176)>, '__enum_values__': {0: <enum G_DBUS_ERROR_FAILED of type Gio.DBusError>, 1: <enum G_DBUS_ERROR_NO_MEMORY of type Gio.DBusError>, 2: <enum G_DBUS_ERROR_SERVICE_UNKNOWN of type Gio.DBusError>, 3: <enum G_DBUS_ERROR_NAME_HAS_NO_OWNER of type Gio.DBusError>, 4: <enum G_DBUS_ERROR_NO_REPLY of type Gio.DBusError>, 5: <enum G_DBUS_ERROR_IO_ERROR of type Gio.DBusError>, 6: <enum G_DBUS_ERROR_BAD_ADDRESS of type Gio.DBusError>, 7: <enum G_DBUS_ERROR_NOT_SUPPORTED of type Gio.DBusError>, 8: <enum G_DBUS_ERROR_LIMITS_EXCEEDED of type Gio.DBusError>, 9: <enum G_DBUS_ERROR_ACCESS_DENIED of type Gio.DBusError>, 10: <enum G_DBUS_ERROR_AUTH_FAILED of type Gio.DBusError>, 11: <enum G_DBUS_ERROR_NO_SERVER of type Gio.DBusError>, 12: <enum G_DBUS_ERROR_TIMEOUT of type Gio.DBusError>, 13: <enum G_DBUS_ERROR_NO_NETWORK of type Gio.DBusError>, 14: <enum G_DBUS_ERROR_ADDRESS_IN_USE of type Gio.DBusError>, 15: <enum G_DBUS_ERROR_DISCONNECTED of type Gio.DBusError>, 16: <enum G_DBUS_ERROR_INVALID_ARGS of type Gio.DBusError>, 17: <enum G_DBUS_ERROR_FILE_NOT_FOUND of type Gio.DBusError>, 18: <enum G_DBUS_ERROR_FILE_EXISTS of type Gio.DBusError>, 19: <enum G_DBUS_ERROR_UNKNOWN_METHOD of type Gio.DBusError>, 20: <enum G_DBUS_ERROR_TIMED_OUT of type Gio.DBusError>, 21: <enum G_DBUS_ERROR_MATCH_RULE_NOT_FOUND of type Gio.DBusError>, 22: <enum G_DBUS_ERROR_MATCH_RULE_INVALID of type Gio.DBusError>, 23: <enum G_DBUS_ERROR_SPAWN_EXEC_FAILED of type Gio.DBusError>, 24: <enum G_DBUS_ERROR_SPAWN_FORK_FAILED of type Gio.DBusError>, 25: <enum G_DBUS_ERROR_SPAWN_CHILD_EXITED of type Gio.DBusError>, 26: <enum G_DBUS_ERROR_SPAWN_CHILD_SIGNALED of type Gio.DBusError>, 27: <enum G_DBUS_ERROR_SPAWN_FAILED of type Gio.DBusError>, 28: <enum G_DBUS_ERROR_SPAWN_SETUP_FAILED of type Gio.DBusError>, 29: <enum G_DBUS_ERROR_SPAWN_CONFIG_INVALID of type Gio.DBusError>, 30: <enum G_DBUS_ERROR_SPAWN_SERVICE_INVALID of type Gio.DBusError>, 31: <enum G_DBUS_ERROR_SPAWN_SERVICE_NOT_FOUND of type Gio.DBusError>, 32: <enum G_DBUS_ERROR_SPAWN_PERMISSIONS_INVALID of type Gio.DBusError>, 33: <enum G_DBUS_ERROR_SPAWN_FILE_INVALID of type Gio.DBusError>, 34: <enum G_DBUS_ERROR_SPAWN_NO_MEMORY of type Gio.DBusError>, 35: <enum G_DBUS_ERROR_UNIX_PROCESS_ID_UNKNOWN of type Gio.DBusError>, 36: <enum G_DBUS_ERROR_INVALID_SIGNATURE of type Gio.DBusError>, 37: <enum G_DBUS_ERROR_INVALID_FILE_CONTENT of type Gio.DBusError>, 38: <enum G_DBUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN of type Gio.DBusError>, 39: <enum G_DBUS_ERROR_ADT_AUDIT_DATA_UNKNOWN of type Gio.DBusError>, 40: <enum G_DBUS_ERROR_OBJECT_PATH_IN_USE of type Gio.DBusError>, 41: <enum G_DBUS_ERROR_UNKNOWN_OBJECT of type Gio.DBusError>, 42: <enum G_DBUS_ERROR_UNKNOWN_INTERFACE of type Gio.DBusError>, 43: <enum G_DBUS_ERROR_UNKNOWN_PROPERTY of type Gio.DBusError>, 44: <enum G_DBUS_ERROR_PROPERTY_READ_ONLY of type Gio.DBusError>}, '__info__': gi.EnumInfo(DBusError), 'FAILED': <enum G_DBUS_ERROR_FAILED of type Gio.DBusError>, 'NO_MEMORY': <enum G_DBUS_ERROR_NO_MEMORY of type Gio.DBusError>, 'SERVICE_UNKNOWN': <enum G_DBUS_ERROR_SERVICE_UNKNOWN of type Gio.DBusError>, 'NAME_HAS_NO_OWNER': <enum G_DBUS_ERROR_NAME_HAS_NO_OWNER of type Gio.DBusError>, 'NO_REPLY': <enum G_DBUS_ERROR_NO_REPLY of type Gio.DBusError>, 'IO_ERROR': <enum G_DBUS_ERROR_IO_ERROR of type Gio.DBusError>, 'BAD_ADDRESS': <enum G_DBUS_ERROR_BAD_ADDRESS of type Gio.DBusError>, 'NOT_SUPPORTED': <enum G_DBUS_ERROR_NOT_SUPPORTED of type Gio.DBusError>, 'LIMITS_EXCEEDED': <enum G_DBUS_ERROR_LIMITS_EXCEEDED of type Gio.DBusError>, 'ACCESS_DENIED': <enum G_DBUS_ERROR_ACCESS_DENIED of type Gio.DBusError>, 'AUTH_FAILED': <enum G_DBUS_ERROR_AUTH_FAILED of type Gio.DBusError>, 'NO_SERVER': <enum G_DBUS_ERROR_NO_SERVER of type Gio.DBusError>, 'TIMEOUT': <enum G_DBUS_ERROR_TIMEOUT of type Gio.DBusError>, 'NO_NETWORK': <enum G_DBUS_ERROR_NO_NETWORK of type Gio.DBusError>, 'ADDRESS_IN_USE': <enum G_DBUS_ERROR_ADDRESS_IN_USE of type Gio.DBusError>, 'DISCONNECTED': <enum G_DBUS_ERROR_DISCONNECTED of type Gio.DBusError>, 'INVALID_ARGS': <enum G_DBUS_ERROR_INVALID_ARGS of type Gio.DBusError>, 'FILE_NOT_FOUND': <enum G_DBUS_ERROR_FILE_NOT_FOUND of type Gio.DBusError>, 'FILE_EXISTS': <enum G_DBUS_ERROR_FILE_EXISTS of type Gio.DBusError>, 'UNKNOWN_METHOD': <enum G_DBUS_ERROR_UNKNOWN_METHOD of type Gio.DBusError>, 'TIMED_OUT': <enum G_DBUS_ERROR_TIMED_OUT of type Gio.DBusError>, 'MATCH_RULE_NOT_FOUND': <enum G_DBUS_ERROR_MATCH_RULE_NOT_FOUND of type Gio.DBusError>, 'MATCH_RULE_INVALID': <enum G_DBUS_ERROR_MATCH_RULE_INVALID of type Gio.DBusError>, 'SPAWN_EXEC_FAILED': <enum G_DBUS_ERROR_SPAWN_EXEC_FAILED of type Gio.DBusError>, 'SPAWN_FORK_FAILED': <enum G_DBUS_ERROR_SPAWN_FORK_FAILED of type Gio.DBusError>, 'SPAWN_CHILD_EXITED': <enum G_DBUS_ERROR_SPAWN_CHILD_EXITED of type Gio.DBusError>, 'SPAWN_CHILD_SIGNALED': <enum G_DBUS_ERROR_SPAWN_CHILD_SIGNALED of type Gio.DBusError>, 'SPAWN_FAILED': <enum G_DBUS_ERROR_SPAWN_FAILED of type Gio.DBusError>, 'SPAWN_SETUP_FAILED': <enum G_DBUS_ERROR_SPAWN_SETUP_FAILED of type Gio.DBusError>, 'SPAWN_CONFIG_INVALID': <enum G_DBUS_ERROR_SPAWN_CONFIG_INVALID of type Gio.DBusError>, 'SPAWN_SERVICE_INVALID': <enum G_DBUS_ERROR_SPAWN_SERVICE_INVALID of type Gio.DBusError>, 'SPAWN_SERVICE_NOT_FOUND': <enum G_DBUS_ERROR_SPAWN_SERVICE_NOT_FOUND of type Gio.DBusError>, 'SPAWN_PERMISSIONS_INVALID': <enum G_DBUS_ERROR_SPAWN_PERMISSIONS_INVALID of type Gio.DBusError>, 'SPAWN_FILE_INVALID': <enum G_DBUS_ERROR_SPAWN_FILE_INVALID of type Gio.DBusError>, 'SPAWN_NO_MEMORY': <enum G_DBUS_ERROR_SPAWN_NO_MEMORY of type Gio.DBusError>, 'UNIX_PROCESS_ID_UNKNOWN': <enum G_DBUS_ERROR_UNIX_PROCESS_ID_UNKNOWN of type Gio.DBusError>, 'INVALID_SIGNATURE': <enum G_DBUS_ERROR_INVALID_SIGNATURE of type Gio.DBusError>, 'INVALID_FILE_CONTENT': <enum G_DBUS_ERROR_INVALID_FILE_CONTENT of type Gio.DBusError>, 'SELINUX_SECURITY_CONTEXT_UNKNOWN': <enum G_DBUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN of type Gio.DBusError>, 'ADT_AUDIT_DATA_UNKNOWN': <enum G_DBUS_ERROR_ADT_AUDIT_DATA_UNKNOWN of type Gio.DBusError>, 'OBJECT_PATH_IN_USE': <enum G_DBUS_ERROR_OBJECT_PATH_IN_USE of type Gio.DBusError>, 'UNKNOWN_OBJECT': <enum G_DBUS_ERROR_UNKNOWN_OBJECT of type Gio.DBusError>, 'UNKNOWN_INTERFACE': <enum G_DBUS_ERROR_UNKNOWN_INTERFACE of type Gio.DBusError>, 'UNKNOWN_PROPERTY': <enum G_DBUS_ERROR_UNKNOWN_PROPERTY of type Gio.DBusError>, 'PROPERTY_READ_ONLY': <enum G_DBUS_ERROR_PROPERTY_READ_ONLY of type Gio.DBusError>, 'encode_gerror': gi.FunctionInfo(encode_gerror, bound=None), 'get_remote_error': gi.FunctionInfo(get_remote_error, bound=None), 'is_remote_error': gi.FunctionInfo(is_remote_error, bound=None), 'new_for_dbus_error': gi.FunctionInfo(new_for_dbus_error, bound=None), 'quark': gi.FunctionInfo(quark, bound=None), 'register_error': gi.FunctionInfo(register_error, bound=None), 'register_error_domain': gi.FunctionInfo(register_error_domain, bound=None), 'strip_remote_error': gi.FunctionInfo(strip_remote_error, bound=None), 'unregister_error': gi.FunctionInfo(unregister_error, bound=None)})"
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
    }
    __gtype__ = None # (!) real value is '<GType GDBusError (2472614176)>'
    __info__ = gi.EnumInfo(DBusError)


