# encoding: utf-8
# module gi.repository.HarfBuzz
# from C:/Program Files/GIMP 3/lib/girepository-1.0\HarfBuzz-0.0.typelib
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


class ot_math_constant_t(__gobject.GEnum):
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


    ACCENT_BASE_HEIGHT = 6
    AXIS_HEIGHT = 5
    DELIMITED_SUB_FORMULA_MIN_HEIGHT = 2
    DISPLAY_OPERATOR_MIN_HEIGHT = 3
    FLATTENED_ACCENT_BASE_HEIGHT = 7
    FRACTION_DENOMINATOR_DISPLAY_STYLE_SHIFT_DOWN = 35
    FRACTION_DENOMINATOR_GAP_MIN = 39
    FRACTION_DENOMINATOR_SHIFT_DOWN = 34
    FRACTION_DENOM_DISPLAY_STYLE_GAP_MIN = 40
    FRACTION_NUMERATOR_DISPLAY_STYLE_SHIFT_UP = 33
    FRACTION_NUMERATOR_GAP_MIN = 36
    FRACTION_NUMERATOR_SHIFT_UP = 32
    FRACTION_NUM_DISPLAY_STYLE_GAP_MIN = 37
    FRACTION_RULE_THICKNESS = 38
    LOWER_LIMIT_BASELINE_DROP_MIN = 21
    LOWER_LIMIT_GAP_MIN = 20
    MATH_LEADING = 4
    OVERBAR_EXTRA_ASCENDER = 45
    OVERBAR_RULE_THICKNESS = 44
    OVERBAR_VERTICAL_GAP = 43
    RADICAL_DEGREE_BOTTOM_RAISE_PERCENT = 55
    RADICAL_DISPLAY_STYLE_VERTICAL_GAP = 50
    RADICAL_EXTRA_ASCENDER = 52
    RADICAL_KERN_AFTER_DEGREE = 54
    RADICAL_KERN_BEFORE_DEGREE = 53
    RADICAL_RULE_THICKNESS = 51
    RADICAL_VERTICAL_GAP = 49
    SCRIPT_PERCENT_SCALE_DOWN = 0
    SCRIPT_SCRIPT_PERCENT_SCALE_DOWN = 1
    SKEWED_FRACTION_HORIZONTAL_GAP = 41
    SKEWED_FRACTION_VERTICAL_GAP = 42
    SPACE_AFTER_SCRIPT = 17
    STACK_BOTTOM_DISPLAY_STYLE_SHIFT_DOWN = 25
    STACK_BOTTOM_SHIFT_DOWN = 24
    STACK_DISPLAY_STYLE_GAP_MIN = 27
    STACK_GAP_MIN = 26
    STACK_TOP_DISPLAY_STYLE_SHIFT_UP = 23
    STACK_TOP_SHIFT_UP = 22
    STRETCH_STACK_BOTTOM_SHIFT_DOWN = 29
    STRETCH_STACK_GAP_ABOVE_MIN = 30
    STRETCH_STACK_GAP_BELOW_MIN = 31
    STRETCH_STACK_TOP_SHIFT_UP = 28
    SUBSCRIPT_BASELINE_DROP_MIN = 10
    SUBSCRIPT_SHIFT_DOWN = 8
    SUBSCRIPT_TOP_MAX = 9
    SUB_SUPERSCRIPT_GAP_MIN = 15
    SUPERSCRIPT_BASELINE_DROP_MAX = 14
    SUPERSCRIPT_BOTTOM_MAX_WITH_SUBSCRIPT = 16
    SUPERSCRIPT_BOTTOM_MIN = 13
    SUPERSCRIPT_SHIFT_UP = 11
    SUPERSCRIPT_SHIFT_UP_CRAMPED = 12
    UNDERBAR_EXTRA_DESCENDER = 48
    UNDERBAR_RULE_THICKNESS = 47
    UNDERBAR_VERTICAL_GAP = 46
    UPPER_LIMIT_BASELINE_RISE_MIN = 19
    UPPER_LIMIT_GAP_MIN = 18
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.HarfBuzz', '__dict__': <attribute '__dict__' of 'ot_math_constant_t' objects>, '__doc__': None, '__gtype__': <GType PyHarfBuzzot_math_constant_t (2667609008)>, '__enum_values__': {0: <enum HB_OT_MATH_CONSTANT_SCRIPT_PERCENT_SCALE_DOWN of type HarfBuzz.ot_math_constant_t>, 1: <enum HB_OT_MATH_CONSTANT_SCRIPT_SCRIPT_PERCENT_SCALE_DOWN of type HarfBuzz.ot_math_constant_t>, 2: <enum HB_OT_MATH_CONSTANT_DELIMITED_SUB_FORMULA_MIN_HEIGHT of type HarfBuzz.ot_math_constant_t>, 3: <enum HB_OT_MATH_CONSTANT_DISPLAY_OPERATOR_MIN_HEIGHT of type HarfBuzz.ot_math_constant_t>, 4: <enum HB_OT_MATH_CONSTANT_MATH_LEADING of type HarfBuzz.ot_math_constant_t>, 5: <enum HB_OT_MATH_CONSTANT_AXIS_HEIGHT of type HarfBuzz.ot_math_constant_t>, 6: <enum HB_OT_MATH_CONSTANT_ACCENT_BASE_HEIGHT of type HarfBuzz.ot_math_constant_t>, 7: <enum HB_OT_MATH_CONSTANT_FLATTENED_ACCENT_BASE_HEIGHT of type HarfBuzz.ot_math_constant_t>, 8: <enum HB_OT_MATH_CONSTANT_SUBSCRIPT_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 9: <enum HB_OT_MATH_CONSTANT_SUBSCRIPT_TOP_MAX of type HarfBuzz.ot_math_constant_t>, 10: <enum HB_OT_MATH_CONSTANT_SUBSCRIPT_BASELINE_DROP_MIN of type HarfBuzz.ot_math_constant_t>, 11: <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 12: <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_SHIFT_UP_CRAMPED of type HarfBuzz.ot_math_constant_t>, 13: <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_BOTTOM_MIN of type HarfBuzz.ot_math_constant_t>, 14: <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_BASELINE_DROP_MAX of type HarfBuzz.ot_math_constant_t>, 15: <enum HB_OT_MATH_CONSTANT_SUB_SUPERSCRIPT_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 16: <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_BOTTOM_MAX_WITH_SUBSCRIPT of type HarfBuzz.ot_math_constant_t>, 17: <enum HB_OT_MATH_CONSTANT_SPACE_AFTER_SCRIPT of type HarfBuzz.ot_math_constant_t>, 18: <enum HB_OT_MATH_CONSTANT_UPPER_LIMIT_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 19: <enum HB_OT_MATH_CONSTANT_UPPER_LIMIT_BASELINE_RISE_MIN of type HarfBuzz.ot_math_constant_t>, 20: <enum HB_OT_MATH_CONSTANT_LOWER_LIMIT_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 21: <enum HB_OT_MATH_CONSTANT_LOWER_LIMIT_BASELINE_DROP_MIN of type HarfBuzz.ot_math_constant_t>, 22: <enum HB_OT_MATH_CONSTANT_STACK_TOP_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 23: <enum HB_OT_MATH_CONSTANT_STACK_TOP_DISPLAY_STYLE_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 24: <enum HB_OT_MATH_CONSTANT_STACK_BOTTOM_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 25: <enum HB_OT_MATH_CONSTANT_STACK_BOTTOM_DISPLAY_STYLE_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 26: <enum HB_OT_MATH_CONSTANT_STACK_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 27: <enum HB_OT_MATH_CONSTANT_STACK_DISPLAY_STYLE_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 28: <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_TOP_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 29: <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_BOTTOM_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 30: <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_GAP_ABOVE_MIN of type HarfBuzz.ot_math_constant_t>, 31: <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_GAP_BELOW_MIN of type HarfBuzz.ot_math_constant_t>, 32: <enum HB_OT_MATH_CONSTANT_FRACTION_NUMERATOR_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 33: <enum HB_OT_MATH_CONSTANT_FRACTION_NUMERATOR_DISPLAY_STYLE_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 34: <enum HB_OT_MATH_CONSTANT_FRACTION_DENOMINATOR_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 35: <enum HB_OT_MATH_CONSTANT_FRACTION_DENOMINATOR_DISPLAY_STYLE_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 36: <enum HB_OT_MATH_CONSTANT_FRACTION_NUMERATOR_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 37: <enum HB_OT_MATH_CONSTANT_FRACTION_NUM_DISPLAY_STYLE_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 38: <enum HB_OT_MATH_CONSTANT_FRACTION_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 39: <enum HB_OT_MATH_CONSTANT_FRACTION_DENOMINATOR_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 40: <enum HB_OT_MATH_CONSTANT_FRACTION_DENOM_DISPLAY_STYLE_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 41: <enum HB_OT_MATH_CONSTANT_SKEWED_FRACTION_HORIZONTAL_GAP of type HarfBuzz.ot_math_constant_t>, 42: <enum HB_OT_MATH_CONSTANT_SKEWED_FRACTION_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 43: <enum HB_OT_MATH_CONSTANT_OVERBAR_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 44: <enum HB_OT_MATH_CONSTANT_OVERBAR_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 45: <enum HB_OT_MATH_CONSTANT_OVERBAR_EXTRA_ASCENDER of type HarfBuzz.ot_math_constant_t>, 46: <enum HB_OT_MATH_CONSTANT_UNDERBAR_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 47: <enum HB_OT_MATH_CONSTANT_UNDERBAR_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 48: <enum HB_OT_MATH_CONSTANT_UNDERBAR_EXTRA_DESCENDER of type HarfBuzz.ot_math_constant_t>, 49: <enum HB_OT_MATH_CONSTANT_RADICAL_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 50: <enum HB_OT_MATH_CONSTANT_RADICAL_DISPLAY_STYLE_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 51: <enum HB_OT_MATH_CONSTANT_RADICAL_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 52: <enum HB_OT_MATH_CONSTANT_RADICAL_EXTRA_ASCENDER of type HarfBuzz.ot_math_constant_t>, 53: <enum HB_OT_MATH_CONSTANT_RADICAL_KERN_BEFORE_DEGREE of type HarfBuzz.ot_math_constant_t>, 54: <enum HB_OT_MATH_CONSTANT_RADICAL_KERN_AFTER_DEGREE of type HarfBuzz.ot_math_constant_t>, 55: <enum HB_OT_MATH_CONSTANT_RADICAL_DEGREE_BOTTOM_RAISE_PERCENT of type HarfBuzz.ot_math_constant_t>}, '__info__': gi.EnumInfo(ot_math_constant_t), 'SCRIPT_PERCENT_SCALE_DOWN': <enum HB_OT_MATH_CONSTANT_SCRIPT_PERCENT_SCALE_DOWN of type HarfBuzz.ot_math_constant_t>, 'SCRIPT_SCRIPT_PERCENT_SCALE_DOWN': <enum HB_OT_MATH_CONSTANT_SCRIPT_SCRIPT_PERCENT_SCALE_DOWN of type HarfBuzz.ot_math_constant_t>, 'DELIMITED_SUB_FORMULA_MIN_HEIGHT': <enum HB_OT_MATH_CONSTANT_DELIMITED_SUB_FORMULA_MIN_HEIGHT of type HarfBuzz.ot_math_constant_t>, 'DISPLAY_OPERATOR_MIN_HEIGHT': <enum HB_OT_MATH_CONSTANT_DISPLAY_OPERATOR_MIN_HEIGHT of type HarfBuzz.ot_math_constant_t>, 'MATH_LEADING': <enum HB_OT_MATH_CONSTANT_MATH_LEADING of type HarfBuzz.ot_math_constant_t>, 'AXIS_HEIGHT': <enum HB_OT_MATH_CONSTANT_AXIS_HEIGHT of type HarfBuzz.ot_math_constant_t>, 'ACCENT_BASE_HEIGHT': <enum HB_OT_MATH_CONSTANT_ACCENT_BASE_HEIGHT of type HarfBuzz.ot_math_constant_t>, 'FLATTENED_ACCENT_BASE_HEIGHT': <enum HB_OT_MATH_CONSTANT_FLATTENED_ACCENT_BASE_HEIGHT of type HarfBuzz.ot_math_constant_t>, 'SUBSCRIPT_SHIFT_DOWN': <enum HB_OT_MATH_CONSTANT_SUBSCRIPT_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 'SUBSCRIPT_TOP_MAX': <enum HB_OT_MATH_CONSTANT_SUBSCRIPT_TOP_MAX of type HarfBuzz.ot_math_constant_t>, 'SUBSCRIPT_BASELINE_DROP_MIN': <enum HB_OT_MATH_CONSTANT_SUBSCRIPT_BASELINE_DROP_MIN of type HarfBuzz.ot_math_constant_t>, 'SUPERSCRIPT_SHIFT_UP': <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 'SUPERSCRIPT_SHIFT_UP_CRAMPED': <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_SHIFT_UP_CRAMPED of type HarfBuzz.ot_math_constant_t>, 'SUPERSCRIPT_BOTTOM_MIN': <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_BOTTOM_MIN of type HarfBuzz.ot_math_constant_t>, 'SUPERSCRIPT_BASELINE_DROP_MAX': <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_BASELINE_DROP_MAX of type HarfBuzz.ot_math_constant_t>, 'SUB_SUPERSCRIPT_GAP_MIN': <enum HB_OT_MATH_CONSTANT_SUB_SUPERSCRIPT_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'SUPERSCRIPT_BOTTOM_MAX_WITH_SUBSCRIPT': <enum HB_OT_MATH_CONSTANT_SUPERSCRIPT_BOTTOM_MAX_WITH_SUBSCRIPT of type HarfBuzz.ot_math_constant_t>, 'SPACE_AFTER_SCRIPT': <enum HB_OT_MATH_CONSTANT_SPACE_AFTER_SCRIPT of type HarfBuzz.ot_math_constant_t>, 'UPPER_LIMIT_GAP_MIN': <enum HB_OT_MATH_CONSTANT_UPPER_LIMIT_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'UPPER_LIMIT_BASELINE_RISE_MIN': <enum HB_OT_MATH_CONSTANT_UPPER_LIMIT_BASELINE_RISE_MIN of type HarfBuzz.ot_math_constant_t>, 'LOWER_LIMIT_GAP_MIN': <enum HB_OT_MATH_CONSTANT_LOWER_LIMIT_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'LOWER_LIMIT_BASELINE_DROP_MIN': <enum HB_OT_MATH_CONSTANT_LOWER_LIMIT_BASELINE_DROP_MIN of type HarfBuzz.ot_math_constant_t>, 'STACK_TOP_SHIFT_UP': <enum HB_OT_MATH_CONSTANT_STACK_TOP_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 'STACK_TOP_DISPLAY_STYLE_SHIFT_UP': <enum HB_OT_MATH_CONSTANT_STACK_TOP_DISPLAY_STYLE_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 'STACK_BOTTOM_SHIFT_DOWN': <enum HB_OT_MATH_CONSTANT_STACK_BOTTOM_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 'STACK_BOTTOM_DISPLAY_STYLE_SHIFT_DOWN': <enum HB_OT_MATH_CONSTANT_STACK_BOTTOM_DISPLAY_STYLE_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 'STACK_GAP_MIN': <enum HB_OT_MATH_CONSTANT_STACK_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'STACK_DISPLAY_STYLE_GAP_MIN': <enum HB_OT_MATH_CONSTANT_STACK_DISPLAY_STYLE_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'STRETCH_STACK_TOP_SHIFT_UP': <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_TOP_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 'STRETCH_STACK_BOTTOM_SHIFT_DOWN': <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_BOTTOM_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 'STRETCH_STACK_GAP_ABOVE_MIN': <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_GAP_ABOVE_MIN of type HarfBuzz.ot_math_constant_t>, 'STRETCH_STACK_GAP_BELOW_MIN': <enum HB_OT_MATH_CONSTANT_STRETCH_STACK_GAP_BELOW_MIN of type HarfBuzz.ot_math_constant_t>, 'FRACTION_NUMERATOR_SHIFT_UP': <enum HB_OT_MATH_CONSTANT_FRACTION_NUMERATOR_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 'FRACTION_NUMERATOR_DISPLAY_STYLE_SHIFT_UP': <enum HB_OT_MATH_CONSTANT_FRACTION_NUMERATOR_DISPLAY_STYLE_SHIFT_UP of type HarfBuzz.ot_math_constant_t>, 'FRACTION_DENOMINATOR_SHIFT_DOWN': <enum HB_OT_MATH_CONSTANT_FRACTION_DENOMINATOR_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 'FRACTION_DENOMINATOR_DISPLAY_STYLE_SHIFT_DOWN': <enum HB_OT_MATH_CONSTANT_FRACTION_DENOMINATOR_DISPLAY_STYLE_SHIFT_DOWN of type HarfBuzz.ot_math_constant_t>, 'FRACTION_NUMERATOR_GAP_MIN': <enum HB_OT_MATH_CONSTANT_FRACTION_NUMERATOR_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'FRACTION_NUM_DISPLAY_STYLE_GAP_MIN': <enum HB_OT_MATH_CONSTANT_FRACTION_NUM_DISPLAY_STYLE_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'FRACTION_RULE_THICKNESS': <enum HB_OT_MATH_CONSTANT_FRACTION_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 'FRACTION_DENOMINATOR_GAP_MIN': <enum HB_OT_MATH_CONSTANT_FRACTION_DENOMINATOR_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'FRACTION_DENOM_DISPLAY_STYLE_GAP_MIN': <enum HB_OT_MATH_CONSTANT_FRACTION_DENOM_DISPLAY_STYLE_GAP_MIN of type HarfBuzz.ot_math_constant_t>, 'SKEWED_FRACTION_HORIZONTAL_GAP': <enum HB_OT_MATH_CONSTANT_SKEWED_FRACTION_HORIZONTAL_GAP of type HarfBuzz.ot_math_constant_t>, 'SKEWED_FRACTION_VERTICAL_GAP': <enum HB_OT_MATH_CONSTANT_SKEWED_FRACTION_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 'OVERBAR_VERTICAL_GAP': <enum HB_OT_MATH_CONSTANT_OVERBAR_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 'OVERBAR_RULE_THICKNESS': <enum HB_OT_MATH_CONSTANT_OVERBAR_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 'OVERBAR_EXTRA_ASCENDER': <enum HB_OT_MATH_CONSTANT_OVERBAR_EXTRA_ASCENDER of type HarfBuzz.ot_math_constant_t>, 'UNDERBAR_VERTICAL_GAP': <enum HB_OT_MATH_CONSTANT_UNDERBAR_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 'UNDERBAR_RULE_THICKNESS': <enum HB_OT_MATH_CONSTANT_UNDERBAR_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 'UNDERBAR_EXTRA_DESCENDER': <enum HB_OT_MATH_CONSTANT_UNDERBAR_EXTRA_DESCENDER of type HarfBuzz.ot_math_constant_t>, 'RADICAL_VERTICAL_GAP': <enum HB_OT_MATH_CONSTANT_RADICAL_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 'RADICAL_DISPLAY_STYLE_VERTICAL_GAP': <enum HB_OT_MATH_CONSTANT_RADICAL_DISPLAY_STYLE_VERTICAL_GAP of type HarfBuzz.ot_math_constant_t>, 'RADICAL_RULE_THICKNESS': <enum HB_OT_MATH_CONSTANT_RADICAL_RULE_THICKNESS of type HarfBuzz.ot_math_constant_t>, 'RADICAL_EXTRA_ASCENDER': <enum HB_OT_MATH_CONSTANT_RADICAL_EXTRA_ASCENDER of type HarfBuzz.ot_math_constant_t>, 'RADICAL_KERN_BEFORE_DEGREE': <enum HB_OT_MATH_CONSTANT_RADICAL_KERN_BEFORE_DEGREE of type HarfBuzz.ot_math_constant_t>, 'RADICAL_KERN_AFTER_DEGREE': <enum HB_OT_MATH_CONSTANT_RADICAL_KERN_AFTER_DEGREE of type HarfBuzz.ot_math_constant_t>, 'RADICAL_DEGREE_BOTTOM_RAISE_PERCENT': <enum HB_OT_MATH_CONSTANT_RADICAL_DEGREE_BOTTOM_RAISE_PERCENT of type HarfBuzz.ot_math_constant_t>})"
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
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
    }
    __gtype__ = None # (!) real value is '<GType PyHarfBuzzot_math_constant_t (2667609008)>'
    __info__ = gi.EnumInfo(ot_math_constant_t)


