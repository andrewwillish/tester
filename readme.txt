BBF Test for Andrew Willis
===================================================================
Administered 	: 13th of December 2024
Deadline		: 20th of December 2024


== General Notes == 
Software version:
	-. Unreal Engine 5.3.2
	-. Maya 2022
	-. PySide6 (Provided)

The entire folder need to be set on M:/ drive. You can use the
given batch script to setup the temporary drive using setup_m_drive.bat
and remove it later using remove_m_drive.bat

The initial folder tree should look like this
---> M:/
------> 1_workflow
------> 2_asset
------> 3-4_animation
------> 5_programming
------> repository

Should you want to check the tools in action, please start Maya and
Unreal session using the provided batch command.

== 1. Workflow ==
Problem:
Draw a flowchart how Unreal Pipeline works (from Asset to FX).
Please describe every process in the flowchart.

Answer:
Flowchart collection and explanation located in folder 1_workflow

== 2. Asset ==
Problem:
Create a skeletal mesh so it can be animate in Unreal, you can choose
any rig system you prefer. You can use this geo: Cartoon Kid | Fab

Answer:
Rigged asset is located at

M:/2_asset/ASSET/CHAR/c_six/c_six.ma

I'm using other model since the link from the test is not working.
Model Credit to Onekro from sketchfab

== 3. Animation ==
Problem:
Create a tool to perform “Playblast” in Unreal Engine

Answer:
Tool source can be found at

C:\tester\3-4_animation\BBFtest\Content\Python\unreal_playblast.py

To try it, start Unreal using start_unreal_session.bat and the tools should
be seen in the "BBF Test Tools" menu in Unreal interface.


== 4. FX ==
Problem:
Create dust FX in Unreal using Niagara System. The dust should attached to
the shoes of the model in question #2.

Answer:
Dust FX using Niagara System has been setup in level named EPS000_SH000 

== 5. Programming ==
Problem:
a. Write code loop to print a pattern
b. Review the code

Answer:
a. M:/5_programming/programming_a.py
b. M:/5_programming/programming_b.py (changes on line 14)