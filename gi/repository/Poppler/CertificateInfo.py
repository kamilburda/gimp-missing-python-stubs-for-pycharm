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


class CertificateInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Poppler.CertificateInfo
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Poppler.CertificateInfo """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_expiration_time(self): # real signature unknown; restored from __doc__
        """ get_expiration_time(self) -> GLib.DateTime """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_issuance_time(self): # real signature unknown; restored from __doc__
        """ get_issuance_time(self) -> GLib.DateTime """
        pass

    def get_issuer_common_name(self): # real signature unknown; restored from __doc__
        """ get_issuer_common_name(self) -> str """
        return ""

    def get_issuer_email(self): # real signature unknown; restored from __doc__
        """ get_issuer_email(self) -> str """
        return ""

    def get_issuer_organization(self): # real signature unknown; restored from __doc__
        """ get_issuer_organization(self) -> str """
        return ""

    def get_subject_common_name(self): # real signature unknown; restored from __doc__
        """ get_subject_common_name(self) -> str """
        return ""

    def get_subject_email(self): # real signature unknown; restored from __doc__
        """ get_subject_email(self) -> str """
        return ""

    def get_subject_organization(self): # real signature unknown; restored from __doc__
        """ get_subject_organization(self) -> str """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Poppler.CertificateInfo """
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
        """ new() -> Poppler.CertificateInfo """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CertificateInfo), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerCertificateInfo (3988361584)>, '__dict__': <attribute '__dict__' of 'CertificateInfo' objects>, '__weakref__': <attribute '__weakref__' of 'CertificateInfo' objects>, '__doc__': None, 'new': gi.FunctionInfo(new, bound=None), 'copy': gi.FunctionInfo(copy, bound=None), 'free': gi.FunctionInfo(free, bound=None), 'get_expiration_time': gi.FunctionInfo(get_expiration_time, bound=None), 'get_id': gi.FunctionInfo(get_id, bound=None), 'get_issuance_time': gi.FunctionInfo(get_issuance_time, bound=None), 'get_issuer_common_name': gi.FunctionInfo(get_issuer_common_name, bound=None), 'get_issuer_email': gi.FunctionInfo(get_issuer_email, bound=None), 'get_issuer_organization': gi.FunctionInfo(get_issuer_organization, bound=None), 'get_subject_common_name': gi.FunctionInfo(get_subject_common_name, bound=None), 'get_subject_email': gi.FunctionInfo(get_subject_email, bound=None), 'get_subject_organization': gi.FunctionInfo(get_subject_organization, bound=None), '__new__': <staticmethod(gi.FunctionInfo(new, bound=None))>, '__init__': <function nothing at 0x000001deefdd7880>})"
    __gtype__ = None # (!) real value is '<GType PopplerCertificateInfo (3988361584)>'
    __info__ = StructInfo(CertificateInfo)


