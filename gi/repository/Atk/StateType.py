# encoding: utf-8
# module gi.repository.Atk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Atk-1.0.typelib
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


class StateType(__gobject.GEnum):
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

    def for_name(self, name): # real signature unknown; restored from __doc__
        """ for_name(name:str) -> Atk.StateType """
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

    def get_name(self, type): # real signature unknown; restored from __doc__
        """ get_name(type:Atk.StateType) -> str """
        return ""

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Returns True. Exists for duck type compatibility with float.is_integer. """
        pass

    def register(self, name): # real signature unknown; restored from __doc__
        """ register(name:str) -> Atk.StateType """
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


    ACTIVE = 1
    ANIMATED = 37
    ARMED = 2
    BUSY = 3
    CHECKABLE = 39
    CHECKED = 4
    COLLAPSED = 43
    DEFAULT = 36
    DEFUNCT = 5
    EDITABLE = 6
    ENABLED = 7
    EXPANDABLE = 8
    EXPANDED = 9
    FOCUSABLE = 10
    FOCUSED = 11
    HAS_POPUP = 40
    HAS_TOOLTIP = 41
    HORIZONTAL = 12
    ICONIFIED = 13
    INDETERMINATE = 30
    INVALID = 0
    INVALID_ENTRY = 33
    LAST_DEFINED = 44
    MANAGES_DESCENDANTS = 29
    MODAL = 14
    MULTISELECTABLE = 16
    MULTI_LINE = 15
    OPAQUE = 17
    PRESSED = 18
    READ_ONLY = 42
    REQUIRED = 32
    RESIZABLE = 19
    SELECTABLE = 20
    SELECTABLE_TEXT = 35
    SELECTED = 21
    SENSITIVE = 22
    SHOWING = 23
    SINGLE_LINE = 24
    STALE = 25
    SUPPORTS_AUTOCOMPLETION = 34
    TRANSIENT = 26
    TRUNCATED = 31
    VERTICAL = 27
    VISIBLE = 28
    VISITED = 38
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Atk', '__dict__': <attribute '__dict__' of 'StateType' objects>, '__doc__': None, '__gtype__': <GType AtkStateType (892675712)>, '__enum_values__': {0: <enum ATK_STATE_INVALID of type Atk.StateType>, 1: <enum ATK_STATE_ACTIVE of type Atk.StateType>, 2: <enum ATK_STATE_ARMED of type Atk.StateType>, 3: <enum ATK_STATE_BUSY of type Atk.StateType>, 4: <enum ATK_STATE_CHECKED of type Atk.StateType>, 5: <enum ATK_STATE_DEFUNCT of type Atk.StateType>, 6: <enum ATK_STATE_EDITABLE of type Atk.StateType>, 7: <enum ATK_STATE_ENABLED of type Atk.StateType>, 8: <enum ATK_STATE_EXPANDABLE of type Atk.StateType>, 9: <enum ATK_STATE_EXPANDED of type Atk.StateType>, 10: <enum ATK_STATE_FOCUSABLE of type Atk.StateType>, 11: <enum ATK_STATE_FOCUSED of type Atk.StateType>, 12: <enum ATK_STATE_HORIZONTAL of type Atk.StateType>, 13: <enum ATK_STATE_ICONIFIED of type Atk.StateType>, 14: <enum ATK_STATE_MODAL of type Atk.StateType>, 15: <enum ATK_STATE_MULTI_LINE of type Atk.StateType>, 16: <enum ATK_STATE_MULTISELECTABLE of type Atk.StateType>, 17: <enum ATK_STATE_OPAQUE of type Atk.StateType>, 18: <enum ATK_STATE_PRESSED of type Atk.StateType>, 19: <enum ATK_STATE_RESIZABLE of type Atk.StateType>, 20: <enum ATK_STATE_SELECTABLE of type Atk.StateType>, 21: <enum ATK_STATE_SELECTED of type Atk.StateType>, 22: <enum ATK_STATE_SENSITIVE of type Atk.StateType>, 23: <enum ATK_STATE_SHOWING of type Atk.StateType>, 24: <enum ATK_STATE_SINGLE_LINE of type Atk.StateType>, 25: <enum ATK_STATE_STALE of type Atk.StateType>, 26: <enum ATK_STATE_TRANSIENT of type Atk.StateType>, 27: <enum ATK_STATE_VERTICAL of type Atk.StateType>, 28: <enum ATK_STATE_VISIBLE of type Atk.StateType>, 29: <enum ATK_STATE_MANAGES_DESCENDANTS of type Atk.StateType>, 30: <enum ATK_STATE_INDETERMINATE of type Atk.StateType>, 31: <enum ATK_STATE_TRUNCATED of type Atk.StateType>, 32: <enum ATK_STATE_REQUIRED of type Atk.StateType>, 33: <enum ATK_STATE_INVALID_ENTRY of type Atk.StateType>, 34: <enum ATK_STATE_SUPPORTS_AUTOCOMPLETION of type Atk.StateType>, 35: <enum ATK_STATE_SELECTABLE_TEXT of type Atk.StateType>, 36: <enum ATK_STATE_DEFAULT of type Atk.StateType>, 37: <enum ATK_STATE_ANIMATED of type Atk.StateType>, 38: <enum ATK_STATE_VISITED of type Atk.StateType>, 39: <enum ATK_STATE_CHECKABLE of type Atk.StateType>, 40: <enum ATK_STATE_HAS_POPUP of type Atk.StateType>, 41: <enum ATK_STATE_HAS_TOOLTIP of type Atk.StateType>, 42: <enum ATK_STATE_READ_ONLY of type Atk.StateType>, 43: <enum ATK_STATE_COLLAPSED of type Atk.StateType>, 44: <enum ATK_STATE_LAST_DEFINED of type Atk.StateType>}, '__info__': gi.EnumInfo(StateType), 'INVALID': <enum ATK_STATE_INVALID of type Atk.StateType>, 'ACTIVE': <enum ATK_STATE_ACTIVE of type Atk.StateType>, 'ARMED': <enum ATK_STATE_ARMED of type Atk.StateType>, 'BUSY': <enum ATK_STATE_BUSY of type Atk.StateType>, 'CHECKED': <enum ATK_STATE_CHECKED of type Atk.StateType>, 'DEFUNCT': <enum ATK_STATE_DEFUNCT of type Atk.StateType>, 'EDITABLE': <enum ATK_STATE_EDITABLE of type Atk.StateType>, 'ENABLED': <enum ATK_STATE_ENABLED of type Atk.StateType>, 'EXPANDABLE': <enum ATK_STATE_EXPANDABLE of type Atk.StateType>, 'EXPANDED': <enum ATK_STATE_EXPANDED of type Atk.StateType>, 'FOCUSABLE': <enum ATK_STATE_FOCUSABLE of type Atk.StateType>, 'FOCUSED': <enum ATK_STATE_FOCUSED of type Atk.StateType>, 'HORIZONTAL': <enum ATK_STATE_HORIZONTAL of type Atk.StateType>, 'ICONIFIED': <enum ATK_STATE_ICONIFIED of type Atk.StateType>, 'MODAL': <enum ATK_STATE_MODAL of type Atk.StateType>, 'MULTI_LINE': <enum ATK_STATE_MULTI_LINE of type Atk.StateType>, 'MULTISELECTABLE': <enum ATK_STATE_MULTISELECTABLE of type Atk.StateType>, 'OPAQUE': <enum ATK_STATE_OPAQUE of type Atk.StateType>, 'PRESSED': <enum ATK_STATE_PRESSED of type Atk.StateType>, 'RESIZABLE': <enum ATK_STATE_RESIZABLE of type Atk.StateType>, 'SELECTABLE': <enum ATK_STATE_SELECTABLE of type Atk.StateType>, 'SELECTED': <enum ATK_STATE_SELECTED of type Atk.StateType>, 'SENSITIVE': <enum ATK_STATE_SENSITIVE of type Atk.StateType>, 'SHOWING': <enum ATK_STATE_SHOWING of type Atk.StateType>, 'SINGLE_LINE': <enum ATK_STATE_SINGLE_LINE of type Atk.StateType>, 'STALE': <enum ATK_STATE_STALE of type Atk.StateType>, 'TRANSIENT': <enum ATK_STATE_TRANSIENT of type Atk.StateType>, 'VERTICAL': <enum ATK_STATE_VERTICAL of type Atk.StateType>, 'VISIBLE': <enum ATK_STATE_VISIBLE of type Atk.StateType>, 'MANAGES_DESCENDANTS': <enum ATK_STATE_MANAGES_DESCENDANTS of type Atk.StateType>, 'INDETERMINATE': <enum ATK_STATE_INDETERMINATE of type Atk.StateType>, 'TRUNCATED': <enum ATK_STATE_TRUNCATED of type Atk.StateType>, 'REQUIRED': <enum ATK_STATE_REQUIRED of type Atk.StateType>, 'INVALID_ENTRY': <enum ATK_STATE_INVALID_ENTRY of type Atk.StateType>, 'SUPPORTS_AUTOCOMPLETION': <enum ATK_STATE_SUPPORTS_AUTOCOMPLETION of type Atk.StateType>, 'SELECTABLE_TEXT': <enum ATK_STATE_SELECTABLE_TEXT of type Atk.StateType>, 'DEFAULT': <enum ATK_STATE_DEFAULT of type Atk.StateType>, 'ANIMATED': <enum ATK_STATE_ANIMATED of type Atk.StateType>, 'VISITED': <enum ATK_STATE_VISITED of type Atk.StateType>, 'CHECKABLE': <enum ATK_STATE_CHECKABLE of type Atk.StateType>, 'HAS_POPUP': <enum ATK_STATE_HAS_POPUP of type Atk.StateType>, 'HAS_TOOLTIP': <enum ATK_STATE_HAS_TOOLTIP of type Atk.StateType>, 'READ_ONLY': <enum ATK_STATE_READ_ONLY of type Atk.StateType>, 'COLLAPSED': <enum ATK_STATE_COLLAPSED of type Atk.StateType>, 'LAST_DEFINED': <enum ATK_STATE_LAST_DEFINED of type Atk.StateType>, 'for_name': gi.FunctionInfo(for_name, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'register': gi.FunctionInfo(register, bound=None)})"
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
    __gtype__ = None # (!) real value is '<GType AtkStateType (892675712)>'
    __info__ = gi.EnumInfo(StateType)


