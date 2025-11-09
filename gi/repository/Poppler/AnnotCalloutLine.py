# encoding: utf-8
# module gi.repository.Poppler
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Poppler-0.18.typelib
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


class AnnotCalloutLine(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        AnnotCalloutLine()
        new() -> Poppler.AnnotCalloutLine
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Poppler.AnnotCalloutLine """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Poppler.AnnotCalloutLine """
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
        """ new() -> Poppler.AnnotCalloutLine """
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

    multiline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AnnotCalloutLine), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerAnnotCalloutLine (3984430016)>, '__dict__': <attribute '__dict__' of 'AnnotCalloutLine' objects>, '__weakref__': <attribute '__weakref__' of 'AnnotCalloutLine' objects>, '__doc__': None, 'multiline': <property object at 0x000001deefead8a0>, 'x1': <property object at 0x000001deefead990>, 'y1': <property object at 0x000001deefeada80>, 'x2': <property object at 0x000001deefeadb70>, 'y2': <property object at 0x000001deefeadc60>, 'x3': <property object at 0x000001deefeadd50>, 'y3': <property object at 0x000001deefeade40>, 'new': gi.FunctionInfo(new, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'free': gi.FunctionInfo(free, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000001deefdd7880>})"
    __gtype__ = None # (!) real value is '<GType PopplerAnnotCalloutLine (3984430016)>'
    __info__ = StructInfo(AnnotCalloutLine)


