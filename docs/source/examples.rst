:orphan:

.. _formatting-examples:

===========================
Formatting Example Document
===========================

Section Title (Level 1)
=======================

Subsection Title (Level 2)
--------------------------

Sub-subsection Title (Level 3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Paragraph Title (Level 4)
"""""""""""""""""""""""""

Formatting
==========

Italics: *text*

Bold: **text**

Monospace/Code: ``text``

* An item
* Another item
   * A nested item

.. This is a comment line and will be invisible.

.. code-block:: console

   .. This is a comment line and will be invisible.

   ..
      The following list is temporarily commented out for review.
      It will not appear in the final output.

      * Item 1
      * Item 2
      * Item 3

Links
======

**Instance Wrangler** is a Blender addon to assist in managing instances.
Developed by `Jeroen Backx <https://jeroenbackx.com/>`_

`More formatting <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

.. _my-target-label:

My Target Section
------------------

:ref:`My Target Section <my-target-label>`.

``To link to another document: ``:doc:`path/to/other/document```

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.
Finally there is also the :doc:`api` page. 

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

Tables
------

Here is a simple table

========  ========
Header 1  Header 2
========  ========
Cell 1    Cell 2
Cell 3    Cell 4
========  ========

We can also create a list table

.. list-table::
   :header-rows: 1

   * - Header 1
     - Header 2
   * - Cell 1
     - Cell 2
   * - Cell 3
     - Cell 4

This is a slightly more complex table

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
