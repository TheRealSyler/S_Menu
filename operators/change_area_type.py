import bpy 


class SM_change_area_type(bpy.types.Operator):

    bl_idname = 'sop.sm_change_area_type'
    bl_label = "S.Menu Change Area Type"
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    areas = [
        ("VIEW_3D","View 3D",""),
        ("VIEW","Image Editor",""),
        ("UV","UV Editor",""),
        ("ShaderNodeTree","Shader Editor",""),
        ("CompositorNodeTree","Compositor",""),
        ("TextureNodeTree","Texture Editor",""),
        ("SEQUENCE_EDITOR","Suquence Editor",""),
        ("CLIP_EDITOR","Clip Editor",""),
        ("DOPESHEET","(Not so) Dope Sheet",""),
        ("TIMELINE","Timeline",""),
        ("FCURVES","Graph Editor",""),
        ("DRIVERS","Drivers",""),
        ("NLA_EDITOR","NLA Editor",""),
        ("TEXT_EDITOR","Text Editor",""),
        ("CONSOLE","Console",""),
        ("INFO","Info",""),
        ("OUTLINER","Outliner",""),
        ("PROPERTIES","Properties",""),
        ("FILE_BROWSER","File Browser",""),
        ("PREFERENCES","Preferences",""),
    ]
    #ShaderNodeTree, CompositorNodeTree, TextureNodeTree, SEQUENCE_EDITOR, CLIP_EDITOR, DOPESHEET, TIMELINE, 
    #FCURVES, DRIVERS, NLA_EDITOR, TEXT_EDITOR, CONSOLE, INFO, OUTLINER, PROPERTIES, FILE_BROWSER, PREFERENCES
    type_enum: bpy.props.EnumProperty(name="Areas", items=areas)
    chose_from_list: bpy.props.BoolProperty(name="Chose area Type:", default=True)
    a_type: bpy.props.StringProperty(name="Change area to:")
    test: bpy.props.StringProperty(name="Last Area:")
    

    def execute(self, context):
        context = bpy.context
        area = context.area
        
        # check if True: get area type from enum else: get area type from string (string has to be set)
        if self.chose_from_list is True:
            self.a_type = self.type_enum
            self.test = area.ui_type
            if self.a_type == "":
                self.report({'ERROR'}, "'a_type' Not Set Operator Cancelled")
                return {'CANCELLED'}
            else:
                area.ui_type = self.a_type
        else:
            if self.a_type == "":
                self.report({'ERROR'}, "'a_type' Not Set Operator Cancelled")
                return {'CANCELLED'}
            else:
                area.ui_type = self.a_type
        
        return {'FINISHED'}


def get_next_area(area, reverse):
    #context = bpy.context
    
    areas = [
        "VIEW_3D",
        "VIEW",
        "UV",
    ]
    
    if reverse is False:
        for index, c in enumerate(areas):
            if c == area.ui_type:
                if index == len(areas) - 1:
                    return areas[0]
                else:
                    return areas[index + 1]
    else:
        for index, c in enumerate(areas):
            if c == area.ui_type:
                if index == 0:
                    return areas[len(areas) - 1]
                else:
                    return areas[index - 1]

class SM_change_area_type_modal(bpy.types.Operator):

    bl_idname = 'sop.sm_change_area_type_modal'
    bl_label = "S.Menu Change Area Type Modal"
    bl_description = 'Calls Change Area Type Modal'
    bl_options = {'REGISTER', 'UNDO', 'GRAB_CURSOR', 'BLOCKING'}



    
    def modal(self, context, event):
        
        area = bpy.context.area
        print (area)

        if event.type == 'WHEELUPMOUSE':
            area.ui_type = get_next_area(area, False)

        if event.type == 'WHEELDOWNMOUSE':
            area.ui_type = get_next_area(area, True)
            
        # -------------------------------------------------------------#   
        #+ Finish/Cancel Modal
        elif event.type == 'LEFTMOUSE':
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            return {'CANCELLED'}
        
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        #self.first_mouse_x = event.mouse_x
        #self.first_mouse_y = event.mouse_y
       
        # self.initial_backdrop_offset = bpy.context.space_data.backdrop_offset

        #self.mouse_path = []
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}