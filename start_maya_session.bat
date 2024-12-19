:: This is simple session launcher. This "method" can be developed with GUI and retrieve data from another party (shotgrid, kitsu, etc)

set mypath=%~dp0

SET PYTHONPATH=%PYTHONPATH%;%mypath%\repository;%mypath%\repository\BBF_testAssetDirect;%mypath%\repository\BBF_testExporter;
set MAYA_PLUG_IN_PATH=%MAYA_PLUG_IN_PATH%;%mypath%\repository;%mypath%\repository\BBF_testAssetDirect;%mypath%\repository\BBF_testExporter;

set AUTOLOAD_PLUGIN=%scriptRootPath%\repository\autoLoad.inf
set BLACKLIST_PLUGIN=%scriptRootPath%\repository\pluginBlacklist.inf

"C:\Program Files\Autodesk\Maya2022\bin\maya.exe"