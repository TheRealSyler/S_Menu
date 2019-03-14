import bpy, os  

from . ui.pie_menus import SM_PIE_Add_Call, SM_PIE_Add_Node_Call

#SM_PIE_Add_Node_Call, 

# -----------------------------------------------------------------------------
#    Keymap      
# -----------------------------------------------------------------------------

addon_keymaps = [] 

def add_hotkey():
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    km.keymap_items.new(SM_PIE_Add_Call.bl_idname, 'A', 'PRESS', shift=True)                           
    addon_keymaps.append(km)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Node Generic', space_type='NODE_EDITOR')
    km.keymap_items.new(SM_PIE_Add_Node_Call.bl_idname, 'A', 'PRESS', shift=True)                           
    addon_keymaps.append(km)
    

    
def remove_hotkey():
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    del addon_keymaps[:]




# -----------------------------------------------------------------------------
#    Preferences      
# ----------------------------------------------------------------------------- 




def get_addon_name():
    return os.path.basename(os.path.dirname(os.path.realpath(__file__)))

# Preferences            
class SM_Prefs(bpy.types.AddonPreferences):
    bl_idname = get_addon_name()
    
    def add_keymap_to_ui(self, context, layout, k_name, idname):
        keymap_item = context.window_manager.keyconfigs.addon.keymaps[k_name].keymap_items
        row = layout.row()
        row.prop(keymap_item[idname], 'active', text="",full_event=True)
        row.prop(keymap_item[idname], 'type', text=keymap_item[idname].name, full_event=True) 

    def draw(self, context):
        layout = self.layout
        #wm = bpy.context.window_manager
        box = layout.box()
        split = box.split()
        col = split.column()       
        col.separator()
        col.label(text="Keymaps:")
        self.add_keymap_to_ui(context, col, 'Object Mode', SM_PIE_Add_Call.bl_idname)
        self.add_keymap_to_ui(context, col, 'Node Generic', SM_PIE_Add_Node_Call.bl_idname)

                

def get_preferences():
    return bpy.context.preferences.addons[get_addon_name()].preferences
