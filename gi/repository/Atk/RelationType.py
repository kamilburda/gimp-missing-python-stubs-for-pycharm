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


class RelationType(__gobject.GEnum):
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
        """ for_name(name:str) -> Atk.RelationType """
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
        """ get_name(type:Atk.RelationType) -> str """
        return ""

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Returns True. Exists for duck type compatibility with float.is_integer. """
        pass

    def register(self, name): # real signature unknown; restored from __doc__
        """ register(name:str) -> Atk.RelationType """
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


    CONTROLLED_BY = 1
    CONTROLLER_FOR = 2
    DESCRIBED_BY = 14
    DESCRIPTION_FOR = 15
    DETAILS = 17
    DETAILS_FOR = 18
    EMBEDDED_BY = 11
    EMBEDS = 10
    ERROR_FOR = 20
    ERROR_MESSAGE = 19
    FLOWS_FROM = 8
    FLOWS_TO = 7
    LABELLED_BY = 4
    LABEL_FOR = 3
    LAST_DEFINED = 21
    MEMBER_OF = 5
    NODE_CHILD_OF = 6
    NODE_PARENT_OF = 16
    NULL = 0
    PARENT_WINDOW_OF = 13
    POPUP_FOR = 12
    SUBWINDOW_OF = 9
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Atk', '__dict__': <attribute '__dict__' of 'RelationType' objects>, '__doc__': None, '__gtype__': <GType AtkRelationType (892677280)>, '__enum_values__': {0: <enum ATK_RELATION_NULL of type Atk.RelationType>, 1: <enum ATK_RELATION_CONTROLLED_BY of type Atk.RelationType>, 2: <enum ATK_RELATION_CONTROLLER_FOR of type Atk.RelationType>, 3: <enum ATK_RELATION_LABEL_FOR of type Atk.RelationType>, 4: <enum ATK_RELATION_LABELLED_BY of type Atk.RelationType>, 5: <enum ATK_RELATION_MEMBER_OF of type Atk.RelationType>, 6: <enum ATK_RELATION_NODE_CHILD_OF of type Atk.RelationType>, 7: <enum ATK_RELATION_FLOWS_TO of type Atk.RelationType>, 8: <enum ATK_RELATION_FLOWS_FROM of type Atk.RelationType>, 9: <enum ATK_RELATION_SUBWINDOW_OF of type Atk.RelationType>, 10: <enum ATK_RELATION_EMBEDS of type Atk.RelationType>, 11: <enum ATK_RELATION_EMBEDDED_BY of type Atk.RelationType>, 12: <enum ATK_RELATION_POPUP_FOR of type Atk.RelationType>, 13: <enum ATK_RELATION_PARENT_WINDOW_OF of type Atk.RelationType>, 14: <enum ATK_RELATION_DESCRIBED_BY of type Atk.RelationType>, 15: <enum ATK_RELATION_DESCRIPTION_FOR of type Atk.RelationType>, 16: <enum ATK_RELATION_NODE_PARENT_OF of type Atk.RelationType>, 17: <enum ATK_RELATION_DETAILS of type Atk.RelationType>, 18: <enum ATK_RELATION_DETAILS_FOR of type Atk.RelationType>, 19: <enum ATK_RELATION_ERROR_MESSAGE of type Atk.RelationType>, 20: <enum ATK_RELATION_ERROR_FOR of type Atk.RelationType>, 21: <enum ATK_RELATION_LAST_DEFINED of type Atk.RelationType>}, '__info__': gi.EnumInfo(RelationType), 'NULL': <enum ATK_RELATION_NULL of type Atk.RelationType>, 'CONTROLLED_BY': <enum ATK_RELATION_CONTROLLED_BY of type Atk.RelationType>, 'CONTROLLER_FOR': <enum ATK_RELATION_CONTROLLER_FOR of type Atk.RelationType>, 'LABEL_FOR': <enum ATK_RELATION_LABEL_FOR of type Atk.RelationType>, 'LABELLED_BY': <enum ATK_RELATION_LABELLED_BY of type Atk.RelationType>, 'MEMBER_OF': <enum ATK_RELATION_MEMBER_OF of type Atk.RelationType>, 'NODE_CHILD_OF': <enum ATK_RELATION_NODE_CHILD_OF of type Atk.RelationType>, 'FLOWS_TO': <enum ATK_RELATION_FLOWS_TO of type Atk.RelationType>, 'FLOWS_FROM': <enum ATK_RELATION_FLOWS_FROM of type Atk.RelationType>, 'SUBWINDOW_OF': <enum ATK_RELATION_SUBWINDOW_OF of type Atk.RelationType>, 'EMBEDS': <enum ATK_RELATION_EMBEDS of type Atk.RelationType>, 'EMBEDDED_BY': <enum ATK_RELATION_EMBEDDED_BY of type Atk.RelationType>, 'POPUP_FOR': <enum ATK_RELATION_POPUP_FOR of type Atk.RelationType>, 'PARENT_WINDOW_OF': <enum ATK_RELATION_PARENT_WINDOW_OF of type Atk.RelationType>, 'DESCRIBED_BY': <enum ATK_RELATION_DESCRIBED_BY of type Atk.RelationType>, 'DESCRIPTION_FOR': <enum ATK_RELATION_DESCRIPTION_FOR of type Atk.RelationType>, 'NODE_PARENT_OF': <enum ATK_RELATION_NODE_PARENT_OF of type Atk.RelationType>, 'DETAILS': <enum ATK_RELATION_DETAILS of type Atk.RelationType>, 'DETAILS_FOR': <enum ATK_RELATION_DETAILS_FOR of type Atk.RelationType>, 'ERROR_MESSAGE': <enum ATK_RELATION_ERROR_MESSAGE of type Atk.RelationType>, 'ERROR_FOR': <enum ATK_RELATION_ERROR_FOR of type Atk.RelationType>, 'LAST_DEFINED': <enum ATK_RELATION_LAST_DEFINED of type Atk.RelationType>, 'for_name': gi.FunctionInfo(for_name, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'register': gi.FunctionInfo(register, bound=None)})"
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
    }
    __gtype__ = None # (!) real value is '<GType AtkRelationType (892677280)>'
    __info__ = gi.EnumInfo(RelationType)


