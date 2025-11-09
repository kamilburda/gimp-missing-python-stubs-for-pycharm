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


# Variables with simple values

ANNOT_TEXT_ICON_CIRCLE = 'Circle'
ANNOT_TEXT_ICON_COMMENT = 'Comment'
ANNOT_TEXT_ICON_CROSS = 'Cross'
ANNOT_TEXT_ICON_HELP = 'Help'
ANNOT_TEXT_ICON_INSERT = 'Insert'
ANNOT_TEXT_ICON_KEY = 'Key'

ANNOT_TEXT_ICON_NEW_PARAGRAPH = 'NewParagraph'

ANNOT_TEXT_ICON_NOTE = 'Note'
ANNOT_TEXT_ICON_PARAGRAPH = 'Paragraph'

HAS_CAIRO = 1

MAJOR_VERSION = 25

MICRO_VERSION = 0

MINOR_VERSION = 1

_namespace = 'Poppler'

_version = '0.18'

__weakref__ = None

# functions

def date_parse(date, timet): # real signature unknown; restored from __doc__
    """ date_parse(date:str, timet:int) -> bool """
    return False

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def get_available_signing_certificates(): # real signature unknown; restored from __doc__
    """ get_available_signing_certificates() -> list """
    return []

def get_backend(): # real signature unknown; restored from __doc__
    """ get_backend() -> Poppler.Backend """
    pass

def get_certificate_info_by_id(id): # real signature unknown; restored from __doc__
    """ get_certificate_info_by_id(id:str) -> Poppler.CertificateInfo """
    pass

def get_nss_dir(): # real signature unknown; restored from __doc__
    """ get_nss_dir() -> str """
    return ""

def get_version(): # real signature unknown; restored from __doc__
    """ get_version() -> str """
    return ""

def named_dest_from_bytestring(data): # real signature unknown; restored from __doc__
    """ named_dest_from_bytestring(data:list) -> str """
    return ""

def named_dest_to_bytestring(name): # real signature unknown; restored from __doc__
    """ named_dest_to_bytestring(name:str) -> list or None """
    return []

def set_nss_dir(path): # real signature unknown; restored from __doc__
    """ set_nss_dir(path:str) """
    pass

def set_nss_password_callback(func): # real signature unknown; restored from __doc__
    """ set_nss_password_callback(func:Poppler.NssPasswordFunc) """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """
    Default object formatter.
    
    Return str(self) if format_spec is empty. Raise TypeError otherwise.
    """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __getstate__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .Action import Action
from .ActionAny import ActionAny
from .ActionGotoDest import ActionGotoDest
from .ActionGotoRemote import ActionGotoRemote
from .ActionJavascript import ActionJavascript
from .ActionLaunch import ActionLaunch
from .ActionLayer import ActionLayer
from .ActionLayerAction import ActionLayerAction
from .ActionMovie import ActionMovie
from .ActionMovieOperation import ActionMovieOperation
from .ActionNamed import ActionNamed
from .ActionOCGState import ActionOCGState
from .ActionRendition import ActionRendition
from .ActionResetForm import ActionResetForm
from .ActionType import ActionType
from .ActionUri import ActionUri
from .AdditionalActionType import AdditionalActionType
from .Annot import Annot
from .AnnotCalloutLine import AnnotCalloutLine
from .AnnotMarkup import AnnotMarkup
from .AnnotCircle import AnnotCircle
from .AnnotExternalDataType import AnnotExternalDataType
from .AnnotFileAttachment import AnnotFileAttachment
from .AnnotFlag import AnnotFlag
from .AnnotFreeText import AnnotFreeText
from .AnnotFreeTextQuadding import AnnotFreeTextQuadding
from .AnnotLine import AnnotLine
from .AnnotMapping import AnnotMapping
from .AnnotMarkupReplyType import AnnotMarkupReplyType
from .AnnotMovie import AnnotMovie
from .AnnotScreen import AnnotScreen
from .AnnotSquare import AnnotSquare
from .AnnotStamp import AnnotStamp
from .AnnotStampIcon import AnnotStampIcon
from .AnnotText import AnnotText
from .AnnotTextMarkup import AnnotTextMarkup
from .AnnotTextState import AnnotTextState
from .AnnotType import AnnotType
from .Attachment import Attachment
from .AttachmentClass import AttachmentClass
from .Backend import Backend
from .CertificateInfo import CertificateInfo
from .CertificateStatus import CertificateStatus
from .Color import Color
from .Dest import Dest
from .DestType import DestType
from .Document import Document
from .Error import Error
from .FindFlags import FindFlags
from .FontDescription import FontDescription
from .FontInfo import FontInfo
from .FontsIter import FontsIter
from .FontType import FontType
from .FormButtonType import FormButtonType
from .FormChoiceType import FormChoiceType
from .FormField import FormField
from .FormFieldMapping import FormFieldMapping
from .FormFieldType import FormFieldType
from .FormTextType import FormTextType
from .ImageMapping import ImageMapping
from .IndexIter import IndexIter
from .Layer import Layer
from .LayersIter import LayersIter
from .LinkMapping import LinkMapping
from .Media import Media
from .Movie import Movie
from .MoviePlayMode import MoviePlayMode
from .Page import Page
from .PageLayout import PageLayout
from .PageMode import PageMode
from .PageRange import PageRange
from .PageTransition import PageTransition
from .PageTransitionAlignment import PageTransitionAlignment
from .PageTransitionDirection import PageTransitionDirection
from .PageTransitionType import PageTransitionType
from .PDFConformance import PDFConformance
from .PDFPart import PDFPart
from .PDFSubtype import PDFSubtype
from .Permissions import Permissions
from .Point import Point
from .PrintDuplex import PrintDuplex
from .PrintFlags import PrintFlags
from .PrintScaling import PrintScaling
from .PSFile import PSFile
from .Quadrilateral import Quadrilateral
from .Rectangle import Rectangle
from .SelectionStyle import SelectionStyle
from .SignatureInfo import SignatureInfo
from .SignatureStatus import SignatureStatus
from .SignatureValidationFlags import SignatureValidationFlags
from .SigningData import SigningData
from .Stretch import Stretch
from .StructureBlockAlign import StructureBlockAlign
from .StructureBorderStyle import StructureBorderStyle
from .StructureElement import StructureElement
from .StructureElementIter import StructureElementIter
from .StructureElementKind import StructureElementKind
from .StructureFormRole import StructureFormRole
from .StructureFormState import StructureFormState
from .StructureGetTextFlags import StructureGetTextFlags
from .StructureGlyphOrientation import StructureGlyphOrientation
from .StructureInlineAlign import StructureInlineAlign
from .StructureListNumbering import StructureListNumbering
from .StructurePlacement import StructurePlacement
from .StructureRubyAlign import StructureRubyAlign
from .StructureRubyPosition import StructureRubyPosition
from .StructureTableScope import StructureTableScope
from .StructureTextAlign import StructureTextAlign
from .StructureTextDecoration import StructureTextDecoration
from .StructureWritingMode import StructureWritingMode
from .Style import Style
from .TextAttributes import TextAttributes
from .TextSpan import TextSpan
from .ViewerPreferences import ViewerPreferences
from .Weight import Weight
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001deed907a40>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Poppler', loader=<gi.importer.DynamicImporter object at 0x000001deed907a40>)"

