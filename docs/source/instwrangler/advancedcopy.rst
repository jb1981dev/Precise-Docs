.. _advancedcopy:

==============
Advanced Copy
==============

The **Advanced Copy** section provides two powerful operators for creating new objects from your selection: **Merged Copy** and **Linked Copy**.

* **Merged Copy** is used to create a single, new mesh from a potentially diverse selection of objects.
* **Linked Copy** is used to create new linked duplicates (instances) of your selection, with advanced options for placement and hierarchy.

Both operators share a set of common options for controlling the placement, parenting, collection, and final selection state of the newly created objects.

.. _mergedcopy:

Merged Copy
===========

The **Merged Copy** operator is a comprehensive tool for creating a **single, clean, game-ready mesh** from a selection of multiple, potentially diverse objects. It automates the process of duplicating, converting, joining, and positioning objects. This is ideal for creating simplified proxy models, preparing assets for game engines, or combining parts for 3D printing.

Its behavior is controlled by the **Merged Name** field and the settings in the **Common Options** section below.

Defining the Origin (Pivot Point)
---------------------------------

The origin of the new merged object is determined by your selection:

* If you have a valid **active object** in your selection, its world-space location is used as the pivot point.
* If there is no valid active object, the origin is set to the **center of the new mesh's bounding box**.

Merged Name
-----------
* **(Merged Copy Only)** The name that will be given to the final, single object and its new mesh data.

.. _linkedcopy:

Linked Copy
===========

The **Linked Copy** operator creates new **linked duplicates** (:kbd:`Alt+D` instances) of your selection. It is a non-destructive way to create more instances while keeping them linked to the same underlying object data.

Its behavior is controlled entirely by the settings in the **Common Options** section below.

Common Options
==============

These settings are shared by both the **Merged Copy** and **Linked Copy** operators.

Clear Parents
-------------
This toggle controls how parent-child relationships are handled for the newly created objects. It behaves differently for each operator.

* For **Merged Copy**:
    * **ON (Default):** The final merged object will have no parent.
    * **OFF:** The operator will attempt to re-parent the final merged object to the parent of the original selection (e.g., the parent of the original active object, or a parent common to all selected objects).

* For **Linked Copy**:
    * **ON (Default):** The new duplicates are unparented from each other, creating a 'flat' selection of new instances.
    * **OFF:** The original parent-child hierarchy is preserved in the duplicated set. The **Offset** is then only applied to the top-level parents, moving the entire hierarchy as a single unit.

Select New
----------
This toggle controls the final selection state after the operation is complete.

* **ON (Default):** The newly created object(s) will be selected.
* **OFF:** The original selection will be restored.

Offset
------
These controls determine the final position of the newly created object(s).

* **Offset (X, Y, Z fields):** The numeric coordinates for the offset.
* **Rel (Relative Toggle):** Controls how the offset is applied.
* **Offset Button:** A shortcut to reset the Offset fields to ``(0, 0, 0)``.

Target Collection
-----------------
This dropdown menu controls which collection the newly created object(s) will be placed in.

* **Automatic (Default):** The operator intelligently determines the most logical collection based on your original selection. The behavior differs for each operator:
    * For **Merged Copy**, the new, single mesh is placed according to the following priority:
        #. It is placed in the **collection of the original active object** (if one was validly selected).
        #. If there was no valid active object, it is placed in the **Scene Collection** (the root of the outliner).
    * For **Linked Copy**, each new duplicate is placed into the **same collection(s) as its original counterpart**. This preserves your scene's organization. For example, if you duplicate objects from a "Props" collection and a "Characters" collection at the same time, the new props will end up in "Props" and the new characters will end up in "Characters".

* **Explicit Choice:** You can select any collection in the scene (including the root **Scene Collection**) to force all new objects into that specific collection, overriding the automatic behavior.
