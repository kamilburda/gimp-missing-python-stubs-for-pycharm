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


class Scanner(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Scanner()
    """
    def cur_line(self): # real signature unknown; restored from __doc__
        """ cur_line(self) -> int """
        return 0

    def cur_position(self): # real signature unknown; restored from __doc__
        """ cur_position(self) -> int """
        return 0

    def cur_token(self): # real signature unknown; restored from __doc__
        """ cur_token(self) -> GLib.TokenType """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def eof(self): # real signature unknown; restored from __doc__
        """ eof(self) -> bool """
        return False

    def get_next_token(self): # real signature unknown; restored from __doc__
        """ get_next_token(self) -> GLib.TokenType """
        pass

    def input_file(self, input_fd): # real signature unknown; restored from __doc__
        """ input_file(self, input_fd:int) """
        pass

    def input_text(self, text, text_len): # real signature unknown; restored from __doc__
        """ input_text(self, text:str, text_len:int) """
        pass

    def lookup_symbol(self, symbol): # real signature unknown; restored from __doc__
        """ lookup_symbol(self, symbol:str) """
        pass

    def peek_next_token(self): # real signature unknown; restored from __doc__
        """ peek_next_token(self) -> GLib.TokenType """
        pass

    def scope_add_symbol(self, scope_id, symbol, value=None): # real signature unknown; restored from __doc__
        """ scope_add_symbol(self, scope_id:int, symbol:str, value=None) """
        pass

    def scope_foreach_symbol(self, scope_id, func, user_data=None): # real signature unknown; restored from __doc__
        """ scope_foreach_symbol(self, scope_id:int, func:GLib.HFunc, user_data=None) """
        pass

    def scope_lookup_symbol(self, scope_id, symbol): # real signature unknown; restored from __doc__
        """ scope_lookup_symbol(self, scope_id:int, symbol:str) """
        pass

    def scope_remove_symbol(self, scope_id, symbol): # real signature unknown; restored from __doc__
        """ scope_remove_symbol(self, scope_id:int, symbol:str) """
        pass

    def set_scope(self, scope_id): # real signature unknown; restored from __doc__
        """ set_scope(self, scope_id:int) -> int """
        return 0

    def sync_file_offset(self): # real signature unknown; restored from __doc__
        """ sync_file_offset(self) """
        pass

    def unexp_token(self, expected_token, identifier_spec, symbol_spec, symbol_name, message, is_error): # real signature unknown; restored from __doc__
        """ unexp_token(self, expected_token:GLib.TokenType, identifier_spec:str, symbol_spec:str, symbol_name:str, message:str, is_error:int) """
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

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input_fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_parse_errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    msg_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parse_errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scope_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    symbol_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Scanner), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Scanner' objects>, '__weakref__': <attribute '__weakref__' of 'Scanner' objects>, '__doc__': None, 'user_data': <property object at 0x000002830bef6660>, 'max_parse_errors': <property object at 0x000002830bef6750>, 'parse_errors': <property object at 0x000002830bef6840>, 'input_name': <property object at 0x000002830bef6930>, 'qdata': <property object at 0x000002830bef6a20>, 'config': <property object at 0x000002830bef6b10>, 'token': <property object at 0x000002830bef6c00>, 'value': <property object at 0x000002830bef6cf0>, 'line': <property object at 0x000002830bef6de0>, 'position': <property object at 0x000002830bef6ed0>, 'next_token': <property object at 0x000002830bef6fc0>, 'next_value': <property object at 0x000002830bef70b0>, 'next_line': <property object at 0x000002830bef71a0>, 'next_position': <property object at 0x000002830bef7290>, 'symbol_table': <property object at 0x000002830bef7380>, 'input_fd': <property object at 0x000002830bef7470>, 'text': <property object at 0x000002830bef7560>, 'text_end': <property object at 0x000002830bef7650>, 'buffer': <property object at 0x000002830bef7740>, 'scope_id': <property object at 0x000002830bef7830>, 'msg_handler': <property object at 0x000002830bef7920>, 'cur_line': gi.FunctionInfo(cur_line, bound=None), 'cur_position': gi.FunctionInfo(cur_position, bound=None), 'cur_token': gi.FunctionInfo(cur_token, bound=None), 'destroy': gi.FunctionInfo(destroy, bound=None), 'eof': gi.FunctionInfo(eof, bound=None), 'get_next_token': gi.FunctionInfo(get_next_token, bound=None), 'input_file': gi.FunctionInfo(input_file, bound=None), 'input_text': gi.FunctionInfo(input_text, bound=None), 'lookup_symbol': gi.FunctionInfo(lookup_symbol, bound=None), 'peek_next_token': gi.FunctionInfo(peek_next_token, bound=None), 'scope_add_symbol': gi.FunctionInfo(scope_add_symbol, bound=None), 'scope_foreach_symbol': gi.FunctionInfo(scope_foreach_symbol, bound=None), 'scope_lookup_symbol': gi.FunctionInfo(scope_lookup_symbol, bound=None), 'scope_remove_symbol': gi.FunctionInfo(scope_remove_symbol, bound=None), 'set_scope': gi.FunctionInfo(set_scope, bound=None), 'sync_file_offset': gi.FunctionInfo(sync_file_offset, bound=None), 'unexp_token': gi.FunctionInfo(unexp_token, bound=None)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Scanner)


