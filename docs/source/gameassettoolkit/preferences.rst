===========
Preferences
===========

The Game Asset Toolkit preferences are accessible via **Edit → Preferences → Add-ons**
(or **Extensions** in Blender 4.2+). Search for "Game Asset Toolkit" and expand the entry.

LOD Hotkeys Configuration
-------------------------

Toggle individual hotkeys on or off. When a hotkey is disabled its keyboard shortcut
becomes available to other Blender operators.

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - :kbd:`Alt` + :kbd:`~`
     - Show all LOD objects
   * - :kbd:`Alt` + :kbd:`1`
     - Show only LOD0 objects
   * - :kbd:`Alt` + :kbd:`2`
     - Show only LOD1 objects
   * - :kbd:`Alt` + :kbd:`3`
     - Show only LOD2 objects
   * - :kbd:`Alt` + :kbd:`4`
     - Show only LOD3 objects
   * - :kbd:`Alt` + :kbd:`5`
     - Hide all LOD objects
   * - :kbd:`Alt+Shift` + :kbd:`1`
     - Toggle all collider objects visible / hidden
   * - :kbd:`Alt+Shift` + :kbd:`2`
     - Toggle all collider objects between Solid and Wire display mode

**Disable Conflicting Blender Hotkeys**
   When enabled, automatically disables Blender's default hotkeys (Object Mode menu
   shortcuts) that conflict with the LOD hotkeys above.

Toolset Management Table
------------------------

Control which toolsets appear in the three UI surfaces, and in what order:

.. list-table::
   :widths: 20 10 12 12 12
   :header-rows: 1

   * - Toolset
     - Order
     - N-Panel
     - Popup
     - Header
   * - Smart Exporter
     - ⬆⬇
     - ✓/✗
     - ✓/✗
     - ✓/✗
   * - Asset Preview
     - ⬆⬇
     - ✓/✗
     - ✓/✗
     - ✓/✗
   * - Asset Tools
     - ⬆⬇
     - ✓/✗
     - ✓/✗
     - ✓/✗
   * - Cleanup
     - ⬆⬇
     - ✓/✗
     - ✓/✗
     - ✓/✗

- **Order** — Click the up/down arrows to swap the position of two adjacent toolsets.
  The number updates automatically. Toolsets in the N-panel, popup, and header toolbar
  follow the order defined here. Rows stay in registration order; only the number changes.
- **N-Panel** — Show or hide the toolset in the sidebar N-panel (:kbd:`N` in the 3D Viewport).
- **Popup** — Show or hide the toolset in the Ctrl+T quick-access popup menu.
- **Header** — Show or hide the toolset in the 3D Viewport header toolbar. When all
  header toolsets are disabled, the GAT header toggle button is hidden automatically.

Header Toolbar
--------------

The header toolbar is accessed via the GAT icon in the top-right of the 3D Viewport
header bar. Click the icon to expand toolset popovers. Each popover auto-expands its
sub-sections for quick access without clicking through collapse toggles.

Visibility and order of header popovers are controlled by the Toolset Management Table
above.

How to Find the Addon
---------------------

.. list-table::
   :widths: 15 85
   :header-rows: 0

   * - N-Panel
     - View3D Sidebar → Precise tab
   * - Popup Menu
     - Press :kbd:`Ctrl+T` in Object Mode
   * - Header Bar
     - Click the GAT icon (top-right toolbar)