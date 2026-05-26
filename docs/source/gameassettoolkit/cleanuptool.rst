============
Cleanup Tool
============

The **Cleanup Tool** removes mesh data, edge marks, and object data from selected mesh objects in bulk. Use it to strip export-irrelevant data before handing off assets.

Filters
-------

Click **Filters** to expand the filter panel. Checkboxes control which data types the cleanup operator will remove. Two quick-action buttons at the bottom of the panel let you toggle all checkboxes on/off or reset them to their defaults.

Mesh Data
^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **UV Maps**
     - Removes all UV layers.
   * - **Vertex Colors**
     - Removes all vertex color layers.
   * - **Shape Keys**
     - Removes all shape keys (including basis).
   * - **Vertex Groups**
     - Clears all vertex groups.
   * - **Custom Normals**
     - Clears custom split normals data.
   * - **Materials**
     - Clears all material slots.
   * - **Unused Mat Slots**
     - Removes material slots that are not assigned to any face.

Edge Data
^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Edge Sharps**
     - Clears all sharp edge marks.
   * - **Edge Creases**
     - Clears all edge crease values.
   * - **Edge Bevels**
     - Clears all edge bevel weights.
   * - **Edge Seams**
     - Clears all UV seam marks.

Object Data
^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - **Modifiers**
     - Removes all modifiers.
   * - **Animation Data**
     - Removes all animation data (actions, NLA tracks, drivers).
   * - **Constraints**
     - Removes all object constraints.
   * - **Custom Properties**
     - Clears all custom properties from the object.

Cleanup Selection
-----------------

Applies all enabled removals to every selected mesh object. Non-mesh objects in the selection are silently skipped.
