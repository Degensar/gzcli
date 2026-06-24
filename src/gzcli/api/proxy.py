"""API wrappers for the Proxy API category.

The two proxy endpoints are WebSocket upgrades that tunnel raw TCP traffic to a
challenge container instance. Each wrapper opens an authenticated WebSocket via
websocket-client and returns the live connection, which the caller reads from /
writes to (for example, to bridge it to a local socket).
"""

from websocket import WebSocket, create_connection
from gzcli.api._http import APIProfile


def _proxy_ws_url(profile: APIProfile, rel_path: str) -> str:
    """build the ws(s):// proxy url from the profile's http(s) base url"""
    base = profile.url
    if base.startswith("https://"):
        base = "wss://" + base[len("https://") :]
    elif base.startswith("http://"):
        base = "ws://" + base[len("http://") :]
    return base + rel_path


def connect_to_instance(profile: APIProfile, instance_id: str) -> WebSocket:
    """
    WebSocket wrapper for `/api/proxy/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/proxy/GET/api/proxy/{id}

    Opens an authenticated WebSocket that tunnels traffic to the given container
    instance and returns the live connection.
    """
    return create_connection(
        _proxy_ws_url(profile, f"/api/proxy/{instance_id}"),
        cookie=f"GZCTF_Token={profile.token}",
    )


def connect_without_instance(profile: APIProfile, instance_id: str) -> WebSocket:
    """
    WebSocket wrapper for `/api/proxy/noinst/{id}`
    docs: https://gzctf.gzti.me/scalar.html#tag/proxy/GET/api/proxy/noinst/{id}

    Opens an authenticated WebSocket to the proxy without provisioning an
    instance and returns the live connection.
    """
    return create_connection(
        _proxy_ws_url(profile, f"/api/proxy/noinst/{instance_id}"),
        cookie=f"GZCTF_Token={profile.token}",
    )
