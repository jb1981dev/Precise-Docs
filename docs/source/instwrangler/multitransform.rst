Multi Transform
===============

The **Multi Transform** panel provides a powerful and precise way to manipulate the position, rotation, and scale of multiple objects simultaneously. It's designed for workflows that demand accurate, numeric input, offering a level of control that goes beyond Blender's standard interactive tools.

The panel is organized into a grid layout, with each row corresponding to a transform **axis** (X, Y, and Z). This allows you to view and edit the Position, Rotation, and Scale values for a specific axis all in one place. This structure is controlled by a powerful set of modes, allowing for both standard independent editing and an **Active Leads Mode** which uses the active object as a group pivot.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/TcjOvJjajvQ?si=HoJK9LkZfPZ27_8A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

UI Controls Explained
-----------------------

* **Header Row:** The top row contains shortcuts to reset the transform values. **Pos** resets Position to ``(0,0,0)``, **Rot** resets Rotation to ``(0,0,0)``, and **Scale** resets Scale to ``(1,1,1)``.
* **Axis Rows (X, Y, Z):** Each of these three rows contains:
    * An **axis toggle** on the left to include or exclude that axis from the operation.
    * Three numeric input fields for that axis's **Position**, **Rotation**, and **Scale**.
* **Set Buttons Row:** The bottom row contains the buttons to apply the transforms:
    * **Set All:** Applies the values for Position, Rotation, and Scale all at once.
    * **Set (per-transform):** Applies only the values for either Position, Rotation, or Scale.

.. figure:: images/multitransform_setall.gif
   :align: center
   :alt: Setting the scale in absolute and relative mode and using the axis rows.

Using "Set All" to set position, rotation and scale at the same time.

* **Mode Toggles:**
    * **Relative Toggle:** Switches between **Absolute** and **Relative** modes. Its behavior changes depending on whether **Active Leads** is enabled.
    * **Active Leads Toggle:** Switches the tool to a powerful mode where the **active object** acts as a pivot or "fake parent" for the rest of the selection.

Relative Toggle
------------------
The **Relative** toggle lets you switch between relative and absolute transform mode.

* **Absolute Mode** (``Relative`` disabled): This mode sets the transform values to the **exact numbers** you enter. It's perfect for aligning objects to a specific coordinate.
    * Example: To align all selected objects to a height of 5 meters, you would disable ``Relative``, enter ``5.0`` in the Z position field, and click **Set**.

* **Relative Mode** (``Relative`` enabled): This mode **adds** (or multiplies for scale) the entered values to each object's current transform. It's ideal for nudging a selection of objects while preserving their existing arrangement.
    * Example: To move all selected objects 2 units to the right, you would enable ``Relative``, enter ``2.0`` in the X position field, and click **Set**.

.. figure:: images/multitransform_position.gif
   :align: center

Setting the position in absolute and relative mode and using the axis rows.

.. figure:: images/multitransform_rotation.gif
   :align: center

Setting the rotation in absolute and relative mode and using the axis rows.

.. figure:: images/multitransform_scale.gif
   :align: center

Setting the scale in absolute and relative mode and using the axis rows.

Active Leads Mode
----------------------

Enabling **Active Leads** makes the **active object** the pivot point for the entire selection, like a lead dancer guiding their partners.
 
* **Position:** The entire group moves rigidly to place the active object at the target coordinates.
* **Rotation:** Followers **orbit** around the active object as it rotates to its new orientation.
* **Scale:** The active object is scaled by the specified factor, and all followers scale with it, moving further from or closer to the leader proportionally.

**Relative Toggle:** offers a lot of flexibility in Active Leads mode.

* **Relative Mode Off (Absolute Mode):** You are setting an **absolute target** for the leader, and the followers will arrange themselves around it.
* **Relative Mode On:** In this mode, the UI values represent an **incremental change** that is applied to the active object, and the followers move with it in a parented fashion with each click.	

.. figure:: images/multitransform_activeleadspos.gif
   :align: center

Use Active Leads to move objects as a group, using the active object as the group pivot.

.. figure:: images/multitransform_activeleadsrot.gif
   :align: center

Use Active Leads to rotate objects as a group, using the active object as the group pivot.

.. figure:: images/multitransform_activeleadsscale.gif
   :align: center

Use Active Leads to scale objects as a group, using the active object as the group pivot.
