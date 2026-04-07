.. _usingtheaddon:

================
Using the Addon
================

This page covers how to install Instance Wrangler and the different ways you can access its tools once it is installed.

Installation
------------

#. Open Blender.
#. Navigate to **Edit > Preferences**.
#. Navigate to the **Add-ons** tab.
#. Click the downward-pointing arrow in the top right and choose **Install from Disk**.
#. Select the Instance Wrangler ``.zip`` file you downloaded from the store platform.
#. Instance Wrangler will now appear in the add-ons list — make sure its checkbox is enabled.

Accessing the Tools
-------------------

Instance Wrangler's tools are available from four different locations. All of them share the same operators, so you can use whichever fits your workflow.

N-Panel (Sidebar)
^^^^^^^^^^^^^^^^^

Open the sidebar with :kbd:`N` in the 3D Viewport and navigate to the **Precise** tab. This is the main persistent panel and is always available. Toolsets can be shown, hidden, and reordered in the addon preferences.

..
   IMAGE PLACEHOLDER
   .. figure:: images/accessing_npanel.png
      :align: center

   *The Instance Wrangler N-panel in the Precise tab.*

Header Toolbar
^^^^^^^^^^^^^^

The **IW logo button** is permanently present in the 3D Viewport's tool header — the same bar as the transform orientation dropdown, pivot point, and snap controls. Click the logo to expand the toolkit buttons inline. Each button opens a floating panel with the same layout as the corresponding N-panel section.

..
   IMAGE PLACEHOLDER
   .. figure:: images/accessing_header.png
      :align: center

   *The header toolbar with toolkit buttons expanded.*

Popup Menu
^^^^^^^^^^

Press :kbd:`Ctrl+Y` in Object Mode or Edit Mode to open a floating popup containing all toolsets in one place. Toolset visibility and ordering mirrors your N-panel preferences.

Right-Click Context Menu
^^^^^^^^^^^^^^^^^^^^^^^^

All major operators appear in the right-click menu in both **Object Mode** and **Edit Mode**. Useful for quick one-off actions without opening any panel.

Redo Panel (F9)
^^^^^^^^^^^^^^^

After running any operator, press :kbd:`F9` or expand the **Last Operator** panel in the viewport's bottom-left corner to adjust its settings. Most operators record their options here — for example, Multi Transform records axis toggles and values, and Advanced Copy records all placement and naming settings.
