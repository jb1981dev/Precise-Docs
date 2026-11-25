=========
Smart LOD
=========

**Smart LOD** generates LOD1, LOD2 and LOD3 from a selected LOD0 object. Instead of reducing
to a fixed percentage, you set how much each LOD may differ from LOD0 (in shape, texture
shift and shading) and Smart LOD removes as many triangles as it can within those limits.

Sharp edges, UV seams and material borders are protected, and every LOD is measured against
LOD0 directly, so errors never stack up from one LOD to the next.

Quick Start
-----------

1. Select one or more mesh objects (your LOD0).
2. Pick a **Preset** under **Settings**, or start with the default *Balanced* preset.
3. Click **Generate LODs**.

The LOD objects are created next to LOD0, in the same collection(s), and named with the active
**LOD Format** (see :doc:`assetpreview`). Objects without a LOD suffix are renamed to LOD0
first, the same way **Make LOD** does. A summary for each LOD (triangle count and percentage of
LOD0) is shown in the panel.

Panel
-----

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **LOD1 / LOD2 / LOD3**
     - Choose which LOD levels to generate. Settings are only shown for the enabled levels.
   * - **Generate LODs**
     - Builds the enabled LODs for every selected mesh object.
   * - **Settings**
     - Expands the preset selector, the settings for each enabled LOD, and the shared settings.
       While collapsed, the results of the last run are listed below it; while expanded, each
       result is shown in the header of its LOD.

A result marked **capped** means the LOD was reduced beyond its quality limits to reach its
**Max Tris** value (see below).

Presets
-------

A preset stores the settings for LOD1–LOD3: which levels are enabled, Max Tris, the quality
limits, the locks and the cleanup options. The shared settings (Texture Size, Custom Normals,
Replace Existing LODs) are not part of a preset.

Pick a preset from the **Preset** dropdown to apply it. Picking it again restores its values
after you have changed them. Once a setting differs from the preset, the dropdown shows
*(edited)* after its name.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Built-in Preset
     - Use
   * - **Conservative**
     - Tight limits. Stays very close to LOD0; removes fewer triangles.
   * - **Balanced**
     - The default settings. A good starting point for most assets.
   * - **Aggressive**
     - Loose limits with triangle caps of 50% / 25% / 10%, plus small-island removal on LOD2
       and LOD3 and hidden-face removal on LOD3.

Managing Presets
^^^^^^^^^^^^^^^^

Click the gear button next to the dropdown to open the preset editor:

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **+**
     - Adds a new preset from the current settings.
   * - **−**
     - Removes the selected preset.
   * - **✓**
     - Overwrites the selected preset with the current settings.
   * - **Rename**
     - Double-click a preset name in the list.

Changes are saved when you click **OK** and discarded with **Cancel**. Built-in presets are
marked with a lock and cannot be changed or removed. Your own presets are stored in Blender's
user folder for the extension, so they are kept when the addon is updated.

Per-LOD Settings
----------------

Each enabled LOD has its own settings. The quality limits (Shape, UV, Normal) decide how far a
LOD is reduced.

Link LODs
^^^^^^^^^

With **Link LODs** on (the default), every LOD stays at least as aggressive as the LOD before
it. When you change a setting on one LOD, the same setting on the other LODs is pushed along
as soon as they would end up out of order:

* Making a LOD more aggressive pushes the later LODs. With Max Tris at 100% on every LOD,
  dragging LOD1 down to 75% takes LOD2 and LOD3 with it.
* Making a LOD less aggressive pushes the earlier LODs. Dragging LOD3 up past LOD2 takes LOD2
  with it.

LODs that are already in order don't move, and pushed values stay where they were pushed. All
sliders and the **Gaps**, **Hidden** and **Islands** checkboxes are linked, including those of
LODs that are switched off. The **Sharps** and **Seams** locks are not linked.

Presets are always applied exactly as saved. Turn **Link LODs** off to set each LOD freely.

Sizes relative to the asset
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Shape**, **Gaps** and **Islands** are set as a percentage of LOD0's size, measured along the
diagonal of its bounding box (100% = the full diagonal). Each selected object is measured on
its own, so the same settings and presets work the same on a small prop and on a building, and
object scale does not matter.

The label of each of these fields shows what the percentage means in scene units for the
active object, for example *Shape (≈ 1.2 cm)*.

.. note::
   On long, thin assets (fences, pipes, cables) the diagonal mostly follows the length, so a
   small percentage can still be larger than the asset is thick. Keep these values low for
   such assets and check the size shown next to the field.

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Max Tris**
     - A cap on the triangle count, as a percentage of LOD0. The quality limits are used first;
       only if they leave more triangles than this cap is the LOD reduced further, past the
       limits, until the cap is reached. **100%** means no cap. The result is then marked
       *capped*.
   * - **Shape**
     - The maximum distance the LOD's surface may move away from LOD0, as a percentage of
       LOD0's size.
   * - **UV**
     - The maximum texture shift, in pixels, at the **Texture Size** set below.
   * - **Normal**
     - The maximum change in surface angle (shading) compared to LOD0.
   * - **Lock: Sharps**
     - Vertices on sharp edges may only slide along their sharp edge. When off, sharp edges may
       move slightly, within the Shape limit.
   * - **Lock: Seams**
     - Vertices on UV seams may only slide along their seam. When off, seams may move slightly,
       within the UV limit, which removes more triangles.
   * - **Gaps**
     - Visually closes narrow gaps between separate pieces of the mesh by moving the facing
       vertices towards each other. The value is the widest gap that is closed, as a percentage
       of LOD0's size. No faces are added and pieces are not welded.
   * - **Hidden**
     - Removes faces that are buried in, or pressed against, other closed pieces of the same
       mesh. The value is how much of a face must be hidden before it is removed (95% by
       default).
   * - **Islands**
     - Removes separate pieces that are small compared to the whole asset: a piece is removed
       when its bounding box diagonal is smaller than this percentage of LOD0's diagonal.

Shared Settings
---------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Texture Size**
     - The texture resolution used to measure the UV limit in pixels. Set it to the resolution
       the asset will use in-game.
   * - **Custom Normals**
     - What to do when LOD0 has custom normals. **Off**: no custom normals on the LODs.
       **Carry**: copy LOD0's normals. **Fit to LOD0** (default): re-fit the normals so the
       LOD's shading matches LOD0 as closely as possible; hard edges stay hard.
   * - **Replace Existing LODs**
     - When a LOD object already exists, replace its mesh. When off, existing LODs are skipped.

Settings are saved with the .blend file.

What Is Kept
------------

Every LOD keeps LOD0's UV maps, color attributes, vertex groups, materials, sharp and seam
marks, flat/smooth shading and other face and point attributes. Modifiers on LOD0 are applied
to the LOD meshes; the LOD objects themselves get no modifiers. Shape keys are not carried
over.

Tips
----

* Start from a preset and adjust one LOD at a time. Generate, compare with LOD0 (see
  :doc:`assetpreview` for the LOD visibility hotkeys), and loosen or tighten from there.
* If a LOD keeps too many triangles, loosen **Shape**, **UV** or **Normal** first. Use
  **Max Tris** when you need a hard triangle budget.
* Turning off **Lock: Seams** often removes many more triangles on assets with many UV islands.
* Detailed measurements for each LOD (largest shape error, UV and shading error) are printed to
  the system console.
