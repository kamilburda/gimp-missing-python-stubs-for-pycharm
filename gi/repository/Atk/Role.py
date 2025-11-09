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


class Role(__gobject.GEnum):
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
        """ for_name(name:str) -> Atk.Role """
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

    def get_localized_name(self, role): # real signature unknown; restored from __doc__
        """ get_localized_name(role:Atk.Role) -> str """
        return ""

    def get_name(self, role): # real signature unknown; restored from __doc__
        """ get_name(role:Atk.Role) -> str """
        return ""

    def is_integer(self, *args, **kwargs): # real signature unknown
        """ Returns True. Exists for duck type compatibility with float.is_integer. """
        pass

    def register(self, name): # real signature unknown; restored from __doc__
        """ register(name:str) -> Atk.Role """
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


    ACCELERATOR_LABEL = 1
    ALERT = 2
    ANIMATION = 3
    APPLICATION = 73
    ARROW = 4
    ARTICLE = 107
    AUDIO = 104
    AUTOCOMPLETE = 74
    BLOCK_QUOTE = 103
    BUTTON = 42
    CALENDAR = 5
    CANVAS = 6
    CAPTION = 79
    CHART = 78
    CHECK_BOX = 7
    CHECK_MENU_ITEM = 8
    COLOR_CHOOSER = 9
    COLUMN_HEADER = 10
    COMBO_BOX = 11
    COMMENT = 95
    CONTENT_DELETION = 123
    CONTENT_INSERTION = 124
    DATE_EDITOR = 12
    DEFINITION = 106
    DESCRIPTION_LIST = 114
    DESCRIPTION_TERM = 115
    DESCRIPTION_VALUE = 116
    DESKTOP_FRAME = 14
    DESKTOP_ICON = 13
    DIAL = 15
    DIALOG = 16
    DIRECTORY_PANE = 17
    DOCUMENT_EMAIL = 94
    DOCUMENT_FRAME = 80
    DOCUMENT_PRESENTATION = 91
    DOCUMENT_SPREADSHEET = 90
    DOCUMENT_TEXT = 92
    DOCUMENT_WEB = 93
    DRAWING_AREA = 18
    EDIT_BAR = 75
    EMBEDDED = 76
    ENTRY = 77
    FILE_CHOOSER = 19
    FILLER = 20
    FONT_CHOOSER = 21
    FOOTER = 70
    FOOTNOTE = 122
    FORM = 85
    FRAME = 22
    GLASS_PANE = 23
    GROUPING = 97
    HEADER = 69
    HEADING = 81
    HTML_CONTAINER = 24
    ICON = 25
    IMAGE = 26
    IMAGE_MAP = 98
    INFO_BAR = 100
    INPUT_METHOD_WINDOW = 87
    INTERNAL_FRAME = 27
    INVALID = 0
    LABEL = 28
    LANDMARK = 108
    LAST_DEFINED = 128
    LAYERED_PANE = 29
    LEVEL_BAR = 101
    LINK = 86
    LIST = 30
    LIST_BOX = 96
    LIST_ITEM = 31
    LOG = 109
    MARK = 125
    MARQUEE = 110
    MATH = 111
    MATH_FRACTION = 118
    MATH_ROOT = 119
    MENU = 32
    MENU_BAR = 33
    MENU_ITEM = 34
    NOTIFICATION = 99
    OPTION_PANE = 35
    PAGE = 82
    PAGE_TAB = 36
    PAGE_TAB_LIST = 37
    PANEL = 38
    PARAGRAPH = 71
    PASSWORD_TEXT = 39
    POPUP_MENU = 40
    PROGRESS_BAR = 41
    PUSH_BUTTON = 42
    PUSH_BUTTON_MENU = 127
    RADIO_BUTTON = 43
    RADIO_MENU_ITEM = 44
    RATING = 112
    REDUNDANT_OBJECT = 84
    ROOT_PANE = 45
    ROW_HEADER = 46
    RULER = 72
    SCROLL_BAR = 47
    SCROLL_PANE = 48
    SECTION = 83
    SEPARATOR = 49
    SLIDER = 50
    SPIN_BUTTON = 52
    SPLIT_PANE = 51
    STATIC = 117
    STATUSBAR = 53
    SUBSCRIPT = 120
    SUGGESTION = 126
    SUPERSCRIPT = 121
    TABLE = 54
    TABLE_CELL = 55
    TABLE_COLUMN_HEADER = 56
    TABLE_ROW = 88
    TABLE_ROW_HEADER = 57
    TEAR_OFF_MENU_ITEM = 58
    TERMINAL = 59
    TEXT = 60
    TIMER = 113
    TITLE_BAR = 102
    TOGGLE_BUTTON = 61
    TOOL_BAR = 62
    TOOL_TIP = 63
    TREE = 64
    TREE_ITEM = 89
    TREE_TABLE = 65
    UNKNOWN = 66
    VIDEO = 105
    VIEWPORT = 67
    WINDOW = 68
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Atk', '__dict__': <attribute '__dict__' of 'Role' objects>, '__doc__': None, '__gtype__': <GType AtkRole (892679184)>, '__enum_values__': {0: <enum ATK_ROLE_INVALID of type Atk.Role>, 1: <enum ATK_ROLE_ACCEL_LABEL of type Atk.Role>, 2: <enum ATK_ROLE_ALERT of type Atk.Role>, 3: <enum ATK_ROLE_ANIMATION of type Atk.Role>, 4: <enum ATK_ROLE_ARROW of type Atk.Role>, 5: <enum ATK_ROLE_CALENDAR of type Atk.Role>, 6: <enum ATK_ROLE_CANVAS of type Atk.Role>, 7: <enum ATK_ROLE_CHECK_BOX of type Atk.Role>, 8: <enum ATK_ROLE_CHECK_MENU_ITEM of type Atk.Role>, 9: <enum ATK_ROLE_COLOR_CHOOSER of type Atk.Role>, 10: <enum ATK_ROLE_COLUMN_HEADER of type Atk.Role>, 11: <enum ATK_ROLE_COMBO_BOX of type Atk.Role>, 12: <enum ATK_ROLE_DATE_EDITOR of type Atk.Role>, 13: <enum ATK_ROLE_DESKTOP_ICON of type Atk.Role>, 14: <enum ATK_ROLE_DESKTOP_FRAME of type Atk.Role>, 15: <enum ATK_ROLE_DIAL of type Atk.Role>, 16: <enum ATK_ROLE_DIALOG of type Atk.Role>, 17: <enum ATK_ROLE_DIRECTORY_PANE of type Atk.Role>, 18: <enum ATK_ROLE_DRAWING_AREA of type Atk.Role>, 19: <enum ATK_ROLE_FILE_CHOOSER of type Atk.Role>, 20: <enum ATK_ROLE_FILLER of type Atk.Role>, 21: <enum ATK_ROLE_FONT_CHOOSER of type Atk.Role>, 22: <enum ATK_ROLE_FRAME of type Atk.Role>, 23: <enum ATK_ROLE_GLASS_PANE of type Atk.Role>, 24: <enum ATK_ROLE_HTML_CONTAINER of type Atk.Role>, 25: <enum ATK_ROLE_ICON of type Atk.Role>, 26: <enum ATK_ROLE_IMAGE of type Atk.Role>, 27: <enum ATK_ROLE_INTERNAL_FRAME of type Atk.Role>, 28: <enum ATK_ROLE_LABEL of type Atk.Role>, 29: <enum ATK_ROLE_LAYERED_PANE of type Atk.Role>, 30: <enum ATK_ROLE_LIST of type Atk.Role>, 31: <enum ATK_ROLE_LIST_ITEM of type Atk.Role>, 32: <enum ATK_ROLE_MENU of type Atk.Role>, 33: <enum ATK_ROLE_MENU_BAR of type Atk.Role>, 34: <enum ATK_ROLE_MENU_ITEM of type Atk.Role>, 35: <enum ATK_ROLE_OPTION_PANE of type Atk.Role>, 36: <enum ATK_ROLE_PAGE_TAB of type Atk.Role>, 37: <enum ATK_ROLE_PAGE_TAB_LIST of type Atk.Role>, 38: <enum ATK_ROLE_PANEL of type Atk.Role>, 39: <enum ATK_ROLE_PASSWORD_TEXT of type Atk.Role>, 40: <enum ATK_ROLE_POPUP_MENU of type Atk.Role>, 41: <enum ATK_ROLE_PROGRESS_BAR of type Atk.Role>, 42: <enum ATK_ROLE_BUTTON of type Atk.Role>, 43: <enum ATK_ROLE_RADIO_BUTTON of type Atk.Role>, 44: <enum ATK_ROLE_RADIO_MENU_ITEM of type Atk.Role>, 45: <enum ATK_ROLE_ROOT_PANE of type Atk.Role>, 46: <enum ATK_ROLE_ROW_HEADER of type Atk.Role>, 47: <enum ATK_ROLE_SCROLL_BAR of type Atk.Role>, 48: <enum ATK_ROLE_SCROLL_PANE of type Atk.Role>, 49: <enum ATK_ROLE_SEPARATOR of type Atk.Role>, 50: <enum ATK_ROLE_SLIDER of type Atk.Role>, 51: <enum ATK_ROLE_SPLIT_PANE of type Atk.Role>, 52: <enum ATK_ROLE_SPIN_BUTTON of type Atk.Role>, 53: <enum ATK_ROLE_STATUSBAR of type Atk.Role>, 54: <enum ATK_ROLE_TABLE of type Atk.Role>, 55: <enum ATK_ROLE_TABLE_CELL of type Atk.Role>, 56: <enum ATK_ROLE_TABLE_COLUMN_HEADER of type Atk.Role>, 57: <enum ATK_ROLE_TABLE_ROW_HEADER of type Atk.Role>, 58: <enum ATK_ROLE_TEAR_OFF_MENU_ITEM of type Atk.Role>, 59: <enum ATK_ROLE_TERMINAL of type Atk.Role>, 60: <enum ATK_ROLE_TEXT of type Atk.Role>, 61: <enum ATK_ROLE_TOGGLE_BUTTON of type Atk.Role>, 62: <enum ATK_ROLE_TOOL_BAR of type Atk.Role>, 63: <enum ATK_ROLE_TOOL_TIP of type Atk.Role>, 64: <enum ATK_ROLE_TREE of type Atk.Role>, 65: <enum ATK_ROLE_TREE_TABLE of type Atk.Role>, 66: <enum ATK_ROLE_UNKNOWN of type Atk.Role>, 67: <enum ATK_ROLE_VIEWPORT of type Atk.Role>, 68: <enum ATK_ROLE_WINDOW of type Atk.Role>, 69: <enum ATK_ROLE_HEADER of type Atk.Role>, 70: <enum ATK_ROLE_FOOTER of type Atk.Role>, 71: <enum ATK_ROLE_PARAGRAPH of type Atk.Role>, 72: <enum ATK_ROLE_RULER of type Atk.Role>, 73: <enum ATK_ROLE_APPLICATION of type Atk.Role>, 74: <enum ATK_ROLE_AUTOCOMPLETE of type Atk.Role>, 75: <enum ATK_ROLE_EDITBAR of type Atk.Role>, 76: <enum ATK_ROLE_EMBEDDED of type Atk.Role>, 77: <enum ATK_ROLE_ENTRY of type Atk.Role>, 78: <enum ATK_ROLE_CHART of type Atk.Role>, 79: <enum ATK_ROLE_CAPTION of type Atk.Role>, 80: <enum ATK_ROLE_DOCUMENT_FRAME of type Atk.Role>, 81: <enum ATK_ROLE_HEADING of type Atk.Role>, 82: <enum ATK_ROLE_PAGE of type Atk.Role>, 83: <enum ATK_ROLE_SECTION of type Atk.Role>, 84: <enum ATK_ROLE_REDUNDANT_OBJECT of type Atk.Role>, 85: <enum ATK_ROLE_FORM of type Atk.Role>, 86: <enum ATK_ROLE_LINK of type Atk.Role>, 87: <enum ATK_ROLE_INPUT_METHOD_WINDOW of type Atk.Role>, 88: <enum ATK_ROLE_TABLE_ROW of type Atk.Role>, 89: <enum ATK_ROLE_TREE_ITEM of type Atk.Role>, 90: <enum ATK_ROLE_DOCUMENT_SPREADSHEET of type Atk.Role>, 91: <enum ATK_ROLE_DOCUMENT_PRESENTATION of type Atk.Role>, 92: <enum ATK_ROLE_DOCUMENT_TEXT of type Atk.Role>, 93: <enum ATK_ROLE_DOCUMENT_WEB of type Atk.Role>, 94: <enum ATK_ROLE_DOCUMENT_EMAIL of type Atk.Role>, 95: <enum ATK_ROLE_COMMENT of type Atk.Role>, 96: <enum ATK_ROLE_LIST_BOX of type Atk.Role>, 97: <enum ATK_ROLE_GROUPING of type Atk.Role>, 98: <enum ATK_ROLE_IMAGE_MAP of type Atk.Role>, 99: <enum ATK_ROLE_NOTIFICATION of type Atk.Role>, 100: <enum ATK_ROLE_INFO_BAR of type Atk.Role>, 101: <enum ATK_ROLE_LEVEL_BAR of type Atk.Role>, 102: <enum ATK_ROLE_TITLE_BAR of type Atk.Role>, 103: <enum ATK_ROLE_BLOCK_QUOTE of type Atk.Role>, 104: <enum ATK_ROLE_AUDIO of type Atk.Role>, 105: <enum ATK_ROLE_VIDEO of type Atk.Role>, 106: <enum ATK_ROLE_DEFINITION of type Atk.Role>, 107: <enum ATK_ROLE_ARTICLE of type Atk.Role>, 108: <enum ATK_ROLE_LANDMARK of type Atk.Role>, 109: <enum ATK_ROLE_LOG of type Atk.Role>, 110: <enum ATK_ROLE_MARQUEE of type Atk.Role>, 111: <enum ATK_ROLE_MATH of type Atk.Role>, 112: <enum ATK_ROLE_RATING of type Atk.Role>, 113: <enum ATK_ROLE_TIMER of type Atk.Role>, 114: <enum ATK_ROLE_DESCRIPTION_LIST of type Atk.Role>, 115: <enum ATK_ROLE_DESCRIPTION_TERM of type Atk.Role>, 116: <enum ATK_ROLE_DESCRIPTION_VALUE of type Atk.Role>, 117: <enum ATK_ROLE_STATIC of type Atk.Role>, 118: <enum ATK_ROLE_MATH_FRACTION of type Atk.Role>, 119: <enum ATK_ROLE_MATH_ROOT of type Atk.Role>, 120: <enum ATK_ROLE_SUBSCRIPT of type Atk.Role>, 121: <enum ATK_ROLE_SUPERSCRIPT of type Atk.Role>, 122: <enum ATK_ROLE_FOOTNOTE of type Atk.Role>, 123: <enum ATK_ROLE_CONTENT_DELETION of type Atk.Role>, 124: <enum ATK_ROLE_CONTENT_INSERTION of type Atk.Role>, 125: <enum ATK_ROLE_MARK of type Atk.Role>, 126: <enum ATK_ROLE_SUGGESTION of type Atk.Role>, 127: <enum ATK_ROLE_PUSH_BUTTON_MENU of type Atk.Role>, 128: <enum ATK_ROLE_LAST_DEFINED of type Atk.Role>}, '__info__': gi.EnumInfo(Role), 'INVALID': <enum ATK_ROLE_INVALID of type Atk.Role>, 'ACCELERATOR_LABEL': <enum ATK_ROLE_ACCEL_LABEL of type Atk.Role>, 'ALERT': <enum ATK_ROLE_ALERT of type Atk.Role>, 'ANIMATION': <enum ATK_ROLE_ANIMATION of type Atk.Role>, 'ARROW': <enum ATK_ROLE_ARROW of type Atk.Role>, 'CALENDAR': <enum ATK_ROLE_CALENDAR of type Atk.Role>, 'CANVAS': <enum ATK_ROLE_CANVAS of type Atk.Role>, 'CHECK_BOX': <enum ATK_ROLE_CHECK_BOX of type Atk.Role>, 'CHECK_MENU_ITEM': <enum ATK_ROLE_CHECK_MENU_ITEM of type Atk.Role>, 'COLOR_CHOOSER': <enum ATK_ROLE_COLOR_CHOOSER of type Atk.Role>, 'COLUMN_HEADER': <enum ATK_ROLE_COLUMN_HEADER of type Atk.Role>, 'COMBO_BOX': <enum ATK_ROLE_COMBO_BOX of type Atk.Role>, 'DATE_EDITOR': <enum ATK_ROLE_DATE_EDITOR of type Atk.Role>, 'DESKTOP_ICON': <enum ATK_ROLE_DESKTOP_ICON of type Atk.Role>, 'DESKTOP_FRAME': <enum ATK_ROLE_DESKTOP_FRAME of type Atk.Role>, 'DIAL': <enum ATK_ROLE_DIAL of type Atk.Role>, 'DIALOG': <enum ATK_ROLE_DIALOG of type Atk.Role>, 'DIRECTORY_PANE': <enum ATK_ROLE_DIRECTORY_PANE of type Atk.Role>, 'DRAWING_AREA': <enum ATK_ROLE_DRAWING_AREA of type Atk.Role>, 'FILE_CHOOSER': <enum ATK_ROLE_FILE_CHOOSER of type Atk.Role>, 'FILLER': <enum ATK_ROLE_FILLER of type Atk.Role>, 'FONT_CHOOSER': <enum ATK_ROLE_FONT_CHOOSER of type Atk.Role>, 'FRAME': <enum ATK_ROLE_FRAME of type Atk.Role>, 'GLASS_PANE': <enum ATK_ROLE_GLASS_PANE of type Atk.Role>, 'HTML_CONTAINER': <enum ATK_ROLE_HTML_CONTAINER of type Atk.Role>, 'ICON': <enum ATK_ROLE_ICON of type Atk.Role>, 'IMAGE': <enum ATK_ROLE_IMAGE of type Atk.Role>, 'INTERNAL_FRAME': <enum ATK_ROLE_INTERNAL_FRAME of type Atk.Role>, 'LABEL': <enum ATK_ROLE_LABEL of type Atk.Role>, 'LAYERED_PANE': <enum ATK_ROLE_LAYERED_PANE of type Atk.Role>, 'LIST': <enum ATK_ROLE_LIST of type Atk.Role>, 'LIST_ITEM': <enum ATK_ROLE_LIST_ITEM of type Atk.Role>, 'MENU': <enum ATK_ROLE_MENU of type Atk.Role>, 'MENU_BAR': <enum ATK_ROLE_MENU_BAR of type Atk.Role>, 'MENU_ITEM': <enum ATK_ROLE_MENU_ITEM of type Atk.Role>, 'OPTION_PANE': <enum ATK_ROLE_OPTION_PANE of type Atk.Role>, 'PAGE_TAB': <enum ATK_ROLE_PAGE_TAB of type Atk.Role>, 'PAGE_TAB_LIST': <enum ATK_ROLE_PAGE_TAB_LIST of type Atk.Role>, 'PANEL': <enum ATK_ROLE_PANEL of type Atk.Role>, 'PASSWORD_TEXT': <enum ATK_ROLE_PASSWORD_TEXT of type Atk.Role>, 'POPUP_MENU': <enum ATK_ROLE_POPUP_MENU of type Atk.Role>, 'PROGRESS_BAR': <enum ATK_ROLE_PROGRESS_BAR of type Atk.Role>, 'BUTTON': <enum ATK_ROLE_BUTTON of type Atk.Role>, 'RADIO_BUTTON': <enum ATK_ROLE_RADIO_BUTTON of type Atk.Role>, 'RADIO_MENU_ITEM': <enum ATK_ROLE_RADIO_MENU_ITEM of type Atk.Role>, 'ROOT_PANE': <enum ATK_ROLE_ROOT_PANE of type Atk.Role>, 'ROW_HEADER': <enum ATK_ROLE_ROW_HEADER of type Atk.Role>, 'SCROLL_BAR': <enum ATK_ROLE_SCROLL_BAR of type Atk.Role>, 'SCROLL_PANE': <enum ATK_ROLE_SCROLL_PANE of type Atk.Role>, 'SEPARATOR': <enum ATK_ROLE_SEPARATOR of type Atk.Role>, 'SLIDER': <enum ATK_ROLE_SLIDER of type Atk.Role>, 'SPLIT_PANE': <enum ATK_ROLE_SPLIT_PANE of type Atk.Role>, 'SPIN_BUTTON': <enum ATK_ROLE_SPIN_BUTTON of type Atk.Role>, 'STATUSBAR': <enum ATK_ROLE_STATUSBAR of type Atk.Role>, 'TABLE': <enum ATK_ROLE_TABLE of type Atk.Role>, 'TABLE_CELL': <enum ATK_ROLE_TABLE_CELL of type Atk.Role>, 'TABLE_COLUMN_HEADER': <enum ATK_ROLE_TABLE_COLUMN_HEADER of type Atk.Role>, 'TABLE_ROW_HEADER': <enum ATK_ROLE_TABLE_ROW_HEADER of type Atk.Role>, 'TEAR_OFF_MENU_ITEM': <enum ATK_ROLE_TEAR_OFF_MENU_ITEM of type Atk.Role>, 'TERMINAL': <enum ATK_ROLE_TERMINAL of type Atk.Role>, 'TEXT': <enum ATK_ROLE_TEXT of type Atk.Role>, 'TOGGLE_BUTTON': <enum ATK_ROLE_TOGGLE_BUTTON of type Atk.Role>, 'TOOL_BAR': <enum ATK_ROLE_TOOL_BAR of type Atk.Role>, 'TOOL_TIP': <enum ATK_ROLE_TOOL_TIP of type Atk.Role>, 'TREE': <enum ATK_ROLE_TREE of type Atk.Role>, 'TREE_TABLE': <enum ATK_ROLE_TREE_TABLE of type Atk.Role>, 'UNKNOWN': <enum ATK_ROLE_UNKNOWN of type Atk.Role>, 'VIEWPORT': <enum ATK_ROLE_VIEWPORT of type Atk.Role>, 'WINDOW': <enum ATK_ROLE_WINDOW of type Atk.Role>, 'HEADER': <enum ATK_ROLE_HEADER of type Atk.Role>, 'FOOTER': <enum ATK_ROLE_FOOTER of type Atk.Role>, 'PARAGRAPH': <enum ATK_ROLE_PARAGRAPH of type Atk.Role>, 'RULER': <enum ATK_ROLE_RULER of type Atk.Role>, 'APPLICATION': <enum ATK_ROLE_APPLICATION of type Atk.Role>, 'AUTOCOMPLETE': <enum ATK_ROLE_AUTOCOMPLETE of type Atk.Role>, 'EDIT_BAR': <enum ATK_ROLE_EDITBAR of type Atk.Role>, 'EMBEDDED': <enum ATK_ROLE_EMBEDDED of type Atk.Role>, 'ENTRY': <enum ATK_ROLE_ENTRY of type Atk.Role>, 'CHART': <enum ATK_ROLE_CHART of type Atk.Role>, 'CAPTION': <enum ATK_ROLE_CAPTION of type Atk.Role>, 'DOCUMENT_FRAME': <enum ATK_ROLE_DOCUMENT_FRAME of type Atk.Role>, 'HEADING': <enum ATK_ROLE_HEADING of type Atk.Role>, 'PAGE': <enum ATK_ROLE_PAGE of type Atk.Role>, 'SECTION': <enum ATK_ROLE_SECTION of type Atk.Role>, 'REDUNDANT_OBJECT': <enum ATK_ROLE_REDUNDANT_OBJECT of type Atk.Role>, 'FORM': <enum ATK_ROLE_FORM of type Atk.Role>, 'LINK': <enum ATK_ROLE_LINK of type Atk.Role>, 'INPUT_METHOD_WINDOW': <enum ATK_ROLE_INPUT_METHOD_WINDOW of type Atk.Role>, 'TABLE_ROW': <enum ATK_ROLE_TABLE_ROW of type Atk.Role>, 'TREE_ITEM': <enum ATK_ROLE_TREE_ITEM of type Atk.Role>, 'DOCUMENT_SPREADSHEET': <enum ATK_ROLE_DOCUMENT_SPREADSHEET of type Atk.Role>, 'DOCUMENT_PRESENTATION': <enum ATK_ROLE_DOCUMENT_PRESENTATION of type Atk.Role>, 'DOCUMENT_TEXT': <enum ATK_ROLE_DOCUMENT_TEXT of type Atk.Role>, 'DOCUMENT_WEB': <enum ATK_ROLE_DOCUMENT_WEB of type Atk.Role>, 'DOCUMENT_EMAIL': <enum ATK_ROLE_DOCUMENT_EMAIL of type Atk.Role>, 'COMMENT': <enum ATK_ROLE_COMMENT of type Atk.Role>, 'LIST_BOX': <enum ATK_ROLE_LIST_BOX of type Atk.Role>, 'GROUPING': <enum ATK_ROLE_GROUPING of type Atk.Role>, 'IMAGE_MAP': <enum ATK_ROLE_IMAGE_MAP of type Atk.Role>, 'NOTIFICATION': <enum ATK_ROLE_NOTIFICATION of type Atk.Role>, 'INFO_BAR': <enum ATK_ROLE_INFO_BAR of type Atk.Role>, 'LEVEL_BAR': <enum ATK_ROLE_LEVEL_BAR of type Atk.Role>, 'TITLE_BAR': <enum ATK_ROLE_TITLE_BAR of type Atk.Role>, 'BLOCK_QUOTE': <enum ATK_ROLE_BLOCK_QUOTE of type Atk.Role>, 'AUDIO': <enum ATK_ROLE_AUDIO of type Atk.Role>, 'VIDEO': <enum ATK_ROLE_VIDEO of type Atk.Role>, 'DEFINITION': <enum ATK_ROLE_DEFINITION of type Atk.Role>, 'ARTICLE': <enum ATK_ROLE_ARTICLE of type Atk.Role>, 'LANDMARK': <enum ATK_ROLE_LANDMARK of type Atk.Role>, 'LOG': <enum ATK_ROLE_LOG of type Atk.Role>, 'MARQUEE': <enum ATK_ROLE_MARQUEE of type Atk.Role>, 'MATH': <enum ATK_ROLE_MATH of type Atk.Role>, 'RATING': <enum ATK_ROLE_RATING of type Atk.Role>, 'TIMER': <enum ATK_ROLE_TIMER of type Atk.Role>, 'DESCRIPTION_LIST': <enum ATK_ROLE_DESCRIPTION_LIST of type Atk.Role>, 'DESCRIPTION_TERM': <enum ATK_ROLE_DESCRIPTION_TERM of type Atk.Role>, 'DESCRIPTION_VALUE': <enum ATK_ROLE_DESCRIPTION_VALUE of type Atk.Role>, 'STATIC': <enum ATK_ROLE_STATIC of type Atk.Role>, 'MATH_FRACTION': <enum ATK_ROLE_MATH_FRACTION of type Atk.Role>, 'MATH_ROOT': <enum ATK_ROLE_MATH_ROOT of type Atk.Role>, 'SUBSCRIPT': <enum ATK_ROLE_SUBSCRIPT of type Atk.Role>, 'SUPERSCRIPT': <enum ATK_ROLE_SUPERSCRIPT of type Atk.Role>, 'FOOTNOTE': <enum ATK_ROLE_FOOTNOTE of type Atk.Role>, 'CONTENT_DELETION': <enum ATK_ROLE_CONTENT_DELETION of type Atk.Role>, 'CONTENT_INSERTION': <enum ATK_ROLE_CONTENT_INSERTION of type Atk.Role>, 'MARK': <enum ATK_ROLE_MARK of type Atk.Role>, 'SUGGESTION': <enum ATK_ROLE_SUGGESTION of type Atk.Role>, 'PUSH_BUTTON_MENU': <enum ATK_ROLE_PUSH_BUTTON_MENU of type Atk.Role>, 'LAST_DEFINED': <enum ATK_ROLE_LAST_DEFINED of type Atk.Role>, 'PUSH_BUTTON': <enum ATK_ROLE_BUTTON of type Atk.Role>, 'for_name': gi.FunctionInfo(for_name, bound=None), 'get_localized_name': gi.FunctionInfo(get_localized_name, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'register': gi.FunctionInfo(register, bound=None)})"
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
    }
    __gtype__ = None # (!) real value is '<GType AtkRole (892679184)>'
    __info__ = gi.EnumInfo(Role)


