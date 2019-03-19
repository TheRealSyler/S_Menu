import bpy

from . ui.pie_menus import (
    #get_prefs,
    SM_PIE_Add,
    SM_PIE_Add_Call, 
    SM_PIE_Add_Node,
    SM_PIE_Add_Node_Call,
    SM_Add_Texture_Node,
    SM_Add_Shader_Node,
    SM_PIE_Q_Menu,
    SM_PIE_Q_Menu_Call,
    SM_PIE_A_OM,
    SM_PIE_A_OM_Call,
    SM_PIE_Q_Node,
    SM_PIE_Q_Node_Call,
)
from . operators.comp_node_adjust_view_modal import SM_Modal_adjust_view

from . prefs import SM_Prefs , add_hotkey, remove_hotkey
from . ui.get_icon import register_icons, unregister_icons
from . ui.add_pose_copy_buttons import add_pose_copy_buttons

bl_info = {
    "name" : "S.Menu",
    "author" : "Syler",
    "version": (0, 0, 0, 9),
    "description": "Adds Pie Menus",
    "blender" : (2, 80, 0),
    "category" : "3D view"
}



classes = [
    SM_PIE_Add,
    SM_PIE_Add_Call,
    SM_PIE_Add_Node,
    SM_PIE_Add_Node_Call,
    SM_Add_Texture_Node,
    SM_Add_Shader_Node,
    SM_PIE_Q_Menu,
    SM_PIE_Q_Menu_Call,
    SM_PIE_A_OM,
    SM_PIE_A_OM_Call,
    SM_PIE_Q_Node,
    SM_PIE_Q_Node_Call,
    SM_Prefs,
    SM_Modal_adjust_view,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    #+ add hotkey
    add_hotkey()
    # ------------------------------------------------------------------------------------------------------------
    # Append Register stuff
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.VIEW3D_MT_editor_menus.append(add_pose_copy_buttons)

    # ------------------------------------------------------------------------------------------------------------
    # Icons Register stuff
    # ------------------------------------------------------------------------------------------------------------
    register_icons(__file__)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    #+ remove hotkey
    remove_hotkey()

    # ------------------------------------------------------------------------------------------------------------
    # Append Unregister stuff
    # ------------------------------------------------------------------------------------------------------------

    bpy.types.VIEW3D_MT_editor_menus.remove(add_pose_copy_buttons)

    # ------------------------------------------------------------------------------------------------------------
    # Icons Unregister stuff
    # ------------------------------------------------------------------------------------------------------------
    unregister_icons()

    
if __name__ == "__main__":
    register()
