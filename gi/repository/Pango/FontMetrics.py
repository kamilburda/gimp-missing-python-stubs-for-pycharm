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


class FontMetrics(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        FontMetrics()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_approximate_char_width(self): # real signature unknown; restored from __doc__
        """ get_approximate_char_width(self) -> int """
        return 0

    def get_approximate_digit_width(self): # real signature unknown; restored from __doc__
        """ get_approximate_digit_width(self) -> int """
        return 0

    def get_ascent(self): # real signature unknown; restored from __doc__
        """ get_ascent(self) -> int """
        return 0

    def get_descent(self): # real signature unknown; restored from __doc__
        """ get_descent(self) -> int """
        return 0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_strikethrough_position(self): # real signature unknown; restored from __doc__
        """ get_strikethrough_position(self) -> int """
        return 0

    def get_strikethrough_thickness(self): # real signature unknown; restored from __doc__
        """ get_strikethrough_thickness(self) -> int """
        return 0

    def get_underline_position(self): # real signature unknown; restored from __doc__
        """ get_underline_position(self) -> int """
        return 0

    def get_underline_thickness(self): # real signature unknown; restored from __doc__
        """ get_underline_thickness(self) -> int """
        return 0

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Pango.FontMetrics or None """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    approximate_char_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    approximate_digit_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ascent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    descent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strikethrough_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strikethrough_thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underline_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    underline_thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FontMetrics), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoFontMetrics (4081765088)>, '__dict__': <attribute '__dict__' of 'FontMetrics' objects>, '__weakref__': <attribute '__weakref__' of 'FontMetrics' objects>, '__doc__': None, 'ref_count': <property object at 0x00000213f6084130>, 'ascent': <property object at 0x00000213f6084220>, 'descent': <property object at 0x00000213f6084310>, 'height': <property object at 0x00000213f6084400>, 'approximate_char_width': <property object at 0x00000213f60844f0>, 'approximate_digit_width': <property object at 0x00000213f60845e0>, 'underline_position': <property object at 0x00000213f60846d0>, 'underline_thickness': <property object at 0x00000213f60847c0>, 'strikethrough_position': <property object at 0x00000213f60848b0>, 'strikethrough_thickness': <property object at 0x00000213f60849a0>, 'get_approximate_char_width': gi.FunctionInfo(get_approximate_char_width, bound=None), 'get_approximate_digit_width': gi.FunctionInfo(get_approximate_digit_width, bound=None), 'get_ascent': gi.FunctionInfo(get_ascent, bound=None), 'get_descent': gi.FunctionInfo(get_descent, bound=None), 'get_height': gi.FunctionInfo(get_height, bound=None), 'get_strikethrough_position': gi.FunctionInfo(get_strikethrough_position, bound=None), 'get_strikethrough_thickness': gi.FunctionInfo(get_strikethrough_thickness, bound=None), 'get_underline_position': gi.FunctionInfo(get_underline_position, bound=None), 'get_underline_thickness': gi.FunctionInfo(get_underline_thickness, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'unref': gi.FunctionInfo(unref, bound=None)})"
    __gtype__ = None # (!) real value is '<GType PangoFontMetrics (4081765088)>'
    __info__ = StructInfo(FontMetrics)


