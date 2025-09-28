.. _version_1_0:

===========
Version 1.0
===========

*Released: September 28, 2025*

This is the first stable public release of the **Instance Wrangler** addon. This version provides a complete toolkit for advanced instance and transform management directly in the 3D Viewport.

Key Features
------------

**Multi Transform**
    * Precisely edit Position, Rotation, and Scale for multiple objects at once using an intuitive, axis-driven grid.
    * Use **Standard Mode** for simple absolute or relative changes to each object.
    * Use the powerful **Active Leads Mode** to treat the active object as a "fake parent," allowing you to transform an entire selection as a single, cohesive group.

**Instance Management**
    * A comprehensive suite of tools for managing linked duplicates:
    * **Modifier Sync:** Sync modifier stacks from a leader object to its instances, either globally or limited to a selection.
    * **Apply Modifiers:** A robust tool that bakes modifiers by converting objects to meshes, while intelligently handling instance groups.
    * **Apply Transforms:** Solves a core Blender limitation by allowing you to apply transforms to instanced objects without breaking their data links.
    * **Link/Unlink Tools:** Includes a powerful **Link Selected** operator that can convert object types on the fly, and two unlinking operators (**Make Single User** and **Make Group Unique**) for breaking links individually or as a group.

**Data Cycler**
    * Rapidly audition different assets or LODs in-place with the **Cycle Data** (**Next/Prev**) and **Randomize Data** tools.
    * Use the **Filter** field to instantly narrow down the list of available data-blocks to cycle through.

**Advanced Copy**
    * **Merged Copy:** Creates a single, clean, joined mesh from a diverse selection of objects, with advanced control over the final pivot point and parenting.
    * **Linked Copy:** Creates new linked duplicates with powerful options for offsetting and preserving or clearing parent-child hierarchies.
    * Both tools share common settings for placing new objects in specific collections and controlling the final selection state.
