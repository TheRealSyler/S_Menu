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
        
    ]
    #ShaderNodeTree, CompositorNodeTree, TextureNodeTree, SEQUENCE_EDITOR, CLIP_EDITOR
    type_enum: bpy.props.EnumProperty(name="Areas", items=areas)
    chose_from_list: bpy.props.BoolProperty(name="Chose area Type:", default=True)
    a_type: bpy.props.StringProperty(name="Change area to:")
    test: bpy.props.StringProperty(name="test:")
    

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