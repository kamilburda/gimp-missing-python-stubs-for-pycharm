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


class RegexError(__gobject.GEnum):
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


    ASSERTION_EXPECTED = 128
    BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN = 159
    BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED = 166
    CHARACTER_VALUE_TOO_LARGE = 176
    COMPILE = 0
    DEFINE_REPETION = 155
    DUPLICATE_SUBPATTERN_NAME = 143
    EXPRESSION_TOO_LARGE = 120
    EXTRA_SUBPATTERN_NAME = 165
    HEX_CODE_TOO_LARGE = 134
    INCONSISTENT_NEWLINE_OPTIONS = 156
    INEXISTENT_SUBPATTERN_REFERENCE = 115
    INFINITE_LOOP = 140
    INTERNAL = 4
    INVALID_CONDITION = 135
    INVALID_CONTROL_CHAR = 168
    INVALID_DATA_CHARACTER = 164
    INVALID_ESCAPE_IN_CHARACTER_CLASS = 107
    INVALID_OCTAL_VALUE = 151
    INVALID_RELATIVE_REFERENCE = 158
    MALFORMED_CONDITION = 126
    MALFORMED_PROPERTY = 146
    MATCH = 3
    MEMORY_ERROR = 121
    MISSING_BACK_REFERENCE = 157
    MISSING_CONTROL_CHAR = 102
    MISSING_DIGIT = 163
    MISSING_NAME = 169
    MISSING_SUBPATTERN_NAME = 162
    MISSING_SUBPATTERN_NAME_TERMINATOR = 142
    NAME_TOO_LONG = 175
    NOTHING_TO_REPEAT = 109
    NOT_SUPPORTED_IN_CLASS = 171
    NUMBER_TOO_BIG = 161
    OPTIMIZE = 1
    POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED = 131
    POSIX_NAMED_CLASS_OUTSIDE_CLASS = 113
    QUANTIFIERS_OUT_OF_ORDER = 104
    QUANTIFIER_TOO_BIG = 105
    RANGE_OUT_OF_ORDER = 108
    REPLACE = 2
    SINGLE_BYTE_MATCH_IN_LOOKBEHIND = 136
    STRAY_BACKSLASH = 101
    SUBPATTERN_NAME_TOO_LONG = 148
    TOO_MANY_BRANCHES_IN_DEFINE = 154
    TOO_MANY_CONDITIONAL_BRANCHES = 127
    TOO_MANY_FORWARD_REFERENCES = 172
    TOO_MANY_SUBPATTERNS = 149
    UNKNOWN_BACKTRACKING_CONTROL_VERB = 160
    UNKNOWN_POSIX_CLASS_NAME = 130
    UNKNOWN_PROPERTY = 147
    UNMATCHED_PARENTHESIS = 114
    UNRECOGNIZED_CHARACTER = 112
    UNRECOGNIZED_ESCAPE = 103
    UNTERMINATED_CHARACTER_CLASS = 106
    UNTERMINATED_COMMENT = 118
    VARIABLE_LENGTH_LOOKBEHIND = 125
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'RegexError' objects>, '__doc__': None, '__gtype__': <GType PyGLibRegexError (163509696)>, '__enum_values__': {0: <enum G_REGEX_ERROR_COMPILE of type GLib.RegexError>, 1: <enum G_REGEX_ERROR_OPTIMIZE of type GLib.RegexError>, 2: <enum G_REGEX_ERROR_REPLACE of type GLib.RegexError>, 3: <enum G_REGEX_ERROR_MATCH of type GLib.RegexError>, 4: <enum G_REGEX_ERROR_INTERNAL of type GLib.RegexError>, 101: <enum G_REGEX_ERROR_STRAY_BACKSLASH of type GLib.RegexError>, 102: <enum G_REGEX_ERROR_MISSING_CONTROL_CHAR of type GLib.RegexError>, 103: <enum G_REGEX_ERROR_UNRECOGNIZED_ESCAPE of type GLib.RegexError>, 104: <enum G_REGEX_ERROR_QUANTIFIERS_OUT_OF_ORDER of type GLib.RegexError>, 105: <enum G_REGEX_ERROR_QUANTIFIER_TOO_BIG of type GLib.RegexError>, 106: <enum G_REGEX_ERROR_UNTERMINATED_CHARACTER_CLASS of type GLib.RegexError>, 107: <enum G_REGEX_ERROR_INVALID_ESCAPE_IN_CHARACTER_CLASS of type GLib.RegexError>, 108: <enum G_REGEX_ERROR_RANGE_OUT_OF_ORDER of type GLib.RegexError>, 109: <enum G_REGEX_ERROR_NOTHING_TO_REPEAT of type GLib.RegexError>, 112: <enum G_REGEX_ERROR_UNRECOGNIZED_CHARACTER of type GLib.RegexError>, 113: <enum G_REGEX_ERROR_POSIX_NAMED_CLASS_OUTSIDE_CLASS of type GLib.RegexError>, 114: <enum G_REGEX_ERROR_UNMATCHED_PARENTHESIS of type GLib.RegexError>, 115: <enum G_REGEX_ERROR_INEXISTENT_SUBPATTERN_REFERENCE of type GLib.RegexError>, 118: <enum G_REGEX_ERROR_UNTERMINATED_COMMENT of type GLib.RegexError>, 120: <enum G_REGEX_ERROR_EXPRESSION_TOO_LARGE of type GLib.RegexError>, 121: <enum G_REGEX_ERROR_MEMORY_ERROR of type GLib.RegexError>, 125: <enum G_REGEX_ERROR_VARIABLE_LENGTH_LOOKBEHIND of type GLib.RegexError>, 126: <enum G_REGEX_ERROR_MALFORMED_CONDITION of type GLib.RegexError>, 127: <enum G_REGEX_ERROR_TOO_MANY_CONDITIONAL_BRANCHES of type GLib.RegexError>, 128: <enum G_REGEX_ERROR_ASSERTION_EXPECTED of type GLib.RegexError>, 130: <enum G_REGEX_ERROR_UNKNOWN_POSIX_CLASS_NAME of type GLib.RegexError>, 131: <enum G_REGEX_ERROR_POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED of type GLib.RegexError>, 134: <enum G_REGEX_ERROR_HEX_CODE_TOO_LARGE of type GLib.RegexError>, 135: <enum G_REGEX_ERROR_INVALID_CONDITION of type GLib.RegexError>, 136: <enum G_REGEX_ERROR_SINGLE_BYTE_MATCH_IN_LOOKBEHIND of type GLib.RegexError>, 140: <enum G_REGEX_ERROR_INFINITE_LOOP of type GLib.RegexError>, 142: <enum G_REGEX_ERROR_MISSING_SUBPATTERN_NAME_TERMINATOR of type GLib.RegexError>, 143: <enum G_REGEX_ERROR_DUPLICATE_SUBPATTERN_NAME of type GLib.RegexError>, 146: <enum G_REGEX_ERROR_MALFORMED_PROPERTY of type GLib.RegexError>, 147: <enum G_REGEX_ERROR_UNKNOWN_PROPERTY of type GLib.RegexError>, 148: <enum G_REGEX_ERROR_SUBPATTERN_NAME_TOO_LONG of type GLib.RegexError>, 149: <enum G_REGEX_ERROR_TOO_MANY_SUBPATTERNS of type GLib.RegexError>, 151: <enum G_REGEX_ERROR_INVALID_OCTAL_VALUE of type GLib.RegexError>, 154: <enum G_REGEX_ERROR_TOO_MANY_BRANCHES_IN_DEFINE of type GLib.RegexError>, 155: <enum G_REGEX_ERROR_DEFINE_REPETION of type GLib.RegexError>, 156: <enum G_REGEX_ERROR_INCONSISTENT_NEWLINE_OPTIONS of type GLib.RegexError>, 157: <enum G_REGEX_ERROR_MISSING_BACK_REFERENCE of type GLib.RegexError>, 158: <enum G_REGEX_ERROR_INVALID_RELATIVE_REFERENCE of type GLib.RegexError>, 159: <enum G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN of type GLib.RegexError>, 160: <enum G_REGEX_ERROR_UNKNOWN_BACKTRACKING_CONTROL_VERB of type GLib.RegexError>, 161: <enum G_REGEX_ERROR_NUMBER_TOO_BIG of type GLib.RegexError>, 162: <enum G_REGEX_ERROR_MISSING_SUBPATTERN_NAME of type GLib.RegexError>, 163: <enum G_REGEX_ERROR_MISSING_DIGIT of type GLib.RegexError>, 164: <enum G_REGEX_ERROR_INVALID_DATA_CHARACTER of type GLib.RegexError>, 165: <enum G_REGEX_ERROR_EXTRA_SUBPATTERN_NAME of type GLib.RegexError>, 166: <enum G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED of type GLib.RegexError>, 168: <enum G_REGEX_ERROR_INVALID_CONTROL_CHAR of type GLib.RegexError>, 169: <enum G_REGEX_ERROR_MISSING_NAME of type GLib.RegexError>, 171: <enum G_REGEX_ERROR_NOT_SUPPORTED_IN_CLASS of type GLib.RegexError>, 172: <enum G_REGEX_ERROR_TOO_MANY_FORWARD_REFERENCES of type GLib.RegexError>, 175: <enum G_REGEX_ERROR_NAME_TOO_LONG of type GLib.RegexError>, 176: <enum G_REGEX_ERROR_CHARACTER_VALUE_TOO_LARGE of type GLib.RegexError>}, '__info__': gi.EnumInfo(RegexError), 'COMPILE': <enum G_REGEX_ERROR_COMPILE of type GLib.RegexError>, 'OPTIMIZE': <enum G_REGEX_ERROR_OPTIMIZE of type GLib.RegexError>, 'REPLACE': <enum G_REGEX_ERROR_REPLACE of type GLib.RegexError>, 'MATCH': <enum G_REGEX_ERROR_MATCH of type GLib.RegexError>, 'INTERNAL': <enum G_REGEX_ERROR_INTERNAL of type GLib.RegexError>, 'STRAY_BACKSLASH': <enum G_REGEX_ERROR_STRAY_BACKSLASH of type GLib.RegexError>, 'MISSING_CONTROL_CHAR': <enum G_REGEX_ERROR_MISSING_CONTROL_CHAR of type GLib.RegexError>, 'UNRECOGNIZED_ESCAPE': <enum G_REGEX_ERROR_UNRECOGNIZED_ESCAPE of type GLib.RegexError>, 'QUANTIFIERS_OUT_OF_ORDER': <enum G_REGEX_ERROR_QUANTIFIERS_OUT_OF_ORDER of type GLib.RegexError>, 'QUANTIFIER_TOO_BIG': <enum G_REGEX_ERROR_QUANTIFIER_TOO_BIG of type GLib.RegexError>, 'UNTERMINATED_CHARACTER_CLASS': <enum G_REGEX_ERROR_UNTERMINATED_CHARACTER_CLASS of type GLib.RegexError>, 'INVALID_ESCAPE_IN_CHARACTER_CLASS': <enum G_REGEX_ERROR_INVALID_ESCAPE_IN_CHARACTER_CLASS of type GLib.RegexError>, 'RANGE_OUT_OF_ORDER': <enum G_REGEX_ERROR_RANGE_OUT_OF_ORDER of type GLib.RegexError>, 'NOTHING_TO_REPEAT': <enum G_REGEX_ERROR_NOTHING_TO_REPEAT of type GLib.RegexError>, 'UNRECOGNIZED_CHARACTER': <enum G_REGEX_ERROR_UNRECOGNIZED_CHARACTER of type GLib.RegexError>, 'POSIX_NAMED_CLASS_OUTSIDE_CLASS': <enum G_REGEX_ERROR_POSIX_NAMED_CLASS_OUTSIDE_CLASS of type GLib.RegexError>, 'UNMATCHED_PARENTHESIS': <enum G_REGEX_ERROR_UNMATCHED_PARENTHESIS of type GLib.RegexError>, 'INEXISTENT_SUBPATTERN_REFERENCE': <enum G_REGEX_ERROR_INEXISTENT_SUBPATTERN_REFERENCE of type GLib.RegexError>, 'UNTERMINATED_COMMENT': <enum G_REGEX_ERROR_UNTERMINATED_COMMENT of type GLib.RegexError>, 'EXPRESSION_TOO_LARGE': <enum G_REGEX_ERROR_EXPRESSION_TOO_LARGE of type GLib.RegexError>, 'MEMORY_ERROR': <enum G_REGEX_ERROR_MEMORY_ERROR of type GLib.RegexError>, 'VARIABLE_LENGTH_LOOKBEHIND': <enum G_REGEX_ERROR_VARIABLE_LENGTH_LOOKBEHIND of type GLib.RegexError>, 'MALFORMED_CONDITION': <enum G_REGEX_ERROR_MALFORMED_CONDITION of type GLib.RegexError>, 'TOO_MANY_CONDITIONAL_BRANCHES': <enum G_REGEX_ERROR_TOO_MANY_CONDITIONAL_BRANCHES of type GLib.RegexError>, 'ASSERTION_EXPECTED': <enum G_REGEX_ERROR_ASSERTION_EXPECTED of type GLib.RegexError>, 'UNKNOWN_POSIX_CLASS_NAME': <enum G_REGEX_ERROR_UNKNOWN_POSIX_CLASS_NAME of type GLib.RegexError>, 'POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED': <enum G_REGEX_ERROR_POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED of type GLib.RegexError>, 'HEX_CODE_TOO_LARGE': <enum G_REGEX_ERROR_HEX_CODE_TOO_LARGE of type GLib.RegexError>, 'INVALID_CONDITION': <enum G_REGEX_ERROR_INVALID_CONDITION of type GLib.RegexError>, 'SINGLE_BYTE_MATCH_IN_LOOKBEHIND': <enum G_REGEX_ERROR_SINGLE_BYTE_MATCH_IN_LOOKBEHIND of type GLib.RegexError>, 'INFINITE_LOOP': <enum G_REGEX_ERROR_INFINITE_LOOP of type GLib.RegexError>, 'MISSING_SUBPATTERN_NAME_TERMINATOR': <enum G_REGEX_ERROR_MISSING_SUBPATTERN_NAME_TERMINATOR of type GLib.RegexError>, 'DUPLICATE_SUBPATTERN_NAME': <enum G_REGEX_ERROR_DUPLICATE_SUBPATTERN_NAME of type GLib.RegexError>, 'MALFORMED_PROPERTY': <enum G_REGEX_ERROR_MALFORMED_PROPERTY of type GLib.RegexError>, 'UNKNOWN_PROPERTY': <enum G_REGEX_ERROR_UNKNOWN_PROPERTY of type GLib.RegexError>, 'SUBPATTERN_NAME_TOO_LONG': <enum G_REGEX_ERROR_SUBPATTERN_NAME_TOO_LONG of type GLib.RegexError>, 'TOO_MANY_SUBPATTERNS': <enum G_REGEX_ERROR_TOO_MANY_SUBPATTERNS of type GLib.RegexError>, 'INVALID_OCTAL_VALUE': <enum G_REGEX_ERROR_INVALID_OCTAL_VALUE of type GLib.RegexError>, 'TOO_MANY_BRANCHES_IN_DEFINE': <enum G_REGEX_ERROR_TOO_MANY_BRANCHES_IN_DEFINE of type GLib.RegexError>, 'DEFINE_REPETION': <enum G_REGEX_ERROR_DEFINE_REPETION of type GLib.RegexError>, 'INCONSISTENT_NEWLINE_OPTIONS': <enum G_REGEX_ERROR_INCONSISTENT_NEWLINE_OPTIONS of type GLib.RegexError>, 'MISSING_BACK_REFERENCE': <enum G_REGEX_ERROR_MISSING_BACK_REFERENCE of type GLib.RegexError>, 'INVALID_RELATIVE_REFERENCE': <enum G_REGEX_ERROR_INVALID_RELATIVE_REFERENCE of type GLib.RegexError>, 'BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN': <enum G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN of type GLib.RegexError>, 'UNKNOWN_BACKTRACKING_CONTROL_VERB': <enum G_REGEX_ERROR_UNKNOWN_BACKTRACKING_CONTROL_VERB of type GLib.RegexError>, 'NUMBER_TOO_BIG': <enum G_REGEX_ERROR_NUMBER_TOO_BIG of type GLib.RegexError>, 'MISSING_SUBPATTERN_NAME': <enum G_REGEX_ERROR_MISSING_SUBPATTERN_NAME of type GLib.RegexError>, 'MISSING_DIGIT': <enum G_REGEX_ERROR_MISSING_DIGIT of type GLib.RegexError>, 'INVALID_DATA_CHARACTER': <enum G_REGEX_ERROR_INVALID_DATA_CHARACTER of type GLib.RegexError>, 'EXTRA_SUBPATTERN_NAME': <enum G_REGEX_ERROR_EXTRA_SUBPATTERN_NAME of type GLib.RegexError>, 'BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED': <enum G_REGEX_ERROR_BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED of type GLib.RegexError>, 'INVALID_CONTROL_CHAR': <enum G_REGEX_ERROR_INVALID_CONTROL_CHAR of type GLib.RegexError>, 'MISSING_NAME': <enum G_REGEX_ERROR_MISSING_NAME of type GLib.RegexError>, 'NOT_SUPPORTED_IN_CLASS': <enum G_REGEX_ERROR_NOT_SUPPORTED_IN_CLASS of type GLib.RegexError>, 'TOO_MANY_FORWARD_REFERENCES': <enum G_REGEX_ERROR_TOO_MANY_FORWARD_REFERENCES of type GLib.RegexError>, 'NAME_TOO_LONG': <enum G_REGEX_ERROR_NAME_TOO_LONG of type GLib.RegexError>, 'CHARACTER_VALUE_TOO_LARGE': <enum G_REGEX_ERROR_CHARACTER_VALUE_TOO_LARGE of type GLib.RegexError>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        112: 112,
        113: 113,
        114: 114,
        115: 115,
        118: 118,
        120: 120,
        121: 121,
        125: 125,
        126: 126,
        127: 127,
        128: 128,
        130: 130,
        131: 131,
        134: 134,
        135: 135,
        136: 136,
        140: 140,
        142: 142,
        143: 143,
        146: 146,
        147: 147,
        148: 148,
        149: 149,
        151: 151,
        154: 154,
        155: 155,
        156: 156,
        157: 157,
        158: 158,
        159: 159,
        160: 160,
        161: 161,
        162: 162,
        163: 163,
        164: 164,
        165: 165,
        166: 166,
        168: 168,
        169: 169,
        171: 171,
        172: 172,
        175: 175,
        176: 176,
    }
    __gtype__ = None # (!) real value is '<GType PyGLibRegexError (163509696)>'
    __info__ = gi.EnumInfo(RegexError)


