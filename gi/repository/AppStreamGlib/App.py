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


class App(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        App(**properties)
        new() -> AppStreamGlib.App
    """
    def add_addon(self, addon): # real signature unknown; restored from __doc__
        """ add_addon(self, addon:AppStreamGlib.App) """
        pass

    def add_agreement(self, agreement): # real signature unknown; restored from __doc__
        """ add_agreement(self, agreement:AppStreamGlib.Agreement) """
        pass

    def add_arch(self, arch): # real signature unknown; restored from __doc__
        """ add_arch(self, arch:str) """
        pass

    def add_bundle(self, bundle): # real signature unknown; restored from __doc__
        """ add_bundle(self, bundle:AppStreamGlib.Bundle) """
        pass

    def add_category(self, category): # real signature unknown; restored from __doc__
        """ add_category(self, category:str) """
        pass

    def add_compulsory_for_desktop(self, compulsory_for_desktop): # real signature unknown; restored from __doc__
        """ add_compulsory_for_desktop(self, compulsory_for_desktop:str) """
        pass

    def add_content_rating(self, content_rating): # real signature unknown; restored from __doc__
        """ add_content_rating(self, content_rating:AppStreamGlib.ContentRating) """
        pass

    def add_extends(self, extends): # real signature unknown; restored from __doc__
        """ add_extends(self, extends:str) """
        pass

    def add_format(self, format): # real signature unknown; restored from __doc__
        """ add_format(self, format:AppStreamGlib.Format) """
        pass

    def add_icon(self, icon): # real signature unknown; restored from __doc__
        """ add_icon(self, icon:AppStreamGlib.Icon) """
        pass

    def add_keyword(self, locale=None, keyword): # real signature unknown; restored from __doc__
        """ add_keyword(self, locale:str=None, keyword:str) """
        pass

    def add_kudo(self, kudo): # real signature unknown; restored from __doc__
        """ add_kudo(self, kudo:str) """
        pass

    def add_kudo_kind(self, kudo_kind): # real signature unknown; restored from __doc__
        """ add_kudo_kind(self, kudo_kind:AppStreamGlib.KudoKind) """
        pass

    def add_language(self, percentage, locale=None): # real signature unknown; restored from __doc__
        """ add_language(self, percentage:int, locale:str=None) """
        pass

    def add_launchable(self, launchable): # real signature unknown; restored from __doc__
        """ add_launchable(self, launchable:AppStreamGlib.Launchable) """
        pass

    def add_metadata(self, key, value=None): # real signature unknown; restored from __doc__
        """ add_metadata(self, key:str, value:str=None) """
        pass

    def add_mimetype(self, mimetype): # real signature unknown; restored from __doc__
        """ add_mimetype(self, mimetype:str) """
        pass

    def add_permission(self, permission): # real signature unknown; restored from __doc__
        """ add_permission(self, permission:str) """
        pass

    def add_pkgname(self, pkgname): # real signature unknown; restored from __doc__
        """ add_pkgname(self, pkgname:str) """
        pass

    def add_provide(self, provide): # real signature unknown; restored from __doc__
        """ add_provide(self, provide:AppStreamGlib.Provide) """
        pass

    def add_quirk(self, quirk): # real signature unknown; restored from __doc__
        """ add_quirk(self, quirk:AppStreamGlib.AppQuirk) """
        pass

    def add_release(self, release): # real signature unknown; restored from __doc__
        """ add_release(self, release:AppStreamGlib.Release) """
        pass

    def add_require(self, require): # real signature unknown; restored from __doc__
        """ add_require(self, require:AppStreamGlib.Require) """
        pass

    def add_review(self, review): # real signature unknown; restored from __doc__
        """ add_review(self, review:AppStreamGlib.Review) """
        pass

    def add_screenshot(self, screenshot): # real signature unknown; restored from __doc__
        """ add_screenshot(self, screenshot:AppStreamGlib.Screenshot) """
        pass

    def add_suggest(self, suggest): # real signature unknown; restored from __doc__
        """ add_suggest(self, suggest:AppStreamGlib.Suggest) """
        pass

    def add_translation(self, translation): # real signature unknown; restored from __doc__
        """ add_translation(self, translation:AppStreamGlib.Translation) """
        pass

    def add_url(self, url_kind, url): # real signature unknown; restored from __doc__
        """ add_url(self, url_kind:AppStreamGlib.UrlKind, url:str) """
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

    def convert_icons(self, kind): # real signature unknown; restored from __doc__
        """ convert_icons(self, kind:AppStreamGlib.IconKind) -> bool """
        return False

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

    def equal(self, app2): # real signature unknown; restored from __doc__
        """ equal(self, app2:AppStreamGlib.App) -> bool """
        return False

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

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

    def get_addons(self): # real signature unknown; restored from __doc__
        """ get_addons(self) -> list """
        return []

    def get_agreement_by_kind(self, kind): # real signature unknown; restored from __doc__
        """ get_agreement_by_kind(self, kind:AppStreamGlib.AgreementKind) -> AppStreamGlib.Agreement """
        pass

    def get_agreement_default(self): # real signature unknown; restored from __doc__
        """ get_agreement_default(self) -> AppStreamGlib.Agreement """
        pass

    def get_architectures(self): # real signature unknown; restored from __doc__
        """ get_architectures(self) -> list """
        return []

    def get_branch(self): # real signature unknown; restored from __doc__
        """ get_branch(self) -> str """
        return ""

    def get_bundles(self): # real signature unknown; restored from __doc__
        """ get_bundles(self) -> list """
        return []

    def get_bundle_default(self): # real signature unknown; restored from __doc__
        """ get_bundle_default(self) -> AppStreamGlib.Bundle """
        pass

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> list """
        return []

    def get_comment(self, locale=None): # real signature unknown; restored from __doc__
        """ get_comment(self, locale:str=None) -> str """
        return ""

    def get_comments(self): # real signature unknown; restored from __doc__
        """ get_comments(self) -> dict """
        return {}

    def get_compulsory_for_desktops(self): # real signature unknown; restored from __doc__
        """ get_compulsory_for_desktops(self) -> list """
        return []

    def get_content_rating(self, kind): # real signature unknown; restored from __doc__
        """ get_content_rating(self, kind:str) -> AppStreamGlib.ContentRating """
        pass

    def get_content_ratings(self): # real signature unknown; restored from __doc__
        """ get_content_ratings(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self, locale=None): # real signature unknown; restored from __doc__
        """ get_description(self, locale:str=None) -> str """
        return ""

    def get_descriptions(self): # real signature unknown; restored from __doc__
        """ get_descriptions(self) -> dict """
        return {}

    def get_developer_name(self, locale=None): # real signature unknown; restored from __doc__
        """ get_developer_name(self, locale:str=None) -> str """
        return ""

    def get_developer_names(self): # real signature unknown; restored from __doc__
        """ get_developer_names(self) -> dict """
        return {}

    def get_extends(self): # real signature unknown; restored from __doc__
        """ get_extends(self) -> list """
        return []

    def get_formats(self): # real signature unknown; restored from __doc__
        """ get_formats(self) -> list """
        return []

    def get_format_by_filename(self, filename): # real signature unknown; restored from __doc__
        """ get_format_by_filename(self, filename:str) -> AppStreamGlib.Format """
        pass

    def get_format_by_kind(self, kind): # real signature unknown; restored from __doc__
        """ get_format_by_kind(self, kind:AppStreamGlib.FormatKind) -> AppStreamGlib.Format """
        pass

    def get_format_default(self): # real signature unknown; restored from __doc__
        """ get_format_default(self) -> AppStreamGlib.Format """
        pass

    def get_icons(self): # real signature unknown; restored from __doc__
        """ get_icons(self) -> list """
        return []

    def get_icon_default(self): # real signature unknown; restored from __doc__
        """ get_icon_default(self) -> AppStreamGlib.Icon """
        pass

    def get_icon_for_size(self, width, height): # real signature unknown; restored from __doc__
        """ get_icon_for_size(self, width:int, height:int) -> AppStreamGlib.Icon """
        pass

    def get_icon_path(self): # real signature unknown; restored from __doc__
        """ get_icon_path(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_id_filename(self): # real signature unknown; restored from __doc__
        """ get_id_filename(self) -> str """
        return ""

    def get_id_kind(self): # real signature unknown; restored from __doc__
        """ get_id_kind(self) -> AppStreamGlib.IdKind """
        pass

    def get_id_no_prefix(self): # real signature unknown; restored from __doc__
        """ get_id_no_prefix(self) -> str """
        return ""

    def get_keywords(self, locale=None): # real signature unknown; restored from __doc__
        """ get_keywords(self, locale:str=None) -> list """
        return []

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> AppStreamGlib.AppKind """
        pass

    def get_kudos(self): # real signature unknown; restored from __doc__
        """ get_kudos(self) -> list """
        return []

    def get_language(self, locale=None): # real signature unknown; restored from __doc__
        """ get_language(self, locale:str=None) -> int """
        return 0

    def get_languages(self): # real signature unknown; restored from __doc__
        """ get_languages(self) -> list """
        return []

    def get_launchables(self): # real signature unknown; restored from __doc__
        """ get_launchables(self) -> list """
        return []

    def get_launchable_by_kind(self, kind): # real signature unknown; restored from __doc__
        """ get_launchable_by_kind(self, kind:AppStreamGlib.LaunchableKind) -> AppStreamGlib.Launchable """
        pass

    def get_launchable_default(self): # real signature unknown; restored from __doc__
        """ get_launchable_default(self) -> AppStreamGlib.Launchable """
        pass

    def get_merge_kind(self): # real signature unknown; restored from __doc__
        """ get_merge_kind(self) -> AppStreamGlib.AppMergeKind """
        pass

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> dict """
        return {}

    def get_metadata_item(self, key): # real signature unknown; restored from __doc__
        """ get_metadata_item(self, key:str) -> str """
        return ""

    def get_metadata_license(self): # real signature unknown; restored from __doc__
        """ get_metadata_license(self) -> str """
        return ""

    def get_mimetypes(self): # real signature unknown; restored from __doc__
        """ get_mimetypes(self) -> list """
        return []

    def get_name(self, locale=None): # real signature unknown; restored from __doc__
        """ get_name(self, locale:str=None) -> str """
        return ""

    def get_names(self): # real signature unknown; restored from __doc__
        """ get_names(self) -> dict """
        return {}

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> str """
        return ""

    def get_permissions(self): # real signature unknown; restored from __doc__
        """ get_permissions(self) -> list """
        return []

    def get_pkgnames(self): # real signature unknown; restored from __doc__
        """ get_pkgnames(self) -> list """
        return []

    def get_pkgname_default(self): # real signature unknown; restored from __doc__
        """ get_pkgname_default(self) -> str """
        return ""

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_project_group(self): # real signature unknown; restored from __doc__
        """ get_project_group(self) -> str """
        return ""

    def get_project_license(self): # real signature unknown; restored from __doc__
        """ get_project_license(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_provides(self): # real signature unknown; restored from __doc__
        """ get_provides(self) -> list """
        return []

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_release(self, version): # real signature unknown; restored from __doc__
        """ get_release(self, version:str) -> AppStreamGlib.Release """
        pass

    def get_releases(self): # real signature unknown; restored from __doc__
        """ get_releases(self) -> list """
        return []

    def get_release_by_version(self, version): # real signature unknown; restored from __doc__
        """ get_release_by_version(self, version:str) -> AppStreamGlib.Release """
        pass

    def get_release_default(self): # real signature unknown; restored from __doc__
        """ get_release_default(self) -> AppStreamGlib.Release """
        pass

    def get_requires(self): # real signature unknown; restored from __doc__
        """ get_requires(self) -> list """
        return []

    def get_require_by_value(self, kind, value): # real signature unknown; restored from __doc__
        """ get_require_by_value(self, kind:AppStreamGlib.RequireKind, value:str) -> AppStreamGlib.Require """
        pass

    def get_reviews(self): # real signature unknown; restored from __doc__
        """ get_reviews(self) -> list """
        return []

    def get_scope(self): # real signature unknown; restored from __doc__
        """ get_scope(self) -> AppStreamGlib.AppScope """
        pass

    def get_screenshots(self): # real signature unknown; restored from __doc__
        """ get_screenshots(self) -> list """
        return []

    def get_screenshot_default(self): # real signature unknown; restored from __doc__
        """ get_screenshot_default(self) -> AppStreamGlib.Screenshot """
        pass

    def get_search_match(self): # real signature unknown; restored from __doc__
        """ get_search_match(self) -> int """
        return 0

    def get_source_file(self): # real signature unknown; restored from __doc__
        """ get_source_file(self) -> str """
        return ""

    def get_source_kind(self): # real signature unknown; restored from __doc__
        """ get_source_kind(self) -> AppStreamGlib.FormatKind """
        pass

    def get_source_pkgname(self): # real signature unknown; restored from __doc__
        """ get_source_pkgname(self) -> str """
        return ""

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> AppStreamGlib.AppState """
        pass

    def get_suggests(self): # real signature unknown; restored from __doc__
        """ get_suggests(self) -> list """
        return []

    def get_translations(self): # real signature unknown; restored from __doc__
        """ get_translations(self) -> list """
        return []

    def get_trust_flags(self): # real signature unknown; restored from __doc__
        """ get_trust_flags(self) -> int """
        return 0

    def get_unique_id(self): # real signature unknown; restored from __doc__
        """ get_unique_id(self) -> str """
        return ""

    def get_update_contact(self): # real signature unknown; restored from __doc__
        """ get_update_contact(self) -> str """
        return ""

    def get_urls(self): # real signature unknown; restored from __doc__
        """ get_urls(self) -> dict """
        return {}

    def get_url_item(self, url_kind): # real signature unknown; restored from __doc__
        """ get_url_item(self, url_kind:AppStreamGlib.UrlKind) -> str """
        return ""

    def get_vetos(self): # real signature unknown; restored from __doc__
        """ get_vetos(self) -> list """
        return []

    def guess_source_kind(self, filename): # real signature unknown; restored from __doc__
        """ guess_source_kind(filename:str) -> AppStreamGlib.FormatKind """
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

    def has_category(self, category): # real signature unknown; restored from __doc__
        """ has_category(self, category:str) -> bool """
        return False

    def has_compulsory_for_desktop(self, desktop): # real signature unknown; restored from __doc__
        """ has_compulsory_for_desktop(self, desktop:str) -> bool """
        return False

    def has_kudo(self, kudo): # real signature unknown; restored from __doc__
        """ has_kudo(self, kudo:str) -> bool """
        return False

    def has_kudo_kind(self, kudo): # real signature unknown; restored from __doc__
        """ has_kudo_kind(self, kudo:AppStreamGlib.KudoKind) -> bool """
        return False

    def has_permission(self, permission): # real signature unknown; restored from __doc__
        """ has_permission(self, permission:str) -> bool """
        return False

    def has_quirk(self, quirk): # real signature unknown; restored from __doc__
        """ has_quirk(self, quirk:AppStreamGlib.AppQuirk) -> bool """
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

    def kind_from_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_from_string(kind:str) -> AppStreamGlib.AppKind """
        pass

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:AppStreamGlib.AppKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def merge_kind_from_string(self, merge_kind): # real signature unknown; restored from __doc__
        """ merge_kind_from_string(merge_kind:str) -> AppStreamGlib.AppMergeKind """
        pass

    def merge_kind_to_string(self, merge_kind): # real signature unknown; restored from __doc__
        """ merge_kind_to_string(merge_kind:AppStreamGlib.AppMergeKind) -> str """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> AppStreamGlib.App """
        pass

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

    def parse_data(self, data, flags): # real signature unknown; restored from __doc__
        """ parse_data(self, data:GLib.Bytes, flags:int) -> bool """
        return False

    def parse_file(self, filename, flags): # real signature unknown; restored from __doc__
        """ parse_file(self, filename:str, flags:int) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_category(self, category): # real signature unknown; restored from __doc__
        """ remove_category(self, category:str) """
        pass

    def remove_format(self, format): # real signature unknown; restored from __doc__
        """ remove_format(self, format:AppStreamGlib.Format) """
        pass

    def remove_kudo(self, kudo): # real signature unknown; restored from __doc__
        """ remove_kudo(self, kudo:str) """
        pass

    def remove_metadata(self, key): # real signature unknown; restored from __doc__
        """ remove_metadata(self, key:str) """
        pass

    def remove_veto(self, description): # real signature unknown; restored from __doc__
        """ remove_veto(self, description:str) """
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

    def scope_from_string(self, scope): # real signature unknown; restored from __doc__
        """ scope_from_string(scope:str) -> AppStreamGlib.AppScope """
        pass

    def scope_to_string(self, scope): # real signature unknown; restored from __doc__
        """ scope_to_string(scope:AppStreamGlib.AppScope) -> str """
        return ""

    def search_matches(self, search): # real signature unknown; restored from __doc__
        """ search_matches(self, search:str) -> int """
        return 0

    def search_matches_all(self, search): # real signature unknown; restored from __doc__
        """ search_matches_all(self, search:str) -> int """
        return 0

    def set_branch(self, branch): # real signature unknown; restored from __doc__
        """ set_branch(self, branch:str) """
        pass

    def set_comment(self, locale=None, comment): # real signature unknown; restored from __doc__
        """ set_comment(self, locale:str=None, comment:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, locale=None, description): # real signature unknown; restored from __doc__
        """ set_description(self, locale:str=None, description:str) """
        pass

    def set_developer_name(self, locale=None, developer_name): # real signature unknown; restored from __doc__
        """ set_developer_name(self, locale:str=None, developer_name:str) """
        pass

    def set_icon_path(self, icon_path): # real signature unknown; restored from __doc__
        """ set_icon_path(self, icon_path:str) """
        pass

    def set_id(self, id): # real signature unknown; restored from __doc__
        """ set_id(self, id:str) """
        pass

    def set_id_kind(self, id_kind): # real signature unknown; restored from __doc__
        """ set_id_kind(self, id_kind:AppStreamGlib.IdKind) """
        pass

    def set_kind(self, kind): # real signature unknown; restored from __doc__
        """ set_kind(self, kind:AppStreamGlib.AppKind) """
        pass

    def set_merge_kind(self, merge_kind): # real signature unknown; restored from __doc__
        """ set_merge_kind(self, merge_kind:AppStreamGlib.AppMergeKind) """
        pass

    def set_metadata_license(self, metadata_license): # real signature unknown; restored from __doc__
        """ set_metadata_license(self, metadata_license:str) """
        pass

    def set_name(self, locale=None, name): # real signature unknown; restored from __doc__
        """ set_name(self, locale:str=None, name:str) """
        pass

    def set_origin(self, origin): # real signature unknown; restored from __doc__
        """ set_origin(self, origin:str) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_project_group(self, project_group): # real signature unknown; restored from __doc__
        """ set_project_group(self, project_group:str) """
        pass

    def set_project_license(self, project_license): # real signature unknown; restored from __doc__
        """ set_project_license(self, project_license:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_scope(self, scope): # real signature unknown; restored from __doc__
        """ set_scope(self, scope:AppStreamGlib.AppScope) """
        pass

    def set_search_match(self, search_match): # real signature unknown; restored from __doc__
        """ set_search_match(self, search_match:int) """
        pass

    def set_source_file(self, source_file): # real signature unknown; restored from __doc__
        """ set_source_file(self, source_file:str) """
        pass

    def set_source_kind(self, source_kind): # real signature unknown; restored from __doc__
        """ set_source_kind(self, source_kind:AppStreamGlib.FormatKind) """
        pass

    def set_source_pkgname(self, source_pkgname): # real signature unknown; restored from __doc__
        """ set_source_pkgname(self, source_pkgname:str) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:AppStreamGlib.AppState) """
        pass

    def set_trust_flags(self, trust_flags): # real signature unknown; restored from __doc__
        """ set_trust_flags(self, trust_flags:int) """
        pass

    def set_update_contact(self, update_contact): # real signature unknown; restored from __doc__
        """ set_update_contact(self, update_contact:str) """
        pass

    def source_kind_from_string(self, source_kind): # real signature unknown; restored from __doc__
        """ source_kind_from_string(source_kind:str) -> AppStreamGlib.FormatKind """
        pass

    def source_kind_to_string(self, source_kind): # real signature unknown; restored from __doc__
        """ source_kind_to_string(source_kind:AppStreamGlib.FormatKind) -> str """
        return ""

    def state_to_string(self, state): # real signature unknown; restored from __doc__
        """ state_to_string(state:AppStreamGlib.AppState) -> str """
        return ""

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

    def subsume(self, donor): # real signature unknown; restored from __doc__
        """ subsume(self, donor:AppStreamGlib.App) """
        pass

    def subsume_full(self, donor, flags): # real signature unknown; restored from __doc__
        """ subsume_full(self, donor:AppStreamGlib.App, flags:int) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def to_file(self, file, cancellable=None): # real signature unknown; restored from __doc__
        """ to_file(self, file:Gio.File, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def to_xml(self): # real signature unknown; restored from __doc__
        """ to_xml(self) -> GLib.String """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def validate(self, flags): # real signature unknown; restored from __doc__
        """ validate(self, flags:int) -> list """
        return []

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001afbef6b3a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(App), '__module__': 'gi.repository.AppStreamGlib', '__gtype__': <GType AsApp (3189448256)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new, bound=None), 'error_quark': gi.FunctionInfo(error_quark, bound=None), 'guess_source_kind': gi.FunctionInfo(guess_source_kind, bound=None), 'kind_from_string': gi.FunctionInfo(kind_from_string, bound=None), 'kind_to_string': gi.FunctionInfo(kind_to_string, bound=None), 'merge_kind_from_string': gi.FunctionInfo(merge_kind_from_string, bound=None), 'merge_kind_to_string': gi.FunctionInfo(merge_kind_to_string, bound=None), 'scope_from_string': gi.FunctionInfo(scope_from_string, bound=None), 'scope_to_string': gi.FunctionInfo(scope_to_string, bound=None), 'source_kind_from_string': gi.FunctionInfo(source_kind_from_string, bound=None), 'source_kind_to_string': gi.FunctionInfo(source_kind_to_string, bound=None), 'state_to_string': gi.FunctionInfo(state_to_string, bound=None), 'add_addon': gi.FunctionInfo(add_addon, bound=None), 'add_agreement': gi.FunctionInfo(add_agreement, bound=None), 'add_arch': gi.FunctionInfo(add_arch, bound=None), 'add_bundle': gi.FunctionInfo(add_bundle, bound=None), 'add_category': gi.FunctionInfo(add_category, bound=None), 'add_compulsory_for_desktop': gi.FunctionInfo(add_compulsory_for_desktop, bound=None), 'add_content_rating': gi.FunctionInfo(add_content_rating, bound=None), 'add_extends': gi.FunctionInfo(add_extends, bound=None), 'add_format': gi.FunctionInfo(add_format, bound=None), 'add_icon': gi.FunctionInfo(add_icon, bound=None), 'add_keyword': gi.FunctionInfo(add_keyword, bound=None), 'add_kudo': gi.FunctionInfo(add_kudo, bound=None), 'add_kudo_kind': gi.FunctionInfo(add_kudo_kind, bound=None), 'add_language': gi.FunctionInfo(add_language, bound=None), 'add_launchable': gi.FunctionInfo(add_launchable, bound=None), 'add_metadata': gi.FunctionInfo(add_metadata, bound=None), 'add_mimetype': gi.FunctionInfo(add_mimetype, bound=None), 'add_permission': gi.FunctionInfo(add_permission, bound=None), 'add_pkgname': gi.FunctionInfo(add_pkgname, bound=None), 'add_provide': gi.FunctionInfo(add_provide, bound=None), 'add_quirk': gi.FunctionInfo(add_quirk, bound=None), 'add_release': gi.FunctionInfo(add_release, bound=None), 'add_require': gi.FunctionInfo(add_require, bound=None), 'add_review': gi.FunctionInfo(add_review, bound=None), 'add_screenshot': gi.FunctionInfo(add_screenshot, bound=None), 'add_suggest': gi.FunctionInfo(add_suggest, bound=None), 'add_translation': gi.FunctionInfo(add_translation, bound=None), 'add_url': gi.FunctionInfo(add_url, bound=None), 'convert_icons': gi.FunctionInfo(convert_icons, bound=None), 'equal': gi.FunctionInfo(equal, bound=None), 'get_addons': gi.FunctionInfo(get_addons, bound=None), 'get_agreement_by_kind': gi.FunctionInfo(get_agreement_by_kind, bound=None), 'get_agreement_default': gi.FunctionInfo(get_agreement_default, bound=None), 'get_architectures': gi.FunctionInfo(get_architectures, bound=None), 'get_branch': gi.FunctionInfo(get_branch, bound=None), 'get_bundle_default': gi.FunctionInfo(get_bundle_default, bound=None), 'get_bundles': gi.FunctionInfo(get_bundles, bound=None), 'get_categories': gi.FunctionInfo(get_categories, bound=None), 'get_comment': gi.FunctionInfo(get_comment, bound=None), 'get_comments': gi.FunctionInfo(get_comments, bound=None), 'get_compulsory_for_desktops': gi.FunctionInfo(get_compulsory_for_desktops, bound=None), 'get_content_rating': gi.FunctionInfo(get_content_rating, bound=None), 'get_content_ratings': gi.FunctionInfo(get_content_ratings, bound=None), 'get_description': gi.FunctionInfo(get_description, bound=None), 'get_descriptions': gi.FunctionInfo(get_descriptions, bound=None), 'get_developer_name': gi.FunctionInfo(get_developer_name, bound=None), 'get_developer_names': gi.FunctionInfo(get_developer_names, bound=None), 'get_extends': gi.FunctionInfo(get_extends, bound=None), 'get_format_by_filename': gi.FunctionInfo(get_format_by_filename, bound=None), 'get_format_by_kind': gi.FunctionInfo(get_format_by_kind, bound=None), 'get_format_default': gi.FunctionInfo(get_format_default, bound=None), 'get_formats': gi.FunctionInfo(get_formats, bound=None), 'get_icon_default': gi.FunctionInfo(get_icon_default, bound=None), 'get_icon_for_size': gi.FunctionInfo(get_icon_for_size, bound=None), 'get_icon_path': gi.FunctionInfo(get_icon_path, bound=None), 'get_icons': gi.FunctionInfo(get_icons, bound=None), 'get_id': gi.FunctionInfo(get_id, bound=None), 'get_id_filename': gi.FunctionInfo(get_id_filename, bound=None), 'get_id_kind': gi.FunctionInfo(get_id_kind, bound=None), 'get_id_no_prefix': gi.FunctionInfo(get_id_no_prefix, bound=None), 'get_keywords': gi.FunctionInfo(get_keywords, bound=None), 'get_kind': gi.FunctionInfo(get_kind, bound=None), 'get_kudos': gi.FunctionInfo(get_kudos, bound=None), 'get_language': gi.FunctionInfo(get_language, bound=None), 'get_languages': gi.FunctionInfo(get_languages, bound=None), 'get_launchable_by_kind': gi.FunctionInfo(get_launchable_by_kind, bound=None), 'get_launchable_default': gi.FunctionInfo(get_launchable_default, bound=None), 'get_launchables': gi.FunctionInfo(get_launchables, bound=None), 'get_merge_kind': gi.FunctionInfo(get_merge_kind, bound=None), 'get_metadata': gi.FunctionInfo(get_metadata, bound=None), 'get_metadata_item': gi.FunctionInfo(get_metadata_item, bound=None), 'get_metadata_license': gi.FunctionInfo(get_metadata_license, bound=None), 'get_mimetypes': gi.FunctionInfo(get_mimetypes, bound=None), 'get_name': gi.FunctionInfo(get_name, bound=None), 'get_names': gi.FunctionInfo(get_names, bound=None), 'get_origin': gi.FunctionInfo(get_origin, bound=None), 'get_permissions': gi.FunctionInfo(get_permissions, bound=None), 'get_pkgname_default': gi.FunctionInfo(get_pkgname_default, bound=None), 'get_pkgnames': gi.FunctionInfo(get_pkgnames, bound=None), 'get_priority': gi.FunctionInfo(get_priority, bound=None), 'get_project_group': gi.FunctionInfo(get_project_group, bound=None), 'get_project_license': gi.FunctionInfo(get_project_license, bound=None), 'get_provides': gi.FunctionInfo(get_provides, bound=None), 'get_release': gi.FunctionInfo(get_release, bound=None), 'get_release_by_version': gi.FunctionInfo(get_release_by_version, bound=None), 'get_release_default': gi.FunctionInfo(get_release_default, bound=None), 'get_releases': gi.FunctionInfo(get_releases, bound=None), 'get_require_by_value': gi.FunctionInfo(get_require_by_value, bound=None), 'get_requires': gi.FunctionInfo(get_requires, bound=None), 'get_reviews': gi.FunctionInfo(get_reviews, bound=None), 'get_scope': gi.FunctionInfo(get_scope, bound=None), 'get_screenshot_default': gi.FunctionInfo(get_screenshot_default, bound=None), 'get_screenshots': gi.FunctionInfo(get_screenshots, bound=None), 'get_search_match': gi.FunctionInfo(get_search_match, bound=None), 'get_source_file': gi.FunctionInfo(get_source_file, bound=None), 'get_source_kind': gi.FunctionInfo(get_source_kind, bound=None), 'get_source_pkgname': gi.FunctionInfo(get_source_pkgname, bound=None), 'get_state': gi.FunctionInfo(get_state, bound=None), 'get_suggests': gi.FunctionInfo(get_suggests, bound=None), 'get_translations': gi.FunctionInfo(get_translations, bound=None), 'get_trust_flags': gi.FunctionInfo(get_trust_flags, bound=None), 'get_unique_id': gi.FunctionInfo(get_unique_id, bound=None), 'get_update_contact': gi.FunctionInfo(get_update_contact, bound=None), 'get_url_item': gi.FunctionInfo(get_url_item, bound=None), 'get_urls': gi.FunctionInfo(get_urls, bound=None), 'get_vetos': gi.FunctionInfo(get_vetos, bound=None), 'has_category': gi.FunctionInfo(has_category, bound=None), 'has_compulsory_for_desktop': gi.FunctionInfo(has_compulsory_for_desktop, bound=None), 'has_kudo': gi.FunctionInfo(has_kudo, bound=None), 'has_kudo_kind': gi.FunctionInfo(has_kudo_kind, bound=None), 'has_permission': gi.FunctionInfo(has_permission, bound=None), 'has_quirk': gi.FunctionInfo(has_quirk, bound=None), 'parse_data': gi.FunctionInfo(parse_data, bound=None), 'parse_file': gi.FunctionInfo(parse_file, bound=None), 'remove_category': gi.FunctionInfo(remove_category, bound=None), 'remove_format': gi.FunctionInfo(remove_format, bound=None), 'remove_kudo': gi.FunctionInfo(remove_kudo, bound=None), 'remove_metadata': gi.FunctionInfo(remove_metadata, bound=None), 'remove_veto': gi.FunctionInfo(remove_veto, bound=None), 'search_matches': gi.FunctionInfo(search_matches, bound=None), 'search_matches_all': gi.FunctionInfo(search_matches_all, bound=None), 'set_branch': gi.FunctionInfo(set_branch, bound=None), 'set_comment': gi.FunctionInfo(set_comment, bound=None), 'set_description': gi.FunctionInfo(set_description, bound=None), 'set_developer_name': gi.FunctionInfo(set_developer_name, bound=None), 'set_icon_path': gi.FunctionInfo(set_icon_path, bound=None), 'set_id': gi.FunctionInfo(set_id, bound=None), 'set_id_kind': gi.FunctionInfo(set_id_kind, bound=None), 'set_kind': gi.FunctionInfo(set_kind, bound=None), 'set_merge_kind': gi.FunctionInfo(set_merge_kind, bound=None), 'set_metadata_license': gi.FunctionInfo(set_metadata_license, bound=None), 'set_name': gi.FunctionInfo(set_name, bound=None), 'set_origin': gi.FunctionInfo(set_origin, bound=None), 'set_priority': gi.FunctionInfo(set_priority, bound=None), 'set_project_group': gi.FunctionInfo(set_project_group, bound=None), 'set_project_license': gi.FunctionInfo(set_project_license, bound=None), 'set_scope': gi.FunctionInfo(set_scope, bound=None), 'set_search_match': gi.FunctionInfo(set_search_match, bound=None), 'set_source_file': gi.FunctionInfo(set_source_file, bound=None), 'set_source_kind': gi.FunctionInfo(set_source_kind, bound=None), 'set_source_pkgname': gi.FunctionInfo(set_source_pkgname, bound=None), 'set_state': gi.FunctionInfo(set_state, bound=None), 'set_trust_flags': gi.FunctionInfo(set_trust_flags, bound=None), 'set_update_contact': gi.FunctionInfo(set_update_contact, bound=None), 'subsume': gi.FunctionInfo(subsume, bound=None), 'subsume_full': gi.FunctionInfo(subsume_full, bound=None), 'to_file': gi.FunctionInfo(to_file, bound=None), 'to_xml': gi.FunctionInfo(to_xml, bound=None), 'validate': gi.FunctionInfo(validate, bound=None), 'parent_instance': <property object at 0x000001afbeae7420>})"
    __gdoc__ = 'Object AsApp\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AsApp (3189448256)>'
    __info__ = ObjectInfo(App)


