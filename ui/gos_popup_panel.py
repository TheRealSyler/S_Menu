import bpy

from bl_ui.space_view3d import (
    VIEW3D_PT_shading,
    VIEW3D_PT_shading_lighting,
    VIEW3D_PT_shading_color,
    VIEW3D_PT_shading_options,
    VIEW3D_PT_overlay_gizmo,
    VIEW3D_PT_overlay_guides,
    VIEW3D_PT_overlay_object,
    VIEW3D_PT_overlay_geometry,
    VIEW3D_PT_overlay_motion_tracking,
    VIEW3D_PT_overlay_edit_mesh,
    VIEW3D_PT_overlay_edit_mesh_shading,
    VIEW3D_PT_overlay_edit_mesh_measurement,
    VIEW3D_PT_overlay_edit_mesh_normals,
    VIEW3D_PT_overlay_edit_mesh_freestyle,
    VIEW3D_PT_overlay_edit_mesh_developer,
    VIEW3D_PT_overlay_edit_curve,
    VIEW3D_PT_overlay_paint,
    VIEW3D_PT_overlay_pose,
    VIEW3D_PT_overlay_sculpt
)


class GOS_Props(bpy.types.PropertyGroup):
    SM_GOS_gaffer_tabs: bpy.props.EnumProperty(
        name="Gaffer Tabs", 
        items=(
            ("LIGHTS","Lights",""),
            ("TOOLS","Tools",""),
            ("OVERLAYS","Overlays",""),
            ("SHADING","Shading",""),
        )
    )
    SM_GOS_tabs: bpy.props.EnumProperty(
        name="GOS Tabs", 
        items=(
            ("OVERLAYS","Overlays",""),
            ("SHADING","Shading",""),
        )
    )
    SM_GOS_test: bpy.props.BoolProperty(name="test", default=True)

class SM_OT_GOS_Popup(bpy.types.Operator):
    bl_idname = 'sop.sm_gos_popup'
    bl_description = 'test'
    bl_label = 'GOS Popup'

    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context): 
        return True


    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self, width=350)


    def execute(self, context):
        return {'FINISHED'}
    
    
    
    def draw(self, context):
        layout = self.layout
        layout.operator("sop.sm_render_settings_popup", icon="SCENE")
        
        view = context.space_data
        scene = context.scene
        gos_props = scene.SM_GOS_Props

    
        if hasattr(scene, "gaf_props"):
            gaf_props = scene.gaf_props
            gaf = True
            tabs = gos_props.SM_GOS_gaffer_tabs
        else:
            tabs =gos_props.SM_GOS_tabs
            gaf = False

        row = layout.row(align=True)
        if hasattr(view, "overlay"):
            overlay = view.overlay
            row.prop(overlay, "show_overlays", icon='OVERLAY', text="")
            #row.popover(panel="VIEW3D_PT_overlay")

        if hasattr(view, "shading"):
            shading = view.shading
            #row.label(text="Shading:")
            if shading.type == 'WIREFRAME':
                row.prop(shading, "show_xray_wireframe", text="", icon='XRAY')
            else:
                row.prop(shading, "show_xray", text="", icon='XRAY')

            row.prop(shading, "type", text=" ", expand=True)
            #row.popover(panel="VIEW3D_PT_shading")

        if gaf is True:
            layout.prop(gos_props, "SM_GOS_gaffer_tabs", expand=True)

            if tabs == "LIGHTS":
                if context.scene.render.engine == "CYCLES":
                    layout.prop(gaf_props, 'hdri_handler_enabled', text="Enable Gaffer HDRI")
                bpy.types.GAFFER_PT_lights.draw(self, context)

            if tabs == "TOOLS":
                bpy.types.GAFFER_PT_tools.draw(self, context)
        else:
            layout.prop(gos_props, "SM_GOS_tabs", expand=True)


        if tabs == "OVERLAYS":
            if view.type == "VIEW_3D":
                layout.prop(view, "show_gizmo")
                VIEW3D_PT_overlay_gizmo.draw(self, context)
                layout.label(text="Guides")
                VIEW3D_PT_overlay_guides.draw(self, context)
                layout.label(text="Object")
                VIEW3D_PT_overlay_object.draw(self, context)
                layout.label(text="Geometry")
                VIEW3D_PT_overlay_geometry.draw(self, context)
                layout.separator()
                layout.prop(view, "show_reconstruction", text="Motion Tacking")
                VIEW3D_PT_overlay_motion_tracking.draw(self, context)

                if context.mode == "EDIT_MESH":
                    layout.label(text="Mesh:") 
                    VIEW3D_PT_overlay_edit_mesh.draw(self, context)
                    VIEW3D_PT_overlay_edit_mesh_shading.draw(self, context)
                    VIEW3D_PT_overlay_edit_mesh_measurement.draw(self, context)
                    VIEW3D_PT_overlay_edit_mesh_normals.draw(self, context)
                    VIEW3D_PT_overlay_edit_mesh_freestyle.draw(self, context)
                    VIEW3D_PT_overlay_edit_mesh_developer.draw(self, context)
                if context.mode == "EDIT_CURVE":
                    layout.label(text="Curve:")  
                    VIEW3D_PT_overlay_edit_curve.draw(self, context)
                if context.mode in {'PAINT_WEIGHT', 'PAINT_VERTEX', 'PAINT_TEXTURE'}: 
                    VIEW3D_PT_overlay_paint.draw_header(self, context)
                    VIEW3D_PT_overlay_paint.draw(self, context)
                if context.mode == "POSE": 
                    layout.label(text="Pose Mode")
                    VIEW3D_PT_overlay_pose.draw(self, context)
                if context.mode == "SCULPT": 
                    layout.label(text="Sculpt")
                    VIEW3D_PT_overlay_sculpt.draw(self, context)
            else:
                layout.label(text="Not in 3D View")

        if tabs == "SHADING":
            if hasattr(view, "shading"):
                shading = view.shading
                if shading.type in {'SOLID', 'MATERIAL'}:
                    layout.label(text="Lighting")
                    VIEW3D_PT_shading_lighting.draw(self, context)

                if shading.type in {'WIREFRAME', 'SOLID'}:
                    layout.label(text="Color")
                    #VIEW3D_PT_shading_color.draw(self, context)
                    shading = VIEW3D_PT_shading.get_shading(context)
                    if shading.type == 'WIREFRAME':
                        layout.row().prop(shading, "wireframe_color_type", expand=True)
                    else:
                        VIEW3D_PT_shading_color._draw_color_type(self, context)
                        layout.separator()
                    VIEW3D_PT_shading_color._draw_background_color(self, context)

                layout.label(text="Options")
                VIEW3D_PT_shading_options.draw(self, context)
            else:
                layout.label(text="Not in 3D View")
