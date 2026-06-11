===========
Asset Tools
===========

The **Asset Tools** section contains operators for building and managing LOD asset hierarchies, collider creation, UV channels, and geometry operations.

Create Asset Collection
-----------------------

Groups selected mesh objects into named collections by LOD base name. Objects without a ``_LOD#`` suffix are renamed to ``_LOD0`` automatically. The LOD sequence must start at ``_LOD0`` and contain no gaps — incomplete sets are skipped with a warning.

Copy as Next LOD
----------------

Duplicates each selected mesh object and increments its LOD number in the name (e.g. ``Chair_LOD0`` → ``Chair_LOD1``). The copy is placed in the same collection(s) as the source. The source object must already have a ``_LOD#`` suffix.

Copy as Collider
----------------

Duplicates each selected mesh object and creates a collider copy. The ``_LOD#`` suffix in the name is replaced with ``_Collider``; if no LOD suffix is present, ``_Collider`` is appended. All modifiers on the source are applied to the copy before it is created.

Decimate
--------

Adds a Decimate modifier to each selected mesh object (or updates an existing one). The ratio can be adjusted in the Redo panel (:kbd:`F9`).

* :kbd:`Ctrl` — Apply the modifier destructively (bakes the result into the mesh and removes the modifier).

Seams to Sharps
---------------

Marks every edge that has a UV seam as sharp on all selected mesh objects.

* :kbd:`Shift` — Invert: marks every sharp edge as a UV seam instead.

UV0 / UV1
---------

Quick-access buttons for managing the first two UV channels (``UV0`` for textures, ``UV1`` for lightmaps) on all selected mesh objects.

.. list-table::
   :widths: 20 80
   :header-rows: 0

   * - :kbd:`LMB`
     - Activate the UV channel (sets it as the active UV layer).
   * - :kbd:`Ctrl`
     - Set the UV channel as active for rendering.
   * - :kbd:`Shift`
     - Create the UV channel if it does not yet exist.
   * - :kbd:`Alt`
     - Remove the UV channel.

Offset Instance UVs
-------------------

Assigns a **UVWarp** modifier to each object in the selection, giving every instance in a set of linked duplicates a unique sequential offset value (``0, 1, 2…``) on the active UV channel. Multiple independent instance sets are handled separately.

Re-clicking the button is idempotent: it re-assigns offsets on the existing modifier.

* :kbd:`Alt` — Remove all UVWarp modifiers from selected objects.

Offset LOD UVs
--------------

Like Offset Instance UVs, but groups by LOD asset base name instead of by mesh data. All LOD variants of the same asset (e.g. ``TreeA_LOD0``, ``TreeA_LOD1``) receive the same offset, so the entire asset shifts as a unit. Different asset base names each receive a unique set index when multiple assets are selected.

Re-clicking is idempotent.

* :kbd:`Alt` — Remove all UVWarp modifiers from selected objects.

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