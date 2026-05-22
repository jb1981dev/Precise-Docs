.. _selectchildren:

===============
Select Children
===============

The **Select Children** tool additively selects all recursive children of every object currently in your selection — across as many separate hierarchies as you have selected simultaneously.

The Blender Limitation
----------------------

Vanilla Blender provides two ways to select child objects: :menuselection:`Select --> Select Grouped --> Children Recursive`, and the Select Hierarchy shortcut. Both work only from the **active object**. No matter how many hierarchy roots you have selected, Blender will only expand children for the single active one.

If your scene has ten separately parented groups and you want to select all of their children, you would need to either process each root one by one, or write a custom script. Instance Wrangler handles this in a single click.

How to Use
----------

#. Select one or more parent objects in the viewport.
#. Click **Select Children**.
#. All recursive children of every selected object are added to the selection.

The operation is **additive** — nothing is deselected. The active object is also preserved exactly as it was.

Key Behavior
------------

* **Multiple Hierarchies at Once:** The operator processes every object in the selection simultaneously. Selecting three separate hierarchy roots and clicking **Select Children** will expand all three in one operation.

* **Fully Recursive:** It does not just select direct children. It walks the entire parent-child chain downward, so grandchildren, great-grandchildren, and so on are all included.

* **Non-Destructive to Selection:** The tool never deselects anything. Existing selection is preserved and children are added on top of it.

* **Skips Inaccessible Objects:** Children that are hidden or located in a disabled or excluded collection are skipped silently. The operator reports the total number of child objects it was able to select.

Practical Example
-----------------

Suppose you have two separate prop hierarchies in your scene — ``Crate_Root`` with five child pieces, and ``Barrel_Root`` with three child pieces. In vanilla Blender, selecting both roots and running Select Grouped would only add children of whichever is the active object.

With **Select Children**, select both roots and click the button once. All eight child objects from both hierarchies are immediately added to your selection, ready for a batch operation.

This is particularly useful before exporting, applying modifiers across a rig, or using any other tool that should cover an entire set of hierarchies at once.
