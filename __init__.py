bl_info = {
    "name" : "POVCam",
    "blender" : (3,4,1),
    "version" : (2,24,23),
    "category" : "3D View",
    "author" : "Kent Edoloverio",
    "location" : "3D View > POVCam",
    "description" : "Adds a camera based on the current point of view",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
}

import bpy
from bpy.types import Panel, Operator


class POVCamera:
    def __init__(self):
        self.camera_data = bpy.data.cameras.new(name="Camera")
        self.camera_object = bpy.data.objects.new(name="Camera", object_data=self.camera_data)
        bpy.context.scene.collection.objects.link(self.camera_object)

    def set_active_camera(self):
        bpy.context.scene.camera = self.camera_object

    def set_camera_to_point_of_view(self):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region, 'edit_object': self.camera_object}
                        bpy.ops.view3d.camera_to_view(override)
        return {'FINISHED'}


class POVCam_op_Add_camera(Operator):
    bl_idname = "object.append_camera"
    bl_label = "ADD CAMERA"

    def execute(self, context):
        camera_manager = POVCamera()
        camera_manager.set_active_camera()
        camera_manager.set_camera_to_point_of_view()
        return {'FINISHED'}


class POVCam_pl_Camera(Panel):
    bl_label = "POVCam"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "POVCam"
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator("object.append_camera", icon="OUTLINER_OB_CAMERA")
        col.label(text="SUPPORT ME ON:")
        op = self.layout.operator(
            'wm.url_open',
            text='KO-FI',
            icon='URL'
            )
        op.url = 'https://ko-fi.com/kents_workof_art'


classes = (
    POVCam_op_Add_camera,
    POVCam_pl_Camera,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()