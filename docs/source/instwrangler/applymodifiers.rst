.. _applymodifiers:

===============
Apply Modifiers
===============

The **Apply Modifiers** operator is a powerful tool designed to permanently "bake" an object's modifier stack into its geometry. Its strength lies in its versatility, handling most object types that support modifiers—such as **Meshes, Curves, and Text**—while intelligently managing linked duplicates to ensure modifiers are applied consistently across all instances.

The primary function is to provide a one-click solution to apply a modifier setup and then clean up the stack across an entire instance group.

.. important::
   This is a **destructive** operation. For non-mesh objects like **Curves** or **Text**, this operator will permanently convert them into **Mesh** objects to apply the modifiers.

The Two-Step Process
--------------------

To understand this tool, it's best to think of it as an automated two-step process that happens in the background:

#. **Apply & Convert:** First, the operator runs a "Convert to Mesh" operation on the leader of each selected group. This bakes the visual result of the modifiers into the shared object data, affecting **all linked duplicates** of that group simultaneously.

#. **Sync & Clean Up:** Immediately after, the operator automatically runs a **Modifier Sync**. Since the modifiers are now part of the base geometry, this step intelligently removes the now-redundant modifier stacks from all linked duplicates, leaving you with a clean result.

How to Use with Selections
--------------------------

This operator performs a **global** action for every instance group you select. It first finds a "leader" (the source object) for each group, then applies that leader's modifiers to all of its instances throughout the scene.

The rules for determining the leader are the same as for **Modifier Sync**:

* **If your entire selection belongs to one group:** The **active object** must be part of the selection and is always considered the leader.

* **If you select objects from multiple groups:** The operator can process all of them at once. To avoid ambiguity, a leader must be clear for each group:
    * If you select only **one object** from a group, it automatically becomes that group's leader.
    * If you select **multiple objects** from a group, the **active object** must be one of them to be designated as that group's leader.

Objects whose leader does not have any modifiers will be skipped.
