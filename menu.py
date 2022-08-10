from . import util, config
import bpy

class ApexRigLegend(bpy.types.Operator):
    """Adjust bone tips for selected Apex legend."""
    bl_idname = "apexaddon.rig_legend"
    bl_label = "Rig Selected Apex Legend"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        util.rigLegendBone(obj, config.legend_pc_rig_bone_pairs)
        return {'FINISHED'}

class ApexRigBloodhoundPipe(bpy.types.Operator):
    """Rig Bloodhound's pipe. Only use this on Bloodhound models with pipes."""
    bl_idname = "apexaddon.rig_pipe"
    bl_label = "Rig Selected Bloodhound's Pipe"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        util.rigLegendBone(obj, config.pipe_pc_rig_bone_pairs)
        return {'FINISHED'}

class ApexBoneConnect(bpy.types.Operator):
    """Set parent & Connect bones"""
    bl_idname = "apexaddon.connect"
    bl_label = "Set Parent & Connect bones"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        util.setParentConnected(obj, config.legend_pc_rig_bone_pairs, True)
        return {'FINISHED'}

class ApexBoneDisconnect(bpy.types.Operator):
    """Set parent but disconnect bones (i.e. offset constraint only?)"""
    bl_idname = "apexaddon.disconnect"
    bl_label = "Set Parent but Disconnect bones"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        util.setParentConnected(obj, config.legend_pc_rig_bone_pairs, False)
        return {'FINISHED'}

class ApexPipeConnect(bpy.types.Operator):
    """Connect pipes"""
    bl_idname = "apexaddon.connect_pipe"
    bl_label = "Set Parent & Connect Bloodhound's Pipes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        util.setParentConnected(obj, config.pipe_pc_rig_bone_pairs, True)
        return {'FINISHED'}

class ApexPipeDisconnect(bpy.types.Operator):
    """Disconnect bones"""
    bl_idname = "apexaddon.disconnect_pipe"
    bl_label = "Set Parent but Disconnect Bloodhound's Pipes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        util.setParentConnected(obj, config.pipe_pc_rig_bone_pairs, False)
        return {'FINISHED'}

class ApexBoneLockRotation(bpy.types.Operator):
    """Lock rotation on predetermined joints"""
    bl_idname = "apexaddon.lock_rotation"
    bl_label = "Lock Rotation on Some Joints"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        
        for mode, xyz_tuple, bone_name_ls in config.lock_rotation_bones:
            util.setRotationLock(obj, mode, xyz_tuple, bone_name_ls)
        return {'FINISHED'}

class ApexBoneUnlockRotation(bpy.types.Operator):
    """Unlock rotation on predetermined joints"""
    bl_idname = "apexaddon.unlock_rotation"
    bl_label = "Unlock Rotation on Some Joints"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        
        for mode, _, bone_name_ls in config.lock_rotation_bones:
            util.setRotationLock(obj, mode, (False, False, False), bone_name_ls)
        return {'FINISHED'}

class ApexBoneSetRotationToXYZ(bpy.types.Operator):
    """Set all bones of the selected model's rotation mode to XYZ Euler"""
    bl_idname = "apexaddon.set_rotation_xyz"
    bl_label = "Set bones rotation mode to XYZ Euler"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        
        util.setAllBoneRotationMode(obj, 'XYZ')
        return {'FINISHED'}

# ---

# classes, None act as separator in menu
classes = (
    ApexRigLegend,
    ApexRigBloodhoundPipe,
    None,
    ApexBoneConnect,
    ApexBoneDisconnect,
    ApexPipeConnect,
    ApexPipeDisconnect,
    None,
    ApexBoneLockRotation,
    ApexBoneUnlockRotation,
    None,
    ApexBoneSetRotationToXYZ
)

class Submenu(bpy.types.Menu):
    bl_idname = "OBJECT_MT_apex_submenu"
    bl_label = "Apex Rigging"

    def draw(self, context):
        layout = self.layout

        for c in classes:
            if c == None:
                layout.separator()
            else:
                layout.operator(c.bl_idname)


def menu_func(self, context):
    layout = self.layout
    layout.menu(Submenu.bl_idname)

def register():
    for c in classes:
        if c != None:
            bpy.utils.register_class(c)
    bpy.utils.register_class(Submenu)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)
    bpy.types.VIEW3D_MT_pose_context_menu.append(menu_func)

def unregister():
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)
    bpy.types.VIEW3D_MT_pose_context_menu.remove(menu_func)
    bpy.utils.unregister_class(Submenu)
    for c in classes:
        if c != None:
            bpy.utils.unregister_class(c)