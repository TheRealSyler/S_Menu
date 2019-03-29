import bpy

from .. prefs import get_prefs
from bpy.props import IntProperty , FloatVectorProperty

class SM_Modal_adjust_view(bpy.types.Operator):
    bl_idname = 'sop.sm_modal_adjust_view'
    bl_label = "S.Menu Change Channel"
    bl_description = 'Calls Change Channel'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL', 'GRAB_CURSOR', 'BLOCKING'}

    first_mouse_x: IntProperty()
    first_mouse_y: IntProperty()
    initial_backdrop_offset: FloatVectorProperty(size=2)
    

    def get_next_backdrop_channel(self, reverse):
        snode = bpy.context.space_data
        a_backdrop_channels = [
            "COLOR_ALPHA",
            "COLOR",
            "ALPHA",
            "RED",
            "GREEN",
            "BLUE",
        ]
        if reverse is False:
            for index, c in enumerate(a_backdrop_channels):
                if c == snode.backdrop_channels:
                    if index == len(a_backdrop_channels) - 1:
                        return a_backdrop_channels[0]
                    else:
                        return a_backdrop_channels[index + 1]
        else:
            for index, c in enumerate(a_backdrop_channels):
                if c == snode.backdrop_channels:
                    if index == 0:
                        return a_backdrop_channels[len(a_backdrop_channels) - 1]
                    else:
                        return a_backdrop_channels[index - 1]

    def get_channel_text(self):
        snode = bpy.context.space_data
        a_backdrop_channels = [
            "COLOR_ALPHA",
            "COLOR",
            "ALPHA",
            "RED",
            "GREEN",
            "BLUE",
        ]
        n_backdrop_channels = [
            "Color + Alpha",
            "Color",
            "Alpha",
            "Red",
            "Green",
            "Blue",
        ]
        for index, c in enumerate(a_backdrop_channels):
            if c == snode.backdrop_channels:
                return n_backdrop_channels[index]

    def modal(self, context, event):
        snode = bpy.context.space_data
        
        bpy.context.area.header_text_set("       {} {}       {} {}       {} {} {} {} {}       {} {}       {} {}".format(
            "Zoom (Wheel Up/Down + Shift for more Precision):",
            round(snode.backdrop_zoom,2),
            "Channel (Ctrl Wheel Up/Down):",
            self.get_channel_text(),
            "Offset",
            "X:",
            snode.backdrop_offset[0],
            "Y:",
            snode.backdrop_offset[1],
            "Suppress Movement (S):",
            get_prefs().SM_Modal_adjust_view_suppress_move,
            "Apply: (LMB)",
            "Cancel: (RMB Or Esc)",
        ))
        # -------------------------------------------------------------#     
        if event.type == 'WHEELUPMOUSE':
            if event.ctrl:
                snode.backdrop_channels = self.get_next_backdrop_channel(True)
            else:
                if event.shift:
                    snode.backdrop_zoom = snode.backdrop_zoom + 0.01
                else:
                    snode.backdrop_zoom = snode.backdrop_zoom + 0.07

        if event.type == 'WHEELDOWNMOUSE':
            if event.ctrl:
                snode.backdrop_channels = self.get_next_backdrop_channel(False) 
            else:
                if event.shift:     
                    snode.backdrop_zoom = snode.backdrop_zoom - 0.01
                else:    
                    snode.backdrop_zoom = snode.backdrop_zoom - 0.07


        if event.type == 'MOUSEMOVE' :
            if get_prefs().SM_Modal_adjust_view_suppress_move is False:
                delta_x = self.first_mouse_x - event.mouse_x
                snode.backdrop_offset[0] = delta_x * -1

                delta_y = self.first_mouse_y - event.mouse_y
                snode.backdrop_offset[1] = delta_y * -1
        
        if event.type == 'S' and event.value == "PRESS":
            if get_prefs().SM_Modal_adjust_view_suppress_move is True:
                get_prefs().SM_Modal_adjust_view_suppress_move = False
            else:
                get_prefs().SM_Modal_adjust_view_suppress_move = True
                
                snode.backdrop_offset[0] = self.initial_backdrop_offset[0]
                snode.backdrop_offset[1] = self.initial_backdrop_offset[1]


        # -------------------------------------------------------------#   
        #+ Finish/Cancel Modal        
        elif event.type == 'LEFTMOUSE':
            bpy.context.area.header_text_set(None)
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.context.area.header_text_set(None)
            return {'CANCELLED'}
        
        return {'RUNNING_MODAL'}
    
    def invoke(self, context, event):
        self.first_mouse_x = event.mouse_x
        self.first_mouse_y = event.mouse_y
        self.initial_backdrop_offset = bpy.context.space_data.backdrop_offset

        self.mouse_path = []
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}