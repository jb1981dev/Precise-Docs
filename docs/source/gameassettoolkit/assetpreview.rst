====================
Asset Preview
====================

The **Asset Preview** toolset combines LOD visibility controls, UV channel access, and
collider display management into a single panel. Use it to quickly switch between detail
levels, access UV channels, and manage collider visibility across the entire scene.

LOD Visibility
--------------

One-click buttons control which LOD level is visible scene-wide. Any object with ``LOD#``
anywhere in its name is affected — regardless of object type or separator (``_``, ``.``,
``-``, or none).

**L0 / L1 / L2 / L3**
   Show objects at the selected LOD level, hide all other LOD objects.

**ALL**
   Show all LOD objects in the scene.

**NONE**
   Hide all LOD objects in the scene.

Modifier Keys
^^^^^^^^^^^^^

Hold a modifier key while clicking any LOD button to perform a selection operation instead
of a show/hide operation.

.. list-table::
   :widths: 20 80
   :header-rows: 0

   * - :kbd:`Ctrl`
     - Replace the current selection with all matching LOD objects. Hidden objects are
       unhidden automatically.
   * - :kbd:`Shift`
     - Add matching LOD objects to the current selection. Hidden objects are unhidden
       automatically.
   * - :kbd:`Alt`
     - Remove matching LOD objects from the current selection.

Child objects are always shown, hidden, selected, or deselected together with their LOD parent.

UV Channels
-----------

Quick-access buttons for the first three UV channels on all selected mesh objects.

**UV0 / UV1 / UV2**

.. list-table::
   :widths: 20 80
   :header-rows: 0

   * - :kbd:`LMB`
     - Activate the UV channel (sets it as the active UV layer).
   * - :kbd:`Ctrl`
     - Set the UV channel as active for rendering.
   * - :kbd:`Shift`
     - Create the UV channel if it does not yet exist.
   * - :kbd:`Alt`
     - Remove the UV channel.

Collider Visibility
-------------------

Visibility and display controls for objects with a ``_Collider`` suffix.

**Show / Hide**
   Shows or hides all collider objects that are in visible collections. Only objects present
   in the active view layer are affected.

   * :kbd:`Ctrl` + Show — Select all visible collider objects (replaces current selection).
   * :kbd:`Ctrl` + Hide — Deselect all visible collider objects.

**Solid / Wire**
   Sets the viewport display mode for all collider objects in the scene. Wire mode is useful
   for inspecting collision geometry without it obscuring the visual mesh.

   * :kbd:`LMB` — Apply to all collider objects in the scene.
   * :kbd:`Ctrl` — Apply to all currently selected objects instead.

Collider Hotkeys
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - :kbd:`Alt+Shift+1`
     - Toggle all collider objects visible / hidden.
   * - :kbd:`Alt+Shift+2`
     - Toggle all collider objects between Solid and Wire display mode.

These hotkeys can be enabled or disabled in the **LOD Hotkeys Configuration** section of
the addon preferences.