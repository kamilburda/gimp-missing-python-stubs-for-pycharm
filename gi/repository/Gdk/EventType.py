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


class EventType(__gobject.GEnum):
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


    2BUTTON_PRESS = 5
    3BUTTON_PRESS = 6
    BUTTON_PRESS = 4
    BUTTON_RELEASE = 7
    CLIENT_EVENT = 28
    CONFIGURE = 13
    DAMAGE = 36
    DELETE = 0
    DESTROY = 1
    DOUBLE_BUTTON_PRESS = 5
    DRAG_ENTER = 22
    DRAG_LEAVE = 23
    DRAG_MOTION = 24
    DRAG_STATUS = 25
    DROP_FINISHED = 27
    DROP_START = 26
    ENTER_NOTIFY = 10
    EVENT_LAST = 48
    EXPOSE = 2
    FOCUS_CHANGE = 12
    GRAB_BROKEN = 35
    KEY_PRESS = 8
    KEY_RELEASE = 9
    LEAVE_NOTIFY = 11
    MAP = 14
    MOTION_NOTIFY = 3
    NOTHING = -1
    OWNER_CHANGE = 34
    PAD_BUTTON_PRESS = 43
    PAD_BUTTON_RELEASE = 44
    PAD_GROUP_MODE = 47
    PAD_RING = 45
    PAD_STRIP = 46
    PROPERTY_NOTIFY = 16
    PROXIMITY_IN = 20
    PROXIMITY_OUT = 21
    SCROLL = 31
    SELECTION_CLEAR = 17
    SELECTION_NOTIFY = 19
    SELECTION_REQUEST = 18
    SETTING = 33
    TOUCHPAD_PINCH = 42
    TOUCHPAD_SWIPE = 41
    TOUCH_BEGIN = 37
    TOUCH_CANCEL = 40
    TOUCH_END = 39
    TOUCH_UPDATE = 38
    TRIPLE_BUTTON_PRESS = 6
    UNMAP = 15
    VISIBILITY_NOTIFY = 29
    WINDOW_STATE = 32
    _2BUTTON_PRESS = 5
    _3BUTTON_PRESS = 6
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gdk', '__dict__': <attribute '__dict__' of 'EventType' objects>, '__doc__': None, '__gtype__': <GType GdkEventType (2575320112)>, '__enum_values__': {-1: <enum GDK_NOTHING of type Gdk.EventType>, 0: <enum GDK_DELETE of type Gdk.EventType>, 1: <enum GDK_DESTROY of type Gdk.EventType>, 2: <enum GDK_EXPOSE of type Gdk.EventType>, 3: <enum GDK_MOTION_NOTIFY of type Gdk.EventType>, 4: <enum GDK_BUTTON_PRESS of type Gdk.EventType>, 5: <enum GDK_2BUTTON_PRESS of type Gdk.EventType>, 6: <enum GDK_3BUTTON_PRESS of type Gdk.EventType>, 7: <enum GDK_BUTTON_RELEASE of type Gdk.EventType>, 8: <enum GDK_KEY_PRESS of type Gdk.EventType>, 9: <enum GDK_KEY_RELEASE of type Gdk.EventType>, 10: <enum GDK_ENTER_NOTIFY of type Gdk.EventType>, 11: <enum GDK_LEAVE_NOTIFY of type Gdk.EventType>, 12: <enum GDK_FOCUS_CHANGE of type Gdk.EventType>, 13: <enum GDK_CONFIGURE of type Gdk.EventType>, 14: <enum GDK_MAP of type Gdk.EventType>, 15: <enum GDK_UNMAP of type Gdk.EventType>, 16: <enum GDK_PROPERTY_NOTIFY of type Gdk.EventType>, 17: <enum GDK_SELECTION_CLEAR of type Gdk.EventType>, 18: <enum GDK_SELECTION_REQUEST of type Gdk.EventType>, 19: <enum GDK_SELECTION_NOTIFY of type Gdk.EventType>, 20: <enum GDK_PROXIMITY_IN of type Gdk.EventType>, 21: <enum GDK_PROXIMITY_OUT of type Gdk.EventType>, 22: <enum GDK_DRAG_ENTER of type Gdk.EventType>, 23: <enum GDK_DRAG_LEAVE of type Gdk.EventType>, 24: <enum GDK_DRAG_MOTION of type Gdk.EventType>, 25: <enum GDK_DRAG_STATUS of type Gdk.EventType>, 26: <enum GDK_DROP_START of type Gdk.EventType>, 27: <enum GDK_DROP_FINISHED of type Gdk.EventType>, 28: <enum GDK_CLIENT_EVENT of type Gdk.EventType>, 29: <enum GDK_VISIBILITY_NOTIFY of type Gdk.EventType>, 31: <enum GDK_SCROLL of type Gdk.EventType>, 32: <enum GDK_WINDOW_STATE of type Gdk.EventType>, 33: <enum GDK_SETTING of type Gdk.EventType>, 34: <enum GDK_OWNER_CHANGE of type Gdk.EventType>, 35: <enum GDK_GRAB_BROKEN of type Gdk.EventType>, 36: <enum GDK_DAMAGE of type Gdk.EventType>, 37: <enum GDK_TOUCH_BEGIN of type Gdk.EventType>, 38: <enum GDK_TOUCH_UPDATE of type Gdk.EventType>, 39: <enum GDK_TOUCH_END of type Gdk.EventType>, 40: <enum GDK_TOUCH_CANCEL of type Gdk.EventType>, 41: <enum GDK_TOUCHPAD_SWIPE of type Gdk.EventType>, 42: <enum GDK_TOUCHPAD_PINCH of type Gdk.EventType>, 43: <enum GDK_PAD_BUTTON_PRESS of type Gdk.EventType>, 44: <enum GDK_PAD_BUTTON_RELEASE of type Gdk.EventType>, 45: <enum GDK_PAD_RING of type Gdk.EventType>, 46: <enum GDK_PAD_STRIP of type Gdk.EventType>, 47: <enum GDK_PAD_GROUP_MODE of type Gdk.EventType>, 48: <enum GDK_EVENT_LAST of type Gdk.EventType>}, '__info__': gi.EnumInfo(EventType), 'NOTHING': <enum GDK_NOTHING of type Gdk.EventType>, 'DELETE': <enum GDK_DELETE of type Gdk.EventType>, 'DESTROY': <enum GDK_DESTROY of type Gdk.EventType>, 'EXPOSE': <enum GDK_EXPOSE of type Gdk.EventType>, 'MOTION_NOTIFY': <enum GDK_MOTION_NOTIFY of type Gdk.EventType>, 'BUTTON_PRESS': <enum GDK_BUTTON_PRESS of type Gdk.EventType>, '2BUTTON_PRESS': <enum GDK_2BUTTON_PRESS of type Gdk.EventType>, 'DOUBLE_BUTTON_PRESS': <enum GDK_2BUTTON_PRESS of type Gdk.EventType>, '3BUTTON_PRESS': <enum GDK_3BUTTON_PRESS of type Gdk.EventType>, 'TRIPLE_BUTTON_PRESS': <enum GDK_3BUTTON_PRESS of type Gdk.EventType>, 'BUTTON_RELEASE': <enum GDK_BUTTON_RELEASE of type Gdk.EventType>, 'KEY_PRESS': <enum GDK_KEY_PRESS of type Gdk.EventType>, 'KEY_RELEASE': <enum GDK_KEY_RELEASE of type Gdk.EventType>, 'ENTER_NOTIFY': <enum GDK_ENTER_NOTIFY of type Gdk.EventType>, 'LEAVE_NOTIFY': <enum GDK_LEAVE_NOTIFY of type Gdk.EventType>, 'FOCUS_CHANGE': <enum GDK_FOCUS_CHANGE of type Gdk.EventType>, 'CONFIGURE': <enum GDK_CONFIGURE of type Gdk.EventType>, 'MAP': <enum GDK_MAP of type Gdk.EventType>, 'UNMAP': <enum GDK_UNMAP of type Gdk.EventType>, 'PROPERTY_NOTIFY': <enum GDK_PROPERTY_NOTIFY of type Gdk.EventType>, 'SELECTION_CLEAR': <enum GDK_SELECTION_CLEAR of type Gdk.EventType>, 'SELECTION_REQUEST': <enum GDK_SELECTION_REQUEST of type Gdk.EventType>, 'SELECTION_NOTIFY': <enum GDK_SELECTION_NOTIFY of type Gdk.EventType>, 'PROXIMITY_IN': <enum GDK_PROXIMITY_IN of type Gdk.EventType>, 'PROXIMITY_OUT': <enum GDK_PROXIMITY_OUT of type Gdk.EventType>, 'DRAG_ENTER': <enum GDK_DRAG_ENTER of type Gdk.EventType>, 'DRAG_LEAVE': <enum GDK_DRAG_LEAVE of type Gdk.EventType>, 'DRAG_MOTION': <enum GDK_DRAG_MOTION of type Gdk.EventType>, 'DRAG_STATUS': <enum GDK_DRAG_STATUS of type Gdk.EventType>, 'DROP_START': <enum GDK_DROP_START of type Gdk.EventType>, 'DROP_FINISHED': <enum GDK_DROP_FINISHED of type Gdk.EventType>, 'CLIENT_EVENT': <enum GDK_CLIENT_EVENT of type Gdk.EventType>, 'VISIBILITY_NOTIFY': <enum GDK_VISIBILITY_NOTIFY of type Gdk.EventType>, 'SCROLL': <enum GDK_SCROLL of type Gdk.EventType>, 'WINDOW_STATE': <enum GDK_WINDOW_STATE of type Gdk.EventType>, 'SETTING': <enum GDK_SETTING of type Gdk.EventType>, 'OWNER_CHANGE': <enum GDK_OWNER_CHANGE of type Gdk.EventType>, 'GRAB_BROKEN': <enum GDK_GRAB_BROKEN of type Gdk.EventType>, 'DAMAGE': <enum GDK_DAMAGE of type Gdk.EventType>, 'TOUCH_BEGIN': <enum GDK_TOUCH_BEGIN of type Gdk.EventType>, 'TOUCH_UPDATE': <enum GDK_TOUCH_UPDATE of type Gdk.EventType>, 'TOUCH_END': <enum GDK_TOUCH_END of type Gdk.EventType>, 'TOUCH_CANCEL': <enum GDK_TOUCH_CANCEL of type Gdk.EventType>, 'TOUCHPAD_SWIPE': <enum GDK_TOUCHPAD_SWIPE of type Gdk.EventType>, 'TOUCHPAD_PINCH': <enum GDK_TOUCHPAD_PINCH of type Gdk.EventType>, 'PAD_BUTTON_PRESS': <enum GDK_PAD_BUTTON_PRESS of type Gdk.EventType>, 'PAD_BUTTON_RELEASE': <enum GDK_PAD_BUTTON_RELEASE of type Gdk.EventType>, 'PAD_RING': <enum GDK_PAD_RING of type Gdk.EventType>, 'PAD_STRIP': <enum GDK_PAD_STRIP of type Gdk.EventType>, 'PAD_GROUP_MODE': <enum GDK_PAD_GROUP_MODE of type Gdk.EventType>, 'EVENT_LAST': <enum GDK_EVENT_LAST of type Gdk.EventType>, '_2BUTTON_PRESS': <enum GDK_2BUTTON_PRESS of type Gdk.EventType>, '_3BUTTON_PRESS': <enum GDK_3BUTTON_PRESS of type Gdk.EventType>})"
    __enum_values__ = {
        -1: -1,
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
    __gtype__ = None # (!) real value is '<GType GdkEventType (2575320112)>'
    __info__ = gi.EnumInfo(EventType)


