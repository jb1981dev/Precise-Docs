Cycle Data
==========

The **Cycle Data** tool is a powerful feature for rapid iteration and asset swapping. It allows you to replace an object's underlying **Object Data** (like its mesh or curve geometry) with the next or previous data-block of the same type available in your Blender file.

Think of it as quickly trying on different versions of an asset without ever moving the object itself. The object's location, rotation, scale, and even its modifiers are all preserved; only its core data is swapped.

How It Works
------------

When you click **Next** or **Prev**, the operator performs the following steps for each selected object:

#. It identifies the object's type (e.g., ``Mesh``, ``Curve``, ``Text``).
#. It finds all other data-blocks of that same type currently in your ``.blend`` file.
#. It sorts these data-blocks **alphabetically** by name.
#. It then replaces the object's current data with the next or previous one in that sorted list.

The cycle will automatically wrap around. For example, clicking **Next** when on the last data-block in the list will cycle back to the first one.

How to Use
----------

The workflow is designed for experimentation:

#. Select one or more objects you wish to change.
#. Click the **Next** or **Prev** buttons to cycle through the available data-blocks.

You can select multiple objects at once, even of different types. Each object will cycle independently within its own category (Meshes will only cycle with other Meshes, Curves with other Curves, etc.).

Example Workflow: Auditioning Assets
------------------------------------

This tool is invaluable for tasks like set dressing or environment design.

Imagine you have placed a generic ``Tree_Placeholder`` object in several locations in your scene. Elsewhere in your file, you have several detailed tree assets with data-blocks named ``Tree_Oak``, ``Tree_Pine``, and ``Tree_Willow``.

Instead of manually changing the data-block for each placeholder, you can simply:

#. Select one or more of the ``Tree_Placeholder`` objects.
#. Click the **Next** button. The placeholder will instantly transform into ``Tree_Oak``.
#. Click **Next** again to see ``Tree_Pine``, and again for ``Tree_Willow``.

This allows you to audition different assets in place, saving a significant amount of time compared to navigating the Object Data dropdown menu for each object individually.

Example Workflow: Swapping Levels of Detail (LODs)
--------------------------------------------------

This tool is also ideal for managing **LODs** (Levels of Detail) for game assets or optimizing heavy scenes.

For this to work seamlessly, ensure your data-blocks are named in alphabetical order, for example: ``MyAsset_LOD0``, ``MyAsset_LOD1``, and ``MyAsset_LOD2``.

#. Your scene is currently populated with the high-detail ``MyAsset_LOD0`` instances.
#. Use the **Select Linked** tool to select all instances of ``MyAsset_LOD0``.
#. Click **Next** once. All selected objects will instantly switch to use the ``MyAsset_LOD1`` data.
#. Click **Next** again to switch them all to the low-poly ``MyAsset_LOD2``.
#. You can use **Prev** to cycle back up to higher detail levels.

This provides a simple, in-viewport method to globally change the detail level of your assets for performance testing or preparing different versions for export.
