# Instance Wrangler Documentation Status

> Last audited: April 7, 2026  
> Docs version: 1.2.00 (stub)  
> Addon version: **1.1.33**

This file tracks which pages are up to date and what needs to be written or updated.

---

## Page Status Overview

| Page | File | Status | Notes |
|---|---|---|---|
| Version History | `iwversions.rst` | ⚠️ Needs update | v1.2.00 stub exists with placeholder text — content needs to be written. |
| Multi Transform | `multitransform.rst` | ✅ Up to date | Include toggles and modifier keys confirmed present |
| Advanced Copy | `advancedcopy.rst` | ✅ Up to date | Target Merge Mode, Apply MT note, wildcard confirmed present |
| Apply Transforms | `applytransforms.rst` | ✅ Up to date | CTRL modifier / Selective Reset section added |
| Modifier Sync | `modifiersync.rst` | ✅ Up to date | |
| Apply Modifiers | `applymodifiers.rst` | ✅ Up to date | |
| Select Linked | `selectlinked.rst` | ✅ Up to date | |
| Link Selected | `linkselected.rst` | ✅ Up to date | |
| Unlink | `unlink.rst` | ✅ Up to date | |
| Group Unlink | `groupunlink.rst` | ✅ Up to date | |
| Cycle Data | `cycledata.rst` | ✅ Up to date | |
| Copy Name | `copyname.rst` | ✅ Up to date | |
| Blender Menus | `blendermenus.rst` | ✅ Up to date | |
| Find Unlinked Duplicates | ❌ **Missing page** | ❌ Not written | Entirely new feature, no page exists yet |
| Accessing the Addon | ❌ **Missing page** | ❌ Not written | New intro page: N-panel, header toolbar, popup (Ctrl+Y), right-click menu, redo/F9 |

---

## Detailed Change Notes Per Page

### `iwversions.rst` — Write v1.2.00 release entry

A v1.2.00 placeholder stub now exists with `Placeholder text.` as the body. The section heading and anchor `.. _version_1_2_00:` are already in place. Replace the placeholder with the real content covering all major changes since 1.1.30:

- **Multi Transform — modifier keys on Set buttons** (Set P / Set R / Set S / Set All):
  - LMB: Apply transform to selection
  - CTRL: Get value from active object (respects axis toggles)
  - Shift: Round values to nearest step (Pos: 0.5 m, Rot: 1°, Scale: 0.1)
  - Alt: Reset values to default (Pos: 0, Rot: 0°, Scale: 1)
  - For **Set All**, CTRL/Shift/Alt also respect the Pos/Rot/Scale include toggles
- **Multi Transform — include toggles** (Pos/Rot/Scale header row): filter which transforms Set All and Advanced Copy's Apply Multi Transform apply.
- **Advanced Copy — Target Merge Mode**: merge selection into an existing object's data-block in-place without creating a new object.
- **Find Unlinked Duplicates**: new operator with UV/Material/Attribute comparison options using SHA256 fingerprinting.
- **Apply Transforms — CTRL modifier**: selective reset on non-leader instances in a group.
- **Toolset visibility and ordering**: show/hide and reorder toolsets per-panel (N-panel / popup) in preferences.
- **Advanced Copy collection placement**: `Automatic` and `Scene Collection` explicit options.
- **Name wildcard**: `*` placeholder in Advanced Copy name field (e.g. `LOD0_*` inserts original object name).
- **Header toolbar**: IW logo button always visible in the tool header; click to expand toolkit buttons inline.

---

### New page needed: `findunlinked.rst`

**Feature:** Find Unlinked Duplicates  
**Operator:** `instance_wrangler.find_unlinked_duplicates`  
**UI location:** Instance Management section, last row. Button + 3 mini toggles.

**What it does:** Searches the scene for objects that appear to be duplicates of the selected object(s) based on geometry fingerprinting (SHA256), but are NOT currently linked (i.e. they share similar geometry but have different data-blocks).

**Comparison options (redo/F9 + mini toggles in panel):**
- `find_unlinked_compare_uvs` — Include UV maps in fingerprint comparison (default: ON)
- `find_unlinked_compare_materials` — Include material assignments in comparison (default: OFF)
- `find_unlinked_compare_attributes` — Include attributes in comparison (default: OFF)

**Result:** Selects all objects that match the fingerprint. The user can then use **Link Selected** to actually link them.

**Use case:** After importing assets from different sources or after manually duplicating instead of instancing, this tool finds all the objects that *should* be instances but aren't.

Add this page and add it to `index.rst` under Instance Management.

---

### New page needed: `accessing.rst`

**Purpose:** Help new users understand the multiple ways to access Instance Wrangler's tools. Add as the **first page** in `index.rst` (before Multi Transform).

**Sections to cover:**

1. **N-Panel (Sidebar)** — Open with `N` key in the 3D viewport, navigate to the *Precise* tab. The main persistent panel; always available. Toolsets can be shown/hidden and reordered in addon preferences.

2. **Header Toolbar** — The IW logo button is permanently present in the 3D viewport's tool header (the same bar as the transform orientation dropdown, pivot point, and snap controls). Click the logo to expand or collapse the toolkit buttons inline. Each toolkit button opens a floating popup panel with the same layout as that section of the N-panel.

3. **Popup Menu (Ctrl+Y)** — Floating popup containing all toolsets in one place. Accessible from anywhere in the viewport without opening the sidebar. Toolset visibility and ordering mirrors N-panel preferences.

4. **Right-Click Context Menu** — All major operators appear in the right-click menu in both **Object Mode** and **Edit Mode**. Useful for quick one-off actions without opening any panel.

5. **Redo Panel (F9 / Last Operator)** — After running any operator, press `F9` or expand the Last Operator panel in the viewport's bottom-left corner to adjust its settings. Multi Transform records axis toggles and values; Advanced Copy records all placement and naming settings.

---

## Index / Structure Notes

- `index.rst` should add a link to the new `accessing.rst` page as the **first entry** (before Multi Transform).
- `index.rst` should add a link to the new `findunlinked.rst` page after `groupunlink`.

---

## General Writing Notes

- Keep the same RST formatting style as existing pages (section headings, `.. figure::`, `.. note::`, `:kbd:` roles).
- Use `.. important::` for destructive operation warnings (see `applymodifiers.rst` for example).
- Every new subsection should ideally have a GIF. Flag image needs in a separate list below.

---

## Images Needed

| Feature | Suggested filename | Priority |
|---|---|---|
| Multi Transform include toggles (Pos/Rot/Scale header row) | `multitransform_includetoggles.gif` | High |
| Multi Transform modifier keys on Set buttons (CTRL Get / Shift Round / Alt Reset) | `multitransform_modifierkeys.gif` | High |
| Advanced Copy Target Merge Mode UI flow | `advancedcopy_targetmerge.gif` | High |
| Find Unlinked Duplicates in action | `findunlinked_overview.gif` | High |
| Apply Transforms CTRL modifier (selective reset) | `apply_transform_ctrl.gif` | Medium |
| Header toolbar expand/collapse via logo button | `header_toolbar_toggle.gif` | Medium |
| Accessing the addon: N-panel / popup / right-click / F9 overview | `accessing_overview.gif` | Low |
