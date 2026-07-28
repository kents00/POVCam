bl_info = {
    "name": "POVCam",
    "blender": (3, 0, 0),
    "version": (2, 25, 0),
    "category": "3D View",
    "author": "Kent Edoloverio",
    "location": "3D View > POVCam",
    "description": "Adds a camera based on the current point of view",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
}

import bpy
from bpy.types import Panel, Operator


class POVCamera:
    def __init__(self):
        self.camera_data = bpy.data.cameras.new(name="Camera")
        self.camera_object = bpy.data.objects.new(name="Camera", object_data=self.camera_data)
        collection = getattr(bpy.context, "collection", None) or bpy.context.scene.collection
        collection.objects.link(self.camera_object)

    def set_active_camera(self):
        bpy.context.scene.camera = self.camera_object
        if getattr(bpy.context, "view_layer", None):
            for obj in bpy.context.selected_objects:
                obj.select_set(False)
            bpy.context.view_layer.objects.active = self.camera_object
            self.camera_object.select_set(True)

    def set_camera_to_point_of_view(self):
        areas = []
        if getattr(bpy.context, "area", None) and bpy.context.area.type == 'VIEW_3D':
            areas = [bpy.context.area]
        elif getattr(bpy.context, "screen", None):
            areas = [area for area in bpy.context.screen.areas if area.type == 'VIEW_3D']

        for area in areas:
            for region in area.regions:
                if region.type == 'WINDOW':
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            override = {
                                'area': area,
                                'region': region,
                                'space_data': space,
                                'region_data': space.region_3d,
                                'edit_object': self.camera_object,
                                'object': self.camera_object,
                                'active_object': self.camera_object,
                                'selected_objects': [self.camera_object],
                                'selected_editable_objects': [self.camera_object],
                            }
                            if hasattr(bpy.context, "temp_override"):
                                with bpy.context.temp_override(**override):
                                    bpy.ops.view3d.camera_to_view()
                            else:
                                bpy.ops.view3d.camera_to_view(override)
                            return {'FINISHED'}
        return {'CANCELLED'}


class POVCam_op_Add_camera(Operator):
    bl_idname = "object.append_camera"
    bl_label = "ADD CAMERA"
    bl_description = "Add a new camera matching the current 3D viewport perspective"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        camera_manager = POVCamera()
        camera_manager.set_active_camera()
        result = camera_manager.set_camera_to_point_of_view()
        return result or {'FINISHED'}


class POVCam_pl_Camera(Panel):
    bl_label = "POVCam"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "POVCam"
    bl_options = {'HEADER_LAYOUT_EXPAND'}

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.enabled = True
        col.scale_x = 2.0
        col.scale_y = 2.0
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
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
