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


class FileError(__gobject.GEnum):
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


    ACCES = 2
    AGAIN = 19
    BADF = 16
    EXIST = 0
    FAILED = 24
    FAULT = 10
    INTR = 20
    INVAL = 17
    IO = 21
    ISDIR = 1
    LOOP = 11
    MFILE = 14
    NAMETOOLONG = 3
    NFILE = 15
    NODEV = 7
    NOENT = 4
    NOMEM = 13
    NOSPC = 12
    NOSYS = 23
    NOTDIR = 5
    NXIO = 6
    PERM = 22
    PIPE = 18
    ROFS = 8
    TXTBSY = 9
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'FileError' objects>, '__doc__': None, '__gtype__': <GType PyGLibFileError (163512160)>, '__enum_values__': {0: <enum G_FILE_ERROR_EXIST of type GLib.FileError>, 1: <enum G_FILE_ERROR_ISDIR of type GLib.FileError>, 2: <enum G_FILE_ERROR_ACCES of type GLib.FileError>, 3: <enum G_FILE_ERROR_NAMETOOLONG of type GLib.FileError>, 4: <enum G_FILE_ERROR_NOENT of type GLib.FileError>, 5: <enum G_FILE_ERROR_NOTDIR of type GLib.FileError>, 6: <enum G_FILE_ERROR_NXIO of type GLib.FileError>, 7: <enum G_FILE_ERROR_NODEV of type GLib.FileError>, 8: <enum G_FILE_ERROR_ROFS of type GLib.FileError>, 9: <enum G_FILE_ERROR_TXTBSY of type GLib.FileError>, 10: <enum G_FILE_ERROR_FAULT of type GLib.FileError>, 11: <enum G_FILE_ERROR_LOOP of type GLib.FileError>, 12: <enum G_FILE_ERROR_NOSPC of type GLib.FileError>, 13: <enum G_FILE_ERROR_NOMEM of type GLib.FileError>, 14: <enum G_FILE_ERROR_MFILE of type GLib.FileError>, 15: <enum G_FILE_ERROR_NFILE of type GLib.FileError>, 16: <enum G_FILE_ERROR_BADF of type GLib.FileError>, 17: <enum G_FILE_ERROR_INVAL of type GLib.FileError>, 18: <enum G_FILE_ERROR_PIPE of type GLib.FileError>, 19: <enum G_FILE_ERROR_AGAIN of type GLib.FileError>, 20: <enum G_FILE_ERROR_INTR of type GLib.FileError>, 21: <enum G_FILE_ERROR_IO of type GLib.FileError>, 22: <enum G_FILE_ERROR_PERM of type GLib.FileError>, 23: <enum G_FILE_ERROR_NOSYS of type GLib.FileError>, 24: <enum G_FILE_ERROR_FAILED of type GLib.FileError>}, '__info__': gi.EnumInfo(FileError), 'EXIST': <enum G_FILE_ERROR_EXIST of type GLib.FileError>, 'ISDIR': <enum G_FILE_ERROR_ISDIR of type GLib.FileError>, 'ACCES': <enum G_FILE_ERROR_ACCES of type GLib.FileError>, 'NAMETOOLONG': <enum G_FILE_ERROR_NAMETOOLONG of type GLib.FileError>, 'NOENT': <enum G_FILE_ERROR_NOENT of type GLib.FileError>, 'NOTDIR': <enum G_FILE_ERROR_NOTDIR of type GLib.FileError>, 'NXIO': <enum G_FILE_ERROR_NXIO of type GLib.FileError>, 'NODEV': <enum G_FILE_ERROR_NODEV of type GLib.FileError>, 'ROFS': <enum G_FILE_ERROR_ROFS of type GLib.FileError>, 'TXTBSY': <enum G_FILE_ERROR_TXTBSY of type GLib.FileError>, 'FAULT': <enum G_FILE_ERROR_FAULT of type GLib.FileError>, 'LOOP': <enum G_FILE_ERROR_LOOP of type GLib.FileError>, 'NOSPC': <enum G_FILE_ERROR_NOSPC of type GLib.FileError>, 'NOMEM': <enum G_FILE_ERROR_NOMEM of type GLib.FileError>, 'MFILE': <enum G_FILE_ERROR_MFILE of type GLib.FileError>, 'NFILE': <enum G_FILE_ERROR_NFILE of type GLib.FileError>, 'BADF': <enum G_FILE_ERROR_BADF of type GLib.FileError>, 'INVAL': <enum G_FILE_ERROR_INVAL of type GLib.FileError>, 'PIPE': <enum G_FILE_ERROR_PIPE of type GLib.FileError>, 'AGAIN': <enum G_FILE_ERROR_AGAIN of type GLib.FileError>, 'INTR': <enum G_FILE_ERROR_INTR of type GLib.FileError>, 'IO': <enum G_FILE_ERROR_IO of type GLib.FileError>, 'PERM': <enum G_FILE_ERROR_PERM of type GLib.FileError>, 'NOSYS': <enum G_FILE_ERROR_NOSYS of type GLib.FileError>, 'FAILED': <enum G_FILE_ERROR_FAILED of type GLib.FileError>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PyGLibFileError (163512160)>'
    __info__ = gi.EnumInfo(FileError)


