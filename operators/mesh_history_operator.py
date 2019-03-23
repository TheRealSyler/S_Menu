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

# todo modifiers
# todo animation memery
# todo help
# todo delete instances
# todo auto instance
# todo materials ?!

#§ Update Frame Function
def on_frame_change(scene):
    
    for ob in bpy.data.objects:
        C = bpy.context

        if C.mode != 'OBJECT':
            return
        if ob.SM_MH_Parent is None:
            continue
        else:
            if ob.SM_MH_is_main_status is True and ob.SM_MH_auto_animate is True:
                index_l = get_last_index(ob)
                animation_l = C.scene.frame_end - C.scene.frame_start
                current_frame = C.scene.frame_current
                
                if index_l == 0:
                    print ("ERROR: SM_MH Index length == 0")
                    continue
            
                index_value = round((current_frame / animation_l) * index_l) + 1
                
                if index_value >= index_l:
                    index_value = index_l
                if ob == C.active_object:
                    ob.SM_MH_current_index = index_value
                else:
                    for obj in bpy.data.objects:
                        if obj.SM_MH_Parent is None:
                            continue
                        else:
                            if obj.SM_MH_Parent == ob:
                                if obj.SM_MH_index == index_value:
                                    ob.data = obj.data
                        continue
            else:             
                continue

   



def update_current_index(self, context):
    active_object = context.active_object
    if self.SM_MH_current_index > get_last_index(context.object):
        self.SM_MH_current_index = get_last_index(context.object)
    else:
        for ob in bpy.data.objects:
            if ob.SM_MH_Parent is None:
                continue
            else:
                if ob.SM_MH_Parent == context.object:
                    if self.SM_MH_current_index == ob.SM_MH_index:
                        active_object.data = ob.data
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
    bpy.types.Object.SM_MH_auto_animate = bpy.props.BoolProperty(
        name="Mesh History Auto Animate",
        default=False,
    )
    bpy.types.Object.SM_MH_is_main_status = bpy.props.BoolProperty(
        name="Mesh History is Main Status",
        default=False,
    )




class SM_mesh_history_make_Instance(bpy.types.Operator):
    """S.Menu Mesh History Make Instance"""
    bl_idname = 'sop.sm_mesh_history_make_instance'
    bl_label = "Mesh History Instance"
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
        #set index
        if is_first is False:
            obj_copy.SM_MH_index = get_last_index(object_to_copy) + 1
        else:
            obj_copy.SM_MH_index = 0
        # make fake user
        obj_copy.use_fake_user = True
        #set is main status to false
        obj_copy.SM_MH_is_main_status = False
    def set_first_copy(self, context, active_object):
        ob = get_object_at_index(active_object, 0)
        ob.data = active_object.data


    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object
        print ("--------------COPY--------------")
        print (active_object)
        print ("--------------COPY--------------")
        if active_object.SM_MH_Parent is None:
            active_object.SM_MH_Parent = active_object
            active_object.SM_MH_index = -1
            active_object.SM_MH_is_main_status = True
            
            self.copy_object(context, active_object, True)
            self.copy_object(context, active_object, False)
        else:
            self.set_first_copy(context, active_object)
            self.copy_object(context, active_object, False)
     
        return {'FINISHED'}

class SM_mesh_history_switch_to_edit_mode(bpy.types.Operator):
    """S.Menu Mesh History Switch to Edit Mode"""
    bl_idname = 'sop.sm_mesh_switch_to_edit_mode'
    bl_label = "Switch to Edit Mode"
    bl_options = {'REGISTER', 'UNDO', "INTERNAL"}

    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object
        
        try:
            active_object.SM_MH_current_index = 0
            bpy.ops.object.mode_set(mode='EDIT')
        except:
            bpy.ops.object.mode_set(mode='EDIT')
        
        return {'FINISHED'}