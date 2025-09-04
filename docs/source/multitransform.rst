Multi Transform
===============

The **Multi Transform** panel provides a powerful and precise way to manipulate the position, rotation, and scale of multiple objects simultaneously. It's designed for workflows that demand accurate, numeric input, offering a level of control that goes beyond Blender's standard interactive tools.

The panel is organized into three rows for **Position**, **Rotation**, and **Scale**, each with its own numeric input fields and a **Set** button to apply the changes. These rows share a set of powerful controls that define how the transformations are applied.

UI Controls Explained
---------------------

* **Affect: X, Y, Z:** These checkboxes let you apply transforms to specific axes while ignoring others.
* **Rel (Relative):** Toggles between **Absolute** and **Relative** modes.
* **Pos, Rot, Scale Buttons:** These are shortcuts to reset the numeric input fields next to them to their default values:
    * **Pos:** Resets the Position fields to ``(0, 0, 0)``.
    * **Rot:** Resets the Rotation fields to ``(0, 0, 0)``.
    * **Scale:** Resets the Scale fields to ``(1, 1, 1)``.
* **Set Button:** Applies the values from the numeric fields to all selected objects, respecting the **Axis** and **Relative** settings.

Absolute vs. Relative Mode
--------------------------

This is the core of the tool's flexibility, controlled by the **Rel** toggle button.

* **Absolute Mode** (``Rel`` disabled): This mode sets the transform values to the **exact numbers** you enter. It's perfect for aligning objects to a specific coordinate or giving them a uniform rotation or scale.
    * *Example: To align all selected objects to a height of 5 meters, you would disable **Rel**, enter ``5.0`` in the Z position field, and click **Set**.*

* **Relative Mode** (``Rel`` enabled): This mode **adds** the entered values to each object's current transform. It's ideal for incrementally nudging or adjusting a selection of objects while preserving their existing arrangement.
    * *Example: To move all selected objects 2 units to the right, you would enable **Rel**, enter ``2.0`` in the X position field, and click **Set**.*

This combination of batch processing, numeric precision, and per-axis control makes the Multi Transform tool essential for technical and architectural work, offering a level of control not easily found in Blender's default toolset.
