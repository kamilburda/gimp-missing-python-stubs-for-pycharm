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


from .FileProcedure import FileProcedure

class ExportProcedure(FileProcedure):
    """
    :Constructors:
    
    ::
    
        ExportProcedure(**properties)
        new(plug_in:Gimp.PlugIn, name:str, proc_type:Gimp.PDBProcType, export_metadata:bool, run_func:Gimp.RunExportFunc, run_data=None) -> Gimp.Procedure
    """
    def add_boolean_argument(self, name, nick, blurb, value, flags): # real signature unknown; restored from __doc__
        """ add_boolean_argument(self, name:str, nick:str, blurb:str, value:bool, flags:GObject.ParamFlags) """
        pass

    def add_boolean_aux_argument(self, name, nick, blurb, value, flags): # real signature unknown; restored from __doc__
        """ add_boolean_aux_argument(self, name:str, nick:str, blurb:str, value:bool, flags:GObject.ParamFlags) """
        pass

    def add_boolean_return_value(self, name, nick, blurb, value, flags): # real signature unknown; restored from __doc__
        """ add_boolean_return_value(self, name:str, nick:str, blurb:str, value:bool, flags:GObject.ParamFlags) """
        pass

    def add_brush_argument(self, name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_brush_argument(self, name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Brush=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_brush_aux_argument(self, name, nick, blurb, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_brush_aux_argument(self, name:str, nick:str, blurb:str, default_value:Gimp.Brush=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_brush_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_brush_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_bytes_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_bytes_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_bytes_aux_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_bytes_aux_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_bytes_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_bytes_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_channel_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_channel_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_channel_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_channel_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_channel_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_channel_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_choice_argument(self, name, nick, blurb, choice, value, flags): # real signature unknown; restored from __doc__
        """ add_choice_argument(self, name:str, nick:str, blurb:str, choice:Gimp.Choice, value:str, flags:GObject.ParamFlags) """
        pass

    def add_choice_aux_argument(self, name, nick, blurb, choice, value, flags): # real signature unknown; restored from __doc__
        """ add_choice_aux_argument(self, name:str, nick:str, blurb:str, choice:Gimp.Choice, value:str, flags:GObject.ParamFlags) """
        pass

    def add_choice_return_value(self, name, nick, blurb, choice, value, flags): # real signature unknown; restored from __doc__
        """ add_choice_return_value(self, name:str, nick:str, blurb:str, choice:Gimp.Choice, value:str, flags:GObject.ParamFlags) """
        pass

    def add_color_argument(self, name, nick, blurb, has_alpha, value, flags): # real signature unknown; restored from __doc__
        """ add_color_argument(self, name:str, nick:str, blurb:str, has_alpha:bool, value:Gegl.Color, flags:GObject.ParamFlags) """
        pass

    def add_color_aux_argument(self, name, nick, blurb, has_alpha, value, flags): # real signature unknown; restored from __doc__
        """ add_color_aux_argument(self, name:str, nick:str, blurb:str, has_alpha:bool, value:Gegl.Color, flags:GObject.ParamFlags) """
        pass

    def add_color_from_string_argument(self, name, nick, blurb, has_alpha, value, flags): # real signature unknown; restored from __doc__
        """ add_color_from_string_argument(self, name:str, nick:str, blurb:str, has_alpha:bool, value:str, flags:GObject.ParamFlags) """
        pass

    def add_color_from_string_aux_argument(self, name, nick, blurb, has_alpha, value, flags): # real signature unknown; restored from __doc__
        """ add_color_from_string_aux_argument(self, name:str, nick:str, blurb:str, has_alpha:bool, value:str, flags:GObject.ParamFlags) """
        pass

    def add_color_from_string_return_value(self, name, nick, blurb, has_alpha, value, flags): # real signature unknown; restored from __doc__
        """ add_color_from_string_return_value(self, name:str, nick:str, blurb:str, has_alpha:bool, value:str, flags:GObject.ParamFlags) """
        pass

    def add_color_return_value(self, name, nick, blurb, has_alpha, value, flags): # real signature unknown; restored from __doc__
        """ add_color_return_value(self, name:str, nick:str, blurb:str, has_alpha:bool, value:Gegl.Color, flags:GObject.ParamFlags) """
        pass

    def add_core_object_array_argument(self, name, nick, blurb, object_type, flags): # real signature unknown; restored from __doc__
        """ add_core_object_array_argument(self, name:str, nick:str, blurb:str, object_type:GType, flags:GObject.ParamFlags) """
        pass

    def add_core_object_array_aux_argument(self, name, nick, blurb, object_type, flags): # real signature unknown; restored from __doc__
        """ add_core_object_array_aux_argument(self, name:str, nick:str, blurb:str, object_type:GType, flags:GObject.ParamFlags) """
        pass

    def add_core_object_array_return_value(self, name, nick, blurb, object_type, flags): # real signature unknown; restored from __doc__
        """ add_core_object_array_return_value(self, name:str, nick:str, blurb:str, object_type:GType, flags:GObject.ParamFlags) """
        pass

    def add_display_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_display_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_display_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_display_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_display_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_display_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_double_argument(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_double_argument(self, name:str, nick:str, blurb:str, min:float, max:float, value:float, flags:GObject.ParamFlags) """
        pass

    def add_double_array_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_double_array_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_double_array_aux_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_double_array_aux_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_double_array_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_double_array_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_double_aux_argument(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_double_aux_argument(self, name:str, nick:str, blurb:str, min:float, max:float, value:float, flags:GObject.ParamFlags) """
        pass

    def add_double_return_value(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_double_return_value(self, name:str, nick:str, blurb:str, min:float, max:float, value:float, flags:GObject.ParamFlags) """
        pass

    def add_drawable_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_drawable_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_drawable_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_drawable_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_drawable_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_drawable_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_enum_argument(self, name, nick, blurb, enum_type, value, flags): # real signature unknown; restored from __doc__
        """ add_enum_argument(self, name:str, nick:str, blurb:str, enum_type:GType, value:int, flags:GObject.ParamFlags) """
        pass

    def add_enum_aux_argument(self, name, nick, blurb, enum_type, value, flags): # real signature unknown; restored from __doc__
        """ add_enum_aux_argument(self, name:str, nick:str, blurb:str, enum_type:GType, value:int, flags:GObject.ParamFlags) """
        pass

    def add_enum_return_value(self, name, nick, blurb, enum_type, value, flags): # real signature unknown; restored from __doc__
        """ add_enum_return_value(self, name:str, nick:str, blurb:str, enum_type:GType, value:int, flags:GObject.ParamFlags) """
        pass

    def add_file_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_file_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_file_aux_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_file_aux_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_file_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_file_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_font_argument(self, name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_font_argument(self, name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Font=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_font_aux_argument(self, name, nick, blurb, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_font_aux_argument(self, name:str, nick:str, blurb:str, default_value:Gimp.Font=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_font_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_font_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_gradient_argument(self, name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_gradient_argument(self, name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Gradient=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_gradient_aux_argument(self, name, nick, blurb, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_gradient_aux_argument(self, name:str, nick:str, blurb:str, default_value:Gimp.Gradient=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_gradient_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_gradient_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_group_layer_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_group_layer_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_group_layer_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_group_layer_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_group_layer_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_group_layer_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_image_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_image_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_image_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_image_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_image_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_image_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_int32_array_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_int32_array_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_int32_array_aux_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_int32_array_aux_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_int32_array_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_int32_array_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_int_argument(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_int_argument(self, name:str, nick:str, blurb:str, min:int, max:int, value:int, flags:GObject.ParamFlags) """
        pass

    def add_int_aux_argument(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_int_aux_argument(self, name:str, nick:str, blurb:str, min:int, max:int, value:int, flags:GObject.ParamFlags) """
        pass

    def add_int_return_value(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_int_return_value(self, name:str, nick:str, blurb:str, min:int, max:int, value:int, flags:GObject.ParamFlags) """
        pass

    def add_item_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_item_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_item_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_item_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_item_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_item_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_layer_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_layer_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_layer_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_layer_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_layer_mask_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_layer_mask_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_layer_mask_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_layer_mask_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_layer_mask_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_layer_mask_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_layer_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_layer_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_menu_path(self, menu_path): # real signature unknown; restored from __doc__
        """ add_menu_path(self, menu_path:str) """
        pass

    def add_palette_argument(self, name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_palette_argument(self, name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Palette=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_palette_aux_argument(self, name, nick, blurb, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_palette_aux_argument(self, name:str, nick:str, blurb:str, default_value:Gimp.Palette=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_palette_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_palette_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_param_argument(self, name, nick, blurb, param_type, flags): # real signature unknown; restored from __doc__
        """ add_param_argument(self, name:str, nick:str, blurb:str, param_type:GType, flags:GObject.ParamFlags) """
        pass

    def add_param_aux_argument(self, name, nick, blurb, param_type, flags): # real signature unknown; restored from __doc__
        """ add_param_aux_argument(self, name:str, nick:str, blurb:str, param_type:GType, flags:GObject.ParamFlags) """
        pass

    def add_param_return_value(self, name, nick, blurb, param_type, flags): # real signature unknown; restored from __doc__
        """ add_param_return_value(self, name:str, nick:str, blurb:str, param_type:GType, flags:GObject.ParamFlags) """
        pass

    def add_parasite_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_parasite_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_parasite_aux_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_parasite_aux_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_parasite_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_parasite_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_path_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_path_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_path_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_path_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_path_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_path_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_pattern_argument(self, name, nick, blurb, none_ok, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_pattern_argument(self, name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Pattern=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_pattern_aux_argument(self, name, nick, blurb, default_value=None, default_to_context, flags): # real signature unknown; restored from __doc__
        """ add_pattern_aux_argument(self, name:str, nick:str, blurb:str, default_value:Gimp.Pattern=None, default_to_context:bool, flags:GObject.ParamFlags) """
        pass

    def add_pattern_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_pattern_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_resource_argument(self, name, nick, blurb, none_ok, default_value=None, flags): # real signature unknown; restored from __doc__
        """ add_resource_argument(self, name:str, nick:str, blurb:str, none_ok:bool, default_value:Gimp.Resource=None, flags:GObject.ParamFlags) """
        pass

    def add_resource_aux_argument(self, name, nick, blurb, default_value=None, flags): # real signature unknown; restored from __doc__
        """ add_resource_aux_argument(self, name:str, nick:str, blurb:str, default_value:Gimp.Resource=None, flags:GObject.ParamFlags) """
        pass

    def add_resource_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_resource_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_selection_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_selection_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_selection_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_selection_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_selection_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_selection_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_string_argument(self, name, nick, blurb, value, flags): # real signature unknown; restored from __doc__
        """ add_string_argument(self, name:str, nick:str, blurb:str, value:str, flags:GObject.ParamFlags) """
        pass

    def add_string_array_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_string_array_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_string_array_aux_argument(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_string_array_aux_argument(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_string_array_return_value(self, name, nick, blurb, flags): # real signature unknown; restored from __doc__
        """ add_string_array_return_value(self, name:str, nick:str, blurb:str, flags:GObject.ParamFlags) """
        pass

    def add_string_aux_argument(self, name, nick, blurb, value, flags): # real signature unknown; restored from __doc__
        """ add_string_aux_argument(self, name:str, nick:str, blurb:str, value:str, flags:GObject.ParamFlags) """
        pass

    def add_string_return_value(self, name, nick, blurb, value, flags): # real signature unknown; restored from __doc__
        """ add_string_return_value(self, name:str, nick:str, blurb:str, value:str, flags:GObject.ParamFlags) """
        pass

    def add_text_layer_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_text_layer_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_text_layer_aux_argument(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_text_layer_aux_argument(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_text_layer_return_value(self, name, nick, blurb, none_ok, flags): # real signature unknown; restored from __doc__
        """ add_text_layer_return_value(self, name:str, nick:str, blurb:str, none_ok:bool, flags:GObject.ParamFlags) """
        pass

    def add_uint_argument(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_uint_argument(self, name:str, nick:str, blurb:str, min:int, max:int, value:int, flags:GObject.ParamFlags) """
        pass

    def add_uint_aux_argument(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_uint_aux_argument(self, name:str, nick:str, blurb:str, min:int, max:int, value:int, flags:GObject.ParamFlags) """
        pass

    def add_uint_return_value(self, name, nick, blurb, min, max, value, flags): # real signature unknown; restored from __doc__
        """ add_uint_return_value(self, name:str, nick:str, blurb:str, min:int, max:int, value:int, flags:GObject.ParamFlags) """
        pass

    def add_unit_argument(self, name, nick, blurb, show_pixels, show_percent, value, flags): # real signature unknown; restored from __doc__
        """ add_unit_argument(self, name:str, nick:str, blurb:str, show_pixels:bool, show_percent:bool, value:Gimp.Unit, flags:GObject.ParamFlags) """
        pass

    def add_unit_aux_argument(self, name, nick, blurb, show_pixels, show_percent, value, flags): # real signature unknown; restored from __doc__
        """ add_unit_aux_argument(self, name:str, nick:str, blurb:str, show_pixels:bool, show_percent:bool, value:Gimp.Unit, flags:GObject.ParamFlags) """
        pass

    def add_unit_return_value(self, name, nick, blurb, show_pixels, show_percent, value, flags): # real signature unknown; restored from __doc__
        """ add_unit_return_value(self, name:str, nick:str, blurb:str, show_pixels:bool, show_percent:bool, value:Gimp.Unit, flags:GObject.ParamFlags) """
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

    def create_config(self): # real signature unknown; restored from __doc__
        """ create_config(self) -> Gimp.ProcedureConfig """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_install(self, *args, **kwargs): # real signature unknown
        """ install(self) """
        pass

    def do_run(self, *args, **kwargs): # real signature unknown
        """ run(self, args:Gimp.ValueArray) -> Gimp.ValueArray """
        pass

    def do_set_sensitivity(self, *args, **kwargs): # real signature unknown
        """ set_sensitivity(self, sensitivity_mask:int) -> bool """
        pass

    def do_uninstall(self, *args, **kwargs): # real signature unknown
        """ uninstall(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_argument(self, name): # real signature unknown; restored from __doc__
        """ find_argument(self, name:str) -> GObject.ParamSpec """
        pass

    def find_aux_argument(self, name): # real signature unknown; restored from __doc__
        """ find_aux_argument(self, name:str) -> GObject.ParamSpec """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_return_value(self, name): # real signature unknown; restored from __doc__
        """ find_return_value(self, name:str) -> GObject.ParamSpec """
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

    def get_arguments(self): # real signature unknown; restored from __doc__
        """ get_arguments(self) -> list """
        return []

    def get_argument_sync(self, arg_name): # real signature unknown; restored from __doc__
        """ get_argument_sync(self, arg_name:str) -> Gimp.ArgumentSync """
        pass

    def get_authors(self): # real signature unknown; restored from __doc__
        """ get_authors(self) -> str """
        return ""

    def get_aux_arguments(self): # real signature unknown; restored from __doc__
        """ get_aux_arguments(self) -> list """
        return []

    def get_blurb(self): # real signature unknown; restored from __doc__
        """ get_blurb(self) -> str """
        return ""

    def get_copyright(self): # real signature unknown; restored from __doc__
        """ get_copyright(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date(self): # real signature unknown; restored from __doc__
        """ get_date(self) -> str """
        return ""

    def get_extensions(self): # real signature unknown; restored from __doc__
        """ get_extensions(self) -> str """
        return ""

    def get_format_name(self): # real signature unknown; restored from __doc__
        """ get_format_name(self) -> str """
        return ""

    def get_handles_remote(self): # real signature unknown; restored from __doc__
        """ get_handles_remote(self) -> bool """
        return False

    def get_help(self): # real signature unknown; restored from __doc__
        """ get_help(self) -> str """
        return ""

    def get_help_id(self): # real signature unknown; restored from __doc__
        """ get_help_id(self) -> str """
        return ""

    def get_icon_file(self): # real signature unknown; restored from __doc__
        """ get_icon_file(self) -> Gio.File or None """
        pass

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str or None """
        return ""

    def get_icon_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_icon_pixbuf(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_icon_type(self): # real signature unknown; restored from __doc__
        """ get_icon_type(self) -> Gimp.IconType """
        pass

    def get_image_types(self): # real signature unknown; restored from __doc__
        """ get_image_types(self) -> str """
        return ""

    def get_magics(self): # real signature unknown; restored from __doc__
        """ get_magics(self) -> str """
        return ""

    def get_menu_label(self): # real signature unknown; restored from __doc__
        """ get_menu_label(self) -> str """
        return ""

    def get_menu_paths(self): # real signature unknown; restored from __doc__
        """ get_menu_paths(self) -> list """
        return []

    def get_mime_types(self): # real signature unknown; restored from __doc__
        """ get_mime_types(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_plug_in(self): # real signature unknown; restored from __doc__
        """ get_plug_in(self) -> Gimp.PlugIn """
        pass

    def get_prefixes(self): # real signature unknown; restored from __doc__
        """ get_prefixes(self) -> str """
        return ""

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_proc_type(self): # real signature unknown; restored from __doc__
        """ get_proc_type(self) -> Gimp.PDBProcType """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_return_values(self): # real signature unknown; restored from __doc__
        """ get_return_values(self) -> list """
        return []

    def get_sensitivity_mask(self): # real signature unknown; restored from __doc__
        """ get_sensitivity_mask(self) -> int """
        return 0

    def get_support_comment(self): # real signature unknown; restored from __doc__
        """ get_support_comment(self) -> bool """
        return False

    def get_support_exif(self): # real signature unknown; restored from __doc__
        """ get_support_exif(self) -> bool """
        return False

    def get_support_iptc(self): # real signature unknown; restored from __doc__
        """ get_support_iptc(self) -> bool """
        return False

    def get_support_profile(self): # real signature unknown; restored from __doc__
        """ get_support_profile(self) -> bool """
        return False

    def get_support_thumbnail(self): # real signature unknown; restored from __doc__
        """ get_support_thumbnail(self) -> bool """
        return False

    def get_support_xmp(self): # real signature unknown; restored from __doc__
        """ get_support_xmp(self) -> bool """
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

    def new(self, plug_in, name, proc_type, export_metadata, run_func, run_data=None): # real signature unknown; restored from __doc__
        """ new(plug_in:Gimp.PlugIn, name:str, proc_type:Gimp.PDBProcType, export_metadata:bool, run_func:Gimp.RunExportFunc, run_data=None) -> Gimp.Procedure """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_return_values(self, status, error=None): # real signature unknown; restored from __doc__
        """ new_return_values(self, status:Gimp.PDBStatusType, error:error=None) -> Gimp.ValueArray """
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

    def persistent_ready(self): # real signature unknown; restored from __doc__
        """ persistent_ready(self) """
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

    def run(self, config=None): # real signature unknown; restored from __doc__
        """ run(self, config:Gimp.ProcedureConfig=None) -> Gimp.ValueArray """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_argument_sync(self, arg_name, sync): # real signature unknown; restored from __doc__
        """ set_argument_sync(self, arg_name:str, sync:Gimp.ArgumentSync) """
        pass

    def set_attribution(self, authors, copyright, date): # real signature unknown; restored from __doc__
        """ set_attribution(self, authors:str, copyright:str, date:str) """
        pass

    def set_capabilities(self, capabilities, get_capabilities_func=None, get_capabilities_data=None): # real signature unknown; restored from __doc__
        """ set_capabilities(self, capabilities:Gimp.ExportCapabilities, get_capabilities_func:Gimp.ExportGetCapabilitiesFunc=None, get_capabilities_data=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_documentation(self, blurb, help=None, help_id=None): # real signature unknown; restored from __doc__
        """ set_documentation(self, blurb:str, help:str=None, help_id:str=None) """
        pass

    def set_extensions(self, extensions): # real signature unknown; restored from __doc__
        """ set_extensions(self, extensions:str) """
        pass

    def set_format_name(self, format_name): # real signature unknown; restored from __doc__
        """ set_format_name(self, format_name:str) """
        pass

    def set_handles_remote(self, handles_remote): # real signature unknown; restored from __doc__
        """ set_handles_remote(self, handles_remote:bool) """
        pass

    def set_icon_file(self, file=None): # real signature unknown; restored from __doc__
        """ set_icon_file(self, file:Gio.File=None) """
        pass

    def set_icon_name(self, icon_name=None): # real signature unknown; restored from __doc__
        """ set_icon_name(self, icon_name:str=None) """
        pass

    def set_icon_pixbuf(self, pixbuf=None): # real signature unknown; restored from __doc__
        """ set_icon_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf=None) """
        pass

    def set_image_types(self, image_types): # real signature unknown; restored from __doc__
        """ set_image_types(self, image_types:str) """
        pass

    def set_magics(self, magics): # real signature unknown; restored from __doc__
        """ set_magics(self, magics:str) """
        pass

    def set_menu_label(self, menu_label): # real signature unknown; restored from __doc__
        """ set_menu_label(self, menu_label:str) """
        pass

    def set_mime_types(self, mime_types): # real signature unknown; restored from __doc__
        """ set_mime_types(self, mime_types:str) """
        pass

    def set_prefixes(self, prefixes): # real signature unknown; restored from __doc__
        """ set_prefixes(self, prefixes:str) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sensitivity_mask(self, sensitivity_mask): # real signature unknown; restored from __doc__
        """ set_sensitivity_mask(self, sensitivity_mask:int) """
        pass

    def set_support_comment(self, supports): # real signature unknown; restored from __doc__
        """ set_support_comment(self, supports:bool) """
        pass

    def set_support_exif(self, supports): # real signature unknown; restored from __doc__
        """ set_support_exif(self, supports:bool) """
        pass

    def set_support_iptc(self, supports): # real signature unknown; restored from __doc__
        """ set_support_iptc(self, supports:bool) """
        pass

    def set_support_profile(self, supports): # real signature unknown; restored from __doc__
        """ set_support_profile(self, supports:bool) """
        pass

    def set_support_thumbnail(self, supports): # real signature unknown; restored from __doc__
        """ set_support_thumbnail(self, supports:bool) """
        pass

    def set_support_xmp(self, supports): # real signature unknown; restored from __doc__
        """ set_support_xmp(self, supports:bool) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001b64069dd50>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ExportProcedure), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpExportProcedure (1066677920)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'get_support_comment': gi.FunctionInfo(get_support_comment, bound=None), 'get_support_exif': gi.FunctionInfo(get_support_exif, bound=None), 'get_support_iptc': gi.FunctionInfo(get_support_iptc, bound=None), 'get_support_profile': gi.FunctionInfo(get_support_profile, bound=None), 'get_support_thumbnail': gi.FunctionInfo(get_support_thumbnail, bound=None), 'get_support_xmp': gi.FunctionInfo(get_support_xmp, bound=None), 'set_capabilities': gi.FunctionInfo(set_capabilities, bound=None), 'set_support_comment': gi.FunctionInfo(set_support_comment, bound=None), 'set_support_exif': gi.FunctionInfo(set_support_exif, bound=None), 'set_support_iptc': gi.FunctionInfo(set_support_iptc, bound=None), 'set_support_profile': gi.FunctionInfo(set_support_profile, bound=None), 'set_support_thumbnail': gi.FunctionInfo(set_support_thumbnail, bound=None), 'set_support_xmp': gi.FunctionInfo(set_support_xmp, bound=None)})"
    __gdoc__ = "Object GimpExportProcedure\n\nProperties from GimpExportProcedure:\n  capabilities -> GimpExportCapabilities: Supported image capabilities\n  supports-exif -> gboolean: Supports EXIF metadata storage\n  supports-iptc -> gboolean: Supports IPTC metadata storage\n  supports-xmp -> gboolean: Supports XMP metadata storage\n  supports-profile -> gboolean: Supports color profile storage\n  supports-thumbnail -> gboolean: Supports thumbnail storage\n  supports-comment -> gboolean: Supports comment storage\n\nProperties from GimpProcedure:\n  plug-in -> GimpPlugIn: Plug-In\n    The GimpPlugIn of this plug-in process\n  name -> gchararray: Name\n    The procedure's name\n  procedure-type -> GimpPDBProcType: Procedure type\n    The procedure's type\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpExportProcedure (1066677920)>'
    __info__ = ObjectInfo(ExportProcedure)


