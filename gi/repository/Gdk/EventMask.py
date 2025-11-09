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


class EventMask(__gobject.GFlags):
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


    ALL_EVENTS_MASK = 67108862
    BUTTON1_MOTION_MASK = 32
    BUTTON2_MOTION_MASK = 64
    BUTTON3_MOTION_MASK = 128
    BUTTON_MOTION_MASK = 16
    BUTTON_PRESS_MASK = 256
    BUTTON_RELEASE_MASK = 512
    ENTER_NOTIFY_MASK = 4096
    EXPOSURE_MASK = 2
    FOCUS_CHANGE_MASK = 16384
    KEY_PRESS_MASK = 1024
    KEY_RELEASE_MASK = 2048
    LEAVE_NOTIFY_MASK = 8192
    POINTER_MOTION_HINT_MASK = 8
    POINTER_MOTION_MASK = 4
    PROPERTY_CHANGE_MASK = 65536
    PROXIMITY_IN_MASK = 262144
    PROXIMITY_OUT_MASK = 524288
    SCROLL_MASK = 2097152
    SMOOTH_SCROLL_MASK = 8388608
    STRUCTURE_MASK = 32768
    SUBSTRUCTURE_MASK = 1048576
    TABLET_PAD_MASK = 33554432
    TOUCHPAD_GESTURE_MASK = 16777216
    TOUCH_MASK = 4194304
    VISIBILITY_NOTIFY_MASK = 131072
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gdk', '__dict__': <attribute '__dict__' of 'EventMask' objects>, '__doc__': None, '__gtype__': <GType GdkEventMask (2579723024)>, '__flags_values__': {2: <flags GDK_EXPOSURE_MASK of type Gdk.EventMask>, 4: <flags GDK_POINTER_MOTION_MASK of type Gdk.EventMask>, 8: <flags GDK_POINTER_MOTION_HINT_MASK of type Gdk.EventMask>, 16: <flags GDK_BUTTON_MOTION_MASK of type Gdk.EventMask>, 32: <flags GDK_BUTTON1_MOTION_MASK of type Gdk.EventMask>, 64: <flags GDK_BUTTON2_MOTION_MASK of type Gdk.EventMask>, 128: <flags GDK_BUTTON3_MOTION_MASK of type Gdk.EventMask>, 256: <flags GDK_BUTTON_PRESS_MASK of type Gdk.EventMask>, 512: <flags GDK_BUTTON_RELEASE_MASK of type Gdk.EventMask>, 1024: <flags GDK_KEY_PRESS_MASK of type Gdk.EventMask>, 2048: <flags GDK_KEY_RELEASE_MASK of type Gdk.EventMask>, 4096: <flags GDK_ENTER_NOTIFY_MASK of type Gdk.EventMask>, 8192: <flags GDK_LEAVE_NOTIFY_MASK of type Gdk.EventMask>, 16384: <flags GDK_FOCUS_CHANGE_MASK of type Gdk.EventMask>, 32768: <flags GDK_STRUCTURE_MASK of type Gdk.EventMask>, 65536: <flags GDK_PROPERTY_CHANGE_MASK of type Gdk.EventMask>, 131072: <flags GDK_VISIBILITY_NOTIFY_MASK of type Gdk.EventMask>, 262144: <flags GDK_PROXIMITY_IN_MASK of type Gdk.EventMask>, 524288: <flags GDK_PROXIMITY_OUT_MASK of type Gdk.EventMask>, 1048576: <flags GDK_SUBSTRUCTURE_MASK of type Gdk.EventMask>, 2097152: <flags GDK_SCROLL_MASK of type Gdk.EventMask>, 4194304: <flags GDK_TOUCH_MASK of type Gdk.EventMask>, 8388608: <flags GDK_SMOOTH_SCROLL_MASK of type Gdk.EventMask>, 16777216: <flags GDK_TOUCHPAD_GESTURE_MASK of type Gdk.EventMask>, 33554432: <flags GDK_TABLET_PAD_MASK of type Gdk.EventMask>, 67108862: <flags GDK_EXPOSURE_MASK | GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_MOTION_MASK | GDK_BUTTON1_MOTION_MASK | GDK_BUTTON2_MOTION_MASK | GDK_BUTTON3_MOTION_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK | GDK_KEY_PRESS_MASK | GDK_KEY_RELEASE_MASK | GDK_ENTER_NOTIFY_MASK | GDK_LEAVE_NOTIFY_MASK | GDK_FOCUS_CHANGE_MASK | GDK_STRUCTURE_MASK | GDK_PROPERTY_CHANGE_MASK | GDK_VISIBILITY_NOTIFY_MASK | GDK_PROXIMITY_IN_MASK | GDK_PROXIMITY_OUT_MASK | GDK_SUBSTRUCTURE_MASK | GDK_SCROLL_MASK | GDK_TOUCH_MASK | GDK_SMOOTH_SCROLL_MASK | GDK_TOUCHPAD_GESTURE_MASK | GDK_TABLET_PAD_MASK | GDK_ALL_EVENTS_MASK of type Gdk.EventMask>}, '__info__': gi.EnumInfo(EventMask), 'EXPOSURE_MASK': <flags GDK_EXPOSURE_MASK of type Gdk.EventMask>, 'POINTER_MOTION_MASK': <flags GDK_POINTER_MOTION_MASK of type Gdk.EventMask>, 'POINTER_MOTION_HINT_MASK': <flags GDK_POINTER_MOTION_HINT_MASK of type Gdk.EventMask>, 'BUTTON_MOTION_MASK': <flags GDK_BUTTON_MOTION_MASK of type Gdk.EventMask>, 'BUTTON1_MOTION_MASK': <flags GDK_BUTTON1_MOTION_MASK of type Gdk.EventMask>, 'BUTTON2_MOTION_MASK': <flags GDK_BUTTON2_MOTION_MASK of type Gdk.EventMask>, 'BUTTON3_MOTION_MASK': <flags GDK_BUTTON3_MOTION_MASK of type Gdk.EventMask>, 'BUTTON_PRESS_MASK': <flags GDK_BUTTON_PRESS_MASK of type Gdk.EventMask>, 'BUTTON_RELEASE_MASK': <flags GDK_BUTTON_RELEASE_MASK of type Gdk.EventMask>, 'KEY_PRESS_MASK': <flags GDK_KEY_PRESS_MASK of type Gdk.EventMask>, 'KEY_RELEASE_MASK': <flags GDK_KEY_RELEASE_MASK of type Gdk.EventMask>, 'ENTER_NOTIFY_MASK': <flags GDK_ENTER_NOTIFY_MASK of type Gdk.EventMask>, 'LEAVE_NOTIFY_MASK': <flags GDK_LEAVE_NOTIFY_MASK of type Gdk.EventMask>, 'FOCUS_CHANGE_MASK': <flags GDK_FOCUS_CHANGE_MASK of type Gdk.EventMask>, 'STRUCTURE_MASK': <flags GDK_STRUCTURE_MASK of type Gdk.EventMask>, 'PROPERTY_CHANGE_MASK': <flags GDK_PROPERTY_CHANGE_MASK of type Gdk.EventMask>, 'VISIBILITY_NOTIFY_MASK': <flags GDK_VISIBILITY_NOTIFY_MASK of type Gdk.EventMask>, 'PROXIMITY_IN_MASK': <flags GDK_PROXIMITY_IN_MASK of type Gdk.EventMask>, 'PROXIMITY_OUT_MASK': <flags GDK_PROXIMITY_OUT_MASK of type Gdk.EventMask>, 'SUBSTRUCTURE_MASK': <flags GDK_SUBSTRUCTURE_MASK of type Gdk.EventMask>, 'SCROLL_MASK': <flags GDK_SCROLL_MASK of type Gdk.EventMask>, 'TOUCH_MASK': <flags GDK_TOUCH_MASK of type Gdk.EventMask>, 'SMOOTH_SCROLL_MASK': <flags GDK_SMOOTH_SCROLL_MASK of type Gdk.EventMask>, 'TOUCHPAD_GESTURE_MASK': <flags GDK_TOUCHPAD_GESTURE_MASK of type Gdk.EventMask>, 'TABLET_PAD_MASK': <flags GDK_TABLET_PAD_MASK of type Gdk.EventMask>, 'ALL_EVENTS_MASK': <flags GDK_EXPOSURE_MASK | GDK_POINTER_MOTION_MASK | GDK_POINTER_MOTION_HINT_MASK | GDK_BUTTON_MOTION_MASK | GDK_BUTTON1_MOTION_MASK | GDK_BUTTON2_MOTION_MASK | GDK_BUTTON3_MOTION_MASK | GDK_BUTTON_PRESS_MASK | GDK_BUTTON_RELEASE_MASK | GDK_KEY_PRESS_MASK | GDK_KEY_RELEASE_MASK | GDK_ENTER_NOTIFY_MASK | GDK_LEAVE_NOTIFY_MASK | GDK_FOCUS_CHANGE_MASK | GDK_STRUCTURE_MASK | GDK_PROPERTY_CHANGE_MASK | GDK_VISIBILITY_NOTIFY_MASK | GDK_PROXIMITY_IN_MASK | GDK_PROXIMITY_OUT_MASK | GDK_SUBSTRUCTURE_MASK | GDK_SCROLL_MASK | GDK_TOUCH_MASK | GDK_SMOOTH_SCROLL_MASK | GDK_TOUCHPAD_GESTURE_MASK | GDK_TABLET_PAD_MASK | GDK_ALL_EVENTS_MASK of type Gdk.EventMask>})"
    __flags_values__ = {
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
        67108862: 67108862,
    }
    __gtype__ = None # (!) real value is '<GType GdkEventMask (2579723024)>'
    __info__ = gi.EnumInfo(EventMask)


