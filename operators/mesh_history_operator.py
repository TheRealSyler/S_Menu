import bpy 
from .. prefs import get_prefs

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

def get_object_at_index(parent, index):

    for ob in bpy.data.objects:
        
        if ob.SM_MH_Parent is None:
            continue
        else:
            if ob.SM_MH_Parent == parent:
                if index == ob.SM_MH_index:
                    return ob
            else:
                continue
    return None

#+-----------------------------------------------------------------------------------------------------+#
#? Update 
#+-----------------------------------------------------------------------------------------------------+#

def update_current_index(self, context):
    print ("update")
    C = bpy.context
    active_object = C.active_object
    if self.SM_MH_current_index > get_last_index(context.active_object):
        self.SM_MH_current_index = get_last_index(context.active_object)
    else:
        
        print("else")
        for ob in bpy.data.objects:
            
            if ob.SM_MH_Parent is None:
                continue
            else:
                
                if ob.SM_MH_Parent == active_object:
                    if self.SM_MH_current_index == ob.SM_MH_index:
                        print (active_object.data)
                        active_object.data = ob.data
                        #if get_prefs().SM_MH_use_modifiers is True:
                        #ob.modifiers.data = active_object.modifiers.data
                        continue
             
            



class SM_mesh_history_Props(bpy.types.PropertyGroup):
    
    bpy.types.Object.SM_MH_Parent = bpy.props.PointerProperty(
        name="Mesh History Parent",
        type=bpy.types.Object
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
    

    def copy_object(self, context, object_to_copy, is_first):
        #create copy 
        obj_copy = object_to_copy.copy()
        #set parent
        obj_copy.SM_MH_Parent = object_to_copy
        #copy data
        obj_copy.data = object_to_copy.data.copy()
        #obj_copy.modifiers.data = object_to_copy.modifiers.data.copy()
        #set index
        if is_first is False:
            obj_copy.SM_MH_index = get_last_index(object_to_copy) + 1
        else:
            obj_copy.SM_MH_index = 0
        # make fake user
        obj_copy.use_fake_user = True
    
    def set_first_copy(self, context, active_object):
        ob = get_object_at_index(active_object, 0)
        ob.data = active_object.data
        #ob.modifiers.data = active_object.modifiers.data


    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object
        print ("--------------COPY--------------")
        print (active_object)
        print ("--------------COPY--------------")
        active_object.SM_MH_current_index = 0
        if active_object.SM_MH_Parent is None:
            active_object.SM_MH_Parent = active_object
            active_object.SM_MH_index = -1
            
            self.copy_object(context, active_object, True)
        else:
            self.set_first_copy(context, active_object)
            self.copy_object(context, active_object, False)
     
        return {'FINISHED'}
