"""Error handling for gzcli"""

import traceback
import click
import requests
from pydantic import ValidationError
from functools import wraps
from gzcli.cli.config import ERROR_LOG
from gzcli.cli.output import error


def format_http_error(exc: requests.HTTPError) -> str:
    """turn an HTTP error from the server into a readable message"""
    resp = exc.response
    if resp is None:
        return str(exc)
    try:
        body = resp.json()
    except ValueError:
        body = None
    if isinstance(body, dict) and body.get("title"):
        return f"{resp.status_code} {body['title']}"
    return f"{resp.status_code} {resp.reason}"


def format_validation_error(exc: ValidationError) -> str:
    """turn a pydantic validation error into a readable, semicolon-joined message"""
    return "; ".join(err["msg"] for err in exc.errors())


def error_wrap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except click.ClickException:
            raise
        except requests.HTTPError as exc:
            raise click.ClickException(format_http_error(exc))
        except Exception:
            ERROR_LOG.write_text(traceback.format_exc())
            error(f"an error occured, error log written to {ERROR_LOG}")

    return wrapper
