import bpy


from . pie_menus import call_pie_menu, get_prefs


def custom_pie_slot_change_workspace(pie_ref, slot, text, icon, type):

    # - 1 -----------------------------------------------------------------
    if slot == '':
        pie_ref.separator()
    else:
        if icon == '':
            icon = "ANTIALIASED"
        else:
            icon = icon
        pie_ref.operator(
            "sop.sm_change_workspace",
            text=text,
            icon=icon,
        ).w_type = type


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

        self.report({'ERROR_INVALID_INPUT'}, "'" +
                    self.w_type + "' Is Not a Valid Workspace")
        return {'CANCELLED'}


class SM_MT_pie_workspaces_menu(bpy.types.Menu):
    bl_label = "S.Menu Workspaces Pie"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        Workspaces = bpy.data.workspaces

        # fill menu based on slot variables in prefs
        if get_prefs().custom_workspace_pie is True:
            # - 1 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_1,
                get_prefs().workspace_pie_slot_1,
                get_prefs().workspace_pie_slot_1_icon,
                get_prefs().workspace_pie_slot_1,
            )
            # - 2 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_2,
                get_prefs().workspace_pie_slot_2,
                get_prefs().workspace_pie_slot_2_icon,
                get_prefs().workspace_pie_slot_2,
            )
            # - 3 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_3,
                get_prefs().workspace_pie_slot_3,
                get_prefs().workspace_pie_slot_3_icon,
                get_prefs().workspace_pie_slot_3,
            )
            # - 4 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_4,
                get_prefs().workspace_pie_slot_4,
                get_prefs().workspace_pie_slot_4_icon,
                get_prefs().workspace_pie_slot_4,
            )
            # - 5 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_5,
                get_prefs().workspace_pie_slot_5,
                get_prefs().workspace_pie_slot_5_icon,
                get_prefs().workspace_pie_slot_5,
            )
            # - 6 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_6,
                get_prefs().workspace_pie_slot_6,
                get_prefs().workspace_pie_slot_6_icon,
                get_prefs().workspace_pie_slot_6,
            )
            # - 7 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_7,
                get_prefs().workspace_pie_slot_7,
                get_prefs().workspace_pie_slot_7_icon,
                get_prefs().workspace_pie_slot_7,
            )
            # - 8 -----------------------------------------------------------------
            custom_pie_slot_change_workspace(
                pie,
                get_prefs().workspace_pie_slot_8,
                get_prefs().workspace_pie_slot_8,
                get_prefs().workspace_pie_slot_8_icon,
                get_prefs().workspace_pie_slot_8,
            )
            # ------------------------------------------------------------------

        else:

            # fill menu with first 8 workspaces
            for index, w in enumerate(Workspaces):
                if index <= 7:
                    pie.operator("sop.sm_change_workspace",
                                 text=w.name).w_type = w.name
                else:
                    return


class SM_MT_pie_workspaces_menu_Call(bpy.types.Operator):

    bl_idname = 'sop.sm_mt_pie_workspaces_menu_call'
    bl_label = "S.Menu Change Workspaces Menu"
    bl_description = 'Calls pie menu'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        call_pie_menu('SM_MT_pie_workspaces_menu', True, 100)

        return {'FINISHED'}
