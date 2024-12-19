import pymel.core as pm
import maya.cmds as cmds
import maya.utils as utils
import maya.mel as mel
import maya.OpenMaya as om
import os
import imp

#Determining root path
__WINROOT__ = os.environ['ProgramFiles'][:2]+'/'

#force to create workspace if possible
if not os.path.isdir(__WINROOT__+'/workspace'): os.makedirs(__WINROOT__+'/workspace')

#callback collections
def beforeSaveCallbackFun(*args):
    global currentLayerVar,daStatLis,allPanelLis
    currentLayerVar=cmds.editRenderLayerGlobals(q=True, crl=True)
    cmds.editRenderLayerGlobals(crl='defaultRenderLayer')
    allPanelLis=cmds.getPanel(type='modelPanel')
    daStatLis=[]
    for chk in allPanelLis:
        daStatLis.append(cmds.modelEditor(chk,q=True,da=True))
        cmds.modelEditor(chk,e=True,da='boundingBox')
    return

def afterOpenCallbackFun(*args):
    unkPlg = cmds.unknownPlugin(q=1,l=1)
    if unkPlg is not None:
        for item in unkPlg :
            cmds.unknownPlugin(item, r=1)

    cmds.delete(cmds.ls(type='unknown'))
    return

def afterSaveCallbackFun(*args):
    global currentLayerVar,daStatLis,allPanelLis
    cmds.editRenderLayerGlobals(crl=currentLayerVar)
    cnt=0
    for chk in allPanelLis:cmds.modelEditor(chk,e=True,da=daStatLis[cnt]);cnt+=1
    return
    
def afterNewCallbackFun(*args):
    # enforce FPS
    try:
        cmds.currentUnit(time=os.environ['FPS'])
    except:
        pass
    return    

# startup funciton. Entry point of the entire system
def startup(*args):
    # create shortcut here. change into more sophisticated technique with configuration ITF
    # # launch playblast
    # pm.nameCommand( 'registrarPlayblastSEA_coreHK', ann='registrarPlayblastSEA_coreHK', c='python("import registrarPlayblastSEA_core;registrarPlayblastSEA_core.mainUI()");')
    # pm.hotkey( keyShortcut='F10', ctrlModifier=True, altModifier=True, name='registrarPlayblastSEA_coreHK') 

    
    #get main window name for menu building
    mainWindow = mel.eval('$temp1=$gMainWindow')

    #build menu here
    #cmds.menu('assistMainMenus',l='test', tearOff=1, p=mainWindow)
    #cmds.menuItem('refreshMenus',l='test test',p='assistMainMenus')

    #start callback function to trigger safety system
    # om.MSceneMessage.addCallback(om.MSceneMessage.kBeforeSave,beforeSaveCallbackFun)
    # om.MSceneMessage.addCallback(om.MSceneMessage.kAfterSave,afterSaveCallbackFun)
    # om.MSceneMessage.addCallback(om.MSceneMessage.kAfterOpen,afterOpenCallbackFun)
    # om.MSceneMessage.addCallback(om.MSceneMessage.kAfterNew,afterNewCallbackFun)

    # automatically start the plugin
    opn = open(os.environ['AUTOLOAD_PLUGIN'].replace('\\','/'), 'r')
    plgData = opn.readlines()
    opn.close()
    for plg in plgData:
        try:
            plg = plg.replace('\r', '')
            plg = plg.replace('\n', '')
            cmds.loadPlugin(plg)
        except:
            pass

    opn = open(os.environ['BLACKLIST_PLUGIN'].replace('\\','/'), 'r')
    plgData = opn.readlines()
    opn.close()
    for plg in plgData:
        try:
            plg = plg.replace('\r', '')
            plg = plg.replace('\n', '')
            cmds.unloadPlugin(plg)     
        except:
            pass

    # Automatically create a list
#     tmp = """
# import maya.cmds as cmds
# import maya.mel as mel
# import imp

# gMainWindow = mel.eval('$temp1=$gMainWindow')
# mainzmenu=cmds.menu(tearOff=True,l='Extra Tools',p=gMainWindow)
# """
#     for path in [x for x in os.environ['EXT_REPO'].split(';') if x != '']:
#         if os.path.isdir(path):
#             cont = [x for x in os.listdir(path) if x.endswith('.py')]
#             for scrip in cont:
#                 if scrip.endswith('.py'):
#                     nme = scrip.replace('.py', '')
#                     tmp += \
# """
# cmds.menuItem(parent=mainzmenu, l='"""+nme+"""', c=lambda*args:imp.load_source('"""+nme+"""','"""+path+'/'+scrip+"""'))
# """

    #opn = open('C:/workspace/tmp.py', 'w')
    #opn.write(tmp)
    #opn.close()

    #imp.load_source('ext_root', 'C:/workspace/tmp.py')
    
    # turn off hypershade texture load
    # mel.eval('refreshPauseButtonCmd 0')

    # set fit camera to 1.0
    # mel.eval('optionVar -fv "defaultFitFactor" 1;')

    # turn on unlimited undo
    cmds.undoInfo(st=1, infinity=1)

    # turn on autosave
    # cmds.autoSave(en=1, prm=0)
    # trgt = 'C:/mdnWorkspace/autosave'
    # if not os.path.isdir(trgt):
    #     os.makedirs(trgt)
    # cmds.autoSave(fol=trgt, dst=1)
    # cmds.confirmDialog(message='HEJJ!!')
    return

#initialize startup sequence
utils.executeDeferred(startup)
