import bpy 

#+-----------------------------------------------------------------------------------------------------+#
#? Utils 
#+-----------------------------------------------------------------------------------------------------+#

def get_last_index(parent):
    index = 0

    for ob in bpy.data.objects:
        
        if ob.SM_MH_Parent is None:
            continue
        else:
            if ob.SM_MH_Parent == parent:
                if index >= ob.SM_MH_index:
                    continue
                index = ob.SM_MH_index
            else:
                continue
    return index

#+-----------------------------------------------------------------------------------------------------+#
#? Update 
#+-----------------------------------------------------------------------------------------------------+#

def update_current_index(self, context):
    print ("update")
    if self.SM_MH_current_index > get_last_index(context.active_object):
        self.SM_MH_current_index = get_last_index(context.active_object)
    else:
        print("else")



class SM_mesh_history_Props(bpy.types.PropertyGroup):
    
    bpy.types.Object.SM_Test = bpy.props.PointerProperty(
        name="SM Test",
        description="TEST",
        type=bpy.types.Object
    )
    bpy.types.Object.SM_MH_Parent = bpy.props.PointerProperty(
        name="Mesh History Parent",
        type=bpy.types.Object
    )
    bpy.types.Object.SM_MH_Status = bpy.props.BoolProperty(
        name="Mesh History Status",
        default=False,
    )
    bpy.types.Object.SM_MH_current_index = bpy.props.IntProperty(
        name="Mesh History current index",
        default=0,
        min=0,
        update=update_current_index,
    )
    bpy.types.Object.SM_MH_index = bpy.props.IntProperty(
        name="Mesh History index",
        default=0,
    )




class SM_mesh_history_make_copy(bpy.types.Operator):
    """S.Menu Mesh History Make Copy"""
    bl_idname = 'sop.sm_mesh_history_make_copy'
    bl_label = "Mesh History Copy"
    bl_options = {'REGISTER', 'UNDO', "INTERNAL"}


    #?Useless !?
    @classmethod
    def poll(cls, context):

        return True
    

    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object
        print ("--------------COPY--------------")
        print (active_object)
        print ("--------------COPY--------------")
        if active_object.SM_MH_Parent is None:
            active_object.SM_MH_Status = True
            active_object.SM_MH_Parent = active_object
            active_object.SM_MH_index = -1
            
            initial_copy = active_object.copy()
            initial_copy.SM_MH_index = 0
         
        obj_copy = active_object.copy()
        obj_copy.SM_MH_Parent = active_object
        obj_copy.SM_MH_index = get_last_index(active_object) + 1

        return {'FINISHED'}
