# encoding: utf-8
# module gi.repository.Gimp
# from C:\Program Files\GIMP 2.99\lib\girepository-1.0\Gimp-3.0.typelib
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


class Procedure(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Procedure(**properties)
        new(plug_in:Gimp.PlugIn, name:str, proc_type:Gimp.PDBProcType, run_func:Gimp.RunFunc, run_data=None) -> Gimp.Procedure
    """
    def add_argument(self, pspec): # real signature unknown; restored from __doc__
        """ add_argument(self, pspec:GObject.ParamSpec) -> GObject.ParamSpec """
        pass

    def add_argument_from_property(self, config, prop_name): # real signature unknown; restored from __doc__
        """ add_argument_from_property(self, config:GObject.Object, prop_name:str) -> GObject.ParamSpec """
        pass

    def add_aux_argument(self, pspec): # real signature unknown; restored from __doc__
        """ add_aux_argument(self, pspec:GObject.ParamSpec) -> GObject.ParamSpec """
        pass

    def add_aux_argument_from_property(self, config, prop_name): # real signature unknown; restored from __doc__
        """ add_aux_argument_from_property(self, config:GObject.Object, prop_name:str) -> GObject.ParamSpec """
        pass

    def add_menu_path(self, menu_path): # real signature unknown; restored from __doc__
        """ add_menu_path(self, menu_path:str) """
        pass

    def add_return_value(self, pspec): # real signature unknown; restored from __doc__
        """ add_return_value(self, pspec:GObject.ParamSpec) -> GObject.ParamSpec """
        pass

    def add_return_value_from_property(self, config, prop_name): # real signature unknown; restored from __doc__
        """ add_return_value_from_property(self, config:GObject.Object, prop_name:str) -> GObject.ParamSpec """
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

    def extension_ready(self): # real signature unknown; restored from __doc__
        """ extension_ready(self) """
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
        """ get_arguments(self) -> list, n_arguments:int """
        return []

    def get_argument_sync(self, arg_name): # real signature unknown; restored from __doc__
        """ get_argument_sync(self, arg_name:str) -> Gimp.ArgumentSync """
        pass

    def get_authors(self): # real signature unknown; restored from __doc__
        """ get_authors(self) -> str """
        return ""

    def get_aux_arguments(self): # real signature unknown; restored from __doc__
        """ get_aux_arguments(self) -> list, n_arguments:int """
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

    def get_menu_label(self): # real signature unknown; restored from __doc__
        """ get_menu_label(self) -> str """
        return ""

    def get_menu_paths(self): # real signature unknown; restored from __doc__
        """ get_menu_paths(self) -> list """
        return []

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_plug_in(self): # real signature unknown; restored from __doc__
        """ get_plug_in(self) -> Gimp.PlugIn """
        pass

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
        """ get_return_values(self) -> list, n_return_values:int """
        return []

    def get_sensitivity_mask(self): # real signature unknown; restored from __doc__
        """ get_sensitivity_mask(self) -> int """
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, plug_in, name, proc_type, run_func, run_data=None): # real signature unknown; restored from __doc__
        """ new(plug_in:Gimp.PlugIn, name:str, proc_type:Gimp.PDBProcType, run_func:Gimp.RunFunc, run_data=None) -> Gimp.Procedure """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_arguments(self): # real signature unknown; restored from __doc__
        """ new_arguments(self) -> Gimp.ValueArray """
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

    def run(self, args): # real signature unknown; restored from __doc__
        """ run(self, args:Gimp.ValueArray) -> Gimp.ValueArray """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_documentation(self, blurb, help, help_id): # real signature unknown; restored from __doc__
        """ set_documentation(self, blurb:str, help:str, help_id:str) """
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

    def set_menu_label(self, menu_label): # real signature unknown; restored from __doc__
        """ set_menu_label(self, menu_label:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sensitivity_mask(self, sensitivity_mask): # real signature unknown; restored from __doc__
        """ set_sensitivity_mask(self, sensitivity_mask:int) """
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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001e82e1c6050>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Procedure), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpProcedure (769169280)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'add_argument': gi.FunctionInfo(add_argument, bound=None), 'add_argument_from_property': gi.FunctionInfo(add_argument_from_property, bound=None), 'add_aux_argument': gi.FunctionInfo(add_aux_argument, bound=None), 'add_aux_argument_from_property': gi.FunctionInfo(add_aux_argument_from_property, bound=None), 'add_menu_path': gi.FunctionInfo(add_menu_path, bound=None), 'add_return_value': gi.FunctionInfo(add_return_value, bound=None), 'add_return_value_from_property': gi.FunctionInfo(add_return_value_from_property, bound=None), 'create_config': gi.FunctionInfo(create_config, bound=None), 'extension_ready': gi.FunctionInfo(extension_ready, bound=None), 'find_argument': gi.FunctionInfo(find_argument, bound=None), 'find_aux_argument': gi.FunctionInfo(find_aux_argument, bound=None), 'find_return_value': gi.FunctionInfo(find_return_value, bound=None), 'get_argument_sync': gi.FunctionInfo(get_argument_sync, bound=None), 'get_arguments': gi.FunctionInfo(get_arguments, bound=None), 'get_authors': gi.FunctionInfo(get_authors, bound=None), 'get_aux_arguments': gi.FunctionInfo(get_aux_arguments, bound=None), 'get_blurb': gi.FunctionInfo(get_blurb, bound=None), 'get_copyright': gi.FunctionInfo(get_copyright, bound=None), 'get_date': gi.FunctionInfo(get_date, bound=None), 'get_help': gi.FunctionInfo(get_help, bound=None), 'get_help_id': gi.FunctionInfo(get_help_id, bound=None), 'get_icon_file': gi.FunctionInfo(get_icon_file, bound=None), 'get_icon_name': gi.FunctionInfo(get_icon_name, bound=None), 'get_icon_pixbuf': gi.FunctionInfo(get_icon_pixbuf, bound=None), 'get_icon_type': gi.FunctionInfo(get_icon_type, bound=None), 'get_image_types': gi.FunctionInfo(get_image_types, bound=None), 'get_menu_label': gi.FunctionInfo(get_menu_label, bound=None), 'get_menu_paths': gi.FunctionInfo(get_menu_paths, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'get_plug_in': gi.FunctionInfo(get_plug_in, bound=None), 'get_proc_type': gi.FunctionInfo(get_proc_type, bound=None), 'get_return_values': gi.FunctionInfo(get_return_values, bound=None), 'get_sensitivity_mask': gi.FunctionInfo(get_sensitivity_mask, bound=None), 'new_arguments': gi.FunctionInfo(new_arguments, bound=None), 'new_return_values': gi.FunctionInfo(new_return_values, bound=None), 'run': gi.FunctionInfo(run, bound=None), 'set_argument_sync': gi.FunctionInfo(set_argument_sync, bound=None), 'set_attribution': gi.FunctionInfo(set_attribution, bound=None), 'set_documentation': gi.FunctionInfo(set_documentation, bound=None), 'set_icon_file': gi.FunctionInfo(set_icon_file, bound=None), 'set_icon_name': gi.FunctionInfo(set_icon_name, bound=None), 'set_icon_pixbuf': gi.FunctionInfo(set_icon_pixbuf, bound=None), 'set_image_types': gi.FunctionInfo(set_image_types, bound=None), 'set_menu_label': gi.FunctionInfo(set_menu_label, bound=None), 'set_sensitivity_mask': gi.FunctionInfo(set_sensitivity_mask, bound=None), 'do_install': gi.VFuncInfo(install, bound=None), 'do_run': gi.VFuncInfo(run, bound=None), 'do_set_sensitivity': gi.VFuncInfo(set_sensitivity, bound=None), 'do_uninstall': gi.VFuncInfo(uninstall, bound=None), 'parent_instance': <property object at 0x000001e82e2cb8d0>, 'priv': <property object at 0x000001e82e2cb9c0>})"
    __gdoc__ = "Object GimpProcedure\n\nProperties from GimpProcedure:\n  plug-in -> GimpPlugIn: Plug-In\n    The GimpPlugIn of this plug-in process\n  name -> gchararray: Name\n    The procedure's name\n  procedure-type -> GimpPDBProcType: Procedure type\n    The procedure's type\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpProcedure (769169280)>'
    __info__ = ObjectInfo(Procedure)


