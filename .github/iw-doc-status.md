# Instance Wrangler Documentation Status

> Last audited: November 26, 2026
> Docs version: 1.2.0 (branch `iw-docs-1.2`)
> Addon version: **1.2.0** (branch `release-1.2.0-fixes`, commit `f646466`)

This file tracks which pages are up to date and what still needs to be made.
The text of every page matches the 1.2.0 addon; what remains is media.

---

## Page Status Overview

| Page | File | Status | Notes |
|---|---|---|---|
| Version History | `iwversions.rst` | ✅ Up to date | 1.2.0 entry includes the release fixes |
| Using the Addon | `usingtheaddon.rst` | ⚠️ Media missing | Preferences table screenshot (commented out) |
| Multi Transform | `multitransform.rst` | ⚠️ Media missing | Text complete, incl. Alt Reset on Set buttons. No GIF for include toggles or Set button modifier keys |
| Advanced Copy | `advancedcopy.rst` | ⚠️ Media missing | Text complete, incl. Skip Active guard. No GIF for Target Merge Mode |
| Apply Transforms | `applytransforms.rst` | ⚠️ Media missing | Ctrl / Selective Reset GIF (commented out) |
| Modifier Sync | `modifiersync.rst` | ✅ Up to date | |
| Apply Modifiers | `applymodifiers.rst` | ✅ Up to date | |
| Select Linked | `selectlinked.rst` | ✅ Up to date | |
| Link Selected | `linkselected.rst` | ✅ Up to date | Empty as active object now documented |
| Unlink | `unlink.rst` | ✅ Up to date | |
| Group Unlink | `groupunlink.rst` | ✅ Up to date | |
| Find Unlinked Duplicates | `findunlinked.rst` | ⚠️ Media missing | Overview GIF and YouTube video (both commented out) |
| Deactivate Selected | `deactivateselected.rst` | ✅ Up to date | |
| Select Children | `selectchildren.rst` | ✅ Up to date | |
| Cycle Data | `cycledata.rst` | ✅ Up to date | |
| Deep Rename | `deeprename.rst` | ✅ Up to date | |
| Deep Delete | `deepdelete.rst` | ✅ Up to date | |
| Copy Name | `copyname.rst` | ✅ Up to date | |
| Blender Menus | `blendermenus.rst` | ✅ Up to date | |

---

## Media Needed

Commented-out placeholders are already in the pages; uncomment them when the file is added.
Without a placeholder, add a new `.. figure::` (inside a `.. dropdown::` like the other animations).

| Feature | Page | Suggested filename | Placeholder in page | Priority |
|---|---|---|---|---|
| Find Unlinked Duplicates in action | `findunlinked.rst` | `findunlinked_overview.gif` | Yes | High |
| Find Unlinked Duplicates video | `findunlinked.rst` | YouTube embed | Yes | High |
| Advanced Copy Target Merge Mode flow | `advancedcopy.rst` | `advancedcopy_targetmerge.gif` | No | High |
| Multi Transform include toggles (Pos/Rot/Scale) | `multitransform.rst` | `multitransform_includetoggles.gif` | No | High |
| Set button modifier keys (Ctrl Get / Alt Reset) | `multitransform.rst` | `multitransform_modifierkeys.gif` | No | High |
| Apply Transforms Ctrl (Selective Reset) | `applytransforms.rst` | `apply_transform_ctrl.gif` | Yes | Medium |
| Preferences toolset table | `usingtheaddon.rst` | `preferences_toolsets.png` | Yes | Medium |
| Header toolbar expand/collapse | `usingtheaddon.rst` | `header_toolbar_toggle.gif` | No | Medium |

---

## Keeping This Up to Date

- Every addon change that alters behaviour described in the docs needs a docs change on the
  addon's docs branch, and a line in the version's entry in `iwversions.rst` (bug fixes under **Fixes**).
- Site-wide changes (CSS, `conf.py`, root `index.rst`) go on `main` first, then `main` is merged
  into `iw-docs-1.2` and `GAT_Release`.
- A new page goes in two places in `instwrangler/index.rst`: the hidden toctree (sidebar) and the
  **Pages** list.

---

## General Writing Notes

- Keep the same RST formatting style as existing pages (section headings, `.. figure::`, `.. note::`, `:kbd:` roles).
- Use `.. important::` for destructive operation warnings (see `applymodifiers.rst` for example).
- Every new subsection should ideally have a GIF. Add image needs to the **Media Needed** table above.
