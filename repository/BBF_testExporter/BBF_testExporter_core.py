import maya.cmds as cmds
import maya.mel as mel
import os

prefix = 'M:/3-4_animation/BBFtest/Content'

class mainUI:
    def __init__(self):
        # delete previously opened windows
        if cmds.window('bbf_export', exists=True):cmds.deleteUI('bbf_export', window=True)

        # create main window
        win=cmds.window(t='BBF Test - Asset Export', s=False,mxb=False,mnb=True)
        cmds.renameUI(win,'bbf_export')

        cmds.columnLayout('cmas', adj=1, w=300)
        cmds.button(l='Export Asset', c=lambda*args:self.exportAsset())
        cmds.button(l='Export Shot')

        cmds.separator(p='cmas')
        cmds.text('Andrew Willis @2024 for BBF Test', p='cmas', ww=1, fn='obliqueLabelFont', h=10)

        cmds.showWindow()
        return
        
    def exportAsset(self):
        currentFile = cmds.file(q=True, sn=True)
        if currentFile == '':
            cmds.confirmDialog(title='BBF Test - Exporter', message='Ensure you open an asset file such as c_six, p_prop, or s_floor')
            return
        filename = os.path.basename(currentFile)
        
        assetLib = {'c': 'CHAR', 'p':'PROPS', 's':'SETS'}
        
        filePath = f'{prefix}/ASSET/{assetLib[filename[0]]}/{filename[:filename.rfind(".")]}'
        if not os.path.isdir(filePath):
            os.makedirs(filePath)
        filePathName = filePath + '/' + filename.replace('.ma', '.fbx')
        filePathName = f'{filePath}/{filename.replace(".ma", ".fbx")}'
        
        mel.eval('file -force -options "" -type "FBX export" -pr -ea "'+filePathName+'";')
        cmds.confirmDialog(message='Export Done!')
        return
   
# mainUI()