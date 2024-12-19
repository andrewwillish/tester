import maya.cmds as cmds

queried_shot = []
class mainUI:
    def __init__(self):
        # delete previously opened windows
        if cmds.window('bbf_assetDirect', exists=True):cmds.deleteUI('bbf_assetDirect', window=True)

        # create main window
        win=cmds.window(t='BBF Test - Asset Direct', s=False,mxb=False,mnb=True)
        cmds.renameUI(win,'bbf_assetDirect')

        cmds.columnLayout('cmas', adj=1, w=300)
        cmds.button(l='OPEN c_six asset', c=lambda*args:cmds.file('M:/2_asset/ASSET/CHAR/c_six/c_six.ma', o=1, f=1))
        cmds.button(l='OPEN EPS000_SH000 shot', c=lambda*args:cmds.file('M:/2_asset/SHOTS/EPS000_SH000.ma', o=1, f=1))

        cmds.separator(p='cmas')
        cmds.text('Andrew Willis @2024 for BBF Test', p='cmas', ww=1, fn='obliqueLabelFont', h=10)

        cmds.showWindow()
        return
    
# mainUI()