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
    ob = get_object_at_index(active_object, 0)
    ob.data = active_object.data
    ob.modifiers.clear()
    copy_object_modifiers(active_object, ob)
#+-----------------------------------------------------------------------------------------------------+#
#? Update 
#+-----------------------------------------------------------------------------------------------------+#

#//     modifiers
#  todo animation memery
#  todo prepend delete (so that all the instances also get deleted)
#//     delete instances
#? todo auto instance maybe later?
#? todo materials ?!


#§ auto instance Function maybe later?

'''
def SM_MH_Auto_Instance():
    print("SM_MH_Auto_Instance")
    for ob in bpy.data.objects:
        if ob.SM_MH_auto_instance_status is True:
            print (ob)
            copy_object(ob, False)
            #set_first_copy(ob)

    return get_prefs().SM_MH_auto_instance_inerval
'''

#§ Update Frame Function
@persistent
def on_frame_change(scene):
    C = bpy.context
    print("abc")
    for ob in bpy.data.objects:
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


# add handler
bpy.app.handlers.frame_change_pre.append(on_frame_change) 

def update_copy_modifiers(self, context):
    active_object = context.active_object
    if active_object.SH_MH_copy_modifiers is True:
        ob = get_object_at_index(active_object, active_object.SM_MH_current_index)
        active_object.modifiers.clear()
        copy_object_modifiers(ob, active_object)
    else:
        ob = get_object_at_index(active_object, 0)
        copy_object_modifiers(ob, active_object)

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
                        
                        if active_object.SH_MH_copy_modifiers is True:
                            active_object.modifiers.clear()
                            copy_object_modifiers(ob, active_object)
                        

                        continue
             

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
    bpy.types.Object.SH_MH_copy_modifiers = bpy.props.BoolProperty(
        name="Copy Modifiers",
        description="Mesh History Copy Modifiers",
        default=True,
        update=update_copy_modifiers,
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
        if active_object.SM_MH_Parent is None:
            active_object.SM_MH_Parent = active_object
            active_object.SM_MH_index = -1
            active_object.SM_MH_is_main_status = True
            
            copy_object(active_object, True)
            copy_object(active_object, False)
        else:
            set_first_copy(active_object)
            copy_object(active_object, False)
        
        if active_object.SM_MH_current_index != 0:
            active_object.SM_MH_current_index = 0
     
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