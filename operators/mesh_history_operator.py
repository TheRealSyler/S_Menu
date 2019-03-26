import bpy
from .. prefs import get_prefs
from bpy.app.handlers import persistent


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

def copy_object_modifiers(object_to_copy_from, object_to_copy_to):
    
    for mSrc in object_to_copy_from.modifiers:
        mDst = object_to_copy_to.modifiers.get(mSrc.name, None)
        if not mDst:
            mDst = object_to_copy_to.modifiers.new(mSrc.name, mSrc.type)

        # collect names of writable properties
        properties = [p.identifier for p in mSrc.bl_rna.properties
                      if not p.is_readonly]

        # copy those properties
        for prop in properties:
            setattr(mDst, prop, getattr(mSrc, prop))

def copy_object(object_to_copy, is_first):
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

    copy_object_modifiers(object_to_copy, obj_copy)

def set_first_copy(active_object):
    ac_i = active_object.SM_MH_Instances[0]
    obj = ac_i.object

    ac_i.data = active_object.data
    obj.modifiers.clear()
    copy_object_modifiers(active_object, obj)
    
    if get_prefs().enable_debug_messages is True:
        print("mesh_history_operator.set_first_copy")
    
    '''
    ob = get_object_at_index(active_object, 0)
    ob.data = active_object.data
    
    '''



#+-----------------------------------------------------------------------------------------------------+#
#? Update 
#+-----------------------------------------------------------------------------------------------------+#

#  todo edit modifiers in instance modifiers
#  todo animation memery
#  todo prepend delete (so that all the instances also get deleted)
#//     delete instances
#? todo auto instance maybe later?
#? todo materials ?!



#§ Update Frame Function
@persistent
def on_frame_change(scene):
    C = bpy.context
    if get_prefs().enable_debug_messages is True:
        print("mesh_history_operator.on_frame_change: Start")
    for ob in bpy.data.objects:
        if C.mode != 'OBJECT':
            return
        if len(ob.SM_MH_Instances) == 0:
            continue
        else:
            if ob.SM_MH_auto_animate is True:
                
                index_l = len(ob.SM_MH_Instances) -1
                animation_l = C.scene.frame_end - C.scene.frame_start
                current_frame = C.scene.frame_current
                
                if index_l == 0:
                    print ("ERROR: SM_MH Index length == 0")
                    continue
            
                index_value = round((current_frame / animation_l) * index_l) + 1
                
                if index_value >= index_l:
                    index_value = index_l
                
                ob.SM_MH_current_index = index_value
                if get_prefs().enable_debug_messages is True:
                    print("mesh_history_operator.on_frame_change: {'Finished'} Obj: " + ob.name)
            else:             
                continue


# add handler
bpy.app.handlers.frame_change_pre.append(on_frame_change) 


def update_current_index(self, context):
    c_index = self.SM_MH_current_index
    instances = self.SM_MH_Instances

    if c_index > len(instances) -1:
        self.SM_MH_current_index = len(instances) - 1
        if get_prefs().enable_debug_messages is True:
            print("mesh_history_operator.update_current_index: SM_MH_current_index is more than SM_MH_Instances items")
    else:
        print(self.SM_MH_current_index)
        print(self.SM_MH_current_index -1)
        #? useless
        #if self.SM_MH_current_index - 1 == 0:
        #    print("aw")
        #    set_first_copy(self) 

        obj_copy = self.copy()
  
        self.data = instances[c_index].object.data
        #self.modifiers.clear()
        copy_object_modifiers(instances[c_index].object, self)

        print(instances[c_index].object.name)
        #instances[c_index].object.modifiers.clear()
        #copy_object_modifiers(obj_copy, instances[c_index].object)

        bpy.data.objects.remove(obj_copy, do_unlink=True)

        if get_prefs().enable_debug_messages is True:
            print("mesh_history_operator.update_current_index: {'Finished (1)'} Obj: " + self.name)
       

             
class SM_MH_Instances(bpy.types.PropertyGroup):
    object : bpy.props.PointerProperty(type=bpy.types.Object)   
    

    def add_instance(self, obj):
        self.object = self.id_data.copy()
        self.object.data = self.object.data.copy()
        self.object.SM_MH_index = len(obj.SM_MH_Instances)
        self.name = self.object.name
        return self.object

    def add_first_instance(self, obj):
        self.object = obj
        self.name = obj.name
        return self.object


    


class SM_mesh_history_Props(bpy.types.PropertyGroup):
    
    bpy.types.Object.SM_MH_Parent = bpy.props.PointerProperty(
        name="Mesh History Parent",
        type=bpy.types.Object
    )
    bpy.types.Object.SM_MH_current_index = bpy.props.IntProperty(
        name="Current Instance",
        description="Mesh History Current Index",
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
    # later ?
    #bpy.types.Object.SM_MH_auto_instance_status = bpy.props.BoolProperty(
    #    name="Auto Instance",
    #    default=False,
    #)

class SM_mesh_history_make_Instance(bpy.types.Operator):
    """S.Menu Mesh History Make Instance"""
    bl_idname = 'sop.sm_mesh_history_make_instance'
    bl_label = "Mesh History Instance"
    bl_options = {'REGISTER', 'UNDO', "INTERNAL"}

    #?Useless !?
    @classmethod
    def poll(cls, context):

        return True
    
    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object
        
        if len(active_object.SM_MH_Instances) == 0:
            active_object.SM_MH_Instances.add().add_first_instance(active_object)
            active_object.SM_MH_Instances.add().add_instance(active_object)
        else:
            if active_object.SM_MH_current_index == 0:
                set_first_copy(active_object)
            active_object.SM_MH_Instances.add().add_instance(active_object)
            
            
        #if active_object.SM_MH_Parent is None:
            #active_object.SM_MH_Parent = active_object
            #active_object.SM_MH_index = -1
            #active_object.SM_MH_is_main_status = True
            
            #copy_object(active_object, True)
            #copy_object(active_object, False) 
            
        #else:
            #set_first_copy(active_object)
            #copy_object(active_object, False)
        
        #if active_object.SM_MH_current_index != 0:
            #active_object.SM_MH_current_index = 0
     
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
            if active_object.SM_MH_current_index == 0:
                copy_object_modifiers(active_object, get_object_at_index(active_object, 0))
                active_object.SM_MH_current_index = 0
            else:
                active_object.SM_MH_current_index = 0
            bpy.ops.object.mode_set(mode='EDIT')
        except:
            bpy.ops.object.mode_set(mode='EDIT')
        
        return {'FINISHED'}

class SM_mesh_history_delete_instances(bpy.types.Operator):
    """S.Menu Mesh History Delete All Instances"""
    bl_idname = 'sop.sm_mesh_history_delete_instances'
    bl_label = "Delete All Instances"
    bl_options = {'REGISTER', 'UNDO', "INTERNAL"}

    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object
        # reset ui
        get_prefs().show_delete_instances = False
        get_prefs().sm_mh_del_inst = 'NO'
        objects_to_delete = []
        instance_num_info = 0
        # report if active_object has no SM MH Parent
        if active_object.SM_MH_Parent is None:
            self.report({'INFO'}, "No Instances to Delete")
            return {'FINISHED'}
        # add objects to objects_to_delete
        for ob in bpy.data.objects:
            if ob.SM_MH_Parent is None:
                continue
            else:
                if ob.SM_MH_Parent == active_object:
                    if ob == active_object:
                        continue
                    else:
                        objects_to_delete.append(ob)
                        instance_num_info = instance_num_info + 1
                else:
                    continue
        objects = bpy.data.objects
        # delete active_object props 
        del active_object['SM_MH_Parent']
        del active_object['SM_MH_is_main_status']
        del active_object['SM_MH_index']

        # delete objects_to_delete
        if objects_to_delete is not None:
            for obj in objects_to_delete:
                obj.use_fake_user = False
                objects.remove(obj, do_unlink=True)
        # report instance_num_info + " Instances Deleted"
        self.report({'INFO'}, str(instance_num_info) + " Instances Deleted")
        return {'FINISHED'}

class SM_mesh_history_delete_current_instance(bpy.types.Operator):
    """S.Menu Mesh History Delete Current Instance"""
    bl_idname = 'sop.sm_mesh_history_delete_current_instance'
    bl_label = "Delete Current Instance"
    bl_options = {'REGISTER', 'UNDO', "INTERNAL"}

    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object
      
        # report if active_object has no SM MH Parent
        if active_object.SM_MH_Parent is None:
            self.report({'INFO'}, "No Instances to Delete")
            return {'FINISHED'}
        if active_object.SM_MH_current_index == 0:
            self.report({'INFO'}, "Cannot Delete Instance 0")
            return {'FINISHED'}
        if get_last_index(active_object) == 1:
            bpy.ops.sop.sm_mesh_history_delete_instances()
            active_object.SM_MH_current_index = active_object.SM_MH_current_index -1
            self.report({'INFO'}, "Last Instance Deleted")
            return {'FINISHED'}
        

        objects = bpy.data.objects
        obj_to_delete = get_object_at_index(active_object, active_object.SM_MH_current_index)

        # sort indexes
        for ob in bpy.data.objects:
            if ob.SM_MH_Parent is None:
                continue
            else:
                if ob.SM_MH_Parent == active_object:
                    if ob == active_object:
                        continue
                    else:
                        if ob == obj_to_delete:
                            continue
                        else:
                            # if ob index is >= than current active object index set ob index = index -1
                            if ob.SM_MH_index >= active_object.SM_MH_current_index:
                                ob.SM_MH_index = ob.SM_MH_index - 1
                            else:

                                continue
                else:
                    continue

        if obj_to_delete is None:
            self.report({'ERROR'}, "NO Instance To Delete")
            return {'FINISHED'}
  
        obj_to_delete.use_fake_user = False
        objects.remove(obj_to_delete, do_unlink=True)
        active_object.SM_MH_current_index = active_object.SM_MH_current_index -1

        # report Instance Deleted"
        self.report({'INFO'}, "Instance Deleted")
        return {'FINISHED'}