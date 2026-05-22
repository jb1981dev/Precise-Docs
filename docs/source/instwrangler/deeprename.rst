.. _deeprename:

===========
Deep Rename
===========

The **Deep Rename** tool renames both the selected objects **and** their underlying datablocks (mesh, curve, etc.) simultaneously using a flexible naming pattern. This "deep" behavior makes it ideal for batch-renaming assets while keeping the object names and data names in sync.

The Problem
-----------

In Blender, object names and datablock names are independent. If you rename an object via the outliner, the underlying mesh/curve data keeps its old name. This leads to scenes where the object is called ``Tree_01`` but its mesh data is still called ``Cube.001``.

**Deep Rename** solves this by renaming both at once, in a single operation.

How to Use
----------

#. Select one or more objects in the viewport. The active object will be treated as #1.
#. Click **Deep Rename**.
#. A dialog appears with a text field for your naming pattern. The dialog shows a live preview of what the active object's new name will be.
#. Type your pattern using tokens (see below), or click the **\*** and **#** buttons to insert tokens at the cursor.
#. Click **OK** or press :kbd:`Enter` to apply the new names to all selected objects and their datablocks.

Naming Pattern Tokens
---------------------

``*`` (Asterisk)
    Expands to the **original name** of each object (the name before the rename). Useful for preserving the base name and adding a suffix or prefix.
    
    *Example:* The pattern ``*_MID`` on an object originally named ``Tree`` produces ``Tree_MID``.

``#``, ``##``, ``###``, etc. (Hash signs)
    Expands to the **1-based index** of each object in the selection, zero-padded to match the number of hash signs.
    The **active object is always #1**, regardless of its position in the selection.
    
    * ``#`` → ``1``, ``2``, ``3``, ... (no padding)
    * ``##`` → ``01``, ``02``, ``03``, ... (padded to 2 digits)
    * ``###`` → ``001``, ``002``, ``003``, ... (padded to 3 digits)
    
    *Example:* The pattern ``Asset_###`` produces ``Asset_001``, ``Asset_002``, ``Asset_003``, etc.

You can combine both tokens in a single pattern, or use neither and provide a static name.

Examples
--------

**Example 1: Rename with Index**

Pattern: ``Prop_##``

Result on three selected objects:
    * ``Prop_01``
    * ``Prop_02``
    * ``Prop_03``

**Example 2: Preserve Original Name + Add Suffix**

Pattern: ``*_Collision``

If the selected objects are named ``Box``, ``Sphere``, and ``Cone``:

Result:
    * ``Box_Collision``
    * ``Sphere_Collision``
    * ``Cone_Collision``

**Example 3: Combine Tokens**

Pattern: ``Asset_*_###``

If the selected objects are named ``Rock``, ``Rock``, and ``Rock`` (three linked duplicates):

Result:
    * ``Asset_Rock_001``
    * ``Asset_Rock_002``
    * ``Asset_Rock_003``

Active Object Behavior
----------------------

The **active object is always treated as #1**, regardless of which object you click or the order of selection. This ensures predictable numbering. If you re-select the objects in a different order, the active object still gets index 1.

This is particularly useful when working with linked duplicates — select all instances, make one the active object, and Deep Rename will respect that choice.

Linked Duplicates and Datablocks
---------------------------------

When you have multiple objects sharing the same datablock (linked duplicates), **Deep Rename only renames the datablock once**. All objects pointing to that shared datablock will have their names updated independently, but the datablock gets only one new name (from whichever object is processed first).

This prevents duplicate data and keeps your scene clean:

* Before: Five instances of a ``Box`` object all point to ``CubeData``
* After Deep Rename with pattern ``Box_##``: Objects are ``Box_01``, ``Box_02``, ..., ``Box_05``, and they all point to ``Box_01Data``

Live Preview
------------

The dialog displays a live preview of what the **active object's name** will become. As you type, the preview updates immediately, helping you verify your pattern before committing.
