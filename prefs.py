import bpy, os  
from bpy.props import EnumProperty, BoolProperty
from . ui.pie_menus import SM_PIE_Add_Call, SM_PIE_Add_Node_Call

# todo create enable all options function for each menu

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

def get_preferences():
    return bpy.context.preferences.addons[get_addon_name()].preferences

# Preferences            
class SM_Prefs(bpy.types.AddonPreferences):
    bl_idname = get_addon_name()
    
    tabs = [
        ("ADD", "Add", ""),
        ("WIP", "Wip", ""),
    ]
    add_sub_tabs = [
        ("OBJECT", "Object Add Menu", ""),
        ("NODE", "Node Add Menu", ""),
        ("WIP", "Wip", ""),
    ]
    enable_qblocker: BoolProperty(
        name="Enable QBlocker",
        default=True
    )
    enable_bolt: BoolProperty(
        name="Enable Bolt",
        default=True
    )
    enable_landscape: BoolProperty(
        name="Enable A.N.T. Landscape",
        default=True
    )
    enable_rock: BoolProperty(
        name="Enable Rock Generator",
        default=True
    )
    enable_pipenightmare: BoolProperty(
        name="Enable Rock Generator",
        default=True
    )
    main_tabs: EnumProperty(name="Main_Tab", items=tabs)
    add_sub_tabs: EnumProperty(name="Add_Sub_Tab", items=add_sub_tabs)


    def add_keymap_to_ui(self, context, layout, k_name, idname):
        keymap_item = context.window_manager.keyconfigs.addon.keymaps[k_name].keymap_items
        row = layout.row()
        row.prop(keymap_item[idname], 'active', text="",full_event=True)
        row.prop(keymap_item[idname], 'type', text=keymap_item[idname].name, full_event=True) 

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        row = col.row()
        row.prop(self, "main_tabs", expand=True)

        box = col.box()
        
        if self.main_tabs == "ADD":
            self.add_main_tab(context, box)


    def add_main_tab(self, context, col):
        
        row = col.row()
        row.prop(self, "add_sub_tabs", expand=True)
        
        if self.add_sub_tabs == "OBJECT":
            self.add_sub_object(context, col)
        elif self.add_sub_tabs == "NODE":
            self.add_sub_node(context, col)
                
    def add_sub_object(self, context ,col):
        col.label(text="Options:")
        
        col.prop(self, "enable_qblocker", text="Enable QBlocker")
        col.prop(self, "enable_bolt", text="Enable Bolt Factory")
        col.prop(self, "enable_landscape", text="Enable A.N.T. Landscape")
        col.prop(self, "enable_rock", text="Enable Rock Generator")
        col.prop(self, "enable_pipenightmare", text="Enable Pipe Nightmare")

        col.label(text="Keymap:")
        self.add_keymap_to_ui(context, col, 'Object Mode', SM_PIE_Add_Call.bl_idname)
     
    def add_sub_node(self, context ,col):
        col.label(text="Options (Wip):")
        
        col.label(text="Keymap:")

        self.add_keymap_to_ui(context, col, 'Node Generic', SM_PIE_Add_Node_Call.bl_idname)
