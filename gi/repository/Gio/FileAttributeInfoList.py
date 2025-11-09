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


class FileAttributeInfoList(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        FileAttributeInfoList()
        new() -> Gio.FileAttributeInfoList
    """
    def add(self, name, type, flags): # real signature unknown; restored from __doc__
        """ add(self, name:str, type:Gio.FileAttributeType, flags:Gio.FileAttributeInfoFlags) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gio.FileAttributeInfoList """
        pass

    def lookup(self, name): # real signature unknown; restored from __doc__
        """ lookup(self, name:str) -> Gio.FileAttributeInfo """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gio.FileAttributeInfoList """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gio.FileAttributeInfoList """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Gio.FileAttributeInfoList """
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

    infos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_infos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FileAttributeInfoList), '__module__': 'gi.repository.Gio', '__gtype__': <GType GFileAttributeInfoList (2472622240)>, '__dict__': <attribute '__dict__' of 'FileAttributeInfoList' objects>, '__weakref__': <attribute '__weakref__' of 'FileAttributeInfoList' objects>, '__doc__': None, 'infos': <property object at 0x000001a793e18450>, 'n_infos': <property object at 0x000001a793e18540>, 'new': gi.FunctionInfo(new, bound=None), 'add': gi.FunctionInfo(add, bound=None), 'dup': gi.FunctionInfo(dup, bound=None), 'lookup': gi.FunctionInfo(lookup, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000001a7937e8680>})"
    __gtype__ = None # (!) real value is '<GType GFileAttributeInfoList (2472622240)>'
    __info__ = StructInfo(FileAttributeInfoList)


