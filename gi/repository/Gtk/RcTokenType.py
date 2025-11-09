# encoding: utf-8
# module gi.repository.Gtk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class RcTokenType(__gobject.GEnum):
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


    ACTIVE = 273
    APPLICATION = 296
    BASE = 280
    BG = 278
    BG_PIXMAP = 286
    BIND = 290
    BINDING = 289
    CLASS = 293
    COLOR = 307
    ENGINE = 300
    FG = 277
    FONT = 283
    FONTSET = 284
    FONT_NAME = 285
    GTK = 295
    HIGHEST = 299
    IM_MODULE_FILE = 303
    IM_MODULE_PATH = 302
    INCLUDE = 271
    INSENSITIVE = 276
    INVALID = 270
    LAST = 309
    LOWEST = 294
    LTR = 305
    MODULE_PATH = 301
    NORMAL = 272
    PIXMAP_PATH = 287
    PRELIGHT = 274
    RC = 298
    RTL = 306
    SELECTED = 275
    STOCK = 304
    STYLE = 288
    TEXT = 279
    THEME = 297
    UNBIND = 308
    WIDGET = 291
    WIDGET_CLASS = 292
    XTHICKNESS = 281
    YTHICKNESS = 282
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gtk', '__dict__': <attribute '__dict__' of 'RcTokenType' objects>, '__doc__': None, '__gtype__': <GType GtkRcTokenType (3923955952)>, '__enum_values__': {270: <enum GTK_RC_TOKEN_INVALID of type Gtk.RcTokenType>, 271: <enum GTK_RC_TOKEN_INCLUDE of type Gtk.RcTokenType>, 272: <enum GTK_RC_TOKEN_NORMAL of type Gtk.RcTokenType>, 273: <enum GTK_RC_TOKEN_ACTIVE of type Gtk.RcTokenType>, 274: <enum GTK_RC_TOKEN_PRELIGHT of type Gtk.RcTokenType>, 275: <enum GTK_RC_TOKEN_SELECTED of type Gtk.RcTokenType>, 276: <enum GTK_RC_TOKEN_INSENSITIVE of type Gtk.RcTokenType>, 277: <enum GTK_RC_TOKEN_FG of type Gtk.RcTokenType>, 278: <enum GTK_RC_TOKEN_BG of type Gtk.RcTokenType>, 279: <enum GTK_RC_TOKEN_TEXT of type Gtk.RcTokenType>, 280: <enum GTK_RC_TOKEN_BASE of type Gtk.RcTokenType>, 281: <enum GTK_RC_TOKEN_XTHICKNESS of type Gtk.RcTokenType>, 282: <enum GTK_RC_TOKEN_YTHICKNESS of type Gtk.RcTokenType>, 283: <enum GTK_RC_TOKEN_FONT of type Gtk.RcTokenType>, 284: <enum GTK_RC_TOKEN_FONTSET of type Gtk.RcTokenType>, 285: <enum GTK_RC_TOKEN_FONT_NAME of type Gtk.RcTokenType>, 286: <enum GTK_RC_TOKEN_BG_PIXMAP of type Gtk.RcTokenType>, 287: <enum GTK_RC_TOKEN_PIXMAP_PATH of type Gtk.RcTokenType>, 288: <enum GTK_RC_TOKEN_STYLE of type Gtk.RcTokenType>, 289: <enum GTK_RC_TOKEN_BINDING of type Gtk.RcTokenType>, 290: <enum GTK_RC_TOKEN_BIND of type Gtk.RcTokenType>, 291: <enum GTK_RC_TOKEN_WIDGET of type Gtk.RcTokenType>, 292: <enum GTK_RC_TOKEN_WIDGET_CLASS of type Gtk.RcTokenType>, 293: <enum GTK_RC_TOKEN_CLASS of type Gtk.RcTokenType>, 294: <enum GTK_RC_TOKEN_LOWEST of type Gtk.RcTokenType>, 295: <enum GTK_RC_TOKEN_GTK of type Gtk.RcTokenType>, 296: <enum GTK_RC_TOKEN_APPLICATION of type Gtk.RcTokenType>, 297: <enum GTK_RC_TOKEN_THEME of type Gtk.RcTokenType>, 298: <enum GTK_RC_TOKEN_RC of type Gtk.RcTokenType>, 299: <enum GTK_RC_TOKEN_HIGHEST of type Gtk.RcTokenType>, 300: <enum GTK_RC_TOKEN_ENGINE of type Gtk.RcTokenType>, 301: <enum GTK_RC_TOKEN_MODULE_PATH of type Gtk.RcTokenType>, 302: <enum GTK_RC_TOKEN_IM_MODULE_PATH of type Gtk.RcTokenType>, 303: <enum GTK_RC_TOKEN_IM_MODULE_FILE of type Gtk.RcTokenType>, 304: <enum GTK_RC_TOKEN_STOCK of type Gtk.RcTokenType>, 305: <enum GTK_RC_TOKEN_LTR of type Gtk.RcTokenType>, 306: <enum GTK_RC_TOKEN_RTL of type Gtk.RcTokenType>, 307: <enum GTK_RC_TOKEN_COLOR of type Gtk.RcTokenType>, 308: <enum GTK_RC_TOKEN_UNBIND of type Gtk.RcTokenType>, 309: <enum GTK_RC_TOKEN_LAST of type Gtk.RcTokenType>}, '__info__': gi.EnumInfo(RcTokenType), 'INVALID': <enum GTK_RC_TOKEN_INVALID of type Gtk.RcTokenType>, 'INCLUDE': <enum GTK_RC_TOKEN_INCLUDE of type Gtk.RcTokenType>, 'NORMAL': <enum GTK_RC_TOKEN_NORMAL of type Gtk.RcTokenType>, 'ACTIVE': <enum GTK_RC_TOKEN_ACTIVE of type Gtk.RcTokenType>, 'PRELIGHT': <enum GTK_RC_TOKEN_PRELIGHT of type Gtk.RcTokenType>, 'SELECTED': <enum GTK_RC_TOKEN_SELECTED of type Gtk.RcTokenType>, 'INSENSITIVE': <enum GTK_RC_TOKEN_INSENSITIVE of type Gtk.RcTokenType>, 'FG': <enum GTK_RC_TOKEN_FG of type Gtk.RcTokenType>, 'BG': <enum GTK_RC_TOKEN_BG of type Gtk.RcTokenType>, 'TEXT': <enum GTK_RC_TOKEN_TEXT of type Gtk.RcTokenType>, 'BASE': <enum GTK_RC_TOKEN_BASE of type Gtk.RcTokenType>, 'XTHICKNESS': <enum GTK_RC_TOKEN_XTHICKNESS of type Gtk.RcTokenType>, 'YTHICKNESS': <enum GTK_RC_TOKEN_YTHICKNESS of type Gtk.RcTokenType>, 'FONT': <enum GTK_RC_TOKEN_FONT of type Gtk.RcTokenType>, 'FONTSET': <enum GTK_RC_TOKEN_FONTSET of type Gtk.RcTokenType>, 'FONT_NAME': <enum GTK_RC_TOKEN_FONT_NAME of type Gtk.RcTokenType>, 'BG_PIXMAP': <enum GTK_RC_TOKEN_BG_PIXMAP of type Gtk.RcTokenType>, 'PIXMAP_PATH': <enum GTK_RC_TOKEN_PIXMAP_PATH of type Gtk.RcTokenType>, 'STYLE': <enum GTK_RC_TOKEN_STYLE of type Gtk.RcTokenType>, 'BINDING': <enum GTK_RC_TOKEN_BINDING of type Gtk.RcTokenType>, 'BIND': <enum GTK_RC_TOKEN_BIND of type Gtk.RcTokenType>, 'WIDGET': <enum GTK_RC_TOKEN_WIDGET of type Gtk.RcTokenType>, 'WIDGET_CLASS': <enum GTK_RC_TOKEN_WIDGET_CLASS of type Gtk.RcTokenType>, 'CLASS': <enum GTK_RC_TOKEN_CLASS of type Gtk.RcTokenType>, 'LOWEST': <enum GTK_RC_TOKEN_LOWEST of type Gtk.RcTokenType>, 'GTK': <enum GTK_RC_TOKEN_GTK of type Gtk.RcTokenType>, 'APPLICATION': <enum GTK_RC_TOKEN_APPLICATION of type Gtk.RcTokenType>, 'THEME': <enum GTK_RC_TOKEN_THEME of type Gtk.RcTokenType>, 'RC': <enum GTK_RC_TOKEN_RC of type Gtk.RcTokenType>, 'HIGHEST': <enum GTK_RC_TOKEN_HIGHEST of type Gtk.RcTokenType>, 'ENGINE': <enum GTK_RC_TOKEN_ENGINE of type Gtk.RcTokenType>, 'MODULE_PATH': <enum GTK_RC_TOKEN_MODULE_PATH of type Gtk.RcTokenType>, 'IM_MODULE_PATH': <enum GTK_RC_TOKEN_IM_MODULE_PATH of type Gtk.RcTokenType>, 'IM_MODULE_FILE': <enum GTK_RC_TOKEN_IM_MODULE_FILE of type Gtk.RcTokenType>, 'STOCK': <enum GTK_RC_TOKEN_STOCK of type Gtk.RcTokenType>, 'LTR': <enum GTK_RC_TOKEN_LTR of type Gtk.RcTokenType>, 'RTL': <enum GTK_RC_TOKEN_RTL of type Gtk.RcTokenType>, 'COLOR': <enum GTK_RC_TOKEN_COLOR of type Gtk.RcTokenType>, 'UNBIND': <enum GTK_RC_TOKEN_UNBIND of type Gtk.RcTokenType>, 'LAST': <enum GTK_RC_TOKEN_LAST of type Gtk.RcTokenType>})"
    __enum_values__ = {
        270: 270,
        271: 271,
        272: 272,
        273: 273,
        274: 274,
        275: 275,
        276: 276,
        277: 277,
        278: 278,
        279: 279,
        280: 280,
        281: 281,
        282: 282,
        283: 283,
        284: 284,
        285: 285,
        286: 286,
        287: 287,
        288: 288,
        289: 289,
        290: 290,
        291: 291,
        292: 292,
        293: 293,
        294: 294,
        295: 295,
        296: 296,
        297: 297,
        298: 298,
        299: 299,
        300: 300,
        301: 301,
        302: 302,
        303: 303,
        304: 304,
        305: 305,
        306: 306,
        307: 307,
        308: 308,
        309: 309,
    }
    __gtype__ = None # (!) real value is '<GType GtkRcTokenType (3923955952)>'
    __info__ = gi.EnumInfo(RcTokenType)


