import bpy


from . pie_menus import call_pie_menu, get_prefs


class SM_change_workspace(bpy.types.Operator):
    bl_idname = 'sop.sm_change_workspace'
    bl_label = "S.Menu Change Workspaces"
    bl_description = ' '
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}


    w_type: bpy.props.StringProperty(name="Change Workspace to:")


    def execute(self, context):
        context = bpy.context
       
        workspaces = bpy.data.workspaces

        for w in workspaces:
            if w.name == self.w_type:
                context.window.workspace = w
                self.report({'INFO'}, "Workspace Changed to: " + w.name)
                return {'FINISHED'}
        

    
        self.report({'ERROR_INVALID_INPUT'}, "'" + self.w_type + "' Is Not a Valid Workspace")
        return {'CANCELLED'}

class SM_PIE_Workspaces_Menu(bpy.types.Menu):
    bl_label = "S.Menu Workspaces Pie"
    

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        Workspaces = bpy.data.workspaces
        

        # fill menu based on slot variables in prefs
        if get_prefs().custom_workspace_pie is True:
            #- 1 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_1 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_1_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_1_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_1,
                    icon=icon,
                ).w_type = get_prefs().workspace_pie_slot_1
            #- 2 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_2 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_2_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_2_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_2,
                    icon=icon,
                ).w_type = get_prefs().workspace_pie_slot_2
            #- 3 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_3 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_3_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_3_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_3,
                    icon=icon,
                ).w_type = get_prefs().workspace_pie_slot_3
            #- 4 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_4 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_4_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_4_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_4,
                    icon=icon,
                ).w_type = get_prefs().workspace_pie_slot_4
            #- 5 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_5 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_5_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_5_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_5,
                    icon=icon,
                ).w_type = get_prefs().workspace_pie_slot_5
            #- 6 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_6 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_6_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_6_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_6,
                    icon=icon,
                ).w_type = get_prefs().workspace_pie_slot_6
            #- 7 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_7 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_7_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_7_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_7,
                    icon=icon,
                ).w_type = get_prefs().workspace_pie_slot_7
            #- 8 -----------------------------------------------------------------
            if get_prefs().workspace_pie_slot_8 == '':
                pie.separator()
            else:
                if get_prefs().workspace_pie_slot_8_icon == '':
                    icon = "ANTIALIASED"
                else:
                    icon = get_prefs().workspace_pie_slot_8_icon
                pie.operator(
                    "sop.sm_change_workspace", 
                    text=get_prefs().workspace_pie_slot_8,
                    icon=icon
                ).w_type = get_prefs().workspace_pie_slot_8
            #------------------------------------------------------------------
            
        else:
        
            # fill menu with first 8 workspaces    
            for index, w in enumerate(Workspaces):
                if index <= 7:
                    pie.operator("sop.sm_change_workspace", text=w.name).w_type = w.name
                else:
                    return
        
class SM_PIE_Workspaces_Menu_Call(bpy.types.Operator):
    
    bl_idname = 'sop.sm_pie_workspaces_menu_call'
    bl_label = "S.Menu Change Workspaces Menu"
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        call_pie_menu('SM_PIE_Workspaces_Menu', True, 100)
        
        return {'FINISHED'}