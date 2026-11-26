Version History
===============

.. _version_1_2_0:

Version 1.2.0
-------------

A major feature release adding new access points, new operators, and significant improvements across existing tools.

Multi Transform
^^^^^^^^^^^^^^^

* **Include toggles (Pos / Rot / Scale):** Control which transform types are affected by **Set All** and Advanced Copy's **Apply Multi Transform**.
* **Modifier keys on Set buttons:** :kbd:`Ctrl` reads the active object's transform into the value fields. :kbd:`Alt` resets the selected objects' transforms, to the world origin or (with **Relative** on) to their parent.
* **Modifier keys on axis/column toggles:** :kbd:`Shift` rounds, :kbd:`Ctrl` inverts (sign flip), :kbd:`Alt` resets the associated values.
* **Parents and children:** When a parent and its children are both selected, Set only transforms the parent; the children follow it.
* **Redo / F9 panel:** Axis toggles, include toggles, and values are now recorded for post-run adjustment.

Advanced Copy
^^^^^^^^^^^^^

* **Target Merge Mode:** Nominate an existing object as a target; Merged Copy replaces its data-block in-place and updates all linked instances automatically.
* **Auto Target (Search):** Search for a target by name or pattern instead of manually setting one. Supports plain text, ``*`` (source name placeholder), and ``%`` (wildcard).
* **Selection Target:** Use the active object's hierarchy as the source and every other selected hierarchy as a target, enabling batch in-place replacement in one operation.
* **Apply Multi Transform** now respects the Pos / Rot / Scale include toggles.
* **Redo / F9 panel:** All Advanced Copy settings are now recorded for post-run adjustment.
* **Wildcard repetition prevention:** Duplicate prefixes or suffixes in the resolved name are automatically dropped.
* **Skip Active guard:** When Skip Active would leave nothing to copy, a confirmation offers to run the copy with Skip Active turned off.

Apply Transforms
^^^^^^^^^^^^^^^^

* **Ctrl — Selective Reset:** Resets the toggled transform channels on non-leader instances in the group.
* **Hidden instance handling:** Instances that are hidden or in excluded collections are temporarily revealed to complete the apply, then hidden again. Instances that only exist in another scene are reported with a clear message instead of being skipped silently.

Instance Management (new operators)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Find Unlinked Duplicates:** Scans the scene for objects sharing the same geometry as the selection but not currently linked to them. Matching objects are added to the selection, ready for **Link Selected**. UV, material, and attribute comparisons are individually toggleable.
* **Deactivate Selected:** Clears the active object slot without affecting the current selection. :kbd:`Ctrl` also removes the previously active object from the selection.
* **Select Children:** Additively selects all recursive children of every selected object, across multiple hierarchies at once. :kbd:`Ctrl` walks up to the root ancestor first, then selects the full subtree.
* **Link Selected with an Empty:** When the active object has no data-block to share (e.g. an Empty), the selected objects are replaced by copies of it, keeping their name, transform, parent and children.

Data Ops (renamed from Data Cycler)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Toolset renamed** from Data Cycler to **Data Ops** to reflect its expanded scope.
* **Deep Rename (new):** Renames selected objects and their underlying datablocks simultaneously using a pattern with ``*`` (original name) and ``#`` / ``##`` / ``###`` (index) tokens.
* **Deep Delete (new):** Deletes selected objects and removes any orphaned datablocks. :kbd:`Ctrl` also deletes all other objects in the scene sharing the same datablocks.

New Access Points
^^^^^^^^^^^^^^^^^

* **Popup Menu (:kbd:`Ctrl+Y`):** A floating popup with all toolsets, accessible anywhere in the 3D Viewport.
* **Right-Click Context Menus:** All major operators are available in the right-click menu in Object Mode and Edit Mode.
* **Header Toolbar:** An IW logo button in the tool header toggles inline icon buttons; each opens a popover panel for its toolset.

Preferences
^^^^^^^^^^^

* **Toolset visibility and ordering:** Control show/hide in the N-panel and popup, display order, and default expanded state per toolset.
* **Custom icons:** Each toolset has a dedicated icon used throughout the UI.

Fixes
^^^^^

* **Get rotation** (:kbd:`Ctrl`-click and right-click Get) now works for objects using quaternion or axis-angle rotation, instead of returning 0.
* **Unlinked Copy** always gives copies their own data, even when Blender's *Preferences > Editing > Duplicate Data* would share it, and no longer renames the original's data.
* **Link Selected** keeps the full transform of replaced objects and their children, in any rotation mode.
* **Find Unlinked (Attr)** ignores Blender's internal attributes and UV maps, so identical meshes are no longer missed.
* **Cycle Data** now cycles NURBS curves (e.g. *Path*) together with other curves instead of with surfaces.
* **Cycle Data** and **Deep Delete** support Grease Pencil objects in Blender 4.3–4.5.
* The right-click Set / Get / Round / Invert / Reset items only appear on Instance Wrangler's own value fields, not on Blender fields with the same name.

.. _version_1_1_30:

Version 1.1.30
--------------

*Released: February 1, 2026*

This is the latest stable release of the **Instance Wrangler** addon. This version provides a complete toolkit for advanced instance and transform management directly in the 3D Viewport.

Key Features
^^^^^^^^^^^^

**Multi Transform**
   * Precisely edit Position, Rotation, and Scale for multiple objects at once using an intuitive, axis-driven grid.
   * Use **Standard Mode** for simple absolute or relative changes to each object.
   * Use the powerful **Active Leads Mode** to treat the active object as a "fake parent," allowing you to transform an entire selection as a single, cohesive group.

**Advanced Copy**
   * **Merged Copy:** Creates a single, clean, joined mesh from a diverse selection of objects, with advanced control over the final pivot point and parenting.
   * **Linked Copy:** Creates new linked duplicates with powerful options for offsetting and preserving or clearing parent-child hierarchies.
   * **Unlinked Copy:** Creates independent copies (Shift+D style) while utilizing the full suite of placement and hierarchy options.
   * **Apply Multi-Transform:** Advanced Copy can directly utilize the Multi Transform values for positioning and scaling new copies.
   * **Skip Active:** Lets you use the active object as a pivot reference without duplicating it in the final result.

**Instance Management**
   * A comprehensive suite of tools for managing linked duplicates:
   * **Modifier Sync:** Sync modifier stacks from a leader object to its instances, either globally or limited to a selection.
   * **Apply Modifiers:** A robust tool that bakes modifiers by converting objects to meshes, while intelligently handling instance groups.
   * **Apply Transforms:** Solves a core Blender limitation by allowing you to apply transforms to instanced objects without breaking their data links.
   * **Link/Unlink Tools:** Includes a powerful **Link Selected** operator that can convert object types on the fly, and two unlinking operators (**Make Single User** and **Make Group Unique**) for breaking links individually or as a group.

**Data Cycler**
   * Rapidly audition different assets or LODs in-place with the **Cycle Data** (**Next/Prev**) and **Randomize Data** tools.
   * Use the **Filter** field to instantly narrow down the list of available data-blocks to cycle through.
