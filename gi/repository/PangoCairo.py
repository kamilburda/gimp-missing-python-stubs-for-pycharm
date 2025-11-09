# encoding: utf-8
# module gi.repository.PangoCairo
# from C:/Program Files/GIMP 3/lib/girepository-1.0\PangoCairo-1.0.typelib
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

import gobject as __gobject


# Variables with simple values

_namespace = 'PangoCairo'

_version = '1.0'

__weakref__ = None

# functions

def context_get_font_options(context): # real signature unknown; restored from __doc__
    """ context_get_font_options(context:Pango.Context) -> cairo.FontOptions or None """
    pass

def context_get_resolution(context): # real signature unknown; restored from __doc__
    """ context_get_resolution(context:Pango.Context) -> float """
    return 0.0

def context_set_font_options(context, options=None): # real signature unknown; restored from __doc__
    """ context_set_font_options(context:Pango.Context, options:cairo.FontOptions=None) """
    pass

def context_set_resolution(context, dpi): # real signature unknown; restored from __doc__
    """ context_set_resolution(context:Pango.Context, dpi:float) """
    pass

def context_set_shape_renderer(context, func=None, data=None): # real signature unknown; restored from __doc__
    """ context_set_shape_renderer(context:Pango.Context, func:PangoCairo.ShapeRendererFunc=None, data=None) """
    pass

def create_context(cr): # real signature unknown; restored from __doc__
    """ create_context(cr:cairo.Context) -> Pango.Context """
    pass

def create_layout(cr): # real signature unknown; restored from __doc__
    """ create_layout(cr:cairo.Context) -> Pango.Layout """
    pass

def error_underline_path(cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ error_underline_path(cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def font_map_get_default(): # real signature unknown; restored from __doc__
    """ font_map_get_default() -> Pango.FontMap """
    pass

def font_map_new(): # real signature unknown; restored from __doc__
    """ font_map_new() -> Pango.FontMap """
    pass

def font_map_new_for_font_type(fonttype): # real signature unknown; restored from __doc__
    """ font_map_new_for_font_type(fonttype:cairo.FontType) -> Pango.FontMap or None """
    pass

def glyph_string_path(cr, font, glyphs): # real signature unknown; restored from __doc__
    """ glyph_string_path(cr:cairo.Context, font:Pango.Font, glyphs:Pango.GlyphString) """
    pass

def layout_line_path(cr, line): # real signature unknown; restored from __doc__
    """ layout_line_path(cr:cairo.Context, line:Pango.LayoutLine) """
    pass

def layout_path(cr, layout): # real signature unknown; restored from __doc__
    """ layout_path(cr:cairo.Context, layout:Pango.Layout) """
    pass

def show_error_underline(cr, x, y, width, height): # real signature unknown; restored from __doc__
    """ show_error_underline(cr:cairo.Context, x:float, y:float, width:float, height:float) """
    pass

def show_glyph_item(cr, text, glyph_item): # real signature unknown; restored from __doc__
    """ show_glyph_item(cr:cairo.Context, text:str, glyph_item:Pango.GlyphItem) """
    pass

def show_glyph_string(cr, font, glyphs): # real signature unknown; restored from __doc__
    """ show_glyph_string(cr:cairo.Context, font:Pango.Font, glyphs:Pango.GlyphString) """
    pass

def show_layout(cr, layout): # real signature unknown; restored from __doc__
    """ show_layout(cr:cairo.Context, layout:Pango.Layout) """
    pass

def show_layout_line(cr, line): # real signature unknown; restored from __doc__
    """ show_layout_line(cr:cairo.Context, line:Pango.LayoutLine) """
    pass

def update_context(cr, context): # real signature unknown; restored from __doc__
    """ update_context(cr:cairo.Context, context:Pango.Context) """
    pass

def update_layout(cr, layout): # real signature unknown; restored from __doc__
    """ update_layout(cr:cairo.Context, layout:Pango.Layout) """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __getstate__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class Font(__gobject.GInterface):
    # no doc
    def get_scaled_font(self): # real signature unknown; restored from __doc__
        """ get_scaled_font(self) -> cairo.ScaledFont or None """
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
        """ Default object formatter. """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Font), '__module__': 'gi.repository.PangoCairo', '__gtype__': <GType PangoCairoFont (3735897552)>, '__dict__': <attribute '__dict__' of 'Font' objects>, '__weakref__': <attribute '__weakref__' of 'Font' objects>, '__doc__': None, '__gsignals__': {}, 'get_scaled_font': gi.FunctionInfo(get_scaled_font, bound=None)})"
    __gdoc__ = 'Interface PangoCairoFont\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PangoCairoFont (3735897552)>'
    __info__ = InterfaceInfo(Font)


class FontMap(__gobject.GInterface):
    # no doc
    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Pango.FontMap """
        pass

    def get_font_type(self): # real signature unknown; restored from __doc__
        """ get_font_type(self) -> cairo.FontType """
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> float """
        return 0.0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Pango.FontMap """
        pass

    def new_for_font_type(self, fonttype): # real signature unknown; restored from __doc__
        """ new_for_font_type(fonttype:cairo.FontType) -> Pango.FontMap or None """
        pass

    def set_default(self): # real signature unknown; restored from __doc__
        """ set_default(self) """
        pass

    def set_resolution(self, dpi): # real signature unknown; restored from __doc__
        """ set_resolution(self, dpi:float) """
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
        """ Default object formatter. """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(FontMap), '__module__': 'gi.repository.PangoCairo', '__gtype__': <GType PangoCairoFontMap (3735897664)>, '__dict__': <attribute '__dict__' of 'FontMap' objects>, '__weakref__': <attribute '__weakref__' of 'FontMap' objects>, '__doc__': None, '__gsignals__': {}, 'get_default': gi.FunctionInfo(get_default, bound=None), 'new': gi.FunctionInfo(new, bound=None), 'new_for_font_type': gi.FunctionInfo(new_for_font_type, bound=None), 'get_font_type': gi.FunctionInfo(get_font_type, bound=None), 'get_resolution': gi.FunctionInfo(get_resolution, bound=None), 'set_default': gi.FunctionInfo(set_default, bound=None), 'set_resolution': gi.FunctionInfo(set_resolution, bound=None)})"
    __gdoc__ = 'Interface PangoCairoFontMap\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PangoCairoFontMap (3735897664)>'
    __info__ = InterfaceInfo(FontMap)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x00000155e0dd8720>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x00000155e0dd8900>, '__repr__': <function IntrospectionModule.__repr__ at 0x00000155e0dd89a0>, '__dir__': <function IntrospectionModule.__dir__ at 0x00000155e0dd8a40>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x00000155e0502090>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.PangoCairo', loader=<gi.importer.DynamicImporter object at 0x00000155e0502090>)"

