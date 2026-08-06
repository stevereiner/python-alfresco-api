"""Runtime compatibility shims for Alfresco responses that deviate from the OpenAPI spec.

Alfresco marks ``UserInfo.displayName`` as *required*, but omits it for JIT / OAuth2 service-account
users (e.g. ``service-account-*`` produced by the client-credentials grant). That makes the generated
``UserInfo.from_dict`` raise ``KeyError('displayName')`` while parsing ``createdByUser`` /
``modifiedByUser`` / ``owner`` on node responses.

This shim defaults ``displayName`` to ``id`` when it is absent, so parsing never crashes. It lives
outside ``raw_clients/`` so it survives client re-generation.

Scope (verified across all 7 generated raw clients): the ``UserInfo`` model — which is what
createdBy/modifiedBy/owner deserialize to — exists **only** in the core and search clients; the other
five (auth, discovery, model, search_sql, workflow) have no required-``displayName`` models. Core's
group models (``Group`` / ``GroupMember`` / ``GroupBodyCreate`` / ``GroupBodyUpdate``) also mark
``displayName`` required, but groups always carry a display name and those models have *other* required
fields (e.g. ``Group.isRoot``), so they are not the JIT/service-account case and are left alone.
"""

from importlib import import_module

# UserInfo covers every user reference (createdByUser / modifiedByUser / owner), in the two clients
# that define it.
_MODELS = (
    ("python_alfresco_api.raw_clients.alfresco_core_client.core_client.models.user_info", "UserInfo"),
    ("python_alfresco_api.raw_clients.alfresco_search_client.search_client.models.user_info", "UserInfo"),
)


def _patch_from_dict(cls) -> None:
    if getattr(cls, "_display_name_shim_installed", False):
        return
    _orig_from_dict = cls.from_dict  # bound classmethod

    def _from_dict(src_dict, _orig=_orig_from_dict):
        d = dict(src_dict)
        if "displayName" not in d and "id" in d:
            # Alfresco omitted the (spec-required) display name; fall back to the id.
            d["displayName"] = d["id"]
        return _orig(d)

    cls.from_dict = staticmethod(_from_dict)
    cls._display_name_shim_installed = True


def install_shims() -> None:
    """Patch ``UserInfo.from_dict`` in the raw clients to tolerate a missing ``displayName``.

    Idempotent — safe to call more than once.
    """
    for mod_path, cls_name in _MODELS:
        try:
            _patch_from_dict(getattr(import_module(mod_path), cls_name))
        except Exception:
            # Model not present in this build/layout — skip quietly.
            continue
