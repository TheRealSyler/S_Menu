import bpy

from . ui.pie_menus import (
    # get_prefs,
    SM_MT_pie_add,
    SM_MT_pie_add_call,
    SM_MT_pie_add_node,
    SM_MT_pie_add_node_call,
    SM_MT_add_texture_node,
    SM_MT_add_shader_node,
    SM_MT_pie_q_menu,
    SM_MT_pie_q_menu_call,
    SM_MT_pie_a_om,
    SM_MT_pie_a_om_call,
    SM_MT_pie_q_node,
    SM_MT_pie_q_node_call,
    SM_MT_pie_a_node,
    SM_MT_pie_a_node_call,
    SM_MT_pie_tab_menu,
    SM_MT_pie_tab_menu_call,
    SM_MT_pie_m4_menu,
    SM_MT_pie_m4_menu_call,
    SM_MT_pie_w_menu,
    SM_MT_pie_w_menu_call,
    SM_MT_pie_w_sculpt_menu,
    SM_MT_ot_w_sculpt_menu_call,
)
from . ui.mesh_history_panel import SM_PT_mesh_history_panel
from . operators.comp_adjust_view import SM_Modal_adjust_view
from . operators.mesh_history_operator import (
    SM_mesh_history_Props,
    SM_mesh_history_make_Instance,
    SM_mesh_history_switch_to_edit_mode,
    on_frame_change,
    # SM_MH_Auto_Instance, later?
    SM_mesh_history_delete_instances,
    SM_mesh_history_delete_current_instance,
    SM_MH_Instances,
)
from . prefs import SM_Prefs, add_hotkey, remove_hotkey
from . ui.get_icon import register_icons, unregister_icons
from . ui.add_pose_copy_buttons import add_pose_copy_buttons


from . operators.change_area_type import SM_change_area_type, SM_change_area_type_modal
from . ui.change_workspaces_pie import SM_MT_pie_workspaces_menu, SM_MT_pie_workspaces_menu_Call, SM_change_workspace

from . ui.main_popup_panel import SM_OT_Main_Popup, Main_Popup_Props, Render_Settings_Props, GOS_Props

bl_info = {
    "name": "S.Menu",
    "author": "Syler",
    "version": (0, 0, 1, 5),
    "description": "Adds Pie Menus",
    "blender": (2, 80, 0),
    "category": "3D view"
}


classes = [
    # § Props
    Main_Popup_Props,
    GOS_Props,
    Render_Settings_Props,
    # ? PIE Menus and pie menu calls
    SM_MT_pie_add,
    SM_MT_pie_add_call,
    SM_MT_pie_add_node,
    SM_MT_pie_add_node_call,
    SM_MT_add_texture_node,
    SM_MT_add_shader_node,
    SM_MT_pie_q_menu,
    SM_MT_pie_q_menu_call,
    SM_MT_pie_a_om,
    SM_MT_pie_a_om_call,
    SM_MT_pie_q_node,
    SM_MT_pie_q_node_call,
    SM_MT_pie_a_node,
    SM_MT_pie_a_node_call,
    SM_MT_pie_tab_menu,
    SM_MT_pie_tab_menu_call,
    SM_MT_pie_m4_menu,
    SM_MT_pie_m4_menu_call,
    SM_MT_pie_w_menu,
    SM_MT_pie_w_menu_call,
    SM_MT_pie_w_sculpt_menu,
    SM_MT_ot_w_sculpt_menu_call,
    # ------
    SM_MT_pie_workspaces_menu,
    SM_MT_pie_workspaces_menu_Call,
    # ? Prefs
    SM_Prefs,
    # + Mesh Hisrtory
    SM_PT_mesh_history_panel,
    SM_mesh_history_Props,
    SM_mesh_history_make_Instance,
    SM_mesh_history_switch_to_edit_mode,
    SM_mesh_history_delete_instances,
    SM_mesh_history_delete_current_instance,
    SM_MH_Instances,
    # ? Popup Panels
    SM_OT_Main_Popup,
    # § Operators
    SM_change_area_type,
    SM_change_workspace,
    # § Modals
    SM_Modal_adjust_view,
    SM_change_area_type_modal,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    # + add hotkey
    add_hotkey()
    # ------------------------------------------------------------------------------------------------------------
    # § Register prop group
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.Object.SM_MH_Instances = bpy.props.CollectionProperty(
        type=SM_MH_Instances)
    bpy.types.Scene.SM_GOS_Props = bpy.props.PointerProperty(type=GOS_Props)
    bpy.types.Scene.SM_Render_Settings_Props = bpy.props.PointerProperty(
        type=Render_Settings_Props)
    bpy.types.Scene.SM_Main_Popup_Props = bpy.props.PointerProperty(
        type=Main_Popup_Props)
    # ------------------------------------------------------------------------------------------------------------
    # + Append Register stuff
    # ------------------------------------------------------------------------------------------------------------
    bpy.types.VIEW3D_MT_editor_menus.append(add_pose_copy_buttons)
    # add on_frame_change handler to blender

    # bpy.app.handlers.frame_change_pre.append(on_frame_change)
    # bpy.app.timers.register(SM_MH_Auto_Instance) later?

    # ------------------------------------------------------------------------------------------------------------
    # Icons Register stuff
    # ------------------------------------------------------------------------------------------------------------
    register_icons(__file__)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    # + remove hotkey
    remove_hotkey()
    # remove on_frame_change handler from blender
    try:
        bpy.app.handlers.frame_change_pre.remove(on_frame_change)
        # bpy.app.timers.unregister(SM_MH_Auto_Instance) later?

    except:
        pass
    # ------------------------------------------------------------------------------------------------------------
    # $ delete prop group
    # ------------------------------------------------------------------------------------------------------------
    del(bpy.types.Object.SM_MH_Instances)
    del(bpy.types.Scene.SM_GOS_Props)
    del(bpy.types.Scene.SM_Render_Settings_Props)
    del(bpy.types.Scene.SM_Main_Popup_Props)
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
