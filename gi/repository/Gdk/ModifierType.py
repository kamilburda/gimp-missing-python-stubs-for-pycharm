# encoding: utf-8
# module gi.repository.Gdk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gdk-3.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ModifierType(__gobject.GFlags):
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


    BUTTON1_MASK = 256
    BUTTON2_MASK = 512
    BUTTON3_MASK = 1024
    BUTTON4_MASK = 2048
    BUTTON5_MASK = 4096
    CONTROL_MASK = 4
    HYPER_MASK = 134217728
    LOCK_MASK = 2
    META_MASK = 268435456
    MOD1_MASK = 8
    MOD2_MASK = 16
    MOD3_MASK = 32
    MOD4_MASK = 64
    MOD5_MASK = 128
    MODIFIER_MASK = 1543512063
    MODIFIER_RESERVED_13_MASK = 8192
    MODIFIER_RESERVED_14_MASK = 16384
    MODIFIER_RESERVED_15_MASK = 32768
    MODIFIER_RESERVED_16_MASK = 65536
    MODIFIER_RESERVED_17_MASK = 131072
    MODIFIER_RESERVED_18_MASK = 262144
    MODIFIER_RESERVED_19_MASK = 524288
    MODIFIER_RESERVED_20_MASK = 1048576
    MODIFIER_RESERVED_21_MASK = 2097152
    MODIFIER_RESERVED_22_MASK = 4194304
    MODIFIER_RESERVED_23_MASK = 8388608
    MODIFIER_RESERVED_24_MASK = 16777216
    MODIFIER_RESERVED_25_MASK = 33554432
    MODIFIER_RESERVED_29_MASK = 536870912
    RELEASE_MASK = 1073741824
    SHIFT_MASK = 1
    SUPER_MASK = 67108864
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gdk', '__dict__': <attribute '__dict__' of 'ModifierType' objects>, '__doc__': None, '__gtype__': <GType GdkModifierType (2579730080)>, '__flags_values__': {1: <flags GDK_SHIFT_MASK of type Gdk.ModifierType>, 2: <flags GDK_LOCK_MASK of type Gdk.ModifierType>, 4: <flags GDK_CONTROL_MASK of type Gdk.ModifierType>, 8: <flags GDK_MOD1_MASK of type Gdk.ModifierType>, 16: <flags GDK_MOD2_MASK of type Gdk.ModifierType>, 32: <flags GDK_MOD3_MASK of type Gdk.ModifierType>, 64: <flags GDK_MOD4_MASK of type Gdk.ModifierType>, 128: <flags GDK_MOD5_MASK of type Gdk.ModifierType>, 256: <flags GDK_BUTTON1_MASK of type Gdk.ModifierType>, 512: <flags GDK_BUTTON2_MASK of type Gdk.ModifierType>, 1024: <flags GDK_BUTTON3_MASK of type Gdk.ModifierType>, 2048: <flags GDK_BUTTON4_MASK of type Gdk.ModifierType>, 4096: <flags GDK_BUTTON5_MASK of type Gdk.ModifierType>, 8192: <flags GDK_MODIFIER_RESERVED_13_MASK of type Gdk.ModifierType>, 16384: <flags GDK_MODIFIER_RESERVED_14_MASK of type Gdk.ModifierType>, 32768: <flags GDK_MODIFIER_RESERVED_15_MASK of type Gdk.ModifierType>, 65536: <flags GDK_MODIFIER_RESERVED_16_MASK of type Gdk.ModifierType>, 131072: <flags GDK_MODIFIER_RESERVED_17_MASK of type Gdk.ModifierType>, 262144: <flags GDK_MODIFIER_RESERVED_18_MASK of type Gdk.ModifierType>, 524288: <flags GDK_MODIFIER_RESERVED_19_MASK of type Gdk.ModifierType>, 1048576: <flags GDK_MODIFIER_RESERVED_20_MASK of type Gdk.ModifierType>, 2097152: <flags GDK_MODIFIER_RESERVED_21_MASK of type Gdk.ModifierType>, 4194304: <flags GDK_MODIFIER_RESERVED_22_MASK of type Gdk.ModifierType>, 8388608: <flags GDK_MODIFIER_RESERVED_23_MASK of type Gdk.ModifierType>, 16777216: <flags GDK_MODIFIER_RESERVED_24_MASK of type Gdk.ModifierType>, 33554432: <flags GDK_MODIFIER_RESERVED_25_MASK of type Gdk.ModifierType>, 67108864: <flags GDK_SUPER_MASK of type Gdk.ModifierType>, 134217728: <flags GDK_HYPER_MASK of type Gdk.ModifierType>, 268435456: <flags GDK_META_MASK of type Gdk.ModifierType>, 536870912: <flags GDK_MODIFIER_RESERVED_29_MASK of type Gdk.ModifierType>, 1073741824: <flags GDK_RELEASE_MASK of type Gdk.ModifierType>, 1543512063: <flags GDK_SHIFT_MASK | GDK_LOCK_MASK | GDK_CONTROL_MASK | GDK_MOD1_MASK | GDK_MOD2_MASK | GDK_MOD3_MASK | GDK_MOD4_MASK | GDK_MOD5_MASK | GDK_BUTTON1_MASK | GDK_BUTTON2_MASK | GDK_BUTTON3_MASK | GDK_BUTTON4_MASK | GDK_BUTTON5_MASK | GDK_SUPER_MASK | GDK_HYPER_MASK | GDK_META_MASK | GDK_RELEASE_MASK | GDK_MODIFIER_MASK of type Gdk.ModifierType>}, '__info__': gi.EnumInfo(ModifierType), 'SHIFT_MASK': <flags GDK_SHIFT_MASK of type Gdk.ModifierType>, 'LOCK_MASK': <flags GDK_LOCK_MASK of type Gdk.ModifierType>, 'CONTROL_MASK': <flags GDK_CONTROL_MASK of type Gdk.ModifierType>, 'MOD1_MASK': <flags GDK_MOD1_MASK of type Gdk.ModifierType>, 'MOD2_MASK': <flags GDK_MOD2_MASK of type Gdk.ModifierType>, 'MOD3_MASK': <flags GDK_MOD3_MASK of type Gdk.ModifierType>, 'MOD4_MASK': <flags GDK_MOD4_MASK of type Gdk.ModifierType>, 'MOD5_MASK': <flags GDK_MOD5_MASK of type Gdk.ModifierType>, 'BUTTON1_MASK': <flags GDK_BUTTON1_MASK of type Gdk.ModifierType>, 'BUTTON2_MASK': <flags GDK_BUTTON2_MASK of type Gdk.ModifierType>, 'BUTTON3_MASK': <flags GDK_BUTTON3_MASK of type Gdk.ModifierType>, 'BUTTON4_MASK': <flags GDK_BUTTON4_MASK of type Gdk.ModifierType>, 'BUTTON5_MASK': <flags GDK_BUTTON5_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_13_MASK': <flags GDK_MODIFIER_RESERVED_13_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_14_MASK': <flags GDK_MODIFIER_RESERVED_14_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_15_MASK': <flags GDK_MODIFIER_RESERVED_15_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_16_MASK': <flags GDK_MODIFIER_RESERVED_16_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_17_MASK': <flags GDK_MODIFIER_RESERVED_17_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_18_MASK': <flags GDK_MODIFIER_RESERVED_18_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_19_MASK': <flags GDK_MODIFIER_RESERVED_19_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_20_MASK': <flags GDK_MODIFIER_RESERVED_20_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_21_MASK': <flags GDK_MODIFIER_RESERVED_21_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_22_MASK': <flags GDK_MODIFIER_RESERVED_22_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_23_MASK': <flags GDK_MODIFIER_RESERVED_23_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_24_MASK': <flags GDK_MODIFIER_RESERVED_24_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_25_MASK': <flags GDK_MODIFIER_RESERVED_25_MASK of type Gdk.ModifierType>, 'SUPER_MASK': <flags GDK_SUPER_MASK of type Gdk.ModifierType>, 'HYPER_MASK': <flags GDK_HYPER_MASK of type Gdk.ModifierType>, 'META_MASK': <flags GDK_META_MASK of type Gdk.ModifierType>, 'MODIFIER_RESERVED_29_MASK': <flags GDK_MODIFIER_RESERVED_29_MASK of type Gdk.ModifierType>, 'RELEASE_MASK': <flags GDK_RELEASE_MASK of type Gdk.ModifierType>, 'MODIFIER_MASK': <flags GDK_SHIFT_MASK | GDK_LOCK_MASK | GDK_CONTROL_MASK | GDK_MOD1_MASK | GDK_MOD2_MASK | GDK_MOD3_MASK | GDK_MOD4_MASK | GDK_MOD5_MASK | GDK_BUTTON1_MASK | GDK_BUTTON2_MASK | GDK_BUTTON3_MASK | GDK_BUTTON4_MASK | GDK_BUTTON5_MASK | GDK_SUPER_MASK | GDK_HYPER_MASK | GDK_META_MASK | GDK_RELEASE_MASK | GDK_MODIFIER_MASK of type Gdk.ModifierType>})"
    __flags_values__ = {
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
        1543512063: 1543512063,
    }
    __gtype__ = None # (!) real value is '<GType GdkModifierType (2579730080)>'
    __info__ = gi.EnumInfo(ModifierType)


