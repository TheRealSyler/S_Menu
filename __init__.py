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
    SM_PIE_W_Menu,
    SM_PIE_W_Menu_Call,
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
from . ui.properties_popup_panel import SM_Properties_Popup
from . ui.render_settings_popup import (
    SM_Render_Settings_Popup, 
    SM_Render_Settings_Panel,
    Init_Render_Settings_Props,
    Del_Render_Settings_Props,
)
from . operators.change_area_type import SM_change_area_type, SM_change_area_type_modal
from . ui.change_workspaces_pie import SM_PIE_Workspaces_Menu, SM_PIE_Workspaces_Menu_Call, SM_change_workspace

bl_info = {
    "name" : "S.Menu",
    "author" : "Syler",
    "version": (0, 0, 1, 5),
    "description": "Adds Pie Menus",
    "blender" : (2, 80, 0),
    "category" : "3D view"
}


classes = [
    #? PIE Menus and pie menu calls
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
    SM_PIE_W_Menu,
    SM_PIE_W_Menu_Call,
    #------
    SM_PIE_Workspaces_Menu, 
    SM_PIE_Workspaces_Menu_Call,
    #? Prefs
    SM_Prefs,
    #+ Mesh Hisrtory
    SM_mesh_history_panel,
    SM_mesh_history_Props,
    SM_mesh_history_make_Instance,
    SM_mesh_history_switch_to_edit_mode,
    SM_mesh_history_delete_instances,
    SM_mesh_history_delete_current_instance, 
    SM_MH_Instances,
    #? Popup Panels
    SM_Properties_Popup,
    # Render Settings
    SM_Render_Settings_Popup,
    SM_Render_Settings_Panel,
    #§ Operators
    SM_change_area_type,
    SM_change_workspace,
    #§ Modals
    SM_Modal_adjust_view,
    SM_change_area_type_modal,
]



def register():
    for c in classes:
        bpy.utils.register_class(c)
    #+ add hotkey
    add_hotkey()
    # ------------------------------------------------------------------------------------------------------------
    #§ Register prop group
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.Object.SM_MH_Instances = bpy.props.CollectionProperty(type=SM_MH_Instances)
    Init_Render_Settings_Props()
    # ------------------------------------------------------------------------------------------------------------
    #+ Append Register stuff
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.VIEW3D_MT_editor_menus.append(add_pose_copy_buttons)
    # add on_frame_change handler to blender
 
    #bpy.app.handlers.frame_change_pre.append(on_frame_change) 
    #bpy.app.timers.register(SM_MH_Auto_Instance) later?
   

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
       
    except:
        pass
    # ------------------------------------------------------------------------------------------------------------
    #$ delete prop group
    # ------------------------------------------------------------------------------------------------------------
    del(bpy.types.Object.SM_MH_Instances)
    Del_Render_Settings_Props()
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
