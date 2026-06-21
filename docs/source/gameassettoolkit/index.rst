:orphan:

==========================
About Game Asset Toolkit
==========================

**Game Asset Toolkit** is a Blender addon that streamlines the game asset export pipeline. It provides tools for LOD management, collider generation, mesh cleanup, and a validated batch FBX exporter — all from a single panel in the 3D Viewport.

The panel is found in the **Precise** tab of the N-panel (:kbd:`N` in the 3D Viewport).

Naming Convention
-----------------

GAT uses a strict naming convention. Most tools both produce and expect these suffixes:

* **LOD objects:** ``AssetName_LOD0``, ``AssetName_LOD1``, ``AssetName_LOD2``, ``AssetName_LOD3``
* **Collider objects:** ``AssetName_Collider``

The Smart Exporter enforces this convention during validation. Other tools (Create Asset Collection, Copy as Next LOD, Copy as Collider) produce names that follow it automatically.

Pages
"""""

* :doc:`smartexporter`
* :doc:`assetpreview`
* :doc:`assettools`
* :doc:`cleanuptool`
* :doc:`preferences`
