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


class UnicodeScript(__gobject.GEnum):
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

    def from_iso15924(self, iso15924): # real signature unknown; restored from __doc__
        """ from_iso15924(iso15924:int) -> GLib.UnicodeScript """
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

    def to_iso15924(self, script): # real signature unknown; restored from __doc__
        """ to_iso15924(script:GLib.UnicodeScript) -> int """
        return 0

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


    ADLAM = 132
    AHOM = 126
    ANATOLIAN_HIEROGLYPHS = 127
    ARABIC = 2
    ARMENIAN = 3
    AVESTAN = 78
    BALINESE = 62
    BAMUM = 79
    BASSA_VAH = 103
    BATAK = 93
    BENGALI = 4
    BHAIKSUKI = 133
    BOPOMOFO = 5
    BRAHMI = 94
    BRAILLE = 46
    BUGINESE = 55
    BUHID = 44
    CANADIAN_ABORIGINAL = 40
    CARIAN = 75
    CAUCASIAN_ALBANIAN = 104
    CHAKMA = 96
    CHAM = 72
    CHEROKEE = 6
    CHORASMIAN = 153
    COMMON = 0
    COPTIC = 7
    CUNEIFORM = 63
    CYPRIOT = 47
    CYPRO_MINOAN = 157
    CYRILLIC = 8
    DESERET = 9
    DEVANAGARI = 10
    DIVES_AKURU = 154
    DOGRA = 142
    DUPLOYAN = 105
    EGYPTIAN_HIEROGLYPHS = 80
    ELBASAN = 106
    ELYMAIC = 149
    ETHIOPIC = 11
    GEORGIAN = 12
    GLAGOLITIC = 56
    GOTHIC = 13
    GRANTHA = 107
    GREEK = 14
    GUJARATI = 15
    GUNJALA_GONDI = 143
    GURMUKHI = 16
    HAN = 17
    HANGUL = 18
    HANIFI_ROHINGYA = 144
    HANUNOO = 43
    HATRAN = 128
    HEBREW = 19
    HIRAGANA = 20
    IMPERIAL_ARAMAIC = 81
    INHERITED = 1
    INSCRIPTIONAL_PAHLAVI = 82
    INSCRIPTIONAL_PARTHIAN = 83
    INVALID_CODE = -1
    JAVANESE = 84
    KAITHI = 85
    KANNADA = 21
    KATAKANA = 22
    KAWI = 163
    KAYAH_LI = 67
    KHAROSHTHI = 60
    KHITAN_SMALL_SCRIPT = 155
    KHMER = 23
    KHOJKI = 108
    KHUDAWADI = 109
    LAO = 24
    LATIN = 25
    LEPCHA = 68
    LIMBU = 48
    LINEAR_A = 110
    LINEAR_B = 51
    LISU = 86
    LYCIAN = 76
    LYDIAN = 77
    MAHAJANI = 111
    MAKASAR = 145
    MALAYALAM = 26
    MANDAIC = 95
    MANICHAEAN = 112
    MARCHEN = 134
    MASARAM_GONDI = 138
    MATH = 162
    MEDEFAIDRIN = 146
    MEETEI_MAYEK = 87
    MENDE_KIKAKUI = 113
    MEROITIC_CURSIVE = 97
    MEROITIC_HIEROGLYPHS = 98
    MIAO = 99
    MODI = 114
    MONGOLIAN = 27
    MRO = 115
    MULTANI = 129
    MYANMAR = 28
    NABATAEAN = 116
    NAG_MUNDARI = 164
    NANDINAGARI = 150
    NEWA = 135
    NEW_TAI_LUE = 54
    NKO = 66
    NUSHU = 139
    NYIAKENG_PUACHUE_HMONG = 151
    OGHAM = 29
    OLD_HUNGARIAN = 130
    OLD_ITALIC = 30
    OLD_NORTH_ARABIAN = 117
    OLD_PERMIC = 118
    OLD_PERSIAN = 59
    OLD_SOGDIAN = 147
    OLD_SOUTH_ARABIAN = 88
    OLD_TURKIC = 89
    OLD_UYGHUR = 158
    OL_CHIKI = 73
    ORIYA = 31
    OSAGE = 136
    OSMANYA = 49
    PAHAWH_HMONG = 119
    PALMYRENE = 120
    PAU_CIN_HAU = 121
    PHAGS_PA = 65
    PHOENICIAN = 64
    PSALTER_PAHLAVI = 122
    REJANG = 69
    RUNIC = 32
    SAMARITAN = 90
    SAURASHTRA = 71
    SHARADA = 100
    SHAVIAN = 50
    SIDDHAM = 123
    SIGNWRITING = 131
    SINHALA = 33
    SOGDIAN = 148
    SORA_SOMPENG = 101
    SOYOMBO = 140
    SUNDANESE = 70
    SYLOTI_NAGRI = 58
    SYRIAC = 34
    TAGALOG = 42
    TAGBANWA = 45
    TAI_LE = 52
    TAI_THAM = 91
    TAI_VIET = 92
    TAKRI = 102
    TAMIL = 35
    TANGSA = 159
    TANGUT = 137
    TELUGU = 36
    THAANA = 37
    THAI = 38
    TIBETAN = 39
    TIFINAGH = 57
    TIRHUTA = 124
    TOTO = 160
    UGARITIC = 53
    UNKNOWN = 61
    VAI = 74
    VITHKUQI = 161
    WANCHO = 152
    WARANG_CITI = 125
    YEZIDI = 156
    YI = 41
    ZANABAZAR_SQUARE = 141
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__dict__': <attribute '__dict__' of 'UnicodeScript' objects>, '__doc__': None, '__gtype__': <GType GUnicodeScript (163504992)>, '__enum_values__': {-1: <enum G_UNICODE_SCRIPT_INVALID_CODE of type GLib.UnicodeScript>, 0: <enum G_UNICODE_SCRIPT_COMMON of type GLib.UnicodeScript>, 1: <enum G_UNICODE_SCRIPT_INHERITED of type GLib.UnicodeScript>, 2: <enum G_UNICODE_SCRIPT_ARABIC of type GLib.UnicodeScript>, 3: <enum G_UNICODE_SCRIPT_ARMENIAN of type GLib.UnicodeScript>, 4: <enum G_UNICODE_SCRIPT_BENGALI of type GLib.UnicodeScript>, 5: <enum G_UNICODE_SCRIPT_BOPOMOFO of type GLib.UnicodeScript>, 6: <enum G_UNICODE_SCRIPT_CHEROKEE of type GLib.UnicodeScript>, 7: <enum G_UNICODE_SCRIPT_COPTIC of type GLib.UnicodeScript>, 8: <enum G_UNICODE_SCRIPT_CYRILLIC of type GLib.UnicodeScript>, 9: <enum G_UNICODE_SCRIPT_DESERET of type GLib.UnicodeScript>, 10: <enum G_UNICODE_SCRIPT_DEVANAGARI of type GLib.UnicodeScript>, 11: <enum G_UNICODE_SCRIPT_ETHIOPIC of type GLib.UnicodeScript>, 12: <enum G_UNICODE_SCRIPT_GEORGIAN of type GLib.UnicodeScript>, 13: <enum G_UNICODE_SCRIPT_GOTHIC of type GLib.UnicodeScript>, 14: <enum G_UNICODE_SCRIPT_GREEK of type GLib.UnicodeScript>, 15: <enum G_UNICODE_SCRIPT_GUJARATI of type GLib.UnicodeScript>, 16: <enum G_UNICODE_SCRIPT_GURMUKHI of type GLib.UnicodeScript>, 17: <enum G_UNICODE_SCRIPT_HAN of type GLib.UnicodeScript>, 18: <enum G_UNICODE_SCRIPT_HANGUL of type GLib.UnicodeScript>, 19: <enum G_UNICODE_SCRIPT_HEBREW of type GLib.UnicodeScript>, 20: <enum G_UNICODE_SCRIPT_HIRAGANA of type GLib.UnicodeScript>, 21: <enum G_UNICODE_SCRIPT_KANNADA of type GLib.UnicodeScript>, 22: <enum G_UNICODE_SCRIPT_KATAKANA of type GLib.UnicodeScript>, 23: <enum G_UNICODE_SCRIPT_KHMER of type GLib.UnicodeScript>, 24: <enum G_UNICODE_SCRIPT_LAO of type GLib.UnicodeScript>, 25: <enum G_UNICODE_SCRIPT_LATIN of type GLib.UnicodeScript>, 26: <enum G_UNICODE_SCRIPT_MALAYALAM of type GLib.UnicodeScript>, 27: <enum G_UNICODE_SCRIPT_MONGOLIAN of type GLib.UnicodeScript>, 28: <enum G_UNICODE_SCRIPT_MYANMAR of type GLib.UnicodeScript>, 29: <enum G_UNICODE_SCRIPT_OGHAM of type GLib.UnicodeScript>, 30: <enum G_UNICODE_SCRIPT_OLD_ITALIC of type GLib.UnicodeScript>, 31: <enum G_UNICODE_SCRIPT_ORIYA of type GLib.UnicodeScript>, 32: <enum G_UNICODE_SCRIPT_RUNIC of type GLib.UnicodeScript>, 33: <enum G_UNICODE_SCRIPT_SINHALA of type GLib.UnicodeScript>, 34: <enum G_UNICODE_SCRIPT_SYRIAC of type GLib.UnicodeScript>, 35: <enum G_UNICODE_SCRIPT_TAMIL of type GLib.UnicodeScript>, 36: <enum G_UNICODE_SCRIPT_TELUGU of type GLib.UnicodeScript>, 37: <enum G_UNICODE_SCRIPT_THAANA of type GLib.UnicodeScript>, 38: <enum G_UNICODE_SCRIPT_THAI of type GLib.UnicodeScript>, 39: <enum G_UNICODE_SCRIPT_TIBETAN of type GLib.UnicodeScript>, 40: <enum G_UNICODE_SCRIPT_CANADIAN_ABORIGINAL of type GLib.UnicodeScript>, 41: <enum G_UNICODE_SCRIPT_YI of type GLib.UnicodeScript>, 42: <enum G_UNICODE_SCRIPT_TAGALOG of type GLib.UnicodeScript>, 43: <enum G_UNICODE_SCRIPT_HANUNOO of type GLib.UnicodeScript>, 44: <enum G_UNICODE_SCRIPT_BUHID of type GLib.UnicodeScript>, 45: <enum G_UNICODE_SCRIPT_TAGBANWA of type GLib.UnicodeScript>, 46: <enum G_UNICODE_SCRIPT_BRAILLE of type GLib.UnicodeScript>, 47: <enum G_UNICODE_SCRIPT_CYPRIOT of type GLib.UnicodeScript>, 48: <enum G_UNICODE_SCRIPT_LIMBU of type GLib.UnicodeScript>, 49: <enum G_UNICODE_SCRIPT_OSMANYA of type GLib.UnicodeScript>, 50: <enum G_UNICODE_SCRIPT_SHAVIAN of type GLib.UnicodeScript>, 51: <enum G_UNICODE_SCRIPT_LINEAR_B of type GLib.UnicodeScript>, 52: <enum G_UNICODE_SCRIPT_TAI_LE of type GLib.UnicodeScript>, 53: <enum G_UNICODE_SCRIPT_UGARITIC of type GLib.UnicodeScript>, 54: <enum G_UNICODE_SCRIPT_NEW_TAI_LUE of type GLib.UnicodeScript>, 55: <enum G_UNICODE_SCRIPT_BUGINESE of type GLib.UnicodeScript>, 56: <enum G_UNICODE_SCRIPT_GLAGOLITIC of type GLib.UnicodeScript>, 57: <enum G_UNICODE_SCRIPT_TIFINAGH of type GLib.UnicodeScript>, 58: <enum G_UNICODE_SCRIPT_SYLOTI_NAGRI of type GLib.UnicodeScript>, 59: <enum G_UNICODE_SCRIPT_OLD_PERSIAN of type GLib.UnicodeScript>, 60: <enum G_UNICODE_SCRIPT_KHAROSHTHI of type GLib.UnicodeScript>, 61: <enum G_UNICODE_SCRIPT_UNKNOWN of type GLib.UnicodeScript>, 62: <enum G_UNICODE_SCRIPT_BALINESE of type GLib.UnicodeScript>, 63: <enum G_UNICODE_SCRIPT_CUNEIFORM of type GLib.UnicodeScript>, 64: <enum G_UNICODE_SCRIPT_PHOENICIAN of type GLib.UnicodeScript>, 65: <enum G_UNICODE_SCRIPT_PHAGS_PA of type GLib.UnicodeScript>, 66: <enum G_UNICODE_SCRIPT_NKO of type GLib.UnicodeScript>, 67: <enum G_UNICODE_SCRIPT_KAYAH_LI of type GLib.UnicodeScript>, 68: <enum G_UNICODE_SCRIPT_LEPCHA of type GLib.UnicodeScript>, 69: <enum G_UNICODE_SCRIPT_REJANG of type GLib.UnicodeScript>, 70: <enum G_UNICODE_SCRIPT_SUNDANESE of type GLib.UnicodeScript>, 71: <enum G_UNICODE_SCRIPT_SAURASHTRA of type GLib.UnicodeScript>, 72: <enum G_UNICODE_SCRIPT_CHAM of type GLib.UnicodeScript>, 73: <enum G_UNICODE_SCRIPT_OL_CHIKI of type GLib.UnicodeScript>, 74: <enum G_UNICODE_SCRIPT_VAI of type GLib.UnicodeScript>, 75: <enum G_UNICODE_SCRIPT_CARIAN of type GLib.UnicodeScript>, 76: <enum G_UNICODE_SCRIPT_LYCIAN of type GLib.UnicodeScript>, 77: <enum G_UNICODE_SCRIPT_LYDIAN of type GLib.UnicodeScript>, 78: <enum G_UNICODE_SCRIPT_AVESTAN of type GLib.UnicodeScript>, 79: <enum G_UNICODE_SCRIPT_BAMUM of type GLib.UnicodeScript>, 80: <enum G_UNICODE_SCRIPT_EGYPTIAN_HIEROGLYPHS of type GLib.UnicodeScript>, 81: <enum G_UNICODE_SCRIPT_IMPERIAL_ARAMAIC of type GLib.UnicodeScript>, 82: <enum G_UNICODE_SCRIPT_INSCRIPTIONAL_PAHLAVI of type GLib.UnicodeScript>, 83: <enum G_UNICODE_SCRIPT_INSCRIPTIONAL_PARTHIAN of type GLib.UnicodeScript>, 84: <enum G_UNICODE_SCRIPT_JAVANESE of type GLib.UnicodeScript>, 85: <enum G_UNICODE_SCRIPT_KAITHI of type GLib.UnicodeScript>, 86: <enum G_UNICODE_SCRIPT_LISU of type GLib.UnicodeScript>, 87: <enum G_UNICODE_SCRIPT_MEETEI_MAYEK of type GLib.UnicodeScript>, 88: <enum G_UNICODE_SCRIPT_OLD_SOUTH_ARABIAN of type GLib.UnicodeScript>, 89: <enum G_UNICODE_SCRIPT_OLD_TURKIC of type GLib.UnicodeScript>, 90: <enum G_UNICODE_SCRIPT_SAMARITAN of type GLib.UnicodeScript>, 91: <enum G_UNICODE_SCRIPT_TAI_THAM of type GLib.UnicodeScript>, 92: <enum G_UNICODE_SCRIPT_TAI_VIET of type GLib.UnicodeScript>, 93: <enum G_UNICODE_SCRIPT_BATAK of type GLib.UnicodeScript>, 94: <enum G_UNICODE_SCRIPT_BRAHMI of type GLib.UnicodeScript>, 95: <enum G_UNICODE_SCRIPT_MANDAIC of type GLib.UnicodeScript>, 96: <enum G_UNICODE_SCRIPT_CHAKMA of type GLib.UnicodeScript>, 97: <enum G_UNICODE_SCRIPT_MEROITIC_CURSIVE of type GLib.UnicodeScript>, 98: <enum G_UNICODE_SCRIPT_MEROITIC_HIEROGLYPHS of type GLib.UnicodeScript>, 99: <enum G_UNICODE_SCRIPT_MIAO of type GLib.UnicodeScript>, 100: <enum G_UNICODE_SCRIPT_SHARADA of type GLib.UnicodeScript>, 101: <enum G_UNICODE_SCRIPT_SORA_SOMPENG of type GLib.UnicodeScript>, 102: <enum G_UNICODE_SCRIPT_TAKRI of type GLib.UnicodeScript>, 103: <enum G_UNICODE_SCRIPT_BASSA_VAH of type GLib.UnicodeScript>, 104: <enum G_UNICODE_SCRIPT_CAUCASIAN_ALBANIAN of type GLib.UnicodeScript>, 105: <enum G_UNICODE_SCRIPT_DUPLOYAN of type GLib.UnicodeScript>, 106: <enum G_UNICODE_SCRIPT_ELBASAN of type GLib.UnicodeScript>, 107: <enum G_UNICODE_SCRIPT_GRANTHA of type GLib.UnicodeScript>, 108: <enum G_UNICODE_SCRIPT_KHOJKI of type GLib.UnicodeScript>, 109: <enum G_UNICODE_SCRIPT_KHUDAWADI of type GLib.UnicodeScript>, 110: <enum G_UNICODE_SCRIPT_LINEAR_A of type GLib.UnicodeScript>, 111: <enum G_UNICODE_SCRIPT_MAHAJANI of type GLib.UnicodeScript>, 112: <enum G_UNICODE_SCRIPT_MANICHAEAN of type GLib.UnicodeScript>, 113: <enum G_UNICODE_SCRIPT_MENDE_KIKAKUI of type GLib.UnicodeScript>, 114: <enum G_UNICODE_SCRIPT_MODI of type GLib.UnicodeScript>, 115: <enum G_UNICODE_SCRIPT_MRO of type GLib.UnicodeScript>, 116: <enum G_UNICODE_SCRIPT_NABATAEAN of type GLib.UnicodeScript>, 117: <enum G_UNICODE_SCRIPT_OLD_NORTH_ARABIAN of type GLib.UnicodeScript>, 118: <enum G_UNICODE_SCRIPT_OLD_PERMIC of type GLib.UnicodeScript>, 119: <enum G_UNICODE_SCRIPT_PAHAWH_HMONG of type GLib.UnicodeScript>, 120: <enum G_UNICODE_SCRIPT_PALMYRENE of type GLib.UnicodeScript>, 121: <enum G_UNICODE_SCRIPT_PAU_CIN_HAU of type GLib.UnicodeScript>, 122: <enum G_UNICODE_SCRIPT_PSALTER_PAHLAVI of type GLib.UnicodeScript>, 123: <enum G_UNICODE_SCRIPT_SIDDHAM of type GLib.UnicodeScript>, 124: <enum G_UNICODE_SCRIPT_TIRHUTA of type GLib.UnicodeScript>, 125: <enum G_UNICODE_SCRIPT_WARANG_CITI of type GLib.UnicodeScript>, 126: <enum G_UNICODE_SCRIPT_AHOM of type GLib.UnicodeScript>, 127: <enum G_UNICODE_SCRIPT_ANATOLIAN_HIEROGLYPHS of type GLib.UnicodeScript>, 128: <enum G_UNICODE_SCRIPT_HATRAN of type GLib.UnicodeScript>, 129: <enum G_UNICODE_SCRIPT_MULTANI of type GLib.UnicodeScript>, 130: <enum G_UNICODE_SCRIPT_OLD_HUNGARIAN of type GLib.UnicodeScript>, 131: <enum G_UNICODE_SCRIPT_SIGNWRITING of type GLib.UnicodeScript>, 132: <enum G_UNICODE_SCRIPT_ADLAM of type GLib.UnicodeScript>, 133: <enum G_UNICODE_SCRIPT_BHAIKSUKI of type GLib.UnicodeScript>, 134: <enum G_UNICODE_SCRIPT_MARCHEN of type GLib.UnicodeScript>, 135: <enum G_UNICODE_SCRIPT_NEWA of type GLib.UnicodeScript>, 136: <enum G_UNICODE_SCRIPT_OSAGE of type GLib.UnicodeScript>, 137: <enum G_UNICODE_SCRIPT_TANGUT of type GLib.UnicodeScript>, 138: <enum G_UNICODE_SCRIPT_MASARAM_GONDI of type GLib.UnicodeScript>, 139: <enum G_UNICODE_SCRIPT_NUSHU of type GLib.UnicodeScript>, 140: <enum G_UNICODE_SCRIPT_SOYOMBO of type GLib.UnicodeScript>, 141: <enum G_UNICODE_SCRIPT_ZANABAZAR_SQUARE of type GLib.UnicodeScript>, 142: <enum G_UNICODE_SCRIPT_DOGRA of type GLib.UnicodeScript>, 143: <enum G_UNICODE_SCRIPT_GUNJALA_GONDI of type GLib.UnicodeScript>, 144: <enum G_UNICODE_SCRIPT_HANIFI_ROHINGYA of type GLib.UnicodeScript>, 145: <enum G_UNICODE_SCRIPT_MAKASAR of type GLib.UnicodeScript>, 146: <enum G_UNICODE_SCRIPT_MEDEFAIDRIN of type GLib.UnicodeScript>, 147: <enum G_UNICODE_SCRIPT_OLD_SOGDIAN of type GLib.UnicodeScript>, 148: <enum G_UNICODE_SCRIPT_SOGDIAN of type GLib.UnicodeScript>, 149: <enum G_UNICODE_SCRIPT_ELYMAIC of type GLib.UnicodeScript>, 150: <enum G_UNICODE_SCRIPT_NANDINAGARI of type GLib.UnicodeScript>, 151: <enum G_UNICODE_SCRIPT_NYIAKENG_PUACHUE_HMONG of type GLib.UnicodeScript>, 152: <enum G_UNICODE_SCRIPT_WANCHO of type GLib.UnicodeScript>, 153: <enum G_UNICODE_SCRIPT_CHORASMIAN of type GLib.UnicodeScript>, 154: <enum G_UNICODE_SCRIPT_DIVES_AKURU of type GLib.UnicodeScript>, 155: <enum G_UNICODE_SCRIPT_KHITAN_SMALL_SCRIPT of type GLib.UnicodeScript>, 156: <enum G_UNICODE_SCRIPT_YEZIDI of type GLib.UnicodeScript>, 157: <enum G_UNICODE_SCRIPT_CYPRO_MINOAN of type GLib.UnicodeScript>, 158: <enum G_UNICODE_SCRIPT_OLD_UYGHUR of type GLib.UnicodeScript>, 159: <enum G_UNICODE_SCRIPT_TANGSA of type GLib.UnicodeScript>, 160: <enum G_UNICODE_SCRIPT_TOTO of type GLib.UnicodeScript>, 161: <enum G_UNICODE_SCRIPT_VITHKUQI of type GLib.UnicodeScript>, 162: <enum G_UNICODE_SCRIPT_MATH of type GLib.UnicodeScript>, 163: <enum G_UNICODE_SCRIPT_KAWI of type GLib.UnicodeScript>, 164: <enum G_UNICODE_SCRIPT_NAG_MUNDARI of type GLib.UnicodeScript>}, '__info__': gi.EnumInfo(UnicodeScript), 'INVALID_CODE': <enum G_UNICODE_SCRIPT_INVALID_CODE of type GLib.UnicodeScript>, 'COMMON': <enum G_UNICODE_SCRIPT_COMMON of type GLib.UnicodeScript>, 'INHERITED': <enum G_UNICODE_SCRIPT_INHERITED of type GLib.UnicodeScript>, 'ARABIC': <enum G_UNICODE_SCRIPT_ARABIC of type GLib.UnicodeScript>, 'ARMENIAN': <enum G_UNICODE_SCRIPT_ARMENIAN of type GLib.UnicodeScript>, 'BENGALI': <enum G_UNICODE_SCRIPT_BENGALI of type GLib.UnicodeScript>, 'BOPOMOFO': <enum G_UNICODE_SCRIPT_BOPOMOFO of type GLib.UnicodeScript>, 'CHEROKEE': <enum G_UNICODE_SCRIPT_CHEROKEE of type GLib.UnicodeScript>, 'COPTIC': <enum G_UNICODE_SCRIPT_COPTIC of type GLib.UnicodeScript>, 'CYRILLIC': <enum G_UNICODE_SCRIPT_CYRILLIC of type GLib.UnicodeScript>, 'DESERET': <enum G_UNICODE_SCRIPT_DESERET of type GLib.UnicodeScript>, 'DEVANAGARI': <enum G_UNICODE_SCRIPT_DEVANAGARI of type GLib.UnicodeScript>, 'ETHIOPIC': <enum G_UNICODE_SCRIPT_ETHIOPIC of type GLib.UnicodeScript>, 'GEORGIAN': <enum G_UNICODE_SCRIPT_GEORGIAN of type GLib.UnicodeScript>, 'GOTHIC': <enum G_UNICODE_SCRIPT_GOTHIC of type GLib.UnicodeScript>, 'GREEK': <enum G_UNICODE_SCRIPT_GREEK of type GLib.UnicodeScript>, 'GUJARATI': <enum G_UNICODE_SCRIPT_GUJARATI of type GLib.UnicodeScript>, 'GURMUKHI': <enum G_UNICODE_SCRIPT_GURMUKHI of type GLib.UnicodeScript>, 'HAN': <enum G_UNICODE_SCRIPT_HAN of type GLib.UnicodeScript>, 'HANGUL': <enum G_UNICODE_SCRIPT_HANGUL of type GLib.UnicodeScript>, 'HEBREW': <enum G_UNICODE_SCRIPT_HEBREW of type GLib.UnicodeScript>, 'HIRAGANA': <enum G_UNICODE_SCRIPT_HIRAGANA of type GLib.UnicodeScript>, 'KANNADA': <enum G_UNICODE_SCRIPT_KANNADA of type GLib.UnicodeScript>, 'KATAKANA': <enum G_UNICODE_SCRIPT_KATAKANA of type GLib.UnicodeScript>, 'KHMER': <enum G_UNICODE_SCRIPT_KHMER of type GLib.UnicodeScript>, 'LAO': <enum G_UNICODE_SCRIPT_LAO of type GLib.UnicodeScript>, 'LATIN': <enum G_UNICODE_SCRIPT_LATIN of type GLib.UnicodeScript>, 'MALAYALAM': <enum G_UNICODE_SCRIPT_MALAYALAM of type GLib.UnicodeScript>, 'MONGOLIAN': <enum G_UNICODE_SCRIPT_MONGOLIAN of type GLib.UnicodeScript>, 'MYANMAR': <enum G_UNICODE_SCRIPT_MYANMAR of type GLib.UnicodeScript>, 'OGHAM': <enum G_UNICODE_SCRIPT_OGHAM of type GLib.UnicodeScript>, 'OLD_ITALIC': <enum G_UNICODE_SCRIPT_OLD_ITALIC of type GLib.UnicodeScript>, 'ORIYA': <enum G_UNICODE_SCRIPT_ORIYA of type GLib.UnicodeScript>, 'RUNIC': <enum G_UNICODE_SCRIPT_RUNIC of type GLib.UnicodeScript>, 'SINHALA': <enum G_UNICODE_SCRIPT_SINHALA of type GLib.UnicodeScript>, 'SYRIAC': <enum G_UNICODE_SCRIPT_SYRIAC of type GLib.UnicodeScript>, 'TAMIL': <enum G_UNICODE_SCRIPT_TAMIL of type GLib.UnicodeScript>, 'TELUGU': <enum G_UNICODE_SCRIPT_TELUGU of type GLib.UnicodeScript>, 'THAANA': <enum G_UNICODE_SCRIPT_THAANA of type GLib.UnicodeScript>, 'THAI': <enum G_UNICODE_SCRIPT_THAI of type GLib.UnicodeScript>, 'TIBETAN': <enum G_UNICODE_SCRIPT_TIBETAN of type GLib.UnicodeScript>, 'CANADIAN_ABORIGINAL': <enum G_UNICODE_SCRIPT_CANADIAN_ABORIGINAL of type GLib.UnicodeScript>, 'YI': <enum G_UNICODE_SCRIPT_YI of type GLib.UnicodeScript>, 'TAGALOG': <enum G_UNICODE_SCRIPT_TAGALOG of type GLib.UnicodeScript>, 'HANUNOO': <enum G_UNICODE_SCRIPT_HANUNOO of type GLib.UnicodeScript>, 'BUHID': <enum G_UNICODE_SCRIPT_BUHID of type GLib.UnicodeScript>, 'TAGBANWA': <enum G_UNICODE_SCRIPT_TAGBANWA of type GLib.UnicodeScript>, 'BRAILLE': <enum G_UNICODE_SCRIPT_BRAILLE of type GLib.UnicodeScript>, 'CYPRIOT': <enum G_UNICODE_SCRIPT_CYPRIOT of type GLib.UnicodeScript>, 'LIMBU': <enum G_UNICODE_SCRIPT_LIMBU of type GLib.UnicodeScript>, 'OSMANYA': <enum G_UNICODE_SCRIPT_OSMANYA of type GLib.UnicodeScript>, 'SHAVIAN': <enum G_UNICODE_SCRIPT_SHAVIAN of type GLib.UnicodeScript>, 'LINEAR_B': <enum G_UNICODE_SCRIPT_LINEAR_B of type GLib.UnicodeScript>, 'TAI_LE': <enum G_UNICODE_SCRIPT_TAI_LE of type GLib.UnicodeScript>, 'UGARITIC': <enum G_UNICODE_SCRIPT_UGARITIC of type GLib.UnicodeScript>, 'NEW_TAI_LUE': <enum G_UNICODE_SCRIPT_NEW_TAI_LUE of type GLib.UnicodeScript>, 'BUGINESE': <enum G_UNICODE_SCRIPT_BUGINESE of type GLib.UnicodeScript>, 'GLAGOLITIC': <enum G_UNICODE_SCRIPT_GLAGOLITIC of type GLib.UnicodeScript>, 'TIFINAGH': <enum G_UNICODE_SCRIPT_TIFINAGH of type GLib.UnicodeScript>, 'SYLOTI_NAGRI': <enum G_UNICODE_SCRIPT_SYLOTI_NAGRI of type GLib.UnicodeScript>, 'OLD_PERSIAN': <enum G_UNICODE_SCRIPT_OLD_PERSIAN of type GLib.UnicodeScript>, 'KHAROSHTHI': <enum G_UNICODE_SCRIPT_KHAROSHTHI of type GLib.UnicodeScript>, 'UNKNOWN': <enum G_UNICODE_SCRIPT_UNKNOWN of type GLib.UnicodeScript>, 'BALINESE': <enum G_UNICODE_SCRIPT_BALINESE of type GLib.UnicodeScript>, 'CUNEIFORM': <enum G_UNICODE_SCRIPT_CUNEIFORM of type GLib.UnicodeScript>, 'PHOENICIAN': <enum G_UNICODE_SCRIPT_PHOENICIAN of type GLib.UnicodeScript>, 'PHAGS_PA': <enum G_UNICODE_SCRIPT_PHAGS_PA of type GLib.UnicodeScript>, 'NKO': <enum G_UNICODE_SCRIPT_NKO of type GLib.UnicodeScript>, 'KAYAH_LI': <enum G_UNICODE_SCRIPT_KAYAH_LI of type GLib.UnicodeScript>, 'LEPCHA': <enum G_UNICODE_SCRIPT_LEPCHA of type GLib.UnicodeScript>, 'REJANG': <enum G_UNICODE_SCRIPT_REJANG of type GLib.UnicodeScript>, 'SUNDANESE': <enum G_UNICODE_SCRIPT_SUNDANESE of type GLib.UnicodeScript>, 'SAURASHTRA': <enum G_UNICODE_SCRIPT_SAURASHTRA of type GLib.UnicodeScript>, 'CHAM': <enum G_UNICODE_SCRIPT_CHAM of type GLib.UnicodeScript>, 'OL_CHIKI': <enum G_UNICODE_SCRIPT_OL_CHIKI of type GLib.UnicodeScript>, 'VAI': <enum G_UNICODE_SCRIPT_VAI of type GLib.UnicodeScript>, 'CARIAN': <enum G_UNICODE_SCRIPT_CARIAN of type GLib.UnicodeScript>, 'LYCIAN': <enum G_UNICODE_SCRIPT_LYCIAN of type GLib.UnicodeScript>, 'LYDIAN': <enum G_UNICODE_SCRIPT_LYDIAN of type GLib.UnicodeScript>, 'AVESTAN': <enum G_UNICODE_SCRIPT_AVESTAN of type GLib.UnicodeScript>, 'BAMUM': <enum G_UNICODE_SCRIPT_BAMUM of type GLib.UnicodeScript>, 'EGYPTIAN_HIEROGLYPHS': <enum G_UNICODE_SCRIPT_EGYPTIAN_HIEROGLYPHS of type GLib.UnicodeScript>, 'IMPERIAL_ARAMAIC': <enum G_UNICODE_SCRIPT_IMPERIAL_ARAMAIC of type GLib.UnicodeScript>, 'INSCRIPTIONAL_PAHLAVI': <enum G_UNICODE_SCRIPT_INSCRIPTIONAL_PAHLAVI of type GLib.UnicodeScript>, 'INSCRIPTIONAL_PARTHIAN': <enum G_UNICODE_SCRIPT_INSCRIPTIONAL_PARTHIAN of type GLib.UnicodeScript>, 'JAVANESE': <enum G_UNICODE_SCRIPT_JAVANESE of type GLib.UnicodeScript>, 'KAITHI': <enum G_UNICODE_SCRIPT_KAITHI of type GLib.UnicodeScript>, 'LISU': <enum G_UNICODE_SCRIPT_LISU of type GLib.UnicodeScript>, 'MEETEI_MAYEK': <enum G_UNICODE_SCRIPT_MEETEI_MAYEK of type GLib.UnicodeScript>, 'OLD_SOUTH_ARABIAN': <enum G_UNICODE_SCRIPT_OLD_SOUTH_ARABIAN of type GLib.UnicodeScript>, 'OLD_TURKIC': <enum G_UNICODE_SCRIPT_OLD_TURKIC of type GLib.UnicodeScript>, 'SAMARITAN': <enum G_UNICODE_SCRIPT_SAMARITAN of type GLib.UnicodeScript>, 'TAI_THAM': <enum G_UNICODE_SCRIPT_TAI_THAM of type GLib.UnicodeScript>, 'TAI_VIET': <enum G_UNICODE_SCRIPT_TAI_VIET of type GLib.UnicodeScript>, 'BATAK': <enum G_UNICODE_SCRIPT_BATAK of type GLib.UnicodeScript>, 'BRAHMI': <enum G_UNICODE_SCRIPT_BRAHMI of type GLib.UnicodeScript>, 'MANDAIC': <enum G_UNICODE_SCRIPT_MANDAIC of type GLib.UnicodeScript>, 'CHAKMA': <enum G_UNICODE_SCRIPT_CHAKMA of type GLib.UnicodeScript>, 'MEROITIC_CURSIVE': <enum G_UNICODE_SCRIPT_MEROITIC_CURSIVE of type GLib.UnicodeScript>, 'MEROITIC_HIEROGLYPHS': <enum G_UNICODE_SCRIPT_MEROITIC_HIEROGLYPHS of type GLib.UnicodeScript>, 'MIAO': <enum G_UNICODE_SCRIPT_MIAO of type GLib.UnicodeScript>, 'SHARADA': <enum G_UNICODE_SCRIPT_SHARADA of type GLib.UnicodeScript>, 'SORA_SOMPENG': <enum G_UNICODE_SCRIPT_SORA_SOMPENG of type GLib.UnicodeScript>, 'TAKRI': <enum G_UNICODE_SCRIPT_TAKRI of type GLib.UnicodeScript>, 'BASSA_VAH': <enum G_UNICODE_SCRIPT_BASSA_VAH of type GLib.UnicodeScript>, 'CAUCASIAN_ALBANIAN': <enum G_UNICODE_SCRIPT_CAUCASIAN_ALBANIAN of type GLib.UnicodeScript>, 'DUPLOYAN': <enum G_UNICODE_SCRIPT_DUPLOYAN of type GLib.UnicodeScript>, 'ELBASAN': <enum G_UNICODE_SCRIPT_ELBASAN of type GLib.UnicodeScript>, 'GRANTHA': <enum G_UNICODE_SCRIPT_GRANTHA of type GLib.UnicodeScript>, 'KHOJKI': <enum G_UNICODE_SCRIPT_KHOJKI of type GLib.UnicodeScript>, 'KHUDAWADI': <enum G_UNICODE_SCRIPT_KHUDAWADI of type GLib.UnicodeScript>, 'LINEAR_A': <enum G_UNICODE_SCRIPT_LINEAR_A of type GLib.UnicodeScript>, 'MAHAJANI': <enum G_UNICODE_SCRIPT_MAHAJANI of type GLib.UnicodeScript>, 'MANICHAEAN': <enum G_UNICODE_SCRIPT_MANICHAEAN of type GLib.UnicodeScript>, 'MENDE_KIKAKUI': <enum G_UNICODE_SCRIPT_MENDE_KIKAKUI of type GLib.UnicodeScript>, 'MODI': <enum G_UNICODE_SCRIPT_MODI of type GLib.UnicodeScript>, 'MRO': <enum G_UNICODE_SCRIPT_MRO of type GLib.UnicodeScript>, 'NABATAEAN': <enum G_UNICODE_SCRIPT_NABATAEAN of type GLib.UnicodeScript>, 'OLD_NORTH_ARABIAN': <enum G_UNICODE_SCRIPT_OLD_NORTH_ARABIAN of type GLib.UnicodeScript>, 'OLD_PERMIC': <enum G_UNICODE_SCRIPT_OLD_PERMIC of type GLib.UnicodeScript>, 'PAHAWH_HMONG': <enum G_UNICODE_SCRIPT_PAHAWH_HMONG of type GLib.UnicodeScript>, 'PALMYRENE': <enum G_UNICODE_SCRIPT_PALMYRENE of type GLib.UnicodeScript>, 'PAU_CIN_HAU': <enum G_UNICODE_SCRIPT_PAU_CIN_HAU of type GLib.UnicodeScript>, 'PSALTER_PAHLAVI': <enum G_UNICODE_SCRIPT_PSALTER_PAHLAVI of type GLib.UnicodeScript>, 'SIDDHAM': <enum G_UNICODE_SCRIPT_SIDDHAM of type GLib.UnicodeScript>, 'TIRHUTA': <enum G_UNICODE_SCRIPT_TIRHUTA of type GLib.UnicodeScript>, 'WARANG_CITI': <enum G_UNICODE_SCRIPT_WARANG_CITI of type GLib.UnicodeScript>, 'AHOM': <enum G_UNICODE_SCRIPT_AHOM of type GLib.UnicodeScript>, 'ANATOLIAN_HIEROGLYPHS': <enum G_UNICODE_SCRIPT_ANATOLIAN_HIEROGLYPHS of type GLib.UnicodeScript>, 'HATRAN': <enum G_UNICODE_SCRIPT_HATRAN of type GLib.UnicodeScript>, 'MULTANI': <enum G_UNICODE_SCRIPT_MULTANI of type GLib.UnicodeScript>, 'OLD_HUNGARIAN': <enum G_UNICODE_SCRIPT_OLD_HUNGARIAN of type GLib.UnicodeScript>, 'SIGNWRITING': <enum G_UNICODE_SCRIPT_SIGNWRITING of type GLib.UnicodeScript>, 'ADLAM': <enum G_UNICODE_SCRIPT_ADLAM of type GLib.UnicodeScript>, 'BHAIKSUKI': <enum G_UNICODE_SCRIPT_BHAIKSUKI of type GLib.UnicodeScript>, 'MARCHEN': <enum G_UNICODE_SCRIPT_MARCHEN of type GLib.UnicodeScript>, 'NEWA': <enum G_UNICODE_SCRIPT_NEWA of type GLib.UnicodeScript>, 'OSAGE': <enum G_UNICODE_SCRIPT_OSAGE of type GLib.UnicodeScript>, 'TANGUT': <enum G_UNICODE_SCRIPT_TANGUT of type GLib.UnicodeScript>, 'MASARAM_GONDI': <enum G_UNICODE_SCRIPT_MASARAM_GONDI of type GLib.UnicodeScript>, 'NUSHU': <enum G_UNICODE_SCRIPT_NUSHU of type GLib.UnicodeScript>, 'SOYOMBO': <enum G_UNICODE_SCRIPT_SOYOMBO of type GLib.UnicodeScript>, 'ZANABAZAR_SQUARE': <enum G_UNICODE_SCRIPT_ZANABAZAR_SQUARE of type GLib.UnicodeScript>, 'DOGRA': <enum G_UNICODE_SCRIPT_DOGRA of type GLib.UnicodeScript>, 'GUNJALA_GONDI': <enum G_UNICODE_SCRIPT_GUNJALA_GONDI of type GLib.UnicodeScript>, 'HANIFI_ROHINGYA': <enum G_UNICODE_SCRIPT_HANIFI_ROHINGYA of type GLib.UnicodeScript>, 'MAKASAR': <enum G_UNICODE_SCRIPT_MAKASAR of type GLib.UnicodeScript>, 'MEDEFAIDRIN': <enum G_UNICODE_SCRIPT_MEDEFAIDRIN of type GLib.UnicodeScript>, 'OLD_SOGDIAN': <enum G_UNICODE_SCRIPT_OLD_SOGDIAN of type GLib.UnicodeScript>, 'SOGDIAN': <enum G_UNICODE_SCRIPT_SOGDIAN of type GLib.UnicodeScript>, 'ELYMAIC': <enum G_UNICODE_SCRIPT_ELYMAIC of type GLib.UnicodeScript>, 'NANDINAGARI': <enum G_UNICODE_SCRIPT_NANDINAGARI of type GLib.UnicodeScript>, 'NYIAKENG_PUACHUE_HMONG': <enum G_UNICODE_SCRIPT_NYIAKENG_PUACHUE_HMONG of type GLib.UnicodeScript>, 'WANCHO': <enum G_UNICODE_SCRIPT_WANCHO of type GLib.UnicodeScript>, 'CHORASMIAN': <enum G_UNICODE_SCRIPT_CHORASMIAN of type GLib.UnicodeScript>, 'DIVES_AKURU': <enum G_UNICODE_SCRIPT_DIVES_AKURU of type GLib.UnicodeScript>, 'KHITAN_SMALL_SCRIPT': <enum G_UNICODE_SCRIPT_KHITAN_SMALL_SCRIPT of type GLib.UnicodeScript>, 'YEZIDI': <enum G_UNICODE_SCRIPT_YEZIDI of type GLib.UnicodeScript>, 'CYPRO_MINOAN': <enum G_UNICODE_SCRIPT_CYPRO_MINOAN of type GLib.UnicodeScript>, 'OLD_UYGHUR': <enum G_UNICODE_SCRIPT_OLD_UYGHUR of type GLib.UnicodeScript>, 'TANGSA': <enum G_UNICODE_SCRIPT_TANGSA of type GLib.UnicodeScript>, 'TOTO': <enum G_UNICODE_SCRIPT_TOTO of type GLib.UnicodeScript>, 'VITHKUQI': <enum G_UNICODE_SCRIPT_VITHKUQI of type GLib.UnicodeScript>, 'MATH': <enum G_UNICODE_SCRIPT_MATH of type GLib.UnicodeScript>, 'KAWI': <enum G_UNICODE_SCRIPT_KAWI of type GLib.UnicodeScript>, 'NAG_MUNDARI': <enum G_UNICODE_SCRIPT_NAG_MUNDARI of type GLib.UnicodeScript>, 'from_iso15924': gi.FunctionInfo(from_iso15924, bound=None), 'to_iso15924': gi.FunctionInfo(to_iso15924, bound=None)})"
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
        117: 117,
        118: 118,
        119: 119,
        120: 120,
        121: 121,
        122: 122,
        123: 123,
        124: 124,
        125: 125,
        126: 126,
        127: 127,
        128: 128,
        129: 129,
        130: 130,
        131: 131,
        132: 132,
        133: 133,
        134: 134,
        135: 135,
        136: 136,
        137: 137,
        138: 138,
        139: 139,
        140: 140,
        141: 141,
        142: 142,
        143: 143,
        144: 144,
        145: 145,
        146: 146,
        147: 147,
        148: 148,
        149: 149,
        150: 150,
        151: 151,
        152: 152,
        153: 153,
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
    }
    __gtype__ = None # (!) real value is '<GType GUnicodeScript (163504992)>'
    __info__ = gi.EnumInfo(UnicodeScript)


