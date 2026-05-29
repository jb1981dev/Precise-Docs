===============
Collider Tools
===============

The **Collider Tools** section contains operators for creating and managing collision meshes. Collider objects follow the ``AssetName_Collider`` naming convention.

Copy as Collider
----------------

Duplicates each selected mesh object and creates a collider copy. The ``_LOD#`` suffix in the name is replaced with ``_Collider``; if no LOD suffix is present, ``_Collider`` is appended. All modifiers on the source are applied to the copy before it is created.

Convex Hull
-----------

Replaces the geometry of selected mesh objects with a convex hull.

* :kbd:`LMB` — Replace the object's geometry with its convex hull in-place.
* :kbd:`Shift` — Create a copy with a ``_Hull`` suffix instead of modifying the original.
* :kbd:`Ctrl` — Combine all selected objects into a single convex hull.

Works in Edit Mode: if faces are selected, only those faces are used as input.

Bounding Box
------------

Replaces the geometry of selected mesh objects with an axis-aligned bounding box.

* :kbd:`LMB` — Replace the object's geometry with its bounding box in-place.
* :kbd:`Shift` — Create a copy with a ``_BBox`` suffix instead of modifying the original.
* :kbd:`Ctrl` — Combine all selected objects into a single bounding box.

Works in Edit Mode: if faces are selected, only those faces are used as input.

Display Mode
------------

**Solid / Wire**
   Sets the viewport display mode for all objects with a ``_Collider`` suffix in the scene. Wire mode is useful for inspecting collision geometry without it obscuring the visual mesh.

   * :kbd:`LMB` — Apply to all collider objects in the scene.
   * :kbd:`Ctrl` — Apply to all currently selected objects instead.

Visibility
----------

**Show / Hide**
   Shows or hides all objects with a ``_Collider`` suffix that are in visible collections. Only objects present in the active view layer are affected.
