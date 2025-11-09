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


class script_t(__gobject.GFlags):
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


    B_SCRIPT_ADLAM = 1097100397
    B_SCRIPT_AHOM = 1097363309
    B_SCRIPT_ANATOLIAN_HIEROGLYPHS = 1215067511
    B_SCRIPT_ARABIC = 1098015074
    B_SCRIPT_ARMENIAN = 1098018158
    B_SCRIPT_AVESTAN = 1098281844
    B_SCRIPT_BALINESE = 1113681001
    B_SCRIPT_BAMUM = 1113681269
    B_SCRIPT_BASSA_VAH = 1113682803
    B_SCRIPT_BATAK = 1113683051
    B_SCRIPT_BENGALI = 1113943655
    B_SCRIPT_BHAIKSUKI = 1114139507
    B_SCRIPT_BOPOMOFO = 1114599535
    B_SCRIPT_BRAHMI = 1114792296
    B_SCRIPT_BRAILLE = 1114792297
    B_SCRIPT_BUGINESE = 1114990441
    B_SCRIPT_BUHID = 1114990692
    B_SCRIPT_CANADIAN_SYLLABICS = 1130458739
    B_SCRIPT_CARIAN = 1130459753
    B_SCRIPT_CAUCASIAN_ALBANIAN = 1097295970
    B_SCRIPT_CHAKMA = 1130457965
    B_SCRIPT_CHAM = 1130914157
    B_SCRIPT_CHEROKEE = 1130915186
    B_SCRIPT_CHORASMIAN = 1130918515
    B_SCRIPT_COMMON = 1517910393
    B_SCRIPT_COPTIC = 1131376756
    B_SCRIPT_CUNEIFORM = 1483961720
    B_SCRIPT_CYPRIOT = 1131442804
    B_SCRIPT_CYPRO_MINOAN = 1131441518
    B_SCRIPT_CYRILLIC = 1132032620
    B_SCRIPT_DESERET = 1148416628
    B_SCRIPT_DEVANAGARI = 1147500129
    B_SCRIPT_DIVES_AKURU = 1147756907
    B_SCRIPT_DOGRA = 1148151666
    B_SCRIPT_DUPLOYAN = 1148547180
    B_SCRIPT_EGYPTIAN_HIEROGLYPHS = 1164409200
    B_SCRIPT_ELBASAN = 1164730977
    B_SCRIPT_ELYMAIC = 1164736877
    B_SCRIPT_ETHIOPIC = 1165256809
    B_SCRIPT_GARAY = 1197568609
    B_SCRIPT_GEORGIAN = 1197830002
    B_SCRIPT_GLAGOLITIC = 1198285159
    B_SCRIPT_GOTHIC = 1198486632
    B_SCRIPT_GRANTHA = 1198678382
    B_SCRIPT_GREEK = 1198679403
    B_SCRIPT_GUJARATI = 1198877298
    B_SCRIPT_GUNJALA_GONDI = 1198485095
    B_SCRIPT_GURMUKHI = 1198879349
    B_SCRIPT_GURUNG_KHEMA = 1198877544
    B_SCRIPT_HAN = 1214344809
    B_SCRIPT_HANGUL = 1214344807
    B_SCRIPT_HANIFI_ROHINGYA = 1383032935
    B_SCRIPT_HANUNOO = 1214344815
    B_SCRIPT_HATRAN = 1214346354
    B_SCRIPT_HEBREW = 1214603890
    B_SCRIPT_HIRAGANA = 1214870113
    B_SCRIPT_IMPERIAL_ARAMAIC = 1098018153
    B_SCRIPT_INHERITED = 1516858984
    B_SCRIPT_INSCRIPTIONAL_PAHLAVI = 1349020777
    B_SCRIPT_INSCRIPTIONAL_PARTHIAN = 1349678185
    B_SCRIPT_INVALID = 0
    B_SCRIPT_JAVANESE = 1247901281
    B_SCRIPT_KAITHI = 1265920105
    B_SCRIPT_KANNADA = 1265525857
    B_SCRIPT_KATAKANA = 1264676449
    B_SCRIPT_KAWI = 1264678761
    B_SCRIPT_KAYAH_LI = 1264675945
    B_SCRIPT_KHAROSHTHI = 1265131890
    B_SCRIPT_KHITAN_SMALL_SCRIPT = 1265202291
    B_SCRIPT_KHMER = 1265134962
    B_SCRIPT_KHOJKI = 1265135466
    B_SCRIPT_KHUDAWADI = 1399418468
    B_SCRIPT_KIRAT_RAI = 1265787241
    B_SCRIPT_LAO = 1281453935
    B_SCRIPT_LATIN = 1281455214
    B_SCRIPT_LEPCHA = 1281716323
    B_SCRIPT_LIMBU = 1281977698
    B_SCRIPT_LINEAR_A = 1281977953
    B_SCRIPT_LINEAR_B = 1281977954
    B_SCRIPT_LISU = 1281979253
    B_SCRIPT_LYCIAN = 1283023721
    B_SCRIPT_LYDIAN = 1283023977
    B_SCRIPT_MAHAJANI = 1298229354
    B_SCRIPT_MAKASAR = 1298230113
    B_SCRIPT_MALAYALAM = 1298954605
    B_SCRIPT_MANDAIC = 1298230884
    B_SCRIPT_MANICHAEAN = 1298230889
    B_SCRIPT_MARCHEN = 1298231907
    B_SCRIPT_MASARAM_GONDI = 1198485101
    B_SCRIPT_MATH = 1517122664
    B_SCRIPT_MEDEFAIDRIN = 1298490470
    B_SCRIPT_MEETEI_MAYEK = 1299473769
    B_SCRIPT_MENDE_KIKAKUI = 1298493028
    B_SCRIPT_MEROITIC_CURSIVE = 1298494051
    B_SCRIPT_MEROITIC_HIEROGLYPHS = 1298494063
    B_SCRIPT_MIAO = 1349284452
    B_SCRIPT_MODI = 1299145833
    B_SCRIPT_MONGOLIAN = 1299148391
    B_SCRIPT_MRO = 1299345263
    B_SCRIPT_MULTANI = 1299541108
    B_SCRIPT_MYANMAR = 1299803506
    B_SCRIPT_NABATAEAN = 1315070324
    B_SCRIPT_NAG_MUNDARI = 1315006317
    B_SCRIPT_NANDINAGARI = 1315008100
    B_SCRIPT_NEWA = 1315272545
    B_SCRIPT_NEW_TAI_LUE = 1415670901
    B_SCRIPT_NKO = 1315663727
    B_SCRIPT_NUSHU = 1316186229
    B_SCRIPT_NYIAKENG_PUACHUE_HMONG = 1215131248
    B_SCRIPT_OGHAM = 1332175213
    B_SCRIPT_OLD_HUNGARIAN = 1215655527
    B_SCRIPT_OLD_ITALIC = 1232363884
    B_SCRIPT_OLD_NORTH_ARABIAN = 1315009122
    B_SCRIPT_OLD_PERMIC = 1348825709
    B_SCRIPT_OLD_PERSIAN = 1483761007
    B_SCRIPT_OLD_SOGDIAN = 1399809903
    B_SCRIPT_OLD_SOUTH_ARABIAN = 1398895202
    B_SCRIPT_OLD_TURKIC = 1332898664
    B_SCRIPT_OLD_UYGHUR = 1333094258
    B_SCRIPT_OL_CHIKI = 1332503403
    B_SCRIPT_OL_ONAL = 1332633967
    B_SCRIPT_ORIYA = 1332902241
    B_SCRIPT_OSAGE = 1332963173
    B_SCRIPT_OSMANYA = 1332964705
    B_SCRIPT_PAHAWH_HMONG = 1215131239
    B_SCRIPT_PALMYRENE = 1348562029
    B_SCRIPT_PAU_CIN_HAU = 1348564323
    B_SCRIPT_PHAGS_PA = 1349017959
    B_SCRIPT_PHOENICIAN = 1349021304
    B_SCRIPT_PSALTER_PAHLAVI = 1349020784
    B_SCRIPT_REJANG = 1382706791
    B_SCRIPT_RUNIC = 1383427698
    B_SCRIPT_SAMARITAN = 1398893938
    B_SCRIPT_SAURASHTRA = 1398895986
    B_SCRIPT_SHARADA = 1399353956
    B_SCRIPT_SHAVIAN = 1399349623
    B_SCRIPT_SIDDHAM = 1399415908
    B_SCRIPT_SIGNWRITING = 1399287415
    B_SCRIPT_SINHALA = 1399418472
    B_SCRIPT_SOGDIAN = 1399809892
    B_SCRIPT_SORA_SOMPENG = 1399812705
    B_SCRIPT_SOYOMBO = 1399814511
    B_SCRIPT_SUNDANESE = 1400204900
    B_SCRIPT_SUNUWAR = 1400204917
    B_SCRIPT_SYLOTI_NAGRI = 1400466543
    B_SCRIPT_SYRIAC = 1400468067
    B_SCRIPT_TAGALOG = 1416064103
    B_SCRIPT_TAGBANWA = 1415669602
    B_SCRIPT_TAI_LE = 1415670885
    B_SCRIPT_TAI_THAM = 1281453665
    B_SCRIPT_TAI_VIET = 1415673460
    B_SCRIPT_TAKRI = 1415670642
    B_SCRIPT_TAMIL = 1415671148
    B_SCRIPT_TANGSA = 1416524641
    B_SCRIPT_TANGUT = 1415671399
    B_SCRIPT_TELUGU = 1415933045
    B_SCRIPT_THAANA = 1416126817
    B_SCRIPT_THAI = 1416126825
    B_SCRIPT_TIBETAN = 1416192628
    B_SCRIPT_TIFINAGH = 1415999079
    B_SCRIPT_TIRHUTA = 1416196712
    B_SCRIPT_TODHRI = 1416586354
    B_SCRIPT_TOTO = 1416590447
    B_SCRIPT_TULU_TIGALARI = 1416983655
    B_SCRIPT_UGARITIC = 1432838514
    B_SCRIPT_UNKNOWN = 1517976186
    B_SCRIPT_VAI = 1449224553
    B_SCRIPT_VITHKUQI = 1449751656
    B_SCRIPT_WANCHO = 1466132591
    B_SCRIPT_WARANG_CITI = 1466004065
    B_SCRIPT_YEZIDI = 1499822697
    B_SCRIPT_YI = 1500080489
    B_SCRIPT_ZANABAZAR_SQUARE = 1516334690
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.HarfBuzz', '__dict__': <attribute '__dict__' of 'script_t' objects>, '__doc__': None, '__gtype__': <GType PyHarfBuzzscript_t (2667605536)>, '__flags_values__': {1517910393: <flags HB_SCRIPT_COMMON of type HarfBuzz.script_t>, 1516858984: <flags HB_SCRIPT_INHERITED of type HarfBuzz.script_t>, 1517976186: <flags HB_SCRIPT_UNKNOWN of type HarfBuzz.script_t>, 1098015074: <flags HB_SCRIPT_ARABIC of type HarfBuzz.script_t>, 1098018158: <flags HB_SCRIPT_ARABIC | HB_SCRIPT_ARMENIAN of type HarfBuzz.script_t>, 1113943655: <flags HB_SCRIPT_BENGALI of type HarfBuzz.script_t>, 1132032620: <flags HB_SCRIPT_CYRILLIC of type HarfBuzz.script_t>, 1147500129: <flags HB_SCRIPT_DEVANAGARI of type HarfBuzz.script_t>, 1197830002: <flags HB_SCRIPT_GEORGIAN of type HarfBuzz.script_t>, 1198679403: <flags HB_SCRIPT_ARABIC | HB_SCRIPT_GREEK | HB_SCRIPT_BRAILLE | HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 1198877298: <flags HB_SCRIPT_GUJARATI of type HarfBuzz.script_t>, 1198879349: <flags HB_SCRIPT_GURMUKHI | HB_SCRIPT_CYPRIOT | HB_SCRIPT_GARAY of type HarfBuzz.script_t>, 1214344807: <flags HB_SCRIPT_HANGUL of type HarfBuzz.script_t>, 1214344809: <flags HB_SCRIPT_HAN of type HarfBuzz.script_t>, 1214603890: <flags HB_SCRIPT_HEBREW of type HarfBuzz.script_t>, 1214870113: <flags HB_SCRIPT_HIRAGANA of type HarfBuzz.script_t>, 1265525857: <flags HB_SCRIPT_KANNADA of type HarfBuzz.script_t>, 1264676449: <flags HB_SCRIPT_KATAKANA of type HarfBuzz.script_t>, 1281453935: <flags HB_SCRIPT_HANGUL | HB_SCRIPT_HAN | HB_SCRIPT_LAO | HB_SCRIPT_HANUNOO | HB_SCRIPT_TAI_THAM of type HarfBuzz.script_t>, 1281455214: <flags HB_SCRIPT_LATIN of type HarfBuzz.script_t>, 1298954605: <flags HB_SCRIPT_MALAYALAM | HB_SCRIPT_ELYMAIC of type HarfBuzz.script_t>, 1332902241: <flags HB_SCRIPT_ORIYA of type HarfBuzz.script_t>, 1415671148: <flags HB_SCRIPT_TAMIL of type HarfBuzz.script_t>, 1415933045: <flags HB_SCRIPT_TELUGU | HB_SCRIPT_TAI_LE | HB_SCRIPT_NEW_TAI_LUE of type HarfBuzz.script_t>, 1416126825: <flags HB_SCRIPT_THAI | HB_SCRIPT_THAANA of type HarfBuzz.script_t>, 1416192628: <flags HB_SCRIPT_TIBETAN of type HarfBuzz.script_t>, 1114599535: <flags HB_SCRIPT_BOPOMOFO of type HarfBuzz.script_t>, 1114792297: <flags HB_SCRIPT_BRAILLE | HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 1130458739: <flags HB_SCRIPT_CANADIAN_SYLLABICS of type HarfBuzz.script_t>, 1130915186: <flags HB_SCRIPT_CHEROKEE of type HarfBuzz.script_t>, 1165256809: <flags HB_SCRIPT_ETHIOPIC of type HarfBuzz.script_t>, 1265134962: <flags HB_SCRIPT_CHEROKEE | HB_SCRIPT_KHMER | HB_SCRIPT_KHAROSHTHI of type HarfBuzz.script_t>, 1299148391: <flags HB_SCRIPT_HANGUL | HB_SCRIPT_MONGOLIAN | HB_SCRIPT_LINEAR_B | HB_SCRIPT_TAI_THAM | HB_SCRIPT_MANDAIC | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_ELBASAN | HB_SCRIPT_LINEAR_A | HB_SCRIPT_MENDE_KIKAKUI | HB_SCRIPT_PAHAWH_HMONG | HB_SCRIPT_MEDEFAIDRIN of type HarfBuzz.script_t>, 1299803506: <flags HB_SCRIPT_MYANMAR | HB_SCRIPT_LIMBU of type HarfBuzz.script_t>, 1332175213: <flags HB_SCRIPT_OGHAM of type HarfBuzz.script_t>, 1383427698: <flags HB_SCRIPT_RUNIC of type HarfBuzz.script_t>, 1399418472: <flags HB_SCRIPT_SINHALA of type HarfBuzz.script_t>, 1400468067: <flags HB_SCRIPT_SYRIAC | HB_SCRIPT_OLD_SOUTH_ARABIAN of type HarfBuzz.script_t>, 1416126817: <flags HB_SCRIPT_THAANA of type HarfBuzz.script_t>, 1500080489: <flags HB_SCRIPT_YI of type HarfBuzz.script_t>, 1148416628: <flags HB_SCRIPT_DESERET of type HarfBuzz.script_t>, 1198486632: <flags HB_SCRIPT_GOTHIC of type HarfBuzz.script_t>, 1232363884: <flags HB_SCRIPT_OLD_ITALIC of type HarfBuzz.script_t>, 1114990692: <flags HB_SCRIPT_BUHID of type HarfBuzz.script_t>, 1214344815: <flags HB_SCRIPT_HANGUL | HB_SCRIPT_HAN | HB_SCRIPT_HANUNOO of type HarfBuzz.script_t>, 1416064103: <flags HB_SCRIPT_TAGALOG | HB_SCRIPT_TAI_LE of type HarfBuzz.script_t>, 1415669602: <flags HB_SCRIPT_TAGBANWA of type HarfBuzz.script_t>, 1131442804: <flags HB_SCRIPT_CYPRIOT of type HarfBuzz.script_t>, 1281977698: <flags HB_SCRIPT_LIMBU of type HarfBuzz.script_t>, 1281977954: <flags HB_SCRIPT_LINEAR_B of type HarfBuzz.script_t>, 1332964705: <flags HB_SCRIPT_OSMANYA of type HarfBuzz.script_t>, 1399349623: <flags HB_SCRIPT_SHAVIAN | HB_SCRIPT_PHAGS_PA of type HarfBuzz.script_t>, 1415670885: <flags HB_SCRIPT_TAI_LE of type HarfBuzz.script_t>, 1432838514: <flags HB_SCRIPT_UGARITIC of type HarfBuzz.script_t>, 1114990441: <flags HB_SCRIPT_BUGINESE of type HarfBuzz.script_t>, 1131376756: <flags HB_SCRIPT_COPTIC of type HarfBuzz.script_t>, 1198285159: <flags HB_SCRIPT_GLAGOLITIC of type HarfBuzz.script_t>, 1265131890: <flags HB_SCRIPT_KHAROSHTHI of type HarfBuzz.script_t>, 1415670901: <flags HB_SCRIPT_TAI_LE | HB_SCRIPT_NEW_TAI_LUE of type HarfBuzz.script_t>, 1483761007: <flags HB_SCRIPT_OLD_PERSIAN of type HarfBuzz.script_t>, 1400466543: <flags HB_SCRIPT_SYLOTI_NAGRI | HB_SCRIPT_BALINESE | HB_SCRIPT_INSCRIPTIONAL_PAHLAVI | HB_SCRIPT_PALMYRENE | HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 1415999079: <flags HB_SCRIPT_TIFINAGH of type HarfBuzz.script_t>, 1113681001: <flags HB_SCRIPT_BALINESE of type HarfBuzz.script_t>, 1483961720: <flags HB_SCRIPT_CUNEIFORM of type HarfBuzz.script_t>, 1315663727: <flags HB_SCRIPT_HANGUL | HB_SCRIPT_HAN | HB_SCRIPT_LAO | HB_SCRIPT_HANUNOO | HB_SCRIPT_LIMBU | HB_SCRIPT_LINEAR_B | HB_SCRIPT_BALINESE | HB_SCRIPT_NKO | HB_SCRIPT_TAI_THAM | HB_SCRIPT_LINEAR_A | HB_SCRIPT_NANDINAGARI | HB_SCRIPT_DIVES_AKURU | HB_SCRIPT_NAG_MUNDARI of type HarfBuzz.script_t>, 1349017959: <flags HB_SCRIPT_PHAGS_PA of type HarfBuzz.script_t>, 1349021304: <flags HB_SCRIPT_PHOENICIAN | HB_SCRIPT_PSALTER_PAHLAVI of type HarfBuzz.script_t>, 1130459753: <flags HB_SCRIPT_CARIAN of type HarfBuzz.script_t>, 1130914157: <flags HB_SCRIPT_CHAM of type HarfBuzz.script_t>, 1264675945: <flags HB_SCRIPT_BALINESE | HB_SCRIPT_KAYAH_LI of type HarfBuzz.script_t>, 1281716323: <flags HB_SCRIPT_LEPCHA of type HarfBuzz.script_t>, 1283023721: <flags HB_SCRIPT_LYCIAN of type HarfBuzz.script_t>, 1283023977: <flags HB_SCRIPT_LYDIAN of type HarfBuzz.script_t>, 1332503403: <flags HB_SCRIPT_OL_CHIKI | HB_SCRIPT_ELBASAN of type HarfBuzz.script_t>, 1382706791: <flags HB_SCRIPT_REJANG of type HarfBuzz.script_t>, 1398895986: <flags HB_SCRIPT_SAURASHTRA of type HarfBuzz.script_t>, 1400204900: <flags HB_SCRIPT_BUHID | HB_SCRIPT_SUNDANESE of type HarfBuzz.script_t>, 1449224553: <flags HB_SCRIPT_VAI of type HarfBuzz.script_t>, 1098281844: <flags HB_SCRIPT_AVESTAN of type HarfBuzz.script_t>, 1113681269: <flags HB_SCRIPT_BAMUM of type HarfBuzz.script_t>, 1164409200: <flags HB_SCRIPT_EGYPTIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 1098018153: <flags HB_SCRIPT_IMPERIAL_ARAMAIC of type HarfBuzz.script_t>, 1349020777: <flags HB_SCRIPT_INSCRIPTIONAL_PAHLAVI of type HarfBuzz.script_t>, 1349678185: <flags HB_SCRIPT_INSCRIPTIONAL_PARTHIAN of type HarfBuzz.script_t>, 1247901281: <flags HB_SCRIPT_JAVANESE of type HarfBuzz.script_t>, 1265920105: <flags HB_SCRIPT_KAITHI of type HarfBuzz.script_t>, 1281979253: <flags HB_SCRIPT_HIRAGANA | HB_SCRIPT_LISU of type HarfBuzz.script_t>, 1299473769: <flags HB_SCRIPT_MEETEI_MAYEK of type HarfBuzz.script_t>, 1398895202: <flags HB_SCRIPT_OLD_SOUTH_ARABIAN of type HarfBuzz.script_t>, 1332898664: <flags HB_SCRIPT_OLD_TURKIC | HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 1398893938: <flags HB_SCRIPT_SAMARITAN of type HarfBuzz.script_t>, 1281453665: <flags HB_SCRIPT_TAI_THAM of type HarfBuzz.script_t>, 1415673460: <flags HB_SCRIPT_TAI_VIET of type HarfBuzz.script_t>, 1113683051: <flags HB_SCRIPT_BATAK of type HarfBuzz.script_t>, 1114792296: <flags HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 1298230884: <flags HB_SCRIPT_MANDAIC of type HarfBuzz.script_t>, 1130457965: <flags HB_SCRIPT_CHAKMA of type HarfBuzz.script_t>, 1298494051: <flags HB_SCRIPT_LEPCHA | HB_SCRIPT_MEROITIC_CURSIVE | HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 1298494063: <flags HB_SCRIPT_LEPCHA | HB_SCRIPT_MEROITIC_CURSIVE | HB_SCRIPT_MEROITIC_HIEROGLYPHS | HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 1349284452: <flags HB_SCRIPT_MIAO of type HarfBuzz.script_t>, 1399353956: <flags HB_SCRIPT_SHARADA of type HarfBuzz.script_t>, 1399812705: <flags HB_SCRIPT_SORA_SOMPENG of type HarfBuzz.script_t>, 1415670642: <flags HB_SCRIPT_TAKRI of type HarfBuzz.script_t>, 1113682803: <flags HB_SCRIPT_BASSA_VAH of type HarfBuzz.script_t>, 1097295970: <flags HB_SCRIPT_CAUCASIAN_ALBANIAN of type HarfBuzz.script_t>, 1148547180: <flags HB_SCRIPT_DUPLOYAN of type HarfBuzz.script_t>, 1164730977: <flags HB_SCRIPT_ELBASAN of type HarfBuzz.script_t>, 1198678382: <flags HB_SCRIPT_ARABIC | HB_SCRIPT_BRAHMI | HB_SCRIPT_GRANTHA of type HarfBuzz.script_t>, 1265135466: <flags HB_SCRIPT_KHOJKI of type HarfBuzz.script_t>, 1399418468: <flags HB_SCRIPT_KHUDAWADI | HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 1281977953: <flags HB_SCRIPT_TAI_THAM | HB_SCRIPT_LINEAR_A of type HarfBuzz.script_t>, 1298229354: <flags HB_SCRIPT_MAHAJANI of type HarfBuzz.script_t>, 1298230889: <flags HB_SCRIPT_HAN | HB_SCRIPT_TAI_THAM | HB_SCRIPT_MANICHAEAN of type HarfBuzz.script_t>, 1298493028: <flags HB_SCRIPT_MANDAIC | HB_SCRIPT_MENDE_KIKAKUI of type HarfBuzz.script_t>, 1299145833: <flags HB_SCRIPT_MODI of type HarfBuzz.script_t>, 1299345263: <flags HB_SCRIPT_ARABIC | HB_SCRIPT_ARMENIAN | HB_SCRIPT_IMPERIAL_ARAMAIC | HB_SCRIPT_MRO of type HarfBuzz.script_t>, 1315070324: <flags HB_SCRIPT_NABATAEAN of type HarfBuzz.script_t>, 1315009122: <flags HB_SCRIPT_OLD_NORTH_ARABIAN of type HarfBuzz.script_t>, 1348825709: <flags HB_SCRIPT_OLD_PERMIC of type HarfBuzz.script_t>, 1215131239: <flags HB_SCRIPT_HANGUL | HB_SCRIPT_PAHAWH_HMONG of type HarfBuzz.script_t>, 1348562029: <flags HB_SCRIPT_PALMYRENE of type HarfBuzz.script_t>, 1348564323: <flags HB_SCRIPT_PAU_CIN_HAU of type HarfBuzz.script_t>, 1349020784: <flags HB_SCRIPT_PSALTER_PAHLAVI of type HarfBuzz.script_t>, 1399415908: <flags HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 1416196712: <flags HB_SCRIPT_TIRHUTA of type HarfBuzz.script_t>, 1466004065: <flags HB_SCRIPT_WARANG_CITI | HB_SCRIPT_GARAY of type HarfBuzz.script_t>, 1097363309: <flags HB_SCRIPT_AHOM of type HarfBuzz.script_t>, 1215067511: <flags HB_SCRIPT_ANATOLIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 1214346354: <flags HB_SCRIPT_HATRAN of type HarfBuzz.script_t>, 1299541108: <flags HB_SCRIPT_MULTANI of type HarfBuzz.script_t>, 1215655527: <flags HB_SCRIPT_HANGUL | HB_SCRIPT_OLD_HUNGARIAN of type HarfBuzz.script_t>, 1399287415: <flags HB_SCRIPT_BENGALI | HB_SCRIPT_CANADIAN_SYLLABICS | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_SIGNWRITING of type HarfBuzz.script_t>, 1097100397: <flags HB_SCRIPT_ADLAM of type HarfBuzz.script_t>, 1114139507: <flags HB_SCRIPT_BHAIKSUKI of type HarfBuzz.script_t>, 1298231907: <flags HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 1332963173: <flags HB_SCRIPT_OSAGE of type HarfBuzz.script_t>, 1415671399: <flags HB_SCRIPT_TAI_LE | HB_SCRIPT_TANGUT of type HarfBuzz.script_t>, 1315272545: <flags HB_SCRIPT_DEVANAGARI | HB_SCRIPT_JAVANESE | HB_SCRIPT_NEWA of type HarfBuzz.script_t>, 1198485101: <flags HB_SCRIPT_BALINESE | HB_SCRIPT_ELBASAN | HB_SCRIPT_ADLAM | HB_SCRIPT_MASARAM_GONDI of type HarfBuzz.script_t>, 1316186229: <flags HB_SCRIPT_NUSHU of type HarfBuzz.script_t>, 1399814511: <flags HB_SCRIPT_BOPOMOFO | HB_SCRIPT_PHAGS_PA | HB_SCRIPT_CHAM | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_SOYOMBO | HB_SCRIPT_HANIFI_ROHINGYA of type HarfBuzz.script_t>, 1516334690: <flags HB_SCRIPT_ZANABAZAR_SQUARE of type HarfBuzz.script_t>, 1148151666: <flags HB_SCRIPT_DOGRA of type HarfBuzz.script_t>, 1198485095: <flags HB_SCRIPT_BENGALI | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_ELBASAN | HB_SCRIPT_GUNJALA_GONDI of type HarfBuzz.script_t>, 1383032935: <flags HB_SCRIPT_HANIFI_ROHINGYA of type HarfBuzz.script_t>, 1298230113: <flags HB_SCRIPT_MAKASAR of type HarfBuzz.script_t>, 1298490470: <flags HB_SCRIPT_MEDEFAIDRIN of type HarfBuzz.script_t>, 1399809903: <flags HB_SCRIPT_PHAGS_PA | HB_SCRIPT_CHAM | HB_SCRIPT_SIDDHAM | HB_SCRIPT_OLD_SOGDIAN | HB_SCRIPT_SOGDIAN of type HarfBuzz.script_t>, 1399809892: <flags HB_SCRIPT_SIDDHAM | HB_SCRIPT_SOGDIAN of type HarfBuzz.script_t>, 1164736877: <flags HB_SCRIPT_ELYMAIC of type HarfBuzz.script_t>, 1315008100: <flags HB_SCRIPT_NANDINAGARI of type HarfBuzz.script_t>, 1215131248: <flags HB_SCRIPT_NYIAKENG_PUACHUE_HMONG of type HarfBuzz.script_t>, 1466132591: <flags HB_SCRIPT_WANCHO of type HarfBuzz.script_t>, 1130918515: <flags HB_SCRIPT_CHORASMIAN of type HarfBuzz.script_t>, 1147756907: <flags HB_SCRIPT_DIVES_AKURU of type HarfBuzz.script_t>, 1265202291: <flags HB_SCRIPT_HATRAN | HB_SCRIPT_KHITAN_SMALL_SCRIPT of type HarfBuzz.script_t>, 1499822697: <flags HB_SCRIPT_YEZIDI of type HarfBuzz.script_t>, 1131441518: <flags HB_SCRIPT_CYPRO_MINOAN of type HarfBuzz.script_t>, 1333094258: <flags HB_SCRIPT_HEBREW | HB_SCRIPT_OLD_UYGHUR of type HarfBuzz.script_t>, 1416524641: <flags HB_SCRIPT_THAANA | HB_SCRIPT_TANGSA of type HarfBuzz.script_t>, 1416590447: <flags HB_SCRIPT_TOTO of type HarfBuzz.script_t>, 1449751656: <flags HB_SCRIPT_VITHKUQI of type HarfBuzz.script_t>, 1517122664: <flags HB_SCRIPT_MATH of type HarfBuzz.script_t>, 1264678761: <flags HB_SCRIPT_CARIAN | HB_SCRIPT_JAVANESE | HB_SCRIPT_KAWI of type HarfBuzz.script_t>, 1315006317: <flags HB_SCRIPT_NAG_MUNDARI of type HarfBuzz.script_t>, 1197568609: <flags HB_SCRIPT_GARAY of type HarfBuzz.script_t>, 1198877544: <flags HB_SCRIPT_GURUNG_KHEMA of type HarfBuzz.script_t>, 1265787241: <flags HB_SCRIPT_BRAILLE | HB_SCRIPT_BRAHMI | HB_SCRIPT_KIRAT_RAI of type HarfBuzz.script_t>, 1332633967: <flags HB_SCRIPT_GLAGOLITIC | HB_SCRIPT_CHAM | HB_SCRIPT_OL_ONAL of type HarfBuzz.script_t>, 1400204917: <flags HB_SCRIPT_BUHID | HB_SCRIPT_SUNDANESE | HB_SCRIPT_SUNUWAR of type HarfBuzz.script_t>, 1416586354: <flags HB_SCRIPT_TODHRI of type HarfBuzz.script_t>, 1416983655: <flags HB_SCRIPT_TULU_TIGALARI of type HarfBuzz.script_t>, 0: <flags 0 of type HarfBuzz.script_t>}, '__info__': gi.EnumInfo(script_t), 'B_SCRIPT_COMMON': <flags HB_SCRIPT_COMMON of type HarfBuzz.script_t>, 'B_SCRIPT_INHERITED': <flags HB_SCRIPT_INHERITED of type HarfBuzz.script_t>, 'B_SCRIPT_UNKNOWN': <flags HB_SCRIPT_UNKNOWN of type HarfBuzz.script_t>, 'B_SCRIPT_ARABIC': <flags HB_SCRIPT_ARABIC of type HarfBuzz.script_t>, 'B_SCRIPT_ARMENIAN': <flags HB_SCRIPT_ARABIC | HB_SCRIPT_ARMENIAN of type HarfBuzz.script_t>, 'B_SCRIPT_BENGALI': <flags HB_SCRIPT_BENGALI of type HarfBuzz.script_t>, 'B_SCRIPT_CYRILLIC': <flags HB_SCRIPT_CYRILLIC of type HarfBuzz.script_t>, 'B_SCRIPT_DEVANAGARI': <flags HB_SCRIPT_DEVANAGARI of type HarfBuzz.script_t>, 'B_SCRIPT_GEORGIAN': <flags HB_SCRIPT_GEORGIAN of type HarfBuzz.script_t>, 'B_SCRIPT_GREEK': <flags HB_SCRIPT_ARABIC | HB_SCRIPT_GREEK | HB_SCRIPT_BRAILLE | HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 'B_SCRIPT_GUJARATI': <flags HB_SCRIPT_GUJARATI of type HarfBuzz.script_t>, 'B_SCRIPT_GURMUKHI': <flags HB_SCRIPT_GURMUKHI | HB_SCRIPT_CYPRIOT | HB_SCRIPT_GARAY of type HarfBuzz.script_t>, 'B_SCRIPT_HANGUL': <flags HB_SCRIPT_HANGUL of type HarfBuzz.script_t>, 'B_SCRIPT_HAN': <flags HB_SCRIPT_HAN of type HarfBuzz.script_t>, 'B_SCRIPT_HEBREW': <flags HB_SCRIPT_HEBREW of type HarfBuzz.script_t>, 'B_SCRIPT_HIRAGANA': <flags HB_SCRIPT_HIRAGANA of type HarfBuzz.script_t>, 'B_SCRIPT_KANNADA': <flags HB_SCRIPT_KANNADA of type HarfBuzz.script_t>, 'B_SCRIPT_KATAKANA': <flags HB_SCRIPT_KATAKANA of type HarfBuzz.script_t>, 'B_SCRIPT_LAO': <flags HB_SCRIPT_HANGUL | HB_SCRIPT_HAN | HB_SCRIPT_LAO | HB_SCRIPT_HANUNOO | HB_SCRIPT_TAI_THAM of type HarfBuzz.script_t>, 'B_SCRIPT_LATIN': <flags HB_SCRIPT_LATIN of type HarfBuzz.script_t>, 'B_SCRIPT_MALAYALAM': <flags HB_SCRIPT_MALAYALAM | HB_SCRIPT_ELYMAIC of type HarfBuzz.script_t>, 'B_SCRIPT_ORIYA': <flags HB_SCRIPT_ORIYA of type HarfBuzz.script_t>, 'B_SCRIPT_TAMIL': <flags HB_SCRIPT_TAMIL of type HarfBuzz.script_t>, 'B_SCRIPT_TELUGU': <flags HB_SCRIPT_TELUGU | HB_SCRIPT_TAI_LE | HB_SCRIPT_NEW_TAI_LUE of type HarfBuzz.script_t>, 'B_SCRIPT_THAI': <flags HB_SCRIPT_THAI | HB_SCRIPT_THAANA of type HarfBuzz.script_t>, 'B_SCRIPT_TIBETAN': <flags HB_SCRIPT_TIBETAN of type HarfBuzz.script_t>, 'B_SCRIPT_BOPOMOFO': <flags HB_SCRIPT_BOPOMOFO of type HarfBuzz.script_t>, 'B_SCRIPT_BRAILLE': <flags HB_SCRIPT_BRAILLE | HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 'B_SCRIPT_CANADIAN_SYLLABICS': <flags HB_SCRIPT_CANADIAN_SYLLABICS of type HarfBuzz.script_t>, 'B_SCRIPT_CHEROKEE': <flags HB_SCRIPT_CHEROKEE of type HarfBuzz.script_t>, 'B_SCRIPT_ETHIOPIC': <flags HB_SCRIPT_ETHIOPIC of type HarfBuzz.script_t>, 'B_SCRIPT_KHMER': <flags HB_SCRIPT_CHEROKEE | HB_SCRIPT_KHMER | HB_SCRIPT_KHAROSHTHI of type HarfBuzz.script_t>, 'B_SCRIPT_MONGOLIAN': <flags HB_SCRIPT_HANGUL | HB_SCRIPT_MONGOLIAN | HB_SCRIPT_LINEAR_B | HB_SCRIPT_TAI_THAM | HB_SCRIPT_MANDAIC | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_ELBASAN | HB_SCRIPT_LINEAR_A | HB_SCRIPT_MENDE_KIKAKUI | HB_SCRIPT_PAHAWH_HMONG | HB_SCRIPT_MEDEFAIDRIN of type HarfBuzz.script_t>, 'B_SCRIPT_MYANMAR': <flags HB_SCRIPT_MYANMAR | HB_SCRIPT_LIMBU of type HarfBuzz.script_t>, 'B_SCRIPT_OGHAM': <flags HB_SCRIPT_OGHAM of type HarfBuzz.script_t>, 'B_SCRIPT_RUNIC': <flags HB_SCRIPT_RUNIC of type HarfBuzz.script_t>, 'B_SCRIPT_SINHALA': <flags HB_SCRIPT_SINHALA of type HarfBuzz.script_t>, 'B_SCRIPT_SYRIAC': <flags HB_SCRIPT_SYRIAC | HB_SCRIPT_OLD_SOUTH_ARABIAN of type HarfBuzz.script_t>, 'B_SCRIPT_THAANA': <flags HB_SCRIPT_THAANA of type HarfBuzz.script_t>, 'B_SCRIPT_YI': <flags HB_SCRIPT_YI of type HarfBuzz.script_t>, 'B_SCRIPT_DESERET': <flags HB_SCRIPT_DESERET of type HarfBuzz.script_t>, 'B_SCRIPT_GOTHIC': <flags HB_SCRIPT_GOTHIC of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_ITALIC': <flags HB_SCRIPT_OLD_ITALIC of type HarfBuzz.script_t>, 'B_SCRIPT_BUHID': <flags HB_SCRIPT_BUHID of type HarfBuzz.script_t>, 'B_SCRIPT_HANUNOO': <flags HB_SCRIPT_HANGUL | HB_SCRIPT_HAN | HB_SCRIPT_HANUNOO of type HarfBuzz.script_t>, 'B_SCRIPT_TAGALOG': <flags HB_SCRIPT_TAGALOG | HB_SCRIPT_TAI_LE of type HarfBuzz.script_t>, 'B_SCRIPT_TAGBANWA': <flags HB_SCRIPT_TAGBANWA of type HarfBuzz.script_t>, 'B_SCRIPT_CYPRIOT': <flags HB_SCRIPT_CYPRIOT of type HarfBuzz.script_t>, 'B_SCRIPT_LIMBU': <flags HB_SCRIPT_LIMBU of type HarfBuzz.script_t>, 'B_SCRIPT_LINEAR_B': <flags HB_SCRIPT_LINEAR_B of type HarfBuzz.script_t>, 'B_SCRIPT_OSMANYA': <flags HB_SCRIPT_OSMANYA of type HarfBuzz.script_t>, 'B_SCRIPT_SHAVIAN': <flags HB_SCRIPT_SHAVIAN | HB_SCRIPT_PHAGS_PA of type HarfBuzz.script_t>, 'B_SCRIPT_TAI_LE': <flags HB_SCRIPT_TAI_LE of type HarfBuzz.script_t>, 'B_SCRIPT_UGARITIC': <flags HB_SCRIPT_UGARITIC of type HarfBuzz.script_t>, 'B_SCRIPT_BUGINESE': <flags HB_SCRIPT_BUGINESE of type HarfBuzz.script_t>, 'B_SCRIPT_COPTIC': <flags HB_SCRIPT_COPTIC of type HarfBuzz.script_t>, 'B_SCRIPT_GLAGOLITIC': <flags HB_SCRIPT_GLAGOLITIC of type HarfBuzz.script_t>, 'B_SCRIPT_KHAROSHTHI': <flags HB_SCRIPT_KHAROSHTHI of type HarfBuzz.script_t>, 'B_SCRIPT_NEW_TAI_LUE': <flags HB_SCRIPT_TAI_LE | HB_SCRIPT_NEW_TAI_LUE of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_PERSIAN': <flags HB_SCRIPT_OLD_PERSIAN of type HarfBuzz.script_t>, 'B_SCRIPT_SYLOTI_NAGRI': <flags HB_SCRIPT_SYLOTI_NAGRI | HB_SCRIPT_BALINESE | HB_SCRIPT_INSCRIPTIONAL_PAHLAVI | HB_SCRIPT_PALMYRENE | HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 'B_SCRIPT_TIFINAGH': <flags HB_SCRIPT_TIFINAGH of type HarfBuzz.script_t>, 'B_SCRIPT_BALINESE': <flags HB_SCRIPT_BALINESE of type HarfBuzz.script_t>, 'B_SCRIPT_CUNEIFORM': <flags HB_SCRIPT_CUNEIFORM of type HarfBuzz.script_t>, 'B_SCRIPT_NKO': <flags HB_SCRIPT_HANGUL | HB_SCRIPT_HAN | HB_SCRIPT_LAO | HB_SCRIPT_HANUNOO | HB_SCRIPT_LIMBU | HB_SCRIPT_LINEAR_B | HB_SCRIPT_BALINESE | HB_SCRIPT_NKO | HB_SCRIPT_TAI_THAM | HB_SCRIPT_LINEAR_A | HB_SCRIPT_NANDINAGARI | HB_SCRIPT_DIVES_AKURU | HB_SCRIPT_NAG_MUNDARI of type HarfBuzz.script_t>, 'B_SCRIPT_PHAGS_PA': <flags HB_SCRIPT_PHAGS_PA of type HarfBuzz.script_t>, 'B_SCRIPT_PHOENICIAN': <flags HB_SCRIPT_PHOENICIAN | HB_SCRIPT_PSALTER_PAHLAVI of type HarfBuzz.script_t>, 'B_SCRIPT_CARIAN': <flags HB_SCRIPT_CARIAN of type HarfBuzz.script_t>, 'B_SCRIPT_CHAM': <flags HB_SCRIPT_CHAM of type HarfBuzz.script_t>, 'B_SCRIPT_KAYAH_LI': <flags HB_SCRIPT_BALINESE | HB_SCRIPT_KAYAH_LI of type HarfBuzz.script_t>, 'B_SCRIPT_LEPCHA': <flags HB_SCRIPT_LEPCHA of type HarfBuzz.script_t>, 'B_SCRIPT_LYCIAN': <flags HB_SCRIPT_LYCIAN of type HarfBuzz.script_t>, 'B_SCRIPT_LYDIAN': <flags HB_SCRIPT_LYDIAN of type HarfBuzz.script_t>, 'B_SCRIPT_OL_CHIKI': <flags HB_SCRIPT_OL_CHIKI | HB_SCRIPT_ELBASAN of type HarfBuzz.script_t>, 'B_SCRIPT_REJANG': <flags HB_SCRIPT_REJANG of type HarfBuzz.script_t>, 'B_SCRIPT_SAURASHTRA': <flags HB_SCRIPT_SAURASHTRA of type HarfBuzz.script_t>, 'B_SCRIPT_SUNDANESE': <flags HB_SCRIPT_BUHID | HB_SCRIPT_SUNDANESE of type HarfBuzz.script_t>, 'B_SCRIPT_VAI': <flags HB_SCRIPT_VAI of type HarfBuzz.script_t>, 'B_SCRIPT_AVESTAN': <flags HB_SCRIPT_AVESTAN of type HarfBuzz.script_t>, 'B_SCRIPT_BAMUM': <flags HB_SCRIPT_BAMUM of type HarfBuzz.script_t>, 'B_SCRIPT_EGYPTIAN_HIEROGLYPHS': <flags HB_SCRIPT_EGYPTIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 'B_SCRIPT_IMPERIAL_ARAMAIC': <flags HB_SCRIPT_IMPERIAL_ARAMAIC of type HarfBuzz.script_t>, 'B_SCRIPT_INSCRIPTIONAL_PAHLAVI': <flags HB_SCRIPT_INSCRIPTIONAL_PAHLAVI of type HarfBuzz.script_t>, 'B_SCRIPT_INSCRIPTIONAL_PARTHIAN': <flags HB_SCRIPT_INSCRIPTIONAL_PARTHIAN of type HarfBuzz.script_t>, 'B_SCRIPT_JAVANESE': <flags HB_SCRIPT_JAVANESE of type HarfBuzz.script_t>, 'B_SCRIPT_KAITHI': <flags HB_SCRIPT_KAITHI of type HarfBuzz.script_t>, 'B_SCRIPT_LISU': <flags HB_SCRIPT_HIRAGANA | HB_SCRIPT_LISU of type HarfBuzz.script_t>, 'B_SCRIPT_MEETEI_MAYEK': <flags HB_SCRIPT_MEETEI_MAYEK of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_SOUTH_ARABIAN': <flags HB_SCRIPT_OLD_SOUTH_ARABIAN of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_TURKIC': <flags HB_SCRIPT_OLD_TURKIC | HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 'B_SCRIPT_SAMARITAN': <flags HB_SCRIPT_SAMARITAN of type HarfBuzz.script_t>, 'B_SCRIPT_TAI_THAM': <flags HB_SCRIPT_TAI_THAM of type HarfBuzz.script_t>, 'B_SCRIPT_TAI_VIET': <flags HB_SCRIPT_TAI_VIET of type HarfBuzz.script_t>, 'B_SCRIPT_BATAK': <flags HB_SCRIPT_BATAK of type HarfBuzz.script_t>, 'B_SCRIPT_BRAHMI': <flags HB_SCRIPT_BRAHMI of type HarfBuzz.script_t>, 'B_SCRIPT_MANDAIC': <flags HB_SCRIPT_MANDAIC of type HarfBuzz.script_t>, 'B_SCRIPT_CHAKMA': <flags HB_SCRIPT_CHAKMA of type HarfBuzz.script_t>, 'B_SCRIPT_MEROITIC_CURSIVE': <flags HB_SCRIPT_LEPCHA | HB_SCRIPT_MEROITIC_CURSIVE | HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 'B_SCRIPT_MEROITIC_HIEROGLYPHS': <flags HB_SCRIPT_LEPCHA | HB_SCRIPT_MEROITIC_CURSIVE | HB_SCRIPT_MEROITIC_HIEROGLYPHS | HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 'B_SCRIPT_MIAO': <flags HB_SCRIPT_MIAO of type HarfBuzz.script_t>, 'B_SCRIPT_SHARADA': <flags HB_SCRIPT_SHARADA of type HarfBuzz.script_t>, 'B_SCRIPT_SORA_SOMPENG': <flags HB_SCRIPT_SORA_SOMPENG of type HarfBuzz.script_t>, 'B_SCRIPT_TAKRI': <flags HB_SCRIPT_TAKRI of type HarfBuzz.script_t>, 'B_SCRIPT_BASSA_VAH': <flags HB_SCRIPT_BASSA_VAH of type HarfBuzz.script_t>, 'B_SCRIPT_CAUCASIAN_ALBANIAN': <flags HB_SCRIPT_CAUCASIAN_ALBANIAN of type HarfBuzz.script_t>, 'B_SCRIPT_DUPLOYAN': <flags HB_SCRIPT_DUPLOYAN of type HarfBuzz.script_t>, 'B_SCRIPT_ELBASAN': <flags HB_SCRIPT_ELBASAN of type HarfBuzz.script_t>, 'B_SCRIPT_GRANTHA': <flags HB_SCRIPT_ARABIC | HB_SCRIPT_BRAHMI | HB_SCRIPT_GRANTHA of type HarfBuzz.script_t>, 'B_SCRIPT_KHOJKI': <flags HB_SCRIPT_KHOJKI of type HarfBuzz.script_t>, 'B_SCRIPT_KHUDAWADI': <flags HB_SCRIPT_KHUDAWADI | HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 'B_SCRIPT_LINEAR_A': <flags HB_SCRIPT_TAI_THAM | HB_SCRIPT_LINEAR_A of type HarfBuzz.script_t>, 'B_SCRIPT_MAHAJANI': <flags HB_SCRIPT_MAHAJANI of type HarfBuzz.script_t>, 'B_SCRIPT_MANICHAEAN': <flags HB_SCRIPT_HAN | HB_SCRIPT_TAI_THAM | HB_SCRIPT_MANICHAEAN of type HarfBuzz.script_t>, 'B_SCRIPT_MENDE_KIKAKUI': <flags HB_SCRIPT_MANDAIC | HB_SCRIPT_MENDE_KIKAKUI of type HarfBuzz.script_t>, 'B_SCRIPT_MODI': <flags HB_SCRIPT_MODI of type HarfBuzz.script_t>, 'B_SCRIPT_MRO': <flags HB_SCRIPT_ARABIC | HB_SCRIPT_ARMENIAN | HB_SCRIPT_IMPERIAL_ARAMAIC | HB_SCRIPT_MRO of type HarfBuzz.script_t>, 'B_SCRIPT_NABATAEAN': <flags HB_SCRIPT_NABATAEAN of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_NORTH_ARABIAN': <flags HB_SCRIPT_OLD_NORTH_ARABIAN of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_PERMIC': <flags HB_SCRIPT_OLD_PERMIC of type HarfBuzz.script_t>, 'B_SCRIPT_PAHAWH_HMONG': <flags HB_SCRIPT_HANGUL | HB_SCRIPT_PAHAWH_HMONG of type HarfBuzz.script_t>, 'B_SCRIPT_PALMYRENE': <flags HB_SCRIPT_PALMYRENE of type HarfBuzz.script_t>, 'B_SCRIPT_PAU_CIN_HAU': <flags HB_SCRIPT_PAU_CIN_HAU of type HarfBuzz.script_t>, 'B_SCRIPT_PSALTER_PAHLAVI': <flags HB_SCRIPT_PSALTER_PAHLAVI of type HarfBuzz.script_t>, 'B_SCRIPT_SIDDHAM': <flags HB_SCRIPT_SIDDHAM of type HarfBuzz.script_t>, 'B_SCRIPT_TIRHUTA': <flags HB_SCRIPT_TIRHUTA of type HarfBuzz.script_t>, 'B_SCRIPT_WARANG_CITI': <flags HB_SCRIPT_WARANG_CITI | HB_SCRIPT_GARAY of type HarfBuzz.script_t>, 'B_SCRIPT_AHOM': <flags HB_SCRIPT_AHOM of type HarfBuzz.script_t>, 'B_SCRIPT_ANATOLIAN_HIEROGLYPHS': <flags HB_SCRIPT_ANATOLIAN_HIEROGLYPHS of type HarfBuzz.script_t>, 'B_SCRIPT_HATRAN': <flags HB_SCRIPT_HATRAN of type HarfBuzz.script_t>, 'B_SCRIPT_MULTANI': <flags HB_SCRIPT_MULTANI of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_HUNGARIAN': <flags HB_SCRIPT_HANGUL | HB_SCRIPT_OLD_HUNGARIAN of type HarfBuzz.script_t>, 'B_SCRIPT_SIGNWRITING': <flags HB_SCRIPT_BENGALI | HB_SCRIPT_CANADIAN_SYLLABICS | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_SIGNWRITING of type HarfBuzz.script_t>, 'B_SCRIPT_ADLAM': <flags HB_SCRIPT_ADLAM of type HarfBuzz.script_t>, 'B_SCRIPT_BHAIKSUKI': <flags HB_SCRIPT_BHAIKSUKI of type HarfBuzz.script_t>, 'B_SCRIPT_MARCHEN': <flags HB_SCRIPT_MARCHEN of type HarfBuzz.script_t>, 'B_SCRIPT_OSAGE': <flags HB_SCRIPT_OSAGE of type HarfBuzz.script_t>, 'B_SCRIPT_TANGUT': <flags HB_SCRIPT_TAI_LE | HB_SCRIPT_TANGUT of type HarfBuzz.script_t>, 'B_SCRIPT_NEWA': <flags HB_SCRIPT_DEVANAGARI | HB_SCRIPT_JAVANESE | HB_SCRIPT_NEWA of type HarfBuzz.script_t>, 'B_SCRIPT_MASARAM_GONDI': <flags HB_SCRIPT_BALINESE | HB_SCRIPT_ELBASAN | HB_SCRIPT_ADLAM | HB_SCRIPT_MASARAM_GONDI of type HarfBuzz.script_t>, 'B_SCRIPT_NUSHU': <flags HB_SCRIPT_NUSHU of type HarfBuzz.script_t>, 'B_SCRIPT_SOYOMBO': <flags HB_SCRIPT_BOPOMOFO | HB_SCRIPT_PHAGS_PA | HB_SCRIPT_CHAM | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_SOYOMBO | HB_SCRIPT_HANIFI_ROHINGYA of type HarfBuzz.script_t>, 'B_SCRIPT_ZANABAZAR_SQUARE': <flags HB_SCRIPT_ZANABAZAR_SQUARE of type HarfBuzz.script_t>, 'B_SCRIPT_DOGRA': <flags HB_SCRIPT_DOGRA of type HarfBuzz.script_t>, 'B_SCRIPT_GUNJALA_GONDI': <flags HB_SCRIPT_BENGALI | HB_SCRIPT_CAUCASIAN_ALBANIAN | HB_SCRIPT_ELBASAN | HB_SCRIPT_GUNJALA_GONDI of type HarfBuzz.script_t>, 'B_SCRIPT_HANIFI_ROHINGYA': <flags HB_SCRIPT_HANIFI_ROHINGYA of type HarfBuzz.script_t>, 'B_SCRIPT_MAKASAR': <flags HB_SCRIPT_MAKASAR of type HarfBuzz.script_t>, 'B_SCRIPT_MEDEFAIDRIN': <flags HB_SCRIPT_MEDEFAIDRIN of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_SOGDIAN': <flags HB_SCRIPT_PHAGS_PA | HB_SCRIPT_CHAM | HB_SCRIPT_SIDDHAM | HB_SCRIPT_OLD_SOGDIAN | HB_SCRIPT_SOGDIAN of type HarfBuzz.script_t>, 'B_SCRIPT_SOGDIAN': <flags HB_SCRIPT_SIDDHAM | HB_SCRIPT_SOGDIAN of type HarfBuzz.script_t>, 'B_SCRIPT_ELYMAIC': <flags HB_SCRIPT_ELYMAIC of type HarfBuzz.script_t>, 'B_SCRIPT_NANDINAGARI': <flags HB_SCRIPT_NANDINAGARI of type HarfBuzz.script_t>, 'B_SCRIPT_NYIAKENG_PUACHUE_HMONG': <flags HB_SCRIPT_NYIAKENG_PUACHUE_HMONG of type HarfBuzz.script_t>, 'B_SCRIPT_WANCHO': <flags HB_SCRIPT_WANCHO of type HarfBuzz.script_t>, 'B_SCRIPT_CHORASMIAN': <flags HB_SCRIPT_CHORASMIAN of type HarfBuzz.script_t>, 'B_SCRIPT_DIVES_AKURU': <flags HB_SCRIPT_DIVES_AKURU of type HarfBuzz.script_t>, 'B_SCRIPT_KHITAN_SMALL_SCRIPT': <flags HB_SCRIPT_HATRAN | HB_SCRIPT_KHITAN_SMALL_SCRIPT of type HarfBuzz.script_t>, 'B_SCRIPT_YEZIDI': <flags HB_SCRIPT_YEZIDI of type HarfBuzz.script_t>, 'B_SCRIPT_CYPRO_MINOAN': <flags HB_SCRIPT_CYPRO_MINOAN of type HarfBuzz.script_t>, 'B_SCRIPT_OLD_UYGHUR': <flags HB_SCRIPT_HEBREW | HB_SCRIPT_OLD_UYGHUR of type HarfBuzz.script_t>, 'B_SCRIPT_TANGSA': <flags HB_SCRIPT_THAANA | HB_SCRIPT_TANGSA of type HarfBuzz.script_t>, 'B_SCRIPT_TOTO': <flags HB_SCRIPT_TOTO of type HarfBuzz.script_t>, 'B_SCRIPT_VITHKUQI': <flags HB_SCRIPT_VITHKUQI of type HarfBuzz.script_t>, 'B_SCRIPT_MATH': <flags HB_SCRIPT_MATH of type HarfBuzz.script_t>, 'B_SCRIPT_KAWI': <flags HB_SCRIPT_CARIAN | HB_SCRIPT_JAVANESE | HB_SCRIPT_KAWI of type HarfBuzz.script_t>, 'B_SCRIPT_NAG_MUNDARI': <flags HB_SCRIPT_NAG_MUNDARI of type HarfBuzz.script_t>, 'B_SCRIPT_GARAY': <flags HB_SCRIPT_GARAY of type HarfBuzz.script_t>, 'B_SCRIPT_GURUNG_KHEMA': <flags HB_SCRIPT_GURUNG_KHEMA of type HarfBuzz.script_t>, 'B_SCRIPT_KIRAT_RAI': <flags HB_SCRIPT_BRAILLE | HB_SCRIPT_BRAHMI | HB_SCRIPT_KIRAT_RAI of type HarfBuzz.script_t>, 'B_SCRIPT_OL_ONAL': <flags HB_SCRIPT_GLAGOLITIC | HB_SCRIPT_CHAM | HB_SCRIPT_OL_ONAL of type HarfBuzz.script_t>, 'B_SCRIPT_SUNUWAR': <flags HB_SCRIPT_BUHID | HB_SCRIPT_SUNDANESE | HB_SCRIPT_SUNUWAR of type HarfBuzz.script_t>, 'B_SCRIPT_TODHRI': <flags HB_SCRIPT_TODHRI of type HarfBuzz.script_t>, 'B_SCRIPT_TULU_TIGALARI': <flags HB_SCRIPT_TULU_TIGALARI of type HarfBuzz.script_t>, 'B_SCRIPT_INVALID': <flags 0 of type HarfBuzz.script_t>})"
    __flags_values__ = {
        0: 0,
        1097100397: 1097100397,
        1097295970: 1097295970,
        1097363309: 1097363309,
        1098015074: 1098015074,
        1098018153: 1098018153,
        1098018158: 1098018158,
        1098281844: 1098281844,
        1113681001: 1113681001,
        1113681269: 1113681269,
        1113682803: 1113682803,
        1113683051: 1113683051,
        1113943655: 1113943655,
        1114139507: 1114139507,
        1114599535: 1114599535,
        1114792296: 1114792296,
        1114792297: 1114792297,
        1114990441: 1114990441,
        1114990692: 1114990692,
        1130457965: 1130457965,
        1130458739: 1130458739,
        1130459753: 1130459753,
        1130914157: 1130914157,
        1130915186: 1130915186,
        1130918515: 1130918515,
        1131376756: 1131376756,
        1131441518: 1131441518,
        1131442804: 1131442804,
        1132032620: 1132032620,
        1147500129: 1147500129,
        1147756907: 1147756907,
        1148151666: 1148151666,
        1148416628: 1148416628,
        1148547180: 1148547180,
        1164409200: 1164409200,
        1164730977: 1164730977,
        1164736877: 1164736877,
        1165256809: 1165256809,
        1197568609: 1197568609,
        1197830002: 1197830002,
        1198285159: 1198285159,
        1198485095: 1198485095,
        1198485101: 1198485101,
        1198486632: 1198486632,
        1198678382: 1198678382,
        1198679403: 1198679403,
        1198877298: 1198877298,
        1198877544: 1198877544,
        1198879349: 1198879349,
        1214344807: 1214344807,
        1214344809: 1214344809,
        1214344815: 1214344815,
        1214346354: 1214346354,
        1214603890: 1214603890,
        1214870113: 1214870113,
        1215067511: 1215067511,
        1215131239: 1215131239,
        1215131248: 1215131248,
        1215655527: 1215655527,
        1232363884: 1232363884,
        1247901281: 1247901281,
        1264675945: 1264675945,
        1264676449: 1264676449,
        1264678761: 1264678761,
        1265131890: 1265131890,
        1265134962: 1265134962,
        1265135466: 1265135466,
        1265202291: 1265202291,
        1265525857: 1265525857,
        1265787241: 1265787241,
        1265920105: 1265920105,
        1281453665: 1281453665,
        1281453935: 1281453935,
        1281455214: 1281455214,
        1281716323: 1281716323,
        1281977698: 1281977698,
        1281977953: 1281977953,
        1281977954: 1281977954,
        1281979253: 1281979253,
        1283023721: 1283023721,
        1283023977: 1283023977,
        1298229354: 1298229354,
        1298230113: 1298230113,
        1298230884: 1298230884,
        1298230889: 1298230889,
        1298231907: 1298231907,
        1298490470: 1298490470,
        1298493028: 1298493028,
        1298494051: 1298494051,
        1298494063: 1298494063,
        1298954605: 1298954605,
        1299145833: 1299145833,
        1299148391: 1299148391,
        1299345263: 1299345263,
        1299473769: 1299473769,
        1299541108: 1299541108,
        1299803506: 1299803506,
        1315006317: 1315006317,
        1315008100: 1315008100,
        1315009122: 1315009122,
        1315070324: 1315070324,
        1315272545: 1315272545,
        1315663727: 1315663727,
        1316186229: 1316186229,
        1332175213: 1332175213,
        1332503403: 1332503403,
        1332633967: 1332633967,
        1332898664: 1332898664,
        1332902241: 1332902241,
        1332963173: 1332963173,
        1332964705: 1332964705,
        1333094258: 1333094258,
        1348562029: 1348562029,
        1348564323: 1348564323,
        1348825709: 1348825709,
        1349017959: 1349017959,
        1349020777: 1349020777,
        1349020784: 1349020784,
        1349021304: 1349021304,
        1349284452: 1349284452,
        1349678185: 1349678185,
        1382706791: 1382706791,
        1383032935: 1383032935,
        1383427698: 1383427698,
        1398893938: 1398893938,
        1398895202: 1398895202,
        1398895986: 1398895986,
        1399287415: 1399287415,
        1399349623: 1399349623,
        1399353956: 1399353956,
        1399415908: 1399415908,
        1399418468: 1399418468,
        1399418472: 1399418472,
        1399809892: 1399809892,
        1399809903: 1399809903,
        1399812705: 1399812705,
        1399814511: 1399814511,
        1400204900: 1400204900,
        1400204917: 1400204917,
        1400466543: 1400466543,
        1400468067: 1400468067,
        1415669602: 1415669602,
        1415670642: 1415670642,
        1415670885: 1415670885,
        1415670901: 1415670901,
        1415671148: 1415671148,
        1415671399: 1415671399,
        1415673460: 1415673460,
        1415933045: 1415933045,
        1415999079: 1415999079,
        1416064103: 1416064103,
        1416126817: 1416126817,
        1416126825: 1416126825,
        1416192628: 1416192628,
        1416196712: 1416196712,
        1416524641: 1416524641,
        1416586354: 1416586354,
        1416590447: 1416590447,
        1416983655: 1416983655,
        1432838514: 1432838514,
        1449224553: 1449224553,
        1449751656: 1449751656,
        1466004065: 1466004065,
        1466132591: 1466132591,
        1483761007: 1483761007,
        1483961720: 1483961720,
        1499822697: 1499822697,
        1500080489: 1500080489,
        1516334690: 1516334690,
        1516858984: 1516858984,
        1517122664: 1517122664,
        1517910393: 1517910393,
        1517976186: 1517976186,
    }
    __gtype__ = None # (!) real value is '<GType PyHarfBuzzscript_t (2667605536)>'
    __info__ = gi.EnumInfo(script_t)


