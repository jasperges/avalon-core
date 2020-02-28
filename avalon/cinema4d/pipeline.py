import sys

import c4d

from pyblish import api as pyblish

from .. import api
from . import lib

self = sys.modules[__name__]


def install():
    """Install Cinema4d-specific functionality of avalon-core.

    This function is called automatically on calling `api.install(maya)`.
    """

    _register_callbacks()
    _install_menu()
    pyblish.register_host("cinema4d")


def uninstall():
    """Uninstall Cinema4d-specific functionality of avalon-core.

    This function is called automatically on calling `api.uninstall()`.
    """

    _uninstall_menu()
    pyblish.deregister_host("cinema4d")


def _install_menu():
    """Install menu in host."""

    # At moment this is done in setup/cinema4d/avalon_c4d.pyp
    pass


def _uninstall_menu():
    """Un-install menu from host."""
    pass


def ls():
    """Yields containers from active Cinema4D scene.

    This is the host-equivalent of api.ls(), but instead of listing
    assets on disk, it lists assets already loaded in Cinema4D. Once loaded
    they are called 'containers'.

    Yields:
        dict: container
    """

    pass


def _register_callbacks():
    pass


class Creator(api.Creator):
    """Base class for creating instances in Cinema4d."""

    def process(self):
        nodes = list()

        with lib.undo_chunk():
            if (self.options or {}).get("useSelection"):
                doc = lib.active_document()
                nodes = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)

            instance = c4d.BaseObject(c4d.Oselection)
            instance.SetName(self.name)
            in_exclude_data = instance[c4d.SELECTIONOBJECT_LIST]
            for node in nodes:
                in_exclude_data.InsertObject(node, 1)
            doc.InsertObject(instance)
            lib.imprint(instance, self.data)
            c4d.EventAdd()

        return instance
