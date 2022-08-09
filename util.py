import bpy

def rigLegendBone(obj, pc_bone_pairs):
    mode = bpy.context.object.mode
    bpy.ops.object.mode_set(mode='EDIT')
    bones = obj.data.edit_bones

    for parent_name, child_name in pc_bone_pairs:
        parent_bone = bones[parent_name]
        child_bone = bones[child_name]
        parent_bone.tail = child_bone.head.copy()

    bpy.ops.object.mode_set(mode=mode)

def setParentConnected(obj, pc_bone_pairs, do_connect):
    mode = bpy.context.object.mode
    bpy.ops.object.mode_set(mode='EDIT')
    bones = obj.data.edit_bones

    for parent_name, child_name in pc_bone_pairs:
        parent_bone = bones[parent_name]
        child_bone = bones[child_name]
        child_bone.parent = parent_bone
        child_bone.use_connect = do_connect

    bpy.ops.object.mode_set(mode=mode)

def setRotationLock(obj, mode, xyz_tuple, bone_name_ls):
    # xyz_tuple: array of 3 bools
    bones = obj.pose.bones
    for bone_name in bone_name_ls:
        bone = bones[bone_name]
        bone.rotation_mode = mode
        for i in range(3):
            bone.lock_rotation[i] = xyz_tuple[i]