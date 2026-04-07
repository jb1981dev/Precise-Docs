Version History
===============

.. _version_1_2_00:

Version 1.2.00
--------------

A major feature release adding new access points, significant Multi Transform improvements, and new operators.

Multi Transform
^^^^^^^^^^^^^^^

* **Include toggles (Pos / Rot / Scale):** Three toggles at the top of each value column now control which transform types are applied by **Set All** and by Advanced Copy's **Apply Multi Transform**. The individual **Set P**, **Set R**, and **Set S** buttons are unaffected — they always apply their own type.
* **Modifier keys on all Set buttons** — all four buttons (**Set All**, **Set P**, **Set R**, **Set S**) now support:

  :kbd:`LMB`
      **Set** — apply values to the selection.

  :kbd:`Ctrl`
      **Get** — read the active object's current transform into the value fields (respects axis toggles).

  :kbd:`Shift`
      **Round** — snap the fields to the nearest clean step: 0.5 m for Position, 1° for Rotation, 0.1 for Scale (respects axis toggles).

  :kbd:`Alt`
      **Reset** — reset the fields to their defaults: Position → 0, Rotation → 0°, Scale → 1 (respects axis toggles).

  For **Set All**, :kbd:`Ctrl`, :kbd:`Shift`, and :kbd:`Alt` also respect the Pos / Rot / Scale include toggles.

* **Bypass Children:** When a parent and its children are all selected, enabling this option skips the children — only the parent receives the transform.
* **Redo / F9 panel:** Multi Transform now records its axis toggles, include toggles, and values in the redo panel for post-run adjustment.
* **Active Leads fix:** Fixed a case where Active Leads mode could silently fail when no valid active object was present.

Advanced Copy
^^^^^^^^^^^^^

* **Target Merge Mode:** A new alternative workflow for Merged Copy. Click **Set Target** to nominate an existing object; Merged Copy then replaces that object's data-block in-place and updates all of its linked instances automatically. A **T: {name}** button re-selects the target; **X** clears it.
* **Apply Multi Transform — include toggle awareness:** When Apply Multi Transform is on, only the transform types currently enabled by the Pos / Rot / Scale include toggles are applied to the new copies.
* **Clear Parents reliability fix:** The clear-parents step now reliably runs before Apply Multi Transform for all three copy types (Linked, Unlinked, Merged).
* **Redo / F9 panel:** All Advanced Copy settings (Skip Active, Include Children, Clear Parents, Name, Target Collection, etc.) are now available in the redo panel.

Apply Transforms
^^^^^^^^^^^^^^^^

* **CTRL — Selective Reset:** Hold :kbd:`Ctrl` when clicking Apply Transforms to also reset the toggled transform channels on non-leader instances in each group. If 2 or more instances from the same group were selected, only those instances are reset. If only 1 was selected, all instances in the group are reset.
* **Cross-scene instance handling:** The operator now searches all scenes for instances of the selected data-block, and temporarily unhides objects in excluded or hidden collections to perform the apply.
* **Text and 2D Curve handling:** These object types only support scale apply. If Position or Rotation is toggled on and one of these objects is in the selection, those channels are skipped and a notice is shown; Scale still applies normally.

Find Unlinked Duplicates (new)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* New operator in the **Instance Management** section. Scans the scene for objects that share the same geometry as the selected object(s) — identified by a SHA256 fingerprint — but are not currently linked to them. Matching objects are added to your selection, ready for **Link Selected**.
* Three comparison toggles refine the fingerprint: **UV** (default on), **Mat** (default off), **Attr** (default off). Available as mini-toggles in the panel and in the redo/F9 panel.

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
