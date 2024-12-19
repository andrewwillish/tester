# BBF Test - Playblast 
# Note:
# This tools require PySide6 to function. Add it on your PYTHONPATH or
# run the tools from the provided launcher.

import sys
import os
import subprocess
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import os
import unreal
loader = QUiLoader()

# determine path_root and path_dir 
if getattr(sys, 'frozen', False) is False:
    path_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
else:
    path_dir = sys.argv[0]
    path_dir = path_dir.replace('\\', '/')
    path_dir = path_dir[:path_dir.rfind('/')]

# declare base_path for unreal base path 
base_path = unreal.Paths.convert_relative_path_to_full(unreal.Paths.project_content_dir())

def pop_shotList(w):
    """
    Populate listWidget with level contained in SHOT output within project
    folder. Relative unreal path will be shown for debug purposes.
    Args:
        w: Loader from PyQt/PySide to load ui files (QtUiTools.QUiLoader)
    Returns:
        None
    """
    all_seq = []
    all_paths = unreal.EditorAssetLibrary.list_assets('/Game/SHOT', recursive=True, include_folder=True)
    for x in all_paths:
         if isinstance(unreal.EditorAssetLibrary.load_asset(x), unreal.World):
            all_seq.append(x)
    w.shot_lw.addItems(all_seq)
    return

def playblast_click(w):
    """
    Execute the "playblast" by opening the level, get sequencer inside the level,
    and then render the movie using MovieSceneCaptureSettings, and finally open the
    output directory.
    Args:
        w: Loader from PyQt/PySide to load ui files (QtUiTools.QUiLoader)
    Returns:
        None
    """
    # get selected level
    dir_sel = [x.text() for x in w.shot_lw.selectedItems()]

    if dir_sel == []:
        QtWidgets.QMessageBox.warning(None, 'BBF Test - Playblast', 'Please select a level from the list!')
        return

    lvl_obj = dir_sel[0]

    # open the level 
    if unreal.EditorAssetLibrary.does_asset_exist(lvl_obj):
        unreal.EditorLevelLibrary.load_level(lvl_obj)

    # get the sequencer 
    all_actors = unreal.EditorLevelLibrary.get_all_level_actors()

    # Filter for actors referencing Level Sequences
    sequencers = []
    for actor in all_actors:
        if isinstance(actor, unreal.LevelSequenceActor):
            sequence = actor.get_sequence()
            if sequence:
                sequencers.append(sequence.get_path_name())

    if not sequencers:
        QtWidgets.QMessageBox.warning(None, 'BBF Test - Playblast', 'Level has no sequencer!')
        return
    sequencers=sequencers[0]

    # setup the setting capture
    capture_settings = unreal.MovieSceneCaptureSettings()
    capture_settings.overwrite_existing = True
    capture_settings.allow_movement = False
    capture_settings.custom_frame_rate = unreal.FrameRate(numerator=24, denominator=1)
    capture_settings.resolution=unreal.CaptureResolution(res_x=1920, res_y=1080)

    # capture process 
    capture_level = unreal.AutomatedLevelSequenceCapture()
    capture_level.settings = capture_settings
    capture_level.level_sequence_asset = unreal.SoftObjectPath(sequencers)

    # get ouput path (note: unchanged due to error when capture directory changed to other dir)
    output_path = unreal.Paths.convert_relative_path_to_full(f'{capture_settings.output_directory.path}')

    try:
        unreal.SequencerTools.render_movie(capture_level, unreal.OnRenderMovieStopped())
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, 'BBF Test - Playblast', 'Error:\n'+str(e))
        return
    
    # open destination folder 
    subprocess.Popen(r'explorer "'+output_path.replace('/', '\\')+'"')
    return

# setup mainWindow from PySide
def mainwindow_setup(w):
    w.setWindowTitle("BBF Test - Unreal Playblast")
    pop_shotList(w)
    w.plb_btn.clicked.connect(lambda*args:playblast_click(w))


def about():
    unreal.EditorDialog.show_message("BBF Test - About Me", "by Andrew Willis\n0812-85670346\nandrewwillish@gmail.com\n\nHire me please!", unreal.AppMsgType.OK)
    return

def starter():
    # check the tools instances 
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    # start and load the apps using processEvents (it doesn't block unreal UI cycle)
    window = loader.load(f"{path_dir}/unreal_playblast_ui.ui", None)
    mainwindow_setup(window)
    window.show()
    app.processEvents()
# starter()