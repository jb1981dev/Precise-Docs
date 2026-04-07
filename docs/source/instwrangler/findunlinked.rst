.. _findunlinked:

========================
Find Unlinked Duplicates
========================

The **Find Unlinked Duplicates** tool searches your scene for objects that share the same geometry as the selected object(s) but are not currently linked to them. These are objects that *should* be instances but aren't — for example, after importing assets from multiple sources or after using :kbd:`Shift+D` instead of :kbd:`Alt+D`.

..
   VIDEO PLACEHOLDER
   .. raw:: html

      <iframe width="700" height="395" src="https://www.youtube.com/embed/PLACEHOLDER" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

How It Works
------------

The operator compares geometry using a **SHA256 fingerprint** — a hash derived from the object's mesh data. When you run the operator, it generates a fingerprint for each selected object and then scans all other objects in the scene for matching fingerprints. Any matches that are not already linked to the selected object are added to the selection.

The comparison can optionally include additional data layers to make the fingerprint more precise:

:UV Maps (UV):
    When enabled (default), UV map data is included in the fingerprint. This means two objects with identical geometry but different UV layouts are treated as distinct.

:Materials (Mat):
    When enabled, material slot assignments are included. Objects with the same geometry but different materials are treated as distinct.

:Attributes (Attr):
    When enabled, custom attribute layers are included. Useful for distinguishing objects that carry per-vertex or per-face data.

..
   IMAGE PLACEHOLDER
   .. figure:: images/findunlinked_overview.gif
      :align: center

   *Find Unlinked Duplicates selects all scene objects that share geometry with the selection.*

How to Use
----------

#. Select one or more objects whose geometry you want to search for.
#. Optionally adjust the **UV**, **Mat**, and **Attr** comparison toggles in the panel.
#. Click **Find Unlinked**.
#. All matching unlinked objects in the scene are added to your selection.
#. Use :doc:`linkselected` to link them all together.

The UV, Mat, and Attr toggles are also available in the redo/F9 panel after the operator runs, so you can adjust them and re-run immediately.

.. note::
   The operator only searches visible objects in the active scene. Objects in disabled or excluded collections are ignored.

Typical Workflow
----------------

This tool is most useful after importing assets from an external source, where objects that represent the same asset have been brought in as separate unlinked meshes. Run **Find Unlinked Duplicates** on one of them, then run **Link Selected** to convert all the matches into proper linked instances.
