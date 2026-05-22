.. _deactivateselected:

====================
Deactivate Selected
====================

The **Deactivate Selected** tool clears the active object slot without affecting your selection. This can be handy for situations where you want to do certain operations which change as a result of having an active object, such as merging meshes, or doing transforms on multiple objects. Blender makes it difficult if not impossible to clear the active object slot, but this tool gives you a one-click way to drop the active status while keeping your selection intact.

Modifier Keys
-------------

:kbd:`LMB`
    **Deactivate** — clears the active object slot. The previously active object remains selected (highlighted in lighter orange), but nothing is active anymore.

:kbd:`Ctrl`
    **Deactivate and Deselect** — clears the active slot and also removes the object from the selection entirely. Useful when you want to exclude the active object from the current selection without touching anything else.

When Is This Useful?
--------------------

A common situation: you select an object and click **Select Linked** to expand the selection to all of its duplicates. The original object is still the active one. If you want to run a batch operation on only the duplicates — keeping the original as a reference — click **Deactivate Selected** to drop the active slot, or :kbd:`Ctrl` click to also remove it from the selection entirely.
