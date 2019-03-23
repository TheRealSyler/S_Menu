import bpy, os
from . get_icon import get_icon


# todo add Extra Object (Curve) support

#+-----------------------------------------------------------------------------------------------------+#
#? Utils 
#+-----------------------------------------------------------------------------------------------------+#

def disabled_button(col, text, icon):
    col.label(text=text, icon_value=icon)

def op_loop_val(col, enum, text, icon, spacer, spinum):
    for index, e in enumerate(enum):            
        if index == spinum and spacer is True:
            col.separator()
        if col.operator(e, text=text[index],icon_value=icon[index]) is None:
            col.label(text="Not Installed")

def op_loop(col, enum, text, icon, spacer, spinum):
    for index, e in enumerate(enum):            
        if index == spinum and spacer is True:
            col.separator()
        if col.operator(e, text=text[index],icon=icon[index]) is None:
            col.label(text="Not Installed")

def op_loop_safe(col, enum, text, icon, type):
    for index, e in enumerate(enum):
        op = col.operator(e, text=text[index],icon=icon[index])
        op.type = type[index]

def op_loop_name(col, enum, text, icon, name):
    for index, e in enumerate(enum):
        op = col.operator(e, text=text[index],icon=icon[index])
        op.name = name[index]

def op_loop_safe_node(col, num, text, icon, type):
    for index in range(0, num):
        op = col.operator("node.add_node", text=text[index],icon=icon[index])
        op.type = type[index]
        op.use_transform = True

def op_loop_safe_node_val(col, num, text, icon, type):
    for index in range(0, num):
        op = col.operator("node.add_node", text=text[index],icon_value=icon[index])
        op.type = type[index]
        op.use_transform = True

def spacer(col, num):
    for i in range(0, num):
        col.label(text="")

def get_addon_name():
    parent = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

    return os.path.split(os.path.dirname(parent))[1]

def get_prefs():
    return bpy.context.preferences.addons[get_addon_name()].preferences

#+-----------------------------------------------------------------------------------------------------+#
#? Utils
#+-----------------------------------------------------------------------------------------------------+#
class SM_PIE_Add(bpy.types.Menu):
    bl_label = "Add"
    

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()

        # 4 - LEFT
        split = pie.split()
        #column = split.column()
        b = split.column(align=True)
        self.add_mesh_box(b)

        # 6 - RIGHT
        split = pie.split()
        b = split.column(align=True)
        column = split.column(align=True)
        self.forces(column, 0)
        self.curve(b, 2)
        
        # 2 - BOTTOM
        split = pie.split()
        if get_prefs().enable_extra_objects_mesh is True:
            b = split.column(align=True)
            self.extra_objects(b)
        b = split.column(align=True)
        self.camera(b, 3)

        column = split.column(align=True)
        self.empty(column, 3)
        
        # 8 - TOP
        split = pie.split()
        column = split.column(align=True)
        self.light_2_box(column, 3)
        
        b = split.column(align=True)
        self.light_1_box(b)

        column = split.column(align=True)
        self.bone(column)
        
        # 7 - TOP - LEFT
        pie.separator()
        # 9 - TOP - RIGHT
        pie.separator()
        # 1 - BOTTOM - LEFT
        pie.separator()
        # 3 - BOTTOM - RIGHT
        split = pie.split()
        column = split.column(align=True)
        self.add_menu(column)

    def add_mesh_box(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("mesh.primitive_ico_sphere_add"),
            ("mesh.primitive_cone_add"),
            ("mesh.primitive_circle_add"),
            ("mesh.primitive_cylinder_add"),
            ("mesh.primitive_uv_sphere_add"),
            ("mesh.primitive_cube_add"),
            ("mesh.primitive_plane_add"),
            ("object.text_add"),
        ]
        text = [
            ("Ico Sphere"),
            ("Cone"),
            ("Cirlce"),
            ("Cylinder"),
            ("Sphere"),
            ("Cube"),
            ("Plane"),
            ("Text"),
        ]
        icon = [
            get_icon("Ico_Sphere_icon", "main"),
            get_icon("Cone_icon", "main"),
            get_icon("Circle_icon", "main"),
            get_icon("Cylinder_icon", "main"),
            get_icon("Sphere_icon", "main"),
            get_icon("Cube_icon", "main"),
            get_icon("Plane_icon", "main"),
            get_icon("Text_icon", "main"),       
        ]

        op_loop_val(col, enum, text, icon, False, 7)

        if get_prefs().enable_extra_objects_mesh is True:
            if col.operator("mesh.primitive_vert_add", text="Single Vert", icon_value=get_icon("Reroute_icon", "main")) is None:
                col.label(text="Please Disable")
            if col.operator("mesh.primitive_round_cube_add", text="Round Cube", icon_value=get_icon("Sphere_icon", "main")) is None:
                col.label(text="Extra Objects in addon prefs")
        if get_prefs().enable_landscape is True:
            if col.operator("mesh.add_mesh_rock", text="Rock Generator", icon_value=get_icon("Rock_icon", "main")) is None:
                col.label(text="Not Installed")
        if get_prefs().enable_landscape is True:
            if col.operator("mesh.landscape_add", text="Landscape", icon_value=get_icon("Landscape_icon", "main"),) is None:
                col.label(text="Not Installed")   
        if get_prefs().enable_bolt is True:
            if col.operator("mesh.bolt_add", text="Bolt", icon_value=get_icon("Bolt_icon", "main"),) is None:
                col.label(text="Not Installed")
        
    def light_1_box(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("object.light_add"),
            ("object.light_add"),
            ("object.light_add"),
            ("object.light_add"),
        ]
        text = [
            ("Area "),
            ("Spot "),
            ("Sun "),
            ("Point "),
        ]
        icon = [
            302,
            300,
            299,
            298,
        ]
        light = [
            ('AREA'),
            ('SPOT'),
            ('SUN'),
            ('POINT'),
        ]

        for index, e in enumerate(enum):
            op = col.operator(e, text=text[index],icon_value=icon[index])
            op.type = light[index]
    
    def light_2_box(self, col, snum):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("object.lightprobe_add"),
            ("object.lightprobe_add"),
            ("object.lightprobe_add"),

        ]
        text = [
            ("Reflection Cubemap"),
            ("Reflection Plane"),
            ("Irrandce Volume"),

        ]
        icon = [
            326,
            327,
            328, 
        ]
        light = [
            ('CUBEMAP'),
            ('PLANAR'),
            ('GRID'),
  
        ]

        for index, e in enumerate(enum):
            op = col.operator(e, text=text[index],icon_value=icon[index])
            op.type = light[index]
        spacer(col, snum)

    def empty(self, col, snum):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("object.empty_add"),
            ("object.empty_add"),
            ("object.empty_add"),
            ("object.empty_add"),
            ("object.empty_add"),
            ("object.empty_add"),
            ("object.empty_add"),
            ("object.empty_add"),
        ]
        text = [
            ("Plain Axes"),
            ("Arrows"),
            ("Single Arrow"),
            ("Circle"),
            ("Cube"),
            ("Sphere"),
            ("Cone"),
            ("Image"),
        ]
        icon = [
            ('EMPTY_AXIS'),
            ('EMPTY_ARROWS'),
            ('EMPTY_SINGLE_ARROW'),
            ('MESH_CIRCLE'),
            ('CUBE'),
            ('SPHERE'),
            ('CONE'),
            ('FILE_IMAGE'),
        ]
        e_type = [
            ('PLAIN_AXES'),
            ('ARROWS'),
            ('SINGLE_ARROW'),
            ('CIRCLE'),
            ('CUBE'),
            ('SPHERE'),
            ('CONE'),
            ('IMAGE'),
        ]
        
        spacer(col, snum)
        op_loop_safe(col, enum, text, icon, e_type)
    
    def camera(self, col, snum):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("object.camera_add"),
            ("object.load_reference_image"),
            ("object.load_background_image"),
            ("import_image.to_plane"),
            ("object.speaker_add"),
            ("object.build_dolly_rig"),
            ("object.build_crane_rig"),
        ]
        text = [
            ("Camera"),
            ("Reference"),
            ("Background"),
            ("As Plane"),
            ("Speaker"),
            ("Dolly Camera Rig"),
            ("Crane Camera Rig"),
        ]
        icon = [
            ("OUTLINER_DATA_CAMERA"),
            ("IMAGE_REFERENCE"),
            ("IMAGE_BACKGROUND"),
            ("TEXTURE_DATA"),
            ("OUTLINER_OB_SPEAKER"),
            ("OUTLINER_OB_CAMERA"),
            ("CAMERA_DATA"),
        ]
  
        spacer(col, snum)
        op_loop(col, enum, text, icon, False, 3)
    
    def forces(self, col, snum):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
            ("object.effector_add"),
        ]
        text = [
            ("Force"),
            ("Wind"),
            ("Vortex"),
            ("Magnetic"),
            ("Harmonic"),
            ("Charge"),
            ("Lennard-Jones"),
            ("Texture"),
            ("Curve Guide"),
            ("Boid"),
            ("Turbulence"),
            ("Drag"),
            ("Smoke Flow"),
        ]
        icon = [
            ("FORCE_FORCE"),
            ("FORCE_WIND"),
            ("FORCE_VORTEX"),
            ("FORCE_MAGNETIC"),
            ("FORCE_HARMONIC"),
            ("FORCE_CHARGE"),
            ("FORCE_LENNARDJONES"),
            ("FORCE_TEXTURE"),
            ("FORCE_CURVE"),
            ("FORCE_BOID"),
            ("FORCE_TURBULENCE"),
            ("FORCE_DRAG"),
            ("FORCE_SMOKEFLOW"),
        ]
        e_type = [
            ('FORCE'),
            ('WIND'),
            ('VORTEX'),
            ('MAGNET'),
            ('HARMONIC'),
            ('CHARGE'),
            ('LENNARDJ'),
            ('TEXTURE'),
            ('GUIDE'),
            ('BOID'),
            ('TURBULENCE'),
            ('DRAG'),
            ('SMOKE'),
        ]
        spacer(col, snum)
        op_loop_safe(col, enum, text, icon, e_type)
    
    def bone(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("object.gpencil_add"),
            ("object.gpencil_add"),
            ("object.gpencil_add"),
            ("object.add"),

        ]
        text = [
            ("Monkey"),
            ("Stroke"),
            ("Blank"),
            ("Lattice"),

        ]
        icon = [
            ("MONKEY"),
            ("OUTLINER_OB_GREASEPENCIL"),
            ("GREASEPENCIL"),
            ("OUTLINER_OB_LATTICE"),
        ]
        e_type = [
            ('MONKEY'),
            ('STROKE'),
            ('EMPTY'),
            ('LATTICE'),
        ]
        
        op_loop_safe(col, enum, text, icon, e_type)
        col.operator("object.armature_add", text="Single Bone",icon="BONE_DATA")

    def curve(self, col, snum):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("curve.primitive_bezier_curve_add"),
            ("curve.primitive_bezier_circle_add"),
            ("curve.primitive_nurbs_curve_add"),
            ("curve.primitive_nurbs_circle_add"),
            ("curve.primitive_nurbs_path_add"),

        ]
        text = [
            ("Bezier"),
            ("Bezier Cirlce"),
            ("Nurbs"),
            ("Nurbs Cirlce"),
            ("Path"),

        ]
        icon = [
            ("CURVE_BEZCURVE"),
            ("CURVE_BEZCIRCLE"),
            ("CURVE_NCURVE"),
            ("CURVE_NCIRCLE"),
            ("CURVE_PATH"),
        ]
        if get_prefs().enable_pipenightmare is False:
            snum = snum + 1
        spacer(col, snum)
        if get_prefs().enable_pipenightmare is True:
            if col.operator("object.pipe_nightmare", text="Pipes", icon="GRAPH") is None:
                col.label(text="Not Installed")
        
        op_loop(col, enum, text, icon, True, 2)

    def add_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 2)
        col.label(text="                                 ")
        box = col.box()
        box.menu("VIEW3D_MT_add", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main"))
        
        if get_prefs().enable_qblocker is True:
            if col.operator("object.box_create", text="Q Cube") is None:
                col.label(text="Not Installed")
            if col.operator("object.cylinder_create", text="Q Cylinder") is None:
                col.label(text="Not Installed")
            if col.operator("object.sphere_create", text="Q Sphere") is None:
                col.label(text="Not Installed")
        

    def extra_objects(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("discombobulate.ops"),
            ("object.parent_to_empty"),
        ]
        text = [
            ("Discombobulator"),
            ("Parent to Empty"),
        ]
        icon = [
            9,
            9,    
        ]
        spacer(col, 3)
        op_loop_val(col, enum, text, icon, False, 7)
        box = col.box()
        col.label(text="                                 ")
        box.menu("VIEW3D_MT_mesh_extras_add",text="Extras", icon_value=get_icon("List_icon", "main"))
        box.menu("VIEW3D_MT_mesh_math_add",text="Math Function", icon_value=get_icon("List_icon", "main"))
        box.menu("VIEW3D_MT_mesh_mech_add",text="Mechanical", icon_value=get_icon("List_icon", "main"))
        box.menu("VIEW3D_MT_mesh_torus_add",text="Torus Objects", icon_value=get_icon("List_icon", "main"))

class SM_PIE_Add_Call(bpy.types.Operator):
    bl_idname = 'sop.sm_pie_add_call'
    bl_label = 'S.Menu Add Pie'
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_PIE_Add")
        return {'FINISHED'}

class SM_PIE_Add_Node(bpy.types.Menu):
    bl_label = "Node"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # check if in compositor
        if bpy.context.area.ui_type == "CompositorNodeTree":
            # 4 - LEFT
            split = pie.split()
            b = split.column_flow(columns=2, align=True)
            self.C9(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column(align=True)
            self.comp_add_menu(b)
            # 2 - BOTTOM
            split = pie.split()
            b = split.column(align=True)
            self.comp_menu_3(b)
            b = split.column(align=True)
            self.comp_menu_2(b)
            b = split.column(align=True)
            self.comp_menu_1(b)
            # 8 - TOP
            split = pie.split()
            b = split.column()
            box = b.box()
            self.group_menu_add(box)
            self.search(b)
            # 7 - TOP - LEFT
            split = pie.split()
            b = split.column(align=True)
            b.label(text="                                   ")
            b = split.column(align=True)
            self.comp_menu_6(b)
            b = split.column(align=True)
            self.comp_menu_8(b)
            # 9 - TOP - RIGHT
            split = pie.split()
            b = split.column(align=True)
            self.comp_menu_4(b)
            b = split.column(align=True)
            self.comp_menu_5(b)
            b = split.column(align=True)
            self.comp_menu_7(b)
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()
        # check if in Texture node tree
        elif bpy.context.area.ui_type == "TextureNodeTree":
            # 4 - LEFT
            split = pie.split()
            b = split.column(align=True)
            self.tex_node_utils(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column(align=True)
            self.add_menu_tex(b)
            # 2 - BOTTOM
            split = pie.split()
            b = split.column()
            self.texture_add(b)
            # 8 - TOP
            split = pie.split()
            self.search(split) 
        # check if in shading
        elif bpy.context.area.ui_type == "ShaderNodeTree":
            
            # 4 - LEFT
            split = pie.split()
            b = split.column(align=True)
            self.node_utils(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column(align=True)
            self.shader_add(b)
            # 2 - BOTTOM
            split = pie.split()
            b = split.column(align=True)
            self.node_color(b)
            b = split.column(align=True)
            self.node_vector(b)
            b = split.column()
            # note: dont change the text
            b.label(text="                                                ")
            # 8 - TOP
            split = pie.split()
            self.search(split)     
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            split = pie.split()
            b = split.column()
            self.texture_add(b)
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            split = pie.split()
            column = split.column(align=True)
            self.add_menu(column)
            column = split.column(align=True)
            self.converter_menu(column)

    def node_utils(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        text = [
            ("Math"),
            ("Color Ramp"),
            ("Value"),
            ("RGB Curve"),
            ("Mix Shader"),
            ("Mix"),
            ("Add Shader"),
            ("Layer Weight"),
            ("Hue Saturation"),
            ("Color Input"),
        ]
        icon = [
            (get_icon("Math_icon", "main")),  
            (get_icon("Color_Ramp_icon", "main")),
            (get_icon("Value_icon", "main")),
            (get_icon("RGB_C_icon", "main")),
            (get_icon("SH_Mix_icon", "main")),
            (get_icon("Mix_Color_icon", "main")),
            (get_icon("SH_Add_icon", "main")),
            (get_icon("LW_icon", "main")),
            (get_icon("Hue_icon", "main")),
            (get_icon("RGB_icon", "main")),
        ]
        e_type = [
            ("ShaderNodeMath"),
            ("ShaderNodeValToRGB"),
            ("ShaderNodeValue"),
            ("ShaderNodeRGBCurve"),
            ("ShaderNodeMixShader"),
            ("ShaderNodeMixRGB"),
            ("ShaderNodeAddShader"),
            ("ShaderNodeLayerWeight"),
            ("ShaderNodeHueSaturation"),
            ("ShaderNodeRGB"),
        ]
        
        op_loop_safe_node_val(col, 10, text, icon, e_type)
    
    def comp_node_utils(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        text = [
            ("Viewer"),
            ("Math"),
            ("Color Ramp"),
            ("Value"),
            ("RGB Curve"),
            ("Mask"),
            ("Mix"),
            ("Glare"),
            ("Sun Beams"),
            ("Lens Distortion"),
            ("Hue Saturation"),
            ("Color Input"),
            ("Split Viewer"),
            ("Switch"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Math_icon", "main")),  
            (get_icon("Color_Ramp_icon", "main")),
            (get_icon("Value_icon", "main")),
            (get_icon("RGB_C_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Mix_Color_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Hue_icon", "main")),
            (get_icon("RGB_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodeViewer"),
            ("CompositorNodeMath"),
            ("CompositorNodeValToRGB"),
            ("CompositorNodeValue"),
            ("CompositorNodeCurveRGB"),
            ("CompositorNodeMask"),
            ("CompositorNodeMixRGB"),
            ("CompositorNodeGlare"),
            ("CompositorNodeSunBeams"),
            ("CompositorNodeLensdist"),
            ("CompositorNodeHueSat"),
            ("CompositorNodeRGB"),
            ("CompositorNodeSplitViewer"),
            ("CompositorNodeSwitch"),
        ]
        
        op_loop_safe_node_val(col, 13, text, icon, e_type)

    def tex_node_utils(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        text = [
            ("Distance"),
            ("Coordinates"),
            ("Curve Time"),
            ("Image"),
            ("Texture"),
            ("RGB Curve"),
            ("Mix"),
            ("Math"),
            ("Color Ramp"),
            ("Checker"),
            ("Brick"),
            ("RGB to BW"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
        ]
        e_type = [
            ("TextureNodeDistance"),
            ("TextureNodeCoordinates"),
            ("TextureNodeCurveTime"),
            ("TextureNodeImage"),
            ("TextureNodeTexture"),
            ("TextureNodeCurveRGB"),
            ("TextureNodeMixRGB"),
            ("TextureNodeMath"),
            ("TextureNodeValToRGB"),
            ("TextureNodeChecker"),
            ("TextureNodeBricks"),
            ("TextureNodeRGBToBW"),
        ]
        
        op_loop_safe_node_val(col, 12, text, icon, e_type)
        box = col.box()
        self.group_menu_add(box)

    def node_vector(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        text = [
            ("Vector Math"),
            ("Bump"),
            ("Displacement"),
            ("Mapping"),
            ("Normal"),
            ("Normal Map"),
            ("Vector Curve"),
            ("Vector Displacement"),
            ("Vector Transform"),
        ]
        icon = [
            (get_icon("Vector_Math_icon", "main")), 
            (get_icon("Bump_icon", "main")),
            (get_icon("Displacement_icon", "main")),
            (get_icon("Mapping_icon", "main")),
            (get_icon("Normal_icon", "main")),
            (get_icon("Normal_Map_icon", "main")), 
            (get_icon("VC_icon", "main")),
            (get_icon("V_Displacement_icon", "main")),
            (get_icon("Vector_Transform_icon", "main")),
        ]
        e_type = [
            ("ShaderNodeVectorMath"),
            ("ShaderNodeBump"),
            ("ShaderNodeDisplacement"),
            ("ShaderNodeMapping"),
            ("ShaderNodeNormal"),
            ("ShaderNodeNormalMap"),
            ("ShaderNodeVectorCurve"),
            ("ShaderNodeVectorDisplacement"),
            ("ShaderNodeVectorTransform"),
        ]
        
        op_loop_safe_node_val(col, 9, text, icon, e_type)

    def node_color(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        text = [
            ("Bright Contrast"),
            ("Gamma"),
            ("Invert"),
            ("Light Falloff"),
            ("Wireframe"),
            ("Fresnel"),
            ("Tangent"),
            ("UV Map"),
        ]
        icon = [
            (get_icon("BrightContrast_icon", "main")), 
            (get_icon("Gamma_icon", "main")),
            (get_icon("Invert_icon", "main")),
            (get_icon("Light_Falloff_icon", "main")),
            (get_icon("Value_icon", "main")), 
            (get_icon("Fresnel_icon", "main")),
            (get_icon("Tangent_icon", "main")),
            (get_icon("UV_Map_icon", "main")),
        ]
        e_type = [
            ("ShaderNodeBrightContrast"),
            ("ShaderNodeGamma"),
            ("ShaderNodeInvert"),
            ("ShaderNodeLightFalloff"),
            ("ShaderNodeWireframe"),
            ("ShaderNodeFresnel"),
            ("ShaderNodeTangent"),
            ("ShaderNodeUVMap"),
        ]
        spacer(col, 2)
        op_loop_safe_node_val(col, 8, text, icon, e_type)

    def search(self, col):
        col.scale_x = 1.35
        col.scale_y = 2
        col.operator("node.add_search", text="Search...", icon="VIEWZOOM")

    def texture_add(self, col):
        col.scale_x = 1.1
        col.scale_y = 1.8
        col.operator_context = "INVOKE_DEFAULT"
        col.operator("wm.call_menu_pie", text="Texture", icon="TEXTURE").name = "SM_Add_Texture_Node"
    
    def shader_add(self, col):
        col.scale_x = 1.1
        col.scale_y = 1.8
        col.operator("wm.call_menu_pie", text="Shader", icon="SHADING_RENDERED").name = "SM_Add_Shader_Node"
    
    def group_menu_add(self, col):
        col.menu("NODE_MT_category_CMP_GROUP", text="Groups", icon_value=get_icon("List_icon", "main"))

    def add_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 10)
        col.label(text="                                    ")
        box = col.box()
        box.menu("NODE_MT_add", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main"))
        text = [
            ("Frame"),
            ("Reroute"),
            ("Material Output"),
            ("Script"),
            ("Light Path"),
            ("Object Info"),
            ("Particle Info"),
            ("Camera Data"),
            ("Geometry"),
            ("Hair Info"),
            ("Tex Coord"),
        ]
        icon = [
            (get_icon("Frame_icon", "main")), 
            (get_icon("Reroute_icon", "main")),
            (get_icon("Mat_Out_icon", "main")),
            (get_icon("Script_icon", "main")),
            (get_icon("Value_icon", "main")), 
            (get_icon("Object_Info_icon", "main")),
            (get_icon("Particle_Info_icon", "main")),
            (get_icon("Value_icon", "main")),
            (get_icon("Value_icon", "main")), 
            (get_icon("Value_icon", "main")),
            (get_icon("Hair_Info_icon", "main")),
            (get_icon("Value_icon", "main")),
           
        ]
        e_type = [
            ("NodeFrame"),
            ("NodeReroute"),
            ("ShaderNodeOutputMaterial"),
            ("ShaderNodeScript"),
            ("ShaderNodeLightPath"),
            ("ShaderNodeObjectInfo"),
            ("ShaderNodeParticleInfo"),
            ("ShaderNodeCameraData"),
            ("ShaderNodeNewGeometry"),
            ("ShaderNodeHairInfo"),
            ("ShaderNodeTexCoord"),
        ]
        self.group_menu_add(box)
        op_loop_safe_node_val(col, 11, text, icon, e_type)
        col.label(text="                                ")

    def add_menu_tex(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        col.label(text="                                ")
        box = col.box()
        box.menu("NODE_MT_add", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main"))
       
        text = [
            ("Frame"),
            ("Reroute"),
            ("Output"),
            ("Viewer"),
            ("Value To Normal"),
            ("Invert"),
            ("Hue Saturation"),
            ("Combine RGBA"),
            ("Separate RGBA"),
            ("At"),
            ("Rotate"),
            ("Scale"),
            ("Translate"),
        ]
        icon = [
            (get_icon("Frame_icon", "main")), 
            (get_icon("Reroute_icon", "main")),
            (get_icon("Mat_Out_icon", "main")),
            (get_icon("Mat_Out_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("NodeFrame"),
            ("NodeReroute"),
            ("TextureNodeOutput"),
            ("TextureNodeViewer"),
            ("TextureNodeValToNor"),
            ("TextureNodeInvert"),
            ("TextureNodeHueSaturation"),
            ("TextureNodeCompose"),
            ("TextureNodeDecompose"),
            ("TextureNodeAt"),
            ("TextureNodeRotate"),
            ("TextureNodeScale"),
            ("TextureNodeTranslate"),
        ]
        op_loop_safe_node_val(col, 13, text, icon, e_type)
        col.label(text="                                ")

    def converter_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        text = [
            ("Shader To RGB"),
            ("RGB to BW"),
            ("Separate HSV"),
            ("Separate RGB"),
            ("Separate XYZ"),
            ("Blackbody"),
            ("Wavelength"),
            ("Combine HVS"),
            ("Combine RGB"),
            ("Combine XYZ"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("ShaderNodeShaderToRGB"),
            ("ShaderNodeRGBToBW"),
            ("ShaderNodeSeparateHSV"),
            ("ShaderNodeSeparateRGB"),
            ("ShaderNodeSeparateXYZ"),
            ("ShaderNodeBlackbody"),
            ("ShaderNodeWavelength"),
            ("ShaderNodeCombineHSV"),
            ("ShaderNodeCombineRGB"),
            ("ShaderNodeCombineXYZ"),
        ]
        spacer(col, 6)
        op_loop_safe_node_val(col, 10, text, icon, e_type)
    
    def comp_add_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 0)
        col.label(text="                                ")
        box = col.box()
        box.menu("NODE_MT_add", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main"))
        text = [
            ("Frame"),
            ("Reroute"),
            ("Cryptomatte"),
            ("Bokeh Image"),
            ("Image"),
            ("Movie Clip"),
            ("Texture"),
            ("Time"),
            ("Track Position"),
            ("Composite"),
            ("File Output"),
            ("Levels"),
        ]
        icon = [
            (get_icon("Frame_icon", "main")), 
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("tex_icon", "main")),
            (get_icon("Reroute_icon", "main")),  
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("NodeFrame"),
            ("NodeReroute"),
            ("CompositorNodeCryptomatte"),
            ("CompositorNodeBokehImage"),
            ("CompositorNodeImage"),
            ("CompositorNodeMovieClip"),
            ("CompositorNodeTexture"),
            ("CompositorNodeTime"),
            ("CompositorNodeTrackPos"),
            ("CompositorNodeComposite"),
            ("CompositorNodeOutputFile"),
            ("CompositorNodeLevels"),
        ]
        op_loop_safe_node_val(col, 12, text, icon, e_type)
        col.label(text="                                ")

    def comp_menu_1(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 3)
        text = [
            ("Color Correction"),
            ("Blur"),
            ("Defocus"),
            ("Bokeh Blur"),
            ("Bilateral Blur"),
            ("Directional Blur"),
            ("Vector Blur"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodeColorCorrection"),
            ("CompositorNodeBlur"),
            ("CompositorNodeDefocus"),
            ("CompositorNodeBokehBlur"),
            ("CompositorNodeBilateralblur"),
            ("CompositorNodeDBlur"),
            ("CompositorNodeVecBlur"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)

    def comp_menu_2(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 3)

        text = [
            ("Alpha Over"),
            ("Hue Correct"),
            ("Gamma"),
            ("Bright/Contrast"),
            ("Invert"),
            ("Tonemap"),
            ("Z Combine"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
        ]
        e_type = [
            ("CompositorNodeAlphaOver"),
            ("CompositorNodeHueCorrect"),
            ("CompositorNodeGamma"),
            ("CompositorNodeBrightContrast"),
            ("CompositorNodeInvert"),
            ("CompositorNodeTonemap"),
            ("CompositorNodeZcombine"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)

    def comp_menu_3(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 3)

        text = [
            ("Color Balance"),
            ("Despeckle"),
            ("Dilate/Erode"),
            ("Filter"),
            ("Inpaint"),
            ("Pixelate"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodeColorBalance"),
            ("CompositorNodeDespeckle"),
            ("CompositorNodeDilateErode"),
            ("CompositorNodeFilter"),
            ("CompositorNodeInpaint"),
            ("CompositorNodePixelate"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)
    
    def comp_menu_4(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        
        text = [
            ("Render Layers"),
            ("Color Spill"),
            ("Color Key"),
            ("Channel Key"),
            ("Chroma Key"),
            ("Box Mask"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodeRLayers"),
            ("CompositorNodeColorSpill"),
            ("CompositorNodeColorMatte"),
            ("CompositorNodeChannelMatte"),
            ("CompositorNodeChromaMatte"),
            ("CompositorNodeBoxMask"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)
        spacer(col, 14)
    
    def comp_menu_5(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        
        text = [
            ("Difference Key"),
            ("Distance Key"),
            ("Double Edge Mask"),
            ("Keying"),
            ("Keying Screen"),
            ("Ellipse Mask"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodeDifMatte"),
            ("CompositorNodeDistanceMatte"),
            ("CompositorNodeDoubleEdgeMask"),
            ("CompositorNodeKeying"),
            ("CompositorNodeKeyingScreen"),
            ("CompositorNodeEllipseMask"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)
        spacer(col, 14)

    def comp_menu_6(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        
        text = [
            ("Map Value"),
            ("Normal"),
            ("Normalize"),
            ("Vector Curve"),
            ("Map Range"),
            ("Displace"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodeMapValue"),
            ("CompositorNodeNormal"),
            ("CompositorNodeNormalize"),
            ("CompositorNodeCurveVec"),
            ("CompositorNodeMapRange"),
            ("CompositorNodeDisplace"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)
        spacer(col, 14)

    def comp_menu_7(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        
        text = [
            ("Luminace Key"),
            ("Corner Pin"),
            ("Crop"),
            ("Flip"),
            ("Map UV"),
            ("Movie Distortion"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodeLumaMatte"),
            ("CompositorNodeCornerPin"),
            ("CompositorNodeCrop"),
            ("CompositorNodeFlip"),
            ("CompositorNodeMapUV"),
            ("CompositorNodeMovieDistortion"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)
        spacer(col, 14)

    def comp_menu_8(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        
        text = [
            ("Plane Track Deform"),
            ("Stabilize 2D"),
            ("Transform"),
            ("Scale"),
            ("Rotate"),
            ("Translate"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodePlaneTrackDeform"),
            ("CompositorNodeStabilize"),
            ("CompositorNodeTransform"),
            ("CompositorNodeScale"),
            ("CompositorNodeRotate"),
            ("CompositorNodeTranslate"),
        ]
        op_loop_safe_node_val(col, 6, text, icon, e_type)
        spacer(col, 14)

    def C9(self, col):
        col.scale_x = 1.81
        col.scale_y = 1.15
        text = [
            ("Alpha Convert"),
            ("Combine HSVA"),
            ("Combine RGBA"),
            ("Combine YCbCrA"),
            ("Combine YUVA"),
            ("Id Mask"),
            ("RGB To BW"),
            ("Separate HSVA"),
            ("Separate RGBA"),
            ("Separate YCbCrA"),
            ("Separate YUVA"),
            ("Set Alpha"),
            ("Switch View"),
            ("Viewer"),
            ("Math"),
            ("Color Ramp"),
            ("Value"),
            ("RGB Curve"),
            ("Mask"),
            ("Mix"),
            ("Glare"),
            ("Sun Beams"),
            ("Lens Distortion"),
            ("Hue Saturation"),
            ("Color Input"),
            ("Split Viewer"),
            ("Switch"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Math_icon", "main")),  
            (get_icon("Color_Ramp_icon", "main")),
            (get_icon("Value_icon", "main")),
            (get_icon("RGB_C_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Mix_Color_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Hue_icon", "main")),
            (get_icon("RGB_icon", "main")),
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")),
        ]
        e_type = [
            ("CompositorNodePremulKey"),
            ("CompositorNodeCombHSVA"),
            ("CompositorNodeCombRGBA"),
            ("CompositorNodeCombYCCA"),
            ("CompositorNodeCombYUVA"),
            ("CompositorNodeIDMask"),
            ("CompositorNodeRGBToBW"),
            ("CompositorNodeSepHSVA"),
            ("CompositorNodeSepRGBA"),
            ("CompositorNodeSepYCCA"),
            ("CompositorNodeSepYUVA"),
            ("CompositorNodeSetAlpha"),
            ("CompositorNodeSwitchView"),
            
            ("CompositorNodeViewer"),
            ("CompositorNodeMath"),
            ("CompositorNodeValToRGB"),
            ("CompositorNodeValue"),
            ("CompositorNodeCurveRGB"),
            ("CompositorNodeMask"),
            ("CompositorNodeMixRGB"),
            ("CompositorNodeGlare"),
            ("CompositorNodeSunBeams"),
            ("CompositorNodeLensdist"),
            ("CompositorNodeHueSat"),
            ("CompositorNodeRGB"),
            ("CompositorNodeSplitViewer"),
            ("CompositorNodeSwitch"),
        ]
        op_loop_safe_node_val(col, 26, text, icon, e_type)

class SM_Add_Texture_Node(bpy.types.Menu):
    bl_label = 'S.Menu Add Texture'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        
        if bpy.context.area.ui_type == "ShaderNodeTree":
            # 4 - LEFT
            split = pie.split()
            b = split.column()
            self.texture_1(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column()
            self.texture_3(b) 
            # 2 - BOTTOM
            split = pie.split()
            b = split.row()
            self.texture_2(b)      
            # 8 - TOP
            split = pie.split()
            b = split.row()
            self.texture_4(b) 

        elif bpy.context.area.ui_type == "TextureNodeTree":
            # 4 - LEFT
            split = pie.split()
            b = split.column()
            self.tex_texture_1(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column()
            self.tex_texture_2(b) 
            # 2 - BOTTOM
            split = pie.split()
            b = split.row()
            self.tex_texture_3(b)      
            # 8 - TOP
            split = pie.split()
            b = split.row()
            self.tex_texture_4(b)  
        
    def texture_1(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Gradient"),
            ("Point Density"),
            ("Sky"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeTexGradient"),
            ("ShaderNodeTexPointDensity"),
            ("ShaderNodeTexSky"),

        ]
        op_loop_safe_node(col, 3, text, icon, e_type)
    
    def texture_2(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Environment"),
            ("IES"),
            ("Image"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeTexEnvironment"),
            ("ShaderNodeTexIES"),
            ("ShaderNodeTexImage"),
        ]
        op_loop_safe_node(col, 3, text, icon, e_type)

    def texture_3(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Magic"),
            ("Musgrave"),
            ("Noise"),
            ("Voronoi"),
            ("Wave"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeTexMagic"),
            ("ShaderNodeTexMusgrave"),
            ("ShaderNodeTexNoise"),
            ("ShaderNodeTexVoronoi"),
            ("ShaderNodeTexWave"),
        ]
        op_loop_safe_node(col, 5, text, icon, e_type)

    def texture_4(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Bick"),
            ("Checker"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeTexBrick"),
            ("ShaderNodeTexChecker"),

        ]
        op_loop_safe_node(col, 2, text, icon, e_type)

    def tex_texture_1(self, col):

        col.scale_x = 1
        col.scale_y = 2
        text = [
            ("Clouds"),
            ("Stucci"),
            ("Voronoi"),

        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
        ]
        e_type = [
            ("TextureNodeTexClouds"),
            ("TextureNodeTexStucci"),
            ("TextureNodeTexVoronoi"),
        ]
        op_loop_safe_node_val(col, 3, text, icon, e_type)

    def tex_texture_2(self, col):

        col.scale_x = 1
        col.scale_y = 2
        text = [
            ("Magic"),
            ("Marble"),
            ("Musgrave"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
            (get_icon("Reroute_icon", "main")), 
        ]
        e_type = [
            ("TextureNodeTexMagic"),
            ("TextureNodeTexMarble"),
            ("TextureNodeTexMusgrave"),
        ]
        op_loop_safe_node_val(col, 3, text, icon, e_type)

    def tex_texture_3(self, col):

        col.scale_x = 1
        col.scale_y = 2
        text = [
            ("Blend"),
            ("Wood"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
        ]
        e_type = [
            ("TextureNodeTexBlend"),
            ("TextureNodeTexWood"),
        ]
        op_loop_safe_node_val(col, 2, text, icon, e_type)

    def tex_texture_4(self, col):

        col.scale_x = 1
        col.scale_y = 2

        text = [
            ("Distorted Noise"),
            ("Noise"),
        ]
        icon = [
            (get_icon("Reroute_icon", "main")),
            (get_icon("Reroute_icon", "main")), 
        ]
        e_type = [
            ("TextureNodeTexDistNoise"),
            ("TextureNodeTexNoise"),
        ]
        op_loop_safe_node_val(col, 2, text, icon, e_type)

class SM_PIE_Add_Node_Call(bpy.types.Operator):

    bl_idname = 'sop.sm_pie_node_add_call'
    bl_label = 'S.Menu Node Add Pie'
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_PIE_Add_Node")
        return {'FINISHED'}

class SM_Add_Shader_Node(bpy.types.Menu):
    bl_label = 'S.Menu Add Shader'
    
    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()

        # 4 - LEFT
        split = pie.split()
        b = split.column()
        self.shader_2(b)
        # 6 - RIGHT
        split = pie.split()
        b = split.column()
        self.shader_1(b)
        # 2 - BOTTOM
        split = pie.split()
        b = split.column()
        row = b.row()
        self.shader_3(row)
        # 8 - TOP
        split = pie.split()
        b = split.column()
        row = b.row()
        self.shader_4(row)

    def shader_1(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Principled"),
            ("Emission"),
            ("Volume Principled"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeBsdfPrincipled"),
            ("ShaderNodeEmission"),
            ("ShaderNodeVolumePrincipled"),
        ]
        op_loop_safe_node(col, 3, text, icon, e_type)

    def shader_2(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Diffuse"),
            ("SSS"),
            ("Glossy"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeBsdfDiffuse"),
            ("ShaderNodeSubsurfaceScattering"),
            ("ShaderNodeBsdfGlossy"),
        ]
        op_loop_safe_node(col, 3, text, icon, e_type)

    def shader_3(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Scatter"),
            ("Absorption"),
            ("Translucent"),
            ("Transparent"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeVolumeScatter"),
            ("ShaderNodeVolumeAbsorption"),
            ("ShaderNodeBsdfTranslucent"),
            ("ShaderNodeBsdfTransparent"),
        ]
        op_loop_safe_node(col, 4, text, icon, e_type)

    def shader_4(self, col): 
        col.scale_x = 1
        col.scale_y = 1.8
        text = [
            ("Specular"),
            ("Refraction"),
            ("Glass"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeEeveeSpecular"),
            ("ShaderNodeBsdfRefraction"),
            ("ShaderNodeBsdfGlass"),
        ]
        op_loop_safe_node(col, 3, text, icon, e_type)

class SM_PIE_Q_Menu(bpy.types.Menu):
    bl_label = "S.Menu 'Q' Menu"
    

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        if not bpy.context.selected_objects == []:

            if bpy.context.active_object.type == 'CURVE':
                # 4 - LEFT
                if get_prefs().enable_hops is True:
                    pie.operator("hops.adjust_curve",text="Adjust Curve", icon="ARROW_LEFTRIGHT")
                else:
                    pie.separator()
                # 6 - RIGHT
                pie.operator("object.convert",text="Convert", icon="OUTLINER_OB_MESH").target = "MESH"        
                # 2 - BOTTOM
                if get_prefs().enable_hops is True:
                    pie.menu("hops_main_menu", text="Hops Menu", icon_value=get_icon("List_icon", "main"))
                else:
                    pie.separator()
                # 8 - TOP
                pie.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
                # 7 - TOP - LEFT
                pie.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
                # 9 - TOP - RIGHT
                if get_prefs().enable_hops is True:
                    pie.operator("hops.helper",text="Hops Helper", icon_value=get_icon("Hops_helper_icon", "main"))
                else:
                    pie.separator()
                # 1 - BOTTOM - LEFT
                pie.separator()
                # 3 - BOTTOM - RIGHT
                pie.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
        
            elif bpy.context.active_object.type == 'EMPTY':
                # 4 - LEFT
                if get_prefs().enable_rarray is True:
                    if bpy.context.active_object.RA_Status is True:
                        split = pie.split()
                        b = split.column()
                        box = b.box()
                        box.scale_x = 1.1
                        box.scale_y = 1.5
                        box.operator("sop.r_array",text="(R) Array", icon_value=get_icon("RA_Icon", "main"))
                    else:
                        split = pie.split()
                        b = split.column()
                        box = b.box()
                        disabled_button(box, "(R) Array", get_icon("Reroute_icon", "main"))
                else:
                    pie.separator()
                # 6 - RIGHT
                split = pie.split()
                col = split.column()
                box = col.box()
                box.scale_x = 1.1
                box.scale_y = 1.5
                edv = box.operator("wm.context_modal_mouse",text="Adjust Empty Size", icon="ARROW_LEFTRIGHT")
                edv.data_path_iter = "selected_editable_objects"
                edv.data_path_item = "empty_display_size"
                edv.input_scale = 0.01
                # 2 - BOTTOM
                if get_prefs().enable_hops is True:
                    pie.menu("hops_main_menu", text="Hops Menu", icon_value=get_icon("List_icon", "main"))
                else:
                    pie.separator()
                # 8 - TOP
                pie.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
                # 7 - TOP - LEFT
                pie.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
                # 9 - TOP - RIGHT
                if get_prefs().enable_hops is True:
                    pie.operator("hops.helper",text="Hops Helper", icon_value=get_icon("Hops_helper_icon", "main"))
                else:
                    pie.separator()
                # 1 - BOTTOM - LEFT
                split = pie.split()
                col = split.column()
                box = col.box()
                box.scale_x = 1.1
                box.scale_y = 1.5
                ob = bpy.context.active_object
                box.prop(ob, "empty_display_type", text="Display As")
                # 3 - BOTTOM - RIGHT
                pie.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
            
            elif bpy.context.active_object.type == 'MESH':
                # 4 - LEFT
                split = pie.split()
                b = split.column_flow(columns=2,align=True)
                self.left_mesh_menu(b)
                # 6 - RIGHT
                split = pie.split()
                b = split.column_flow(columns=3,align=True)
                self.QA_02(b)
                # 2 - BOTTOM
                split = pie.split()
                b = split.column()
                self.QA_03(b)
                # 8 - TOP
                split = pie.split()
                b = split.column()
                if get_prefs().enable_hops is True:
                    b.menu("hops_main_menu", text="Hops Menu (Old)", icon_value=get_icon("List_icon", "main"))
                
                self.QA_01(b)
                # 7 - TOP - LEFT
                pie.separator()
                # 9 - TOP - RIGHT
                pie.separator()
                # 1 - BOTTOM - LEFT
                if get_prefs().enable_hops is True:
                    split = pie.split()
                    b = split.column(align=True)
                    self.mesh_menu_bottom_01(b)
                else:
                    pie.separator()
                # 3 - BOTTOM - RIGHT
                if get_prefs().enable_hops is True:
                    split = pie.split()
                    b = split.column(align=True)
                    self.mesh_menu_bottom_02(b)
                else:
                    pie.separator()
            
            elif bpy.context.active_object.type == 'CAMERA':
                # 4 - LEFT
                pie.separator()
                # 6 - RIGHT
                split = pie.split()
                b = split.column()
                self.camera_menu(b)
                # 2 - BOTTOM
                if get_prefs().enable_hops is True:
                    split = pie.split()
                    col = split.column()
                    col.label(text="                                    ")
                    box = col.box()
                    box.operator("hops.helper",text="Hops Helper", icon_value=get_icon("Hops_helper_icon", "main"))
                    box.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
                    box.menu("hops_main_menu", text="Hops Menu", icon_value=get_icon("List_icon", "main"))
                    box.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
                else:
                    split = pie.split()
                    col = split.column()
                    col.label(text="                                    ")
                    box = col.box()
                    box.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
                    box.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
                # 8 - TOP
                pie.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
                # 7 - TOP - LEFT
                split = pie.split()
                col = split.column()
                col.label(text="                                              ")
                box = col.box()
                box.scale_x = 1
                box.scale_y = 1.2
                edv = box.operator("wm.context_modal_mouse",text="Adjust Focus Distance", icon="ARROW_LEFTRIGHT")
                edv.data_path_iter = "selected_editable_objects"
                edv.data_path_item = "data.dof_distance"
                edv.input_scale = 0.01
                edv = box.operator("wm.context_modal_mouse",text="Adjust Passepartout", icon="ARROW_LEFTRIGHT")
                edv.input_scale = 0.001
                edv.data_path_iter = "selected_editable_objects"
                edv.data_path_item = "data.passepartout_alpha"
                edv = box.operator("wm.context_modal_mouse",text="Adjust Focal Length", icon="ARROW_LEFTRIGHT")
                edv.input_scale = 0.01
                edv.data_path_iter = "selected_editable_objects"
                edv.data_path_item = "data.lens"
                #edv.header_text = "test"
                edv = box.operator("wm.context_modal_mouse",text="Adjust F-Stop", icon="ARROW_LEFTRIGHT")
                edv.input_scale = 0.01
                edv.data_path_iter = "selected_editable_objects"
                edv.data_path_item = "data.gpu_dof.fstop"
            
                if get_prefs().enable_hops is True:
                    box.operator("hops.set_camera",text="Set Active Camera", icon="HIDE_OFF")
                # 9 - TOP - RIGHT
                pie.separator()
                # 1 - BOTTOM - LEFT
                split = pie.split()
                b = split.column()
                self.camera_menu_2(b)
                # 3 - BOTTOM - RIGHT
            
            elif bpy.context.active_object.type == 'LIGHT':
                # 4 - LEFT
                if get_prefs().enable_hops is True:
                    pie.operator("hops.helper",text="Hops Helper", icon_value=get_icon("Hops_helper_icon", "main"))
                else:
                    pie.separator()
                # 6 - RIGHT
                split = pie.split()
                col = split.column()
                self.lamp_menu(col)
                # 2 - BOTTOM
                if get_prefs().enable_hops is True:
                    pie.menu("hops_main_menu", text="Hops Menu", icon_value=get_icon("List_icon", "main"))
                else:
                    pie.separator()
                # 8 - TOP
                pie.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
                # 7 - TOP - LEFT
                pie.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
                # 9 - TOP - RIGHT
                pie.separator()
                # 1 - BOTTOM - LEFT
                pie.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
                # 3 - BOTTOM - RIGHT
                pie.separator()
            
            elif bpy.context.active_object.type == 'FONT':
                # 4 - LEFT
                split = pie.split()
                col = split.column()
                self.text_font_menu(col)
                # 6 - RIGHT
                split = pie.split()
                col = split.column()
                self.text_geo_menu(col)
                # 2 - BOTTOM
                if get_prefs().enable_hops is True:
                    split = pie.split()
                    col = split.column()
                    col.label(text="                                    ")
                    box = col.box()
                    box.operator("object.convert",text="Convert", icon="OUTLINER_OB_MESH").target = "MESH"
                    box.operator("hops.helper",text="Hops Helper", icon_value=get_icon("Hops_helper_icon", "main"))
                    box.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
                    box.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
                else:
                    split = pie.split()
                    col = split.column()
                    col.label(text="                                    ")
                    box = col.box()
                    box.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
                    box.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
                # 8 - TOP
                pie.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
                # 7 - TOP - LEFT
                pie.separator()
                # 9 - TOP - RIGHT
                pie.separator()
                # 1 - BOTTOM - LEFT
                pie.separator()
                # 3 - BOTTOM - RIGHT
                pie.separator()

            else:
                pie.separator()
                pie.separator()
                split = pie.split()
                disabled_button(split,"For Now", 2)
                split = pie.split()
                disabled_button(split,"Not Supported", 2)

        else:
            pie.separator()
            pie.separator()
            split = pie.split()
            split = pie.split()
            disabled_button(split,"No Object Selected", 2)



    def left_mesh_menu(self, col):
        col.scale_x = 1.9
        col.scale_y = 1.8

        enum = [
            ("view3d.bevel_multiplier"),
            ("hops.step"),
            ("hops.shrinkwrap2"),
            ("hops.reset_axis_modal"),
            ("hops.sphere_cast"),
        ]
        
        text = [
            ("Bevel multiplier"),
            ("Step"),
            ("Hops Shrink"),
            ("Reset Axis"),
            ("Sphere Cast"),
        ]
        icon = [
            get_icon("BevelMultiply", "main"),
            get_icon("Sstep", "main"),
            get_icon("ShrinkTo", "main"),
            get_icon("Xslap", "main"),
            get_icon("SphereCast", "main"),
        ]
        #spacer(col, 1 )
        if get_prefs().enable_hops is True:
            
            hops = True
            if col.operator("hops.xunwrap", text="Auto Unwrap",icon_value=get_icon("PUnwrap", "main")) is None:
                col.label(text="Hard Ops Not Installed")
                hops = False

            op_loop_val(col, enum, text, icon, 0, False)
            if hops is True:
                col.operator("hops.apply_modifiers", text="Smart Apply",icon_value=get_icon("Applyall", "main")).modifier_types = 'BOOLEAN'
                col.operator("hops.bool_toggle_viewport", text="Toggle Modifiers",icon_value=get_icon("Tris", "main")).all_modifiers = True
                op = col.operator("hops.modifier_scroll", text="Modifier Scroll",icon_value=get_icon("Diagonal", "main"))
                op.all = True
                op.additive = True
         
            
        if get_prefs().enable_rarray is True:
            if col.operator("sop.r_array", text="(R) Array",icon_value=get_icon("RA_Icon", "main")) is None:
                col.label(text="(R) Array Not Installed")

    def QA_01(self, col):
        col.scale_x = 1.1
        col.scale_y = 1.8
        col = col.row(align=True)
        enum = [
            ("hops.helper"),
            ("hops.mirror_gizmo"),
        ]
        text = [
            ("Hops Helper"),
            ("Hops Mirror"),
        ]
        icon = [
            get_icon("Hops_helper_icon", "main"),
            get_icon("Mirror_Icon", "main"),
        ]
        col.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
        if get_prefs().enable_hops is True:
            op_loop_val(col, enum, text, icon, 0, False)
    
    def QA_02(self, col):
        if get_prefs().enable_hops is True:
            col.scale_x = 1.4
            col.scale_y = 1.8
        else:
            col.scale_x = 1.4
            col.scale_y = 1.6
        #colunm 1
        obj = bpy.context.active_object.data
        col.prop(obj, "use_auto_smooth", text="Auto Smooth")
        hops = True
        if get_prefs().enable_hops is True: 
            if col.operator("hops.soft_sharpen",text="(S) Sharp", icon_value=get_icon("Ssharpen", "main")) is None:
                col.label(text="Not Installed")
                hops = False
            active_object = bpy.context.active_object
            if hops is True:    
                if active_object.hops.status in ("CSHARP", "CSTEP"):
                    col.operator("hops.adjust_bevel",text="(B) Width", icon_value=get_icon("AdjustBevel", "main"))
                else:
                    col.operator("hops.complex_sharpen",text="(C) Sharp", icon_value=get_icon("CSharpen", "main"))
        else:
            col.label(text="")
            col.label(text="")
        col.operator("object.subdivision_set",text="Subdiv (1)", icon="MOD_SUBSURF").level = 1
        col.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")
        #colunm 2
        col.operator("object.shade_smooth",text="Shade Smooth", icon_value=get_icon("Smooth_Shading_icon", "main"))
        if get_prefs().enable_hops is True:
            if col.operator("hops.adjust_tthick",text="Adjust (T) Thick", icon_value=get_icon("Tthick", "main")) is None:
                col.label(text="Not Installed")
            if col.operator("hops.adjust_array",text="Adjust Array", icon="ARROW_LEFTRIGHT") is None:
                col.label(text="Not Installed")
        else:
            col.label(text="")
            col.label(text="")
        col.operator("object.subdivision_set",text="(2)", icon="MOD_SUBSURF").level = 2
        if get_prefs().enable_hops is True:
            if col.operator("hops.reset_status",text="Reset Status", icon_value=get_icon("StatusReset", "main")) is None:
                col.label(text="Not Installed")
        else:
            col.label(text="")
        #colunm 3
        col.operator("object.shade_flat",text="Shade Flat", icon_value=get_icon("Flat_Shading_icon", "main"))
        if get_prefs().enable_hops is True:
            if col.operator("view3d.clean_mesh",text="Clean Mesh", icon_value=get_icon("FaceGrate", "main")) is None:
                col.label(text="Not Installed")
            if col.operator("hops.array_gizmo",text="Array Gizmo", icon_value=get_icon("Array", "main")) is None:
                col.label(text="Not Installed")
        else:
            col.label(text="")
            col.label(text="")
        col.operator("object.subdivision_set",text="(3)", icon="MOD_SUBSURF").level = 3
        if get_prefs().enable_hops is True:
            if col.operator("clean.sharps",text="Clean Sharps",icon_value=get_icon("CleansharpsE", "main")) is None:
                col.label(text="Not Installed")
        else:
            col.label(text="")

    def QA_03(self, col):
        col.scale_x = 1.4
        col.scale_y = 1.8
        col = col.row(align=True)
        enum = [
            ("wm.tool_set_by_id"),
            ("wm.tool_set_by_id"),
        ]
        text = [
            ("Select Box"),
            ("Cursor"),
        ]
        icon = [
            "RESTRICT_SELECT_OFF",
            "PIVOT_CURSOR",
        ]
        name = [
            ("builtin.select_box"),
            ("builtin.cursor"),
        ]
        
        if get_prefs().enable_box_cutter is True:
            if col.operator("bc.topbar_activate",text="Activate Box Cutter", icon_value=get_icon("BoxCutter", "main")) is None:
                col.label(text="Box Cutter Not Installed")
        op_loop_name(col, enum, text, icon, name)
    
    def mesh_menu_bottom_01(self, col):
        col.scale_x = 1.4
        col.scale_y = 1.8
        enum = [
            ("hops.bevel_helper"),
            ("view3d.status_helper_popup"),
            ("hops.sharp_manager"),
        ]
        text = [
            ("Bevel Helper"),
            ("Status Helper"),
            ("Sharp Manager"),
        ]
        icon = [
            get_icon("Xslap", "main"),
            get_icon("StatusOveride", "main"),
            get_icon("Diagonal", "main"),
        ]
  
        spacer(col, 9)
        if get_prefs().enable_hops is True:
            op_loop_val(col, enum, text, icon, 0, False)
        box = col.box()
        box.menu("SCREEN_MT_user_menu", text="Quick Favorites", icon_value=get_icon("List_icon", "main"))
    
    def mesh_menu_bottom_02(self, col):
        col.scale_x = 1.4
        col.scale_y = 1.8
        spacer(col, 8)
        col.operator_context = "INVOKE_DEFAULT"
        hops = True
        if col.operator("hops.bool_scroll_objects", text="Object Scroll", icon_value=get_icon("StatusReset", "main")) is None:
            col.label(text="Hard Ops Not Installed")
            hops = False
        if hops is True:
            op = col.operator("hops.modifier_scroll", text="Cycle Booleans", icon_value=get_icon("StatusOveride", "main"))
            op.additive = False
            op.type = 'BOOLEAN'

            op = col.operator("hops.modifier_scroll", text="Additive Scroll", icon_value=get_icon("Diagonal", "main"))
            op.additive = True
            op.type = 'BOOLEAN'

    def camera_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1
        col = col.box()
        
        
        obj = bpy.context.object.data
        dof_options = obj.gpu_dof
        col.prop(obj, "passepartout_alpha", text="Passepartout")
        col.prop(obj, "dof_object", text="Focus on Object")
        col.prop(obj, "dof_distance", text="Focus Distance")
        col.prop(dof_options, "fstop")
        col.prop(dof_options, "blades")
        col.prop(dof_options, "rotation")
        col.prop(dof_options, "ratio")


        split = col.split()
        split.prop_menu_enum(obj, "show_guide")

        col = col.column(align=True)

        col.separator()

        col.prop(obj, "display_size", text="Camera Display Size")

        col.separator()

        col.prop(obj, "show_limits", text="Limits")
        col.prop(obj, "show_mist", text="Mist")
        col.prop(obj, "show_sensor", text="Sensor")
        col.prop(obj, "show_name", text="Name")
    
    def camera_menu_2(self, col):
        col.scale_x = 1
        col.scale_y = 1
        spacer(col, 7)
        col = col.box()
        scene = bpy.context.scene
        cam = bpy.context.object.data
        col.label(text="Lens")
        col.prop(cam, "type")

        col = col.column()
        col.separator()

        if cam.type == 'PERSP':
            col = col.column()
            if cam.lens_unit == 'MILLIMETERS':
                col.prop(cam, "lens")
            elif cam.lens_unit == 'FOV':
                col.prop(cam, "angle")
            col.prop(cam, "lens_unit")

        elif cam.type == 'ORTHO':
            col.prop(cam, "ortho_scale")

        elif cam.type == 'PANO':
            engine = scene.render.engine
            if engine == 'CYCLES':
                ccam = cam.cycles
                col.prop(ccam, "panorama_type")
                if ccam.panorama_type == 'FISHEYE_EQUIDISTANT':
                    col.prop(ccam, "fisheye_fov")
                elif ccam.panorama_type == 'FISHEYE_EQUISOLID':
                    col.prop(ccam, "fisheye_lens", text="Lens")
                    col.prop(ccam, "fisheye_fov")
                elif ccam.panorama_type == 'EQUIRECTANGULAR':
                    sub = col.column(align=True)
                    sub.prop(ccam, "latitude_min", text="Latitude Min")
                    sub.prop(ccam, "latitude_max", text="Max")
                    sub = col.column(align=True)
                    sub.prop(ccam, "longitude_min", text="Longitude Min")
                    sub.prop(ccam, "longitude_max", text="Max")
            elif engine in {'BLENDER_RENDER', 'BLENDER_EEVEE', 'BLENDER_WORKBENCH'}:
                if cam.lens_unit == 'MILLIMETERS':
                    col.prop(cam, "lens")
                elif cam.lens_unit == 'FOV':
                    col.prop(cam, "angle")
                col.prop(cam, "lens_unit")

        col = col.column()
        col.separator()

        sub = col.column(align=True)
        sub.prop(cam, "shift_x", text="Shift X")
        sub.prop(cam, "shift_y", text="Y")

        col.separator()
        sub = col.column(align=True)
        sub.prop(cam, "clip_start", text="Clip Start")
        sub.prop(cam, "clip_end", text="End")

    def lamp_menu(self, col):
        scene = bpy.context.scene
        col = col.box()
        col.scale_x = 1
        col.scale_y = 1.4
        
        if scene.render.engine == 'BLENDER_EEVEE':
            light = bpy.context.object.data
            
            row = col.row()
            row.prop(light, "type", expand=True)
            
            col.prop(light, "color")
            col.prop(light, "energy")
            col.prop(light, "specular_factor", text="Specular")

            col.separator()

            if light.type in {'POINT', 'SPOT', 'SUN'}:
                col.prop(light, "shadow_soft_size", text="Radius")
            elif light.type == 'AREA':
                col.prop(light, "shape")

                sub = col.column(align=True)

                if light.shape in {'SQUARE', 'DISK'}:
                    sub.prop(light, "size")
                elif light.shape in {'RECTANGLE', 'ELLIPSE'}:
                    sub.prop(light, "size", text="Size X")
                    sub.prop(light, "size_y", text="Y")

        if scene.render.engine == 'CYCLES':
            light = bpy.context.object.data
            clamp = light.cycles
            row = col.row()
            row.prop(light, "type", expand=True)    
            if light.type in {'POINT', 'SUN', 'SPOT'}:
                col.prop(light, "shadow_soft_size", text="Size")
            elif light.type == 'AREA':
                col.prop(light, "shape", text="Shape")
                sub = col.column(align=True)
    
                if light.shape in {'SQUARE', 'DISK'}:
                    sub.prop(light, "size")
                elif light.shape in {'RECTANGLE', 'ELLIPSE'}:
                    sub.prop(light, "size", text="Size X")
                    sub.prop(light, "size_y", text="Y")
    
            sub = col.column(align=True)
            sub.active = not (light.type == 'AREA' and clamp.is_portal)
            sub.prop(clamp, "cast_shadow")
            sub.prop(clamp, "use_multiple_importance_sampling", text="Multiple Importance")
           
            if light.type == 'AREA':
                col.prop(clamp, "is_portal", text="Portal")
    
    def text_geo_menu(self, col):
        col = col.box()
        col.scale_x = 1
        col.scale_y = 1.2
        
        curve = bpy.context.object.data
        col.label(text="Geometry")
        sub = col.column()
        edv = sub.operator("wm.context_modal_mouse",text="Adjust Offset", icon="ARROW_LEFTRIGHT")
        edv.input_scale = 0.001
        edv.data_path_iter = "selected_objects"
        edv.data_path_item = "data.offset"

        
        sub.active = (curve.bevel_object is None)
        edv = sub.operator("wm.context_modal_mouse",text="Adjust Extrusion", icon="ARROW_LEFTRIGHT")
        edv.input_scale = 0.001
        edv.data_path_iter = "selected_objects"
        edv.data_path_item = "data.extrude"

        col.prop(curve, "taper_object")

        sub = col.column()
        sub.active = curve.taper_object is not None
        sub.prop(curve, "use_map_taper")

        sub.label(text="Bevel")
        sub.active = (curve.bevel_object is None)
        edv = sub.operator("wm.context_modal_mouse",text="Adjust Bevel Depth", icon="ARROW_LEFTRIGHT")
        edv.input_scale = 0.001
        edv.data_path_iter = "selected_objects"
        edv.data_path_item = "data.bevel_depth"
        edv = sub.operator("wm.context_modal_mouse",text="Adjust Bevel Resolution", icon="ARROW_LEFTRIGHT")
        edv.input_scale = 0.1
        edv.data_path_iter = "selected_objects"
        edv.data_path_item = "data.bevel_resolution"
        col.prop(curve, "bevel_object", text="Bevel Object")
        sub = col.column()
        sub.active = curve.bevel_object is not None
        sub.prop(curve, "use_fill_caps")
        col.label(text="Shape")
        sub = col.column(align=True)
        sub.prop(curve, "resolution_u", text="Resolution Preview U")
        sub = col.column(align=True)
        sub.prop(curve, "render_resolution_u", text="Render U")
        col.prop(curve, "use_fast_edit", text="Fast Editing")
        sub = col.column()
        sub.active = (curve.dimensions == '2D' or (curve.bevel_object is None and curve.dimensions == '3D'))
        sub.prop(curve, "fill_mode")
        col.prop(curve, "use_fill_deform")
        
    def text_font_menu(self, col):
        col = col.box()
        col.scale_x = 1
        col.scale_y = 1.2


        text = bpy.context.object.data
        char = bpy.context.object.data.edit_format

        row = col.split(factor=0.25)
        row.label(text="Regular")
        row.template_ID(text, "font", open="font.open", unlink="font.unlink")
        row = col.split(factor=0.25)
        row.label(text="Bold")
        row.template_ID(text, "font_bold", open="font.open", unlink="font.unlink")
        row = col.split(factor=0.25)
        row.label(text="Italic")
        row.template_ID(text, "font_italic", open="font.open", unlink="font.unlink")
        row = col.split(factor=0.25)
        row.label(text="Bold & Italic")
        row.template_ID(text, "font_bold_italic", open="font.open", unlink="font.unlink")

        col.separator()

        row = col.row(align=True)
        row.prop(char, "use_bold", toggle=True)
        row.prop(char, "use_italic", toggle=True)
        row.prop(char, "use_underline", toggle=True)
        row.prop(char, "use_small_caps", toggle=True)

class SM_PIE_Q_Menu_Call(bpy.types.Operator):
    bl_idname = 'sop.sm_pie_q_menu_call'
    bl_label = 'S.Menu Q Menu Pie'
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_PIE_Q_Menu")
        return {'FINISHED'}

class SM_PIE_A_OM(bpy.types.Menu):
    bl_label = "S.Menu 'A' Menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        # 4 - LEFT
        pie.operator("object.select_all",text="Select All", icon_value=get_icon("O_Selcet_icon", "main")).action = 'SELECT'
        # 6 - RIGHT
        pie.operator("object.select_all",text="Deselect All", icon_value=get_icon("O_DeSelcet_icon", "main")).action = 'DESELECT'
        # 2 - BOTTOM
        pie.operator("wm.call_menu",text="Apply Menu", icon_value=get_icon("List_icon", "main")).name = "VIEW3D_MT_object_apply"
        # 8 - TOP
        pie.operator("object.select_all",text="Invert", icon="ARROW_LEFTRIGHT").action = 'INVERT'
            
class SM_PIE_A_OM_Call(bpy.types.Operator):
    bl_idname = 'sop.sm_pie_a_menu_call'
    bl_label = "S.Menu 'A' Menu"
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_PIE_A_OM")
        return {'FINISHED'}

class SM_PIE_A_NODE(bpy.types.Menu):
    bl_label = "S.Menu 'A' Node Menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        
        # 4 - LEFT
        pie.operator("node.select_all",text="Select All", icon_value=get_icon("O_Selcet_icon", "main")).action = 'SELECT'
        # 6 - RIGHT
        pie.operator("node.select_all",text="Deselect All", icon_value=get_icon("O_DeSelcet_icon", "main")).action = 'DESELECT'
        # 2 - BOTTOM
        pie.operator("wm.tool_set_by_id",text="Annotate", icon="GREASEPENCIL").name = 'builtin.annotate'
        # 8 - TOP
        pie.operator("node.select_all",text="Invert Selection", icon="ARROW_LEFTRIGHT").action = 'INVERT'
        # 7 - TOP - LEFT
        pie.operator("wm.tool_set_by_id",text="Select", icon="RESTRICT_SELECT_OFF").name = 'builtin.select'
        # 9 - TOP - RIGHT
        pie.operator("wm.tool_set_by_id",text="Annotate Eraser", icon="BRUSH_DATA").name = 'builtin.annotate_eraser'
        # 1 - BOTTOM - LEFT
        pie.operator("wm.tool_set_by_id",text="Select Box", icon="SHADING_BBOX").name = 'builtin.select_box'
        # 3 - BOTTOM - RIGHT
        pie.operator("wm.tool_set_by_id",text="Links Cut", icon="SCULPTMODE_HLT").name = 'builtin.links_cut'
            
class SM_PIE_A_NODE_Call(bpy.types.Operator):
    bl_idname = 'sop.sm_pie_a_node_menu_call'
    bl_label = "S.Menu 'A' Node Menu"
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_PIE_A_NODE")
        return {'FINISHED'}

class SM_PIE_Q_Node(bpy.types.Menu):
    bl_label = "S.Menu 'Q' Node Menu"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        if bpy.context.area.ui_type == "CompositorNodeTree":
            # 4 - LEFT
            split = pie.split()
            col = split.column()
            self.comp_q_04(col)
            # 6 - RIGHT
            split = pie.split()
            col = split.column()
            self.comp_q_01(col)
            # 2 - BOTTOM
            split = pie.split()
            col = split.column()
            self.comp_q_02(col)
            # 8 - TOP
            split = pie.split()
            col = split.column()
            self.comp_q_03(col)
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            split = pie.split()
            col = split.column()
            self.comp_q_06(col)
            # 3 - BOTTOM - RIGHT
            split = pie.split()
            col = split.column()
            self.comp_q_05(col)
        elif bpy.context.area.ui_type == "ShaderNodeTree":
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            split = pie.split()
            split.label(text="WIP", icon="ERROR")
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()
        
        elif bpy.context.area.ui_type == "TextureNodeTree":
            # 4 - LEFT
            pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            split = pie.split()
            split.label(text="WIP", icon="ERROR")
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()

    def comp_q_01(self, col):
        col.scale_x = 1.1
        col.scale_y = 2
        
        snode = bpy.context.space_data

        box = col.box()
        box.prop(snode, "show_backdrop", text="Backdrop", emboss=False)

        box.active = snode.show_backdrop

        box.operator("sop.sm_modal_adjust_view", text="Adjust Backdrop", icon="PREFERENCES")

        box.operator("node.backimage_fit", text="Fit Backdrop", icon="OBJECT_DATA")
    
    def comp_q_02(self, col):
        col.scale_x = 1.1
        col.scale_y = 1.2
        spacer(col, 1)

        snode = bpy.context.space_data
        snode_id = snode.id
        tree = snode.node_tree
        box = col.box()
        
        box.label(text="Performance:")
        box = box.column()
        if snode_id:
            box.prop(snode_id, "use_nodes")
        box.prop(snode, "use_auto_render")
        box.prop(tree, "render_quality", text="Render")
        box.prop(tree, "edit_quality", text="Edit")
        box.prop(tree, "chunk_size")

        box = box.column()
        box.prop(tree, "use_opencl")
        box.prop(tree, "use_groupnode_buffer")
        box.prop(tree, "use_two_pass")
        box.prop(tree, "use_viewer_border")

    def comp_q_03(self, col):
        col.scale_x = 1.1
        col.scale_y = 1.2
        
        node = bpy.context.active_node

        box = col.box()
        

        box.label(text="Node:")
        box.prop(node, "name")
        box.prop(node, "label")

        box.prop(node, "use_custom_color", text="Color", emboss=False)
        sub = box.column()
        sub.enabled = node.use_custom_color
        sub.prop(node, "color", text="")
        sub.operator("node.node_copy_color", text="", icon='COPYDOWN') #? useless
    
    def comp_q_04(self, col):
        col.scale_x = 1.1
        col.scale_y = 1.6

        box = col.box()

        box.operator("node.toolbar", text="Toggle Shelf", icon='MENU_PANEL')
        box.operator("screen.screen_full_area", text="Toggle Maximize Area", icon='WINDOW')
        box.operator("node.properties", text="Toggle Sidebar", icon='MENU_PANEL')

    def comp_q_05(self, col):
        col.scale_x = 2
        col.scale_y = 1.8
        spacer(col, 1)
        #box = col.box()
        tool_settings = bpy.context.tool_settings
        row = col.row(align=True)
        row.prop(tool_settings, "use_snap", text="")
        row.prop(tool_settings, "snap_node_element", icon_only=True)
        if tool_settings.snap_node_element != 'GRID':
            row.prop(tool_settings, "snap_target", text="")

    def comp_q_06(self, col):
        col.scale_x = 2
        col.scale_y = 1.8
        spacer(col, 1)
     
        col.operator("node.tree_path_parent", text="", icon='FILE_PARENT')

class SM_PIE_Q_Node_Call(bpy.types.Operator):

    bl_idname = 'sop.sm_pie_q_node_menu_call'
    bl_label = "S.Menu 'Q' Node Menu"
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_PIE_Q_Node")
        return {'FINISHED'}

class SM_PIE_Tab_Menu(bpy.types.Menu):
    bl_label = "S.Menu 'Tab' Menu"
    
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("object.mode_set",text="Object Mode", icon="OBJECT_DATAMODE").mode = 'OBJECT'
        # 6 - RIGHT
        pie.operator("sop.sm_mesh_switch_to_edit_mode",text="Edit Mode", icon="EDITMODE_HLT")
        # 2 - BOTTOM
        pie.operator("object.mode_set",text="Sculpt Mode", icon="SCULPTMODE_HLT").mode = 'SCULPT'
        # 8 - TOP
        pie.operator("object.mode_set",text="Vertex Paint", icon="WPAINT_HLT").mode = 'VERTEX_PAINT'
        # 7 - TOP - LEFT
        pie.operator("object.mode_set",text="Weight Paint", icon="WPAINT_HLT").mode = 'WEIGHT_PAINT'
        # 9 - TOP - RIGHT
        pie.operator("object.mode_set",text="Texture Paint", icon="TPAINT_HLT").mode = 'TEXTURE_PAINT'
        # 1 - BOTTOM - LEFT
        pie.separator()
        # 3 - BOTTOM - RIGHT
        if bpy.context.active_object.SM_MH_Parent is None:
            pie.separator()
        else:
            if bpy.context.mode == "EDIT_MESH":
                pie.separator()
            else:
                if bpy.context.active_object.SM_MH_current_index == 0:
                    pie.separator()
                else:
                    pie.operator("object.mode_set",text="Edit Instance", icon="EDITMODE_HLT").mode = 'EDIT'

class SM_PIE_Tab_Menu_Call(bpy.types.Operator):

    bl_idname = 'sop.sm_pie_tab_menu_call'
    bl_label = "S.Menu 'Tab' Menu"
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_PIE_Tab_Menu")
        return {'FINISHED'}