Version History
===============

.. _version_1_2_00:

Version 1.2.00
--------------

A major feature release adding new access points, significant Multi Transform improvements, and new operators.

Multi Transform
^^^^^^^^^^^^^^^

* **Include toggles (Pos / Rot / Scale):** Three toggles at the top of each value column now control which transform types are applied by **Set All** and by Advanced Copy's **Apply Multi Transform**. The individual **Set P**, **Set R**, and **Set S** buttons are unaffected — they always apply their own type.
* **Modifier keys on Set buttons** — all four buttons (**Set All**, **Set P**, **Set R**, **Set S**) now support :kbd:`LMB` **Set** and :kbd:`Ctrl` **Get** (reads the active object's transform into the value fields). On **Set All**, both shortcuts also respect the Pos / Rot / Scale include toggles.
* **Modifier keys on axis and column toggles** — the six toggle buttons (**X**, **Y**, **Z**, **Pos**, **Rot**, **Scale**) now support :kbd:`Shift` **Round**, :kbd:`Ctrl` **Invert** (sign flip), and :kbd:`Alt` **Reset**, operating directly on their associated value fields without changing the toggle state.

* **Bypass Children:** When a parent and its children are all selected, the transform is applied only to the parent — children are automatically skipped.
* **Redo / F9 panel:** Multi Transform now records its axis toggles, include toggles, and values in the redo panel for post-run adjustment.

Advanced Copy
^^^^^^^^^^^^^

* **Target Merge Mode:** A new alternative workflow for Merged Copy. Click **Set Target** to nominate an existing object; Merged Copy then replaces that object's data-block in-place and updates all of its linked instances automatically. A **T: {name}** button re-selects the target; **X** clears it.
* **Auto Target (Search):** The operator now supports searching for a target by name or pattern. The Search field accepts plain text (substring match), wildcard ``*`` as a placeholder for the source object's name, and wildcard ``%`` to match any sequence of characters. Linked/Unlinked Copy replaces matched objects in-place; Merged Copy swaps the data-block; H Merge targets per hierarchy group.
* **Selection Target:** A new targeting mode where the active object's hierarchy is the source and every other selected hierarchy is a target. Each target hierarchy is replaced in-place at its own position, enabling batch replacement of multiple hierarchies in one operation.
* **Apply Multi Transform — include toggle awareness:** When Apply Multi Transform is on, only the transform types currently enabled by the Pos / Rot / Scale include toggles are applied to the new copies.
* **Redo / F9 panel:** All Advanced Copy settings (Skip Active, Include Children, Clear Parents, Name, Target Collection, etc.) are now available in the redo panel.
* **Wildcard repetition prevention:** When a wildcard pattern's prefix or suffix is already present in the source name, the duplicate part is automatically dropped — e.g. ``New_*`` on ``New_Cube`` produces ``New_Cube`` rather than ``New_New_Cube``. This also handles numeric format variants: ``*_01`` on ``Cube_02`` produces ``Cube_02`` rather than ``Cube_02_01``.

Apply Transforms
^^^^^^^^^^^^^^^^

* **CTRL — Selective Reset:** Hold :kbd:`Ctrl` when clicking Apply Transforms to also reset the toggled transform channels on non-leader instances in each group. If 2 or more instances from the same group were selected, only those instances are reset. If only 1 was selected, all instances in the group are reset.
* **Cross-scene instance handling:** The operator now searches all scenes for instances of the selected data-block, and temporarily unhides objects in excluded or hidden collections to perform the apply.

Find Unlinked Duplicates (new)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* New operator in the **Instance Management** section. Scans the scene for objects that share the same geometry as the selected object(s) — identified by a SHA256 fingerprint — but are not currently linked to them. Matching objects are added to your selection, ready for **Link Selected**.
* Three comparison toggles refine the fingerprint: **UV** (default on), **Mat** (default off), **Attr** (default off). Available as mini-toggles in the panel and in the redo/F9 panel.

Deactivate Selected (new)
^^^^^^^^^^^^^^^^^^^^^^^^^

* New operator in the **Instance Management** section. Clears the active object slot without affecting the current selection — a convenience that is otherwise impossible in vanilla Blender. Supports :kbd:`Ctrl` to also remove the previously active object from the selection entirely.

Select Children (new)
^^^^^^^^^^^^^^^^^^^^^

* New operator in the **Instance Management** section. Additively selects all recursive children of every selected object simultaneously, across any number of separate hierarchies at once. Supports :kbd:`Ctrl` to walk up to the root ancestor of each selected object first, then select that root's entire subtree.

Data Ops (renamed from Data Cycler)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The **Data Cycler** toolset has been renamed to **Data Ops** to reflect its expanded scope beyond cycling.
* **Deep Rename (new):** Renames selected objects and their underlying datablocks simultaneously using a flexible naming pattern. Supports tokens: ``*`` (original name) and ``#`` / ``##`` / ``###`` (1-based selection index, zero-padded). The active object is always #1.
* **Deep Delete (new):** Deletes selected objects and automatically removes any datablocks that become orphaned in the process. :kbd:`Ctrl` also finds and deletes all other objects in the scene sharing the same datablocks.

New Access Points
^^^^^^^^^^^^^^^^^

* **Popup Menu (:kbd:`Ctrl+Y`):** A floating popup containing all toolsets, accessible from anywhere in the 3D Viewport in Object Mode or Edit Mode.
* **Right-Click Context Menus:** All major operators are now available in the right-click menu in both Object Mode and Edit Mode.
* **Header Toolbar:** The IW logo button is permanently present in the 3D Viewport tool header. Click it to toggle inline icon buttons for each toolkit; each opens a popover panel anchored below the header bar.

Preferences
^^^^^^^^^^^

* **Toolset visibility and ordering:** Each toolset now has four controls in the preferences table — show/hide in the N-panel, show/hide in the popup menu, display order, and default expanded state for new scenes.
* **Custom icons:** Each toolset now has a dedicated icon used in the preferences table, N-panel headers, popup menu, right-click menus, and header toolbar.

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
