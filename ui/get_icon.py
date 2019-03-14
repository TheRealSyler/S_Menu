import bpy, os
import bpy.utils.previews

# list of icon collections
preview_collections = {}

def register_icons(init_loc):    
    pcoll = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(init_loc), "icons")

    for i in sorted(os.listdir(icons_dir)):
        if i.endswith(".png"):
            iconname = i[:-4]
            filepath = os.path.join(icons_dir, i)

            pcoll.load(iconname, filepath, 'IMAGE')

    preview_collections["main"] = pcoll
 

def unregister_icons(): 
  
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()



def get_icon(name, coll):
    try:
        icoll = preview_collections[coll]
        return icoll[name].icon_id
    except:
        return 2
