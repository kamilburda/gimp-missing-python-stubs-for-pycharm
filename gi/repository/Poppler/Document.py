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


class Document(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Document(**properties)
        new_from_bytes(bytes:GLib.Bytes, password:str=None) -> Poppler.Document
        new_from_data(data:list, password:str=None) -> Poppler.Document
        new_from_file(uri:str, password:str=None) -> Poppler.Document
        new_from_gfile(file:Gio.File, password:str=None, cancellable:Gio.Cancellable=None) -> Poppler.Document
        new_from_stream(stream:Gio.InputStream, length:int, password:str=None, cancellable:Gio.Cancellable=None) -> Poppler.Document
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

    def create_dests_tree(self): # real signature unknown; restored from __doc__
        """ create_dests_tree(self) -> GLib.Tree or None """
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

    def find_dest(self, link_name): # real signature unknown; restored from __doc__
        """ find_dest(self, link_name:str) -> Poppler.Dest """
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

    def get_attachments(self): # real signature unknown; restored from __doc__
        """ get_attachments(self) -> list """
        return []

    def get_author(self): # real signature unknown; restored from __doc__
        """ get_author(self) -> str """
        return ""

    def get_creation_date(self): # real signature unknown; restored from __doc__
        """ get_creation_date(self) -> int """
        return 0

    def get_creation_date_time(self): # real signature unknown; restored from __doc__
        """ get_creation_date_time(self) -> GLib.DateTime or None """
        pass

    def get_creator(self): # real signature unknown; restored from __doc__
        """ get_creator(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_form_field(self, id): # real signature unknown; restored from __doc__
        """ get_form_field(self, id:int) -> Poppler.FormField """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> bool, permanent_id:str, update_id:str """
        return False

    def get_keywords(self): # real signature unknown; restored from __doc__
        """ get_keywords(self) -> str """
        return ""

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> str """
        return ""

    def get_modification_date(self): # real signature unknown; restored from __doc__
        """ get_modification_date(self) -> int """
        return 0

    def get_modification_date_time(self): # real signature unknown; restored from __doc__
        """ get_modification_date_time(self) -> GLib.DateTime or None """
        pass

    def get_n_attachments(self): # real signature unknown; restored from __doc__
        """ get_n_attachments(self) -> int """
        return 0

    def get_n_pages(self): # real signature unknown; restored from __doc__
        """ get_n_pages(self) -> int """
        return 0

    def get_n_signatures(self): # real signature unknown; restored from __doc__
        """ get_n_signatures(self) -> int """
        return 0

    def get_page(self, index): # real signature unknown; restored from __doc__
        """ get_page(self, index:int) -> Poppler.Page """
        pass

    def get_page_by_label(self, label): # real signature unknown; restored from __doc__
        """ get_page_by_label(self, label:str) -> Poppler.Page """
        pass

    def get_page_layout(self): # real signature unknown; restored from __doc__
        """ get_page_layout(self) -> Poppler.PageLayout """
        pass

    def get_page_mode(self): # real signature unknown; restored from __doc__
        """ get_page_mode(self) -> Poppler.PageMode """
        pass

    def get_pdf_conformance(self): # real signature unknown; restored from __doc__
        """ get_pdf_conformance(self) -> Poppler.PDFConformance """
        pass

    def get_pdf_part(self): # real signature unknown; restored from __doc__
        """ get_pdf_part(self) -> Poppler.PDFPart """
        pass

    def get_pdf_subtype(self): # real signature unknown; restored from __doc__
        """ get_pdf_subtype(self) -> Poppler.PDFSubtype """
        pass

    def get_pdf_subtype_string(self): # real signature unknown; restored from __doc__
        """ get_pdf_subtype_string(self) -> str or None """
        return ""

    def get_pdf_version(self): # real signature unknown; restored from __doc__
        """ get_pdf_version(self) -> major_version:int, minor_version:int """
        pass

    def get_pdf_version_string(self): # real signature unknown; restored from __doc__
        """ get_pdf_version_string(self) -> str """
        return ""

    def get_permissions(self): # real signature unknown; restored from __doc__
        """ get_permissions(self) -> Poppler.Permissions """
        pass

    def get_print_duplex(self): # real signature unknown; restored from __doc__
        """ get_print_duplex(self) -> Poppler.PrintDuplex """
        pass

    def get_print_n_copies(self): # real signature unknown; restored from __doc__
        """ get_print_n_copies(self) -> int """
        return 0

    def get_print_page_ranges(self): # real signature unknown; restored from __doc__
        """ get_print_page_ranges(self) -> list """
        return []

    def get_print_scaling(self): # real signature unknown; restored from __doc__
        """ get_print_scaling(self) -> Poppler.PrintScaling """
        pass

    def get_producer(self): # real signature unknown; restored from __doc__
        """ get_producer(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_signature_fields(self): # real signature unknown; restored from __doc__
        """ get_signature_fields(self) -> list """
        return []

    def get_subject(self): # real signature unknown; restored from __doc__
        """ get_subject(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

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

    def has_attachments(self): # real signature unknown; restored from __doc__
        """ has_attachments(self) -> bool """
        return False

    def has_javascript(self): # real signature unknown; restored from __doc__
        """ has_javascript(self) -> bool """
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

    def is_linearized(self): # real signature unknown; restored from __doc__
        """ is_linearized(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_bytes(self, bytes, password=None): # real signature unknown; restored from __doc__
        """ new_from_bytes(bytes:GLib.Bytes, password:str=None) -> Poppler.Document """
        pass

    def new_from_data(self, data, password=None): # real signature unknown; restored from __doc__
        """ new_from_data(data:list, password:str=None) -> Poppler.Document """
        pass

    def new_from_file(self, uri, password=None): # real signature unknown; restored from __doc__
        """ new_from_file(uri:str, password:str=None) -> Poppler.Document """
        pass

    def new_from_gfile(self, file, password=None, cancellable=None): # real signature unknown; restored from __doc__
        """ new_from_gfile(file:Gio.File, password:str=None, cancellable:Gio.Cancellable=None) -> Poppler.Document """
        pass

    def new_from_stream(self, stream, length, password=None, cancellable=None): # real signature unknown; restored from __doc__
        """ new_from_stream(stream:Gio.InputStream, length:int, password:str=None, cancellable:Gio.Cancellable=None) -> Poppler.Document """
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

    def reset_form(self, fields=None, exclude_fields): # real signature unknown; restored from __doc__
        """ reset_form(self, fields:list=None, exclude_fields:bool) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def save(self, uri): # real signature unknown; restored from __doc__
        """ save(self, uri:str) -> bool """
        return False

    def save_a_copy(self, uri): # real signature unknown; restored from __doc__
        """ save_a_copy(self, uri:str) -> bool """
        return False

    def set_author(self, author): # real signature unknown; restored from __doc__
        """ set_author(self, author:str) """
        pass

    def set_creation_date(self, creation_date): # real signature unknown; restored from __doc__
        """ set_creation_date(self, creation_date:int) """
        pass

    def set_creation_date_time(self, creation_datetime=None): # real signature unknown; restored from __doc__
        """ set_creation_date_time(self, creation_datetime:GLib.DateTime=None) """
        pass

    def set_creator(self, creator): # real signature unknown; restored from __doc__
        """ set_creator(self, creator:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_keywords(self, keywords): # real signature unknown; restored from __doc__
        """ set_keywords(self, keywords:str) """
        pass

    def set_modification_date(self, modification_date): # real signature unknown; restored from __doc__
        """ set_modification_date(self, modification_date:int) """
        pass

    def set_modification_date_time(self, modification_datetime=None): # real signature unknown; restored from __doc__
        """ set_modification_date_time(self, modification_datetime:GLib.DateTime=None) """
        pass

    def set_producer(self, producer): # real signature unknown; restored from __doc__
        """ set_producer(self, producer:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_subject(self, subject): # real signature unknown; restored from __doc__
        """ set_subject(self, subject:str) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def sign(self, signing_data, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ sign(self, signing_data:Poppler.SigningData, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def sign_finish(self, result): # real signature unknown; restored from __doc__
        """ sign_finish(self, result:Gio.AsyncResult) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001deee3bffa0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Document), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerDocument (3988361472)>, '__doc__': None, '__gsignals__': {}, 'new_from_bytes': gi.FunctionInfo(new_from_bytes, bound=None), 'new_from_data': gi.FunctionInfo(new_from_data, bound=None), 'new_from_file': gi.FunctionInfo(new_from_file, bound=None), 'new_from_gfile': gi.FunctionInfo(new_from_gfile, bound=None), 'new_from_stream': gi.FunctionInfo(new_from_stream, bound=None), 'create_dests_tree': gi.FunctionInfo(create_dests_tree, bound=None), 'find_dest': gi.FunctionInfo(find_dest, bound=None), 'get_attachments': gi.FunctionInfo(get_attachments, bound=None), 'get_author': gi.FunctionInfo(get_author, bound=None), 'get_creation_date': gi.FunctionInfo(get_creation_date, bound=None), 'get_creation_date_time': gi.FunctionInfo(get_creation_date_time, bound=None), 'get_creator': gi.FunctionInfo(get_creator, bound=None), 'get_form_field': gi.FunctionInfo(get_form_field, bound=None), 'get_id': gi.FunctionInfo(get_id, bound=None), 'get_keywords': gi.FunctionInfo(get_keywords, bound=None), 'get_metadata': gi.FunctionInfo(get_metadata, bound=None), 'get_modification_date': gi.FunctionInfo(get_modification_date, bound=None), 'get_modification_date_time': gi.FunctionInfo(get_modification_date_time, bound=None), 'get_n_attachments': gi.FunctionInfo(get_n_attachments, bound=None), 'get_n_pages': gi.FunctionInfo(get_n_pages, bound=None), 'get_n_signatures': gi.FunctionInfo(get_n_signatures, bound=None), 'get_page': gi.FunctionInfo(get_page, bound=None), 'get_page_by_label': gi.FunctionInfo(get_page_by_label, bound=None), 'get_page_layout': gi.FunctionInfo(get_page_layout, bound=None), 'get_page_mode': gi.FunctionInfo(get_page_mode, bound=None), 'get_pdf_conformance': gi.FunctionInfo(get_pdf_conformance, bound=None), 'get_pdf_part': gi.FunctionInfo(get_pdf_part, bound=None), 'get_pdf_subtype': gi.FunctionInfo(get_pdf_subtype, bound=None), 'get_pdf_subtype_string': gi.FunctionInfo(get_pdf_subtype_string, bound=None), 'get_pdf_version': gi.FunctionInfo(get_pdf_version, bound=None), 'get_pdf_version_string': gi.FunctionInfo(get_pdf_version_string, bound=None), 'get_permissions': gi.FunctionInfo(get_permissions, bound=None), 'get_print_duplex': gi.FunctionInfo(get_print_duplex, bound=None), 'get_print_n_copies': gi.FunctionInfo(get_print_n_copies, bound=None), 'get_print_page_ranges': gi.FunctionInfo(get_print_page_ranges, bound=None), 'get_print_scaling': gi.FunctionInfo(get_print_scaling, bound=None), 'get_producer': gi.FunctionInfo(get_producer, bound=None), 'get_signature_fields': gi.FunctionInfo(get_signature_fields, bound=None), 'get_subject': gi.FunctionInfo(get_subject, bound=None), 'get_title': gi.FunctionInfo(get_title, bound=None), 'has_attachments': gi.FunctionInfo(has_attachments, bound=None), 'has_javascript': gi.FunctionInfo(has_javascript, bound=None), 'is_linearized': gi.FunctionInfo(is_linearized, bound=None), 'reset_form': gi.FunctionInfo(reset_form, bound=None), 'save': gi.FunctionInfo(save, bound=None), 'save_a_copy': gi.FunctionInfo(save_a_copy, bound=None), 'set_author': gi.FunctionInfo(set_author, bound=None), 'set_creation_date': gi.FunctionInfo(set_creation_date, bound=None), 'set_creation_date_time': gi.FunctionInfo(set_creation_date_time, bound=None), 'set_creator': gi.FunctionInfo(set_creator, bound=None), 'set_keywords': gi.FunctionInfo(set_keywords, bound=None), 'set_modification_date': gi.FunctionInfo(set_modification_date, bound=None), 'set_modification_date_time': gi.FunctionInfo(set_modification_date_time, bound=None), 'set_producer': gi.FunctionInfo(set_producer, bound=None), 'set_subject': gi.FunctionInfo(set_subject, bound=None), 'set_title': gi.FunctionInfo(set_title, bound=None), 'sign': gi.FunctionInfo(sign, bound=None), 'sign_finish': gi.FunctionInfo(sign_finish, bound=None)})"
    __gdoc__ = 'Object PopplerDocument\n\nProperties from PopplerDocument:\n  title -> gchararray: Document Title\n    The title of the document\n  format -> gchararray: PDF Format\n    The PDF version of the document\n  format-major -> guint: PDF Format Major\n    The PDF major version number of the document\n  format-minor -> guint: PDF Format Minor\n    The PDF minor version number of the document\n  subtype -> PopplerPDFSubtype: PDF Format Subtype Type\n    The PDF subtype of the document\n  subtype-string -> gchararray: PDF Format Subtype\n    The PDF subtype of the document\n  subtype-part -> PopplerPDFPart: PDF Format Subtype Part\n    The part of PDF conformance\n  subtype-conformance -> PopplerPDFConformance: PDF Format Subtype Conformance\n    The conformance level of PDF subtype\n  author -> gchararray: Author\n    The author of the document\n  subject -> gchararray: Subject\n    Subjects the document touches\n  keywords -> gchararray: Keywords\n    Keywords\n  creator -> gchararray: Creator\n    The software that created the document\n  producer -> gchararray: Producer\n    The software that converted the document\n  creation-date -> gint: Creation Date\n    The date and time the document was created\n  mod-date -> gint: Modification Date\n    The date and time the document was modified\n  linearized -> gboolean: Fast Web View Enabled\n    Is the document optimized for web viewing?\n  page-layout -> PopplerPageLayout: Page Layout\n    Initial Page Layout\n  page-mode -> PopplerPageMode: Page Mode\n    Page Mode\n  viewer-preferences -> PopplerViewerPreferences: Viewer Preferences\n    Viewer Preferences\n  permissions -> PopplerPermissions: Permissions\n    Permissions\n  metadata -> gchararray: XML Metadata\n    Embedded XML metadata\n  print-scaling -> PopplerPrintScaling: Print Scaling\n    Print Scaling Viewer Preference\n  print-duplex -> PopplerPrintDuplex: Print Duplex\n    Duplex Viewer Preference\n  print-n-copies -> gint: Number of Copies to Print\n    Number of Copies Viewer Preference\n  creation-datetime -> GDateTime: Creation DateTime\n    The date and time the document was created\n  mod-datetime -> GDateTime: Modification DateTime\n    The date and time the document was modified\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PopplerDocument (3988361472)>'
    __info__ = ObjectInfo(Document)


