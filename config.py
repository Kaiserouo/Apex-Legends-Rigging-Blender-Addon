# (parent, child) pair for legend bodies
legend_pc_rig_bone_pairs = [
    ("def_l_clav", "def_l_shoulder"), ("def_l_shoulder", "def_l_elbow"), ("def_l_elbow", "def_l_wrist"),

    ("def_r_clav", "def_r_shoulder"), ("def_r_shoulder", "def_r_elbow"), ("def_r_elbow", "def_r_wrist"),

    ("def_l_finThumbA", "def_l_finThumbB"), ("def_l_finThumbB", "def_l_finThumbC"),
    ("def_l_finIndexA", "def_l_finIndexB"), ("def_l_finIndexB", "def_l_finIndexC"),
    ("def_l_finMidA", "def_l_finMidB"), ("def_l_finMidB", "def_l_finMidC"),
    ("def_l_finRingA", "def_l_finRingB"), ("def_l_finRingB", "def_l_finRingC"),
    ("def_l_finPinkyA", "def_l_finPinkyB"), ("def_l_finPinkyB", "def_l_finPinkyC"),

    ("def_r_finThumbA", "def_r_finThumbB"), ("def_r_finThumbB", "def_r_finThumbC"),
    ("def_r_finIndexA", "def_r_finIndexB"), ("def_r_finIndexB", "def_r_finIndexC"),
    ("def_r_finMidA", "def_r_finMidB"), ("def_r_finMidB", "def_r_finMidC"),
    ("def_r_finRingA", "def_r_finRingB"), ("def_r_finRingB", "def_r_finRingC"),
    ("def_r_finPinkyA", "def_r_finPinkyB"), ("def_r_finPinkyB", "def_r_finPinkyC"),

    ("def_l_thigh", "def_l_knee"), ("def_l_knee", "def_l_ankle"), ("def_l_ankle", "def_l_ball"),

    ("def_r_thigh", "def_r_knee"), ("def_r_knee", "def_r_ankle"), ("def_r_ankle", "def_r_ball"),
]


# lock rotation config: (rotation mode, lock_rotation (XYZ), List[names of bones to lock])
# ref. 
#   https://docs.blender.org/api/current/bpy.types.PoseBone.html#bpy.types.PoseBone.lock_rotation
#   https://docs.blender.org/api/current/bpy.types.PoseBone.html#bpy.types.PoseBone.rotation_mode
lock_rotation_bones = [
    (
        'XYZ', (True, True, False),
        ["def_l_knee", "def_r_knee", "def_l_elbow", "def_r_elbow"]
    )
]

# (parent, child) pair for Bloodhound's pipe
pipe_pc_rig_bone_pairs = [
    ("def_c_top_rope_1", "def_c_top_rope_2"),
    ("def_c_top_rope_2", "def_c_top_rope_3"),
    ("def_c_top_rope_3", "def_c_top_rope_4"),
    ("def_c_top_rope_4", "def_c_top_rope_5"),
    ("def_c_top_rope_5", "def_c_top_rope_6"),
    ("def_c_top_rope_6", "def_c_top_rope_7"),
    ("def_c_top_rope_7", "def_c_top_rope_8"),
    ("def_c_top_rope_8", "def_c_top_rope_9"),
    ("def_c_top_rope_9", "def_c_top_rope_10"),
    ("def_c_top_rope_10", "def_c_top_rope_11"),
    ("def_c_top_rope_11", "def_c_top_rope_12")
]