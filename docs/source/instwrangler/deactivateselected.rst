.. _deactivateselected:

====================
Deactivate Selected
====================

The **Deactivate Selected** tool clears the active object slot without affecting your selection. Blender makes it difficult if not impossible to clear the active object slot, but this tool gives you a one-click way to drop the active status while keeping your selection intact.

This functionality can be useful for situations where you want to do certain operations which change as a result of having an active object, such as merging meshes (a Merged Copy operation will put the pivot point at the center of the bounding box instead of the active object's origin).

Modifier Keys
-------------

:kbd:`LMB`
    **Deactivate** — clears the active object slot. The previously active object (highlighted in lighter orange) remains selected, but nothing is active anymore.

:kbd:`Ctrl`
    **Deactivate and Deselect** — clears the active slot and also removes the object from the selection entirely. Useful when you want to exclude the active object from the current selection without touching anything else.