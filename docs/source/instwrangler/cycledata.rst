.. _cycledata:

==========
Cycle Data
==========

The **Cycle Data** tool is a powerful feature for rapid iteration and asset swapping. It allows you to replace an object's underlying **Object Data** (like its mesh or curve geometry) with another data-block of the same type available in your Blender file.

Think of it as quickly trying on different versions of an asset without ever moving the object itself. The object's location, rotation, scale, and even its modifiers are all preserved; only its core data is swapped.

.. raw:: html

   <iframe width="700" height="395" src="https://www.youtube.com/embed/dd3mXKKQt6k?si=TiFg6e3Zyk9GaseU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

How It Works
------------

When you click **Next**, **Prev**, or **Random**, the tool collects all data-blocks of the same type as the selected object(s) from your ``.blend`` file, sorts them **alphabetically**, applies any active **Filter**, and swaps each object's data to the chosen entry. Each selected object cycles independently within its own type.

The Next/Prev cycle behavior depends on the filter mode (see `Filter Modes`_ below).

.. dropdown:: Animation: Cycle Data
   :open:

   .. figure:: images/cycledata.gif
      :align: center

   *Cycling through object data on one or more objects.*

How to Use
----------

The basic workflow:

#. Select one or more objects you wish to change (the tool also works on children if enabled).
#. Optionally enable **Filter** and enter a filter pattern to narrow your choices.
#. Click **Next**, **Prev**, or **Random** to change the data.

You can select multiple objects at once, even of different types. Each object will cycle independently within its own category and respects the **Include Children** setting.

Settings and Controls
---------------------

**Include Children**
    When enabled (default: on), the cycle operation also applies to all children of selected objects, recursively walking the entire hierarchy. When disabled, only the directly selected objects are affected.
    
    *Example: Select a rig root and click Next — the tool cycles data for the root and every bone/child object in the hierarchy.*

**Filter Toggle**
    Enables or disables the filter field. When off, the tool cycles through every data-block of the same type. When on, the filter narrows the candidates.

**Filter Field**
    A text pattern that narrows which data-blocks are available to cycle through. Supports plain substring matching or group-based cycling using ``%``. See `Filter Modes`_ below for details.

Filter Modes
------------

The filter works in two distinct modes depending on whether you use the special ``%`` character.

Plain Text Mode (No ``%``)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Type any text to filter by substring matching. The filter is case-insensitive and matches any data-block whose name *contains* your text.

* Candidate pool: all blocks matching the substring
* Cycle behavior: **Wraps around** — clicking **Next** on the last block cycles back to the first

*Examples:*

* Filter: ``LOD`` matches all blocks named ``Cube_LOD0``, ``Cylinder_LOD2``, ``Tree_LOD1``, etc. All three objects cycle through the entire shared pool.
* Filter: ``Rock`` matches ``Rock_001``, ``Rock_002``, ``My_Rock``, etc.
* Filter: ``v2`` matches ``Char_v2``, ``Prop_v2``, ``Asset_v2`` — all data containing the substring.

Group Mode (With ``%``)
~~~~~~~~~~~~~~~~~~~~~~~

Use ``%`` as a placeholder to define separate cycling groups per object. Each object cycles within its own group based on the part of the name that varies.

* ``%`` marks the variable part of the naming pattern
* Each object groups candidates based on its current data name
* Cycle behavior: **Clamps at both ends** — clicking **Prev** at the first option stays there (doesn't wrap)

This is ideal for **Levels of Detail (LODs)** or versioned assets where each base object should have its own set of variants.

*Examples:*

**Pattern: ``_LOD%``**

Suppose you have:
    * ``Cube`` using ``CubeMesh_LOD0``
    * ``Cylinder`` using ``CylinderMesh_LOD0``
    * Available blocks: ``CubeMesh_LOD0``, ``CubeMesh_LOD1``, ``CubeMesh_LOD2``, ``CylinderMesh_LOD0``, ``CylinderMesh_LOD1``, ``CylinderMesh_LOD2``

When you click **Next** on ``Cube``:
    * It cycles through only ``CubeMesh_LOD0 → LOD1 → LOD2``
    * It does NOT cycle to ``CylinderMesh_*`` (separate group)
    * Clicking **Prev** on ``LOD0`` stays at ``LOD0`` (clamping, no wrap)

**Pattern: ``_v%``**

Blocks named ``Prop_v1``, ``Prop_v2``, ``Prop_v3``, ``Asset_v1``, ``Asset_v2``:
    * ``Prop`` objects cycle through ``v1 → v2 → v3``
    * ``Asset`` objects cycle through ``v1 → v2``
    * Each object stays within its own version group

Filter Examples
---------------

**Auditioning a single variant type:**

Filter: ``_LOD0`` → cycle through only LOD0 meshes across your scene. Useful for checking low-poly coverage.

**Browsing versions of one asset:**

Filter: ``Prop_`` → cycle through all versions of ``Prop_*`` blocks. Other assets are excluded.

**Random button with filtering:**

Select ten objects, set filter to ``Rock_``, and click **Random** → each object gets a random rock variant. The **Random** button respects both plain text and group mode filters, and avoids assigning an object its current data-block.

.. dropdown:: Animation: Filter
   :open:

   .. figure:: images/cycledata_filter.gif
      :align: center

   *Using a filter to limit the range of cycled objects.*

Example Workflows
-----------------

**Auditioning Assets**
    This tool is invaluable for tasks like set dressing. If you have a ``Tree_Placeholder`` object, you can select it and click **Next** repeatedly to cycle through all available tree models (``Tree_Oak``, ``Tree_Pine``, etc.) to see which one fits best in your scene.

.. dropdown:: Animation: Auditioning assets
   :open:

   .. figure:: images/cycledata_staging.gif
      :align: center

   *Auditioning trees and rocks and using the randomize and filter functionality.*

**Swapping Levels of Detail (LODs)**
    This tool is also ideal for managing **LODs**. If your assets are named alphabetically (e.g., ``MyAsset_LOD0``, ``MyAsset_LOD1``), you can select all ``_LOD0`` instances and click **Next** to switch them all to ``_LOD1`` instantly. You can also use the **Filter** field: typing ``LOD2`` and clicking **Next** will jump all selected objects directly to their ``_LOD2`` version.
