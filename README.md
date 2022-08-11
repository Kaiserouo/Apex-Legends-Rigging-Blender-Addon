# Apex Legends Rigging Blender Addon
Blender addon for rigging Apex Legend's characters etc.

Follows the guide in [this video](https://www.youtube.com/watch?v=NJ_M1W85KYA) about rigging. This addon do the rigging automatically so no manual copy & paste stuff needed.

Most importantly, you can use the `Auto IK` (Auto Inverse Kinematics) functionality built inside Blender to make posing way easier. Not as properly as Auto Rig Pro did it, but still way better than posing imported models directly with FK (Forward Kinematics).

**RIGGING WILL MAKE THE MODEL IMCOMPATIBLE WITH IMPORTED ANIMATION!** ref. `Functionality > Rigging > Note` below for detailed description.

## Installation
1. Clone this repository and zip it, or just download as zip file on Github.
2. `Edit -> Preferences -> Add-ons -> Install..` and choose the zip file.
3. Activate the addon by checking the box.
4. `Save Preference`

## Functionality

### Rigging
Import your **legend** model by other addons. The model should have bones like `def_l_shoulder` and other bones defined in `config.py`'s `legend_pc_rig_bone_pairs`.

In object mode, select the armature (i.e. those dots on the model) and `Right-click > Apex-Rigging > Rig Selected Apex Legend` to get the rigging done.

Notes:
+ No renaming needed. I think the video did the renaming to perform mirroring. By not renaming the bones we can still import the animations just fine, even after rigging.
+ "Rigging" is defined as "changing bone's head and tail position". This will make imported animation break as discussed below.
+ You could do your posing now, but only FK (forward kinematics) available, just like before rigging. But rigging makes the bones more easily to select.
+ **WILL MESS UP IMPORTED ANIMATION!** 
  + This rigging method is destined to not be compatible with imported animation. The changing of bone tail position messes up rotation, so the imported rotation information is not compatible with the bones after rigging.
  + Basically any importing method will mess up the pose in some ways (e.g. directly import; use pose library to copy from other models; rig before or after importing; etc.).
  + But some of the animation would look...less messed up. You can start posing from there if you want.
  + **It is suggested to use this only if you want to pose from the ground up.**

> In theory, you might be able to calculate new pose-mode rotation from imported rotation information, but I cannot find a way to calculate that after hours of research. I am just not good at CG-related math.
> 
> If you can somehow fix this it will be appreciated.

### Connect Bones
To use `Auto IK` functionality inside Blender, bones needs to be connected.

**Only use AFTER rigging!**

In object mode, select the armature (i.e. those dots on the model) and `Right-click > Apex-Rigging > Set Parent & Connect Bones` to connect the bones. After connecting, do `Pose Mode -> Pose Options -> Auto IK` to use IK.

Notes:
+ The `Set Parent` part messes with the original parent-child relationship. Not really a problem when rigging but still, FYI.
  + e.g. `def_l_elbow`'s parent was originally `def_l_shoulderMid`, but will be overridden to `def_l_shoulder` to make Auto IK work properly. All parent-child relationships overridden can be found in `config.py`'s `legend_pc_rig_bone_pairs`.
+ You can disconnect by using `Set Parent & Disconnect Bones`, if you need to do that.
+ Some bones that don't have major effect or I don't really know the use of (e.g. `shoulderMid, forearm, elbowB`) is not tackled. You still can pose them individually if you want. Fix `config.py`'s `legend_pc_rig_bone_pairs` if you know what to do.

### Lock Rotation on Joints
There are some joints that should have limited rotation direction (e.g. `def_l_knee` should not rotate around any axis other than Z-axis).

In object mode, select the armature (i.e. those dots on the model) and `Right-click > Apex-Rigging > Lock Rotation on Some Joints` to lock the rotation. You should see that the rotation is locked for some bones in pose mode.

Notes:
+ The bones subjected to the rotation locks are defined in `config.py`'s `lock_rotation_bones`, as well as what kind of lock it is subjected to.

### Bloodhound's Pipe
Rigging & bone connecting for Bloodhound's pipe is also supported. Make sure the selected legend has Bloodhound's pipes on it (i.e. `def_c_top_rope_1` ~ `def_c_top_rope_12`)

The steps is the same as above but has its own options (e.g. `Rig Selected Bloodhound's Pipe`). After rigging, connecting & opening Auto IK, you can control Bloodhound's pipe by grabbing `def_c_top_rope_12` (the one closest to the mask). 