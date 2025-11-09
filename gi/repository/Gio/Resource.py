# encoding: utf-8
# module gi.repository.Gio
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Resource(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_from_data(data:GLib.Bytes) -> Gio.Resource
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def enumerate_children(self, path, lookup_flags): # real signature unknown; restored from __doc__
        """ enumerate_children(self, path:str, lookup_flags:Gio.ResourceLookupFlags) -> list """
        return []

    def get_info(self, path, lookup_flags): # real signature unknown; restored from __doc__
        """ get_info(self, path:str, lookup_flags:Gio.ResourceLookupFlags) -> bool, size:int, flags:int """
        return False

    def load(self, filename): # real signature unknown; restored from __doc__
        """ load(filename:str) -> Gio.Resource """
        pass

    def lookup_data(self, path, lookup_flags): # real signature unknown; restored from __doc__
        """ lookup_data(self, path:str, lookup_flags:Gio.ResourceLookupFlags) -> GLib.Bytes """
        pass

    def new_from_data(self, data): # real signature unknown; restored from __doc__
        """ new_from_data(data:GLib.Bytes) -> Gio.Resource """
        pass

    def open_stream(self, path, lookup_flags): # real signature unknown; restored from __doc__
        """ open_stream(self, path:str, lookup_flags:Gio.ResourceLookupFlags) -> Gio.InputStream """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gio.Resource """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def _register(self): # real signature unknown; restored from __doc__
        """ _register(self) """
        pass

    def _unregister(self): # real signature unknown; restored from __doc__
        """ _unregister(self) """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Resource), '__module__': 'gi.repository.Gio', '__gtype__': <GType GResource (2466393984)>, '__dict__': <attribute '__dict__' of 'Resource' objects>, '__weakref__': <attribute '__weakref__' of 'Resource' objects>, '__doc__': None, 'new_from_data': gi.FunctionInfo(new_from_data, bound=None), '_register': gi.FunctionInfo(_register, bound=None), '_unregister': gi.FunctionInfo(_unregister, bound=None), 'enumerate_children': gi.FunctionInfo(enumerate_children, bound=None), 'get_info': gi.FunctionInfo(get_info, bound=None), 'lookup_data': gi.FunctionInfo(lookup_data, bound=None), 'open_stream': gi.FunctionInfo(open_stream, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), 'load': gi.FunctionInfo(load, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GResource (2466393984)>'
    __info__ = StructInfo(Resource)


