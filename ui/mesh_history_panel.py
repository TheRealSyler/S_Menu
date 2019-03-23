import bpy 
from .. prefs import get_prefs




class SM_mesh_history_panel(bpy.types.Panel):
    """S.Menu Mesh History Panel"""
    bl_label = "Mesh History"
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
            col = layout.column()
            if C.mode == 'OBJECT':
                col.enabled = True
            else:
                col.enabled = False
            
            if active_object.SM_MH_Parent is None:
                text = "Initialize History"
            else:
                text = "Make Instance"
                col.label(text="History Length: " + str(history_length))
            
            col.operator("sop.sm_mesh_history_make_instance", text=text)
            layout.label(text="Switch Mode:")
            col = layout.column()
            if C.mode == 'OBJECT':
                col.operator("sop.sm_mesh_switch_to_edit_mode", text="Edit Mesh", icon="EDITMODE_HLT")
                col.operator("object.mode_set",text="Edit Instance", icon="EDITMODE_HLT").mode = 'EDIT'
            elif C.mode == 'EDIT_MESH':
                col.operator("object.mode_set",text="Object Mode", icon="OBJECT_DATAMODE").mode = 'OBJECT'
                
            
            col = layout.column()
            if C.mode == 'OBJECT':
                col.enabled = True
            else:
                col.enabled = False
            col.label(text="Animation:")
            col.prop(active_object, "SM_MH_auto_animate", text="Auto Animate")
            #SM_MH_auto_animate
            col.label(text="Current Index:")
            col.prop(active_object, "SM_MH_current_index")
            
            
            col = layout.column()
            col.prop(get_prefs(), "SM_MH_help")
            if get_prefs().SM_MH_help is True:
                col.label(text="help is Enabled WIP")
