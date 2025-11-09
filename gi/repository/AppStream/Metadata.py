# encoding: utf-8
# module gi.repository.AppStream
# from C:/Program Files/GIMP 3/lib/girepository-1.0\AppStream-1.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi


class Metadata(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Metadata(**properties)
        new() -> AppStream.Metadata
    """
    def add_component(self, cpt): # real signature unknown; restored from __doc__
        """ add_component(self, cpt:AppStream.Component) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_components(self): # real signature unknown; restored from __doc__
        """ clear_components(self) """
        pass

    def clear_releases(self): # real signature unknown; restored from __doc__
        """ clear_releases(self) """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def components_to_catalog(self, format): # real signature unknown; restored from __doc__
        """ components_to_catalog(self, format:AppStream.FormatKind) -> str """
        return ""

    def component_to_metainfo(self, format): # real signature unknown; restored from __doc__
        """ component_to_metainfo(self, format:AppStream.FormatKind) -> str """
        return ""

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, connect_flags=0): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def file_guess_style(self, filename): # real signature unknown; restored from __doc__
        """ file_guess_style(filename:str) -> AppStream.FormatStyle """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_architecture(self): # real signature unknown; restored from __doc__
        """ get_architecture(self) -> str """
        return ""

    def get_component(self): # real signature unknown; restored from __doc__
        """ get_component(self) -> AppStream.Component or None """
        pass

    def get_components(self): # real signature unknown; restored from __doc__
        """ get_components(self) -> AppStream.ComponentBox """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_format_style(self): # real signature unknown; restored from __doc__
        """ get_format_style(self) -> AppStream.FormatStyle """
        pass

    def get_format_version(self): # real signature unknown; restored from __doc__
        """ get_format_version(self) -> AppStream.FormatVersion """
        pass

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str """
        return ""

    def get_media_baseurl(self): # real signature unknown; restored from __doc__
        """ get_media_baseurl(self) -> str """
        return ""

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> str """
        return ""

    def get_parse_flags(self): # real signature unknown; restored from __doc__
        """ get_parse_flags(self) -> AppStream.ParseFlags """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_release_list(self): # real signature unknown; restored from __doc__
        """ get_release_list(self) -> AppStream.ReleaseList or None """
        pass

    def get_release_lists(self): # real signature unknown; restored from __doc__
        """ get_release_lists(self) -> list """
        return []

    def get_update_existing(self): # real signature unknown; restored from __doc__
        """ get_update_existing(self) -> bool """
        return False

    def get_write_header(self): # real signature unknown; restored from __doc__
        """ get_write_header(self) -> bool """
        return False

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> AppStream.Metadata """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def parse_bytes(self, bytes, format): # real signature unknown; restored from __doc__
        """ parse_bytes(self, bytes:GLib.Bytes, format:AppStream.FormatKind) -> bool """
        return False

    def parse_data(self, data, data_len, format): # real signature unknown; restored from __doc__
        """ parse_data(self, data:str, data_len:int, format:AppStream.FormatKind) -> bool """
        return False

    def parse_desktop_data(self, cid, data, data_len): # real signature unknown; restored from __doc__
        """ parse_desktop_data(self, cid:str, data:str, data_len:int) -> bool """
        return False

    def parse_file(self, file, format): # real signature unknown; restored from __doc__
        """ parse_file(self, file:Gio.File, format:AppStream.FormatKind) -> bool """
        return False

    def parse_releases_bytes(self, bytes): # real signature unknown; restored from __doc__
        """ parse_releases_bytes(self, bytes:GLib.Bytes) -> bool """
        return False

    def parse_releases_file(self, file): # real signature unknown; restored from __doc__
        """ parse_releases_file(self, file:Gio.File) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def releases_to_data(self, releases): # real signature unknown; restored from __doc__
        """ releases_to_data(self, releases:AppStream.ReleaseList) -> str """
        return ""

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def save_catalog(self, fname, format): # real signature unknown; restored from __doc__
        """ save_catalog(self, fname:str, format:AppStream.FormatKind) -> bool """
        return False

    def save_metainfo(self, fname, format): # real signature unknown; restored from __doc__
        """ save_metainfo(self, fname:str, format:AppStream.FormatKind) -> bool """
        return False

    def set_architecture(self, arch): # real signature unknown; restored from __doc__
        """ set_architecture(self, arch:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_format_style(self, mode): # real signature unknown; restored from __doc__
        """ set_format_style(self, mode:AppStream.FormatStyle) """
        pass

    def set_format_version(self, version): # real signature unknown; restored from __doc__
        """ set_format_version(self, version:AppStream.FormatVersion) """
        pass

    def set_locale(self, locale): # real signature unknown; restored from __doc__
        """ set_locale(self, locale:str) """
        pass

    def set_media_baseurl(self, url): # real signature unknown; restored from __doc__
        """ set_media_baseurl(self, url:str) """
        pass

    def set_origin(self, origin): # real signature unknown; restored from __doc__
        """ set_origin(self, origin:str) """
        pass

    def set_parse_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_parse_flags(self, flags:AppStream.ParseFlags) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_update_existing(self, update): # real signature unknown; restored from __doc__
        """ set_update_existing(self, update:bool) """
        pass

    def set_write_header(self, wheader): # real signature unknown; restored from __doc__
        """ set_write_header(self, wheader:bool) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self): # reliably restored by inspect
        """ Deprecated, do not explicitly float GObjects. """
        pass

    def _ref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _ref_sink(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ecec6c9c30>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Metadata), '__module__': 'gi.repository.AppStream', '__gtype__': <GType AsMetadata (3928804288)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'file_guess_style': <staticmethod(gi.FunctionInfo(file_guess_style))>, 'add_component': gi.FunctionInfo(add_component), 'clear_components': gi.FunctionInfo(clear_components), 'clear_releases': gi.FunctionInfo(clear_releases), 'component_to_metainfo': gi.FunctionInfo(component_to_metainfo), 'components_to_catalog': gi.FunctionInfo(components_to_catalog), 'get_architecture': gi.FunctionInfo(get_architecture), 'get_component': gi.FunctionInfo(get_component), 'get_components': gi.FunctionInfo(get_components), 'get_format_style': gi.FunctionInfo(get_format_style), 'get_format_version': gi.FunctionInfo(get_format_version), 'get_locale': gi.FunctionInfo(get_locale), 'get_media_baseurl': gi.FunctionInfo(get_media_baseurl), 'get_origin': gi.FunctionInfo(get_origin), 'get_parse_flags': gi.FunctionInfo(get_parse_flags), 'get_release_list': gi.FunctionInfo(get_release_list), 'get_release_lists': gi.FunctionInfo(get_release_lists), 'get_update_existing': gi.FunctionInfo(get_update_existing), 'get_write_header': gi.FunctionInfo(get_write_header), 'parse_bytes': gi.FunctionInfo(parse_bytes), 'parse_data': gi.FunctionInfo(parse_data), 'parse_desktop_data': gi.FunctionInfo(parse_desktop_data), 'parse_file': gi.FunctionInfo(parse_file), 'parse_releases_bytes': gi.FunctionInfo(parse_releases_bytes), 'parse_releases_file': gi.FunctionInfo(parse_releases_file), 'releases_to_data': gi.FunctionInfo(releases_to_data), 'save_catalog': gi.FunctionInfo(save_catalog), 'save_metainfo': gi.FunctionInfo(save_metainfo), 'set_architecture': gi.FunctionInfo(set_architecture), 'set_format_style': gi.FunctionInfo(set_format_style), 'set_format_version': gi.FunctionInfo(set_format_version), 'set_locale': gi.FunctionInfo(set_locale), 'set_media_baseurl': gi.FunctionInfo(set_media_baseurl), 'set_origin': gi.FunctionInfo(set_origin), 'set_parse_flags': gi.FunctionInfo(set_parse_flags), 'set_update_existing': gi.FunctionInfo(set_update_existing), 'set_write_header': gi.FunctionInfo(set_write_header), 'parent_instance': <property object at 0x000001ecec6d5ee0>})"
    __gdoc__ = 'Object AsMetadata\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AsMetadata (3928804288)>'
    __info__ = ObjectInfo(Metadata)


