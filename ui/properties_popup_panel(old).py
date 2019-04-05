import bpy

from cycles.ui import CYCLES_RENDER_PT_sampling, CYCLES_RENDER_PT_sampling_advanced
#from space_properties import PROPERTIES_PT_navigation_bar


class SM_Properties_Popup(bpy.types.Operator):
    bl_idname = 'sop.sm_properties_popup'
    bl_description = 'test'
    bl_label = 'Properties'

    bl_options = {'UNDO'}

    panels: dict = {}
    label: bool = True


    @classmethod
    def poll(cls, context): 
        return True #PROPERTIES_PT_navigation_bar.poll(context)


    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self, width=300)


    def execute(self, context):
        return {'FINISHED'}


    def draw(self, context):
        layout = self.layout


        #PROPERTIES_PT_navigation_bar.draw(self, context)

        CYCLES_RENDER_PT_sampling.draw(self, context)
        layout.label(text="Advanced")
        CYCLES_RENDER_PT_sampling_advanced.draw(self, context)