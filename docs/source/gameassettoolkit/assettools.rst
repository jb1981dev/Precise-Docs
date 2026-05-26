===========
Asset Tools
===========

The **Asset Tools** section contains operators for building and managing LOD asset hierarchies and UV channels.

Create Asset Collection
-----------------------

Groups selected mesh objects into named collections by LOD base name. Objects without a ``_LOD#`` suffix are renamed to ``_LOD0`` automatically. The LOD sequence must start at ``_LOD0`` and contain no gaps — incomplete sets are skipped with a warning.

Copy as Next LOD
----------------

Duplicates each selected mesh object and increments its LOD number in the name (e.g. ``Chair_LOD0`` → ``Chair_LOD1``). The copy is placed in the same collection(s) as the source. The source object must already have a ``_LOD#`` suffix.

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
