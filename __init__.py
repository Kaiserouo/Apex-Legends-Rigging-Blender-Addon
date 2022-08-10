bl_info = {
    "name": "Apex Rigging Addon",
    "description": "Addon that helps Apex Legends character rigging.",
    "author": "Kaiserouo",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Object Context Menu / Pose Context Menu > Apex Rigging",
    "doc_url": "https://github.com/Kaiserouo/Apex-Legends-Rigging-Blender-Addon",
    "category": "Object"
}

import bpy
from . import menu

def register():
    menu.register()
    
def unregister():
    menu.unregister()

if __name__ == "__main__":
    register()