import bpy 

class SM_mesh_history_Props(bpy.types.PropertyGroup):
    
    bpy.types.Object.SM_Test = bpy.props.PointerProperty(
        name="SM Test",
        description="TEST",
        type=bpy.types.Object
    )

    bpy.types.Object.SM_Array = []
    

class SM_mesh_history_OP(bpy.types.Operator):
    bl_idname = 'sop.sm_mesh_history'
    bl_label = "S.Menu Mesh History"
    bl_options = {'REGISTER', 'UNDO', } #- add later "INTERNAL"


    #?Useless !?
    @classmethod
    def poll(cls, context):

        return True
    

    def execute(self, context):
        #Create Bpy.context Variable
        C = bpy.context
        active_object = C.active_object


        if active_object.SM_Test is None:
            print ("First")
            active_object.SM_Test = active_object.copy()
            active_object.SM_Test.name = "Works"
            active_object.SM_Test.data = active_object.data.copy()
            print(active_object.SM_Array)
            active_object.SM_Array.append(active_object.SM_Test)
            print(active_object.SM_Array)
        else:
            print ("Second")
            print (active_object.data)
            
            active_object.SM_Test = active_object.copy()
            active_object.SM_Test.name = "wad"
            active_object.SM_Test.data = active_object.data.copy()
            print(active_object.SM_Array)
            active_object.SM_Array.append(active_object.SM_Test)
            print(active_object.SM_Array)

            print (active_object.data)
            
            

        return {'FINISHED'}