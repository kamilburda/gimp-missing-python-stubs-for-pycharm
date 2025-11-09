# encoding: utf-8
# module gi.repository.Poppler
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Poppler-0.18.typelib
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


class StructureElementKind(__gobject.GEnum):
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


    ANNOT = 14
    ARTICLE = 4
    BIBENTRY = 11
    BLOCKQUOTE = 15
    CAPTION = 16
    CODE = 12
    CONTENT = 0
    DIV = 6
    DOCUMENT = 2
    FIGURE = 48
    FORM = 50
    FORMULA = 49
    HEADING = 23
    HEADING_1 = 24
    HEADING_2 = 25
    HEADING_3 = 26
    HEADING_4 = 27
    HEADING_5 = 28
    HEADING_6 = 29
    INDEX = 20
    LINK = 13
    LIST = 30
    LIST_BODY = 33
    LIST_ITEM = 31
    LIST_LABEL = 32
    NONSTRUCT = 17
    NOTE = 9
    OBJECT_REFERENCE = 1
    PARAGRAPH = 22
    PART = 3
    PRIVATE = 21
    QUOTE = 8
    REFERENCE = 10
    RUBY = 41
    RUBY_ANNOT_TEXT = 43
    RUBY_BASE_TEXT = 42
    RUBY_PUNCTUATION = 44
    SECTION = 5
    SPAN = 7
    TABLE = 34
    TABLE_BODY = 40
    TABLE_DATA = 37
    TABLE_FOOTER = 39
    TABLE_HEADER = 38
    TABLE_HEADING = 36
    TABLE_ROW = 35
    TOC = 18
    TOC_ITEM = 19
    WARICHU = 45
    WARICHU_PUNCTUATION = 47
    WARICHU_TEXT = 46
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Poppler', '__dict__': <attribute '__dict__' of 'StructureElementKind' objects>, '__doc__': None, '__gtype__': <GType PopplerStructureElementKind (3984841280)>, '__enum_values__': {0: <enum POPPLER_STRUCTURE_ELEMENT_CONTENT of type Poppler.StructureElementKind>, 1: <enum POPPLER_STRUCTURE_ELEMENT_OBJECT_REFERENCE of type Poppler.StructureElementKind>, 2: <enum POPPLER_STRUCTURE_ELEMENT_DOCUMENT of type Poppler.StructureElementKind>, 3: <enum POPPLER_STRUCTURE_ELEMENT_PART of type Poppler.StructureElementKind>, 4: <enum POPPLER_STRUCTURE_ELEMENT_ARTICLE of type Poppler.StructureElementKind>, 5: <enum POPPLER_STRUCTURE_ELEMENT_SECTION of type Poppler.StructureElementKind>, 6: <enum POPPLER_STRUCTURE_ELEMENT_DIV of type Poppler.StructureElementKind>, 7: <enum POPPLER_STRUCTURE_ELEMENT_SPAN of type Poppler.StructureElementKind>, 8: <enum POPPLER_STRUCTURE_ELEMENT_QUOTE of type Poppler.StructureElementKind>, 9: <enum POPPLER_STRUCTURE_ELEMENT_NOTE of type Poppler.StructureElementKind>, 10: <enum POPPLER_STRUCTURE_ELEMENT_REFERENCE of type Poppler.StructureElementKind>, 11: <enum POPPLER_STRUCTURE_ELEMENT_BIBENTRY of type Poppler.StructureElementKind>, 12: <enum POPPLER_STRUCTURE_ELEMENT_CODE of type Poppler.StructureElementKind>, 13: <enum POPPLER_STRUCTURE_ELEMENT_LINK of type Poppler.StructureElementKind>, 14: <enum POPPLER_STRUCTURE_ELEMENT_ANNOT of type Poppler.StructureElementKind>, 15: <enum POPPLER_STRUCTURE_ELEMENT_BLOCKQUOTE of type Poppler.StructureElementKind>, 16: <enum POPPLER_STRUCTURE_ELEMENT_CAPTION of type Poppler.StructureElementKind>, 17: <enum POPPLER_STRUCTURE_ELEMENT_NONSTRUCT of type Poppler.StructureElementKind>, 18: <enum POPPLER_STRUCTURE_ELEMENT_TOC of type Poppler.StructureElementKind>, 19: <enum POPPLER_STRUCTURE_ELEMENT_TOC_ITEM of type Poppler.StructureElementKind>, 20: <enum POPPLER_STRUCTURE_ELEMENT_INDEX of type Poppler.StructureElementKind>, 21: <enum POPPLER_STRUCTURE_ELEMENT_PRIVATE of type Poppler.StructureElementKind>, 22: <enum POPPLER_STRUCTURE_ELEMENT_PARAGRAPH of type Poppler.StructureElementKind>, 23: <enum POPPLER_STRUCTURE_ELEMENT_HEADING of type Poppler.StructureElementKind>, 24: <enum POPPLER_STRUCTURE_ELEMENT_HEADING_1 of type Poppler.StructureElementKind>, 25: <enum POPPLER_STRUCTURE_ELEMENT_HEADING_2 of type Poppler.StructureElementKind>, 26: <enum POPPLER_STRUCTURE_ELEMENT_HEADING_3 of type Poppler.StructureElementKind>, 27: <enum POPPLER_STRUCTURE_ELEMENT_HEADING_4 of type Poppler.StructureElementKind>, 28: <enum POPPLER_STRUCTURE_ELEMENT_HEADING_5 of type Poppler.StructureElementKind>, 29: <enum POPPLER_STRUCTURE_ELEMENT_HEADING_6 of type Poppler.StructureElementKind>, 30: <enum POPPLER_STRUCTURE_ELEMENT_LIST of type Poppler.StructureElementKind>, 31: <enum POPPLER_STRUCTURE_ELEMENT_LIST_ITEM of type Poppler.StructureElementKind>, 32: <enum POPPLER_STRUCTURE_ELEMENT_LIST_LABEL of type Poppler.StructureElementKind>, 33: <enum POPPLER_STRUCTURE_ELEMENT_LIST_BODY of type Poppler.StructureElementKind>, 34: <enum POPPLER_STRUCTURE_ELEMENT_TABLE of type Poppler.StructureElementKind>, 35: <enum POPPLER_STRUCTURE_ELEMENT_TABLE_ROW of type Poppler.StructureElementKind>, 36: <enum POPPLER_STRUCTURE_ELEMENT_TABLE_HEADING of type Poppler.StructureElementKind>, 37: <enum POPPLER_STRUCTURE_ELEMENT_TABLE_DATA of type Poppler.StructureElementKind>, 38: <enum POPPLER_STRUCTURE_ELEMENT_TABLE_HEADER of type Poppler.StructureElementKind>, 39: <enum POPPLER_STRUCTURE_ELEMENT_TABLE_FOOTER of type Poppler.StructureElementKind>, 40: <enum POPPLER_STRUCTURE_ELEMENT_TABLE_BODY of type Poppler.StructureElementKind>, 41: <enum POPPLER_STRUCTURE_ELEMENT_RUBY of type Poppler.StructureElementKind>, 42: <enum POPPLER_STRUCTURE_ELEMENT_RUBY_BASE_TEXT of type Poppler.StructureElementKind>, 43: <enum POPPLER_STRUCTURE_ELEMENT_RUBY_ANNOT_TEXT of type Poppler.StructureElementKind>, 44: <enum POPPLER_STRUCTURE_ELEMENT_RUBY_PUNCTUATION of type Poppler.StructureElementKind>, 45: <enum POPPLER_STRUCTURE_ELEMENT_WARICHU of type Poppler.StructureElementKind>, 46: <enum POPPLER_STRUCTURE_ELEMENT_WARICHU_TEXT of type Poppler.StructureElementKind>, 47: <enum POPPLER_STRUCTURE_ELEMENT_WARICHU_PUNCTUATION of type Poppler.StructureElementKind>, 48: <enum POPPLER_STRUCTURE_ELEMENT_FIGURE of type Poppler.StructureElementKind>, 49: <enum POPPLER_STRUCTURE_ELEMENT_FORMULA of type Poppler.StructureElementKind>, 50: <enum POPPLER_STRUCTURE_ELEMENT_FORM of type Poppler.StructureElementKind>}, '__info__': gi.EnumInfo(StructureElementKind), 'CONTENT': <enum POPPLER_STRUCTURE_ELEMENT_CONTENT of type Poppler.StructureElementKind>, 'OBJECT_REFERENCE': <enum POPPLER_STRUCTURE_ELEMENT_OBJECT_REFERENCE of type Poppler.StructureElementKind>, 'DOCUMENT': <enum POPPLER_STRUCTURE_ELEMENT_DOCUMENT of type Poppler.StructureElementKind>, 'PART': <enum POPPLER_STRUCTURE_ELEMENT_PART of type Poppler.StructureElementKind>, 'ARTICLE': <enum POPPLER_STRUCTURE_ELEMENT_ARTICLE of type Poppler.StructureElementKind>, 'SECTION': <enum POPPLER_STRUCTURE_ELEMENT_SECTION of type Poppler.StructureElementKind>, 'DIV': <enum POPPLER_STRUCTURE_ELEMENT_DIV of type Poppler.StructureElementKind>, 'SPAN': <enum POPPLER_STRUCTURE_ELEMENT_SPAN of type Poppler.StructureElementKind>, 'QUOTE': <enum POPPLER_STRUCTURE_ELEMENT_QUOTE of type Poppler.StructureElementKind>, 'NOTE': <enum POPPLER_STRUCTURE_ELEMENT_NOTE of type Poppler.StructureElementKind>, 'REFERENCE': <enum POPPLER_STRUCTURE_ELEMENT_REFERENCE of type Poppler.StructureElementKind>, 'BIBENTRY': <enum POPPLER_STRUCTURE_ELEMENT_BIBENTRY of type Poppler.StructureElementKind>, 'CODE': <enum POPPLER_STRUCTURE_ELEMENT_CODE of type Poppler.StructureElementKind>, 'LINK': <enum POPPLER_STRUCTURE_ELEMENT_LINK of type Poppler.StructureElementKind>, 'ANNOT': <enum POPPLER_STRUCTURE_ELEMENT_ANNOT of type Poppler.StructureElementKind>, 'BLOCKQUOTE': <enum POPPLER_STRUCTURE_ELEMENT_BLOCKQUOTE of type Poppler.StructureElementKind>, 'CAPTION': <enum POPPLER_STRUCTURE_ELEMENT_CAPTION of type Poppler.StructureElementKind>, 'NONSTRUCT': <enum POPPLER_STRUCTURE_ELEMENT_NONSTRUCT of type Poppler.StructureElementKind>, 'TOC': <enum POPPLER_STRUCTURE_ELEMENT_TOC of type Poppler.StructureElementKind>, 'TOC_ITEM': <enum POPPLER_STRUCTURE_ELEMENT_TOC_ITEM of type Poppler.StructureElementKind>, 'INDEX': <enum POPPLER_STRUCTURE_ELEMENT_INDEX of type Poppler.StructureElementKind>, 'PRIVATE': <enum POPPLER_STRUCTURE_ELEMENT_PRIVATE of type Poppler.StructureElementKind>, 'PARAGRAPH': <enum POPPLER_STRUCTURE_ELEMENT_PARAGRAPH of type Poppler.StructureElementKind>, 'HEADING': <enum POPPLER_STRUCTURE_ELEMENT_HEADING of type Poppler.StructureElementKind>, 'HEADING_1': <enum POPPLER_STRUCTURE_ELEMENT_HEADING_1 of type Poppler.StructureElementKind>, 'HEADING_2': <enum POPPLER_STRUCTURE_ELEMENT_HEADING_2 of type Poppler.StructureElementKind>, 'HEADING_3': <enum POPPLER_STRUCTURE_ELEMENT_HEADING_3 of type Poppler.StructureElementKind>, 'HEADING_4': <enum POPPLER_STRUCTURE_ELEMENT_HEADING_4 of type Poppler.StructureElementKind>, 'HEADING_5': <enum POPPLER_STRUCTURE_ELEMENT_HEADING_5 of type Poppler.StructureElementKind>, 'HEADING_6': <enum POPPLER_STRUCTURE_ELEMENT_HEADING_6 of type Poppler.StructureElementKind>, 'LIST': <enum POPPLER_STRUCTURE_ELEMENT_LIST of type Poppler.StructureElementKind>, 'LIST_ITEM': <enum POPPLER_STRUCTURE_ELEMENT_LIST_ITEM of type Poppler.StructureElementKind>, 'LIST_LABEL': <enum POPPLER_STRUCTURE_ELEMENT_LIST_LABEL of type Poppler.StructureElementKind>, 'LIST_BODY': <enum POPPLER_STRUCTURE_ELEMENT_LIST_BODY of type Poppler.StructureElementKind>, 'TABLE': <enum POPPLER_STRUCTURE_ELEMENT_TABLE of type Poppler.StructureElementKind>, 'TABLE_ROW': <enum POPPLER_STRUCTURE_ELEMENT_TABLE_ROW of type Poppler.StructureElementKind>, 'TABLE_HEADING': <enum POPPLER_STRUCTURE_ELEMENT_TABLE_HEADING of type Poppler.StructureElementKind>, 'TABLE_DATA': <enum POPPLER_STRUCTURE_ELEMENT_TABLE_DATA of type Poppler.StructureElementKind>, 'TABLE_HEADER': <enum POPPLER_STRUCTURE_ELEMENT_TABLE_HEADER of type Poppler.StructureElementKind>, 'TABLE_FOOTER': <enum POPPLER_STRUCTURE_ELEMENT_TABLE_FOOTER of type Poppler.StructureElementKind>, 'TABLE_BODY': <enum POPPLER_STRUCTURE_ELEMENT_TABLE_BODY of type Poppler.StructureElementKind>, 'RUBY': <enum POPPLER_STRUCTURE_ELEMENT_RUBY of type Poppler.StructureElementKind>, 'RUBY_BASE_TEXT': <enum POPPLER_STRUCTURE_ELEMENT_RUBY_BASE_TEXT of type Poppler.StructureElementKind>, 'RUBY_ANNOT_TEXT': <enum POPPLER_STRUCTURE_ELEMENT_RUBY_ANNOT_TEXT of type Poppler.StructureElementKind>, 'RUBY_PUNCTUATION': <enum POPPLER_STRUCTURE_ELEMENT_RUBY_PUNCTUATION of type Poppler.StructureElementKind>, 'WARICHU': <enum POPPLER_STRUCTURE_ELEMENT_WARICHU of type Poppler.StructureElementKind>, 'WARICHU_TEXT': <enum POPPLER_STRUCTURE_ELEMENT_WARICHU_TEXT of type Poppler.StructureElementKind>, 'WARICHU_PUNCTUATION': <enum POPPLER_STRUCTURE_ELEMENT_WARICHU_PUNCTUATION of type Poppler.StructureElementKind>, 'FIGURE': <enum POPPLER_STRUCTURE_ELEMENT_FIGURE of type Poppler.StructureElementKind>, 'FORMULA': <enum POPPLER_STRUCTURE_ELEMENT_FORMULA of type Poppler.StructureElementKind>, 'FORM': <enum POPPLER_STRUCTURE_ELEMENT_FORM of type Poppler.StructureElementKind>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PopplerStructureElementKind (3984841280)>'
    __info__ = gi.EnumInfo(StructureElementKind)


