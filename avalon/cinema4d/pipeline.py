import importlib
import sys

from pyblish import api as pyblish

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
    pass


def _uninstall_menu():
    pass


def ls():
    """Yields containers from active Cinema4d scene

    This is the host-equivalent of api.ls(), but instead of listing
    assets on disk, it lists assets already loaded in Cinema4d; once loaded
    they are called 'containers'

    Yields:
        dict: container

    """
    pass


def _register_callbacks():
    pass
