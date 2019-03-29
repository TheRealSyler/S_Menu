import bpy 


class SM_change_area_type(bpy.types.Operator):

    bl_idname = 'sop.sm_change_area_type'
    bl_label = "S.Menu Change Area Type"
    bl_description = '(Old) Change area Type'
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


class SM_change_area_type_modal(bpy.types.Operator):
    bl_idname = 'sop.sm_change_area_type_modal'
    bl_label = "S.Menu Change Area Type Modal"
    bl_description = 'Calls Change Area Type Modal'
    #bl_options = {'GRAB_CURSOR', 'BLOCKING'}
    index = 0
    screen_area_index = 0
    save_area_ui_type = ''

    def get_next_area(self, area, delta):

        areas = [
            "VIEW_3D",
            "VIEW",
            "UV",
            "ShaderNodeTree",
            "CompositorNodeTree",
            "TextureNodeTree",
            "SEQUENCE_EDITOR",
            "CLIP_EDITOR",
            "DOPESHEET",
            "TIMELINE",
            "FCURVES",
            "DRIVERS",
            "NLA_EDITOR",
            "TEXT_EDITOR",
            "CONSOLE",
            "INFO",
            "OUTLINER",
            "PROPERTIES",
            "FILE_BROWSER",
            "PREFERENCES",
        ]

        self.index = (self.index + len(areas) + delta) % len(areas)
        area.ui_type = areas[self.index]

    def modal(self, context, event):
        area = context.screen.areas[self.screen_area_index]
        area.header_text_set(" {} {}                    {}    {}    {}    {}".format(
            "Current Area:",
            area.type,
            "Next: (Wheel Up)",
            "Previous: (Wheel Down)",
            "Apply: (LMB)",
            "Cancel: (RMB Or Esc)",
        ))

        if event.type == 'WHEELUPMOUSE':
            self.get_next_area(area, 1)
            return {'RUNNING_MODAL'}
        
        elif event.type == 'WHEELDOWNMOUSE':
            self.get_next_area(area, -1)
            return {'RUNNING_MODAL'}

        elif event.type == 'LEFTMOUSE':
            area.header_text_set(None)
            return {'FINISHED'}
        
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            area.header_text_set(None)
            area.ui_type = self.save_area_ui_type
            return {'CANCELLED'}

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        self.screen_area_index = context.screen.areas[:].index(context.area)
        self.save_area_ui_type = context.area.ui_type
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
