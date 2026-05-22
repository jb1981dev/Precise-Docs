.. _deselectactive:

===============
Deselect Active
===============

The **Deselect Active** tool removes the active object from the selection and clears the active object slot — a simple action that is surprisingly impossible to do cleanly in vanilla Blender.

The Blender Limitation
----------------------

In vanilla Blender, :kbd:`Shift+LMB` can deselect an object, but it does not clear the **active object slot**. The previously active object keeps its orange highlight and remains considered "active" by Blender's operators, even though it is technically deselected.

The only native way to have no active object at all is to click on empty space in the viewport — but that clears your **entire selection** at the same time. There is no built-in way to remove just the active object from a larger selection while leaving the rest intact.

How to Use
----------

#. Have any object selected and active in the viewport.
#. Click **Deselect Active**.

The active object is deselected and the active slot is cleared. The rest of your selection remains untouched.

When Is This Useful?
--------------------

A common situation where this matters: you select an object and click **Select Linked** to expand the selection to all of its duplicates. The original object you clicked is still the active one. If you then want to run a batch operation that excludes the original — keeping it as a reference — you would normally have no clean way to do that.

With **Deselect Active** you can drop the original from the selection in one click and proceed with only the instances you care about, with no active object interfering.

It is also useful any time a tool has unexpectedly left the wrong object as active, and you want a clean slate without disrupting the rest of your carefully built selection.
