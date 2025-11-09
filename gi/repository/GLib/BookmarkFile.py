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


class BookmarkFile(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> GLib.BookmarkFile
    """
    def add_application(self, uri, name=None, exec=None): # real signature unknown; restored from __doc__
        """ add_application(self, uri:str, name:str=None, exec:str=None) """
        pass

    def add_group(self, uri, group): # real signature unknown; restored from __doc__
        """ add_group(self, uri:str, group:str) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GLib.BookmarkFile """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_added(self, uri): # real signature unknown; restored from __doc__
        """ get_added(self, uri:str) -> int """
        return 0

    def get_added_date_time(self, uri): # real signature unknown; restored from __doc__
        """ get_added_date_time(self, uri:str) -> GLib.DateTime """
        pass

    def get_applications(self, uri): # real signature unknown; restored from __doc__
        """ get_applications(self, uri:str) -> list """
        return []

    def get_application_info(self, uri, name): # real signature unknown; restored from __doc__
        """ get_application_info(self, uri:str, name:str) -> bool, exec:str, count:int, stamp:GLib.DateTime """
        return False

    def get_app_info(self, uri, name): # real signature unknown; restored from __doc__
        """ get_app_info(self, uri:str, name:str) -> bool, exec:str, count:int, stamp:int """
        return False

    def get_description(self, uri): # real signature unknown; restored from __doc__
        """ get_description(self, uri:str) -> str """
        return ""

    def get_groups(self, uri): # real signature unknown; restored from __doc__
        """ get_groups(self, uri:str) -> list """
        return []

    def get_icon(self, uri): # real signature unknown; restored from __doc__
        """ get_icon(self, uri:str) -> bool, href:str, mime_type:str """
        return False

    def get_is_private(self, uri): # real signature unknown; restored from __doc__
        """ get_is_private(self, uri:str) -> bool """
        return False

    def get_mime_type(self, uri): # real signature unknown; restored from __doc__
        """ get_mime_type(self, uri:str) -> str """
        return ""

    def get_modified(self, uri): # real signature unknown; restored from __doc__
        """ get_modified(self, uri:str) -> int """
        return 0

    def get_modified_date_time(self, uri): # real signature unknown; restored from __doc__
        """ get_modified_date_time(self, uri:str) -> GLib.DateTime """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_title(self, uri=None): # real signature unknown; restored from __doc__
        """ get_title(self, uri:str=None) -> str """
        return ""

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list """
        return []

    def get_visited(self, uri): # real signature unknown; restored from __doc__
        """ get_visited(self, uri:str) -> int """
        return 0

    def get_visited_date_time(self, uri): # real signature unknown; restored from __doc__
        """ get_visited_date_time(self, uri:str) -> GLib.DateTime """
        pass

    def has_application(self, uri, name): # real signature unknown; restored from __doc__
        """ has_application(self, uri:str, name:str) -> bool """
        return False

    def has_group(self, uri, group): # real signature unknown; restored from __doc__
        """ has_group(self, uri:str, group:str) -> bool """
        return False

    def has_item(self, uri): # real signature unknown; restored from __doc__
        """ has_item(self, uri:str) -> bool """
        return False

    def load_from_data(self, data): # real signature unknown; restored from __doc__
        """ load_from_data(self, data:list) -> bool """
        return False

    def load_from_data_dirs(self, file): # real signature unknown; restored from __doc__
        """ load_from_data_dirs(self, file:str) -> bool, full_path:str """
        return False

    def load_from_file(self, filename): # real signature unknown; restored from __doc__
        """ load_from_file(self, filename:str) -> bool """
        return False

    def move_item(self, old_uri, new_uri=None): # real signature unknown; restored from __doc__
        """ move_item(self, old_uri:str, new_uri:str=None) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GLib.BookmarkFile """
        pass

    def remove_application(self, uri, name): # real signature unknown; restored from __doc__
        """ remove_application(self, uri:str, name:str) -> bool """
        return False

    def remove_group(self, uri, group): # real signature unknown; restored from __doc__
        """ remove_group(self, uri:str, group:str) -> bool """
        return False

    def remove_item(self, uri): # real signature unknown; restored from __doc__
        """ remove_item(self, uri:str) -> bool """
        return False

    def set_added(self, uri, added): # real signature unknown; restored from __doc__
        """ set_added(self, uri:str, added:int) """
        pass

    def set_added_date_time(self, uri, added): # real signature unknown; restored from __doc__
        """ set_added_date_time(self, uri:str, added:GLib.DateTime) """
        pass

    def set_application_info(self, uri, name, exec, count, stamp=None): # real signature unknown; restored from __doc__
        """ set_application_info(self, uri:str, name:str, exec:str, count:int, stamp:GLib.DateTime=None) -> bool """
        return False

    def set_app_info(self, uri, name, exec, count, stamp): # real signature unknown; restored from __doc__
        """ set_app_info(self, uri:str, name:str, exec:str, count:int, stamp:int) -> bool """
        return False

    def set_description(self, uri=None, description): # real signature unknown; restored from __doc__
        """ set_description(self, uri:str=None, description:str) """
        pass

    def set_groups(self, uri, groups=None): # real signature unknown; restored from __doc__
        """ set_groups(self, uri:str, groups:list=None) """
        pass

    def set_icon(self, uri, href=None, mime_type): # real signature unknown; restored from __doc__
        """ set_icon(self, uri:str, href:str=None, mime_type:str) """
        pass

    def set_is_private(self, uri, is_private): # real signature unknown; restored from __doc__
        """ set_is_private(self, uri:str, is_private:bool) """
        pass

    def set_mime_type(self, uri, mime_type): # real signature unknown; restored from __doc__
        """ set_mime_type(self, uri:str, mime_type:str) """
        pass

    def set_modified(self, uri, modified): # real signature unknown; restored from __doc__
        """ set_modified(self, uri:str, modified:int) """
        pass

    def set_modified_date_time(self, uri, modified): # real signature unknown; restored from __doc__
        """ set_modified_date_time(self, uri:str, modified:GLib.DateTime) """
        pass

    def set_title(self, uri=None, title): # real signature unknown; restored from __doc__
        """ set_title(self, uri:str=None, title:str) """
        pass

    def set_visited(self, uri, visited): # real signature unknown; restored from __doc__
        """ set_visited(self, uri:str, visited:int) """
        pass

    def set_visited_date_time(self, uri, visited): # real signature unknown; restored from __doc__
        """ set_visited_date_time(self, uri:str, visited:GLib.DateTime) """
        pass

    def to_data(self): # real signature unknown; restored from __doc__
        """ to_data(self) -> list """
        return []

    def to_file(self, filename): # real signature unknown; restored from __doc__
        """ to_file(self, filename:str) -> bool """
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
        """ new() -> GLib.BookmarkFile """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookmarkFile), '__module__': 'gi.repository.GLib', '__gtype__': <GType GBookmarkFile (155711344)>, '__dict__': <attribute '__dict__' of 'BookmarkFile' objects>, '__weakref__': <attribute '__weakref__' of 'BookmarkFile' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'add_application': gi.FunctionInfo(add_application, bound=None), 'add_group': gi.FunctionInfo(add_group, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_added': gi.FunctionInfo(get_added, bound=None), 'get_added_date_time': gi.FunctionInfo(get_added_date_time, bound=None), 'get_app_info': gi.FunctionInfo(get_app_info, bound=None), 'get_application_info': gi.FunctionInfo(get_application_info, bound=None), 'get_applications': gi.FunctionInfo(get_applications, bound=None), 'get_description': gi.FunctionInfo(get_description, bound=None), 'get_groups': gi.FunctionInfo(get_groups, bound=None), 'get_icon': gi.FunctionInfo(get_icon, bound=None), 'get_is_private': gi.FunctionInfo(get_is_private, bound=None), 'get_mime_type': gi.FunctionInfo(get_mime_type, bound=None), 'get_modified': gi.FunctionInfo(get_modified, bound=None), 'get_modified_date_time': gi.FunctionInfo(get_modified_date_time, bound=None), 'get_size': gi.FunctionInfo(get_size, bound=None), 'get_title': gi.FunctionInfo(get_title, bound=None), 'get_uris': gi.FunctionInfo(get_uris, bound=None), 'get_visited': gi.FunctionInfo(get_visited, bound=None), 'get_visited_date_time': gi.FunctionInfo(get_visited_date_time, bound=None), 'has_application': gi.FunctionInfo(has_application, bound=None), 'has_group': gi.FunctionInfo(has_group, bound=None), 'has_item': gi.FunctionInfo(has_item, bound=None), 'load_from_data': gi.FunctionInfo(load_from_data, bound=None), 'load_from_data_dirs': gi.FunctionInfo(load_from_data_dirs, bound=None), 'load_from_file': gi.FunctionInfo(load_from_file, bound=None), 'move_item': gi.FunctionInfo(move_item, bound=None), 'remove_application': gi.FunctionInfo(remove_application, bound=None), 'remove_group': gi.FunctionInfo(remove_group, bound=None), 'remove_item': gi.FunctionInfo(remove_item, bound=None), 'set_added': gi.FunctionInfo(set_added, bound=None), 'set_added_date_time': gi.FunctionInfo(set_added_date_time, bound=None), 'set_app_info': gi.FunctionInfo(set_app_info, bound=None), 'set_application_info': gi.FunctionInfo(set_application_info, bound=None), 'set_description': gi.FunctionInfo(set_description, bound=None), 'set_groups': gi.FunctionInfo(set_groups, bound=None), 'set_icon': gi.FunctionInfo(set_icon, bound=None), 'set_is_private': gi.FunctionInfo(set_is_private, bound=None), 'set_mime_type': gi.FunctionInfo(set_mime_type, bound=None), 'set_modified': gi.FunctionInfo(set_modified, bound=None), 'set_modified_date_time': gi.FunctionInfo(set_modified_date_time, bound=None), 'set_title': gi.FunctionInfo(set_title, bound=None), 'set_visited': gi.FunctionInfo(set_visited, bound=None), 'set_visited_date_time': gi.FunctionInfo(set_visited_date_time, bound=None), 'to_data': gi.FunctionInfo(to_data, bound=None), 'to_file': gi.FunctionInfo(to_file, bound=None), 'error_quark': gi.FunctionInfo(error_quark, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000002830be60720>})"
    __gtype__ = None # (!) real value is '<GType GBookmarkFile (155711344)>'
    __info__ = StructInfo(BookmarkFile)


