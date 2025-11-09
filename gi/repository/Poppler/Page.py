# encoding: utf-8
# module gi.repository.Poppler
# from C:/Program Files/GIMP 3/lib/girepository-1.0\Poppler-0.18.typelib
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


class Page(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Page(**properties)
    """
    def add_annot(self, annot): # real signature unknown; restored from __doc__
        """ add_annot(self, annot:Poppler.Annot) """
        pass

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

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_text(self, text): # real signature unknown; restored from __doc__
        """ find_text(self, text:str) -> list """
        return []

    def find_text_with_options(self, text, options): # real signature unknown; restored from __doc__
        """ find_text_with_options(self, text:str, options:Poppler.FindFlags) -> list """
        return []

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

    def free_annot_mapping(self, p_list): # real signature unknown; restored from __doc__
        """ free_annot_mapping(list:list) """
        pass

    def free_form_field_mapping(self, p_list): # real signature unknown; restored from __doc__
        """ free_form_field_mapping(list:list) """
        pass

    def free_image_mapping(self, p_list): # real signature unknown; restored from __doc__
        """ free_image_mapping(list:list) """
        pass

    def free_link_mapping(self, p_list): # real signature unknown; restored from __doc__
        """ free_link_mapping(list:list) """
        pass

    def free_text_attributes(self, p_list): # real signature unknown; restored from __doc__
        """ free_text_attributes(list:list) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_annot_mapping(self): # real signature unknown; restored from __doc__
        """ get_annot_mapping(self) -> list """
        return []

    def get_bounding_box(self, rect): # real signature unknown; restored from __doc__
        """ get_bounding_box(self, rect:Poppler.Rectangle) -> bool """
        return False

    def get_crop_box(self): # real signature unknown; restored from __doc__
        """ get_crop_box(self) -> rect:Poppler.Rectangle """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> float """
        return 0.0

    def get_form_field_mapping(self): # real signature unknown; restored from __doc__
        """ get_form_field_mapping(self) -> list """
        return []

    def get_image(self, image_id): # real signature unknown; restored from __doc__
        """ get_image(self, image_id:int) -> cairo.Surface """
        pass

    def get_image_mapping(self): # real signature unknown; restored from __doc__
        """ get_image_mapping(self) -> list """
        return []

    def get_index(self): # real signature unknown; restored from __doc__
        """ get_index(self) -> int """
        return 0

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_link_mapping(self): # real signature unknown; restored from __doc__
        """ get_link_mapping(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_selected_region(self, scale, style, selection): # real signature unknown; restored from __doc__
        """ get_selected_region(self, scale:float, style:Poppler.SelectionStyle, selection:Poppler.Rectangle) -> cairo.Region """
        pass

    def get_selected_text(self, style, selection): # real signature unknown; restored from __doc__
        """ get_selected_text(self, style:Poppler.SelectionStyle, selection:Poppler.Rectangle) -> str """
        return ""

    def get_selection_region(self, scale, style, selection): # real signature unknown; restored from __doc__
        """ get_selection_region(self, scale:float, style:Poppler.SelectionStyle, selection:Poppler.Rectangle) -> list """
        return []

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:float, height:float """
        pass

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str """
        return ""

    def get_text_attributes(self): # real signature unknown; restored from __doc__
        """ get_text_attributes(self) -> list """
        return []

    def get_text_attributes_for_area(self, area): # real signature unknown; restored from __doc__
        """ get_text_attributes_for_area(self, area:Poppler.Rectangle) -> list """
        return []

    def get_text_for_area(self, area): # real signature unknown; restored from __doc__
        """ get_text_for_area(self, area:Poppler.Rectangle) -> str """
        return ""

    def get_text_layout(self): # real signature unknown; restored from __doc__
        """ get_text_layout(self) -> bool, rectangles:list """
        return False

    def get_text_layout_for_area(self, area): # real signature unknown; restored from __doc__
        """ get_text_layout_for_area(self, area:Poppler.Rectangle) -> bool, rectangles:list """
        return False

    def get_thumbnail(self): # real signature unknown; restored from __doc__
        """ get_thumbnail(self) -> cairo.Surface """
        pass

    def get_thumbnail_size(self): # real signature unknown; restored from __doc__
        """ get_thumbnail_size(self) -> bool, width:int, height:int """
        return False

    def get_transition(self): # real signature unknown; restored from __doc__
        """ get_transition(self) -> Poppler.PageTransition """
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

    def remove_annot(self, annot): # real signature unknown; restored from __doc__
        """ remove_annot(self, annot:Poppler.Annot) """
        pass

    def render(self, cairo): # real signature unknown; restored from __doc__
        """ render(self, cairo:cairo.Context) """
        pass

    def render_for_printing(self, cairo): # real signature unknown; restored from __doc__
        """ render_for_printing(self, cairo:cairo.Context) """
        pass

    def render_for_printing_with_options(self, cairo, options): # real signature unknown; restored from __doc__
        """ render_for_printing_with_options(self, cairo:cairo.Context, options:Poppler.PrintFlags) """
        pass

    def render_selection(self, cairo, selection, old_selection, style, glyph_color, background_color): # real signature unknown; restored from __doc__
        """ render_selection(self, cairo:cairo.Context, selection:Poppler.Rectangle, old_selection:Poppler.Rectangle, style:Poppler.SelectionStyle, glyph_color:Poppler.Color, background_color:Poppler.Color) """
        pass

    def render_to_ps(self, ps_file): # real signature unknown; restored from __doc__
        """ render_to_ps(self, ps_file:Poppler.PSFile) """
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

    def selection_region_free(self, region): # real signature unknown; restored from __doc__
        """ selection_region_free(region:list) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001deefec67d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Page), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerPage (3987916384)>, '__doc__': None, '__gsignals__': {}, 'free_annot_mapping': gi.FunctionInfo(free_annot_mapping, bound=None), 'free_form_field_mapping': gi.FunctionInfo(free_form_field_mapping, bound=None), 'free_image_mapping': gi.FunctionInfo(free_image_mapping, bound=None), 'free_link_mapping': gi.FunctionInfo(free_link_mapping, bound=None), 'free_text_attributes': gi.FunctionInfo(free_text_attributes, bound=None), 'selection_region_free': gi.FunctionInfo(selection_region_free, bound=None), 'add_annot': gi.FunctionInfo(add_annot, bound=None), 'find_text': gi.FunctionInfo(find_text, bound=None), 'find_text_with_options': gi.FunctionInfo(find_text_with_options, bound=None), 'get_annot_mapping': gi.FunctionInfo(get_annot_mapping, bound=None), 'get_bounding_box': gi.FunctionInfo(get_bounding_box, bound=None), 'get_crop_box': gi.FunctionInfo(get_crop_box, bound=None), 'get_duration': gi.FunctionInfo(get_duration, bound=None), 'get_form_field_mapping': gi.FunctionInfo(get_form_field_mapping, bound=None), 'get_image': gi.FunctionInfo(get_image, bound=None), 'get_image_mapping': gi.FunctionInfo(get_image_mapping, bound=None), 'get_index': gi.FunctionInfo(get_index, bound=None), 'get_label': gi.FunctionInfo(get_label, bound=None), 'get_link_mapping': gi.FunctionInfo(get_link_mapping, bound=None), 'get_selected_region': gi.FunctionInfo(get_selected_region, bound=None), 'get_selected_text': gi.FunctionInfo(get_selected_text, bound=None), 'get_selection_region': gi.FunctionInfo(get_selection_region, bound=None), 'get_size': gi.FunctionInfo(get_size, bound=None), 'get_text': gi.FunctionInfo(get_text, bound=None), 'get_text_attributes': gi.FunctionInfo(get_text_attributes, bound=None), 'get_text_attributes_for_area': gi.FunctionInfo(get_text_attributes_for_area, bound=None), 'get_text_for_area': gi.FunctionInfo(get_text_for_area, bound=None), 'get_text_layout': gi.FunctionInfo(get_text_layout, bound=None), 'get_text_layout_for_area': gi.FunctionInfo(get_text_layout_for_area, bound=None), 'get_thumbnail': gi.FunctionInfo(get_thumbnail, bound=None), 'get_thumbnail_size': gi.FunctionInfo(get_thumbnail_size, bound=None), 'get_transition': gi.FunctionInfo(get_transition, bound=None), 'remove_annot': gi.FunctionInfo(remove_annot, bound=None), 'render': gi.FunctionInfo(render, bound=None), 'render_for_printing': gi.FunctionInfo(render_for_printing, bound=None), 'render_for_printing_with_options': gi.FunctionInfo(render_for_printing_with_options, bound=None), 'render_selection': gi.FunctionInfo(render_selection, bound=None), 'render_to_ps': gi.FunctionInfo(render_to_ps, bound=None)})"
    __gdoc__ = 'Object PopplerPage\n\nProperties from PopplerPage:\n  label -> gchararray: Page Label\n    The label of the page\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PopplerPage (3987916384)>'
    __info__ = ObjectInfo(Page)


