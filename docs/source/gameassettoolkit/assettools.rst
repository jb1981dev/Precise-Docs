===========
Asset Tools
===========

The **Asset Tools** section contains operators for building and managing LOD asset
hierarchies, collider creation, geometry operations, and UV offset assignment.

Create Asset Collection
-----------------------

Groups selected mesh objects into named collections by LOD base name. Objects without a
``_LOD#`` suffix are renamed to ``_LOD0`` automatically. Objects already in a correctly
named collection are kept in place; others are moved. Duplicate names are skipped with a
warning.

Make LOD
--------

Duplicates each selected mesh object and increments its LOD number in the name
(e.g. ``Chair_LOD0`` → ``Chair_LOD1``). Objects without a ``_LOD#`` suffix are renamed to
``_LOD0`` instead. The copy is placed in the same collection(s) as the source.

* :kbd:`Ctrl` — Create a linked copy (shared mesh data) instead of an unlinked copy.

Copy as Collider
----------------

Duplicates each selected mesh object and creates a collider copy. The ``_LOD#`` suffix in
the name is replaced with ``_Collider``; if no LOD suffix is present, ``_Collider`` is
appended. All modifiers on the source are applied to the copy before it is created.

Decimate
--------

Adds a Decimate modifier to each selected mesh object (or updates an existing one). The
ratio can be adjusted in the Redo panel (:kbd:`F9`).

* :kbd:`Ctrl` — Apply the modifier destructively (bakes the result into the mesh and
  removes the modifier). Linked duplicates cannot be applied destructively and will
  remain non-destructive with a warning.

Seams to Sharps
---------------

Marks every edge that has a UV seam as sharp on all selected mesh objects.

* :kbd:`Shift` — Invert: marks every sharp edge as a UV seam instead.

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

Offset UVs
----------

Assigns a **UVWarp** modifier to each object in the selection, giving every instance in a
set of linked duplicates a unique sequential offset value (``0, 1, 2…``) on the active UV
channel. Multiple independent instance sets are handled separately.

Re-clicking the button is idempotent: it re-assigns offsets on the existing modifier.

* :kbd:`Shift` — LOD mode: groups by LOD asset base name instead of by mesh data. All
  LOD variants of the same asset (e.g. ``TreeA_LOD0``, ``TreeA_LOD1``) receive the same
  offset, so the entire asset shifts as a unit. Different asset base names each receive
  a unique set index when multiple assets are selected.
* :kbd:`Alt` — Remove all UVWarp modifiers from selected objects.

Move UV's
---------

Moves UV channels up or down in the stack order on all selected mesh objects.

* :kbd:`▲` — Move the active UV channel up one slot (lower index).
* :kbd:`▼` — Move the active UV channel down one slot (higher index).