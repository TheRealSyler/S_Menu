import bpy

from .utils import ui_spacer
from cycles.ui import (
    CYCLES_RENDER_PT_sampling, 
    CYCLES_RENDER_PT_sampling_advanced,
    CYCLES_RENDER_PT_bake,
    CYCLES_RENDER_PT_bake_influence,
    CYCLES_RENDER_PT_bake_selected_to_active,
    CYCLES_RENDER_PT_bake_output,
    CYCLES_RENDER_PT_performance_threads,
    CYCLES_RENDER_PT_performance_tiles,
    CYCLES_RENDER_PT_performance_acceleration_structure,
    CYCLES_RENDER_PT_performance_final_render,
    CYCLES_RENDER_PT_performance_viewport,
    CYCLES_RENDER_PT_film,
    CYCLES_RENDER_PT_film_pixel_filter,
    CYCLES_RENDER_PT_film_transparency,
    CYCLES_RENDER_PT_hair,
    CYCLES_RENDER_PT_simplify_viewport,
    CYCLES_RENDER_PT_simplify_render,
    CYCLES_RENDER_PT_simplify_culling,
    CYCLES_RENDER_PT_motion_blur,
    CYCLES_RENDER_PT_motion_blur_curve,
    use_branched_path,
    use_sample_all_lights,
    draw_samples_info,
    show_device_active,
    use_cpu,
)
from bl_ui.properties_render import (
    RENDER_PT_color_management,
    RENDER_PT_color_management_curves,
)
from bl_ui.properties_freestyle import (
    RENDER_PT_freestyle,
)


def Init_Render_Settings_Props():
    cycles_tabs = [
        ("SAMPLING", "Sampling", ""),
        ("PERFORMANCE", "Performance", ""),
        ("CM", "CM", "Color Management"),
        ("FILM", "Film", ""),
        ("BAKE", "Bake", ""),
        ("OTHER", "Other", ""),
    ]
    cycles_sub_tabs = [
        ("FREESTYLE", "Freestyle", ""),
        ("HAIR", "Hair", ""),
        ("SIMPLIFY", "Simplify", ""),
        ("MBLUR", "Motion Blur", ""),
    ]
    bpy.types.Scene.SM_RS_cycles_tabs = bpy.props.EnumProperty(items=cycles_tabs)
    bpy.types.Scene.SM_RS_cycles_sub_tabs = bpy.props.EnumProperty(items=cycles_sub_tabs)
    
    
def Del_Render_Settings_Props():
    del(bpy.types.Scene.SM_RS_cycles_tabs)


     
#------------------------------------------------
#------------------------------------------------

class SM_Render_Settings_Panel(bpy.types.Panel):
    bl_label = "Render Settings Panel"
    bl_idname = "SM_Render_Settings_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        cscene = scene.cycles
        ccscene = scene.cycles_curves
        view = scene.view_settings
        cbk = scene.render.bake
        rd = scene.render
        
        if context.engine == 'CYCLES':
            layout.prop(scene, "SM_RS_cycles_tabs", expand=True)

            if scene.SM_RS_cycles_tabs == 'CM':
                RENDER_PT_color_management.draw(self, context)
                ui_spacer(layout, 1)
                layout.prop(view, "use_curve_mapping", text="Use Curves")
                if view.use_curve_mapping is True:
                    RENDER_PT_color_management_curves.draw(self, context)

            # Cycles Stuff
            if scene.SM_RS_cycles_tabs == 'BAKE':
                ui_spacer(layout, 1)
                CYCLES_RENDER_PT_bake.draw(self, context)
                CYCLES_RENDER_PT_bake_influence.draw(self, context)

                if rd.use_bake_multires is False:
                    ui_spacer(layout, 1)
                    box = layout.box()
                    box.prop(cbk ,'use_selected_to_active')

                    if cbk.use_selected_to_active is True:
                        CYCLES_RENDER_PT_bake_selected_to_active.draw(self, context)

                layout.label(text="Output:")
                CYCLES_RENDER_PT_bake_output.draw(self, context)

            if scene.SM_RS_cycles_tabs == 'SAMPLING':
                CYCLES_RENDER_PT_sampling.draw(self, context)
                ui_spacer(layout, 1)
                if cscene.progressive != 'PATH' and use_branched_path(context) is True:
                    layout.use_property_split = True
                    layout.use_property_decorate = False

                    col = layout.column(align=True)
                    col.prop(cscene, "diffuse_samples", text="Diffuse")
                    col.prop(cscene, "glossy_samples", text="Glossy")
                    col.prop(cscene, "transmission_samples", text="Transmission")
                    col.prop(cscene, "ao_samples", text="AO")

                    sub = col.row(align=True)
                    sub.active = use_sample_all_lights(context)
                    sub.prop(cscene, "mesh_light_samples", text="Mesh Light")
                    col.prop(cscene, "subsurface_samples", text="Subsurface")
                    col.prop(cscene, "volume_samples", text="Volume")

                    draw_samples_info(layout, context)   
                CYCLES_RENDER_PT_sampling_advanced.draw(self, context)

            if scene.SM_RS_cycles_tabs == 'PERFORMANCE':
                #layout.label(text="Threads:")
                CYCLES_RENDER_PT_performance_threads.draw(self, context)
                #layout.label(text="Tiles:")
                CYCLES_RENDER_PT_performance_tiles.draw(self, context)
                #layout.label(text="Acceleration:")
                CYCLES_RENDER_PT_performance_acceleration_structure.draw(self, context)
                #layout.label(text="Acceleration:")
                CYCLES_RENDER_PT_performance_final_render.draw(self, context)
                #layout.label(text="Acceleration:")
                CYCLES_RENDER_PT_performance_viewport.draw(self, context)
            if scene.SM_RS_cycles_tabs == 'FILM':
                CYCLES_RENDER_PT_film.draw(self, context)
                CYCLES_RENDER_PT_film_pixel_filter.draw(self, context)

                box = layout.box()
                box.prop(cscene, "film_transparent", text="Transparency")
                if cscene.film_transparent is True:
                    CYCLES_RENDER_PT_film_transparency.draw(self, context)
            if scene.SM_RS_cycles_tabs == 'OTHER':
                layout.prop(scene, "SM_RS_cycles_sub_tabs", expand=True)
                if scene.SM_RS_cycles_sub_tabs == 'FREESTYLE':
                    layout.prop(rd, "use_freestyle", text="Enable Freestyle")
                    if rd.use_freestyle is True:
                        RENDER_PT_freestyle.draw(self, context)
                if scene.SM_RS_cycles_sub_tabs == 'HAIR':
                    layout.prop(ccscene, "use_curves", text="Enable Hair")
                    if ccscene.use_curves is True:
                        CYCLES_RENDER_PT_hair.draw(self, context)
                if scene.SM_RS_cycles_sub_tabs == 'SIMPLIFY':
                    layout.prop(rd, "use_simplify", text="Enable Simplify")
                    if rd.use_simplify is True:
                        CYCLES_RENDER_PT_simplify_viewport.draw(self, context)
                        CYCLES_RENDER_PT_simplify_render.draw(self, context)
                        CYCLES_RENDER_PT_simplify_culling.draw(self, context)
                if scene.SM_RS_cycles_sub_tabs == 'MBLUR':
                    layout.prop(rd, "use_motion_blur", text="Enable Motion Blur")
                    if rd.use_motion_blur is True:
                        CYCLES_RENDER_PT_motion_blur.draw(self, context)
                        CYCLES_RENDER_PT_motion_blur_curve.draw(self, context)
                   
        else:
            layout.label(text="WIP")

class SM_Render_Settings_Popup(bpy.types.Operator):
    bl_idname = 'sop.sm_render_settings_popup'
    bl_description = 'Displays Render Settings'
    bl_label = 'Render Settings'

    bl_options = {'UNDO'}

    @classmethod
    def poll(cls, context): 
        return True


    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self, width=450)


    def execute(self, context):
        return {'FINISHED'}


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        rd = scene.render

        col = layout.column()
        row = col.row(align=True)

        row.operator("render.render", icon="RENDER_STILL")
        row.operator("render.render", text="Animation", icon="RENDER_ANIMATION").animation = True
        
        ui_spacer(col, 2)
        
        col = col.column()
        col.use_property_split = True
        col.use_property_decorate = False

        if rd.has_multiple_engines:
            col.prop(rd, "engine", text="Render Engine")

        if context.engine == 'CYCLES':
            from cycles import engine
            cscene = scene.cycles

            col = layout.column()
            col.prop(cscene, "feature_set")

            col = layout.column()
            col.active = show_device_active(context)
            col.prop(cscene, "device")

            if engine.with_osl() and use_cpu(context):
                col.prop(cscene, "shading_system")
        ui_spacer(col, 2)

        SM_Render_Settings_Panel.draw(self, context)
