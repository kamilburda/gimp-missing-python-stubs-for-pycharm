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


class CursorType(__gobject.GEnum):
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


    ARROW = 2
    BASED_ARROW_DOWN = 4
    BASED_ARROW_UP = 6
    BLANK_CURSOR = -2
    BOAT = 8
    BOGOSITY = 10
    BOTTOM_LEFT_CORNER = 12
    BOTTOM_RIGHT_CORNER = 14
    BOTTOM_SIDE = 16
    BOTTOM_TEE = 18
    BOX_SPIRAL = 20
    CENTER_PTR = 22
    CIRCLE = 24
    CLOCK = 26
    COFFEE_MUG = 28
    CROSS = 30
    CROSSHAIR = 34
    CROSS_REVERSE = 32
    CURSOR_IS_PIXMAP = -1
    DIAMOND_CROSS = 36
    DOT = 38
    DOTBOX = 40
    DOUBLE_ARROW = 42
    DRAFT_LARGE = 44
    DRAFT_SMALL = 46
    DRAPED_BOX = 48
    EXCHANGE = 50
    FLEUR = 52
    GOBBLER = 54
    GUMBY = 56
    HAND1 = 58
    HAND2 = 60
    HEART = 62
    ICON = 64
    IRON_CROSS = 66
    LAST_CURSOR = 153
    LEFTBUTTON = 74
    LEFT_PTR = 68
    LEFT_SIDE = 70
    LEFT_TEE = 72
    LL_ANGLE = 76
    LR_ANGLE = 78
    MAN = 80
    MIDDLEBUTTON = 82
    MOUSE = 84
    PENCIL = 86
    PIRATE = 88
    PLUS = 90
    QUESTION_ARROW = 92
    RIGHTBUTTON = 100
    RIGHT_PTR = 94
    RIGHT_SIDE = 96
    RIGHT_TEE = 98
    RTL_LOGO = 102
    SAILBOAT = 104
    SB_DOWN_ARROW = 106
    SB_H_DOUBLE_ARROW = 108
    SB_LEFT_ARROW = 110
    SB_RIGHT_ARROW = 112
    SB_UP_ARROW = 114
    SB_V_DOUBLE_ARROW = 116
    SHUTTLE = 118
    SIZING = 120
    SPIDER = 122
    SPRAYCAN = 124
    STAR = 126
    TARGET = 128
    TCROSS = 130
    TOP_LEFT_ARROW = 132
    TOP_LEFT_CORNER = 134
    TOP_RIGHT_CORNER = 136
    TOP_SIDE = 138
    TOP_TEE = 140
    TREK = 142
    UL_ANGLE = 144
    UMBRELLA = 146
    UR_ANGLE = 148
    WATCH = 150
    XTERM = 152
    X_CURSOR = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gdk', '__dict__': <attribute '__dict__' of 'CursorType' objects>, '__doc__': None, '__gtype__': <GType GdkCursorType (2579722464)>, '__enum_values__': {0: <enum GDK_X_CURSOR of type Gdk.CursorType>, 2: <enum GDK_ARROW of type Gdk.CursorType>, 4: <enum GDK_BASED_ARROW_DOWN of type Gdk.CursorType>, 6: <enum GDK_BASED_ARROW_UP of type Gdk.CursorType>, 8: <enum GDK_BOAT of type Gdk.CursorType>, 10: <enum GDK_BOGOSITY of type Gdk.CursorType>, 12: <enum GDK_BOTTOM_LEFT_CORNER of type Gdk.CursorType>, 14: <enum GDK_BOTTOM_RIGHT_CORNER of type Gdk.CursorType>, 16: <enum GDK_BOTTOM_SIDE of type Gdk.CursorType>, 18: <enum GDK_BOTTOM_TEE of type Gdk.CursorType>, 20: <enum GDK_BOX_SPIRAL of type Gdk.CursorType>, 22: <enum GDK_CENTER_PTR of type Gdk.CursorType>, 24: <enum GDK_CIRCLE of type Gdk.CursorType>, 26: <enum GDK_CLOCK of type Gdk.CursorType>, 28: <enum GDK_COFFEE_MUG of type Gdk.CursorType>, 30: <enum GDK_CROSS of type Gdk.CursorType>, 32: <enum GDK_CROSS_REVERSE of type Gdk.CursorType>, 34: <enum GDK_CROSSHAIR of type Gdk.CursorType>, 36: <enum GDK_DIAMOND_CROSS of type Gdk.CursorType>, 38: <enum GDK_DOT of type Gdk.CursorType>, 40: <enum GDK_DOTBOX of type Gdk.CursorType>, 42: <enum GDK_DOUBLE_ARROW of type Gdk.CursorType>, 44: <enum GDK_DRAFT_LARGE of type Gdk.CursorType>, 46: <enum GDK_DRAFT_SMALL of type Gdk.CursorType>, 48: <enum GDK_DRAPED_BOX of type Gdk.CursorType>, 50: <enum GDK_EXCHANGE of type Gdk.CursorType>, 52: <enum GDK_FLEUR of type Gdk.CursorType>, 54: <enum GDK_GOBBLER of type Gdk.CursorType>, 56: <enum GDK_GUMBY of type Gdk.CursorType>, 58: <enum GDK_HAND1 of type Gdk.CursorType>, 60: <enum GDK_HAND2 of type Gdk.CursorType>, 62: <enum GDK_HEART of type Gdk.CursorType>, 64: <enum GDK_ICON of type Gdk.CursorType>, 66: <enum GDK_IRON_CROSS of type Gdk.CursorType>, 68: <enum GDK_LEFT_PTR of type Gdk.CursorType>, 70: <enum GDK_LEFT_SIDE of type Gdk.CursorType>, 72: <enum GDK_LEFT_TEE of type Gdk.CursorType>, 74: <enum GDK_LEFTBUTTON of type Gdk.CursorType>, 76: <enum GDK_LL_ANGLE of type Gdk.CursorType>, 78: <enum GDK_LR_ANGLE of type Gdk.CursorType>, 80: <enum GDK_MAN of type Gdk.CursorType>, 82: <enum GDK_MIDDLEBUTTON of type Gdk.CursorType>, 84: <enum GDK_MOUSE of type Gdk.CursorType>, 86: <enum GDK_PENCIL of type Gdk.CursorType>, 88: <enum GDK_PIRATE of type Gdk.CursorType>, 90: <enum GDK_PLUS of type Gdk.CursorType>, 92: <enum GDK_QUESTION_ARROW of type Gdk.CursorType>, 94: <enum GDK_RIGHT_PTR of type Gdk.CursorType>, 96: <enum GDK_RIGHT_SIDE of type Gdk.CursorType>, 98: <enum GDK_RIGHT_TEE of type Gdk.CursorType>, 100: <enum GDK_RIGHTBUTTON of type Gdk.CursorType>, 102: <enum GDK_RTL_LOGO of type Gdk.CursorType>, 104: <enum GDK_SAILBOAT of type Gdk.CursorType>, 106: <enum GDK_SB_DOWN_ARROW of type Gdk.CursorType>, 108: <enum GDK_SB_H_DOUBLE_ARROW of type Gdk.CursorType>, 110: <enum GDK_SB_LEFT_ARROW of type Gdk.CursorType>, 112: <enum GDK_SB_RIGHT_ARROW of type Gdk.CursorType>, 114: <enum GDK_SB_UP_ARROW of type Gdk.CursorType>, 116: <enum GDK_SB_V_DOUBLE_ARROW of type Gdk.CursorType>, 118: <enum GDK_SHUTTLE of type Gdk.CursorType>, 120: <enum GDK_SIZING of type Gdk.CursorType>, 122: <enum GDK_SPIDER of type Gdk.CursorType>, 124: <enum GDK_SPRAYCAN of type Gdk.CursorType>, 126: <enum GDK_STAR of type Gdk.CursorType>, 128: <enum GDK_TARGET of type Gdk.CursorType>, 130: <enum GDK_TCROSS of type Gdk.CursorType>, 132: <enum GDK_TOP_LEFT_ARROW of type Gdk.CursorType>, 134: <enum GDK_TOP_LEFT_CORNER of type Gdk.CursorType>, 136: <enum GDK_TOP_RIGHT_CORNER of type Gdk.CursorType>, 138: <enum GDK_TOP_SIDE of type Gdk.CursorType>, 140: <enum GDK_TOP_TEE of type Gdk.CursorType>, 142: <enum GDK_TREK of type Gdk.CursorType>, 144: <enum GDK_UL_ANGLE of type Gdk.CursorType>, 146: <enum GDK_UMBRELLA of type Gdk.CursorType>, 148: <enum GDK_UR_ANGLE of type Gdk.CursorType>, 150: <enum GDK_WATCH of type Gdk.CursorType>, 152: <enum GDK_XTERM of type Gdk.CursorType>, 153: <enum GDK_LAST_CURSOR of type Gdk.CursorType>, -2: <enum GDK_BLANK_CURSOR of type Gdk.CursorType>, -1: <enum GDK_CURSOR_IS_PIXMAP of type Gdk.CursorType>}, '__info__': gi.EnumInfo(CursorType), 'X_CURSOR': <enum GDK_X_CURSOR of type Gdk.CursorType>, 'ARROW': <enum GDK_ARROW of type Gdk.CursorType>, 'BASED_ARROW_DOWN': <enum GDK_BASED_ARROW_DOWN of type Gdk.CursorType>, 'BASED_ARROW_UP': <enum GDK_BASED_ARROW_UP of type Gdk.CursorType>, 'BOAT': <enum GDK_BOAT of type Gdk.CursorType>, 'BOGOSITY': <enum GDK_BOGOSITY of type Gdk.CursorType>, 'BOTTOM_LEFT_CORNER': <enum GDK_BOTTOM_LEFT_CORNER of type Gdk.CursorType>, 'BOTTOM_RIGHT_CORNER': <enum GDK_BOTTOM_RIGHT_CORNER of type Gdk.CursorType>, 'BOTTOM_SIDE': <enum GDK_BOTTOM_SIDE of type Gdk.CursorType>, 'BOTTOM_TEE': <enum GDK_BOTTOM_TEE of type Gdk.CursorType>, 'BOX_SPIRAL': <enum GDK_BOX_SPIRAL of type Gdk.CursorType>, 'CENTER_PTR': <enum GDK_CENTER_PTR of type Gdk.CursorType>, 'CIRCLE': <enum GDK_CIRCLE of type Gdk.CursorType>, 'CLOCK': <enum GDK_CLOCK of type Gdk.CursorType>, 'COFFEE_MUG': <enum GDK_COFFEE_MUG of type Gdk.CursorType>, 'CROSS': <enum GDK_CROSS of type Gdk.CursorType>, 'CROSS_REVERSE': <enum GDK_CROSS_REVERSE of type Gdk.CursorType>, 'CROSSHAIR': <enum GDK_CROSSHAIR of type Gdk.CursorType>, 'DIAMOND_CROSS': <enum GDK_DIAMOND_CROSS of type Gdk.CursorType>, 'DOT': <enum GDK_DOT of type Gdk.CursorType>, 'DOTBOX': <enum GDK_DOTBOX of type Gdk.CursorType>, 'DOUBLE_ARROW': <enum GDK_DOUBLE_ARROW of type Gdk.CursorType>, 'DRAFT_LARGE': <enum GDK_DRAFT_LARGE of type Gdk.CursorType>, 'DRAFT_SMALL': <enum GDK_DRAFT_SMALL of type Gdk.CursorType>, 'DRAPED_BOX': <enum GDK_DRAPED_BOX of type Gdk.CursorType>, 'EXCHANGE': <enum GDK_EXCHANGE of type Gdk.CursorType>, 'FLEUR': <enum GDK_FLEUR of type Gdk.CursorType>, 'GOBBLER': <enum GDK_GOBBLER of type Gdk.CursorType>, 'GUMBY': <enum GDK_GUMBY of type Gdk.CursorType>, 'HAND1': <enum GDK_HAND1 of type Gdk.CursorType>, 'HAND2': <enum GDK_HAND2 of type Gdk.CursorType>, 'HEART': <enum GDK_HEART of type Gdk.CursorType>, 'ICON': <enum GDK_ICON of type Gdk.CursorType>, 'IRON_CROSS': <enum GDK_IRON_CROSS of type Gdk.CursorType>, 'LEFT_PTR': <enum GDK_LEFT_PTR of type Gdk.CursorType>, 'LEFT_SIDE': <enum GDK_LEFT_SIDE of type Gdk.CursorType>, 'LEFT_TEE': <enum GDK_LEFT_TEE of type Gdk.CursorType>, 'LEFTBUTTON': <enum GDK_LEFTBUTTON of type Gdk.CursorType>, 'LL_ANGLE': <enum GDK_LL_ANGLE of type Gdk.CursorType>, 'LR_ANGLE': <enum GDK_LR_ANGLE of type Gdk.CursorType>, 'MAN': <enum GDK_MAN of type Gdk.CursorType>, 'MIDDLEBUTTON': <enum GDK_MIDDLEBUTTON of type Gdk.CursorType>, 'MOUSE': <enum GDK_MOUSE of type Gdk.CursorType>, 'PENCIL': <enum GDK_PENCIL of type Gdk.CursorType>, 'PIRATE': <enum GDK_PIRATE of type Gdk.CursorType>, 'PLUS': <enum GDK_PLUS of type Gdk.CursorType>, 'QUESTION_ARROW': <enum GDK_QUESTION_ARROW of type Gdk.CursorType>, 'RIGHT_PTR': <enum GDK_RIGHT_PTR of type Gdk.CursorType>, 'RIGHT_SIDE': <enum GDK_RIGHT_SIDE of type Gdk.CursorType>, 'RIGHT_TEE': <enum GDK_RIGHT_TEE of type Gdk.CursorType>, 'RIGHTBUTTON': <enum GDK_RIGHTBUTTON of type Gdk.CursorType>, 'RTL_LOGO': <enum GDK_RTL_LOGO of type Gdk.CursorType>, 'SAILBOAT': <enum GDK_SAILBOAT of type Gdk.CursorType>, 'SB_DOWN_ARROW': <enum GDK_SB_DOWN_ARROW of type Gdk.CursorType>, 'SB_H_DOUBLE_ARROW': <enum GDK_SB_H_DOUBLE_ARROW of type Gdk.CursorType>, 'SB_LEFT_ARROW': <enum GDK_SB_LEFT_ARROW of type Gdk.CursorType>, 'SB_RIGHT_ARROW': <enum GDK_SB_RIGHT_ARROW of type Gdk.CursorType>, 'SB_UP_ARROW': <enum GDK_SB_UP_ARROW of type Gdk.CursorType>, 'SB_V_DOUBLE_ARROW': <enum GDK_SB_V_DOUBLE_ARROW of type Gdk.CursorType>, 'SHUTTLE': <enum GDK_SHUTTLE of type Gdk.CursorType>, 'SIZING': <enum GDK_SIZING of type Gdk.CursorType>, 'SPIDER': <enum GDK_SPIDER of type Gdk.CursorType>, 'SPRAYCAN': <enum GDK_SPRAYCAN of type Gdk.CursorType>, 'STAR': <enum GDK_STAR of type Gdk.CursorType>, 'TARGET': <enum GDK_TARGET of type Gdk.CursorType>, 'TCROSS': <enum GDK_TCROSS of type Gdk.CursorType>, 'TOP_LEFT_ARROW': <enum GDK_TOP_LEFT_ARROW of type Gdk.CursorType>, 'TOP_LEFT_CORNER': <enum GDK_TOP_LEFT_CORNER of type Gdk.CursorType>, 'TOP_RIGHT_CORNER': <enum GDK_TOP_RIGHT_CORNER of type Gdk.CursorType>, 'TOP_SIDE': <enum GDK_TOP_SIDE of type Gdk.CursorType>, 'TOP_TEE': <enum GDK_TOP_TEE of type Gdk.CursorType>, 'TREK': <enum GDK_TREK of type Gdk.CursorType>, 'UL_ANGLE': <enum GDK_UL_ANGLE of type Gdk.CursorType>, 'UMBRELLA': <enum GDK_UMBRELLA of type Gdk.CursorType>, 'UR_ANGLE': <enum GDK_UR_ANGLE of type Gdk.CursorType>, 'WATCH': <enum GDK_WATCH of type Gdk.CursorType>, 'XTERM': <enum GDK_XTERM of type Gdk.CursorType>, 'LAST_CURSOR': <enum GDK_LAST_CURSOR of type Gdk.CursorType>, 'BLANK_CURSOR': <enum GDK_BLANK_CURSOR of type Gdk.CursorType>, 'CURSOR_IS_PIXMAP': <enum GDK_CURSOR_IS_PIXMAP of type Gdk.CursorType>})"
    __enum_values__ = {
        -2: -2,
        -1: -1,
        0: 0,
        2: 2,
        4: 4,
        6: 6,
        8: 8,
        10: 10,
        12: 12,
        14: 14,
        16: 16,
        18: 18,
        20: 20,
        22: 22,
        24: 24,
        26: 26,
        28: 28,
        30: 30,
        32: 32,
        34: 34,
        36: 36,
        38: 38,
        40: 40,
        42: 42,
        44: 44,
        46: 46,
        48: 48,
        50: 50,
        52: 52,
        54: 54,
        56: 56,
        58: 58,
        60: 60,
        62: 62,
        64: 64,
        66: 66,
        68: 68,
        70: 70,
        72: 72,
        74: 74,
        76: 76,
        78: 78,
        80: 80,
        82: 82,
        84: 84,
        86: 86,
        88: 88,
        90: 90,
        92: 92,
        94: 94,
        96: 96,
        98: 98,
        100: 100,
        102: 102,
        104: 104,
        106: 106,
        108: 108,
        110: 110,
        112: 112,
        114: 114,
        116: 116,
        118: 118,
        120: 120,
        122: 122,
        124: 124,
        126: 126,
        128: 128,
        130: 130,
        132: 132,
        134: 134,
        136: 136,
        138: 138,
        140: 140,
        142: 142,
        144: 144,
        146: 146,
        148: 148,
        150: 150,
        152: 152,
        153: 153,
    }
    __gtype__ = None # (!) real value is '<GType GdkCursorType (2579722464)>'
    __info__ = gi.EnumInfo(CursorType)


