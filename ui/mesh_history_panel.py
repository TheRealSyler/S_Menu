import bpy
from .. prefs import get_prefs


class SM_PT_mesh_history_panel(bpy.types.Panel):
    """S.Menu Mesh History Panel"""
    bl_label = "Mesh History (Alpha)"
    bl_idname = "SM_PT_mesh_history_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'History'

    def get_last_index(self, parent):
        index = 0

        for ob in bpy.data.objects:

            if ob.SM_MH_Parent is None:
                return 0
            else:
                if ob.SM_MH_Parent == parent:
                    if index >= ob.SM_MH_index:
                        continue
                    index = ob.SM_MH_index
                else:
                    continue
        return index

    def draw(self, context):
        layout = self.layout

        C = bpy.context
        active_object = C.active_object

        if active_object is not None:
            history_length = len(active_object.SM_MH_Instances) - 1
            col = layout.column()
            if C.mode == 'OBJECT':
                col.enabled = True
            else:
                col.enabled = False

            # if active_object.SM_MH_Parent is None:
            if len(active_object.SM_MH_Instances) == 0:
                panel_enabled = False
                text = "Initialize History"
            else:
                panel_enabled = True

                text = "Add New Instance"

            col.operator("sop.sm_mesh_history_make_instance", text=text)
            if panel_enabled is True:
                box = col.box()
                box.label(text="Instances: " + str(history_length))

            layout.label(text="Switch Mode:")
            col = layout.column()
            if C.mode == 'OBJECT':
                col.operator("sop.sm_mesh_switch_to_edit_mode",
                             text="Edit Mesh", icon="EDITMODE_HLT")
                col.operator("object.mode_set", text="Edit Instance",
                             icon="EDITMODE_HLT").mode = 'EDIT'
            elif C.mode == 'EDIT_MESH':
                col.operator("object.mode_set", text="Object Mode",
                             icon="OBJECT_DATAMODE").mode = 'OBJECT'

            if panel_enabled is True:
                col = layout.column()
                if C.mode == 'OBJECT':
                    col.enabled = True
                else:
                    col.enabled = False
                col.label(text="Animation:")
                col.prop(active_object, "SM_MH_auto_animate",
                         text="Auto Animate")
                col.prop(active_object, "SM_MH_current_index")

                row = col.row()
                row.operator("sop.sm_mesh_history_delete_current_instance",
                             text="Delete Current Instance", icon="CANCEL")

                if get_prefs().show_delete_instances is True:
                    text = "Delete All Instances"
                    box = col.box()
                    box.label(text=text)
                    row = col.row()
                    row.prop(get_prefs(), "sm_mh_del_inst", expand=True)
                    if get_prefs().sm_mh_del_inst == 'NO':
                        row = col.row()
                        row.prop(get_prefs(), "show_delete_instances",
                                 text="Return", icon="CANCEL", expand=True)
                    elif get_prefs().sm_mh_del_inst == 'YES':
                        row = col.row()
                        row.operator("sop.sm_mesh_history_delete_instances",
                                     text="Delete All Instances", icon="CANCEL")
                else:
                    text = ""
                    box = col.box()
                    box.label(text=text)
                    row = col.row()
                    row.prop(get_prefs(), "show_delete_instances",
                             icon="CANCEL")

            # col.prop(active_object, "SM_MH_auto_instance_status") later ?
            #col.prop(get_prefs(), "SM_MH_auto_instance_inerval")
