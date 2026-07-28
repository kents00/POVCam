![POVCam](https://user-images.githubusercontent.com/69900896/221138308-e2863d4a-2406-4232-b1df-1c2ef6da6a3a.png)

# POVCam

"Adds a camera based on the current point of view”

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Q5Q8BW198)

## Introduction

Adding a camera and adjusting it to your needs can be time-consuming, which is the reason I created this addon to make it easier to add a camera. It allows the user to add a new camera object to the scene, make it the active camera, and adjust its position and orientation to match the current point of view in the active 3D viewport.

## Compatibility

POVCam supports **Blender 3.0 up to Blender 5.x**:
- **Blender 3.0 to 4.1**: Compatible as a traditional add-on via `bl_info` in `__init__.py`.
- **Blender 4.2 to 5.x**: Compatible with Blender's updated operator override API (`bpy.context.temp_override`) and the Extensions manifest format (`blender_manifest.toml`).

https://user-images.githubusercontent.com/69900896/221156617-0ef188bf-1f77-4063-90a0-0e5130e41c2c.mp4


## Installation

To install this add-on in Blender, follow these steps:

- Open Blender and go to Edit > Preferences.
- In the Preferences window, select the "Add-ons" tab.
- At the bottom of the window, click the "Install" button.
- In the file browser that opens, navigate to the location of the add-on file you want to install. The add-on file should have a .zip extension.
- Select the add-on file and click the "Install Add-on from File" button.

The add-on will now be installed and will appear in the list of available add-ons. To enable the add-on, locate it in the list and click the checkbox next to its name.
You can also install an add-on by clicking the "Install from File" button in the "Add-ons" tab of the Preferences window and selecting the add-on file from the file browser.

https://user-images.githubusercontent.com/69900896/221189519-8832c069-e5f5-4ed8-b2b8-ba49380d67af.mp4

