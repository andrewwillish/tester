:: This is simple session launcher. This "method" can be developed with GUI and retrieve data from another party (shotgrid, kitsu, etc)

set mypath=%~dp0

SET PYTHONPATH=%PYTHON%;%PYTHONPATH%;%mypath%3-4_animation\BBFtest\Content\Python\additionalPackages;
SET UE_PYTHONPATH=%UE_PYTHONPATH%;%mypath%3-4_animation\BBFtest\Content\Python\additionalPackages;

"C:\Program Files\Epic Games\UE_5.3\Engine\Binaries\Win64\UnrealEditor.exe" "%mypath%3-4_animation\BBFtest\BBFtest.uproject"