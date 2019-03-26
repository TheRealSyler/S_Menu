import bpy

from cycles.ui import CYCLES_RENDER_PT_sampling, CYCLES_RENDER_PT_sampling_advanced


class SM_Render_Settings_Popup(bpy.types.Operator):
    bl_idname = 'sop.sm_render_settings_popup'
    bl_description = 'test'
    bl_label = 'Properties'

    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context): 
        return True


    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self, width=400)


    def execute(self, context):
        return {'FINISHED'}


    def draw(self, context):
        layout = self.layout


     

        CYCLES_RENDER_PT_sampling.draw(self, context)
        layout.label(text="Advanced")
        CYCLES_RENDER_PT_sampling_advanced.draw(self, context)