.. _deepdelete:

===========
Deep Delete
===========

The **Deep Delete** tool deletes selected objects and automatically removes any datablocks (mesh, curve, etc.) that become orphaned in the process. With the :kbd:`Ctrl` modifier, it also finds and deletes all other objects in the scene that share the same datablocks.

In Blender, deleting an object does not automatically delete its datablock. If you had three linked instances of a mesh and you delete all three objects, the underlying mesh data remains in the file as "orphaned" data — data which is not used anywhere. Blender will eventually clean them up zero user datablocks when you save and reopen the file, but until then they will stick around. This can be inconvenient when using functions like cylcle data, which will still cycle through orphaned datablocks.

**Deep Delete** cleans this up automatically, keeping your scene efficient.

How to Use
----------

#. Select one or more objects in the viewport.
#. Click **Deep Delete** to remove them and clean up their unused datablocks.

Modifier Keys
-------------

:kbd:`LMB`
    **Delete Selected** — removes the selected objects and automatically deletes any datablocks that no longer have any users (objects pointing to them). If other objects in the scene still use the datablock, it is preserved.

:kbd:`Ctrl`
    **Delete Linked** — deletes the selected objects **and** finds every other object in the scene that shares the same datablocks, then deletes all of them together. Also cleans up orphaned datablocks afterward.

Orphaned Datablocks
-------------------

A datablock becomes "orphaned" when no object uses it anymore. For example:

* You have three instances of a cube mesh (all using ``Cube`` datablock).
* You delete all three objects.
* The ``Cube`` datablock now has zero users and becomes orphaned.
* Normal Blender delete leaves the datablock behind; **Deep Delete** removes it.

Orphaned datablocks accumulate over the course of a project. While harmless, they increase file size and clutter your datablock list. Regularly running **Deep Delete** on objects you no longer need keeps your file clean.

Practical Example
-----------------

Suppose your scene contains:

* Five instances of a ``Tree`` mesh (all using ``TreeMesh`` datablock).
* Three instances of a ``Rock`` mesh (all using ``RockMesh`` datablock).

You select two of the five trees and click **Deep Delete** (LMB):

* Those two tree objects are deleted.
* ``TreeMesh`` still has three users (the remaining trees), so it is preserved.
* Only the two objects are gone.

Now select one of the remaining three trees and press :kbd:`Ctrl` click **Deep Delete**:

* The operator finds all three remaining tree objects (the one you clicked plus the two others sharing ``TreeMesh``).
* All three trees are deleted.
* ``TreeMesh`` now has zero users and becomes orphaned, so it is automatically removed.

The ``Rock`` mesh and its three instances remain untouched throughout.

Hidden and Excluded Objects
----------------------------

**Deep Delete** can process hidden objects and objects in excluded collections without needing to unhide or reveal them first. The deletion happens directly at the datablock level, so visibility does not matter. This is useful when cleaning up complex scene hierarchies where some objects are intentionally hidden.
