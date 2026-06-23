"""API wrappers for the Proxy API category.

The two proxy endpoints (`/api/proxy/{id}` and `/api/proxy/noinst/{id}`) are
WebSocket upgrades that tunnel traffic to a container instance, not plain REST
calls, so they are intentionally not wrapped here -- a WebSocket client would be
required to use them.

docs: https://gzctf.gzti.me/scalar.html#tag/proxy
"""
