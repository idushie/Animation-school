import maya.api.OpenMaya as om

import maya.cmds as cmds


def maya_useNewAPI():
    """
    The presence of this function tells Maya that the plugin produces, and
    expects to be passed, objects created using the Maya Python API 2.0.
    """
    pass

def initializePlugin(plugin):
    """
    Entry point for a plugin. It is called once -- immediately after the plugin is loaded.
    This function registers all of the commands, nodes, contexts, etc... associated with the plugin.

    It is required by all plugins.

    :param plugin: MObject used to register the plugin using an MFnPlugin function set
    """
    vendor = "Oleg Usov"
    version = "1.0.0"

    om.MFnPlugin(plugin, vendor, version)

def uninitializePlugin(plugin):
    """
    Exit point for a plugin. It is called once -- when the plugin is unloaded.
    This function de-registers everything that was registered in the initializePlugin function.

    It is required by all plugins.

    :param plugin: MObject used to de-register the plugin using an MFnPlugin function set
    """
    pass


if __name__ == "__main__":
    """
    For Development Only

    Specialized code that can be executed through the script editor to speed up the development process.

    For example: scene cleanup, reloading the plugin, loading a test scene
    """

    # Any code required before unloading the plug-in (e.g. creating a new scene)


    # Reload the plugin
    plugin_name = "empty_plugin.py"
    cmds.evalDeferred('if cmds.pluginInfo("{0}", q=True, loaded=True): cmds.unloadPlugin("{0}")'.format(plugin_name))
    cmds.evalDeferred('if not cmds.pluginInfo("{0}", q=True, loaded=True): cmds.loadPlugin("{0}")'.format(plugin_name))


    # Any setup code to help speed up testing (e.g. loading a test scene)
