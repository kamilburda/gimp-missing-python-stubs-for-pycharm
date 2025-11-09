# encoding: utf-8
# module gi.repository.Gtk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class PrintSettings(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        PrintSettings(**properties)
        new() -> Gtk.PrintSettings
        new_from_file(file_name:str) -> Gtk.PrintSettings
        new_from_gvariant(variant:GLib.Variant) -> Gtk.PrintSettings
        new_from_key_file(key_file:GLib.KeyFile, group_name:str=None) -> Gtk.PrintSettings
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

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.PrintSettings """
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

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gtk.PrintSettingsFunc, user_data=None) """
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

    def get(self, key): # real signature unknown; restored from __doc__
        """ get(self, key:str) -> str """
        return ""

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_bool(self, key): # real signature unknown; restored from __doc__
        """ get_bool(self, key:str) -> bool """
        return False

    def get_collate(self): # real signature unknown; restored from __doc__
        """ get_collate(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_source(self): # real signature unknown; restored from __doc__
        """ get_default_source(self) -> str """
        return ""

    def get_dither(self): # real signature unknown; restored from __doc__
        """ get_dither(self) -> str """
        return ""

    def get_double(self, key): # real signature unknown; restored from __doc__
        """ get_double(self, key:str) -> float """
        return 0.0

    def get_double_with_default(self, key, def_): # real signature unknown; restored from __doc__
        """ get_double_with_default(self, key:str, def_:float) -> float """
        return 0.0

    def get_duplex(self): # real signature unknown; restored from __doc__
        """ get_duplex(self) -> Gtk.PrintDuplex """
        pass

    def get_finishings(self): # real signature unknown; restored from __doc__
        """ get_finishings(self) -> str """
        return ""

    def get_int(self, key): # real signature unknown; restored from __doc__
        """ get_int(self, key:str) -> int """
        return 0

    def get_int_with_default(self, key, def_): # real signature unknown; restored from __doc__
        """ get_int_with_default(self, key:str, def_:int) -> int """
        return 0

    def get_length(self, key, unit): # real signature unknown; restored from __doc__
        """ get_length(self, key:str, unit:Gtk.Unit) -> float """
        return 0.0

    def get_media_type(self): # real signature unknown; restored from __doc__
        """ get_media_type(self) -> str """
        return ""

    def get_number_up(self): # real signature unknown; restored from __doc__
        """ get_number_up(self) -> int """
        return 0

    def get_number_up_layout(self): # real signature unknown; restored from __doc__
        """ get_number_up_layout(self) -> Gtk.NumberUpLayout """
        pass

    def get_n_copies(self): # real signature unknown; restored from __doc__
        """ get_n_copies(self) -> int """
        return 0

    def get_orientation(self): # real signature unknown; restored from __doc__
        """ get_orientation(self) -> Gtk.PageOrientation """
        pass

    def get_output_bin(self): # real signature unknown; restored from __doc__
        """ get_output_bin(self) -> str """
        return ""

    def get_page_ranges(self): # real signature unknown; restored from __doc__
        """ get_page_ranges(self) -> list """
        return []

    def get_page_set(self): # real signature unknown; restored from __doc__
        """ get_page_set(self) -> Gtk.PageSet """
        pass

    def get_paper_height(self, unit): # real signature unknown; restored from __doc__
        """ get_paper_height(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_paper_size(self): # real signature unknown; restored from __doc__
        """ get_paper_size(self) -> Gtk.PaperSize """
        pass

    def get_paper_width(self, unit): # real signature unknown; restored from __doc__
        """ get_paper_width(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_printer(self): # real signature unknown; restored from __doc__
        """ get_printer(self) -> str """
        return ""

    def get_printer_lpi(self): # real signature unknown; restored from __doc__
        """ get_printer_lpi(self) -> float """
        return 0.0

    def get_print_pages(self): # real signature unknown; restored from __doc__
        """ get_print_pages(self) -> Gtk.PrintPages """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_quality(self): # real signature unknown; restored from __doc__
        """ get_quality(self) -> Gtk.PrintQuality """
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> int """
        return 0

    def get_resolution_x(self): # real signature unknown; restored from __doc__
        """ get_resolution_x(self) -> int """
        return 0

    def get_resolution_y(self): # real signature unknown; restored from __doc__
        """ get_resolution_y(self) -> int """
        return 0

    def get_reverse(self): # real signature unknown; restored from __doc__
        """ get_reverse(self) -> bool """
        return False

    def get_scale(self): # real signature unknown; restored from __doc__
        """ get_scale(self) -> float """
        return 0.0

    def get_use_color(self): # real signature unknown; restored from __doc__
        """ get_use_color(self) -> bool """
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

    def has_key(self, key): # real signature unknown; restored from __doc__
        """ has_key(self, key:str) -> bool """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def load_file(self, file_name): # real signature unknown; restored from __doc__
        """ load_file(self, file_name:str) -> bool """
        return False

    def load_key_file(self, key_file, group_name=None): # real signature unknown; restored from __doc__
        """ load_key_file(self, key_file:GLib.KeyFile, group_name:str=None) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.PrintSettings """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_file(self, file_name): # real signature unknown; restored from __doc__
        """ new_from_file(file_name:str) -> Gtk.PrintSettings """
        pass

    def new_from_gvariant(self, variant): # real signature unknown; restored from __doc__
        """ new_from_gvariant(variant:GLib.Variant) -> Gtk.PrintSettings """
        pass

    def new_from_key_file(self, key_file, group_name=None): # real signature unknown; restored from __doc__
        """ new_from_key_file(key_file:GLib.KeyFile, group_name:str=None) -> Gtk.PrintSettings """
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

    def set(self, key, value=None): # real signature unknown; restored from __doc__
        """ set(self, key:str, value:str=None) """
        pass

    def set_bool(self, key, value): # real signature unknown; restored from __doc__
        """ set_bool(self, key:str, value:bool) """
        pass

    def set_collate(self, collate): # real signature unknown; restored from __doc__
        """ set_collate(self, collate:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_source(self, default_source): # real signature unknown; restored from __doc__
        """ set_default_source(self, default_source:str) """
        pass

    def set_dither(self, dither): # real signature unknown; restored from __doc__
        """ set_dither(self, dither:str) """
        pass

    def set_double(self, key, value): # real signature unknown; restored from __doc__
        """ set_double(self, key:str, value:float) """
        pass

    def set_duplex(self, duplex): # real signature unknown; restored from __doc__
        """ set_duplex(self, duplex:Gtk.PrintDuplex) """
        pass

    def set_finishings(self, finishings): # real signature unknown; restored from __doc__
        """ set_finishings(self, finishings:str) """
        pass

    def set_int(self, key, value): # real signature unknown; restored from __doc__
        """ set_int(self, key:str, value:int) """
        pass

    def set_length(self, key, value, unit): # real signature unknown; restored from __doc__
        """ set_length(self, key:str, value:float, unit:Gtk.Unit) """
        pass

    def set_media_type(self, media_type): # real signature unknown; restored from __doc__
        """ set_media_type(self, media_type:str) """
        pass

    def set_number_up(self, number_up): # real signature unknown; restored from __doc__
        """ set_number_up(self, number_up:int) """
        pass

    def set_number_up_layout(self, number_up_layout): # real signature unknown; restored from __doc__
        """ set_number_up_layout(self, number_up_layout:Gtk.NumberUpLayout) """
        pass

    def set_n_copies(self, num_copies): # real signature unknown; restored from __doc__
        """ set_n_copies(self, num_copies:int) """
        pass

    def set_orientation(self, orientation): # real signature unknown; restored from __doc__
        """ set_orientation(self, orientation:Gtk.PageOrientation) """
        pass

    def set_output_bin(self, output_bin): # real signature unknown; restored from __doc__
        """ set_output_bin(self, output_bin:str) """
        pass

    def set_page_ranges(self, page_ranges): # real signature unknown; restored from __doc__
        """ set_page_ranges(self, page_ranges:list) """
        pass

    def set_page_set(self, page_set): # real signature unknown; restored from __doc__
        """ set_page_set(self, page_set:Gtk.PageSet) """
        pass

    def set_paper_height(self, height, unit): # real signature unknown; restored from __doc__
        """ set_paper_height(self, height:float, unit:Gtk.Unit) """
        pass

    def set_paper_size(self, paper_size): # real signature unknown; restored from __doc__
        """ set_paper_size(self, paper_size:Gtk.PaperSize) """
        pass

    def set_paper_width(self, width, unit): # real signature unknown; restored from __doc__
        """ set_paper_width(self, width:float, unit:Gtk.Unit) """
        pass

    def set_printer(self, printer): # real signature unknown; restored from __doc__
        """ set_printer(self, printer:str) """
        pass

    def set_printer_lpi(self, lpi): # real signature unknown; restored from __doc__
        """ set_printer_lpi(self, lpi:float) """
        pass

    def set_print_pages(self, pages): # real signature unknown; restored from __doc__
        """ set_print_pages(self, pages:Gtk.PrintPages) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_quality(self, quality): # real signature unknown; restored from __doc__
        """ set_quality(self, quality:Gtk.PrintQuality) """
        pass

    def set_resolution(self, resolution): # real signature unknown; restored from __doc__
        """ set_resolution(self, resolution:int) """
        pass

    def set_resolution_xy(self, resolution_x, resolution_y): # real signature unknown; restored from __doc__
        """ set_resolution_xy(self, resolution_x:int, resolution_y:int) """
        pass

    def set_reverse(self, reverse): # real signature unknown; restored from __doc__
        """ set_reverse(self, reverse:bool) """
        pass

    def set_scale(self, scale): # real signature unknown; restored from __doc__
        """ set_scale(self, scale:float) """
        pass

    def set_use_color(self, use_color): # real signature unknown; restored from __doc__
        """ set_use_color(self, use_color:bool) """
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

    def to_file(self, file_name): # real signature unknown; restored from __doc__
        """ to_file(self, file_name:str) -> bool """
        return False

    def to_gvariant(self): # real signature unknown; restored from __doc__
        """ to_gvariant(self) -> GLib.Variant """
        pass

    def to_key_file(self, key_file, group_name=None): # real signature unknown; restored from __doc__
        """ to_key_file(self, key_file:GLib.KeyFile, group_name:str=None) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unset(self, key): # real signature unknown; restored from __doc__
        """ unset(self, key:str) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002eceabb0be0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(PrintSettings), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkPrintSettings (3923954720)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'new_from_file': gi.FunctionInfo(new_from_file, bound=None), 'new_from_gvariant': gi.FunctionInfo(new_from_gvariant, bound=None), 'new_from_key_file': gi.FunctionInfo(new_from_key_file, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'foreach': gi.FunctionInfo(foreach, bound=None), 'get': gi.FunctionInfo(get, bound=None), 'get_bool': gi.FunctionInfo(get_bool, bound=None), 'get_collate': gi.FunctionInfo(get_collate, bound=None), 'get_default_source': gi.FunctionInfo(get_default_source, bound=None), 'get_dither': gi.FunctionInfo(get_dither, bound=None), 'get_double': gi.FunctionInfo(get_double, bound=None), 'get_double_with_default': gi.FunctionInfo(get_double_with_default, bound=None), 'get_duplex': gi.FunctionInfo(get_duplex, bound=None), 'get_finishings': gi.FunctionInfo(get_finishings, bound=None), 'get_int': gi.FunctionInfo(get_int, bound=None), 'get_int_with_default': gi.FunctionInfo(get_int_with_default, bound=None), 'get_length': gi.FunctionInfo(get_length, bound=None), 'get_media_type': gi.FunctionInfo(get_media_type, bound=None), 'get_n_copies': gi.FunctionInfo(get_n_copies, bound=None), 'get_number_up': gi.FunctionInfo(get_number_up, bound=None), 'get_number_up_layout': gi.FunctionInfo(get_number_up_layout, bound=None), 'get_orientation': gi.FunctionInfo(get_orientation, bound=None), 'get_output_bin': gi.FunctionInfo(get_output_bin, bound=None), 'get_page_ranges': gi.FunctionInfo(get_page_ranges, bound=None), 'get_page_set': gi.FunctionInfo(get_page_set, bound=None), 'get_paper_height': gi.FunctionInfo(get_paper_height, bound=None), 'get_paper_size': gi.FunctionInfo(get_paper_size, bound=None), 'get_paper_width': gi.FunctionInfo(get_paper_width, bound=None), 'get_print_pages': gi.FunctionInfo(get_print_pages, bound=None), 'get_printer': gi.FunctionInfo(get_printer, bound=None), 'get_printer_lpi': gi.FunctionInfo(get_printer_lpi, bound=None), 'get_quality': gi.FunctionInfo(get_quality, bound=None), 'get_resolution': gi.FunctionInfo(get_resolution, bound=None), 'get_resolution_x': gi.FunctionInfo(get_resolution_x, bound=None), 'get_resolution_y': gi.FunctionInfo(get_resolution_y, bound=None), 'get_reverse': gi.FunctionInfo(get_reverse, bound=None), 'get_scale': gi.FunctionInfo(get_scale, bound=None), 'get_use_color': gi.FunctionInfo(get_use_color, bound=None), 'has_key': gi.FunctionInfo(has_key, bound=None), 'load_file': gi.FunctionInfo(load_file, bound=None), 'load_key_file': gi.FunctionInfo(load_key_file, bound=None), 'set': gi.FunctionInfo(set, bound=None), 'set_bool': gi.FunctionInfo(set_bool, bound=None), 'set_collate': gi.FunctionInfo(set_collate, bound=None), 'set_default_source': gi.FunctionInfo(set_default_source, bound=None), 'set_dither': gi.FunctionInfo(set_dither, bound=None), 'set_double': gi.FunctionInfo(set_double, bound=None), 'set_duplex': gi.FunctionInfo(set_duplex, bound=None), 'set_finishings': gi.FunctionInfo(set_finishings, bound=None), 'set_int': gi.FunctionInfo(set_int, bound=None), 'set_length': gi.FunctionInfo(set_length, bound=None), 'set_media_type': gi.FunctionInfo(set_media_type, bound=None), 'set_n_copies': gi.FunctionInfo(set_n_copies, bound=None), 'set_number_up': gi.FunctionInfo(set_number_up, bound=None), 'set_number_up_layout': gi.FunctionInfo(set_number_up_layout, bound=None), 'set_orientation': gi.FunctionInfo(set_orientation, bound=None), 'set_output_bin': gi.FunctionInfo(set_output_bin, bound=None), 'set_page_ranges': gi.FunctionInfo(set_page_ranges, bound=None), 'set_page_set': gi.FunctionInfo(set_page_set, bound=None), 'set_paper_height': gi.FunctionInfo(set_paper_height, bound=None), 'set_paper_size': gi.FunctionInfo(set_paper_size, bound=None), 'set_paper_width': gi.FunctionInfo(set_paper_width, bound=None), 'set_print_pages': gi.FunctionInfo(set_print_pages, bound=None), 'set_printer': gi.FunctionInfo(set_printer, bound=None), 'set_printer_lpi': gi.FunctionInfo(set_printer_lpi, bound=None), 'set_quality': gi.FunctionInfo(set_quality, bound=None), 'set_resolution': gi.FunctionInfo(set_resolution, bound=None), 'set_resolution_xy': gi.FunctionInfo(set_resolution_xy, bound=None), 'set_reverse': gi.FunctionInfo(set_reverse, bound=None), 'set_scale': gi.FunctionInfo(set_scale, bound=None), 'set_use_color': gi.FunctionInfo(set_use_color, bound=None), 'to_file': gi.FunctionInfo(to_file, bound=None), 'to_gvariant': gi.FunctionInfo(to_gvariant, bound=None), 'to_key_file': gi.FunctionInfo(to_key_file, bound=None), 'unset': gi.FunctionInfo(unset, bound=None)})"
    __gdoc__ = 'Object GtkPrintSettings\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkPrintSettings (3923954720)>'
    __info__ = ObjectInfo(PrintSettings)


