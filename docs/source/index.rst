=================
Document Title
=================

Section Title (Level 1)
=======================

Subsection Title (Level 2)
--------------------------

Sub-subsection Title (Level 3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Paragraph Title (Level 4)
"""""""""""""""""""""""""

Italics: *text*

Bold: **text**

Monospace/Code: ``text``

* An item
* Another item
   * A nested item

Links

**Instance Wrangler** is a Blender addon to assist in managing instances.
Developed by `Jeroen Backx <https://jeroenbackx.com/>`_

.. _my-target-label:

My Target Section
=================

:ref:`My Target Section <my-target-label>`.

``To link to another document: ``:doc:`path/to/other/document```


Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. code-block:: python
   :linenos:
   :emphasize-lines: 3,4

   def my_function():
       """A sample function."""
       print("Hello, world!")
       return True

.. note::
   This is something you should pay attention to.

.. warning::
   Be careful with this command as it can cause data loss.

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   usage
   api
