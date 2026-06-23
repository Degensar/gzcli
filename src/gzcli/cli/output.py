"""Helpers for styled (coloured) terminal output.

Colours are emitted with click, which automatically strips the ANSI codes
when the output is not a terminal (e.g. when piped to a file), so the plain
text stays clean.
"""

import click


def success(message: str) -> None:
    """print a success message in green, prefixed with [+]."""
    click.secho(f"[+] {message}", fg="green")


def info(message: str) -> None:
    """print an informational message in cyan, prefixed with [*]."""
    click.secho(f"[*] {message}", fg="cyan")


def warn(message: str) -> None:
    """print a warning message in yellow, prefixed with [!]."""
    click.secho(f"[!] {message}", fg="yellow")


def error(message: str) -> None:
    """print an error message in red, prefixed with [-], to stderr."""
    click.secho(f"[-] {message}", fg="red", err=True)
