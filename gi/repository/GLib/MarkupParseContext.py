# encoding: utf-8
# module gi.repository.GLib
# from C:/Program Files/GIMP 3/lib/girepository-1.0\GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # C:\Program Files\GIMP 3\lib\python3.12\site-packages\gi\_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class MarkupParseContext(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(parser:GLib.MarkupParser, flags:GLib.MarkupParseFlags, user_data=None, user_data_dnotify:GLib.DestroyNotify) -> GLib.MarkupParseContext
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def end_parse(self): # real signature unknown; restored from __doc__
        """ end_parse(self) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_element(self): # real signature unknown; restored from __doc__
        """ get_element(self) -> str """
        return ""

    def get_element_stack(self): # real signature unknown; restored from __doc__
        """ get_element_stack(self) -> list """
        return []

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> line_number:int, char_number:int """
        pass

    def get_user_data(self): # real signature unknown; restored from __doc__
        """ get_user_data(self) """
        pass

    def new(self, parser, flags, user_data=None, user_data_dnotify): # real signature unknown; restored from __doc__
        """ new(parser:GLib.MarkupParser, flags:GLib.MarkupParseFlags, user_data=None, user_data_dnotify:GLib.DestroyNotify) -> GLib.MarkupParseContext """
        pass

    def parse(self, text, text_len): # real signature unknown; restored from __doc__
        """ parse(self, text:str, text_len:int) -> bool """
        return False

    def pop(self): # real signature unknown; restored from __doc__
        """ pop(self) """
        pass

    def push(self, parser, user_data=None): # real signature unknown; restored from __doc__
        """ push(self, parser:GLib.MarkupParser, user_data=None) """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.MarkupParseContext """
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
        """ new(parser:GLib.MarkupParser, flags:GLib.MarkupParseFlags, user_data=None, user_data_dnotify:GLib.DestroyNotify) -> GLib.MarkupParseContext """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MarkupParseContext), '__module__': 'gi.repository.GLib', '__gtype__': <GType GMarkupParseContext (163504432)>, '__dict__': <attribute '__dict__' of 'MarkupParseContext' objects>, '__weakref__': <attribute '__weakref__' of 'MarkupParseContext' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'end_parse': gi.FunctionInfo(end_parse, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_element': gi.FunctionInfo(get_element, bound=None), 'get_element_stack': gi.FunctionInfo(get_element_stack, bound=None), 'get_position': gi.FunctionInfo(get_position, bound=None), 'get_user_data': gi.FunctionInfo(get_user_data, bound=None), 'parse': gi.FunctionInfo(parse, bound=None), 'pop': gi.FunctionInfo(pop, bound=None), 'push': gi.FunctionInfo(push, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'unref': gi.FunctionInfo(unref, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000002830be60720>})"
    __gtype__ = None # (!) real value is '<GType GMarkupParseContext (163504432)>'
    __info__ = StructInfo(MarkupParseContext)


