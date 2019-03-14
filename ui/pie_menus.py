import bpy
from .get_icon import get_icon


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

def op_loop_safe_node(col, enum, text, icon, type):
    for index, e in enumerate(enum):
        op = col.operator(e, text=text[index],icon=icon[index])
        op.type = type[index]
        op.use_transform = True

def spacer(col, num):
    for i in range(0, num):
        col.label(text="")

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
        self.curve(b, 3)
        
        # 2 - BOTTOM
        split = pie.split()
        
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
        self.add_menu(split)

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
            ("mesh.primitive_grid_add"),
            ("mesh.primitive_monkey_add"),
            ("mesh.add_mesh_rock"),
            ("mesh.landscape_add"),
            ("mesh.bolt_add"),

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
            ("Grid"),
            ("Monkey"),
            ("Rock Generator"),
            ("Landscape"),
            ("Bolt"),
        
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
            get_icon("Grid_icon", "main"),
            get_icon("Monkey_icon", "main"),
            get_icon("Rock_icon", "main"),
            get_icon("Landscape_icon", "main"),
            get_icon("Bolt_icon", "main"),
        ]

        op_loop_val(col, enum, text, icon, False, 7)

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
        
        spacer(col, snum)
        op_loop(col, enum, text, icon, True, 2)

    def add_menu(self, col):
        col.scale_x = 1
        col.scale_y = 1.4
        col.operator("wm.call_menu", text="Add Menu (Old)", icon_value=get_icon("List_icon", "main")).name = "VIEW3D_MT_add"

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

        # 4 - LEFT
        split = pie.split()
        b = split.column()
        self.node_utils(b)
        # 6 - RIGHT
        pie.separator()
        # 2 - BOTTOM
        pie.separator()      
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
        pie.separator()

    def node_utils(self, col):
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
        ]
        text = [
            ("Math"),
            ("Mix"),
            ("Color Ramp"),
            ("Value"),
            ("RGB Curve"),
            ("Mix Shader"),
            ("Add Shader"),
            ("Layer Weight"),
            ("Hue Saturation"),
        ]
        icon = [
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
            ("ERROR"),
        ]
        e_type = [
            ("ShaderNodeMath"),
            ("ShaderNodeMixRGB"),
            ("ShaderNodeValToRGB"),
            ("ShaderNodeValue"),
            ("ShaderNodeRGBCurve"),
            ("ShaderNodeMixShader"),
            ("ShaderNodeAddShader"),
            ("ShaderNodeLayerWeight"),
            ("ShaderNodeHueSaturation"),
        ]
        
        op_loop_safe_node(col, enum, text, icon, e_type)

    def search(self, col):
        col.scale_x = 1.4
        col.scale_y = 2
        col.operator("node.add_search", text="Search", icon="VIEWZOOM")

    def texture_add(self, col):
        col.scale_x = 1.4
        col.scale_y = 1.8
        col.operator("sop.sm_sdd_texture_node_call", text="Texture", icon="TEXTURE")

class SM_Add_Texture_Node(bpy.types.Menu):
    bl_label = 'S.Menu Add Texture'

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

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

        
    def texture_1(self, col): 
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
        ]
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
        op_loop_safe_node(col, enum, text, icon, e_type)
    
    def texture_2(self, col): 
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),

        ]
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
        op_loop_safe_node(col, enum, text, icon, e_type)

    def texture_3(self, col): 
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
            ("node.add_node"),
        ]
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
        op_loop_safe_node(col, enum, text, icon, e_type)

    def texture_4(self, col): 
        col.scale_x = 1
        col.scale_y = 1.2
        enum = [
            ("node.add_node"),
            ("node.add_node"),
        ]
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
        op_loop_safe_node(col, enum, text, icon, e_type)

class SM_Add_Texture_Node_Call(bpy.types.Operator):
    bl_idname = 'sop.sm_sdd_texture_node_call'
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
