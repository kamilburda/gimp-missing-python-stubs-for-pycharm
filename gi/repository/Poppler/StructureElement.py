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


class StructureElement(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        StructureElement(**properties)
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

    def get_abbreviation(self): # real signature unknown; restored from __doc__
        """ get_abbreviation(self) -> str """
        return ""

    def get_actual_text(self): # real signature unknown; restored from __doc__
        """ get_actual_text(self) -> str """
        return ""

    def get_alt_text(self): # real signature unknown; restored from __doc__
        """ get_alt_text(self) -> str """
        return ""

    def get_background_color(self): # real signature unknown; restored from __doc__
        """ get_background_color(self) -> bool, color:Poppler.Color """
        return False

    def get_baseline_shift(self): # real signature unknown; restored from __doc__
        """ get_baseline_shift(self) -> float """
        return 0.0

    def get_block_align(self): # real signature unknown; restored from __doc__
        """ get_block_align(self) -> Poppler.StructureBlockAlign """
        pass

    def get_border_color(self): # real signature unknown; restored from __doc__
        """ get_border_color(self) -> bool, colors:list """
        return False

    def get_border_style(self): # real signature unknown; restored from __doc__
        """ get_border_style(self) -> border_styles:list """
        pass

    def get_border_thickness(self): # real signature unknown; restored from __doc__
        """ get_border_thickness(self) -> bool, border_thicknesses:list """
        return False

    def get_bounding_box(self): # real signature unknown; restored from __doc__
        """ get_bounding_box(self) -> bool, bounding_box:Poppler.Rectangle """
        return False

    def get_color(self): # real signature unknown; restored from __doc__
        """ get_color(self) -> bool, color:Poppler.Color """
        return False

    def get_column_count(self): # real signature unknown; restored from __doc__
        """ get_column_count(self) -> int """
        return 0

    def get_column_gaps(self): # real signature unknown; restored from __doc__
        """ get_column_gaps(self) -> list """
        return []

    def get_column_widths(self): # real signature unknown; restored from __doc__
        """ get_column_widths(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_end_indent(self): # real signature unknown; restored from __doc__
        """ get_end_indent(self) -> float """
        return 0.0

    def get_form_description(self): # real signature unknown; restored from __doc__
        """ get_form_description(self) -> str """
        return ""

    def get_form_role(self): # real signature unknown; restored from __doc__
        """ get_form_role(self) -> Poppler.StructureFormRole """
        pass

    def get_form_state(self): # real signature unknown; restored from __doc__
        """ get_form_state(self) -> Poppler.StructureFormState """
        pass

    def get_glyph_orientation(self): # real signature unknown; restored from __doc__
        """ get_glyph_orientation(self) -> Poppler.StructureGlyphOrientation """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> float """
        return 0.0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_inline_align(self): # real signature unknown; restored from __doc__
        """ get_inline_align(self) -> Poppler.StructureInlineAlign """
        pass

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> Poppler.StructureElementKind """
        pass

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str """
        return ""

    def get_line_height(self): # real signature unknown; restored from __doc__
        """ get_line_height(self) -> float """
        return 0.0

    def get_list_numbering(self): # real signature unknown; restored from __doc__
        """ get_list_numbering(self) -> Poppler.StructureListNumbering """
        pass

    def get_padding(self): # real signature unknown; restored from __doc__
        """ get_padding(self) -> paddings:list """
        pass

    def get_page(self): # real signature unknown; restored from __doc__
        """ get_page(self) -> int """
        return 0

    def get_placement(self): # real signature unknown; restored from __doc__
        """ get_placement(self) -> Poppler.StructurePlacement """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_ruby_align(self): # real signature unknown; restored from __doc__
        """ get_ruby_align(self) -> Poppler.StructureRubyAlign """
        pass

    def get_ruby_position(self): # real signature unknown; restored from __doc__
        """ get_ruby_position(self) -> Poppler.StructureRubyPosition """
        pass

    def get_space_after(self): # real signature unknown; restored from __doc__
        """ get_space_after(self) -> float """
        return 0.0

    def get_space_before(self): # real signature unknown; restored from __doc__
        """ get_space_before(self) -> float """
        return 0.0

    def get_start_indent(self): # real signature unknown; restored from __doc__
        """ get_start_indent(self) -> float """
        return 0.0

    def get_table_border_style(self): # real signature unknown; restored from __doc__
        """ get_table_border_style(self) -> border_styles:list """
        pass

    def get_table_column_span(self): # real signature unknown; restored from __doc__
        """ get_table_column_span(self) -> int """
        return 0

    def get_table_headers(self): # real signature unknown; restored from __doc__
        """ get_table_headers(self) -> list """
        return []

    def get_table_padding(self): # real signature unknown; restored from __doc__
        """ get_table_padding(self) -> paddings:list """
        pass

    def get_table_row_span(self): # real signature unknown; restored from __doc__
        """ get_table_row_span(self) -> int """
        return 0

    def get_table_scope(self): # real signature unknown; restored from __doc__
        """ get_table_scope(self) -> Poppler.StructureTableScope """
        pass

    def get_table_summary(self): # real signature unknown; restored from __doc__
        """ get_table_summary(self) -> str """
        return ""

    def get_text(self, flags): # real signature unknown; restored from __doc__
        """ get_text(self, flags:Poppler.StructureGetTextFlags) -> str """
        return ""

    def get_text_align(self): # real signature unknown; restored from __doc__
        """ get_text_align(self) -> Poppler.StructureTextAlign """
        pass

    def get_text_decoration_color(self): # real signature unknown; restored from __doc__
        """ get_text_decoration_color(self) -> bool, color:Poppler.Color """
        return False

    def get_text_decoration_thickness(self): # real signature unknown; restored from __doc__
        """ get_text_decoration_thickness(self) -> float """
        return 0.0

    def get_text_decoration_type(self): # real signature unknown; restored from __doc__
        """ get_text_decoration_type(self) -> Poppler.StructureTextDecoration """
        pass

    def get_text_indent(self): # real signature unknown; restored from __doc__
        """ get_text_indent(self) -> float """
        return 0.0

    def get_text_spans(self): # real signature unknown; restored from __doc__
        """ get_text_spans(self) -> list """
        return []

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> float """
        return 0.0

    def get_writing_mode(self): # real signature unknown; restored from __doc__
        """ get_writing_mode(self) -> Poppler.StructureWritingMode """
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

    def is_block(self): # real signature unknown; restored from __doc__
        """ is_block(self) -> bool """
        return False

    def is_content(self): # real signature unknown; restored from __doc__
        """ is_content(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_grouping(self): # real signature unknown; restored from __doc__
        """ is_grouping(self) -> bool """
        return False

    def is_inline(self): # real signature unknown; restored from __doc__
        """ is_inline(self) -> bool """
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

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001deefed7b20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(StructureElement), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerStructureElement (3984840720)>, '__doc__': None, '__gsignals__': {}, 'get_abbreviation': gi.FunctionInfo(get_abbreviation, bound=None), 'get_actual_text': gi.FunctionInfo(get_actual_text, bound=None), 'get_alt_text': gi.FunctionInfo(get_alt_text, bound=None), 'get_background_color': gi.FunctionInfo(get_background_color, bound=None), 'get_baseline_shift': gi.FunctionInfo(get_baseline_shift, bound=None), 'get_block_align': gi.FunctionInfo(get_block_align, bound=None), 'get_border_color': gi.FunctionInfo(get_border_color, bound=None), 'get_border_style': gi.FunctionInfo(get_border_style, bound=None), 'get_border_thickness': gi.FunctionInfo(get_border_thickness, bound=None), 'get_bounding_box': gi.FunctionInfo(get_bounding_box, bound=None), 'get_color': gi.FunctionInfo(get_color, bound=None), 'get_column_count': gi.FunctionInfo(get_column_count, bound=None), 'get_column_gaps': gi.FunctionInfo(get_column_gaps, bound=None), 'get_column_widths': gi.FunctionInfo(get_column_widths, bound=None), 'get_end_indent': gi.FunctionInfo(get_end_indent, bound=None), 'get_form_description': gi.FunctionInfo(get_form_description, bound=None), 'get_form_role': gi.FunctionInfo(get_form_role, bound=None), 'get_form_state': gi.FunctionInfo(get_form_state, bound=None), 'get_glyph_orientation': gi.FunctionInfo(get_glyph_orientation, bound=None), 'get_height': gi.FunctionInfo(get_height, bound=None), 'get_id': gi.FunctionInfo(get_id, bound=None), 'get_inline_align': gi.FunctionInfo(get_inline_align, bound=None), 'get_kind': gi.FunctionInfo(get_kind, bound=None), 'get_language': gi.FunctionInfo(get_language, bound=None), 'get_line_height': gi.FunctionInfo(get_line_height, bound=None), 'get_list_numbering': gi.FunctionInfo(get_list_numbering, bound=None), 'get_padding': gi.FunctionInfo(get_padding, bound=None), 'get_page': gi.FunctionInfo(get_page, bound=None), 'get_placement': gi.FunctionInfo(get_placement, bound=None), 'get_ruby_align': gi.FunctionInfo(get_ruby_align, bound=None), 'get_ruby_position': gi.FunctionInfo(get_ruby_position, bound=None), 'get_space_after': gi.FunctionInfo(get_space_after, bound=None), 'get_space_before': gi.FunctionInfo(get_space_before, bound=None), 'get_start_indent': gi.FunctionInfo(get_start_indent, bound=None), 'get_table_border_style': gi.FunctionInfo(get_table_border_style, bound=None), 'get_table_column_span': gi.FunctionInfo(get_table_column_span, bound=None), 'get_table_headers': gi.FunctionInfo(get_table_headers, bound=None), 'get_table_padding': gi.FunctionInfo(get_table_padding, bound=None), 'get_table_row_span': gi.FunctionInfo(get_table_row_span, bound=None), 'get_table_scope': gi.FunctionInfo(get_table_scope, bound=None), 'get_table_summary': gi.FunctionInfo(get_table_summary, bound=None), 'get_text': gi.FunctionInfo(get_text, bound=None), 'get_text_align': gi.FunctionInfo(get_text_align, bound=None), 'get_text_decoration_color': gi.FunctionInfo(get_text_decoration_color, bound=None), 'get_text_decoration_thickness': gi.FunctionInfo(get_text_decoration_thickness, bound=None), 'get_text_decoration_type': gi.FunctionInfo(get_text_decoration_type, bound=None), 'get_text_indent': gi.FunctionInfo(get_text_indent, bound=None), 'get_text_spans': gi.FunctionInfo(get_text_spans, bound=None), 'get_title': gi.FunctionInfo(get_title, bound=None), 'get_width': gi.FunctionInfo(get_width, bound=None), 'get_writing_mode': gi.FunctionInfo(get_writing_mode, bound=None), 'is_block': gi.FunctionInfo(is_block, bound=None), 'is_content': gi.FunctionInfo(is_content, bound=None), 'is_grouping': gi.FunctionInfo(is_grouping, bound=None), 'is_inline': gi.FunctionInfo(is_inline, bound=None)})"
    __gdoc__ = 'Object PopplerStructureElement\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PopplerStructureElement (3984840720)>'
    __info__ = ObjectInfo(StructureElement)


