"""Insert menu in Cinema4D.

For every menu item you need a plug-in ID. At the moment I quickly registered
id's for the current Avalon tools.

Keep this table here for reference.

Associated Label            Plugin ID   Creation Date
===========================================================
avalontoolsworkfiles        1054572     2020-02-28 14:55:41
avalontoolssceneinventory   1054571     2020-02-28 14:55:30
avalontoolspublish          1054570     2020-02-28 14:55:17
avalontoolsprojectmanager   1054569     2020-02-28 14:55:04
avalontoolsloader           1054568     2020-02-28 14:54:50
avalontoolscreator          1054567     2020-02-28 14:53:55

"""

AVALONTOOLSWORKFILES_ID = 1054572
AVALONTOOLSSCENEINVENTORY_ID = 1054571
AVALONTOOLSPUBLISH_ID = 1054570
AVALONTOOLSPROJECTMANAGER_ID = 1054569
AVALONTOOLSLOADER_ID = 1054568
AVALONTOOLSCREATOR_ID = 1054567

import c4d
from c4d import gui

import avalon.api
import avalon.cinema4d
from avalon.vendor.Qt import QtWidgets


class ShowCreator(c4d.plugins.CommandData):
    id = AVALONTOOLSCREATOR_ID
    label = "Create..."
    help = "Show Avalon Creator"
    icon = None

    def Execute(self, doc):
        from avalon.tools import creator as tool
        tool.show()
        return True


class ShowLoader(c4d.plugins.CommandData):
    id = AVALONTOOLSLOADER_ID
    label = "Loader..."
    help = "Show Avalon Loader"
    icon = None

    def Execute(self, doc):
        from avalon.tools import loader as tool
        tool.show()
        return True


class ShowSceneInventory(c4d.plugins.CommandData):
    id = AVALONTOOLSSCENEINVENTORY_ID
    label = "Manage..."
    help = "Show Avalon Loader"
    icon = None

    def Execute(self, doc):
        from avalon.tools import sceneinventory as tool
        tool.show()
        return True


class ShowPublish(c4d.plugins.CommandData):
    id = AVALONTOOLSPUBLISH_ID
    label = "Publish..."
    help = "Show Avalon Publish"
    icon = None

    def Execute(self, doc):
        from avalon.tools import publish
        publish.show()
        return True


class ShowWorkFiles(c4d.plugins.CommandData):
    id = AVALONTOOLSWORKFILES_ID
    label = "Work Files..."
    help = "Show Avalon Work Files"
    icon = None

    def Execute(self, doc):
        from avalon.tools import workfiles as tool
        tool.show()
        return True


def _install_menu():

    main_menu = gui.GetMenuResource('M_EDITOR')

    # Create Avalon menu
    menu = c4d.BaseContainer()
    menu.InsData(c4d.MENURESOURCE_SUBTITLE, "Avalon")

    # Add commands
    menu.InsData(
        c4d.MENURESOURCE_COMMAND,
        "PLUGIN_CMD_{}".format(ShowCreator.id),
    )
    menu.InsData(
        c4d.MENURESOURCE_COMMAND,
        "PLUGIN_CMD_{}".format(ShowLoader.id),
    )
    menu.InsData(
        c4d.MENURESOURCE_COMMAND,
        "PLUGIN_CMD_{}".format(ShowPublish.id),
    )
    menu.InsData(
        c4d.MENURESOURCE_COMMAND,
        "PLUGIN_CMD_{}".format(ShowSceneInventory.id),
    )
    menu.InsData(c4d.MENURESOURCE_SEPERATOR, True)
    menu.InsData(
        c4d.MENURESOURCE_COMMAND,
        "PLUGIN_CMD_{}".format(ShowWorkFiles.id),
    )

    # Add Avalon menu to main menu
    main_menu.InsData(c4d.MENURESOURCE_STRING, menu)

    # Refresh menu bar
    gui.UpdateMenus()


def _register_commands():
    """Register C4D commands.

    This is required to make Menu Item entries

    """

    for command in [
            ShowCreator,
            ShowLoader,
            ShowSceneInventory,
            ShowPublish,
            ShowWorkFiles,
    ]:
        c4d.plugins.RegisterCommandPlugin(
            id=command.id,
            str=command.label,
            info=0,
            icon=command.icon,
            help=command.help,
            dat=command(),
        )


def main():

    # Initialize a QApplication instance so that whenever we run
    # an Avalon tool it assumes the QApplication is already running.
    # This way QApplication.exec_() will never be triggered which
    # is somehow magically how Qt works in Cinema4D
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])
    app.aboutToQuit.connect(app.deleteLater)  # ensure cleanup with C4D

    # Install avalon itself
    avalon.api.install(avalon.cinema4d)

    _register_commands()


def PluginMessage(id, data):

    if id == c4d.C4DPL_BUILDMENU:
        _install_menu()

    return True


# Execute main()
if __name__ == '__main__':
    main()

#  vim: set ft=python ts=4 sw=4 tw=0 et :
