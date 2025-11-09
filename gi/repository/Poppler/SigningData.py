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


class SigningData(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Poppler.SigningData
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Poppler.SigningData """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_background_color(self): # real signature unknown; restored from __doc__
        """ get_background_color(self) -> Poppler.Color """
        pass

    def get_border_color(self): # real signature unknown; restored from __doc__
        """ get_border_color(self) -> Poppler.Color """
        pass

    def get_border_width(self): # real signature unknown; restored from __doc__
        """ get_border_width(self) -> float """
        return 0.0

    def get_certificate_info(self): # real signature unknown; restored from __doc__
        """ get_certificate_info(self) -> Poppler.CertificateInfo """
        pass

    def get_destination_filename(self): # real signature unknown; restored from __doc__
        """ get_destination_filename(self) -> str """
        return ""

    def get_document_owner_password(self): # real signature unknown; restored from __doc__
        """ get_document_owner_password(self) -> str """
        return ""

    def get_document_user_password(self): # real signature unknown; restored from __doc__
        """ get_document_user_password(self) -> str """
        return ""

    def get_field_partial_name(self): # real signature unknown; restored from __doc__
        """ get_field_partial_name(self) -> str """
        return ""

    def get_font_color(self): # real signature unknown; restored from __doc__
        """ get_font_color(self) -> Poppler.Color """
        pass

    def get_font_size(self): # real signature unknown; restored from __doc__
        """ get_font_size(self) -> float """
        return 0.0

    def get_image_path(self): # real signature unknown; restored from __doc__
        """ get_image_path(self) -> str """
        return ""

    def get_left_font_size(self): # real signature unknown; restored from __doc__
        """ get_left_font_size(self) -> float """
        return 0.0

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> str """
        return ""

    def get_page(self): # real signature unknown; restored from __doc__
        """ get_page(self) -> int """
        return 0

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str """
        return ""

    def get_reason(self): # real signature unknown; restored from __doc__
        """ get_reason(self) -> str """
        return ""

    def get_signature_rectangle(self): # real signature unknown; restored from __doc__
        """ get_signature_rectangle(self) -> Poppler.Rectangle """
        pass

    def get_signature_text(self): # real signature unknown; restored from __doc__
        """ get_signature_text(self) -> str """
        return ""

    def get_signature_text_left(self): # real signature unknown; restored from __doc__
        """ get_signature_text_left(self) -> str """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Poppler.SigningData """
        pass

    def set_background_color(self, background_color): # real signature unknown; restored from __doc__
        """ set_background_color(self, background_color:Poppler.Color) """
        pass

    def set_border_color(self, border_color): # real signature unknown; restored from __doc__
        """ set_border_color(self, border_color:Poppler.Color) """
        pass

    def set_border_width(self, border_width): # real signature unknown; restored from __doc__
        """ set_border_width(self, border_width:float) """
        pass

    def set_certificate_info(self, certificate_info): # real signature unknown; restored from __doc__
        """ set_certificate_info(self, certificate_info:Poppler.CertificateInfo) """
        pass

    def set_destination_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_destination_filename(self, filename:str) """
        pass

    def set_document_owner_password(self, document_owner_password): # real signature unknown; restored from __doc__
        """ set_document_owner_password(self, document_owner_password:str) """
        pass

    def set_document_user_password(self, document_user_password): # real signature unknown; restored from __doc__
        """ set_document_user_password(self, document_user_password:str) """
        pass

    def set_field_partial_name(self, field_partial_name): # real signature unknown; restored from __doc__
        """ set_field_partial_name(self, field_partial_name:str) """
        pass

    def set_font_color(self, font_color): # real signature unknown; restored from __doc__
        """ set_font_color(self, font_color:Poppler.Color) """
        pass

    def set_font_size(self, font_size): # real signature unknown; restored from __doc__
        """ set_font_size(self, font_size:float) """
        pass

    def set_image_path(self, image_path): # real signature unknown; restored from __doc__
        """ set_image_path(self, image_path:str) """
        pass

    def set_left_font_size(self, font_size): # real signature unknown; restored from __doc__
        """ set_left_font_size(self, font_size:float) """
        pass

    def set_location(self, location): # real signature unknown; restored from __doc__
        """ set_location(self, location:str) """
        pass

    def set_page(self, page): # real signature unknown; restored from __doc__
        """ set_page(self, page:int) """
        pass

    def set_password(self, password): # real signature unknown; restored from __doc__
        """ set_password(self, password:str) """
        pass

    def set_reason(self, reason): # real signature unknown; restored from __doc__
        """ set_reason(self, reason:str) """
        pass

    def set_signature_rectangle(self, signature_rect): # real signature unknown; restored from __doc__
        """ set_signature_rectangle(self, signature_rect:Poppler.Rectangle) """
        pass

    def set_signature_text(self, signature_text): # real signature unknown; restored from __doc__
        """ set_signature_text(self, signature_text:str) """
        pass

    def set_signature_text_left(self, signature_text_left): # real signature unknown; restored from __doc__
        """ set_signature_text_left(self, signature_text_left:str) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Poppler.SigningData """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SigningData), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerSigningData (3984819104)>, '__dict__': <attribute '__dict__' of 'SigningData' objects>, '__weakref__': <attribute '__weakref__' of 'SigningData' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_background_color': gi.FunctionInfo(get_background_color, bound=None), 'get_border_color': gi.FunctionInfo(get_border_color, bound=None), 'get_border_width': gi.FunctionInfo(get_border_width, bound=None), 'get_certificate_info': gi.FunctionInfo(get_certificate_info, bound=None), 'get_destination_filename': gi.FunctionInfo(get_destination_filename, bound=None), 'get_document_owner_password': gi.FunctionInfo(get_document_owner_password, bound=None), 'get_document_user_password': gi.FunctionInfo(get_document_user_password, bound=None), 'get_field_partial_name': gi.FunctionInfo(get_field_partial_name, bound=None), 'get_font_color': gi.FunctionInfo(get_font_color, bound=None), 'get_font_size': gi.FunctionInfo(get_font_size, bound=None), 'get_image_path': gi.FunctionInfo(get_image_path, bound=None), 'get_left_font_size': gi.FunctionInfo(get_left_font_size, bound=None), 'get_location': gi.FunctionInfo(get_location, bound=None), 'get_page': gi.FunctionInfo(get_page, bound=None), 'get_password': gi.FunctionInfo(get_password, bound=None), 'get_reason': gi.FunctionInfo(get_reason, bound=None), 'get_signature_rectangle': gi.FunctionInfo(get_signature_rectangle, bound=None), 'get_signature_text': gi.FunctionInfo(get_signature_text, bound=None), 'get_signature_text_left': gi.FunctionInfo(get_signature_text_left, bound=None), 'set_background_color': gi.FunctionInfo(set_background_color, bound=None), 'set_border_color': gi.FunctionInfo(set_border_color, bound=None), 'set_border_width': gi.FunctionInfo(set_border_width, bound=None), 'set_certificate_info': gi.FunctionInfo(set_certificate_info, bound=None), 'set_destination_filename': gi.FunctionInfo(set_destination_filename, bound=None), 'set_document_owner_password': gi.FunctionInfo(set_document_owner_password, bound=None), 'set_document_user_password': gi.FunctionInfo(set_document_user_password, bound=None), 'set_field_partial_name': gi.FunctionInfo(set_field_partial_name, bound=None), 'set_font_color': gi.FunctionInfo(set_font_color, bound=None), 'set_font_size': gi.FunctionInfo(set_font_size, bound=None), 'set_image_path': gi.FunctionInfo(set_image_path, bound=None), 'set_left_font_size': gi.FunctionInfo(set_left_font_size, bound=None), 'set_location': gi.FunctionInfo(set_location, bound=None), 'set_page': gi.FunctionInfo(set_page, bound=None), 'set_password': gi.FunctionInfo(set_password, bound=None), 'set_reason': gi.FunctionInfo(set_reason, bound=None), 'set_signature_rectangle': gi.FunctionInfo(set_signature_rectangle, bound=None), 'set_signature_text': gi.FunctionInfo(set_signature_text, bound=None), 'set_signature_text_left': gi.FunctionInfo(set_signature_text_left, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000001deefdd7880>})"
    __gtype__ = None # (!) real value is '<GType PopplerSigningData (3984819104)>'
    __info__ = StructInfo(SigningData)


