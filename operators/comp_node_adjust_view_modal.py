import bpy

from bpy.props import IntProperty
from .. ui.comp_node_adjust_view_modal_ui import SM_adujst_view_modal_draw

class SM_Modal_adjust_view(bpy.types.Operator):
    bl_idname = 'sop.sm_modal_adjust_view'
    bl_label = "S.Menu Adjust View Modal"
    bl_description = 'Calls Adjust View Modal'
    bl_options = {'REGISTER', 'UNDO', "BLOCKING", "GRAB_CURSOR"}  # § add later "INTERNAL"

    first_mouse_x: IntProperty()


    def modal(self, context, event):
    
        #C = context
        context.area.tag_redraw()  # Important Dont Remove
        # -------------------------------------------------------------#     
        #+ change offset        
        if event.type == 'MOUSEMOVE' :
            #delta = self.first_mouse_x - event.mouse_x
            pass

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceNodeEditor.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}
    
    def invoke(self, context, event):
        
        args = (self, context)

        self.mouse_path = []
        self._handle = bpy.types.SpaceNodeEditor.draw_handler_add(SM_adujst_view_modal_draw, args, 'WINDOW', 'POST_PIXEL')
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
