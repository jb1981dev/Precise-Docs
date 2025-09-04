Apply Modifiers
===============

The **Apply Modifiers** operator is a powerful tool designed to permanently "bake" an object's modifier stack into its geometry. Its strength lies in its versatility, handling most object types that support modifiers—such as **Meshes, Curves, and Text**—while intelligently managing linked duplicates to ensure modifiers are applied consistently across all instances.

The primary function is to provide a one-click solution to apply a modifier setup and then clean up the stack across an entire instance group.

.. important::
   This is a **destructive** operation. For non-mesh objects like **Curves** or **Text**, this operator will permanently convert them into **Mesh** objects to apply the modifiers.

The Two-Step Process
--------------------

To understand this tool, it's best to think of it as an automated two-step process that happens in the background:

#. **Apply & Convert:** First, the operator runs a "Convert to Mesh" operation on your selected source object(s). This is what "bakes" the visual result of the modifiers into the object's actual geometry. Because this action modifies the shared object data, **all linked duplicates are affected simultaneously.**

#. **Sync & Clean Up:** Immediately after, the operator automatically runs a **Modifier Sync**. Since the modifiers are now part of the base geometry, the original modifier stack is redundant. This second step intelligently removes the now-unnecessary modifiers from all the linked duplicates, leaving you with a clean, applied result across all instances.

How to Use with Selections
--------------------------

This operator uses a "leader-based" system to determine which modifier stack to apply.

* **Unique Objects:** If you select one or more objects that are all unique (not linked duplicates of each other), the operator will simply process each one, applying its own modifiers.

* **Groups of Linked Duplicates:** If your selection includes a group of linked duplicates, you **must** specify which object's modifier stack to use as the source. You do this by making it the **active object** (selected last, with a brighter outline). The operator will then apply the active object's modifiers to every instance sharing that data.

Objects in your selection that do not have any modifiers will be skipped.
