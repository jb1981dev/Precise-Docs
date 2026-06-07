.. _deeprename:

===========
Deep Rename
===========

The **Deep Rename** tool renames selected objects **and** their underlying
datablocks (mesh, curve, etc.) simultaneously using a flexible naming pattern.
This keeps object names and data names in sync during batch-renaming.

In Blender, object names and datablock names are independent — renaming an
object via the outliner leaves its mesh/curve data with the old name. Deep Rename
solves this by updating both at once.

.. dropdown:: Animation: Deep Rename Basics and UI
   :open:

   .. figure:: images/deeprename_basics.gif
      :align: left

   *Basic operations using Deep Rename (IW v1.2)*

   .. figure:: images/deeprename_ui.gif
      :align: left

   *Deep Rename User Interface (IW v1.2)*

How to Use
----------

#. Select one or more objects. The active object is always treated as #1.
#. Click **Deep Rename**.
#. A dialog opens with a text field pre-filled with the active object's name.
   A **live preview** shows the resulting object and datablock name as you type.
#. Build your pattern by typing directly or clicking the token buttons
   (Clear ×, \*, %, #). The **Clear** button resets the pattern to blank.
#. Choose the **Separator** character used between token elements
   (None, Underscore, Dash, Dot, or Tilde).
#. Choose the **Numbering** scope — across the full selection, or restarting
   within each shared datablock group.
#. Optionally enable **Extend to all datablock users** to also rename
   non-selected scene objects sharing the same datablocks.
#. Click **OK** or press :kbd:`Enter` to apply.

Naming Pattern Tokens
---------------------

The text field supports tokens that are replaced with actual names at runtime.
Click the **\***, **%**, or **#** buttons to insert them, or type them directly.
Token buttons use the current **Separator** setting to join elements.

.. dropdown:: Animation: Deep Rename Wildcards
   :open:

   .. figure:: images/deeprename_wildcards.gif
      :align: left

   *Deep Rename Wildcards (IW v1.2)*

``*`` (Asterisk)
    For **object names**: replaced with the object's original name.

    For **datablock names**: replaced with the datablock's own original name
    (not an arbitrary object's name). This ensures shared datablocks get
    predictable names regardless of which object is active.

    *Example:* ``*_Dead`` on object ``Tree`` → object ``Tree_Dead``,
    datablock ``Tree_Dead`` (or ``Shrub_Dead`` if the data was named
    ``Shrub``).

``%`` (Percent)
    Replaced with the **original datablock name**, both for object and
    datablock names. Useful for inserting the data name into object names.

    *Example:* ``%_##`` on two objects with datablocks ``Cube`` and ``Sphere``
    → ``Cube_01``, ``Sphere_01``.

.. warning::

   Using both ``*`` and ``%`` in the same pattern causes a warning:
   they are redundant for datablock names and only ``%`` is applied
   at the data level. Object names still use both as expected.

``#``, ``##``, ``###``, etc. (Hash signs)
    A 1-based index, zero-padded to the number of hash characters. The
    active object is always #1.

    * ``#`` → ``1``, ``2``, ``3``, ...
    * ``##`` → ``01``, ``02``, ``03``, ...
    * ``###`` → ``001``, ``002``, ``003``, ...

    *Example:* ``Asset_###`` → ``Asset_001``, ``Asset_002``, ``Asset_003``.

    .. dropdown:: Animation: Deep Rename Numbering using hash signs
   :open:

   .. figure:: images/deeprename_numbering.gif
      :align: left

   *Deep Rename numbering (IW v1.2)*

You can combine all three tokens in one pattern, or provide a static name
with no tokens at all.

.. note::

   The token buttons also act as **toggles**: clicking ``*`` or ``%``
   again removes the token from the pattern if it already exists.
   The ``#`` button stacks additional hash characters for deeper padding.

Numbering Scope
---------------

Two numbering modes control how the ``#`` token resolves:

``Selection``
    ``#`` counts across the full ordered selection. The active object is #1.

``Datablock Group``
    ``#`` restarts for each shared datablock group. Ideal for renaming linked
    instances like ``Cube_01``, ``Cube_02``, ``Sphere_01``, ``Sphere_02``
    within one multi-selection.

Separator Control
-----------------

The **Separator** dropdown controls which character is inserted between
tokens when using the \*, %, and # buttons, and is also used to render
separators in the pattern itself. Changing the separator updates the
text field in real time — switching to **None** strips separators
adjacent to wildcards, and switching to any real separator re-inserts
them at the correct positions.

The separator only affects button-inserted tokens — text you type
manually is untouched.

Choices: **None** (no separator), **Underscore** (``_``), **Dash** (``-``),
**Dot** (``.``), and **Tilde** (``~``). Default is Underscore.

Extend to All Datablock Users
-----------------------------

When enabled, the operation also includes scene objects that share datablocks
with the selected objects but are not themselves selected. This ensures all
users of a shared datablock get consistent names.

Examples
--------

**Example 1: Rename with Index**

Pattern: ``Prop_##``  — Numbering: Selection

Result on three objects:
    * ``Prop_01``
    * ``Prop_02``
    * ``Prop_03``

**Example 2: Preserve Original Name + Add Suffix**

Pattern: ``*_Collision``

If the objects are named ``Box``, ``Sphere``, and ``Cone``:

Result:
    * ``Box_Collision``
    * ``Sphere_Collision``
    * ``Cone_Collision``

**Example 3: Datablock Token + Group Numbering**

Pattern: ``%_##``  — Numbering: Datablock Group

If the selection contains two ``Cube`` instances and two ``Sphere`` instances:

Result:
    * ``Cube_01``, ``Cube_02``
    * ``Sphere_01``, ``Sphere_02``

**Example 4: Static Name (No Tokens)**

Pattern: ``MyProp``

All objects and datablocks are renamed to ``MyProp``. If name conflicts
occur, implicit numbers are added automatically (e.g., ``MyProp_1``,
``MyProp_2``).

Live Preview & Warnings
-----------------------

The dialog shows a live preview of the active object's new **Object** and
**Data** names, updating as you type or change settings.

If the pattern causes datablock name conflicts (for example, a static name
that collides with an existing datablock), a warning appears indicating
that implicit numbering will be added to resolve the conflict. The preview
reflects these resolved names so you can verify them before committing.