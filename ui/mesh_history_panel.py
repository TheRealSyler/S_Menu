import bpy 


class SM_mesh_history_panel(bpy.types.Panel):
    """S.Menu Mesh History Panel"""
    bl_label = "Mesh History Panel"
    bl_idname = "SM_mesh_history_panel"
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
            history_length = self.get_last_index(active_object)

            layout.label(text="History Length: " + str(history_length))
            layout.operator("sop.sm_mesh_history_make_copy", text="Make Copy")
            layout.label(text="Mode:")
            layout.operator("sop.sm_mesh_switch_to_edit_mode", text="Edit Mode")
            layout.label(text="wdwad")
            layout.prop(active_object, "SM_MH_current_index")
