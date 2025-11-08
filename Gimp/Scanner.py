# encoding: utf-8
# module gi.repository.Gimp
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Scanner(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_file(file:Gio.File) -> Gimp.Scanner
        new_stream(input:Gio.InputStream) -> Gimp.Scanner
        new_string(text:list) -> Gimp.Scanner
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def new_file(self, file): # real signature unknown; restored from __doc__
        """ new_file(file:Gio.File) -> Gimp.Scanner """
        pass

    def new_stream(self, input): # real signature unknown; restored from __doc__
        """ new_stream(input:Gio.InputStream) -> Gimp.Scanner """
        pass

    def new_string(self, text): # real signature unknown; restored from __doc__
        """ new_string(text:list) -> Gimp.Scanner """
        pass

    def parse_boolean(self): # real signature unknown; restored from __doc__
        """ parse_boolean(self) -> bool, dest:bool """
        return False

    def parse_color(self): # real signature unknown; restored from __doc__
        """ parse_color(self) -> bool, color:Gegl.Color """
        return False

    def parse_data(self): # real signature unknown; restored from __doc__
        """ parse_data(self) -> bool, dest:list """
        return False

    def parse_double(self): # real signature unknown; restored from __doc__
        """ parse_double(self) -> bool, dest:float """
        return False

    def parse_identifier(self): # real signature unknown; restored from __doc__
        """ parse_identifier(self) -> bool, identifier:str """
        return False

    def parse_int(self): # real signature unknown; restored from __doc__
        """ parse_int(self) -> bool, dest:int """
        return False

    def parse_int64(self): # real signature unknown; restored from __doc__
        """ parse_int64(self) -> bool, dest:int """
        return False

    def parse_matrix2(self): # real signature unknown; restored from __doc__
        """ parse_matrix2(self) -> bool, dest:Gimp.Matrix2 """
        return False

    def parse_string(self): # real signature unknown; restored from __doc__
        """ parse_string(self) -> bool, dest:str """
        return False

    def parse_string_no_validate(self): # real signature unknown; restored from __doc__
        """ parse_string_no_validate(self) -> bool, dest:str """
        return False

    def parse_token(self, token): # real signature unknown; restored from __doc__
        """ parse_token(self, token:GLib.TokenType) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gimp.Scanner """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Scanner), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpScanner (3595414624)>, '__dict__': <attribute '__dict__' of 'Scanner' objects>, '__weakref__': <attribute '__weakref__' of 'Scanner' objects>, '__doc__': None, 'new_file': gi.FunctionInfo(new_file, bound=None), 'new_stream': gi.FunctionInfo(new_stream, bound=None), 'new_string': gi.FunctionInfo(new_string, bound=None), 'parse_boolean': gi.FunctionInfo(parse_boolean, bound=None), 'parse_color': gi.FunctionInfo(parse_color, bound=None), 'parse_data': gi.FunctionInfo(parse_data, bound=None), 'parse_double': gi.FunctionInfo(parse_double, bound=None), 'parse_identifier': gi.FunctionInfo(parse_identifier, bound=None), 'parse_int': gi.FunctionInfo(parse_int, bound=None), 'parse_int64': gi.FunctionInfo(parse_int64, bound=None), 'parse_matrix2': gi.FunctionInfo(parse_matrix2, bound=None), 'parse_string': gi.FunctionInfo(parse_string, bound=None), 'parse_string_no_validate': gi.FunctionInfo(parse_string_no_validate, bound=None), 'parse_token': gi.FunctionInfo(parse_token, bound=None), 'ref': gi.FunctionInfo(ref, bound=None), 'unref': gi.FunctionInfo(unref, bound=None)})"
    __gtype__ = None # (!) real value is '<GType GimpScanner (3595414624)>'
    __info__ = StructInfo(Scanner)


