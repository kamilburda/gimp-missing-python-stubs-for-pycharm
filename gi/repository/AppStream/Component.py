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


class Component(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Component(**properties)
        new() -> AppStream.Component
    """
    def add_addon(self, addon): # real signature unknown; restored from __doc__
        """ add_addon(self, addon:AppStream.Component) """
        pass

    def add_agreement(self, agreement): # real signature unknown; restored from __doc__
        """ add_agreement(self, agreement:AppStream.Agreement) """
        pass

    def add_bundle(self, bundle): # real signature unknown; restored from __doc__
        """ add_bundle(self, bundle:AppStream.Bundle) """
        pass

    def add_category(self, category): # real signature unknown; restored from __doc__
        """ add_category(self, category:str) """
        pass

    def add_content_rating(self, content_rating): # real signature unknown; restored from __doc__
        """ add_content_rating(self, content_rating:AppStream.ContentRating) """
        pass

    def add_extends(self, cpt_id): # real signature unknown; restored from __doc__
        """ add_extends(self, cpt_id:str) """
        pass

    def add_icon(self, icon): # real signature unknown; restored from __doc__
        """ add_icon(self, icon:AppStream.Icon) """
        pass

    def add_keyword(self, keyword, locale=None): # real signature unknown; restored from __doc__
        """ add_keyword(self, keyword:str, locale:str=None) """
        pass

    def add_language(self, locale=None, percentage): # real signature unknown; restored from __doc__
        """ add_language(self, locale:str=None, percentage:int) """
        pass

    def add_launchable(self, launchable): # real signature unknown; restored from __doc__
        """ add_launchable(self, launchable:AppStream.Launchable) """
        pass

    def add_provided(self, prov): # real signature unknown; restored from __doc__
        """ add_provided(self, prov:AppStream.Provided) """
        pass

    def add_provided_item(self, kind, item): # real signature unknown; restored from __doc__
        """ add_provided_item(self, kind:AppStream.ProvidedKind, item:str) """
        pass

    def add_reference(self, reference): # real signature unknown; restored from __doc__
        """ add_reference(self, reference:AppStream.Reference) """
        pass

    def add_relation(self, relation): # real signature unknown; restored from __doc__
        """ add_relation(self, relation:AppStream.Relation) """
        pass

    def add_release(self, release): # real signature unknown; restored from __doc__
        """ add_release(self, release:AppStream.Release) """
        pass

    def add_replaces(self, cid): # real signature unknown; restored from __doc__
        """ add_replaces(self, cid:str) """
        pass

    def add_review(self, review): # real signature unknown; restored from __doc__
        """ add_review(self, review:AppStream.Review) """
        pass

    def add_screenshot(self, sshot): # real signature unknown; restored from __doc__
        """ add_screenshot(self, sshot:AppStream.Screenshot) """
        pass

    def add_suggested(self, suggested): # real signature unknown; restored from __doc__
        """ add_suggested(self, suggested:AppStream.Suggested) """
        pass

    def add_tag(self, ns, tag): # real signature unknown; restored from __doc__
        """ add_tag(self, ns:str, tag:str) -> bool """
        return False

    def add_translation(self, tr): # real signature unknown; restored from __doc__
        """ add_translation(self, tr:AppStream.Translation) """
        pass

    def add_url(self, url_kind, url): # real signature unknown; restored from __doc__
        """ add_url(self, url_kind:AppStream.UrlKind, url:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_relations(self, sysinfo=None, pool=None, rel_kind): # real signature unknown; restored from __doc__
        """ check_relations(self, sysinfo:AppStream.SystemInfo=None, pool:AppStream.Pool=None, rel_kind:AppStream.RelationKind) -> list """
        return []

    def clear_keywords(self, locale=None): # real signature unknown; restored from __doc__
        """ clear_keywords(self, locale:str=None) """
        pass

    def clear_languages(self): # real signature unknown; restored from __doc__
        """ clear_languages(self) """
        pass

    def clear_tags(self): # real signature unknown; restored from __doc__
        """ clear_tags(self) """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, connect_flags=0): # reliably restored by inspect
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
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

    def get_addons(self): # real signature unknown; restored from __doc__
        """ get_addons(self) -> list """
        return []

    def get_agreements(self): # real signature unknown; restored from __doc__
        """ get_agreements(self) -> list """
        return []

    def get_agreement_by_kind(self, kind): # real signature unknown; restored from __doc__
        """ get_agreement_by_kind(self, kind:AppStream.AgreementKind) -> AppStream.Agreement or None """
        pass

    def get_branch(self): # real signature unknown; restored from __doc__
        """ get_branch(self) -> str """
        return ""

    def get_branding(self): # real signature unknown; restored from __doc__
        """ get_branding(self) -> AppStream.Branding or None """
        pass

    def get_bundle(self, bundle_kind): # real signature unknown; restored from __doc__
        """ get_bundle(self, bundle_kind:AppStream.BundleKind) -> AppStream.Bundle or None """
        pass

    def get_bundles(self): # real signature unknown; restored from __doc__
        """ get_bundles(self) -> list """
        return []

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> list """
        return []

    def get_compulsory_for_desktops(self): # real signature unknown; restored from __doc__
        """ get_compulsory_for_desktops(self) -> list """
        return []

    def get_content_rating(self, kind): # real signature unknown; restored from __doc__
        """ get_content_rating(self, kind:str) -> AppStream.ContentRating or None """
        pass

    def get_content_ratings(self): # real signature unknown; restored from __doc__
        """ get_content_ratings(self) -> list """
        return []

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) -> AppStream.Context or None """
        pass

    def get_custom(self): # real signature unknown; restored from __doc__
        """ get_custom(self) -> dict """
        return {}

    def get_custom_value(self, key): # real signature unknown; restored from __doc__
        """ get_custom_value(self, key:str) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_data_id(self): # real signature unknown; restored from __doc__
        """ get_data_id(self) -> str """
        return ""

    def get_date_eol(self): # real signature unknown; restored from __doc__
        """ get_date_eol(self) -> str """
        return ""

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_developer(self): # real signature unknown; restored from __doc__
        """ get_developer(self) -> AppStream.Developer """
        pass

    def get_extends(self): # real signature unknown; restored from __doc__
        """ get_extends(self) -> list or None """
        return []

    def get_icons(self): # real signature unknown; restored from __doc__
        """ get_icons(self) -> list """
        return []

    def get_icon_by_size(self, width, height): # real signature unknown; restored from __doc__
        """ get_icon_by_size(self, width:int, height:int) -> AppStream.Icon or None """
        pass

    def get_icon_stock(self): # real signature unknown; restored from __doc__
        """ get_icon_stock(self) -> AppStream.Icon or None """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_keywords(self): # real signature unknown; restored from __doc__
        """ get_keywords(self) -> list """
        return []

    def get_keywords_table(self): # real signature unknown; restored from __doc__
        """ get_keywords_table(self) -> dict """
        return {}

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> AppStream.ComponentKind """
        pass

    def get_language(self, locale=None): # real signature unknown; restored from __doc__
        """ get_language(self, locale:str=None) -> int """
        return 0

    def get_languages(self): # real signature unknown; restored from __doc__
        """ get_languages(self) -> list """
        return []

    def get_launchable(self, kind): # real signature unknown; restored from __doc__
        """ get_launchable(self, kind:AppStream.LaunchableKind) -> AppStream.Launchable or None """
        pass

    def get_launchables(self): # real signature unknown; restored from __doc__
        """ get_launchables(self) -> list """
        return []

    def get_merge_kind(self): # real signature unknown; restored from __doc__
        """ get_merge_kind(self) -> AppStream.MergeKind """
        pass

    def get_metadata_license(self): # real signature unknown; restored from __doc__
        """ get_metadata_license(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_name_table(self): # real signature unknown; restored from __doc__
        """ get_name_table(self) -> dict """
        return {}

    def get_name_variant_suffix(self): # real signature unknown; restored from __doc__
        """ get_name_variant_suffix(self) -> str """
        return ""

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> str """
        return ""

    def get_pkgname(self): # real signature unknown; restored from __doc__
        """ get_pkgname(self) -> str """
        return ""

    def get_pkgnames(self): # real signature unknown; restored from __doc__
        """ get_pkgnames(self) -> list """
        return []

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

    def get_provided(self): # real signature unknown; restored from __doc__
        """ get_provided(self) -> list """
        return []

    def get_provided_for_kind(self, kind): # real signature unknown; restored from __doc__
        """ get_provided_for_kind(self, kind:AppStream.ProvidedKind) -> AppStream.Provided or None """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_recommends(self): # real signature unknown; restored from __doc__
        """ get_recommends(self) -> list """
        return []

    def get_references(self): # real signature unknown; restored from __doc__
        """ get_references(self) -> list """
        return []

    def get_releases_plain(self): # real signature unknown; restored from __doc__
        """ get_releases_plain(self) -> AppStream.ReleaseList """
        pass

    def get_replaces(self): # real signature unknown; restored from __doc__
        """ get_replaces(self) -> list """
        return []

    def get_requires(self): # real signature unknown; restored from __doc__
        """ get_requires(self) -> list """
        return []

    def get_reviews(self): # real signature unknown; restored from __doc__
        """ get_reviews(self) -> list """
        return []

    def get_scope(self): # real signature unknown; restored from __doc__
        """ get_scope(self) -> AppStream.ComponentScope """
        pass

    def get_screenshots_all(self): # real signature unknown; restored from __doc__
        """ get_screenshots_all(self) -> list """
        return []

    def get_search_tokens(self): # real signature unknown; restored from __doc__
        """ get_search_tokens(self) -> list """
        return []

    def get_sort_score(self): # real signature unknown; restored from __doc__
        """ get_sort_score(self) -> int """
        return 0

    def get_source_pkgname(self): # real signature unknown; restored from __doc__
        """ get_source_pkgname(self) -> str """
        return ""

    def get_suggested(self): # real signature unknown; restored from __doc__
        """ get_suggested(self) -> list """
        return []

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_summary_table(self): # real signature unknown; restored from __doc__
        """ get_summary_table(self) -> dict """
        return {}

    def get_supports(self): # real signature unknown; restored from __doc__
        """ get_supports(self) -> list """
        return []

    def get_system_compatibility_score(self, sysinfo, is_template): # real signature unknown; restored from __doc__
        """ get_system_compatibility_score(self, sysinfo:AppStream.SystemInfo, is_template:bool) -> int, results:list """
        return 0

    def get_timestamp_eol(self): # real signature unknown; restored from __doc__
        """ get_timestamp_eol(self) -> int """
        return 0

    def get_translations(self): # real signature unknown; restored from __doc__
        """ get_translations(self) -> list """
        return []

    def get_url(self, url_kind): # real signature unknown; restored from __doc__
        """ get_url(self, url_kind:AppStream.UrlKind) -> str or None """
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

    def has_bundle(self): # real signature unknown; restored from __doc__
        """ has_bundle(self) -> bool """
        return False

    def has_category(self, category): # real signature unknown; restored from __doc__
        """ has_category(self, category:str) -> bool """
        return False

    def has_tag(self, ns, tag): # real signature unknown; restored from __doc__
        """ has_tag(self, ns:str, tag:str) -> bool """
        return False

    def insert_custom_value(self, key, value): # real signature unknown; restored from __doc__
        """ insert_custom_value(self, key:str, value:str) -> bool """
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

    def is_compulsory_for_desktop(self, desktop): # real signature unknown; restored from __doc__
        """ is_compulsory_for_desktop(self, desktop:str) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_floss(self): # real signature unknown; restored from __doc__
        """ is_floss(self) -> bool """
        return False

    def is_ignored(self): # real signature unknown; restored from __doc__
        """ is_ignored(self) -> bool """
        return False

    def is_member_of_category(self, category): # real signature unknown; restored from __doc__
        """ is_member_of_category(self, category:AppStream.Category) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def load_from_bytes(self, context, format, bytes): # real signature unknown; restored from __doc__
        """ load_from_bytes(self, context:AppStream.Context, format:AppStream.FormatKind, bytes:GLib.Bytes) -> bool """
        return False

    def load_releases(self, allow_net): # real signature unknown; restored from __doc__
        """ load_releases(self, allow_net:bool) -> AppStream.ReleaseList or None """
        pass

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> AppStream.Component """
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

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_tag(self, ns, tag): # real signature unknown; restored from __doc__
        """ remove_tag(self, ns:str, tag:str) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def search_matches(self, term): # real signature unknown; restored from __doc__
        """ search_matches(self, term:str) -> int """
        return 0

    def search_matches_all(self, terms): # real signature unknown; restored from __doc__
        """ search_matches_all(self, terms:str) -> int """
        return 0

    def set_branch(self, branch): # real signature unknown; restored from __doc__
        """ set_branch(self, branch:str) """
        pass

    def set_branding(self, branding): # real signature unknown; restored from __doc__
        """ set_branding(self, branding:AppStream.Branding) """
        pass

    def set_compulsory_for_desktop(self, desktop): # real signature unknown; restored from __doc__
        """ set_compulsory_for_desktop(self, desktop:str) """
        pass

    def set_context(self, context): # real signature unknown; restored from __doc__
        """ set_context(self, context:AppStream.Context) """
        pass

    def set_context_locale(self, locale): # real signature unknown; restored from __doc__
        """ set_context_locale(self, locale:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data_id(self, value): # real signature unknown; restored from __doc__
        """ set_data_id(self, value:str) """
        pass

    def set_date_eol(self, date): # real signature unknown; restored from __doc__
        """ set_date_eol(self, date:str) """
        pass

    def set_description(self, value, locale=None): # real signature unknown; restored from __doc__
        """ set_description(self, value:str, locale:str=None) """
        pass

    def set_developer(self, developer): # real signature unknown; restored from __doc__
        """ set_developer(self, developer:AppStream.Developer) """
        pass

    def set_id(self, value): # real signature unknown; restored from __doc__
        """ set_id(self, value:str) """
        pass

    def set_keywords(self, new_keywords, locale=None, deep_copy): # real signature unknown; restored from __doc__
        """ set_keywords(self, new_keywords:list, locale:str=None, deep_copy:bool) """
        pass

    def set_kind(self, value): # real signature unknown; restored from __doc__
        """ set_kind(self, value:AppStream.ComponentKind) """
        pass

    def set_merge_kind(self, kind): # real signature unknown; restored from __doc__
        """ set_merge_kind(self, kind:AppStream.MergeKind) """
        pass

    def set_metadata_license(self, value): # real signature unknown; restored from __doc__
        """ set_metadata_license(self, value:str) """
        pass

    def set_name(self, value, locale=None): # real signature unknown; restored from __doc__
        """ set_name(self, value:str, locale:str=None) """
        pass

    def set_name_variant_suffix(self, value, locale=None): # real signature unknown; restored from __doc__
        """ set_name_variant_suffix(self, value:str, locale:str=None) """
        pass

    def set_origin(self, origin): # real signature unknown; restored from __doc__
        """ set_origin(self, origin:str) """
        pass

    def set_pkgname(self, pkgname): # real signature unknown; restored from __doc__
        """ set_pkgname(self, pkgname:str) """
        pass

    def set_pkgnames(self, packages): # real signature unknown; restored from __doc__
        """ set_pkgnames(self, packages:list) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_project_group(self, value): # real signature unknown; restored from __doc__
        """ set_project_group(self, value:str) """
        pass

    def set_project_license(self, value): # real signature unknown; restored from __doc__
        """ set_project_license(self, value:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_releases(self, releases): # real signature unknown; restored from __doc__
        """ set_releases(self, releases:AppStream.ReleaseList) """
        pass

    def set_scope(self, scope): # real signature unknown; restored from __doc__
        """ set_scope(self, scope:AppStream.ComponentScope) """
        pass

    def set_sort_score(self, score): # real signature unknown; restored from __doc__
        """ set_sort_score(self, score:int) """
        pass

    def set_source_pkgname(self, spkgname): # real signature unknown; restored from __doc__
        """ set_source_pkgname(self, spkgname:str) """
        pass

    def set_summary(self, value, locale=None): # real signature unknown; restored from __doc__
        """ set_summary(self, value:str, locale:str=None) """
        pass

    def sort_screenshots(self, environment=None, style=None, prioritize_style): # real signature unknown; restored from __doc__
        """ sort_screenshots(self, environment:str=None, style:str=None, prioritize_style:bool) """
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

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def to_xml_data(self, context): # real signature unknown; restored from __doc__
        """ to_xml_data(self, context:AppStream.Context) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self): # reliably restored by inspect
        """ Deprecated, do not explicitly float GObjects. """
        pass

    def _ref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _ref_sink(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ece9975bd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Component), '__module__': 'gi.repository.AppStream', '__gtype__': <GType AsComponent (3928800544)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'add_addon': gi.FunctionInfo(add_addon), 'add_agreement': gi.FunctionInfo(add_agreement), 'add_bundle': gi.FunctionInfo(add_bundle), 'add_category': gi.FunctionInfo(add_category), 'add_content_rating': gi.FunctionInfo(add_content_rating), 'add_extends': gi.FunctionInfo(add_extends), 'add_icon': gi.FunctionInfo(add_icon), 'add_keyword': gi.FunctionInfo(add_keyword), 'add_language': gi.FunctionInfo(add_language), 'add_launchable': gi.FunctionInfo(add_launchable), 'add_provided': gi.FunctionInfo(add_provided), 'add_provided_item': gi.FunctionInfo(add_provided_item), 'add_reference': gi.FunctionInfo(add_reference), 'add_relation': gi.FunctionInfo(add_relation), 'add_release': gi.FunctionInfo(add_release), 'add_replaces': gi.FunctionInfo(add_replaces), 'add_review': gi.FunctionInfo(add_review), 'add_screenshot': gi.FunctionInfo(add_screenshot), 'add_suggested': gi.FunctionInfo(add_suggested), 'add_tag': gi.FunctionInfo(add_tag), 'add_translation': gi.FunctionInfo(add_translation), 'add_url': gi.FunctionInfo(add_url), 'check_relations': gi.FunctionInfo(check_relations), 'clear_keywords': gi.FunctionInfo(clear_keywords), 'clear_languages': gi.FunctionInfo(clear_languages), 'clear_tags': gi.FunctionInfo(clear_tags), 'get_addons': gi.FunctionInfo(get_addons), 'get_agreement_by_kind': gi.FunctionInfo(get_agreement_by_kind), 'get_agreements': gi.FunctionInfo(get_agreements), 'get_branch': gi.FunctionInfo(get_branch), 'get_branding': gi.FunctionInfo(get_branding), 'get_bundle': gi.FunctionInfo(get_bundle), 'get_bundles': gi.FunctionInfo(get_bundles), 'get_categories': gi.FunctionInfo(get_categories), 'get_compulsory_for_desktops': gi.FunctionInfo(get_compulsory_for_desktops), 'get_content_rating': gi.FunctionInfo(get_content_rating), 'get_content_ratings': gi.FunctionInfo(get_content_ratings), 'get_context': gi.FunctionInfo(get_context), 'get_custom': gi.FunctionInfo(get_custom), 'get_custom_value': gi.FunctionInfo(get_custom_value), 'get_data_id': gi.FunctionInfo(get_data_id), 'get_date_eol': gi.FunctionInfo(get_date_eol), 'get_description': gi.FunctionInfo(get_description), 'get_developer': gi.FunctionInfo(get_developer), 'get_extends': gi.FunctionInfo(get_extends), 'get_icon_by_size': gi.FunctionInfo(get_icon_by_size), 'get_icon_stock': gi.FunctionInfo(get_icon_stock), 'get_icons': gi.FunctionInfo(get_icons), 'get_id': gi.FunctionInfo(get_id), 'get_keywords': gi.FunctionInfo(get_keywords), 'get_keywords_table': gi.FunctionInfo(get_keywords_table), 'get_kind': gi.FunctionInfo(get_kind), 'get_language': gi.FunctionInfo(get_language), 'get_languages': gi.FunctionInfo(get_languages), 'get_launchable': gi.FunctionInfo(get_launchable), 'get_launchables': gi.FunctionInfo(get_launchables), 'get_merge_kind': gi.FunctionInfo(get_merge_kind), 'get_metadata_license': gi.FunctionInfo(get_metadata_license), 'get_name': gi.FunctionInfo(get_name), 'get_name_table': gi.FunctionInfo(get_name_table), 'get_name_variant_suffix': gi.FunctionInfo(get_name_variant_suffix), 'get_origin': gi.FunctionInfo(get_origin), 'get_pkgname': gi.FunctionInfo(get_pkgname), 'get_pkgnames': gi.FunctionInfo(get_pkgnames), 'get_priority': gi.FunctionInfo(get_priority), 'get_project_group': gi.FunctionInfo(get_project_group), 'get_project_license': gi.FunctionInfo(get_project_license), 'get_provided': gi.FunctionInfo(get_provided), 'get_provided_for_kind': gi.FunctionInfo(get_provided_for_kind), 'get_recommends': gi.FunctionInfo(get_recommends), 'get_references': gi.FunctionInfo(get_references), 'get_releases_plain': gi.FunctionInfo(get_releases_plain), 'get_replaces': gi.FunctionInfo(get_replaces), 'get_requires': gi.FunctionInfo(get_requires), 'get_reviews': gi.FunctionInfo(get_reviews), 'get_scope': gi.FunctionInfo(get_scope), 'get_screenshots_all': gi.FunctionInfo(get_screenshots_all), 'get_search_tokens': gi.FunctionInfo(get_search_tokens), 'get_sort_score': gi.FunctionInfo(get_sort_score), 'get_source_pkgname': gi.FunctionInfo(get_source_pkgname), 'get_suggested': gi.FunctionInfo(get_suggested), 'get_summary': gi.FunctionInfo(get_summary), 'get_summary_table': gi.FunctionInfo(get_summary_table), 'get_supports': gi.FunctionInfo(get_supports), 'get_system_compatibility_score': gi.FunctionInfo(get_system_compatibility_score), 'get_timestamp_eol': gi.FunctionInfo(get_timestamp_eol), 'get_translations': gi.FunctionInfo(get_translations), 'get_url': gi.FunctionInfo(get_url), 'has_bundle': gi.FunctionInfo(has_bundle), 'has_category': gi.FunctionInfo(has_category), 'has_tag': gi.FunctionInfo(has_tag), 'insert_custom_value': gi.FunctionInfo(insert_custom_value), 'is_compulsory_for_desktop': gi.FunctionInfo(is_compulsory_for_desktop), 'is_floss': gi.FunctionInfo(is_floss), 'is_ignored': gi.FunctionInfo(is_ignored), 'is_member_of_category': gi.FunctionInfo(is_member_of_category), 'is_valid': gi.FunctionInfo(is_valid), 'load_from_bytes': gi.FunctionInfo(load_from_bytes), 'load_releases': gi.FunctionInfo(load_releases), 'remove_tag': gi.FunctionInfo(remove_tag), 'search_matches': gi.FunctionInfo(search_matches), 'search_matches_all': gi.FunctionInfo(search_matches_all), 'set_branch': gi.FunctionInfo(set_branch), 'set_branding': gi.FunctionInfo(set_branding), 'set_compulsory_for_desktop': gi.FunctionInfo(set_compulsory_for_desktop), 'set_context': gi.FunctionInfo(set_context), 'set_context_locale': gi.FunctionInfo(set_context_locale), 'set_data_id': gi.FunctionInfo(set_data_id), 'set_date_eol': gi.FunctionInfo(set_date_eol), 'set_description': gi.FunctionInfo(set_description), 'set_developer': gi.FunctionInfo(set_developer), 'set_id': gi.FunctionInfo(set_id), 'set_keywords': gi.FunctionInfo(set_keywords), 'set_kind': gi.FunctionInfo(set_kind), 'set_merge_kind': gi.FunctionInfo(set_merge_kind), 'set_metadata_license': gi.FunctionInfo(set_metadata_license), 'set_name': gi.FunctionInfo(set_name), 'set_name_variant_suffix': gi.FunctionInfo(set_name_variant_suffix), 'set_origin': gi.FunctionInfo(set_origin), 'set_pkgname': gi.FunctionInfo(set_pkgname), 'set_pkgnames': gi.FunctionInfo(set_pkgnames), 'set_priority': gi.FunctionInfo(set_priority), 'set_project_group': gi.FunctionInfo(set_project_group), 'set_project_license': gi.FunctionInfo(set_project_license), 'set_releases': gi.FunctionInfo(set_releases), 'set_scope': gi.FunctionInfo(set_scope), 'set_sort_score': gi.FunctionInfo(set_sort_score), 'set_source_pkgname': gi.FunctionInfo(set_source_pkgname), 'set_summary': gi.FunctionInfo(set_summary), 'sort_screenshots': gi.FunctionInfo(sort_screenshots), 'to_string': gi.FunctionInfo(to_string), 'to_xml_data': gi.FunctionInfo(to_xml_data), 'parent_instance': <property object at 0x000001ecec664b30>})"
    __gdoc__ = 'Object AsComponent\n\nProperties from AsComponent:\n  kind -> AsComponentKind: kind\n    kind\n  pkgnames -> GStrv: pkgnames\n    pkgnames\n  id -> gchararray: id\n    id\n  name -> gchararray: name\n    name\n  summary -> gchararray: summary\n    summary\n  description -> gchararray: description\n    description\n  keywords -> GStrv: keywords\n    keywords\n  icons -> gpointer: icons\n    icons\n  urls -> GHashTable: urls\n    urls\n  categories -> GPtrArray: categories\n    categories\n  project-license -> gchararray: project-license\n    project-license\n  project-group -> gchararray: project-group\n    project-group\n  screenshots -> GPtrArray: screenshots\n    screenshots\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AsComponent (3928800544)>'
    __info__ = ObjectInfo(Component)


