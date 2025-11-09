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


class LayoutIter(__gi.Boxed):
    # no doc
    def at_last_line(self): # real signature unknown; restored from __doc__
        """ at_last_line(self) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.LayoutIter or None """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_baseline(self): # real signature unknown; restored from __doc__
        """ get_baseline(self) -> int """
        return 0

    def get_char_extents(self): # real signature unknown; restored from __doc__
        """ get_char_extents(self) -> logical_rect:Pango.Rectangle """
        pass

    def get_cluster_extents(self): # real signature unknown; restored from __doc__
        """ get_cluster_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_index(self): # real signature unknown; restored from __doc__
        """ get_index(self) -> int """
        return 0

    def get_layout(self): # real signature unknown; restored from __doc__
        """ get_layout(self) -> Pango.Layout or None """
        pass

    def get_layout_extents(self): # real signature unknown; restored from __doc__
        """ get_layout_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_line(self): # real signature unknown; restored from __doc__
        """ get_line(self) -> Pango.LayoutLine or None """
        pass

    def get_line_extents(self): # real signature unknown; restored from __doc__
        """ get_line_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_line_readonly(self): # real signature unknown; restored from __doc__
        """ get_line_readonly(self) -> Pango.LayoutLine or None """
        pass

    def get_line_yrange(self): # real signature unknown; restored from __doc__
        """ get_line_yrange(self) -> y0_:int, y1_:int """
        pass

    def get_run(self): # real signature unknown; restored from __doc__
        """ get_run(self) -> Pango.GlyphItem or None """
        pass

    def get_run_baseline(self): # real signature unknown; restored from __doc__
        """ get_run_baseline(self) -> int """
        return 0

    def get_run_extents(self): # real signature unknown; restored from __doc__
        """ get_run_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_run_readonly(self): # real signature unknown; restored from __doc__
        """ get_run_readonly(self) -> Pango.GlyphItem or None """
        pass

    def next_char(self): # real signature unknown; restored from __doc__
        """ next_char(self) -> bool """
        return False

    def next_cluster(self): # real signature unknown; restored from __doc__
        """ next_cluster(self) -> bool """
        return False

    def next_line(self): # real signature unknown; restored from __doc__
        """ next_line(self) -> bool """
        return False

    def next_run(self): # real signature unknown; restored from __doc__
        """ next_run(self) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(LayoutIter), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoLayoutIter (4081760048)>, '__dict__': <attribute '__dict__' of 'LayoutIter' objects>, '__weakref__': <attribute '__weakref__' of 'LayoutIter' objects>, '__doc__': None, 'at_last_line': gi.FunctionInfo(at_last_line, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_baseline': gi.FunctionInfo(get_baseline, bound=None), 'get_char_extents': gi.FunctionInfo(get_char_extents, bound=None), 'get_cluster_extents': gi.FunctionInfo(get_cluster_extents, bound=None), 'get_index': gi.FunctionInfo(get_index, bound=None), 'get_layout': gi.FunctionInfo(get_layout, bound=None), 'get_layout_extents': gi.FunctionInfo(get_layout_extents, bound=None), 'get_line': gi.FunctionInfo(get_line, bound=None), 'get_line_extents': gi.FunctionInfo(get_line_extents, bound=None), 'get_line_readonly': gi.FunctionInfo(get_line_readonly, bound=None), 'get_line_yrange': gi.FunctionInfo(get_line_yrange, bound=None), 'get_run': gi.FunctionInfo(get_run, bound=None), 'get_run_baseline': gi.FunctionInfo(get_run_baseline, bound=None), 'get_run_extents': gi.FunctionInfo(get_run_extents, bound=None), 'get_run_readonly': gi.FunctionInfo(get_run_readonly, bound=None), 'next_char': gi.FunctionInfo(next_char, bound=None), 'next_cluster': gi.FunctionInfo(next_cluster, bound=None), 'next_line': gi.FunctionInfo(next_line, bound=None), 'next_run': gi.FunctionInfo(next_run, bound=None)})"
    __gtype__ = None # (!) real value is '<GType PangoLayoutIter (4081760048)>'
    __info__ = StructInfo(LayoutIter)


