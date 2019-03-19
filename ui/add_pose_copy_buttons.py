import bpy

from .. ui.pie_menus import (
    get_prefs,
)

def add_pose_copy_buttons(self, context):
    if get_prefs().enable_pose_buttons is True:
        if bpy.context.mode == 'POSE':
            row = self.layout.row(align=True)
            row.separator()
            row.operator("pose.copy", text="", icon='COPYDOWN')
            row.operator("pose.paste", text="", icon='PASTEDOWN').flipped = False
            row.operator("pose.paste", text="", icon='PASTEFLIPDOWN').flipped = True