# encoding: utf-8
# module gi.repository.AppStreamGlib
# from C:/Program Files/GIMP 3/lib/girepository-1.0\AppStreamGlib-1.0.typelib
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


class Image(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Image(**properties)
        new() -> AppStreamGlib.Image
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
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

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equal(self, image2): # real signature unknown; restored from __doc__
        """ equal(self, image2:AppStreamGlib.Image) -> bool """
        return False

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

    def get_basename(self): # real signature unknown; restored from __doc__
        """ get_basename(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> AppStreamGlib.ImageKind """
        pass

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str """
        return ""

    def get_md5(self): # real signature unknown; restored from __doc__
        """ get_md5(self) -> str """
        return ""

    def get_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_pixbuf(self) -> GdkPixbuf.Pixbuf """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> str """
        return ""

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

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

    def kind_from_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_from_string(kind:str) -> AppStreamGlib.ImageKind """
        pass

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:AppStreamGlib.ImageKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def load_filename(self, filename): # real signature unknown; restored from __doc__
        """ load_filename(self, filename:str) -> bool """
        return False

    def load_filename_full(self, filename, dest_size, src_size_min, flags): # real signature unknown; restored from __doc__
        """ load_filename_full(self, filename:str, dest_size:int, src_size_min:int, flags:AppStreamGlib.ImageLoadFlags) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> AppStreamGlib.Image """
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

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def save_filename(self, filename, width, height, flags): # real signature unknown; restored from __doc__
        """ save_filename(self, filename:str, width:int, height:int, flags:AppStreamGlib.ImageSaveFlags) -> bool """
        return False

    def save_pixbuf(self, width, height, flags): # real signature unknown; restored from __doc__
        """ save_pixbuf(self, width:int, height:int, flags:AppStreamGlib.ImageSaveFlags) -> GdkPixbuf.Pixbuf """
        pass

    def set_basename(self, basename): # real signature unknown; restored from __doc__
        """ set_basename(self, basename:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_height(self, height): # real signature unknown; restored from __doc__
        """ set_height(self, height:int) """
        pass

    def set_kind(self, kind): # real signature unknown; restored from __doc__
        """ set_kind(self, kind:AppStreamGlib.ImageKind) """
        pass

    def set_locale(self, locale): # real signature unknown; restored from __doc__
        """ set_locale(self, locale:str) """
        pass

    def set_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ set_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_url(self, url): # real signature unknown; restored from __doc__
        """ set_url(self, url:str) """
        pass

    def set_width(self, width): # real signature unknown; restored from __doc__
        """ set_width(self, width:int) """
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

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001afbef6ace0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Image), '__module__': 'gi.repository.AppStreamGlib', '__gtype__': <GType AsImage (3189455760)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'kind_from_string': gi.FunctionInfo(kind_from_string, bound=None), 'kind_to_string': gi.FunctionInfo(kind_to_string, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'get_basename': gi.FunctionInfo(get_basename, bound=None), 'get_height': gi.FunctionInfo(get_height, bound=None), 'get_kind': gi.FunctionInfo(get_kind, bound=None), 'get_locale': gi.FunctionInfo(get_locale, bound=None), 'get_md5': gi.FunctionInfo(get_md5, bound=None), 'get_pixbuf': gi.FunctionInfo(get_pixbuf, bound=None), 'get_url': gi.FunctionInfo(get_url, bound=None), 'get_width': gi.FunctionInfo(get_width, bound=None), 'load_filename': gi.FunctionInfo(load_filename, bound=None), 'load_filename_full': gi.FunctionInfo(load_filename_full, bound=None), 'save_filename': gi.FunctionInfo(save_filename, bound=None), 'save_pixbuf': gi.FunctionInfo(save_pixbuf, bound=None), 'set_basename': gi.FunctionInfo(set_basename, bound=None), 'set_height': gi.FunctionInfo(set_height, bound=None), 'set_kind': gi.FunctionInfo(set_kind, bound=None), 'set_locale': gi.FunctionInfo(set_locale, bound=None), 'set_pixbuf': gi.FunctionInfo(set_pixbuf, bound=None), 'set_url': gi.FunctionInfo(set_url, bound=None), 'set_width': gi.FunctionInfo(set_width, bound=None), 'parent_instance': <property object at 0x000001afbee9cea0>})"
    __gdoc__ = 'Object AsImage\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AsImage (3189455760)>'
    __info__ = ObjectInfo(Image)


