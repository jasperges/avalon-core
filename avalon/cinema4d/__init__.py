"""Public API

Anything that isn't defined here is INTERNAL and unreliable for external use.

"""

from .pipeline import (
    install,
    uninstall,
    ls,
    Creator,
)

from .lib import (
    active_document,
    maintained_selection,
)

from .workio import (
    open_file,
    save_file,
    current_file,
    has_unsaved_changes,
    file_extensions,
    work_root,
)


__all__ = [
    "install",
    "uninstall",
    "ls",
    "Creator",

    "active_document",
    "maintained_selection",

    # Workfiles API
    "open_file",
    "save_file",
    "current_file",
    "has_unsaved_changes",
    "file_extensions",
    "work_root",
]

# Backwards API compatibility
open = open_file
save = save_file
