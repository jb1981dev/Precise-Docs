=====================
Show / Hide LOD
=====================

The **Show/Hide LOD** section provides one-click buttons to control LOD level visibility across the entire scene. This is useful for quickly switching between detail levels without manually toggling objects in the outliner.

Any object with ``LOD#`` anywhere in its name is affected — regardless of object type or separator (``_``, ``.``, ``-``, or none).

Buttons
-------

**L0 / L1 / L2 / L3**
   Show objects at the selected LOD level, hide all other LOD objects.

**ALL**
   Show all LOD objects in the scene.

**NONE**
   Hide all LOD objects in the scene.

Modifier Keys
-------------

Hold a modifier key while clicking any LOD button to perform a selection operation instead of a show/hide operation.

.. list-table::
   :widths: 20 80
   :header-rows: 0

   * - :kbd:`Ctrl`
     - Replace the current selection with all matching LOD objects. Hidden objects are unhidden automatically.
   * - :kbd:`Shift`
     - Add matching LOD objects to the current selection. Hidden objects are unhidden automatically.
   * - :kbd:`Alt`
     - Remove matching LOD objects from the current selection.

Child objects are always shown, hidden, selected, or deselected together with their LOD parent.
