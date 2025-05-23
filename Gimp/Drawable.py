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


from .Item import Item

class Drawable(Item):
    """
    :Constructors:
    
    ::
    
        Drawable(**properties)
    """
    def append_filter(self, filter): # real signature unknown; restored from __doc__
        """ append_filter(self, filter:Gimp.DrawableFilter) """
        pass

    def attach_parasite(self, parasite): # real signature unknown; restored from __doc__
        """ attach_parasite(self, parasite:Gimp.Parasite) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def brightness_contrast(self, brightness, contrast): # real signature unknown; restored from __doc__
        """ brightness_contrast(self, brightness:float, contrast:float) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def colorize_hsl(self, hue, saturation, lightness): # real signature unknown; restored from __doc__
        """ colorize_hsl(self, hue:float, saturation:float, lightness:float) -> bool """
        return False

    def color_balance(self, transfer_mode, preserve_lum, cyan_red, magenta_green, yellow_blue): # real signature unknown; restored from __doc__
        """ color_balance(self, transfer_mode:Gimp.TransferMode, preserve_lum:bool, cyan_red:float, magenta_green:float, yellow_blue:float) -> bool """
        return False

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

    def curves_explicit(self, channel, values): # real signature unknown; restored from __doc__
        """ curves_explicit(self, channel:Gimp.HistogramChannel, values:list) -> bool """
        return False

    def curves_spline(self, channel, points): # real signature unknown; restored from __doc__
        """ curves_spline(self, channel:Gimp.HistogramChannel, points:list) -> bool """
        return False

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) -> bool """
        return False

    def desaturate(self, desaturate_mode): # real signature unknown; restored from __doc__
        """ desaturate(self, desaturate_mode:Gimp.DesaturateMode) -> bool """
        return False

    def detach_parasite(self, name): # real signature unknown; restored from __doc__
        """ detach_parasite(self, name:str) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def edit_bucket_fill(self, fill_type, x, y): # real signature unknown; restored from __doc__
        """ edit_bucket_fill(self, fill_type:Gimp.FillType, x:float, y:float) -> bool """
        return False

    def edit_clear(self): # real signature unknown; restored from __doc__
        """ edit_clear(self) -> bool """
        return False

    def edit_fill(self, fill_type): # real signature unknown; restored from __doc__
        """ edit_fill(self, fill_type:Gimp.FillType) -> bool """
        return False

    def edit_gradient_fill(self, gradient_type, offset, supersample, supersample_max_depth, supersample_threshold, dither, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ edit_gradient_fill(self, gradient_type:Gimp.GradientType, offset:float, supersample:bool, supersample_max_depth:int, supersample_threshold:float, dither:bool, x1:float, y1:float, x2:float, y2:float) -> bool """
        return False

    def edit_stroke_item(self, item): # real signature unknown; restored from __doc__
        """ edit_stroke_item(self, item:Gimp.Item) -> bool """
        return False

    def edit_stroke_selection(self): # real signature unknown; restored from __doc__
        """ edit_stroke_selection(self) -> bool """
        return False

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equalize(self, mask_only): # real signature unknown; restored from __doc__
        """ equalize(self, mask_only:bool) -> bool """
        return False

    def extract_component(self, component, invert, linear): # real signature unknown; restored from __doc__
        """ extract_component(self, component:int, invert:bool, linear:bool) -> bool """
        return False

    def fill(self, fill_type): # real signature unknown; restored from __doc__
        """ fill(self, fill_type:Gimp.FillType) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreground_extract(self, mode, mask): # real signature unknown; restored from __doc__
        """ foreground_extract(self, mode:Gimp.ForegroundExtractMode, mask:Gimp.Drawable) -> bool """
        return False

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

    def free_shadow(self): # real signature unknown; restored from __doc__
        """ free_shadow(self) -> bool """
        return False

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_bpp(self): # real signature unknown; restored from __doc__
        """ get_bpp(self) -> int """
        return 0

    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> Gegl.Buffer """
        pass

    def get_by_id(self, drawable_id): # real signature unknown; restored from __doc__
        """ get_by_id(drawable_id:int) -> Gimp.Drawable or None """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_color_tag(self): # real signature unknown; restored from __doc__
        """ get_color_tag(self) -> Gimp.ColorTag """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_expanded(self): # real signature unknown; restored from __doc__
        """ get_expanded(self) -> bool """
        return False

    def get_filters(self): # real signature unknown; restored from __doc__
        """ get_filters(self) -> list """
        return []

    def get_format(self): # real signature unknown; restored from __doc__
        """ get_format(self) -> Babl.Object """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_image(self): # real signature unknown; restored from __doc__
        """ get_image(self) -> Gimp.Image """
        pass

    def get_lock_content(self): # real signature unknown; restored from __doc__
        """ get_lock_content(self) -> bool """
        return False

    def get_lock_position(self): # real signature unknown; restored from __doc__
        """ get_lock_position(self) -> bool """
        return False

    def get_lock_visibility(self): # real signature unknown; restored from __doc__
        """ get_lock_visibility(self) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_offsets(self): # real signature unknown; restored from __doc__
        """ get_offsets(self) -> bool, offset_x:int, offset_y:int """
        return False

    def get_parasite(self, name): # real signature unknown; restored from __doc__
        """ get_parasite(self, name:str) -> Gimp.Parasite """
        pass

    def get_parasite_list(self): # real signature unknown; restored from __doc__
        """ get_parasite_list(self) -> list """
        return []

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gimp.Item """
        pass

    def get_pixel(self, x_coord, y_coord): # real signature unknown; restored from __doc__
        """ get_pixel(self, x_coord:int, y_coord:int) -> Gegl.Color """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_shadow_buffer(self): # real signature unknown; restored from __doc__
        """ get_shadow_buffer(self) -> Gegl.Buffer """
        pass

    def get_sub_thumbnail(self, src_x, src_y, src_width, src_height, dest_width, dest_height, alpha): # real signature unknown; restored from __doc__
        """ get_sub_thumbnail(self, src_x:int, src_y:int, src_width:int, src_height:int, dest_width:int, dest_height:int, alpha:Gimp.PixbufTransparency) -> GdkPixbuf.Pixbuf """
        pass

    def get_sub_thumbnail_data(self, src_x, src_y, src_width, src_height, dest_width, dest_height): # real signature unknown; restored from __doc__
        """ get_sub_thumbnail_data(self, src_x:int, src_y:int, src_width:int, src_height:int, dest_width:int, dest_height:int) -> GLib.Bytes, actual_width:int, actual_height:int, bpp:int """
        pass

    def get_tattoo(self): # real signature unknown; restored from __doc__
        """ get_tattoo(self) -> int """
        return 0

    def get_thumbnail(self, width, height, alpha): # real signature unknown; restored from __doc__
        """ get_thumbnail(self, width:int, height:int, alpha:Gimp.PixbufTransparency) -> GdkPixbuf.Pixbuf """
        pass

    def get_thumbnail_data(self, width, height): # real signature unknown; restored from __doc__
        """ get_thumbnail_data(self, width:int, height:int) -> GLib.Bytes or None, actual_width:int, actual_height:int, bpp:int """
        pass

    def get_thumbnail_format(self): # real signature unknown; restored from __doc__
        """ get_thumbnail_format(self) -> Babl.Object """
        pass

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

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

    def has_alpha(self): # real signature unknown; restored from __doc__
        """ has_alpha(self) -> bool """
        return False

    def histogram(self, channel, start_range, end_range): # real signature unknown; restored from __doc__
        """ histogram(self, channel:Gimp.HistogramChannel, start_range:float, end_range:float) -> bool, mean:float, std_dev:float, median:float, pixels:float, count:float, percentile:float """
        return False

    def hue_saturation(self, hue_range, hue_offset, lightness, saturation, overlap): # real signature unknown; restored from __doc__
        """ hue_saturation(self, hue_range:Gimp.HueRange, hue_offset:float, lightness:float, saturation:float, overlap:float) -> bool """
        return False

    def id_is_channel(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_channel(item_id:int) -> bool """
        return False

    def id_is_drawable(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_drawable(item_id:int) -> bool """
        return False

    def id_is_group_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_group_layer(item_id:int) -> bool """
        return False

    def id_is_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_layer(item_id:int) -> bool """
        return False

    def id_is_layer_mask(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_layer_mask(item_id:int) -> bool """
        return False

    def id_is_path(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_path(item_id:int) -> bool """
        return False

    def id_is_selection(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_selection(item_id:int) -> bool """
        return False

    def id_is_text_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_text_layer(item_id:int) -> bool """
        return False

    def id_is_valid(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_valid(item_id:int) -> bool """
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

    def invert(self, linear): # real signature unknown; restored from __doc__
        """ invert(self, linear:bool) -> bool """
        return False

    def is_channel(self): # real signature unknown; restored from __doc__
        """ is_channel(self) -> bool """
        return False

    def is_drawable(self): # real signature unknown; restored from __doc__
        """ is_drawable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_gray(self): # real signature unknown; restored from __doc__
        """ is_gray(self) -> bool """
        return False

    def is_group(self): # real signature unknown; restored from __doc__
        """ is_group(self) -> bool """
        return False

    def is_group_layer(self): # real signature unknown; restored from __doc__
        """ is_group_layer(self) -> bool """
        return False

    def is_indexed(self): # real signature unknown; restored from __doc__
        """ is_indexed(self) -> bool """
        return False

    def is_layer(self): # real signature unknown; restored from __doc__
        """ is_layer(self) -> bool """
        return False

    def is_layer_mask(self): # real signature unknown; restored from __doc__
        """ is_layer_mask(self) -> bool """
        return False

    def is_path(self): # real signature unknown; restored from __doc__
        """ is_path(self) -> bool """
        return False

    def is_rgb(self): # real signature unknown; restored from __doc__
        """ is_rgb(self) -> bool """
        return False

    def is_selection(self): # real signature unknown; restored from __doc__
        """ is_selection(self) -> bool """
        return False

    def is_text_layer(self): # real signature unknown; restored from __doc__
        """ is_text_layer(self) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def levels(self, channel, low_input, high_input, clamp_input, gamma, low_output, high_output, clamp_output): # real signature unknown; restored from __doc__
        """ levels(self, channel:Gimp.HistogramChannel, low_input:float, high_input:float, clamp_input:bool, gamma:float, low_output:float, high_output:float, clamp_output:bool) -> bool """
        return False

    def levels_stretch(self): # real signature unknown; restored from __doc__
        """ levels_stretch(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def mask_bounds(self): # real signature unknown; restored from __doc__
        """ mask_bounds(self) -> bool, x1:int, y1:int, x2:int, y2:int """
        return False

    def mask_intersect(self): # real signature unknown; restored from __doc__
        """ mask_intersect(self) -> bool, x:int, y:int, width:int, height:int """
        return False

    def merge_filter(self, filter): # real signature unknown; restored from __doc__
        """ merge_filter(self, filter:Gimp.DrawableFilter) """
        pass

    def merge_filters(self): # real signature unknown; restored from __doc__
        """ merge_filters(self) -> bool """
        return False

    def merge_shadow(self, undo): # real signature unknown; restored from __doc__
        """ merge_shadow(self, undo:bool) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def offset(self, wrap_around, fill_type, color, offset_x, offset_y): # real signature unknown; restored from __doc__
        """ offset(self, wrap_around:bool, fill_type:Gimp.OffsetType, color:Gegl.Color, offset_x:int, offset_y:int) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def posterize(self, levels): # real signature unknown; restored from __doc__
        """ posterize(self, levels:int) -> bool """
        return False

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

    def set_color_tag(self, color_tag): # real signature unknown; restored from __doc__
        """ set_color_tag(self, color_tag:Gimp.ColorTag) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_expanded(self, expanded): # real signature unknown; restored from __doc__
        """ set_expanded(self, expanded:bool) -> bool """
        return False

    def set_lock_content(self, lock_content): # real signature unknown; restored from __doc__
        """ set_lock_content(self, lock_content:bool) -> bool """
        return False

    def set_lock_position(self, lock_position): # real signature unknown; restored from __doc__
        """ set_lock_position(self, lock_position:bool) -> bool """
        return False

    def set_lock_visibility(self, lock_visibility): # real signature unknown; restored from __doc__
        """ set_lock_visibility(self, lock_visibility:bool) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) -> bool """
        return False

    def set_pixel(self, x_coord, y_coord, color): # real signature unknown; restored from __doc__
        """ set_pixel(self, x_coord:int, y_coord:int, color:Gegl.Color) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_tattoo(self, tattoo): # real signature unknown; restored from __doc__
        """ set_tattoo(self, tattoo:int) -> bool """
        return False

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) -> bool """
        return False

    def shadows_highlights(self, shadows, highlights, whitepoint, radius, compress, shadows_ccorrect, highlights_ccorrect): # real signature unknown; restored from __doc__
        """ shadows_highlights(self, shadows:float, highlights:float, whitepoint:float, radius:float, compress:float, shadows_ccorrect:float, highlights_ccorrect:float) -> bool """
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

    def threshold(self, channel, low_threshold, high_threshold): # real signature unknown; restored from __doc__
        """ threshold(self, channel:Gimp.HistogramChannel, low_threshold:float, high_threshold:float) -> bool """
        return False

    def transform_2d(self, source_x, source_y, scale_x, scale_y, angle, dest_x, dest_y): # real signature unknown; restored from __doc__
        """ transform_2d(self, source_x:float, source_y:float, scale_x:float, scale_y:float, angle:float, dest_x:float, dest_y:float) -> Gimp.Item """
        pass

    def transform_flip(self, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """ transform_flip(self, x0:float, y0:float, x1:float, y1:float) -> Gimp.Item """
        pass

    def transform_flip_simple(self, flip_type, auto_center, axis): # real signature unknown; restored from __doc__
        """ transform_flip_simple(self, flip_type:Gimp.OrientationType, auto_center:bool, axis:float) -> Gimp.Item """
        pass

    def transform_matrix(self, coeff_0_0, coeff_0_1, coeff_0_2, coeff_1_0, coeff_1_1, coeff_1_2, coeff_2_0, coeff_2_1, coeff_2_2): # real signature unknown; restored from __doc__
        """ transform_matrix(self, coeff_0_0:float, coeff_0_1:float, coeff_0_2:float, coeff_1_0:float, coeff_1_1:float, coeff_1_2:float, coeff_2_0:float, coeff_2_1:float, coeff_2_2:float) -> Gimp.Item """
        pass

    def transform_perspective(self, x0, y0, x1, y1, x2, y2, x3, y3): # real signature unknown; restored from __doc__
        """ transform_perspective(self, x0:float, y0:float, x1:float, y1:float, x2:float, y2:float, x3:float, y3:float) -> Gimp.Item """
        pass

    def transform_rotate(self, angle, auto_center, center_x, center_y): # real signature unknown; restored from __doc__
        """ transform_rotate(self, angle:float, auto_center:bool, center_x:float, center_y:float) -> Gimp.Item """
        pass

    def transform_rotate_simple(self, rotate_type, auto_center, center_x, center_y): # real signature unknown; restored from __doc__
        """ transform_rotate_simple(self, rotate_type:Gimp.RotationType, auto_center:bool, center_x:float, center_y:float) -> Gimp.Item """
        pass

    def transform_scale(self, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """ transform_scale(self, x0:float, y0:float, x1:float, y1:float) -> Gimp.Item """
        pass

    def transform_shear(self, shear_type, magnitude): # real signature unknown; restored from __doc__
        """ transform_shear(self, shear_type:Gimp.OrientationType, magnitude:float) -> Gimp.Item """
        pass

    def transform_translate(self, off_x, off_y): # real signature unknown; restored from __doc__
        """ transform_translate(self, off_x:float, off_y:float) -> Gimp.Item """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> Gimp.ImageType """
        pass

    def type_with_alpha(self): # real signature unknown; restored from __doc__
        """ type_with_alpha(self) -> Gimp.ImageType """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ update(self, x:int, y:int, width:int, height:int) -> bool """
        return False

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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001dcd6734280>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Drawable), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpDrawable (3599984448)>, '__doc__': None, '__gsignals__': {}, 'get_by_id': gi.FunctionInfo(get_by_id, bound=None), 'append_filter': gi.FunctionInfo(append_filter, bound=None), 'brightness_contrast': gi.FunctionInfo(brightness_contrast, bound=None), 'color_balance': gi.FunctionInfo(color_balance, bound=None), 'colorize_hsl': gi.FunctionInfo(colorize_hsl, bound=None), 'curves_explicit': gi.FunctionInfo(curves_explicit, bound=None), 'curves_spline': gi.FunctionInfo(curves_spline, bound=None), 'desaturate': gi.FunctionInfo(desaturate, bound=None), 'edit_bucket_fill': gi.FunctionInfo(edit_bucket_fill, bound=None), 'edit_clear': gi.FunctionInfo(edit_clear, bound=None), 'edit_fill': gi.FunctionInfo(edit_fill, bound=None), 'edit_gradient_fill': gi.FunctionInfo(edit_gradient_fill, bound=None), 'edit_stroke_item': gi.FunctionInfo(edit_stroke_item, bound=None), 'edit_stroke_selection': gi.FunctionInfo(edit_stroke_selection, bound=None), 'equalize': gi.FunctionInfo(equalize, bound=None), 'extract_component': gi.FunctionInfo(extract_component, bound=None), 'fill': gi.FunctionInfo(fill, bound=None), 'foreground_extract': gi.FunctionInfo(foreground_extract, bound=None), 'free_shadow': gi.FunctionInfo(free_shadow, bound=None), 'get_bpp': gi.FunctionInfo(get_bpp, bound=None), 'get_buffer': gi.FunctionInfo(get_buffer, bound=None), 'get_filters': gi.FunctionInfo(get_filters, bound=None), 'get_format': gi.FunctionInfo(get_format, bound=None), 'get_height': gi.FunctionInfo(get_height, bound=None), 'get_offsets': gi.FunctionInfo(get_offsets, bound=None), 'get_pixel': gi.FunctionInfo(get_pixel, bound=None), 'get_shadow_buffer': gi.FunctionInfo(get_shadow_buffer, bound=None), 'get_sub_thumbnail': gi.FunctionInfo(get_sub_thumbnail, bound=None), 'get_sub_thumbnail_data': gi.FunctionInfo(get_sub_thumbnail_data, bound=None), 'get_thumbnail': gi.FunctionInfo(get_thumbnail, bound=None), 'get_thumbnail_data': gi.FunctionInfo(get_thumbnail_data, bound=None), 'get_thumbnail_format': gi.FunctionInfo(get_thumbnail_format, bound=None), 'get_width': gi.FunctionInfo(get_width, bound=None), 'has_alpha': gi.FunctionInfo(has_alpha, bound=None), 'histogram': gi.FunctionInfo(histogram, bound=None), 'hue_saturation': gi.FunctionInfo(hue_saturation, bound=None), 'invert': gi.FunctionInfo(invert, bound=None), 'is_gray': gi.FunctionInfo(is_gray, bound=None), 'is_indexed': gi.FunctionInfo(is_indexed, bound=None), 'is_rgb': gi.FunctionInfo(is_rgb, bound=None), 'levels': gi.FunctionInfo(levels, bound=None), 'levels_stretch': gi.FunctionInfo(levels_stretch, bound=None), 'mask_bounds': gi.FunctionInfo(mask_bounds, bound=None), 'mask_intersect': gi.FunctionInfo(mask_intersect, bound=None), 'merge_filter': gi.FunctionInfo(merge_filter, bound=None), 'merge_filters': gi.FunctionInfo(merge_filters, bound=None), 'merge_shadow': gi.FunctionInfo(merge_shadow, bound=None), 'offset': gi.FunctionInfo(offset, bound=None), 'posterize': gi.FunctionInfo(posterize, bound=None), 'set_pixel': gi.FunctionInfo(set_pixel, bound=None), 'shadows_highlights': gi.FunctionInfo(shadows_highlights, bound=None), 'threshold': gi.FunctionInfo(threshold, bound=None), 'type': gi.FunctionInfo(type, bound=None), 'type_with_alpha': gi.FunctionInfo(type_with_alpha, bound=None), 'update': gi.FunctionInfo(update, bound=None), 'parent_instance': <property object at 0x000001dcd90ac2c0>})"
    __gdoc__ = 'Object GimpDrawable\n\nProperties from GimpItem:\n  id -> gint: The item id\n    The item id for internal use\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpDrawable (3599984448)>'
    __info__ = ObjectInfo(Drawable)


