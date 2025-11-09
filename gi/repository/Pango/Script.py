# encoding: utf-8
# module gi.repository.Pango
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Pango-1.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class Script(__gobject.GEnum):
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

    def for_unichar(self, ch): # real signature unknown; restored from __doc__
        """ for_unichar(ch:str) -> Pango.Script """
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

    def get_sample_language(self, script): # real signature unknown; restored from __doc__
        """ get_sample_language(script:Pango.Script) -> Pango.Language or None """
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


    AHOM = 111
    ANATOLIAN_HIEROGLYPHS = 112
    ARABIC = 2
    ARMENIAN = 3
    BALINESE = 62
    BASSA_VAH = 88
    BATAK = 78
    BENGALI = 4
    BOPOMOFO = 5
    BRAHMI = 79
    BRAILLE = 46
    BUGINESE = 55
    BUHID = 44
    CANADIAN_ABORIGINAL = 40
    CARIAN = 75
    CAUCASIAN_ALBANIAN = 89
    CHAKMA = 81
    CHAM = 72
    CHEROKEE = 6
    COMMON = 0
    COPTIC = 7
    CUNEIFORM = 63
    CYPRIOT = 47
    CYRILLIC = 8
    DESERET = 9
    DEVANAGARI = 10
    DUPLOYAN = 90
    ELBASAN = 91
    ETHIOPIC = 11
    GEORGIAN = 12
    GLAGOLITIC = 56
    GOTHIC = 13
    GRANTHA = 92
    GREEK = 14
    GUJARATI = 15
    GURMUKHI = 16
    HAN = 17
    HANGUL = 18
    HANUNOO = 43
    HATRAN = 113
    HEBREW = 19
    HIRAGANA = 20
    INHERITED = 1
    INVALID_CODE = -1
    KANNADA = 21
    KATAKANA = 22
    KAYAH_LI = 67
    KHAROSHTHI = 60
    KHMER = 23
    KHOJKI = 93
    KHUDAWADI = 94
    LAO = 24
    LATIN = 25
    LEPCHA = 68
    LIMBU = 48
    LINEAR_A = 95
    LINEAR_B = 51
    LYCIAN = 76
    LYDIAN = 77
    MAHAJANI = 96
    MALAYALAM = 26
    MANDAIC = 80
    MANICHAEAN = 97
    MENDE_KIKAKUI = 98
    MEROITIC_CURSIVE = 82
    MEROITIC_HIEROGLYPHS = 83
    MIAO = 84
    MODI = 99
    MONGOLIAN = 27
    MRO = 100
    MULTANI = 114
    MYANMAR = 28
    NABATAEAN = 101
    NEW_TAI_LUE = 54
    NKO = 66
    OGHAM = 29
    OLD_HUNGARIAN = 115
    OLD_ITALIC = 30
    OLD_NORTH_ARABIAN = 102
    OLD_PERMIC = 103
    OLD_PERSIAN = 59
    OL_CHIKI = 73
    ORIYA = 31
    OSMANYA = 49
    PAHAWH_HMONG = 104
    PALMYRENE = 105
    PAU_CIN_HAU = 106
    PHAGS_PA = 65
    PHOENICIAN = 64
    PSALTER_PAHLAVI = 107
    REJANG = 69
    RUNIC = 32
    SAURASHTRA = 71
    SHARADA = 85
    SHAVIAN = 50
    SIDDHAM = 108
    SIGNWRITING = 116
    SINHALA = 33
    SORA_SOMPENG = 86
    SUNDANESE = 70
    SYLOTI_NAGRI = 58
    SYRIAC = 34
    TAGALOG = 42
    TAGBANWA = 45
    TAI_LE = 52
    TAKRI = 87
    TAMIL = 35
    TELUGU = 36
    THAANA = 37
    THAI = 38
    TIBETAN = 39
    TIFINAGH = 57
    TIRHUTA = 109
    UGARITIC = 53
    UNKNOWN = 61
    VAI = 74
    WARANG_CITI = 110
    YI = 41
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Pango', '__dict__': <attribute '__dict__' of 'Script' objects>, '__doc__': None, '__gtype__': <GType PangoScript (4081762400)>, '__enum_values__': {-1: <enum PANGO_SCRIPT_INVALID_CODE of type Pango.Script>, 0: <enum PANGO_SCRIPT_COMMON of type Pango.Script>, 1: <enum PANGO_SCRIPT_INHERITED of type Pango.Script>, 2: <enum PANGO_SCRIPT_ARABIC of type Pango.Script>, 3: <enum PANGO_SCRIPT_ARMENIAN of type Pango.Script>, 4: <enum PANGO_SCRIPT_BENGALI of type Pango.Script>, 5: <enum PANGO_SCRIPT_BOPOMOFO of type Pango.Script>, 6: <enum PANGO_SCRIPT_CHEROKEE of type Pango.Script>, 7: <enum PANGO_SCRIPT_COPTIC of type Pango.Script>, 8: <enum PANGO_SCRIPT_CYRILLIC of type Pango.Script>, 9: <enum PANGO_SCRIPT_DESERET of type Pango.Script>, 10: <enum PANGO_SCRIPT_DEVANAGARI of type Pango.Script>, 11: <enum PANGO_SCRIPT_ETHIOPIC of type Pango.Script>, 12: <enum PANGO_SCRIPT_GEORGIAN of type Pango.Script>, 13: <enum PANGO_SCRIPT_GOTHIC of type Pango.Script>, 14: <enum PANGO_SCRIPT_GREEK of type Pango.Script>, 15: <enum PANGO_SCRIPT_GUJARATI of type Pango.Script>, 16: <enum PANGO_SCRIPT_GURMUKHI of type Pango.Script>, 17: <enum PANGO_SCRIPT_HAN of type Pango.Script>, 18: <enum PANGO_SCRIPT_HANGUL of type Pango.Script>, 19: <enum PANGO_SCRIPT_HEBREW of type Pango.Script>, 20: <enum PANGO_SCRIPT_HIRAGANA of type Pango.Script>, 21: <enum PANGO_SCRIPT_KANNADA of type Pango.Script>, 22: <enum PANGO_SCRIPT_KATAKANA of type Pango.Script>, 23: <enum PANGO_SCRIPT_KHMER of type Pango.Script>, 24: <enum PANGO_SCRIPT_LAO of type Pango.Script>, 25: <enum PANGO_SCRIPT_LATIN of type Pango.Script>, 26: <enum PANGO_SCRIPT_MALAYALAM of type Pango.Script>, 27: <enum PANGO_SCRIPT_MONGOLIAN of type Pango.Script>, 28: <enum PANGO_SCRIPT_MYANMAR of type Pango.Script>, 29: <enum PANGO_SCRIPT_OGHAM of type Pango.Script>, 30: <enum PANGO_SCRIPT_OLD_ITALIC of type Pango.Script>, 31: <enum PANGO_SCRIPT_ORIYA of type Pango.Script>, 32: <enum PANGO_SCRIPT_RUNIC of type Pango.Script>, 33: <enum PANGO_SCRIPT_SINHALA of type Pango.Script>, 34: <enum PANGO_SCRIPT_SYRIAC of type Pango.Script>, 35: <enum PANGO_SCRIPT_TAMIL of type Pango.Script>, 36: <enum PANGO_SCRIPT_TELUGU of type Pango.Script>, 37: <enum PANGO_SCRIPT_THAANA of type Pango.Script>, 38: <enum PANGO_SCRIPT_THAI of type Pango.Script>, 39: <enum PANGO_SCRIPT_TIBETAN of type Pango.Script>, 40: <enum PANGO_SCRIPT_CANADIAN_ABORIGINAL of type Pango.Script>, 41: <enum PANGO_SCRIPT_YI of type Pango.Script>, 42: <enum PANGO_SCRIPT_TAGALOG of type Pango.Script>, 43: <enum PANGO_SCRIPT_HANUNOO of type Pango.Script>, 44: <enum PANGO_SCRIPT_BUHID of type Pango.Script>, 45: <enum PANGO_SCRIPT_TAGBANWA of type Pango.Script>, 46: <enum PANGO_SCRIPT_BRAILLE of type Pango.Script>, 47: <enum PANGO_SCRIPT_CYPRIOT of type Pango.Script>, 48: <enum PANGO_SCRIPT_LIMBU of type Pango.Script>, 49: <enum PANGO_SCRIPT_OSMANYA of type Pango.Script>, 50: <enum PANGO_SCRIPT_SHAVIAN of type Pango.Script>, 51: <enum PANGO_SCRIPT_LINEAR_B of type Pango.Script>, 52: <enum PANGO_SCRIPT_TAI_LE of type Pango.Script>, 53: <enum PANGO_SCRIPT_UGARITIC of type Pango.Script>, 54: <enum PANGO_SCRIPT_NEW_TAI_LUE of type Pango.Script>, 55: <enum PANGO_SCRIPT_BUGINESE of type Pango.Script>, 56: <enum PANGO_SCRIPT_GLAGOLITIC of type Pango.Script>, 57: <enum PANGO_SCRIPT_TIFINAGH of type Pango.Script>, 58: <enum PANGO_SCRIPT_SYLOTI_NAGRI of type Pango.Script>, 59: <enum PANGO_SCRIPT_OLD_PERSIAN of type Pango.Script>, 60: <enum PANGO_SCRIPT_KHAROSHTHI of type Pango.Script>, 61: <enum PANGO_SCRIPT_UNKNOWN of type Pango.Script>, 62: <enum PANGO_SCRIPT_BALINESE of type Pango.Script>, 63: <enum PANGO_SCRIPT_CUNEIFORM of type Pango.Script>, 64: <enum PANGO_SCRIPT_PHOENICIAN of type Pango.Script>, 65: <enum PANGO_SCRIPT_PHAGS_PA of type Pango.Script>, 66: <enum PANGO_SCRIPT_NKO of type Pango.Script>, 67: <enum PANGO_SCRIPT_KAYAH_LI of type Pango.Script>, 68: <enum PANGO_SCRIPT_LEPCHA of type Pango.Script>, 69: <enum PANGO_SCRIPT_REJANG of type Pango.Script>, 70: <enum PANGO_SCRIPT_SUNDANESE of type Pango.Script>, 71: <enum PANGO_SCRIPT_SAURASHTRA of type Pango.Script>, 72: <enum PANGO_SCRIPT_CHAM of type Pango.Script>, 73: <enum PANGO_SCRIPT_OL_CHIKI of type Pango.Script>, 74: <enum PANGO_SCRIPT_VAI of type Pango.Script>, 75: <enum PANGO_SCRIPT_CARIAN of type Pango.Script>, 76: <enum PANGO_SCRIPT_LYCIAN of type Pango.Script>, 77: <enum PANGO_SCRIPT_LYDIAN of type Pango.Script>, 78: <enum PANGO_SCRIPT_BATAK of type Pango.Script>, 79: <enum PANGO_SCRIPT_BRAHMI of type Pango.Script>, 80: <enum PANGO_SCRIPT_MANDAIC of type Pango.Script>, 81: <enum PANGO_SCRIPT_CHAKMA of type Pango.Script>, 82: <enum PANGO_SCRIPT_MEROITIC_CURSIVE of type Pango.Script>, 83: <enum PANGO_SCRIPT_MEROITIC_HIEROGLYPHS of type Pango.Script>, 84: <enum PANGO_SCRIPT_MIAO of type Pango.Script>, 85: <enum PANGO_SCRIPT_SHARADA of type Pango.Script>, 86: <enum PANGO_SCRIPT_SORA_SOMPENG of type Pango.Script>, 87: <enum PANGO_SCRIPT_TAKRI of type Pango.Script>, 88: <enum PANGO_SCRIPT_BASSA_VAH of type Pango.Script>, 89: <enum PANGO_SCRIPT_CAUCASIAN_ALBANIAN of type Pango.Script>, 90: <enum PANGO_SCRIPT_DUPLOYAN of type Pango.Script>, 91: <enum PANGO_SCRIPT_ELBASAN of type Pango.Script>, 92: <enum PANGO_SCRIPT_GRANTHA of type Pango.Script>, 93: <enum PANGO_SCRIPT_KHOJKI of type Pango.Script>, 94: <enum PANGO_SCRIPT_KHUDAWADI of type Pango.Script>, 95: <enum PANGO_SCRIPT_LINEAR_A of type Pango.Script>, 96: <enum PANGO_SCRIPT_MAHAJANI of type Pango.Script>, 97: <enum PANGO_SCRIPT_MANICHAEAN of type Pango.Script>, 98: <enum PANGO_SCRIPT_MENDE_KIKAKUI of type Pango.Script>, 99: <enum PANGO_SCRIPT_MODI of type Pango.Script>, 100: <enum PANGO_SCRIPT_MRO of type Pango.Script>, 101: <enum PANGO_SCRIPT_NABATAEAN of type Pango.Script>, 102: <enum PANGO_SCRIPT_OLD_NORTH_ARABIAN of type Pango.Script>, 103: <enum PANGO_SCRIPT_OLD_PERMIC of type Pango.Script>, 104: <enum PANGO_SCRIPT_PAHAWH_HMONG of type Pango.Script>, 105: <enum PANGO_SCRIPT_PALMYRENE of type Pango.Script>, 106: <enum PANGO_SCRIPT_PAU_CIN_HAU of type Pango.Script>, 107: <enum PANGO_SCRIPT_PSALTER_PAHLAVI of type Pango.Script>, 108: <enum PANGO_SCRIPT_SIDDHAM of type Pango.Script>, 109: <enum PANGO_SCRIPT_TIRHUTA of type Pango.Script>, 110: <enum PANGO_SCRIPT_WARANG_CITI of type Pango.Script>, 111: <enum PANGO_SCRIPT_AHOM of type Pango.Script>, 112: <enum PANGO_SCRIPT_ANATOLIAN_HIEROGLYPHS of type Pango.Script>, 113: <enum PANGO_SCRIPT_HATRAN of type Pango.Script>, 114: <enum PANGO_SCRIPT_MULTANI of type Pango.Script>, 115: <enum PANGO_SCRIPT_OLD_HUNGARIAN of type Pango.Script>, 116: <enum PANGO_SCRIPT_SIGNWRITING of type Pango.Script>}, '__info__': gi.EnumInfo(Script), 'INVALID_CODE': <enum PANGO_SCRIPT_INVALID_CODE of type Pango.Script>, 'COMMON': <enum PANGO_SCRIPT_COMMON of type Pango.Script>, 'INHERITED': <enum PANGO_SCRIPT_INHERITED of type Pango.Script>, 'ARABIC': <enum PANGO_SCRIPT_ARABIC of type Pango.Script>, 'ARMENIAN': <enum PANGO_SCRIPT_ARMENIAN of type Pango.Script>, 'BENGALI': <enum PANGO_SCRIPT_BENGALI of type Pango.Script>, 'BOPOMOFO': <enum PANGO_SCRIPT_BOPOMOFO of type Pango.Script>, 'CHEROKEE': <enum PANGO_SCRIPT_CHEROKEE of type Pango.Script>, 'COPTIC': <enum PANGO_SCRIPT_COPTIC of type Pango.Script>, 'CYRILLIC': <enum PANGO_SCRIPT_CYRILLIC of type Pango.Script>, 'DESERET': <enum PANGO_SCRIPT_DESERET of type Pango.Script>, 'DEVANAGARI': <enum PANGO_SCRIPT_DEVANAGARI of type Pango.Script>, 'ETHIOPIC': <enum PANGO_SCRIPT_ETHIOPIC of type Pango.Script>, 'GEORGIAN': <enum PANGO_SCRIPT_GEORGIAN of type Pango.Script>, 'GOTHIC': <enum PANGO_SCRIPT_GOTHIC of type Pango.Script>, 'GREEK': <enum PANGO_SCRIPT_GREEK of type Pango.Script>, 'GUJARATI': <enum PANGO_SCRIPT_GUJARATI of type Pango.Script>, 'GURMUKHI': <enum PANGO_SCRIPT_GURMUKHI of type Pango.Script>, 'HAN': <enum PANGO_SCRIPT_HAN of type Pango.Script>, 'HANGUL': <enum PANGO_SCRIPT_HANGUL of type Pango.Script>, 'HEBREW': <enum PANGO_SCRIPT_HEBREW of type Pango.Script>, 'HIRAGANA': <enum PANGO_SCRIPT_HIRAGANA of type Pango.Script>, 'KANNADA': <enum PANGO_SCRIPT_KANNADA of type Pango.Script>, 'KATAKANA': <enum PANGO_SCRIPT_KATAKANA of type Pango.Script>, 'KHMER': <enum PANGO_SCRIPT_KHMER of type Pango.Script>, 'LAO': <enum PANGO_SCRIPT_LAO of type Pango.Script>, 'LATIN': <enum PANGO_SCRIPT_LATIN of type Pango.Script>, 'MALAYALAM': <enum PANGO_SCRIPT_MALAYALAM of type Pango.Script>, 'MONGOLIAN': <enum PANGO_SCRIPT_MONGOLIAN of type Pango.Script>, 'MYANMAR': <enum PANGO_SCRIPT_MYANMAR of type Pango.Script>, 'OGHAM': <enum PANGO_SCRIPT_OGHAM of type Pango.Script>, 'OLD_ITALIC': <enum PANGO_SCRIPT_OLD_ITALIC of type Pango.Script>, 'ORIYA': <enum PANGO_SCRIPT_ORIYA of type Pango.Script>, 'RUNIC': <enum PANGO_SCRIPT_RUNIC of type Pango.Script>, 'SINHALA': <enum PANGO_SCRIPT_SINHALA of type Pango.Script>, 'SYRIAC': <enum PANGO_SCRIPT_SYRIAC of type Pango.Script>, 'TAMIL': <enum PANGO_SCRIPT_TAMIL of type Pango.Script>, 'TELUGU': <enum PANGO_SCRIPT_TELUGU of type Pango.Script>, 'THAANA': <enum PANGO_SCRIPT_THAANA of type Pango.Script>, 'THAI': <enum PANGO_SCRIPT_THAI of type Pango.Script>, 'TIBETAN': <enum PANGO_SCRIPT_TIBETAN of type Pango.Script>, 'CANADIAN_ABORIGINAL': <enum PANGO_SCRIPT_CANADIAN_ABORIGINAL of type Pango.Script>, 'YI': <enum PANGO_SCRIPT_YI of type Pango.Script>, 'TAGALOG': <enum PANGO_SCRIPT_TAGALOG of type Pango.Script>, 'HANUNOO': <enum PANGO_SCRIPT_HANUNOO of type Pango.Script>, 'BUHID': <enum PANGO_SCRIPT_BUHID of type Pango.Script>, 'TAGBANWA': <enum PANGO_SCRIPT_TAGBANWA of type Pango.Script>, 'BRAILLE': <enum PANGO_SCRIPT_BRAILLE of type Pango.Script>, 'CYPRIOT': <enum PANGO_SCRIPT_CYPRIOT of type Pango.Script>, 'LIMBU': <enum PANGO_SCRIPT_LIMBU of type Pango.Script>, 'OSMANYA': <enum PANGO_SCRIPT_OSMANYA of type Pango.Script>, 'SHAVIAN': <enum PANGO_SCRIPT_SHAVIAN of type Pango.Script>, 'LINEAR_B': <enum PANGO_SCRIPT_LINEAR_B of type Pango.Script>, 'TAI_LE': <enum PANGO_SCRIPT_TAI_LE of type Pango.Script>, 'UGARITIC': <enum PANGO_SCRIPT_UGARITIC of type Pango.Script>, 'NEW_TAI_LUE': <enum PANGO_SCRIPT_NEW_TAI_LUE of type Pango.Script>, 'BUGINESE': <enum PANGO_SCRIPT_BUGINESE of type Pango.Script>, 'GLAGOLITIC': <enum PANGO_SCRIPT_GLAGOLITIC of type Pango.Script>, 'TIFINAGH': <enum PANGO_SCRIPT_TIFINAGH of type Pango.Script>, 'SYLOTI_NAGRI': <enum PANGO_SCRIPT_SYLOTI_NAGRI of type Pango.Script>, 'OLD_PERSIAN': <enum PANGO_SCRIPT_OLD_PERSIAN of type Pango.Script>, 'KHAROSHTHI': <enum PANGO_SCRIPT_KHAROSHTHI of type Pango.Script>, 'UNKNOWN': <enum PANGO_SCRIPT_UNKNOWN of type Pango.Script>, 'BALINESE': <enum PANGO_SCRIPT_BALINESE of type Pango.Script>, 'CUNEIFORM': <enum PANGO_SCRIPT_CUNEIFORM of type Pango.Script>, 'PHOENICIAN': <enum PANGO_SCRIPT_PHOENICIAN of type Pango.Script>, 'PHAGS_PA': <enum PANGO_SCRIPT_PHAGS_PA of type Pango.Script>, 'NKO': <enum PANGO_SCRIPT_NKO of type Pango.Script>, 'KAYAH_LI': <enum PANGO_SCRIPT_KAYAH_LI of type Pango.Script>, 'LEPCHA': <enum PANGO_SCRIPT_LEPCHA of type Pango.Script>, 'REJANG': <enum PANGO_SCRIPT_REJANG of type Pango.Script>, 'SUNDANESE': <enum PANGO_SCRIPT_SUNDANESE of type Pango.Script>, 'SAURASHTRA': <enum PANGO_SCRIPT_SAURASHTRA of type Pango.Script>, 'CHAM': <enum PANGO_SCRIPT_CHAM of type Pango.Script>, 'OL_CHIKI': <enum PANGO_SCRIPT_OL_CHIKI of type Pango.Script>, 'VAI': <enum PANGO_SCRIPT_VAI of type Pango.Script>, 'CARIAN': <enum PANGO_SCRIPT_CARIAN of type Pango.Script>, 'LYCIAN': <enum PANGO_SCRIPT_LYCIAN of type Pango.Script>, 'LYDIAN': <enum PANGO_SCRIPT_LYDIAN of type Pango.Script>, 'BATAK': <enum PANGO_SCRIPT_BATAK of type Pango.Script>, 'BRAHMI': <enum PANGO_SCRIPT_BRAHMI of type Pango.Script>, 'MANDAIC': <enum PANGO_SCRIPT_MANDAIC of type Pango.Script>, 'CHAKMA': <enum PANGO_SCRIPT_CHAKMA of type Pango.Script>, 'MEROITIC_CURSIVE': <enum PANGO_SCRIPT_MEROITIC_CURSIVE of type Pango.Script>, 'MEROITIC_HIEROGLYPHS': <enum PANGO_SCRIPT_MEROITIC_HIEROGLYPHS of type Pango.Script>, 'MIAO': <enum PANGO_SCRIPT_MIAO of type Pango.Script>, 'SHARADA': <enum PANGO_SCRIPT_SHARADA of type Pango.Script>, 'SORA_SOMPENG': <enum PANGO_SCRIPT_SORA_SOMPENG of type Pango.Script>, 'TAKRI': <enum PANGO_SCRIPT_TAKRI of type Pango.Script>, 'BASSA_VAH': <enum PANGO_SCRIPT_BASSA_VAH of type Pango.Script>, 'CAUCASIAN_ALBANIAN': <enum PANGO_SCRIPT_CAUCASIAN_ALBANIAN of type Pango.Script>, 'DUPLOYAN': <enum PANGO_SCRIPT_DUPLOYAN of type Pango.Script>, 'ELBASAN': <enum PANGO_SCRIPT_ELBASAN of type Pango.Script>, 'GRANTHA': <enum PANGO_SCRIPT_GRANTHA of type Pango.Script>, 'KHOJKI': <enum PANGO_SCRIPT_KHOJKI of type Pango.Script>, 'KHUDAWADI': <enum PANGO_SCRIPT_KHUDAWADI of type Pango.Script>, 'LINEAR_A': <enum PANGO_SCRIPT_LINEAR_A of type Pango.Script>, 'MAHAJANI': <enum PANGO_SCRIPT_MAHAJANI of type Pango.Script>, 'MANICHAEAN': <enum PANGO_SCRIPT_MANICHAEAN of type Pango.Script>, 'MENDE_KIKAKUI': <enum PANGO_SCRIPT_MENDE_KIKAKUI of type Pango.Script>, 'MODI': <enum PANGO_SCRIPT_MODI of type Pango.Script>, 'MRO': <enum PANGO_SCRIPT_MRO of type Pango.Script>, 'NABATAEAN': <enum PANGO_SCRIPT_NABATAEAN of type Pango.Script>, 'OLD_NORTH_ARABIAN': <enum PANGO_SCRIPT_OLD_NORTH_ARABIAN of type Pango.Script>, 'OLD_PERMIC': <enum PANGO_SCRIPT_OLD_PERMIC of type Pango.Script>, 'PAHAWH_HMONG': <enum PANGO_SCRIPT_PAHAWH_HMONG of type Pango.Script>, 'PALMYRENE': <enum PANGO_SCRIPT_PALMYRENE of type Pango.Script>, 'PAU_CIN_HAU': <enum PANGO_SCRIPT_PAU_CIN_HAU of type Pango.Script>, 'PSALTER_PAHLAVI': <enum PANGO_SCRIPT_PSALTER_PAHLAVI of type Pango.Script>, 'SIDDHAM': <enum PANGO_SCRIPT_SIDDHAM of type Pango.Script>, 'TIRHUTA': <enum PANGO_SCRIPT_TIRHUTA of type Pango.Script>, 'WARANG_CITI': <enum PANGO_SCRIPT_WARANG_CITI of type Pango.Script>, 'AHOM': <enum PANGO_SCRIPT_AHOM of type Pango.Script>, 'ANATOLIAN_HIEROGLYPHS': <enum PANGO_SCRIPT_ANATOLIAN_HIEROGLYPHS of type Pango.Script>, 'HATRAN': <enum PANGO_SCRIPT_HATRAN of type Pango.Script>, 'MULTANI': <enum PANGO_SCRIPT_MULTANI of type Pango.Script>, 'OLD_HUNGARIAN': <enum PANGO_SCRIPT_OLD_HUNGARIAN of type Pango.Script>, 'SIGNWRITING': <enum PANGO_SCRIPT_SIGNWRITING of type Pango.Script>, 'for_unichar': gi.FunctionInfo(for_unichar, bound=None), 'get_sample_language': gi.FunctionInfo(get_sample_language, bound=None)})"
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
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
        64: 64,
        65: 65,
        66: 66,
        67: 67,
        68: 68,
        69: 69,
        70: 70,
        71: 71,
        72: 72,
        73: 73,
        74: 74,
        75: 75,
        76: 76,
        77: 77,
        78: 78,
        79: 79,
        80: 80,
        81: 81,
        82: 82,
        83: 83,
        84: 84,
        85: 85,
        86: 86,
        87: 87,
        88: 88,
        89: 89,
        90: 90,
        91: 91,
        92: 92,
        93: 93,
        94: 94,
        95: 95,
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        110: 110,
        111: 111,
        112: 112,
        113: 113,
        114: 114,
        115: 115,
        116: 116,
    }
    __gtype__ = None # (!) real value is '<GType PangoScript (4081762400)>'
    __info__ = gi.EnumInfo(Script)


