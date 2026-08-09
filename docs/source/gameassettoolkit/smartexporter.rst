===============
Smart Exporter
===============

The Smart Exporter exports selected objects (or collections) as individual FBX files. It validates each object before exporting and reports errors and warnings in a dedicated Validator Panel.

The exporter resides in the **Precise** tab → **Smart Exporter** section.

Export Path
-----------

Set the target directory in the **Export target path** field. Blender relative paths (``//``) are supported.

Click the arrow button next to the path field to pick from recently used paths.

Export
------

**Batch Export**
   Exports each selected object (or LOD group) as a separate FBX file. Objects are identified by their base name (the part before ``_LOD#``). All LOD levels of an asset are written into one file.

**Export by Collection**
   Exports each selected collection as a separate FBX file. All objects in the collection are included.

Validation
----------

**Validator Panel**
   Toggles a split area in the viewport that displays validation messages. Messages from the last export or validation run persist until auto-cleared or manually cleared.

**Validate**
   Runs the full validation pass on all collections without exporting. Useful for checking assets before a real export run.

Validation Checks
^^^^^^^^^^^^^^^^^

Each object is checked for:

* **Name pattern** — must end in ``_LOD#`` (e.g. ``_LOD0``) or ``_Collider``. Fails as an error by default.
* **Geometry** — mesh must not be empty.
* **UV Maps** — must have at least UV0 (textures) and UV1 (lightmap). UV1 must be fully within the 0–1 range and have no overlapping UV islands.

Objects with errors block export. Objects with only warnings are exported but flagged.

Options
-------

Options are accessible under the collapsible **Exporter Options** section.

**Preset**
   Select a Blender FBX export preset to control the underlying FBX settings (coordinate system, scale, etc.).

**Center Objects**
   Moves each object to the world origin before exporting and restores its position afterwards.

**Auto-Clear Validator Panel**
   Clears previous messages in the Validator Panel before each new export or validation run.

**Split by Materials**
   Splits objects by material during export. Each material becomes a separate FBX (transparent to the end result).

**Use Material Aliases**
   When enabled, material names are matched against a user‑curated alias list. If a material name matches a stored pattern, the matching alias is used as the export suffix (e.g. ``_Wood``). If no alias matches, a numbered fallback suffix is applied (e.g. ``_Part01``).

   Click **Use Material Aliases** to open the alias editor popup. Each entry has an **Alias** (the suffix to apply) and a **Search Pattern** (with ``%`` wildcards matching the material name). Use the ``%`` button to append a wildcard, the ``+``/``-`` buttons to add or remove entries, and the column headers to sort.

**Suffix** (Fallback)
   Prefix for numbered fallback suffixes when no material alias matches. Default is ``Part``.

**Number Padding** (Fallback)
   Controls the zero‑padded width of fallback numbers. For ``2`` the suffix is ``_Part01``; for ``3`` it is ``_Part001``.

**Save Settings / Load Settings**
   Persist the current exporter options to ``exporter/settings.json`` or reload from it.

Cheats
^^^^^^

These override validation rules and should only be used during development.

**Skip UV2 Overlap Check**
   Bypasses the lightmap UV overlap check. A warning is still added per object.

**Allow Deviant Names**
   Downgrades the name pattern error to a warning, allowing objects with non-standard names to export.

**Allow Incomplete LOD Ranges**
   Allows LOD sets that do not go up to LOD3 (e.g. only LOD0–LOD1). Gaps within a range (e.g. LOD0 and LOD2 without LOD1) are still blocked.
