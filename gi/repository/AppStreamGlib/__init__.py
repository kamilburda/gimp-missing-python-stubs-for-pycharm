# encoding: utf-8
# module gi.repository.AppStreamGlib
# from C:/Program Files/GIMP 3/lib/girepository-1.0\AppStreamGlib-1.0.typelib
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

APP_SUBSUME_FLAG_DEDUPE = 1913126968
APP_SUBSUME_FLAG_MERGE = 267911104

IMAGE_ALPHA_FLAG_BOTTOM = 2
IMAGE_ALPHA_FLAG_INTERNAL = 16
IMAGE_ALPHA_FLAG_LEFT = 4
IMAGE_ALPHA_FLAG_NONE = 0
IMAGE_ALPHA_FLAG_RIGHT = 8
IMAGE_ALPHA_FLAG_TOP = 1

IMAGE_LARGE_HEIGHT = 423
IMAGE_LARGE_WIDTH = 752

IMAGE_NORMAL_HEIGHT = 351
IMAGE_NORMAL_WIDTH = 624

IMAGE_THUMBNAIL_HEIGHT = 63
IMAGE_THUMBNAIL_WIDTH = 112

_namespace = 'AppStreamGlib'

_version = '1.0'

__weakref__ = None

# functions

def id_kind_from_string(id_kind): # real signature unknown; restored from __doc__
    """ id_kind_from_string(id_kind:str) -> AppStreamGlib.IdKind """
    pass

def id_kind_to_string(id_kind): # real signature unknown; restored from __doc__
    """ id_kind_to_string(id_kind:AppStreamGlib.IdKind) -> str """
    return ""

def inf_error_quark(): # real signature unknown; restored from __doc__
    """ inf_error_quark() -> int """
    return 0

def inf_get_driver_version(keyfile, timestamp): # real signature unknown; restored from __doc__
    """ inf_get_driver_version(keyfile:GLib.KeyFile, timestamp:int) -> str """
    return ""

def inf_load_data(keyfile, data, flags): # real signature unknown; restored from __doc__
    """ inf_load_data(keyfile:GLib.KeyFile, data:str, flags:AppStreamGlib.InfLoadFlags) -> bool """
    return False

def inf_load_file(keyfile, filename, flags): # real signature unknown; restored from __doc__
    """ inf_load_file(keyfile:GLib.KeyFile, filename:str, flags:AppStreamGlib.InfLoadFlags) -> bool """
    return False

def kudo_kind_from_string(kudo_kind): # real signature unknown; restored from __doc__
    """ kudo_kind_from_string(kudo_kind:str) -> AppStreamGlib.KudoKind """
    pass

def kudo_kind_to_string(kudo_kind): # real signature unknown; restored from __doc__
    """ kudo_kind_to_string(kudo_kind:AppStreamGlib.KudoKind) -> str """
    return ""

def markup_convert(markup, format): # real signature unknown; restored from __doc__
    """ markup_convert(markup:str, format:AppStreamGlib.MarkupConvertFormat) -> str """
    return ""

def markup_convert_full(markup, format, flags): # real signature unknown; restored from __doc__
    """ markup_convert_full(markup:str, format:AppStreamGlib.MarkupConvertFormat, flags:AppStreamGlib.MarkupConvertFlag) -> str """
    return ""

def markup_convert_simple(markup): # real signature unknown; restored from __doc__
    """ markup_convert_simple(markup:str) -> str """
    return ""

def markup_import(text, format): # real signature unknown; restored from __doc__
    """ markup_import(text:str, format:AppStreamGlib.MarkupConvertFormat) -> str """
    return ""

def markup_strsplit_words(text, line_len): # real signature unknown; restored from __doc__
    """ markup_strsplit_words(text:str, line_len:int) -> list """
    return []

def markup_validate(markup): # real signature unknown; restored from __doc__
    """ markup_validate(markup:str) -> bool """
    return False

def node_error_quark(): # real signature unknown; restored from __doc__
    """ node_error_quark() -> int """
    return 0

def node_get_attribute(node, key): # real signature unknown; restored from __doc__
    """ node_get_attribute(node:GLib.Node, key:str) -> str """
    return ""

def node_get_attribute_as_int(node, key): # real signature unknown; restored from __doc__
    """ node_get_attribute_as_int(node:GLib.Node, key:str) -> int """
    return 0

def node_get_attribute_as_uint(node, key): # real signature unknown; restored from __doc__
    """ node_get_attribute_as_uint(node:GLib.Node, key:str) -> int """
    return 0

def node_get_comment(node): # real signature unknown; restored from __doc__
    """ node_get_comment(node:GLib.Node) -> str """
    return ""

def node_get_data(node): # real signature unknown; restored from __doc__
    """ node_get_data(node:GLib.Node) -> str """
    return ""

def node_get_localized(node, key): # real signature unknown; restored from __doc__
    """ node_get_localized(node:GLib.Node, key:str) -> dict """
    return {}

def node_get_localized_best(node, key): # real signature unknown; restored from __doc__
    """ node_get_localized_best(node:GLib.Node, key:str) -> str """
    return ""

def node_get_localized_unwrap(node): # real signature unknown; restored from __doc__
    """ node_get_localized_unwrap(node:GLib.Node) -> dict """
    return {}

def node_get_name(node): # real signature unknown; restored from __doc__
    """ node_get_name(node:GLib.Node) -> str """
    return ""

def node_get_tag(node): # real signature unknown; restored from __doc__
    """ node_get_tag(node:GLib.Node) -> AppStreamGlib.Tag """
    pass

def node_insert_hash(parent, name, attr_key, hash, insert_flags): # real signature unknown; restored from __doc__
    """ node_insert_hash(parent:GLib.Node, name:str, attr_key:str, hash:dict, insert_flags:AppStreamGlib.NodeInsertFlags) """
    pass

def node_insert_localized(parent, name, localized, insert_flags): # real signature unknown; restored from __doc__
    """ node_insert_localized(parent:GLib.Node, name:str, localized:dict, insert_flags:AppStreamGlib.NodeInsertFlags) """
    pass

def node_to_xml(node, flags): # real signature unknown; restored from __doc__
    """ node_to_xml(node:GLib.Node, flags:AppStreamGlib.NodeToXmlFlags) -> GLib.String """
    pass

def node_unref(node): # real signature unknown; restored from __doc__
    """ node_unref(node:GLib.Node) """
    pass

def size_kind_from_string(size_kind): # real signature unknown; restored from __doc__
    """ size_kind_from_string(size_kind:str) -> AppStreamGlib.SizeKind """
    pass

def size_kind_to_string(size_kind): # real signature unknown; restored from __doc__
    """ size_kind_to_string(size_kind:AppStreamGlib.SizeKind) -> str """
    return ""

def tag_from_string(tag): # real signature unknown; restored from __doc__
    """ tag_from_string(tag:str) -> AppStreamGlib.Tag """
    pass

def tag_from_string_full(tag, flags): # real signature unknown; restored from __doc__
    """ tag_from_string_full(tag:str, flags:AppStreamGlib.TagFlags) -> AppStreamGlib.Tag """
    pass

def tag_to_string(tag): # real signature unknown; restored from __doc__
    """ tag_to_string(tag:AppStreamGlib.Tag) -> str """
    return ""

def urgency_kind_from_string(urgency_kind): # real signature unknown; restored from __doc__
    """ urgency_kind_from_string(urgency_kind:str) -> AppStreamGlib.UrgencyKind """
    pass

def urgency_kind_to_string(urgency_kind): # real signature unknown; restored from __doc__
    """ urgency_kind_to_string(urgency_kind:AppStreamGlib.UrgencyKind) -> str """
    return ""

def url_kind_from_string(url_kind): # real signature unknown; restored from __doc__
    """ url_kind_from_string(url_kind:str) -> AppStreamGlib.UrlKind """
    pass

def url_kind_to_string(url_kind): # real signature unknown; restored from __doc__
    """ url_kind_to_string(url_kind:AppStreamGlib.UrlKind) -> str """
    return ""

def utils_appstream_id_build(p_str): # real signature unknown; restored from __doc__
    """ utils_appstream_id_build(str:str) -> str """
    return ""

def utils_appstream_id_valid(p_str): # real signature unknown; restored from __doc__
    """ utils_appstream_id_valid(str:str) -> bool """
    return False

def utils_error_quark(): # real signature unknown; restored from __doc__
    """ utils_error_quark() -> int """
    return 0

def utils_find_icon_filename(destdir, search): # real signature unknown; restored from __doc__
    """ utils_find_icon_filename(destdir:str, search:str) -> str """
    return ""

def utils_find_icon_filename_full(destdir, search, flags): # real signature unknown; restored from __doc__
    """ utils_find_icon_filename_full(destdir:str, search:str, flags:AppStreamGlib.UtilsFindIconFlag) -> str """
    return ""

def utils_guid_from_data(namespace_id, data, data_len): # real signature unknown; restored from __doc__
    """ utils_guid_from_data(namespace_id:str, data:int, data_len:int) -> str """
    return ""

def utils_guid_from_string(p_str): # real signature unknown; restored from __doc__
    """ utils_guid_from_string(str:str) -> str """
    return ""

def utils_guid_is_valid(guid): # real signature unknown; restored from __doc__
    """ utils_guid_is_valid(guid:str) -> bool """
    return False

def utils_install_filename(location, filename, origin, destdir): # real signature unknown; restored from __doc__
    """ utils_install_filename(location:AppStreamGlib.UtilsLocation, filename:str, origin:str, destdir:str) -> bool """
    return False

def utils_is_blacklisted_id(desktop_id): # real signature unknown; restored from __doc__
    """ utils_is_blacklisted_id(desktop_id:str) -> bool """
    return False

def utils_is_category_id(category_id): # real signature unknown; restored from __doc__
    """ utils_is_category_id(category_id:str) -> bool """
    return False

def utils_is_environment_id(environment_id): # real signature unknown; restored from __doc__
    """ utils_is_environment_id(environment_id:str) -> bool """
    return False

def utils_is_spdx_license(license): # real signature unknown; restored from __doc__
    """ utils_is_spdx_license(license:str) -> bool """
    return False

def utils_is_spdx_license_id(license_id): # real signature unknown; restored from __doc__
    """ utils_is_spdx_license_id(license_id:str) -> bool """
    return False

def utils_is_stock_icon_name(name): # real signature unknown; restored from __doc__
    """ utils_is_stock_icon_name(name:str) -> bool """
    return False

def utils_license_to_spdx(license): # real signature unknown; restored from __doc__
    """ utils_license_to_spdx(license:str) -> str """
    return ""

def utils_search_tokenize(search): # real signature unknown; restored from __doc__
    """ utils_search_tokenize(search:str) -> list """
    return []

def utils_search_token_valid(token): # real signature unknown; restored from __doc__
    """ utils_search_token_valid(token:str) -> bool """
    return False

def utils_spdx_license_detokenize(license_tokens): # real signature unknown; restored from __doc__
    """ utils_spdx_license_detokenize(license_tokens:str) -> str """
    return ""

def utils_spdx_license_tokenize(license): # real signature unknown; restored from __doc__
    """ utils_spdx_license_tokenize(license:str) -> list """
    return []

def utils_string_replace(string, search, replace): # real signature unknown; restored from __doc__
    """ utils_string_replace(string:GLib.String, search:str, replace:str) -> int """
    return 0

def utils_unique_id_build(scope, bundle_kind, origin, kind, id, branch): # real signature unknown; restored from __doc__
    """ utils_unique_id_build(scope:AppStreamGlib.AppScope, bundle_kind:AppStreamGlib.BundleKind, origin:str, kind:AppStreamGlib.AppKind, id:str, branch:str) -> str """
    return ""

def utils_unique_id_equal(unique_id1, unique_id2): # real signature unknown; restored from __doc__
    """ utils_unique_id_equal(unique_id1:str, unique_id2:str) -> bool """
    return False

def utils_unique_id_hash(unique_id): # real signature unknown; restored from __doc__
    """ utils_unique_id_hash(unique_id:str) -> int """
    return 0

def utils_unique_id_match(unique_id1, unique_id2, match_flags): # real signature unknown; restored from __doc__
    """ utils_unique_id_match(unique_id1:str, unique_id2:str, match_flags:AppStreamGlib.UniqueIdMatchFlags) -> bool """
    return False

def utils_unique_id_valid(unique_id): # real signature unknown; restored from __doc__
    """ utils_unique_id_valid(unique_id:str) -> bool """
    return False

def utils_vercmp(version_a, version_b): # real signature unknown; restored from __doc__
    """ utils_vercmp(version_a:str, version_b:str) -> int """
    return 0

def utils_vercmp_full(version_a, version_b, flags): # real signature unknown; restored from __doc__
    """ utils_vercmp_full(version_a:str, version_b:str, flags:AppStreamGlib.VersionCompareFlag) -> int """
    return 0

def utils_version_from_uint16(val, flags): # real signature unknown; restored from __doc__
    """ utils_version_from_uint16(val:int, flags:AppStreamGlib.VersionParseFlag) -> str """
    return ""

def utils_version_from_uint32(val, flags): # real signature unknown; restored from __doc__
    """ utils_version_from_uint32(val:int, flags:AppStreamGlib.VersionParseFlag) -> str """
    return ""

def utils_version_parse(version): # real signature unknown; restored from __doc__
    """ utils_version_parse(version:str) -> str """
    return ""

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
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

from .Agreement import Agreement
from .AgreementClass import AgreementClass
from .AgreementKind import AgreementKind
from .AgreementSection import AgreementSection
from .AgreementSectionClass import AgreementSectionClass
from .App import App
from .AppClass import AppClass
from .AppError import AppError
from .AppKind import AppKind
from .AppMergeKind import AppMergeKind
from .AppParseFlags import AppParseFlags
from .AppQuirk import AppQuirk
from .AppScope import AppScope
from .AppSearchMatch import AppSearchMatch
from .AppState import AppState
from .AppSubsumeFlags import AppSubsumeFlags
from .AppTrustFlags import AppTrustFlags
from .AppValidateFlags import AppValidateFlags
from .Bundle import Bundle
from .BundleClass import BundleClass
from .BundleKind import BundleKind
from .Checksum import Checksum
from .ChecksumClass import ChecksumClass
from .ChecksumTarget import ChecksumTarget
from .ContentRating import ContentRating
from .ContentRatingClass import ContentRatingClass
from .ContentRatingSystem import ContentRatingSystem
from .ContentRatingValue import ContentRatingValue
from .Format import Format
from .FormatClass import FormatClass
from .FormatKind import FormatKind
from .Icon import Icon
from .IconClass import IconClass
from .IconError import IconError
from .IconKind import IconKind
from .IconLoadFlags import IconLoadFlags
from .IdKind import IdKind
from .Image import Image
from .ImageClass import ImageClass
from .ImageKind import ImageKind
from .ImageLoadFlags import ImageLoadFlags
from .ImageSaveFlags import ImageSaveFlags
from .InfError import InfError
from .InfLoadFlags import InfLoadFlags
from .KudoKind import KudoKind
from .Launchable import Launchable
from .LaunchableClass import LaunchableClass
from .LaunchableKind import LaunchableKind
from .MarkupConvertFlag import MarkupConvertFlag
from .MarkupConvertFormat import MarkupConvertFormat
from .NodeError import NodeError
from .NodeFromXmlFlags import NodeFromXmlFlags
from .NodeInsertFlags import NodeInsertFlags
from .NodeToXmlFlags import NodeToXmlFlags
from .Problem import Problem
from .ProblemClass import ProblemClass
from .ProblemKind import ProblemKind
from .Provide import Provide
from .ProvideClass import ProvideClass
from .ProvideKind import ProvideKind
from .Release import Release
from .ReleaseClass import ReleaseClass
from .ReleaseKind import ReleaseKind
from .ReleaseState import ReleaseState
from .Require import Require
from .RequireClass import RequireClass
from .RequireCompare import RequireCompare
from .RequireKind import RequireKind
from .Review import Review
from .ReviewClass import ReviewClass
from .ReviewFlags import ReviewFlags
from .Screenshot import Screenshot
from .ScreenshotClass import ScreenshotClass
from .ScreenshotKind import ScreenshotKind
from .SizeKind import SizeKind
from .Store import Store
from .StoreAddFlags import StoreAddFlags
from .StoreClass import StoreClass
from .StoreError import StoreError
from .StoreLoadFlags import StoreLoadFlags
from .StoreSearchFlags import StoreSearchFlags
from .StoreWatchFlags import StoreWatchFlags
from .Suggest import Suggest
from .SuggestClass import SuggestClass
from .SuggestKind import SuggestKind
from .Tag import Tag
from .TagFlags import TagFlags
from .Translation import Translation
from .TranslationClass import TranslationClass
from .TranslationKind import TranslationKind
from .UniqueIdMatchFlags import UniqueIdMatchFlags
from .UrgencyKind import UrgencyKind
from .UrlKind import UrlKind
from .UtilsError import UtilsError
from .UtilsFindIconFlag import UtilsFindIconFlag
from .UtilsLocation import UtilsLocation
from .VersionCompareFlag import VersionCompareFlag
from .VersionParseFlag import VersionParseFlag
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001afbdff2090>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.AppStreamGlib', loader=<gi.importer.DynamicImporter object at 0x000001afbdff2090>)"

