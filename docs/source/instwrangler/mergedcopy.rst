Merged Copy
===========

The **Merged Copy** operator is a comprehensive tool for creating a **single, clean, game-ready mesh** from a selection of multiple, potentially diverse objects. It automates the process of duplicating, converting, joining, and positioning objects.

This is ideal for creating simplified proxy models for complex scenes, preparing assets for game engines, or combining parts for 3D printing.

The Process in Detail
---------------------

When you click **Merged Copy**, the operator performs a sequence of actions:

#. **Duplicate & Convert:** It first creates a safe, unlinked copy of your selection. It then converts all convertible objects in the new copy (like Curves, Text, Surfaces, etc.) into meshes. Objects that cannot be converted (like Lights, Cameras, or Empties) are automatically discarded from the new set.
#. **Join:** All the newly created meshes are joined together into a single object with clean, applied transforms (rotation and scale are baked in).
#. **Set Origin:** The pivot point (origin) of this new mesh is precisely placed based on your active object.
#. **Offset & Rename:** Finally, the new object is moved to the position specified in the **Offset** fields and given the name from the **Name** field.

UI Controls Explained
---------------------

* **Offset (X, Y, Z fields):** These fields determine the final world-space location of your new merged object.
* **Rel (Relative Toggle):** Controls how the offset is applied. When enabled, the offset is added to the pivot point's location. When disabled, the object is moved to the absolute coordinates you enter.
* **Offset Button:** A simple shortcut to reset the Offset fields to ``(0, 0, 0)``.
* **Name Field:** The name that will be given to the final, merged object.

Defining the Origin (Pivot Point)
---------------------------------

The origin of the new merged object is placed at the location of the **active object** from your original selection. This gives you precise control over the final pivot point.

A key part of this feature's power is that you can use *any* type of object to define this pivot, even an **Empty**. Since Empties have no geometry, they will not be visible in the final result, making them perfect, non-destructive guides for your pivot point.

Workflow: Using an Empty for a Precise Pivot
--------------------------------------------

This is a handy workflow for creating a merged asset with a perfectly placed origin, such as at the base of a collection of objects.

#. Create an **Empty** and move it to the exact location where you want the final merged object's pivot point to be.
#. *Optional (but recommended):* Parent all the objects you intend to merge to this Empty. This keeps your components grouped and organized.
#. Select all the objects you want to merge (the meshes, curves, etc.).
#. While holding :kbd:`Shift`, click the **Empty** last. This makes it the active object without adding it to the merge geometry.
#. Set your desired **Offset** and **Name** in the panel.
#. Click the **Merged Copy** button.

The result is a new, single mesh object with its origin placed exactly at the Empty's location, ready to be exported or used elsewhere in your scene.
