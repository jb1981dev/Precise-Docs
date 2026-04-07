# Instance Wrangler Documentation Status

> Last audited: April 7, 2026  
> Docs version: 1.2.00 (stub)  
> Addon version: **1.1.33**

This file tracks which pages are up to date and what needs to be written or updated.

---

## Page Status Overview

| Page | File | Status | Notes |
|---|---|---|---|
| Version History | `iwversions.rst` | ✅ Up to date | v1.2.00 entry written |
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
| Find Unlinked Duplicates | `findunlinked.rst` | ⚠️ Needs update | Page created. Needs GIF and YouTube video when available. |
| Accessing the Addon | `usingtheaddon.rst` | ⚠️ Needs update | Page created as "Using the Addon". Needs screenshots when available. |

---

## Detailed Change Notes Per Page

### `iwversions.rst` — Write v1.2.00 release entry

A v1.2.00 placeholder stub now exists with `Placeholder text.` as the body. The section heading and anchor `.. _version_1_2_00:` are already in place. Replace the placeholder with the real content covering all major changes since 1.1.30.

Changes are sourced from git tags `1.1.31`, `1.1.32`, and commits on the `header-toolbar` branch (HEAD, no tag yet). Group by feature area, not by internal version number.

---

#### Multi Transform

- **Include toggles (Pos / Rot / Scale):** Three toggle buttons now appear at the top of the Position, Rotation, and Scale columns. They control which transform types are applied by **Set All** and by Advanced Copy's **Apply Multi Transform**. The individual Set P / Set R / Set S buttons are unaffected — they always apply their own type. *(commit 95647ea)*
- **Modifier keys on all Set buttons** (Set P, Set R, Set S, Set All): *(commit d6edf7b / 95647ea)*
  - `LMB` → Set (apply values to selection)
  - `CTRL` → Get (read active object's transform into the fields; respects axis toggles)
  - `Shift` → Round (snap fields to nearest clean step: 0.5 m / 1° / 0.1; respects axis toggles)
  - `Alt` → Reset (reset fields to defaults: 0 / 0° / 1; respects axis toggles)
  - For **Set All**, Ctrl/Shift/Alt also respect the Pos/Rot/Scale include toggles.
- **Bypass Children option:** When a parent and its children are all selected, enabling Bypass Children skips the children — only the parent receives the transform. *(commit 79e2871)*
- **Redo / F9 panel support:** Multi Transform now records its axis toggles, include toggles, and values in the redo panel so they can be adjusted and re-run with F9. *(commit d6edf7b)*
- **Active Leads validation fix:** Fixed a case where Active Leads mode could silently fail; the operator now validates the active object before running. *(commit a43256e)*

---

#### Advanced Copy

- **Target Merge Mode:** A new alternative workflow for Merged Copy. Click **Set Target** to nominate an existing object; running Merged Copy then replaces that object's data-block in-place, updating all its linked instances automatically. A **T: {name}** button re-selects the target; **X** clears it. Redo/F9 is not available in this mode. *(commit b7a89f0)*
- **Apply Multi Transform — include toggle awareness:** When Apply Multi Transform is on, only the transform types enabled by the Pos/Rot/Scale include toggles in the Multi Transform panel are applied to new copies. *(commit 95647ea)*
- **Clear Parents before transform apply:** The clear-parents step now reliably runs before Apply Multi Transform, ensuring transforms are applied on a flattened hierarchy for all three copy types (Linked, Unlinked, Merged). *(commits 9c49508, ac21638)*
- **Redo / F9 panel support:** All Advanced Copy settings (Skip Active, Include Children, Clear Parents, etc.) are now available in the redo panel. *(commit d482e2c)*

---

#### Apply Transforms

- **CTRL modifier — Selective Reset:** Hold Ctrl when clicking Apply Transforms to also reset the toggled transform channels on non-leader instances after applying. If 2+ instances from the same group were selected, only those selected instances are reset; if just 1 was selected, all instances in the group are reset. *(commits e50b510, 905ebbc)*
- **Cross-scene instance handling:** The operator now searches all scenes for instances of the selected object's data-block, not just the active scene, and temporarily unhides objects in excluded or hidden collections to perform the apply. *(commit 0728691)*
- **Text and 2D Curve graceful handling:** Text objects and 2D Curve objects only support scale apply. If you select P or R with one of these in your selection, those channels are silently skipped and a warning is shown in the info bar; the scale apply still proceeds. *(commit d7cf965)*

---

#### Find Unlinked Duplicates (new)

- New operator in the Instance Management section. Searches the scene for objects that share the same geometry (via SHA256 fingerprint) as the selected object(s) but are not currently linked. Adds them to the selection so you can follow up with **Link Selected**. *(commit f8b5dd2)*
- Three comparison toggles control what is included in the fingerprint: **UV** (default on), **Mat** (default off), **Attr** (default off). Available in the panel mini-toggles and in the redo/F9 panel.

---

#### New Access Points

- **Popup Menu (Ctrl+Y):** A new floating popup menu containing all toolsets, accessible with Ctrl+Y in Object Mode or Edit Mode. *(commit 26a116b)*
- **Right-Click Context Menus:** All major operators now appear in the right-click menu in Object Mode and Edit Mode, including a Multi Transform entry. *(commits 1007ed1, 2acfcc9)*
- **Header Toolbar:** The IW logo button is permanently visible in the 3D Viewport tool header. Click it to expand/collapse inline icon buttons for each toolkit; each button opens a popover panel anchored below the header bar. *(commits e13391f, 2041364, e08f9f8, 3778946)*

---

#### Preferences

- **Toolset visibility and ordering:** Each toolset now has four per-panel controls in preferences: show/hide in N-panel, show/hide in popup menu, display order (up/down arrows), and default expanded/collapsed state for new scenes. *(commit 4766382, 37eb666)*
- **Custom icons throughout:** Custom icons are used for each toolset in the preferences table, on the N-panel section headers, in the popup menu header, in the right-click menus, and in the header toolbar. *(commits 2f22ecb, d10b7e9, 38c1a13, 66ba8ef)*

---

#### Internal / Stability

- UI state is now stored using Blender-native properties on WindowManager and Scene instead of a JSON file, improving reliability on file load. *(commit 1ef1b1a)*
- Panel state persists across file saves and loads; new scenes start from preference defaults. *(commit 1826797)*

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

- ~~`index.rst` should add a link to the new `accessing.rst` page as the **first entry** (before Multi Transform).~~ ✅ Done (as `usingtheaddon.rst`, listed after Version History).
- ~~`index.rst` should add a link to the new `findunlinked.rst` page after `groupunlink`.~~ ✅ Done.

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
