Apply Transforms
================

The **Apply Transforms** tool is one of the most powerful features of Instance Wrangler, solving a common limitation in Blender. By default, Blender requires you to make an object a **single user** before you can apply its transform, breaking its link to all other instances. This tool overcomes that restriction.

**Apply Transforms** allows you to "bake" the position, rotation, and/or scale of an object while keeping its data linked to all its instances. It effectively applies the transform at the object level, allowing each instance to have unique transforms while still sharing the same underlying geometry.

How It Works
------------
When you select an object and click **Apply Transforms**, the operator automatically finds every linked duplicate of that object in your entire scene (even in hidden collections) and applies the selected transforms to all of them at once. When the operation is complete, you will not see any objects visually change their position, rotation, or scale. The tool's purpose is to reset the transform *values* (e.g., setting Scale to 1.0) while ensuring the object's appearance in the scene remains exactly the same. This process is repeated for every unique object in your selection, making it a powerful batch-processing tool.

P, R, S Toggles
---------------
Next to the button, you have three toggles to control exactly which transforms are applied:

* ``P``: Applies the object's **Position** (Location).
* ``R``: Applies the object's **Rotation**.
* ``S``: Applies the object's **Scale**.

You can use any combination of these toggles. For example, you can apply the scale of several objects while leaving their unique positions and rotations untouched.

Usage with Selections
---------------------
The operator is designed to be simple and efficient, regardless of your selection:

* **Single Object:** Select any single object that has linked duplicates and run the operator. The transform will be applied to that object and all of its instances.
* **Multiple Objects:** You can select multiple objects at once, even if they belong to different instance groups. The operator will try to find a leader for each group, if the instances belong to a single group it will try to find the active object as a reference. If the instances belong to different groups, you can only have one instance of each group selected, so that it knows which object to use when applying the transforms. 
