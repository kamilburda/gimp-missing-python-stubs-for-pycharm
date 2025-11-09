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


class StyleContext(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        StyleContext(**properties)
        new() -> Gtk.StyleContext
    """
    def add_class(self, class_name): # real signature unknown; restored from __doc__
        """ add_class(self, class_name:str) """
        pass

    def add_provider(self, provider, priority): # real signature unknown; restored from __doc__
        """ add_provider(self, provider:Gtk.StyleProvider, priority:int) """
        pass

    def add_provider_for_screen(self, screen, provider, priority): # real signature unknown; restored from __doc__
        """ add_provider_for_screen(screen:Gdk.Screen, provider:Gtk.StyleProvider, priority:int) """
        pass

    def add_region(self, region_name, flags): # real signature unknown; restored from __doc__
        """ add_region(self, region_name:str, flags:Gtk.RegionFlags) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cancel_animations(self, region_id=None): # real signature unknown; restored from __doc__
        """ cancel_animations(self, region_id=None) """
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

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
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

    def get_background_color(self, state): # real signature unknown; restored from __doc__
        """ get_background_color(self, state:Gtk.StateFlags) -> color:Gdk.RGBA """
        pass

    def get_border(self, state): # real signature unknown; restored from __doc__
        """ get_border(self, state:Gtk.StateFlags) -> border:Gtk.Border """
        pass

    def get_border_color(self, state): # real signature unknown; restored from __doc__
        """ get_border_color(self, state:Gtk.StateFlags) -> color:Gdk.RGBA """
        pass

    def get_color(self, state): # real signature unknown; restored from __doc__
        """ get_color(self, state:Gtk.StateFlags) -> color:Gdk.RGBA """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_font(self, state): # real signature unknown; restored from __doc__
        """ get_font(self, state:Gtk.StateFlags) -> Pango.FontDescription """
        pass

    def get_frame_clock(self): # real signature unknown; restored from __doc__
        """ get_frame_clock(self) -> Gdk.FrameClock or None """
        pass

    def get_junction_sides(self): # real signature unknown; restored from __doc__
        """ get_junction_sides(self) -> Gtk.JunctionSides """
        pass

    def get_margin(self, state): # real signature unknown; restored from __doc__
        """ get_margin(self, state:Gtk.StateFlags) -> margin:Gtk.Border """
        pass

    def get_padding(self, state): # real signature unknown; restored from __doc__
        """ get_padding(self, state:Gtk.StateFlags) -> padding:Gtk.Border """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gtk.StyleContext or None """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.WidgetPath """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, property, state): # real signature unknown; restored from __doc__
        """ get_property(self, property:str, state:Gtk.StateFlags) -> value:GObject.Value """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_scale(self): # real signature unknown; restored from __doc__
        """ get_scale(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_section(self, property): # real signature unknown; restored from __doc__
        """ get_section(self, property:str) -> Gtk.CssSection or None """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateFlags """
        pass

    def get_style_property(self, property_name, value): # real signature unknown; restored from __doc__
        """ get_style_property(self, property_name:str, value:GObject.Value) """
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

    def has_class(self, class_name): # real signature unknown; restored from __doc__
        """ has_class(self, class_name:str) -> bool """
        return False

    def has_region(self, region_name): # real signature unknown; restored from __doc__
        """ has_region(self, region_name:str) -> bool, flags_return:Gtk.RegionFlags """
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

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_classes(self): # real signature unknown; restored from __doc__
        """ list_classes(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def list_regions(self): # real signature unknown; restored from __doc__
        """ list_regions(self) -> list """
        return []

    def lookup_color(self, color_name): # real signature unknown; restored from __doc__
        """ lookup_color(self, color_name:str) -> bool, color:Gdk.RGBA """
        return False

    def lookup_icon_set(self, stock_id): # real signature unknown; restored from __doc__
        """ lookup_icon_set(self, stock_id:str) -> Gtk.IconSet or None """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.StyleContext """
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

    def notify_state_change(self, window, region_id=None, state, state_value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, window:Gdk.Window, region_id=None, state:Gtk.StateType, state_value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def pop_animatable_region(self): # real signature unknown; restored from __doc__
        """ pop_animatable_region(self) """
        pass

    def push_animatable_region(self, region_id=None): # real signature unknown; restored from __doc__
        """ push_animatable_region(self, region_id=None) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_class(self, class_name): # real signature unknown; restored from __doc__
        """ remove_class(self, class_name:str) """
        pass

    def remove_provider(self, provider): # real signature unknown; restored from __doc__
        """ remove_provider(self, provider:Gtk.StyleProvider) """
        pass

    def remove_provider_for_screen(self, screen, provider): # real signature unknown; restored from __doc__
        """ remove_provider_for_screen(screen:Gdk.Screen, provider:Gtk.StyleProvider) """
        pass

    def remove_region(self, region_name): # real signature unknown; restored from __doc__
        """ remove_region(self, region_name:str) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_widgets(self, screen): # real signature unknown; restored from __doc__
        """ reset_widgets(screen:Gdk.Screen) """
        pass

    def restore(self): # real signature unknown; restored from __doc__
        """ restore(self) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) """
        pass

    def scroll_animations(self, window, dx, dy): # real signature unknown; restored from __doc__
        """ scroll_animations(self, window:Gdk.Window, dx:int, dy:int) """
        pass

    def set_background(self, window): # real signature unknown; restored from __doc__
        """ set_background(self, window:Gdk.Window) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_direction(self, direction): # real signature unknown; restored from __doc__
        """ set_direction(self, direction:Gtk.TextDirection) """
        pass

    def set_frame_clock(self, frame_clock): # real signature unknown; restored from __doc__
        """ set_frame_clock(self, frame_clock:Gdk.FrameClock) """
        pass

    def set_junction_sides(self, sides): # real signature unknown; restored from __doc__
        """ set_junction_sides(self, sides:Gtk.JunctionSides) """
        pass

    def set_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gtk.StyleContext=None) """
        pass

    def set_path(self, path): # real signature unknown; restored from __doc__
        """ set_path(self, path:Gtk.WidgetPath) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_scale(self, scale): # real signature unknown; restored from __doc__
        """ set_scale(self, scale:int) """
        pass

    def set_screen(self, screen): # real signature unknown; restored from __doc__
        """ set_screen(self, screen:Gdk.Screen) """
        pass

    def set_state(self, flags): # real signature unknown; restored from __doc__
        """ set_state(self, flags:Gtk.StateFlags) """
        pass

    def state_is_running(self, state): # real signature unknown; restored from __doc__
        """ state_is_running(self, state:Gtk.StateType) -> bool, progress:float """
        return False

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

    def to_string(self, flags): # real signature unknown; restored from __doc__
        """ to_string(self, flags:Gtk.StyleContextPrintFlags) -> str """
        return ""

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

    parent_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002ece90287f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(StyleContext), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkStyleContext (3923965920)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'add_provider_for_screen': gi.FunctionInfo(add_provider_for_screen, bound=None), 'remove_provider_for_screen': gi.FunctionInfo(remove_provider_for_screen, bound=None), 'reset_widgets': gi.FunctionInfo(reset_widgets, bound=None), 'add_class': gi.FunctionInfo(add_class, bound=None), 'add_provider': gi.FunctionInfo(add_provider, bound=None), 'add_region': gi.FunctionInfo(add_region, bound=None), 'cancel_animations': gi.FunctionInfo(cancel_animations, bound=None), 'get_background_color': gi.FunctionInfo(get_background_color, bound=None), 'get_border': gi.FunctionInfo(get_border, bound=None), 'get_border_color': gi.FunctionInfo(get_border_color, bound=None), 'get_color': gi.FunctionInfo(get_color, bound=None), 'get_direction': gi.FunctionInfo(get_direction, bound=None), 'get_font': gi.FunctionInfo(get_font, bound=None), 'get_frame_clock': gi.FunctionInfo(get_frame_clock, bound=None), 'get_junction_sides': gi.FunctionInfo(get_junction_sides, bound=None), 'get_margin': gi.FunctionInfo(get_margin, bound=None), 'get_padding': gi.FunctionInfo(get_padding, bound=None), 'get_parent': gi.FunctionInfo(get_parent, bound=None), 'get_path': gi.FunctionInfo(get_path, bound=None), 'get_property': gi.FunctionInfo(get_property, bound=None), 'get_scale': gi.FunctionInfo(get_scale, bound=None), 'get_screen': gi.FunctionInfo(get_screen, bound=None), 'get_section': gi.FunctionInfo(get_section, bound=None), 'get_state': gi.FunctionInfo(get_state, bound=None), 'get_style_property': gi.FunctionInfo(get_style_property, bound=None), 'has_class': gi.FunctionInfo(has_class, bound=None), 'has_region': gi.FunctionInfo(has_region, bound=None), 'invalidate': gi.FunctionInfo(invalidate, bound=None), 'list_classes': gi.FunctionInfo(list_classes, bound=None), 'list_regions': gi.FunctionInfo(list_regions, bound=None), 'lookup_color': gi.FunctionInfo(lookup_color, bound=None), 'lookup_icon_set': gi.FunctionInfo(lookup_icon_set, bound=None), 'notify_state_change': gi.FunctionInfo(notify_state_change, bound=None), 'pop_animatable_region': gi.FunctionInfo(pop_animatable_region, bound=None), 'push_animatable_region': gi.FunctionInfo(push_animatable_region, bound=None), 'remove_class': gi.FunctionInfo(remove_class, bound=None), 'remove_provider': gi.FunctionInfo(remove_provider, bound=None), 'remove_region': gi.FunctionInfo(remove_region, bound=None), 'restore': gi.FunctionInfo(restore, bound=None), 'save': gi.FunctionInfo(save, bound=None), 'scroll_animations': gi.FunctionInfo(scroll_animations, bound=None), 'set_background': gi.FunctionInfo(set_background, bound=None), 'set_direction': gi.FunctionInfo(set_direction, bound=None), 'set_frame_clock': gi.FunctionInfo(set_frame_clock, bound=None), 'set_junction_sides': gi.FunctionInfo(set_junction_sides, bound=None), 'set_parent': gi.FunctionInfo(set_parent, bound=None), 'set_path': gi.FunctionInfo(set_path, bound=None), 'set_scale': gi.FunctionInfo(set_scale, bound=None), 'set_screen': gi.FunctionInfo(set_screen, bound=None), 'set_state': gi.FunctionInfo(set_state, bound=None), 'state_is_running': gi.FunctionInfo(state_is_running, bound=None), 'to_string': gi.FunctionInfo(to_string, bound=None), 'do_changed': gi.VFuncInfo(changed, bound=None), 'parent_object': <property object at 0x000002ece9b7e7f0>, 'priv': <property object at 0x000002ece9b7e8e0>})"
    __gdoc__ = 'Object GtkStyleContext\n\nSignals from GtkStyleContext:\n  changed ()\n\nProperties from GtkStyleContext:\n  screen -> GdkScreen: Screen\n    The associated GdkScreen\n  direction -> GtkTextDirection: Direction\n    Text direction\n  paint-clock -> GdkFrameClock: FrameClock\n    The associated GdkFrameClock\n  parent -> GtkStyleContext: Parent\n    The parent style context\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkStyleContext (3923965920)>'
    __info__ = ObjectInfo(StyleContext)


