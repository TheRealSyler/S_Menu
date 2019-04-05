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
    CYCLES_PT_post_processing,
    use_branched_path,
    use_sample_all_lights,
    draw_samples_info,
    show_device_active,
    use_cpu,
)
from bl_ui.properties_render import (
    RENDER_PT_color_management,
    RENDER_PT_color_management_curves,
    RENDER_PT_eevee_sampling,
    RENDER_PT_eevee_film,
    RENDER_PT_eevee_film_overscan,
    RENDER_PT_eevee_indirect_lighting,
    RENDER_PT_eevee_indirect_lighting_display,
    RENDER_PT_eevee_ambient_occlusion,
    RENDER_PT_eevee_bloom,
    RENDER_PT_eevee_screen_space_reflections,
    RENDER_PT_eevee_volumetric,
    RENDER_PT_opengl_film,
    RENDER_PT_simplify_viewport,
    RENDER_PT_simplify_render,
)
from bl_ui.properties_freestyle import (
    RENDER_PT_freestyle, 
)
from bl_ui.properties_output import (
    RENDER_PT_dimensions,
    RENDER_PT_frame_remapping,
    RENDER_PT_output,
    RENDER_PT_stamp,
    RENDER_PT_stereoscopy,
    RENDER_PT_output_views,
) 
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

class Main_Popup_Props(bpy.types.PropertyGroup):
    main_tabs = [
        ("RENDER", "Render", "", "SCENE", 0),
        ("RENDER", "Render", "", "OUTPUT", 0),
        ("GOS", "GOS", "", "MENU_PANEL", 1),
        ("OUTPUT", "Output", "", "ERROR", 2),
    ]
  
    main_tabs: bpy.props.EnumProperty(items=main_tabs)

   
class Render_Settings_Props(bpy.types.PropertyGroup):

    cycles_tabs = [
        ("OUTPUT", "Output", "Dimensions/ Output/ Metadata/ Post Processing/ Stereoscopy"),
        ("SAMPLING", "Sampling", ""),
        ("PERFORMANCE", "Performance", ""),
        ("CM", "CM", "Color Management"),
        ("BAKE", "Bake", ""),
        ("OTHER", "Other", "Freestyle/ Hair/ Simplify/ Film/ Motion Blur"),
    ]
    cycles_sub_tabs = [
        ("FREESTYLE", "Freestyle", ""),
        ("HAIR", "Hair", ""),
        ("SIMPLIFY", "Simplify", ""),
        ("FILM", "Film", ""),
        ("MBLUR", "Motion Blur", ""),
    ]
    output_sub_tabs = [
        ("DIM", "Dimensions", ""),
        ("OUTPUT", "Output", ""),
        ("META", "Metadata", ""),
        ("OTHER", "Other", "Post Processing/ Stereoscopy"),
    ]
    eevee_tabs = [
        ("OUTPUT", "Output", "Dimensions/ Output/ Metadata/ Post Processing/ Stereoscopy"),
        ("PP", "PP", ""),
        ("CM", "CM", "Color Management"),
        ("LIGHT", "Indirect Lighting", ""),
        ("OTHER", "Other", "Freestyle/ Hair/ Simplify/ Film/ Motion Blur"),
    ]
    eevee_sub_tabs = [
        ("AO", "AO", ""),
        ("BLOOM", "Bloom", ""),
        ("SSR", "SSR", "Screen Space Reflections"),
        ("VOLUMETRIC", "Volumetric", ""),
        ("OTHER", "Other", "Freestyle/ Hair/ Simplify/ Film/ Motion Blur"),
    ]
    workbench_tabs = [
        ("MAIN", "Main", ""),
        ("OUTPUT", "Output", ""),
        ("CM", "Color Management", "Color Management"),
        ("SIMPLIFY", "Simplify", ""),
    ]
    SM_RS_cycles_tabs: bpy.props.EnumProperty(items=cycles_tabs)
    SM_RS_cycles_sub_tabs: bpy.props.EnumProperty(items=cycles_sub_tabs)
    SM_RS_output_sub_tabs: bpy.props.EnumProperty(items=output_sub_tabs)
    SM_RS_eevee_tabs: bpy.props.EnumProperty(items=eevee_tabs)
    SM_RS_eevee_sub_tabs: bpy.props.EnumProperty(items=eevee_sub_tabs)
    SM_RS_workbench_tabs: bpy.props.EnumProperty(items=workbench_tabs)

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

def render_settings_panel(self, layout, context):
    
    scene = context.scene
    cscene = scene.cycles
    ccscene = scene.cycles_curves
    props = scene.eevee
    view = scene.view_settings
    cbk = scene.render.bake
    rd = scene.render

    tabs = scene.SM_Render_Settings_Props
    
    
    
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
    
    if context.engine == 'CYCLES':
        row = layout.row(align=True)
        row.prop(tabs, "SM_RS_cycles_tabs", expand=True)
        
        if tabs.SM_RS_cycles_tabs == 'OUTPUT':
            row = layout.row(align=True)
            row.prop(tabs, "SM_RS_output_sub_tabs", expand=True)
            
            if tabs.SM_RS_output_sub_tabs == 'DIM':
                RENDER_PT_dimensions.draw(self, context)
                layout.label(text="Time Remapping")
                RENDER_PT_frame_remapping.draw(self, context)
            
            if tabs.SM_RS_output_sub_tabs == 'OUTPUT':
                RENDER_PT_output.draw(self, context)
                box = layout.box()
                col = box.column(align=True)
                col.prop(scene, 'auto_save_after_render')
                if scene.auto_save_after_render is True:
                    col = box.column(align=True)
                    col.prop(context.scene, 'auto_save_format', text='as', expand=False)
                    col.prop(context.scene, 'auto_save_blend', toggle=False)
                    col.prop(context.scene, 'auto_save_subfolders', toggle=False)
                    col.prop(context.scene, 'auto_save_use_framenumber', toggle=False)
            if tabs.SM_RS_output_sub_tabs == 'META': 
                RENDER_PT_stamp.draw(self, context)
                
                box = layout.box()
                box.prop(rd, "use_stamp_note")
                if rd.use_stamp_note is True:
                    box.active = rd.use_stamp_note
                    box.prop(rd, "stamp_note_text", text="")
                
                box = layout.box()
                box.prop(rd, "use_stamp")
                if rd.use_stamp is True:
                    col = layout.column()
                    col.active = rd.use_stamp
                    col.prop(rd, "stamp_font_size", text="Font Size")
                    col.column().prop(rd, "stamp_foreground", slider=True)
                    col.column().prop(rd, "stamp_background", slider=True)
                    col.prop(rd, "use_stamp_labels", text="Include Labels")
            if tabs.SM_RS_output_sub_tabs == 'OTHER':
                CYCLES_PT_post_processing.draw(self, context)
                box = layout.box()
                box.prop(rd, "use_multiview", text="Stereoscopy")
                if rd.use_multiview is True:
                    RENDER_PT_stereoscopy.draw(self, context)
                    ui_spacer(layout, 1)
                    RENDER_PT_output_views.draw(self, context)

        if tabs.SM_RS_cycles_tabs == 'CM':
            RENDER_PT_color_management.draw(self, context)
            ui_spacer(layout, 1)
            layout.prop(view, "use_curve_mapping", text="Use Curves")
            if view.use_curve_mapping is True:
                RENDER_PT_color_management_curves.draw(self, context)

        # Cycles Stuff
        if tabs.SM_RS_cycles_tabs == 'BAKE':
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

        if tabs.SM_RS_cycles_tabs == 'SAMPLING':
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

        if tabs.SM_RS_cycles_tabs == 'PERFORMANCE':
            CYCLES_RENDER_PT_performance_threads.draw(self, context)
            CYCLES_RENDER_PT_performance_tiles.draw(self, context)
            CYCLES_RENDER_PT_performance_acceleration_structure.draw(self, context)
            CYCLES_RENDER_PT_performance_final_render.draw(self, context)
            CYCLES_RENDER_PT_performance_viewport.draw(self, context)
        
        if tabs.SM_RS_cycles_tabs == 'OTHER':
            layout.prop(tabs, "SM_RS_cycles_sub_tabs", expand=True)
            if tabs.SM_RS_cycles_sub_tabs == 'FREESTYLE':
                layout.prop(rd, "use_freestyle", text="Enable Freestyle")
                if rd.use_freestyle is True:
                    RENDER_PT_freestyle.draw(self, context)
            if tabs.SM_RS_cycles_sub_tabs == 'HAIR':
                layout.prop(ccscene, "use_curves", text="Enable Hair")
                if ccscene.use_curves is True:
                    CYCLES_RENDER_PT_hair.draw(self, context)
            if tabs.SM_RS_cycles_sub_tabs == 'SIMPLIFY':
                layout.prop(rd, "use_simplify", text="Enable Simplify")
                if rd.use_simplify is True:
                    CYCLES_RENDER_PT_simplify_viewport.draw(self, context)
                    CYCLES_RENDER_PT_simplify_render.draw(self, context)
                    CYCLES_RENDER_PT_simplify_culling.draw(self, context)
            if tabs.SM_RS_cycles_sub_tabs == 'MBLUR':
                layout.prop(rd, "use_motion_blur", text="Enable Motion Blur")
                if rd.use_motion_blur is True:
                    CYCLES_RENDER_PT_motion_blur.draw(self, context)
                    CYCLES_RENDER_PT_motion_blur_curve.draw(self, context)
            if tabs.SM_RS_cycles_sub_tabs == 'FILM':
                CYCLES_RENDER_PT_film.draw(self, context)
                CYCLES_RENDER_PT_film_pixel_filter.draw(self, context)
                box = layout.box()
                box.prop(cscene, "film_transparent", text="Transparency")
                if cscene.film_transparent is True:
                    CYCLES_RENDER_PT_film_transparency.draw(self, context)

    elif context.engine == 'BLENDER_EEVEE':
        layout.prop(tabs, "SM_RS_eevee_tabs", expand=True)
        if tabs.SM_RS_eevee_tabs == 'OUTPUT':
            layout.prop(tabs, "SM_RS_output_sub_tabs", expand=True)
            
            if tabs.SM_RS_output_sub_tabs == 'DIM':
                RENDER_PT_dimensions.draw(self, context)
                layout.label(text="Time Remapping")
                RENDER_PT_frame_remapping.draw(self, context)
            
            if tabs.SM_RS_output_sub_tabs == 'OUTPUT':
                RENDER_PT_output.draw(self, context)
                box = layout.box()
                col = box.column(align=True)
                col.prop(scene, 'auto_save_after_render')
                if scene.auto_save_after_render is True:
                    col = box.column(align=True)
                    col.prop(context.scene, 'auto_save_format', text='as', expand=False)
                    col.prop(context.scene, 'auto_save_blend', toggle=False)
                    col.prop(context.scene, 'auto_save_subfolders', toggle=False)
                    col.prop(context.scene, 'auto_save_use_framenumber', toggle=False)
            
            if tabs.SM_RS_output_sub_tabs == 'META': 
                RENDER_PT_stamp.draw(self, context)
                
                box = layout.box()
                box.prop(rd, "use_stamp_note")
                if rd.use_stamp_note is True:
                    box.active = rd.use_stamp_note
                    box.prop(rd, "stamp_note_text", text="")
                
                box = layout.box()
                box.prop(rd, "use_stamp")
                if rd.use_stamp is True:
                    col = layout.column()
                    col.active = rd.use_stamp
                    col.prop(rd, "stamp_font_size", text="Font Size")
                    col.column().prop(rd, "stamp_foreground", slider=True)
                    col.column().prop(rd, "stamp_background", slider=True)
                    col.prop(rd, "use_stamp_labels", text="Include Labels")
            
            if tabs.SM_RS_output_sub_tabs == 'OTHER':
                CYCLES_PT_post_processing.draw(self, context)
                box = layout.box()
                box.prop(rd, "use_multiview", text="Stereoscopy")
                if rd.use_multiview is True:
                    RENDER_PT_stereoscopy.draw(self, context)
                    ui_spacer(layout, 1)
                    RENDER_PT_output_views.draw(self, context)    
        
        if tabs.SM_RS_eevee_tabs == 'CM':
            RENDER_PT_color_management.draw(self, context)
            ui_spacer(layout, 1)
            layout.prop(view, "use_curve_mapping", text="Use Curves")
            if view.use_curve_mapping is True:
                RENDER_PT_color_management_curves.draw(self, context)
        
        if tabs.SM_RS_eevee_tabs == 'LIGHT':
            RENDER_PT_eevee_indirect_lighting.draw(self, context)
            RENDER_PT_eevee_indirect_lighting_display.draw(self, context)

        if tabs.SM_RS_eevee_tabs == 'OTHER':
            box = layout.box()
            box.label(text="Film")
            RENDER_PT_eevee_film.draw(self, context)
            layout.prop(props, "use_overscan")
            if props.use_overscan is True:
                RENDER_PT_eevee_film_overscan.draw(self, context)
            box = layout.box()
            box.label(text="Sampling")
            RENDER_PT_eevee_sampling.draw(self, context) 
            box = layout.box()
            box.prop(rd, "use_freestyle", text="Enable Freestyle")
            if rd.use_freestyle is True:
                RENDER_PT_freestyle.draw(self, context)
            
            box = layout.box()
            box.prop(rd, "use_simplify", text="Enable Simplify")
            if rd.use_simplify is True:
                CYCLES_RENDER_PT_simplify_viewport.draw(self, context)
                CYCLES_RENDER_PT_simplify_render.draw(self, context)
                CYCLES_RENDER_PT_simplify_culling.draw(self, context)
        
        if tabs.SM_RS_eevee_tabs == 'PP':
            box = layout.box()
            box.prop(props, "use_gtao", text="Ambient Occlusion - AO")
            box.prop(props, "use_bloom", text="Bloom - Bloom")
            box.prop(props, "use_ssr", text="Screen Space Reflections - SSR")
            box.prop(props, "use_volumetric", text="Volumetric - Volumetric")
            box.prop(props, "use_motion_blur", text="Motion Blur - Other")
            box.prop(props, "use_sss", text="Subsurface Scattering - Other")
            box.prop(props, "use_dof", text="Depth of Field - Other")
            layout.label(text="Settings")
            layout.prop(tabs, 'SM_RS_eevee_sub_tabs', expand=True)
            if tabs.SM_RS_eevee_sub_tabs == 'AO':
                if props.use_gtao is True:
                    RENDER_PT_eevee_ambient_occlusion.draw(self, context)
                else:
                    layout.label(text="Please Enable: Ambient Occlusion")
            if tabs.SM_RS_eevee_sub_tabs == 'BLOOM':
                if props.use_bloom is True:
                    RENDER_PT_eevee_bloom.draw(self, context)
                else:
                    layout.label(text="Please Enable: Bloom")
            
            if tabs.SM_RS_eevee_sub_tabs == 'SSR':
                if props.use_ssr is True:
                    RENDER_PT_eevee_screen_space_reflections.draw(self, context)
                else:
                    layout.label(text="Please Enable: Screen Space Reflections")
                    
            if tabs.SM_RS_eevee_sub_tabs == 'VOLUMETRIC':
                if props.use_volumetric is True:
                    RENDER_PT_eevee_volumetric.draw(self, context)
                    box = layout.box()
                    box.prop(props, "use_volumetric_lights", text="Volumetric Lighting")
                    if props.use_volumetric_lights is True:
                        box.prop(props, "volumetric_light_clamp", text="Light Clamping")
                    box = layout.box()
                    box.prop(props, "use_volumetric_shadows", text="Volumetric Shadows")
                    if props.use_volumetric_shadows is True:
                        box.prop(props, "volumetric_shadow_samples", text="Shadow Samples")
                else:
                    layout.label(text="Please Enable: Volumetric")
                
            if tabs.SM_RS_eevee_sub_tabs == 'OTHER':
                box = layout.box()
                box.active = props.use_motion_blur
                box.use_property_split = True
                box.label(text="Motion Blur")
                box.prop(props, "motion_blur_samples")
                box.prop(props, "motion_blur_shutter")
                box = layout.box()
                box.active = props.use_sss
                box.use_property_split = True
                box.label(text="Subsurface Scattering")
                box.prop(props, "sss_samples")
                box.prop(props, "sss_jitter_threshold")
                box.prop(props, "use_sss_separate_albedo")
                box = layout.box()
                box.active = props.use_dof
                box.use_property_split = True
                box.label(text="Depth of Field")
                box.prop(props, "bokeh_max_size")

    elif context.engine == 'BLENDER_WORKBENCH':
        layout.prop(tabs, "SM_RS_workbench_tabs", expand=True)
        if tabs.SM_RS_workbench_tabs == 'OUTPUT':
            layout.prop(tabs, "SM_RS_output_sub_tabs", expand=True)
            
            if tabs.SM_RS_output_sub_tabs == 'DIM':
                RENDER_PT_dimensions.draw(self, context)
                layout.label(text="Time Remapping")
                RENDER_PT_frame_remapping.draw(self, context)
            
            if tabs.SM_RS_output_sub_tabs == 'OUTPUT':
                RENDER_PT_output.draw(self, context)
                box = layout.box()
                col = box.column(align=True)
                col.prop(scene, 'auto_save_after_render')
                if scene.auto_save_after_render is True:
                    col = box.column(align=True)
                    col.prop(context.scene, 'auto_save_format', text='as', expand=False)
                    col.prop(context.scene, 'auto_save_blend', toggle=False)
                    col.prop(context.scene, 'auto_save_subfolders', toggle=False)
                    col.prop(context.scene, 'auto_save_use_framenumber', toggle=False)
            
            if tabs.SM_RS_output_sub_tabs == 'META': 
                RENDER_PT_stamp.draw(self, context)
                
                box = layout.box()
                box.prop(rd, "use_stamp_note")
                if rd.use_stamp_note is True:
                    box.active = rd.use_stamp_note
                    box.prop(rd, "stamp_note_text", text="")
                
                box = layout.box()
                box.prop(rd, "use_stamp")
                if rd.use_stamp is True:
                    col = layout.column()
                    col.active = rd.use_stamp
                    col.prop(rd, "stamp_font_size", text="Font Size")
                    col.column().prop(rd, "stamp_foreground", slider=True)
                    col.column().prop(rd, "stamp_background", slider=True)
                    col.prop(rd, "use_stamp_labels", text="Include Labels")
            
            if tabs.SM_RS_output_sub_tabs == 'OTHER':
                CYCLES_PT_post_processing.draw(self, context)
                box = layout.box()
                box.prop(rd, "use_multiview", text="Stereoscopy")
                if rd.use_multiview is True:
                    RENDER_PT_stereoscopy.draw(self, context)
                    ui_spacer(layout, 1)
                    RENDER_PT_output_views.draw(self, context)

        if tabs.SM_RS_workbench_tabs == 'MAIN':
            VIEW3D_PT_shading_lighting.draw(self, context)
            VIEW3D_PT_shading_color.draw(self, context)
            VIEW3D_PT_shading_options.draw(self, context)
            RENDER_PT_opengl_film.draw(self, context)
        
        if tabs.SM_RS_workbench_tabs == 'CM':
            RENDER_PT_color_management.draw(self, context)
            ui_spacer(layout, 1)
            layout.prop(view, "use_curve_mapping", text="Use Curves")
            if view.use_curve_mapping is True:
                RENDER_PT_color_management_curves.draw(self, context)
        
        if tabs.SM_RS_workbench_tabs == 'SIMPLIFY':
            layout.prop(rd, "use_simplify", text="Enable Simplify")
            if rd.use_simplify is True:
                RENDER_PT_simplify_viewport.draw(self, context)
                RENDER_PT_simplify_render.draw(self, context)

    else:
        layout.label(text="Not Supported")


def gos_panel(self, layout, context):
    

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
    row = layout.row(align=True)
    if gaf is True:
        row.prop(gos_props, "SM_GOS_gaffer_tabs", expand=True)

        if tabs == "LIGHTS":
            if context.scene.render.engine == "CYCLES":
                layout.prop(gaf_props, 'hdri_handler_enabled', text="Enable Gaffer HDRI")
            bpy.types.GAFFER_PT_lights.draw(self, context)

        if tabs == "TOOLS":
            bpy.types.GAFFER_PT_tools.draw(self, context)
    else:
        row.prop(gos_props, "SM_GOS_tabs", expand=True)


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


class SM_OT_Main_Popup(bpy.types.Operator):
    bl_idname = 'sop.sm_main_popup'
    bl_description = ' '
    bl_label = 'S.Menu Popup'

    bl_options = {'UNDO'}

    
  
    main_tabs: bpy.props.StringProperty(name="Tabs")
    single_panel: bpy.props.BoolProperty(name="Single Panel", default=False)


    @classmethod
    def poll(cls, context): 
        return True


    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self, width=475)


    def execute(self, context):
        self.single_panel = False
        return {'FINISHED'}
    #----------------------------------------------------------------------------------------
    #+ needed to draw output
    @staticmethod
    def _draw_framerate_label(*args):
        # avoids re-creating text string each draw
        if RENDER_PT_dimensions._frame_rate_args_prev == args:
            return RENDER_PT_dimensions._frame_rate_ret

        fps, fps_base, preset_label = args

        if fps_base == 1.0:
            fps_rate = round(fps)
        else:
            fps_rate = round(fps / fps_base, 2)

        # TODO: Change the following to iterate over existing presets
        custom_framerate = (fps_rate not in {23.98, 24, 25, 29.97, 30, 50, 59.94, 60})

        if custom_framerate is True:
            fps_label_text = f"Custom ({fps_rate!r} fps)"
            show_framerate = True
        else:
            fps_label_text = f"{fps_rate!r} fps"
            show_framerate = (preset_label == "Custom")

        RENDER_PT_dimensions._frame_rate_args_prev = args
        RENDER_PT_dimensions._frame_rate_ret = args = (fps_label_text, show_framerate)
        return args

    @staticmethod
    def draw_framerate(layout, sub, rd):
        if RENDER_PT_dimensions._preset_class is None:
            RENDER_PT_dimensions._preset_class = bpy.types.RENDER_MT_framerate_presets

        args = rd.fps, rd.fps_base, RENDER_PT_dimensions._preset_class.bl_label
        fps_label_text, show_framerate = RENDER_PT_dimensions._draw_framerate_label(*args)

        sub.menu("RENDER_MT_framerate_presets", text=fps_label_text)

        if show_framerate:
            col = layout.column(align=True)
            col.prop(rd, "fps")
            col.prop(rd, "fps_base", text="Base")
    #----------------------------------------------------------------------------------------
    #+ workbench stuff
    def _draw_color_type(self, context):
        layout = self.layout
        shading = VIEW3D_PT_shading.get_shading(context)

        layout.row().prop(shading, "color_type", expand=True)
        if shading.color_type == 'SINGLE':
            layout.row().prop(shading, "single_color", text="")

    def _draw_background_color(self, context):
        layout = self.layout
        shading = VIEW3D_PT_shading.get_shading(context)

        layout.row().label(text="Background")
        layout.row().prop(shading, "background_type", expand=True)
        if shading.background_type == 'VIEWPORT':
            layout.row().prop(shading, "background_color", text="")
    #----------------------------------------------------------------------------------------
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        main_props = scene.SM_Main_Popup_Props
        
        

        if self.single_panel is True:
            box = layout.box()
            box.prop(self, "single_panel", text="Go To Main Panel", icon="DECORATE", expand=True)
            if self.main_tabs == "RENDER":
                render_settings_panel(self, layout, context)
            if self.main_tabs == "GOS":
                gos_panel(self, layout, context)
        else:
            
            row = layout.row()
            row.scale_x = 1.4
            row.scale_y = 1.4
            row.prop(main_props, "main_tabs", expand=True, icon_only=True)



            if main_props.main_tabs == "RENDER":
                render_settings_panel(self, layout, context)
            if main_props.main_tabs == "GOS":
                gos_panel(self, layout, context)
