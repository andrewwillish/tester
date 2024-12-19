import sys
import maya.cmds as cmds
import maya.mel as mel
import imp
import os
import BBF_testExporter_core

kPluginCmdName = "stepSnapGenCore"

# Initialize the script plug-in
def initializePlugin(mobject):
    # generate menu
    mainWindow = mel.eval('$temp1=$gMainWindow')

    if not cmds.menu('toolsMainMenu', exists=1):
        cmds.menu('toolsMainMenu',l='BBF Test Tools', tearOff=1, p=mainWindow)
    cmds.menuItem('ae_GEN_core',l='Asset Exporter',p='toolsMainMenu', c=lambda*args:BBF_testExporter_core.mainUI())       
    return

# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    # delete this plugin menu first
    cmds.deleteUI('ae_GEN_core')

    # check if the root menu has other menu or not. If not then delete it
    if cmds.menu('toolsMainMenu', q=1, ni=1) == 0:
        cmds.deleteUI('toolsMainMenu')
    return