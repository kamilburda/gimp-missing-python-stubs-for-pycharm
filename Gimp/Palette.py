# encoding: utf-8
# module gi.repository.Gimp
# from C:\Program Files\GIMP 3\lib\girepository-1.0\Gimp-3.0.typelib
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


from .Resource import Resource

class Palette(Resource):
    """
    :Constructors:
    
    ::
    
        Palette(**properties)
        new(name:str) -> Gimp.Palette
    """
    def add_entry(self, entry_name, color): # real signature unknown; restored from __doc__
        """ add_entry(self, entry_name:str, color:Gegl.Color) -> bool, entry_num:int """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def build_data_path(self, name): # real signature unknown; restored from __doc__
        """ build_data_path(name:str) -> str """
        return ""

    def build_plug_in_path(self, name): # real signature unknown; restored from __doc__
        """ build_plug_in_path(name:str) -> str """
        return ""

    def build_system_path(self, name): # real signature unknown; restored from __doc__
        """ build_system_path(name:str) -> str """
        return ""

    def build_writable_path(self, name): # real signature unknown; restored from __doc__
        """ build_writable_path(name:str) -> str """
        return ""

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

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) -> bool """
        return False

    def delete_entry(self, entry_num): # real signature unknown; restored from __doc__
        """ delete_entry(self, entry_num:int) -> bool """
        return False

    def deserialize_return(self, scanner, expected_token, nest_level): # real signature unknown; restored from __doc__
        """ deserialize_return(scanner:GLib.Scanner, expected_token:GLib.TokenType, nest_level:int) -> bool """
        return False

    def diff(self, a, b, flags): # real signature unknown; restored from __doc__
        """ diff(a:GObject.Object, b:GObject.Object, flags:GObject.ParamFlags) -> list """
        return []

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) -> Gimp.Resource """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

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

    def get_by_id(self, resource_id): # real signature unknown; restored from __doc__
        """ get_by_id(resource_id:int) -> Gimp.Resource or None """
        pass

    def get_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_by_name(name:str) -> Gimp.Palette or None """
        pass

    def get_colormap(self, format): # real signature unknown; restored from __doc__
        """ get_colormap(self, format:Babl.Object) -> list, num_colors:int """
        return []

    def get_colors(self): # real signature unknown; restored from __doc__
        """ get_colors(self) -> list """
        return []

    def get_color_count(self): # real signature unknown; restored from __doc__
        """ get_color_count(self) -> int """
        return 0

    def get_columns(self): # real signature unknown; restored from __doc__
        """ get_columns(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_entry_color(self, entry_num): # real signature unknown; restored from __doc__
        """ get_entry_color(self, entry_num:int) -> Gegl.Color """
        pass

    def get_entry_name(self, entry_num): # real signature unknown; restored from __doc__
        """ get_entry_name(self, entry_num:int) -> bool, entry_name:str """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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

    def id_is_brush(self, resource_id): # real signature unknown; restored from __doc__
        """ id_is_brush(resource_id:int) -> bool """
        return False

    def id_is_font(self, resource_id): # real signature unknown; restored from __doc__
        """ id_is_font(resource_id:int) -> bool """
        return False

    def id_is_gradient(self, resource_id): # real signature unknown; restored from __doc__
        """ id_is_gradient(resource_id:int) -> bool """
        return False

    def id_is_palette(self, resource_id): # real signature unknown; restored from __doc__
        """ id_is_palette(resource_id:int) -> bool """
        return False

    def id_is_pattern(self, resource_id): # real signature unknown; restored from __doc__
        """ id_is_pattern(resource_id:int) -> bool """
        return False

    def id_is_valid(self, resource_id): # real signature unknown; restored from __doc__
        """ id_is_valid(resource_id:int) -> bool """
        return False

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

    def is_brush(self): # real signature unknown; restored from __doc__
        """ is_brush(self) -> bool """
        return False

    def is_editable(self): # real signature unknown; restored from __doc__
        """ is_editable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_font(self): # real signature unknown; restored from __doc__
        """ is_font(self) -> bool """
        return False

    def is_gradient(self): # real signature unknown; restored from __doc__
        """ is_gradient(self) -> bool """
        return False

    def is_palette(self): # real signature unknown; restored from __doc__
        """ is_palette(self) -> bool """
        return False

    def is_pattern(self): # real signature unknown; restored from __doc__
        """ is_pattern(self) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def new(self, name): # real signature unknown; restored from __doc__
        """ new(name:str) -> Gimp.Palette """
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

    def param_spec_duplicate(self, pspec): # real signature unknown; restored from __doc__
        """ param_spec_duplicate(pspec:GObject.ParamSpec) -> GObject.ParamSpec """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def rename(self, new_name): # real signature unknown; restored from __doc__
        """ rename(self, new_name:str) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_properties(self, p_object): # real signature unknown; restored from __doc__
        """ reset_properties(object:GObject.Object) """
        pass

    def reset_property(self, p_object, property_name): # real signature unknown; restored from __doc__
        """ reset_property(object:GObject.Object, property_name:str) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def serialize_value(self, value, p_str, escaped): # real signature unknown; restored from __doc__
        """ serialize_value(value:GObject.Value, str:GLib.String, escaped:bool) -> bool """
        return False

    def set_colormap(self, format, colormap, num_bytes): # real signature unknown; restored from __doc__
        """ set_colormap(self, format:Babl.Object, colormap:int, num_bytes:int) -> bool """
        return False

    def set_columns(self, columns): # real signature unknown; restored from __doc__
        """ set_columns(self, columns:int) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_entry_color(self, entry_num, color): # real signature unknown; restored from __doc__
        """ set_entry_color(self, entry_num:int, color:Gegl.Color) -> bool """
        return False

    def set_entry_name(self, entry_num, entry_name): # real signature unknown; restored from __doc__
        """ set_entry_name(self, entry_num:int, entry_name:str) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    def string_append_escaped(self, string, val): # real signature unknown; restored from __doc__
        """ string_append_escaped(string:GLib.String, val:str) """
        pass

    def sync(self, src, dest, flags): # real signature unknown; restored from __doc__
        """ sync(src:GObject.Object, dest:GObject.Object, flags:GObject.ParamFlags) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def type_register(self, parent_type, type_name, pspecs): # real signature unknown; restored from __doc__
        """ type_register(parent_type:GType, type_name:str, pspecs:list) -> GType """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001b64069e050>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Palette), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpPalette (1069009792)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'get_by_name': gi.FunctionInfo(get_by_name, bound=None), 'add_entry': gi.FunctionInfo(add_entry, bound=None), 'delete_entry': gi.FunctionInfo(delete_entry, bound=None), 'get_color_count': gi.FunctionInfo(get_color_count, bound=None), 'get_colormap': gi.FunctionInfo(get_colormap, bound=None), 'get_colors': gi.FunctionInfo(get_colors, bound=None), 'get_columns': gi.FunctionInfo(get_columns, bound=None), 'get_entry_color': gi.FunctionInfo(get_entry_color, bound=None), 'get_entry_name': gi.FunctionInfo(get_entry_name, bound=None), 'set_colormap': gi.FunctionInfo(set_colormap, bound=None), 'set_columns': gi.FunctionInfo(set_columns, bound=None), 'set_entry_color': gi.FunctionInfo(set_entry_color, bound=None), 'set_entry_name': gi.FunctionInfo(set_entry_name, bound=None)})"
    __gdoc__ = 'Object GimpPalette\n\nProperties from GimpResource:\n  id -> gint: The id\n    The id for internal use\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpPalette (1069009792)>'
    __info__ = ObjectInfo(Palette)


