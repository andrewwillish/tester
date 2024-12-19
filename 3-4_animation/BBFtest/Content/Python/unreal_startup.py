import unreal
import unreal_playblast

# Get the main ToolMenu of Unreal
menus = unreal.ToolMenus.get()
main_menu = menus.find_menu('LevelEditor.MainMenu')

# Create custom ToolMenu
my_menu = main_menu.add_sub_menu(
    owner=main_menu.get_name(),
    name='bbf_tools_menu',
    label='BBF Test Tools',
    section_name=''
)

# ToolMenuSection for ToolMenuEntry
my_menu.add_section(section_name='animation', label='Animation')
my_menu.add_section(section_name='others', label='Others')

# ToolMenuEntry
entry_a = unreal.ToolMenuEntry(type=unreal.MultiBlockType.MENU_ENTRY)
entry_a.set_label("Playblast Tools")
entry_a.set_string_command(
    type=unreal.ToolMenuStringCommandType.PYTHON,
    custom_type=unreal.Name(''),
    string='import unreal_playblast\nunreal_playblast.starter()'
)
my_menu.add_menu_entry(section_name='animation', args=entry_a)

# ToolMenuSection for a sub ToolMenu
my_menu.add_section(section_name='others', label='Others')

entry_b = unreal.ToolMenuEntry(type=unreal.MultiBlockType.MENU_ENTRY)
entry_b.set_label("About")
entry_b.set_string_command(
    type=unreal.ToolMenuStringCommandType.PYTHON,
    custom_type=unreal.Name(''),
    string='import unreal_playblast\nunreal_playblast.about()'
)
my_menu.add_menu_entry(section_name='others', args=entry_b)


menus.refresh_all_widgets()