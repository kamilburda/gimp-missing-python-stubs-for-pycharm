# encoding: utf-8
# module gi.repository.Gdk
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Gdk-3.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .Event import Event

class Event(Event):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gdk.Event """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get() -> Gdk.Event or None """
        pass

    def get_axis(self, axis_use): # real signature unknown; restored from __doc__
        """ get_axis(self, axis_use:Gdk.AxisUse) -> bool, value:float """
        return False

    def get_button(self): # real signature unknown; restored from __doc__
        """ get_button(self) -> bool, button:int """
        return False

    def get_click_count(self): # real signature unknown; restored from __doc__
        """ get_click_count(self) -> bool, click_count:int """
        return False

    def get_coords(self): # real signature unknown; restored from __doc__
        """ get_coords(self) -> bool, x_win:float, y_win:float """
        return False

    def get_device(self): # real signature unknown; restored from __doc__
        """ get_device(self) -> Gdk.Device or None """
        pass

    def get_device_tool(self): # real signature unknown; restored from __doc__
        """ get_device_tool(self) -> Gdk.DeviceTool """
        pass

    def get_event_sequence(self): # real signature unknown; restored from __doc__
        """ get_event_sequence(self) -> Gdk.EventSequence """
        pass

    def get_event_type(self): # real signature unknown; restored from __doc__
        """ get_event_type(self) -> Gdk.EventType """
        pass

    def get_keycode(self): # real signature unknown; restored from __doc__
        """ get_keycode(self) -> bool, keycode:int """
        return False

    def get_keyval(self): # real signature unknown; restored from __doc__
        """ get_keyval(self) -> bool, keyval:int """
        return False

    def get_pointer_emulated(self): # real signature unknown; restored from __doc__
        """ get_pointer_emulated(self) -> bool """
        return False

    def get_root_coords(self): # real signature unknown; restored from __doc__
        """ get_root_coords(self) -> bool, x_root:float, y_root:float """
        return False

    def get_scancode(self): # real signature unknown; restored from __doc__
        """ get_scancode(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_scroll_deltas(self): # real signature unknown; restored from __doc__
        """ get_scroll_deltas(self) -> bool, delta_x:float, delta_y:float """
        return False

    def get_scroll_direction(self): # real signature unknown; restored from __doc__
        """ get_scroll_direction(self) -> bool, direction:Gdk.ScrollDirection """
        return False

    def get_seat(self): # real signature unknown; restored from __doc__
        """ get_seat(self) -> Gdk.Seat """
        pass

    def get_source_device(self): # real signature unknown; restored from __doc__
        """ get_source_device(self) -> Gdk.Device or None """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> bool, state:Gdk.ModifierType """
        return False

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window """
        pass

    def handler_set(self, func, data=None): # real signature unknown; restored from __doc__
        """ handler_set(func:Gdk.EventFunc, data=None) """
        pass

    def is_scroll_stop_event(self): # real signature unknown; restored from __doc__
        """ is_scroll_stop_event(self) -> bool """
        return False

    def new(self, type): # real signature unknown; restored from __doc__
        """ new(type:Gdk.EventType) -> Gdk.Event """
        pass

    def peek(self): # real signature unknown; restored from __doc__
        """ peek() -> Gdk.Event or None """
        pass

    def put(self): # real signature unknown; restored from __doc__
        """ put(self) """
        pass

    def request_motions(self, event): # real signature unknown; restored from __doc__
        """ request_motions(event:Gdk.EventMotion) """
        pass

    def set_device(self, device): # real signature unknown; restored from __doc__
        """ set_device(self, device:Gdk.Device) """
        pass

    def set_device_tool(self, tool=None): # real signature unknown; restored from __doc__
        """ set_device_tool(self, tool:Gdk.DeviceTool=None) """
        pass

    def set_screen(self, screen): # real signature unknown; restored from __doc__
        """ set_screen(self, screen:Gdk.Screen) """
        pass

    def set_source_device(self, device): # real signature unknown; restored from __doc__
        """ set_source_device(self, device:Gdk.Device) """
        pass

    def triggers_context_menu(self): # real signature unknown; restored from __doc__
        """ triggers_context_menu(self) -> bool """
        return False

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def _get_angle(self, event2): # real signature unknown; restored from __doc__
        """ _get_angle(self, event2:Gdk.Event) -> bool, angle:float """
        return False

    def _get_center(self, event2): # real signature unknown; restored from __doc__
        """ _get_center(self, event2:Gdk.Event) -> bool, x:float, y:float """
        return False

    def _get_distance(self, event2): # real signature unknown; restored from __doc__
        """ _get_distance(self, event2:Gdk.Event) -> bool, distance:float """
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
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, name, value): # reliably restored by inspect
        # no doc
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

    any = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    configure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    crossing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_broken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    motion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owner_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_group_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proximity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    setting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touchpad_pinch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touchpad_swipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _UNION_MEMBERS = {
        <enum GDK_DELETE of type Gdk.EventType>: 'any',
        <enum GDK_DESTROY of type Gdk.EventType>: 'any',
        <enum GDK_EXPOSE of type Gdk.EventType>: 'expose',
        <enum GDK_MOTION_NOTIFY of type Gdk.EventType>: 'motion',
        <enum GDK_BUTTON_PRESS of type Gdk.EventType>: 'button',
        <enum GDK_2BUTTON_PRESS of type Gdk.EventType>: 'button',
        <enum GDK_3BUTTON_PRESS of type Gdk.EventType>: 'button',
        <enum GDK_BUTTON_RELEASE of type Gdk.EventType>: 'button',
        <enum GDK_KEY_PRESS of type Gdk.EventType>: 'key',
        <enum GDK_KEY_RELEASE of type Gdk.EventType>: 'key',
        <enum GDK_ENTER_NOTIFY of type Gdk.EventType>: 'crossing',
        <enum GDK_LEAVE_NOTIFY of type Gdk.EventType>: 'crossing',
        <enum GDK_FOCUS_CHANGE of type Gdk.EventType>: 'focus_change',
        <enum GDK_CONFIGURE of type Gdk.EventType>: 'configure',
        <enum GDK_MAP of type Gdk.EventType>: 'any',
        <enum GDK_UNMAP of type Gdk.EventType>: 'any',
        <enum GDK_PROPERTY_NOTIFY of type Gdk.EventType>: 'property',
        <enum GDK_SELECTION_CLEAR of type Gdk.EventType>: 'selection',
        <enum GDK_SELECTION_REQUEST of type Gdk.EventType>: 'selection',
        <enum GDK_SELECTION_NOTIFY of type Gdk.EventType>: 'selection',
        <enum GDK_PROXIMITY_IN of type Gdk.EventType>: 'proximity',
        <enum GDK_PROXIMITY_OUT of type Gdk.EventType>: 'proximity',
        <enum GDK_DRAG_ENTER of type Gdk.EventType>: 'dnd',
        <enum GDK_DRAG_LEAVE of type Gdk.EventType>: 'dnd',
        <enum GDK_DRAG_MOTION of type Gdk.EventType>: 'dnd',
        <enum GDK_DRAG_STATUS of type Gdk.EventType>: 'dnd',
        <enum GDK_DROP_START of type Gdk.EventType>: 'dnd',
        <enum GDK_DROP_FINISHED of type Gdk.EventType>: 'dnd',
        <enum GDK_CLIENT_EVENT of type Gdk.EventType>: 'client',
        <enum GDK_VISIBILITY_NOTIFY of type Gdk.EventType>: 'visibility',
        <enum GDK_SCROLL of type Gdk.EventType>: 'scroll',
        <enum GDK_TOUCH_BEGIN of type Gdk.EventType>: 'touch',
        <enum GDK_TOUCH_UPDATE of type Gdk.EventType>: 'touch',
        <enum GDK_TOUCH_END of type Gdk.EventType>: 'touch',
        <enum GDK_TOUCH_CANCEL of type Gdk.EventType>: 'touch',
    }
    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gdk', '_UNION_MEMBERS': {<enum GDK_DELETE of type Gdk.EventType>: 'any', <enum GDK_DESTROY of type Gdk.EventType>: 'any', <enum GDK_MOTION_NOTIFY of type Gdk.EventType>: 'motion', <enum GDK_BUTTON_PRESS of type Gdk.EventType>: 'button', <enum GDK_BUTTON_RELEASE of type Gdk.EventType>: 'button', <enum GDK_KEY_PRESS of type Gdk.EventType>: 'key', <enum GDK_KEY_RELEASE of type Gdk.EventType>: 'key', <enum GDK_ENTER_NOTIFY of type Gdk.EventType>: 'crossing', <enum GDK_LEAVE_NOTIFY of type Gdk.EventType>: 'crossing', <enum GDK_FOCUS_CHANGE of type Gdk.EventType>: 'focus_change', <enum GDK_CONFIGURE of type Gdk.EventType>: 'configure', <enum GDK_PROXIMITY_IN of type Gdk.EventType>: 'proximity', <enum GDK_PROXIMITY_OUT of type Gdk.EventType>: 'proximity', <enum GDK_DRAG_ENTER of type Gdk.EventType>: 'dnd', <enum GDK_DRAG_LEAVE of type Gdk.EventType>: 'dnd', <enum GDK_DRAG_MOTION of type Gdk.EventType>: 'dnd', <enum GDK_DROP_START of type Gdk.EventType>: 'dnd', <enum GDK_2BUTTON_PRESS of type Gdk.EventType>: 'button', <enum GDK_3BUTTON_PRESS of type Gdk.EventType>: 'button', <enum GDK_PROPERTY_NOTIFY of type Gdk.EventType>: 'property', <enum GDK_SELECTION_CLEAR of type Gdk.EventType>: 'selection', <enum GDK_SELECTION_REQUEST of type Gdk.EventType>: 'selection', <enum GDK_SELECTION_NOTIFY of type Gdk.EventType>: 'selection', <enum GDK_DRAG_STATUS of type Gdk.EventType>: 'dnd', <enum GDK_DROP_FINISHED of type Gdk.EventType>: 'dnd', <enum GDK_CLIENT_EVENT of type Gdk.EventType>: 'client', <enum GDK_VISIBILITY_NOTIFY of type Gdk.EventType>: 'visibility', <enum GDK_SCROLL of type Gdk.EventType>: 'scroll', <enum GDK_EXPOSE of type Gdk.EventType>: 'expose', <enum GDK_MAP of type Gdk.EventType>: 'any', <enum GDK_UNMAP of type Gdk.EventType>: 'any', <enum GDK_TOUCH_BEGIN of type Gdk.EventType>: 'touch', <enum GDK_TOUCH_UPDATE of type Gdk.EventType>: 'touch', <enum GDK_TOUCH_END of type Gdk.EventType>: 'touch', <enum GDK_TOUCH_CANCEL of type Gdk.EventType>: 'touch'}, '__getattr__': <function Event.__getattr__ at 0x000002459bda6200>, '__setattr__': <function Event.__setattr__ at 0x000002459bda62a0>, '__repr__': <function Event.__repr__ at 0x000002459bda6340>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType GdkEvent (2575317872)>'
    __info__ = gi.UnionInfo(Event)


