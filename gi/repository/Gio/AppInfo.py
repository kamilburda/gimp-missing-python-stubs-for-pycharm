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


class AppInfo(__gobject.GInterface):
    # no doc
    def add_supports_type(self, content_type): # real signature unknown; restored from __doc__
        """ add_supports_type(self, content_type:str) -> bool """
        return False

    def can_delete(self): # real signature unknown; restored from __doc__
        """ can_delete(self) -> bool """
        return False

    def can_remove_supports_type(self): # real signature unknown; restored from __doc__
        """ can_remove_supports_type(self) -> bool """
        return False

    def create_from_commandline(self, commandline, application_name=None, flags): # real signature unknown; restored from __doc__
        """ create_from_commandline(commandline:str, application_name:str=None, flags:Gio.AppInfoCreateFlags) -> Gio.AppInfo """
        pass

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) -> bool """
        return False

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gio.AppInfo """
        pass

    def equal(self, appinfo2): # real signature unknown; restored from __doc__
        """ equal(self, appinfo2:Gio.AppInfo) -> bool """
        return False

    def get_all(self): # real signature unknown; restored from __doc__
        """ get_all() -> list """
        return []

    def get_all_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ get_all_for_type(content_type:str) -> list """
        return []

    def get_commandline(self): # real signature unknown; restored from __doc__
        """ get_commandline(self) -> str or None """
        return ""

    def get_default_for_type(self, content_type, must_support_uris): # real signature unknown; restored from __doc__
        """ get_default_for_type(content_type:str, must_support_uris:bool) -> Gio.AppInfo or None """
        pass

    def get_default_for_type_async(self, content_type, must_support_uris, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_default_for_type_async(content_type:str, must_support_uris:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_default_for_type_finish(self, result): # real signature unknown; restored from __doc__
        """ get_default_for_type_finish(result:Gio.AsyncResult) -> Gio.AppInfo """
        pass

    def get_default_for_uri_scheme(self, uri_scheme): # real signature unknown; restored from __doc__
        """ get_default_for_uri_scheme(uri_scheme:str) -> Gio.AppInfo or None """
        pass

    def get_default_for_uri_scheme_async(self, uri_scheme, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_default_for_uri_scheme_async(uri_scheme:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_default_for_uri_scheme_finish(self, result): # real signature unknown; restored from __doc__
        """ get_default_for_uri_scheme_finish(result:Gio.AsyncResult) -> Gio.AppInfo """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str or None """
        return ""

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_executable(self): # real signature unknown; restored from __doc__
        """ get_executable(self) -> str """
        return ""

    def get_fallback_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ get_fallback_for_type(content_type:str) -> list """
        return []

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon or None """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str or None """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_recommended_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ get_recommended_for_type(content_type:str) -> list """
        return []

    def get_supported_types(self): # real signature unknown; restored from __doc__
        """ get_supported_types(self) -> list """
        return []

    def launch(self, files=None, context=None): # real signature unknown; restored from __doc__
        """ launch(self, files:list=None, context:Gio.AppLaunchContext=None) -> bool """
        return False

    def launch_default_for_uri(self, uri, context=None): # real signature unknown; restored from __doc__
        """ launch_default_for_uri(uri:str, context:Gio.AppLaunchContext=None) -> bool """
        return False

    def launch_default_for_uri_async(self, uri, context=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ launch_default_for_uri_async(uri:str, context:Gio.AppLaunchContext=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def launch_default_for_uri_finish(self, result): # real signature unknown; restored from __doc__
        """ launch_default_for_uri_finish(result:Gio.AsyncResult) -> bool """
        return False

    def launch_uris(self, uris=None, context=None): # real signature unknown; restored from __doc__
        """ launch_uris(self, uris:list=None, context:Gio.AppLaunchContext=None) -> bool """
        return False

    def launch_uris_async(self, uris=None, context=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ launch_uris_async(self, uris:list=None, context:Gio.AppLaunchContext=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def launch_uris_finish(self, result): # real signature unknown; restored from __doc__
        """ launch_uris_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_supports_type(self, content_type): # real signature unknown; restored from __doc__
        """ remove_supports_type(self, content_type:str) -> bool """
        return False

    def reset_type_associations(self, content_type): # real signature unknown; restored from __doc__
        """ reset_type_associations(content_type:str) """
        pass

    def set_as_default_for_extension(self, extension): # real signature unknown; restored from __doc__
        """ set_as_default_for_extension(self, extension:str) -> bool """
        return False

    def set_as_default_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ set_as_default_for_type(self, content_type:str) -> bool """
        return False

    def set_as_last_used_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ set_as_last_used_for_type(self, content_type:str) -> bool """
        return False

    def should_show(self): # real signature unknown; restored from __doc__
        """ should_show(self) -> bool """
        return False

    def supports_files(self): # real signature unknown; restored from __doc__
        """ supports_files(self) -> bool """
        return False

    def supports_uris(self): # real signature unknown; restored from __doc__
        """ supports_uris(self) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(AppInfo), '__module__': 'gi.repository.Gio', '__gtype__': <GType GAppInfo (2472614848)>, '__dict__': <attribute '__dict__' of 'AppInfo' objects>, '__weakref__': <attribute '__weakref__' of 'AppInfo' objects>, '__doc__': None, '__gsignals__': {}, 'create_from_commandline': gi.FunctionInfo(create_from_commandline, bound=None), 'get_all': gi.FunctionInfo(get_all, bound=None), 'get_all_for_type': gi.FunctionInfo(get_all_for_type, bound=None), 'get_default_for_type': gi.FunctionInfo(get_default_for_type, bound=None), 'get_default_for_type_async': gi.FunctionInfo(get_default_for_type_async, bound=None), 'get_default_for_type_finish': gi.FunctionInfo(get_default_for_type_finish, bound=None), 'get_default_for_uri_scheme': gi.FunctionInfo(get_default_for_uri_scheme, bound=None), 'get_default_for_uri_scheme_async': gi.FunctionInfo(get_default_for_uri_scheme_async, bound=None), 'get_default_for_uri_scheme_finish': gi.FunctionInfo(get_default_for_uri_scheme_finish, bound=None), 'get_fallback_for_type': gi.FunctionInfo(get_fallback_for_type, bound=None), 'get_recommended_for_type': gi.FunctionInfo(get_recommended_for_type, bound=None), 'launch_default_for_uri': gi.FunctionInfo(launch_default_for_uri, bound=None), 'launch_default_for_uri_async': gi.FunctionInfo(launch_default_for_uri_async, bound=None), 'launch_default_for_uri_finish': gi.FunctionInfo(launch_default_for_uri_finish, bound=None), 'reset_type_associations': gi.FunctionInfo(reset_type_associations, bound=None), 'add_supports_type': gi.FunctionInfo(add_supports_type, bound=None), 'can_delete': gi.FunctionInfo(can_delete, bound=None), 'can_remove_supports_type': gi.FunctionInfo(can_remove_supports_type, bound=None), 'delete': gi.FunctionInfo(delete, bound=None), 'dup': gi.FunctionInfo(dup, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'get_commandline': gi.FunctionInfo(get_commandline, bound=None), 'get_description': gi.FunctionInfo(get_description, bound=None), 'get_display_name': gi.FunctionInfo(get_display_name, bound=None), 'get_executable': gi.FunctionInfo(get_executable, bound=None), 'get_icon': gi.FunctionInfo(get_icon, bound=None), 'get_id': gi.FunctionInfo(get_id, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'get_supported_types': gi.FunctionInfo(get_supported_types, bound=None), 'launch': gi.FunctionInfo(launch, bound=None), 'launch_uris': gi.FunctionInfo(launch_uris, bound=None), 'launch_uris_async': gi.FunctionInfo(launch_uris_async, bound=None), 'launch_uris_finish': gi.FunctionInfo(launch_uris_finish, bound=None), 'remove_supports_type': gi.FunctionInfo(remove_supports_type, bound=None), 'set_as_default_for_extension': gi.FunctionInfo(set_as_default_for_extension, bound=None), 'set_as_default_for_type': gi.FunctionInfo(set_as_default_for_type, bound=None), 'set_as_last_used_for_type': gi.FunctionInfo(set_as_last_used_for_type, bound=None), 'should_show': gi.FunctionInfo(should_show, bound=None), 'supports_files': gi.FunctionInfo(supports_files, bound=None), 'supports_uris': gi.FunctionInfo(supports_uris, bound=None)})"
    __gdoc__ = 'Interface GAppInfo\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GAppInfo (2472614848)>'
    __info__ = InterfaceInfo(AppInfo)


