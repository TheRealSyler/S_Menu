import bpy

from . ui.pie_menus import (
    SM_PIE_Add,
    SM_PIE_Add_Call, 
    SM_PIE_Add_Node,
    SM_PIE_Add_Node_Call,
    SM_Add_Texture_Node,
    SM_Add_Texture_Node_Call,
    SM_Add_Shader_Node,
    SM_Add_Shader_Node_Call,
)
#SM_PIE_Add_Node, 
#SM_PIE_Add_Node_Call, 
#

from . prefs import SM_Prefs , add_hotkey, remove_hotkey
from . ui.get_icon import register_icons, unregister_icons

bl_info = {
    "name" : "S.Menu",
    "author" : "Syler",
    "version": (0, 0, 0, 5),
    "description": "Adds Pie Menus",
    "blender" : (2, 80, 0),
    "category" : "Object"
}


classes = [
    SM_PIE_Add,
    SM_PIE_Add_Call,
    SM_PIE_Add_Node,
    SM_PIE_Add_Node_Call,
    SM_Add_Texture_Node,
    SM_Add_Texture_Node_Call,
    SM_Add_Shader_Node,
    SM_Add_Shader_Node_Call,
    SM_Prefs,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    #+ add hotkey
    add_hotkey()
    
    # ------------------------------------------------------------------------------------------------------------
    # Icons Register stuff
    # ------------------------------------------------------------------------------------------------------------
    register_icons(__file__)




def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    #+ remove hotkey
    remove_hotkey()

    # ------------------------------------------------------------------------------------------------------------
    # Icons Unregister stuff
    # ------------------------------------------------------------------------------------------------------------
    unregister_icons()
    

if __name__ == "__main__":
    register()
