import c4d
from c4d import gui

        
class ShowCreator(c4d.plugins.CommandData):
    id = 999121031
    label = "Create.."
    help = "Show Avalon Creator"
    icon = None

    def Execute(self, doc):
        from avalon.tools import creator as tool
        tool.show()
        return True


class ShowLoader(c4d.plugins.CommandData):
    id = 999121032
    label = "Loader.."
    help = "Show Avalon Loader"
    icon = None

    def Execute(self, doc):
        from avalon.tools import loader as tool
        tool.show()
        return True


class ShowSceneInventory(c4d.plugins.CommandData):
    id = 999121033
    label = "Manage.."
    help = "Show Avalon Loader"
    icon = None

    def Execute(self, doc):
        from avalon.tools import sceneinventory as tool
        tool.show()
        return True


class ShowPublish(c4d.plugins.CommandData):
    id = 999121034
    label = "Publish.."
    help = "Show Avalon Publish"
    icon = None

    def Execute(self, doc):
        from avalon.tools import publish
        publish.show()
        return True


class ShowWorkFiles(c4d.plugins.CommandData):
    id = 999121035
    label = "Work Files.."
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
    menu.InsData(c4d.MENURESOURCE_COMMAND,
                 "PLUGIN_CMD_%s" % ShowCreator.id)
    menu.InsData(c4d.MENURESOURCE_COMMAND,
                 "PLUGIN_CMD_%s" % ShowLoader.id)
    menu.InsData(c4d.MENURESOURCE_COMMAND,
                 "PLUGIN_CMD_%s" % ShowPublish.id)
    menu.InsData(c4d.MENURESOURCE_COMMAND,
                 "PLUGIN_CMD_%s" % ShowSceneInventory.id)
    menu.InsData(c4d.MENURESOURCE_SEPERATOR, True)
    menu.InsData(c4d.MENURESOURCE_COMMAND,
                 "PLUGIN_CMD_%s" % ShowWorkFiles.id)

    # Add Avalon menu to main menu
    main_menu.InsData(c4d.MENURESOURCE_STRING, menu)
    
    # Refresh menu bar
    gui.UpdateMenus()
    
    
def _register_commands():
    """Register C4D commands.

    This is required to make Menu Item entries
    
    """
    
    for command in [ShowCreator,
                    ShowLoader,
                    ShowSceneInventory,
                    ShowPublish,
                    ShowWorkFiles]:
        c4d.plugins.RegisterCommandPlugin(id=command.id,
                                          str=command.label,
                                          info=0,
                                          icon=command.icon,
                                          help=command.help,
                                          dat=command())


def main():
    
    from avalon.vendor.Qt import QtWidgets
    
    # Initialize a QApplication instance so that whenever we run
    # an Avalon tool it assumes the QApplication is already running.
    # This way QApplication.exec_() will never be triggered which
    # is somehow magically how Qt works in Cinema4D
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])
    app.aboutToQuit.connect(app.deleteLater)    # ensure cleanup with C4D
    
    # Install avalon itself
    import avalon.api
    import avalon.cinema4d
    avalon.api.install(avalon.cinema4d)

    _register_commands()

    
def PluginMessage(id, data):

    if id == c4d.C4DPL_BUILDMENU:
        _install_menu()
        
    return True
    
    
# Execute main()
if __name__ == '__main__':
    main()
