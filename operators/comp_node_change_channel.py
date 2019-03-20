import bpy


class SM_Modal_change_channel(bpy.types.Operator):
    bl_idname = 'sop.sm_modal_change_channel'
    bl_label = "S.Menu Change Channel"
    bl_description = 'Calls Change Channel'
    bl_options = {'REGISTER', 'UNDO', "INTERNAL"}

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
        bpy.context.area.header_text_set("  Channel: " + self.get_channel_text() + "                  Use the Mousewheel to change Channel")
        # -------------------------------------------------------------#     
        if event.type == 'WHEELUPMOUSE':
            snode.backdrop_channels = self.get_next_backdrop_channel(False) 
            
            
        if event.type == 'WHEELDOWNMOUSE':
            snode.backdrop_channels = self.get_next_backdrop_channel(True)

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


        self.mouse_path = []
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
