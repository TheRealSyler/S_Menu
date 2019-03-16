import bpy, os
from . get_icon import get_icon

# todo add Extra Object (Curve) support
# todo Q Menu

#+-----------------------------------------------------------------------------------------------------+#
#? Utils
#+-----------------------------------------------------------------------------------------------------+#

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
        b = split.column()
        self.add_mesh_box(b)

        # 6 - RIGHT
        split = pie.split()
        b = split.column()
        column = split.column()
        self.forces(column, 0)
        self.curve(b, 2)
        
        # 2 - BOTTOM
        split = pie.split()
        if get_prefs().enable_extra_objects_mesh is True:
            b = split.column()
            self.extra_objects(b)
        b = split.column()
        self.camera(b, 3)

        column = split.column()
        self.empty(column, 3)
        
        # 8 - TOP
        split = pie.split()
        column = split.column()
        self.light_2_box(column, 3)
        
        b = split.column()
        self.light_1_box(b)

        column = split.column()
        self.bone(column)
        
        # 7 - TOP - LEFT
        pie.separator()
        # 9 - TOP - RIGHT
        pie.separator()
        # 1 - BOTTOM - LEFT
        pie.separator()
        # 3 - BOTTOM - RIGHT
        split = pie.split()
        column = split.column()
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
        col.scale_y = 1.4
        spacer(col, 3)
        col.operator("wm.call_menu", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main")).name = "VIEW3D_MT_add"
        
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
        col.operator("wm.call_menu",text="Extras", icon_value=get_icon("List_icon", "main")).name = "VIEW3D_MT_mesh_extras_add"
        col.operator("wm.call_menu",text="Math Function", icon_value=get_icon("List_icon", "main")).name = "VIEW3D_MT_mesh_math_add"
        col.operator("wm.call_menu",text="Mechanical", icon_value=get_icon("List_icon", "main")).name = "VIEW3D_MT_mesh_mech_add"
        col.operator("wm.call_menu",text="Torus Objects", icon_value=get_icon("List_icon", "main")).name = "VIEW3D_MT_mesh_torus_add"

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
            b = split.column()
            self.comp_node_utils(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column()
            self.comp_add_menu(b)
            # 2 - BOTTOM
            split = pie.split()
            b = split.column()
            self.comp_menu_3(b)
            b = split.column()
            self.comp_menu_2(b)
            b = split.column()
            self.comp_menu_1(b)
            # 8 - TOP
            split = pie.split()
            self.search(split)
            # 7 - TOP - LEFT
            split = pie.split()
            b = split.column()
            b.label(text="                            ")
            b = split.column()
            self.comp_menu_6(b)
            b = split.column()
            self.comp_menu_8(b)
            # 9 - TOP - RIGHT
            split = pie.split()
            b = split.column()
            self.comp_menu_4(b)
            b = split.column()
            self.comp_menu_5(b)
            b = split.column()
            self.comp_menu_7(b)
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()
        # check if in Texture node tree
        elif bpy.context.area.ui_type == "TextureNodeTree":
            # 4 - LEFT
            split = pie.split()
            b = split.column()
            self.tex_node_utils(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column()
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
            b = split.column()
            self.node_utils(b)
            # 6 - RIGHT
            split = pie.split()
            b = split.column()
            self.shader_add(b)
            # 2 - BOTTOM
            split = pie.split()
            b = split.column()
            self.node_color(b)
            b = split.column()
            self.node_vector(b)
            b = split.column()
            # note: dont change the text
            b.label(text="                                             ")
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
            column = split.column()
            self.add_menu(column)
            column = split.column()
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
        col.operator("sop.sm_texture_node_call", text="Texture", icon="TEXTURE")
    
    def shader_add(self, col):
        col.scale_x = 1.1
        col.scale_y = 1.8
        col.operator("sop.sm_shader_node_call", text="Shader", icon="SHADING_RENDERED")
    
    def add_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 9)
        col.operator("wm.call_menu", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main")).name = "NODE_MT_add"
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
        op_loop_safe_node_val(col, 11, text, icon, e_type)
    
    def add_menu_tex(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        col.operator("wm.call_menu", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main")).name = "NODE_MT_add"
       
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
        spacer(col, 3)
        op_loop_safe_node_val(col, 10, text, icon, e_type)
    
    def comp_add_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        spacer(col, 0)
        col.operator("wm.call_menu", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main")).name = "NODE_MT_add"
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
        spacer(col, 0)

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
            ("Map Range"),
            ("Map Value"),
            ("Normal"),
            ("Normalize"),
            ("Vector Curve"),
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
            ("CompositorNodeMapRange"),
            ("CompositorNodeMapValue"),
            ("CompositorNodeNormal"),
            ("CompositorNodeNormalize"),
            ("CompositorNodeCurveVec"),
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

class SM_Add_Texture_Node_Call(bpy.types.Operator):
    bl_idname = 'sop.sm_texture_node_call'
    bl_label = 'S.Menu Texture Add Pie'
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_Add_Texture_Node")
        return {'FINISHED'}

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

class SM_Add_Shader_Node_Call(bpy.types.Operator):
    bl_idname = 'sop.sm_shader_node_call'
    bl_label = 'S.Menu Shader Add Pie'
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}
    
    
    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="SM_Add_Shader_Node")
        return {'FINISHED'}

class SM_PIE_Q_Menu(bpy.types.Menu):
    bl_label = "Q Menu"
    

    def draw(self, context):
        layout = self.layout
        print (bpy.context.active_object.type)
        pie = layout.menu_pie()
        
        
        if bpy.context.active_object.type == 'CURVE':
            # 4 - LEFT
            if get_prefs().enable_hops is True:
                pie.operator("hops.adjust_curve",text="Adjust Curve", icon="ARROW_LEFTRIGHT")
            else:
                pie.separator()
            # 6 - RIGHT
            pie.operator("object.convert",text="Convert", icon="OUTLINER_OB_MESH").target = "MESH"        
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
            # 7 - TOP - LEFT
            pie.operator("wm.call_menu",text="Quick Favorites", icon_value=get_icon("List_icon", "main")).name = "SCREEN_MT_user_menu"
            # 9 - TOP - RIGHT
            if get_prefs().enable_hops is True:
                pie.operator("hops.helper",text="Hops Helper", icon_value=get_icon("Hops_helper_icon", "main"))
            else:
                pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")

        if bpy.context.active_object.type == 'EMPTY':
            # 4 - LEFT
            if get_prefs().enable_rarray is True:
                pie.operator("sop.r_array",text="(R) Array", icon_value=get_icon("RA_Icon", "main"))
            else:
                pie.separator()
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            pie.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
            # 7 - TOP - LEFT
            pie.operator("wm.call_menu",text="Quick Favorites", icon_value=get_icon("List_icon", "main")).name = "SCREEN_MT_user_menu"
            # 9 - TOP - RIGHT
            if get_prefs().enable_hops is True:
                pie.operator("hops.helper",text="Hops Helper", icon_value=get_icon("Hops_helper_icon", "main"))
            else:
                pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.operator("anim.keyframe_insert_menu",text="Insert Keyframe", icon="KEYTYPE_KEYFRAME_VEC")

        if bpy.context.active_object.type == 'MESH':
            # 4 - LEFT
            split = pie.split()
            b = split.column()
            self.left_mesh_menu(b)
            # 6 - RIGHT
            pie.separator()
            # 2 - BOTTOM
            pie.separator()
            # 8 - TOP
            split = pie.split()
            row = split.row()
            self.QA_01(row)
            # 7 - TOP - LEFT
            pie.separator()
            # 9 - TOP - RIGHT
            pie.separator()
            # 1 - BOTTOM - LEFT
            pie.separator()
            # 3 - BOTTOM - RIGHT
            pie.separator()
        
    def left_mesh_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.8
        
        if get_prefs().enable_rarray is True:
            col.operator("sop.r_array", text="(R) Array",icon_value=get_icon("RA_Icon", "main"))

        enum = [
            ("hops.reset_axis_modal"),
            ("hops.reset_status"),
            ("hops.slash"),
            ("hops.sphere_cast"),
        ]
        
        text = [
            ("Reset Axis"),
            ("Reset Status"),
            ("Slash"),
            ("Sphere Cast"),
        ]
        icon = [
            get_icon("Xslap", "main"),
            get_icon("StatusReset", "main"),
            get_icon("Csplit", "main"),
            get_icon("SphereCast", "main"),
        ]
        
        if get_prefs().enable_hops is True:
            op_loop_val(col, enum, text, icon, 0, False)

    def QA_01(self, col):
        col.scale_x = 1
        col.scale_y = 1.8

        enum = [
            ("hops.helper"),
            ("hops.mirror_gizmo"),
        ]
        text = [
            ("Hops Helper"),
            ("Hops Mirror(broken?!)"),
        ]
        icon = [
            get_icon("Hops_helper_icon", "main"),
            get_icon("Mirror_Icon", "main"),
        ]
        col.operator("wm.search_menu",text="Search", icon="VIEWZOOM")
        if get_prefs().enable_kitops is True:
            col.operator("view3d.insertpopup", text="Kit Ops",icon_value=get_icon("Insert", "main"))
        if get_prefs().enable_hops is True:
            op_loop_val(col, enum, text, icon, 0, False)

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