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


class Language(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def from_string(self, language=None): # real signature unknown; restored from __doc__
        """ from_string(language:str=None) -> Pango.Language or None """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Pango.Language """
        pass

    def get_preferred(self): # real signature unknown; restored from __doc__
        """ get_preferred() -> list or None """
        return []

    def get_sample_string(self): # real signature unknown; restored from __doc__
        """ get_sample_string(self) -> str """
        return ""

    def get_scripts(self): # real signature unknown; restored from __doc__
        """ get_scripts(self) -> list or None """
        return []

    def includes_script(self, script): # real signature unknown; restored from __doc__
        """ includes_script(self, script:Pango.Script) -> bool """
        return False

    def matches(self, range_list): # real signature unknown; restored from __doc__
        """ matches(self, range_list:str) -> bool """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Language), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoLanguage (4081766208)>, '__dict__': <attribute '__dict__' of 'Language' objects>, '__weakref__': <attribute '__weakref__' of 'Language' objects>, '__doc__': None, 'get_sample_string': gi.FunctionInfo(get_sample_string, bound=None), 'get_scripts': gi.FunctionInfo(get_scripts, bound=None), 'includes_script': gi.FunctionInfo(includes_script, bound=None), 'matches': gi.FunctionInfo(matches, bound=None), 'to_string': gi.FunctionInfo(to_string, bound=None), 'from_string': gi.FunctionInfo(from_string, bound=None), 'get_default': gi.FunctionInfo(get_default, bound=None), 'get_preferred': gi.FunctionInfo(get_preferred, bound=None)})"
    __gtype__ = None # (!) real value is '<GType PangoLanguage (4081766208)>'
    __info__ = StructInfo(Language)


