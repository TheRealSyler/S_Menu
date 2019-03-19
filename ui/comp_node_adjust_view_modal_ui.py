import bpy
#import gpu
import blf
#from gpu_extras.batch import batch_for_shader


def SM_adujst_view_modal_draw(self, context):
    height = bpy.context.region.height
    width = bpy.context.region.width

    font_id = 0

    blf.position(font_id, (width/2), (height/2), 0)
    blf.size(font_id, 20, 60)
    blf.draw(font_id, "test")