# encoding: utf-8
# module gi.repository.AppStream
# from C:/Program Files/GIMP 3/lib/girepository-1.0\AppStream-1.0.typelib
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi


# Variables with simple values

MAJOR_VERSION = 1

MICRO_VERSION = 6

MINOR_VERSION = 0

_namespace = 'AppStream'

_version = '1.0'

# functions

def agreement_kind_from_string(value): # real signature unknown; restored from __doc__
    """ agreement_kind_from_string(value:str) -> AppStream.AgreementKind """
    pass

def agreement_kind_to_string(value): # real signature unknown; restored from __doc__
    """ agreement_kind_to_string(value:AppStream.AgreementKind) -> str """
    return ""

def artifact_kind_from_string(kind): # real signature unknown; restored from __doc__
    """ artifact_kind_from_string(kind:str) -> AppStream.ArtifactKind """
    pass

def artifact_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ artifact_kind_to_string(kind:AppStream.ArtifactKind) -> str """
    return ""

def bundle_kind_from_string(bundle_str): # real signature unknown; restored from __doc__
    """ bundle_kind_from_string(bundle_str:str) -> AppStream.BundleKind """
    pass

def bundle_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ bundle_kind_to_string(kind:AppStream.BundleKind) -> str """
    return ""

def chassis_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ chassis_kind_from_string(kind_str:str) -> AppStream.ChassisKind """
    pass

def chassis_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ chassis_kind_to_string(kind:AppStream.ChassisKind) -> str """
    return ""

def checksum_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ checksum_kind_from_string(kind_str:str) -> AppStream.ChecksumKind """
    pass

def checksum_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ checksum_kind_to_string(kind:AppStream.ChecksumKind) -> str """
    return ""

def color_kind_from_string(p_str): # real signature unknown; restored from __doc__
    """ color_kind_from_string(str:str) -> AppStream.ColorKind """
    pass

def color_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ color_kind_to_string(kind:AppStream.ColorKind) -> str """
    return ""

def color_scheme_kind_from_string(p_str): # real signature unknown; restored from __doc__
    """ color_scheme_kind_from_string(str:str) -> AppStream.ColorSchemeKind """
    pass

def color_scheme_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ color_scheme_kind_to_string(kind:AppStream.ColorSchemeKind) -> str """
    return ""

def component_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ component_kind_from_string(kind_str:str) -> AppStream.ComponentKind """
    pass

def component_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ component_kind_to_string(kind:AppStream.ComponentKind) -> str """
    return ""

def component_scope_from_string(scope_str): # real signature unknown; restored from __doc__
    """ component_scope_from_string(scope_str:str) -> AppStream.ComponentScope """
    pass

def component_scope_to_string(scope): # real signature unknown; restored from __doc__
    """ component_scope_to_string(scope:AppStream.ComponentScope) -> str """
    return ""

def content_rating_system_format_age(system, age): # real signature unknown; restored from __doc__
    """ content_rating_system_format_age(system:AppStream.ContentRatingSystem, age:int) -> str or None """
    return ""

def content_rating_system_from_locale(locale): # real signature unknown; restored from __doc__
    """ content_rating_system_from_locale(locale:str) -> AppStream.ContentRatingSystem """
    pass

def content_rating_system_get_csm_ages(system): # real signature unknown; restored from __doc__
    """ content_rating_system_get_csm_ages(system:AppStream.ContentRatingSystem) -> list """
    return []

def content_rating_system_get_formatted_ages(system): # real signature unknown; restored from __doc__
    """ content_rating_system_get_formatted_ages(system:AppStream.ContentRatingSystem) -> list """
    return []

def content_rating_system_to_string(system): # real signature unknown; restored from __doc__
    """ content_rating_system_to_string(system:AppStream.ContentRatingSystem) -> str or None """
    return ""

def content_rating_value_from_string(value): # real signature unknown; restored from __doc__
    """ content_rating_value_from_string(value:str) -> AppStream.ContentRatingValue """
    pass

def content_rating_value_to_string(value): # real signature unknown; restored from __doc__
    """ content_rating_value_to_string(value:AppStream.ContentRatingValue) -> str """
    return ""

def control_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ control_kind_from_string(kind_str:str) -> AppStream.ControlKind """
    pass

def control_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ control_kind_to_string(kind:AppStream.ControlKind) -> str """
    return ""

def display_side_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ display_side_kind_from_string(kind_str:str) -> AppStream.DisplaySideKind """
    pass

def display_side_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ display_side_kind_to_string(kind:AppStream.DisplaySideKind) -> str """
    return ""

def format_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ format_kind_from_string(kind_str:str) -> AppStream.FormatKind """
    pass

def format_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ format_kind_to_string(kind:AppStream.FormatKind) -> str """
    return ""

def format_version_from_string(version_str): # real signature unknown; restored from __doc__
    """ format_version_from_string(version_str:str) -> AppStream.FormatVersion """
    pass

def format_version_to_string(version): # real signature unknown; restored from __doc__
    """ format_version_to_string(version:AppStream.FormatVersion) -> str """
    return ""

def get_current_distro_component_id(): # real signature unknown; restored from __doc__
    """ get_current_distro_component_id() -> str """
    return ""

def get_default_categories(with_special): # real signature unknown; restored from __doc__
    """ get_default_categories(with_special:bool) -> list """
    return []

def get_license_name(license): # real signature unknown; restored from __doc__
    """ get_license_name(license:str) -> str or None """
    return ""

def get_license_url(license): # real signature unknown; restored from __doc__
    """ get_license_url(license:str) -> str or None """
    return ""

def gstring_replace(string, find, replace, limit): # real signature unknown; restored from __doc__
    """ gstring_replace(string:GLib.String, find:str, replace:str, limit:int) -> int """
    return 0

def icon_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ icon_kind_from_string(kind_str:str) -> AppStream.IconKind """
    pass

def icon_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ icon_kind_to_string(kind:AppStream.IconKind) -> str """
    return ""

def image_kind_from_string(kind): # real signature unknown; restored from __doc__
    """ image_kind_from_string(kind:str) -> AppStream.ImageKind """
    pass

def image_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ image_kind_to_string(kind:AppStream.ImageKind) -> str """
    return ""

def internet_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ internet_kind_from_string(kind_str:str) -> AppStream.InternetKind """
    pass

def internet_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ internet_kind_to_string(kind:AppStream.InternetKind) -> str """
    return ""

def issue_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ issue_kind_from_string(kind_str:str) -> AppStream.IssueKind """
    pass

def issue_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ issue_kind_to_string(kind:AppStream.IssueKind) -> str """
    return ""

def issue_severity_from_string(p_str): # real signature unknown; restored from __doc__
    """ issue_severity_from_string(str:str) -> AppStream.IssueSeverity """
    pass

def issue_severity_to_string(severity): # real signature unknown; restored from __doc__
    """ issue_severity_to_string(severity:AppStream.IssueSeverity) -> str """
    return ""

def is_spdx_license_exception_id(exception_id): # real signature unknown; restored from __doc__
    """ is_spdx_license_exception_id(exception_id:str) -> bool """
    return False

def is_spdx_license_expression(license): # real signature unknown; restored from __doc__
    """ is_spdx_license_expression(license:str) -> bool """
    return False

def is_spdx_license_id(license_id): # real signature unknown; restored from __doc__
    """ is_spdx_license_id(license_id:str) -> bool """
    return False

def launchable_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ launchable_kind_from_string(kind_str:str) -> AppStream.LaunchableKind """
    pass

def launchable_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ launchable_kind_to_string(kind:AppStream.LaunchableKind) -> str """
    return ""

def license_is_free_license(license): # real signature unknown; restored from __doc__
    """ license_is_free_license(license:str) -> bool """
    return False

def license_is_metadata_license(license): # real signature unknown; restored from __doc__
    """ license_is_metadata_license(license:str) -> bool """
    return False

def license_is_metadata_license_id(license_id): # real signature unknown; restored from __doc__
    """ license_is_metadata_license_id(license_id:str) -> bool """
    return False

def license_to_spdx_id(license): # real signature unknown; restored from __doc__
    """ license_to_spdx_id(license:str) -> str """
    return ""

def markup_convert(markup, to_kind): # real signature unknown; restored from __doc__
    """ markup_convert(markup:str, to_kind:AppStream.MarkupKind) -> str """
    return ""

def markup_strsplit_words(text, line_len): # real signature unknown; restored from __doc__
    """ markup_strsplit_words(text:str, line_len:int) -> list """
    return []

def merge_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ merge_kind_from_string(kind_str:str) -> AppStream.MergeKind """
    pass

def merge_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ merge_kind_to_string(kind:AppStream.MergeKind) -> str """
    return ""

def metadata_error_quark(): # real signature unknown; restored from __doc__
    """ metadata_error_quark() -> int """
    return 0

def pool_error_quark(): # real signature unknown; restored from __doc__
    """ pool_error_quark() -> int """
    return 0

def provided_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ provided_kind_from_string(kind_str:str) -> AppStream.ProvidedKind """
    pass

def provided_kind_to_l10n_string(kind): # real signature unknown; restored from __doc__
    """ provided_kind_to_l10n_string(kind:AppStream.ProvidedKind) -> str """
    return ""

def provided_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ provided_kind_to_string(kind:AppStream.ProvidedKind) -> str """
    return ""

def reference_kind_from_string(p_str): # real signature unknown; restored from __doc__
    """ reference_kind_from_string(str:str) -> AppStream.ReferenceKind """
    pass

def reference_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ reference_kind_to_string(kind:AppStream.ReferenceKind) -> str """
    return ""

def relation_compare_from_string(compare_str): # real signature unknown; restored from __doc__
    """ relation_compare_from_string(compare_str:str) -> AppStream.RelationCompare """
    pass

def relation_compare_to_string(compare): # real signature unknown; restored from __doc__
    """ relation_compare_to_string(compare:AppStream.RelationCompare) -> str """
    return ""

def relation_compare_to_symbols_string(compare): # real signature unknown; restored from __doc__
    """ relation_compare_to_symbols_string(compare:AppStream.RelationCompare) -> str """
    return ""

def relation_error_quark(): # real signature unknown; restored from __doc__
    """ relation_error_quark() -> int """
    return 0

def relation_item_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ relation_item_kind_from_string(kind_str:str) -> AppStream.RelationItemKind """
    pass

def relation_item_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ relation_item_kind_to_string(kind:AppStream.RelationItemKind) -> str """
    return ""

def relation_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ relation_kind_from_string(kind_str:str) -> AppStream.RelationKind """
    pass

def relation_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ relation_kind_to_string(kind:AppStream.RelationKind) -> str """
    return ""

def release_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ release_kind_from_string(kind_str:str) -> AppStream.ReleaseKind """
    pass

def release_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ release_kind_to_string(kind:AppStream.ReleaseKind) -> str """
    return ""

def release_list_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ release_list_kind_from_string(kind_str:str) -> AppStream.ReleaseListKind """
    pass

def release_list_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ release_list_kind_to_string(kind:AppStream.ReleaseListKind) -> str """
    return ""

def release_url_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ release_url_kind_from_string(kind_str:str) -> AppStream.ReleaseUrlKind """
    pass

def release_url_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ release_url_kind_to_string(kind:AppStream.ReleaseUrlKind) -> str """
    return ""

def screenshot_kind_from_string(kind): # real signature unknown; restored from __doc__
    """ screenshot_kind_from_string(kind:str) -> AppStream.ScreenshotKind """
    pass

def screenshot_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ screenshot_kind_to_string(kind:AppStream.ScreenshotKind) -> str """
    return ""

def size_kind_from_string(size_kind): # real signature unknown; restored from __doc__
    """ size_kind_from_string(size_kind:str) -> AppStream.SizeKind """
    pass

def size_kind_to_string(size_kind): # real signature unknown; restored from __doc__
    """ size_kind_to_string(size_kind:AppStream.SizeKind) -> str """
    return ""

def spdx_license_detokenize(license_tokens): # real signature unknown; restored from __doc__
    """ spdx_license_detokenize(license_tokens:str) -> str or None """
    return ""

def spdx_license_tokenize(license): # real signature unknown; restored from __doc__
    """ spdx_license_tokenize(license:str) -> list or None """
    return []

def suggested_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ suggested_kind_from_string(kind_str:str) -> AppStream.SuggestedKind """
    pass

def suggested_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ suggested_kind_to_string(kind:AppStream.SuggestedKind) -> str """
    return ""

def system_info_error_quark(): # real signature unknown; restored from __doc__
    """ system_info_error_quark() -> int """
    return 0

def translation_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ translation_kind_from_string(kind_str:str) -> AppStream.TranslationKind """
    pass

def translation_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ translation_kind_to_string(kind:AppStream.TranslationKind) -> str """
    return ""

def urgency_kind_from_string(urgency_kind): # real signature unknown; restored from __doc__
    """ urgency_kind_from_string(urgency_kind:str) -> AppStream.UrgencyKind """
    pass

def urgency_kind_to_string(urgency_kind): # real signature unknown; restored from __doc__
    """ urgency_kind_to_string(urgency_kind:AppStream.UrgencyKind) -> str """
    return ""

def url_kind_from_string(url_kind): # real signature unknown; restored from __doc__
    """ url_kind_from_string(url_kind:str) -> AppStream.UrlKind """
    pass

def url_kind_to_string(url_kind): # real signature unknown; restored from __doc__
    """ url_kind_to_string(url_kind:AppStream.UrlKind) -> str """
    return ""

def utils_build_data_id(scope, bundle_kind, origin, cid, branch): # real signature unknown; restored from __doc__
    """ utils_build_data_id(scope:AppStream.ComponentScope, bundle_kind:AppStream.BundleKind, origin:str, cid:str, branch:str) -> str """
    return ""

def utils_data_id_equal(data_id1, data_id2): # real signature unknown; restored from __doc__
    """ utils_data_id_equal(data_id1:str, data_id2:str) -> bool """
    return False

def utils_data_id_get_cid(data_id): # real signature unknown; restored from __doc__
    """ utils_data_id_get_cid(data_id:str) -> str """
    return ""

def utils_data_id_hash(data_id): # real signature unknown; restored from __doc__
    """ utils_data_id_hash(data_id:str) -> int """
    return 0

def utils_data_id_match(data_id1, data_id2, match_flags): # real signature unknown; restored from __doc__
    """ utils_data_id_match(data_id1:str, data_id2:str, match_flags:AppStream.DataIdMatchFlags) -> bool """
    return False

def utils_data_id_valid(data_id): # real signature unknown; restored from __doc__
    """ utils_data_id_valid(data_id:str) -> bool """
    return False

def utils_error_quark(): # real signature unknown; restored from __doc__
    """ utils_error_quark() -> int """
    return 0

def utils_get_desktop_environment_name(de_id): # real signature unknown; restored from __doc__
    """ utils_get_desktop_environment_name(de_id:str) -> str """
    return ""

def utils_get_gui_environment_style_name(env_style): # real signature unknown; restored from __doc__
    """ utils_get_gui_environment_style_name(env_style:str) -> str """
    return ""

def utils_get_tag_search_weight(tag_name): # real signature unknown; restored from __doc__
    """ utils_get_tag_search_weight(tag_name:str) -> int """
    return 0

def utils_guess_scope_from_path(path): # real signature unknown; restored from __doc__
    """ utils_guess_scope_from_path(path:str) -> AppStream.ComponentScope """
    pass

def utils_install_metadata_file(location, filename, origin, destdir): # real signature unknown; restored from __doc__
    """ utils_install_metadata_file(location:AppStream.MetadataLocation, filename:str, origin:str, destdir:str) -> bool """
    return False

def utils_is_category_name(category_name): # real signature unknown; restored from __doc__
    """ utils_is_category_name(category_name:str) -> bool """
    return False

def utils_is_desktop_environment(de_id): # real signature unknown; restored from __doc__
    """ utils_is_desktop_environment(de_id:str) -> bool """
    return False

def utils_is_gui_environment_style(env_style): # real signature unknown; restored from __doc__
    """ utils_is_gui_environment_style(env_style:str) -> bool """
    return False

def utils_is_platform_triplet(triplet): # real signature unknown; restored from __doc__
    """ utils_is_platform_triplet(triplet:str) -> bool """
    return False

def utils_is_tld(tld): # real signature unknown; restored from __doc__
    """ utils_is_tld(tld:str) -> bool """
    return False

def utils_locale_is_compatible(locale1=None, locale2=None): # real signature unknown; restored from __doc__
    """ utils_locale_is_compatible(locale1:str=None, locale2:str=None) -> bool """
    return False

def utils_posix_locale_to_bcp47(locale): # real signature unknown; restored from __doc__
    """ utils_posix_locale_to_bcp47(locale:str) -> str """
    return ""

def utils_sort_components_into_categories(cpts, categories, check_duplicates): # real signature unknown; restored from __doc__
    """ utils_sort_components_into_categories(cpts:list, categories:list, check_duplicates:bool) """
    pass

def validator_error_quark(): # real signature unknown; restored from __doc__
    """ validator_error_quark() -> int """
    return 0

def vercmp(a, b, flags): # real signature unknown; restored from __doc__
    """ vercmp(a:str, b:str, flags:AppStream.VercmpFlags) -> int """
    return 0

def vercmp_simple(a, b): # real signature unknown; restored from __doc__
    """ vercmp_simple(a:str, b:str) -> int """
    return 0

def vercmp_test_match(ver1, compare, ver2, flags): # real signature unknown; restored from __doc__
    """ vercmp_test_match(ver1:str, compare:AppStream.RelationCompare, ver2:str, flags:AppStream.VercmpFlags) -> bool """
    return False

def version_string(): # real signature unknown; restored from __doc__
    """ version_string() -> str """
    return ""

def video_codec_kind_from_string(p_str): # real signature unknown; restored from __doc__
    """ video_codec_kind_from_string(str:str) -> AppStream.VideoCodecKind """
    pass

def video_codec_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ video_codec_kind_to_string(kind:AppStream.VideoCodecKind) -> str """
    return ""

def video_container_kind_from_string(p_str): # real signature unknown; restored from __doc__
    """ video_container_kind_from_string(str:str) -> AppStream.VideoContainerKind """
    pass

def video_container_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ video_container_kind_to_string(kind:AppStream.VideoContainerKind) -> str """
    return ""

# classes

from .Agreement import Agreement
from .AgreementClass import AgreementClass
from .AgreementKind import AgreementKind
from .AgreementSection import AgreementSection
from .AgreementSectionClass import AgreementSectionClass
from .Artifact import Artifact
from .ArtifactClass import ArtifactClass
from .ArtifactKind import ArtifactKind
from .Branding import Branding
from .BrandingClass import BrandingClass
from .BrandingColorIter import BrandingColorIter
from .Bundle import Bundle
from .BundleClass import BundleClass
from .BundleKind import BundleKind
from .CacheFlags import CacheFlags
from .Category import Category
from .CategoryClass import CategoryClass
from .ChassisKind import ChassisKind
from .CheckResult import CheckResult
from .Checksum import Checksum
from .ChecksumClass import ChecksumClass
from .ChecksumKind import ChecksumKind
from .ColorKind import ColorKind
from .ColorSchemeKind import ColorSchemeKind
from .Component import Component
from .ComponentBox import ComponentBox
from .ComponentBoxClass import ComponentBoxClass
from .ComponentBoxFlags import ComponentBoxFlags
from .ComponentClass import ComponentClass
from .ComponentKind import ComponentKind
from .ComponentScope import ComponentScope
from .ContentRating import ContentRating
from .ContentRatingClass import ContentRatingClass
from .ContentRatingSystem import ContentRatingSystem
from .ContentRatingValue import ContentRatingValue
from .Context import Context
from .ContextClass import ContextClass
from .ControlKind import ControlKind
from .DataIdMatchFlags import DataIdMatchFlags
from .Developer import Developer
from .DeveloperClass import DeveloperClass
from .DisplaySideKind import DisplaySideKind
from .FormatKind import FormatKind
from .FormatStyle import FormatStyle
from .FormatVersion import FormatVersion
from .Icon import Icon
from .IconClass import IconClass
from .IconKind import IconKind
from .Image import Image
from .ImageClass import ImageClass
from .ImageKind import ImageKind
from .InternetKind import InternetKind
from .Issue import Issue
from .IssueClass import IssueClass
from .IssueKind import IssueKind
from .IssueSeverity import IssueSeverity
from .Launchable import Launchable
from .LaunchableClass import LaunchableClass
from .LaunchableKind import LaunchableKind
from .MarkupKind import MarkupKind
from .MergeKind import MergeKind
from .Metadata import Metadata
from .MetadataClass import MetadataClass
from .MetadataError import MetadataError
from .MetadataLocation import MetadataLocation
from .ParseFlags import ParseFlags
from .Pool import Pool
from .PoolClass import PoolClass
from .PoolError import PoolError
from .PoolFlags import PoolFlags
from .Provided import Provided
from .ProvidedClass import ProvidedClass
from .ProvidedKind import ProvidedKind
from .Reference import Reference
from .ReferenceClass import ReferenceClass
from .ReferenceKind import ReferenceKind
from .Relation import Relation
from .RelationCheckResult import RelationCheckResult
from .RelationCheckResultClass import RelationCheckResultClass
from .RelationClass import RelationClass
from .RelationCompare import RelationCompare
from .RelationError import RelationError
from .RelationItemKind import RelationItemKind
from .RelationKind import RelationKind
from .RelationStatus import RelationStatus
from .Release import Release
from .ReleaseClass import ReleaseClass
from .ReleaseKind import ReleaseKind
from .ReleaseList import ReleaseList
from .ReleaseListClass import ReleaseListClass
from .ReleaseListKind import ReleaseListKind
from .ReleaseUrlKind import ReleaseUrlKind
from .Review import Review
from .ReviewClass import ReviewClass
from .ReviewFlags import ReviewFlags
from .Screenshot import Screenshot
from .ScreenshotClass import ScreenshotClass
from .ScreenshotKind import ScreenshotKind
from .ScreenshotMediaKind import ScreenshotMediaKind
from .SizeKind import SizeKind
from .Suggested import Suggested
from .SuggestedClass import SuggestedClass
from .SuggestedKind import SuggestedKind
from .SystemInfo import SystemInfo
from .SystemInfoClass import SystemInfoClass
from .SystemInfoError import SystemInfoError
from .Translation import Translation
from .TranslationClass import TranslationClass
from .TranslationKind import TranslationKind
from .UrgencyKind import UrgencyKind
from .UrlKind import UrlKind
from .UtilsError import UtilsError
from .Validator import Validator
from .ValidatorClass import ValidatorClass
from .ValidatorError import ValidatorError
from .ValidatorIssue import ValidatorIssue
from .ValidatorIssueClass import ValidatorIssueClass
from .ValueFlags import ValueFlags
from .VercmpFlags import VercmpFlags
from .Video import Video
from .VideoClass import VideoClass
from .VideoCodecKind import VideoCodecKind
from .VideoContainerKind import VideoContainerKind
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x000001ece9c1fe00>'

__path__ = []

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.AppStream', loader=<gi.importer.DynamicImporter object at 0x000001ece9c1fe00>)"

