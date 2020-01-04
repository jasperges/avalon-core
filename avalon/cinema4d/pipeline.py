import sys
import importlib

from pyblish import api as pyblish


self = sys.modules[__name__]


def install(config):
    """Install Maya-specific functionality of avalon-core.

    This function is called automatically on calling `api.install(maya)`.

    """

    _register_callbacks()
    _install_menu()

    pyblish.register_host("cinema4d")
    
    config = find_host_config(config)
    if config and hasattr(config, "install"):
        config.install()


def find_host_config(config):
    module = config.__name__ + ".cinema4d"
    try:
        config = importlib.import_module(module)
    except ImportError as exc:
        if str(exc) != "No module name {}".format(module):
            print(exc)
        config = None

    return config


def uninstall(config):
    """Uninstall Maya-specific functionality of avalon-core.

    This function is called automatically on calling `api.uninstall()`.

    """
    config = find_host_config(config)
    if config and hasattr(config, "uninstall"):
        config.uninstall()

    _uninstall_menu()

    pyblish.deregister_host("cinema4d")

    
def _install_menu():
    pass


def _uninstall_menu():
    pass


def ls():
    """Yields containers from active Maya scene

    This is the host-equivalent of api.ls(), but instead of listing
    assets on disk, it lists assets already loaded in Maya; once loaded
    they are called 'containers'

    Yields:
        dict: container

    """
    pass


def _register_callbacks():
    pass

