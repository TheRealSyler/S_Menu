import bpy 







class SM_mesh_history_panel(bpy.types.Panel):
    """S.Menu Mesh History Panel"""
    bl_label = "Mesh History Panel"
    bl_idname = "SM_mesh_history_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'History'





    def draw(self, context):
        layout = self.layout


        layout.label(text="wdwad")