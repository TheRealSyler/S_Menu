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
    SM_PIE_A_NODE,
    SM_PIE_A_NODE_Call,
    SM_PIE_Tab_Menu,
    SM_PIE_Tab_Menu_Call,
    SM_PIE_M4_Menu,
    SM_PIE_M4_Menu_Call,
)
from . ui.mesh_history_panel import SM_mesh_history_panel
from . operators.comp_adjust_view import SM_Modal_adjust_view
from . operators.mesh_history_operator import (
    SM_mesh_history_Props, 
    SM_mesh_history_make_Instance,
    SM_mesh_history_switch_to_edit_mode,
    on_frame_change,
    #SM_MH_Auto_Instance, later?
    SM_mesh_history_delete_instances,
    SM_mesh_history_delete_current_instance,
    SM_MH_Instances,
)
from . prefs import SM_Prefs , add_hotkey, remove_hotkey
from . ui.get_icon import register_icons, unregister_icons
from . ui.add_pose_copy_buttons import add_pose_copy_buttons

bl_info = {
    "name" : "S.Menu",
    "author" : "Syler",
    "version": (0, 0, 1, 2),
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
    SM_PIE_A_NODE,
    SM_PIE_A_NODE_Call,
    SM_Prefs,
    SM_Modal_adjust_view,
    SM_mesh_history_panel,
    SM_mesh_history_Props,
    SM_mesh_history_make_Instance,
    SM_mesh_history_switch_to_edit_mode,
    SM_PIE_Tab_Menu,
    SM_PIE_Tab_Menu_Call,
    SM_mesh_history_delete_instances,
    SM_mesh_history_delete_current_instance,
    SM_PIE_M4_Menu,
    SM_PIE_M4_Menu_Call,
    SM_MH_Instances,
]

    

def register():
    for c in classes:
        bpy.utils.register_class(c)
    #+ add hotkey
    add_hotkey()
    # ------------------------------------------------------------------------------------------------------------
    # Register prop group
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.Object.SM_MH_Instances = bpy.props.CollectionProperty(type=SM_MH_Instances)
    # ------------------------------------------------------------------------------------------------------------
    # Append Register stuff
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.VIEW3D_MT_editor_menus.append(add_pose_copy_buttons)
    # add on_frame_change handler to blender
    try:
        #bpy.app.handlers.frame_change_pre.append(on_frame_change) 
        #bpy.app.timers.register(SM_MH_Auto_Instance) later?
        print ("add Handler")
    except:
        pass

    # ------------------------------------------------------------------------------------------------------------
    # Icons Register stuff
    # ------------------------------------------------------------------------------------------------------------
    register_icons(__file__)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    #+ remove hotkey
    remove_hotkey()
    # remove on_frame_change handler from blender
    try:
        bpy.app.handlers.frame_change_pre.remove(on_frame_change) 
        #bpy.app.timers.unregister(SM_MH_Auto_Instance) later?
        print ("remove Handler")
    except:
        pass
    # ------------------------------------------------------------------------------------------------------------
    # delete prop group
    # ------------------------------------------------------------------------------------------------------------
    del(bpy.types.Object.SM_MH_Instances)
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
