"""Command-line interface for NetAudit."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from netaudit import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level argument parser."""
    parser = argparse.ArgumentParser(prog="netaudit", description="Asynchronous network inventory and exposure audit for networks you are authorized to assess.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point. Returns a process exit code."""
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0
